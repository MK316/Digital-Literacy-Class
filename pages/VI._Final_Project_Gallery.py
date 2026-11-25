
def display_peer_evaluation():
    st.markdown("### ⛄ Peer Evaluation")

    st.write("""
    Peer review summaries of each group's
    application and its classroom use are
    presented below.
    """)

    # ----------------------------------------------
    # Load Feedback
    # ----------------------------------------------
    try:
        df = load_feedback_data()

    except Exception as e:
        st.error(
            f"Unable to load peer evaluation data: {e}"
        )
        return

    if "Group" not in df.columns:
        st.error(
            "The feedback dataset does not contain "
            "a 'Group' column."
        )
        return

    group_list = df["Group"].dropna().unique()

    if len(group_list) == 0:
        st.warning(
            "No group feedback is available."
        )
        return

    selected_group = st.selectbox(
        "🔍 Select a group to view feedback:",
        group_list
    )

    group_df = df[
        df["Group"] == selected_group
    ]

    st.markdown(
        f"## 🧾 Feedback Summary for {selected_group}"
    )

    # ----------------------------------------------
    # SWOT Image
    # ----------------------------------------------
    if selected_group in SWOT_IMAGE_URLS:

        st.image(
            SWOT_IMAGE_URLS[selected_group],
            caption=f"SWOT Analysis: {selected_group}",
            use_container_width=True
        )

    # ----------------------------------------------
    # Quantitative Ratings
    # ----------------------------------------------
    st.markdown(
        "### 📊 Quantitative Ratings (1–10 Scale)"
    )

    rating_columns = [
        f"Q{i:02d}"
        for i in range(1, 8)
    ]

    missing_columns = [
        col for col in rating_columns
        if col not in df.columns
    ]

    if missing_columns:

        st.warning(
            "Missing rating columns: "
            + ", ".join(missing_columns)
        )

    else:

        # Convert ratings to numeric
        for col in rating_columns:

            df[col] = pd.to_numeric(
                df[col],
                errors="coerce"
            )

        group_df = df[
            df["Group"] == selected_group
        ]

        group_means = group_df[
            rating_columns
        ].mean()

        overall_means = df[
            rating_columns
        ].mean()

        labels = [
            QUESTION_LABELS[q]
            for q in rating_columns
        ]

        x = np.arange(len(labels))
        width = 0.35

        fig, ax = plt.subplots(
            figsize=(9, 4.5)
        )

        bars1 = ax.bar(
            x - width / 2,
            group_means.values,
            width,
            label=selected_group,
            color="skyblue"
        )

        bars2 = ax.bar(
            x + width / 2,
            overall_means.values,
            width,
            label="All Groups (Average)",
            color="yellow"
        )

        # Group value labels
        for bar in bars1:

            height = bar.get_height()

            if np.isfinite(height):

                ax.text(
                    bar.get_x()
                    + bar.get_width() / 2,
                    height + 0.1,
                    f"{height:.1f}",
                    ha="center",
                    va="bottom",
                    fontsize=8
                )

        # Overall value labels
        for bar in bars2:

            height = bar.get_height()

            if np.isfinite(height):

                ax.text(
                    bar.get_x()
                    + bar.get_width() / 2,
                    height + 0.1,
                    f"{height:.1f}",
                    ha="center",
                    va="bottom",
                    fontsize=8,
                    color="gray"
                )

        ax.set_ylabel("Average Rating")

        ax.set_title(
            "Average Ratings: Group vs Overall"
        )

        ax.set_xticks(x)

        ax.set_xticklabels(
            labels,
            rotation=45,
            ha="right"
        )

        ax.set_ylim(0, 10.5)

        ax.legend()

        fig.tight_layout()

        st.pyplot(fig)
        plt.close(fig)
