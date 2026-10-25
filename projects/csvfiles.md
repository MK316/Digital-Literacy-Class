## How to Save an Excel File as CSV

If your vocabulary data is in an Excel file such as:

```text
vocabulary.xlsx
```

you can convert it to CSV very easily.

### In Microsoft Excel

1. Open the `.xlsx` file.
2. Click **File → Save As**.
3. Choose a folder.
4. In **File Format**, select:

```text
CSV UTF-8 (Comma delimited) (*.csv)
```

5. Click **Save**.

Your file will now look like:

```text
vocabulary.csv
```

### Important: Use UTF-8

Because our data may contain both English and Korean, always choose:

```text
CSV UTF-8
```

Do not choose a regular CSV format if UTF-8 is available.

UTF-8 helps Korean characters display correctly.

### In Python (optional)

You can then read the file with:

```python
import pandas as pd

df = pd.read_csv("vocabulary.csv", encoding="utf-8-sig")
```

`utf-8-sig` is a safe choice for CSV files saved from Excel, especially when Korean text is included.
