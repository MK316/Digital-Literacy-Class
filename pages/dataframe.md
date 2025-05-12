# Beginner’s Guide to Pandas DataFrames Using GitHub & Colab

## Learning Goals
By the end of this tutorial, you'll be able to:

+ Create a CSV file using GitHub (no need for Notepad or Excel softwares)  
+ Load the file into Google Colab using pandas  
+ Explore basic DataFrame operations  
+ Save updates back to a CSV file

### Step 1: Create a data File on GitHub

1. Go to https://github.com

2. Click ➕ → New repository

3. Name it something like my_data

4. After creating it, click Add file → Create new file

5. Name your file students.csv (comma delimited data file) or students.txt

6. Paste the following:

```
# Example 1. CSV file
Name,Age,Grade
Alice,14,A
Bob,15,B
Cindy,13,A
David,14,C
Ella,15,B
```

```
# Example 2: Reading a TXT File (Tab-Delimited)
Name	Age	Grade
Alice	14	A
Bob	15	B

```

7. Scroll down and click Commit new file  
✅ You now have a CSV file you can access anywhere!

   
### Step 2: Open Google Colab and Read the File

+ Visit https://colab.research.google.com

+ Open a new notebook

+ Run this code (replace the GitHub link if using your own):

```
# Reading a csv file

import pandas as pd

url = 'https://raw.githubusercontent.com/YOUR_USERNAME/my-first-data/main/students.csv'
df = pd.read_csv(url)

df  # display the data
```

```
# Reading a txt file
import pandas as pd

url = "https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/students.txt"
df = pd.read_csv(url, delimiter="\t")  # specify tab as delimiter

df
```

+ Summary: csv file vs. txt file

| Task                    | Try this code                            |
| ----------------------- | ---------------------------------------- |
| Load a file with spaces | `pd.read_csv("file.txt", delimiter=" ")` |
| Load a semicolon file   | `pd.read_csv("file.txt", delimiter=";")` |


### Step 3: Basic Data Access and Manipulation

+ 🔍 View dataframe

```
df.head()     # Show first 5 rows
df.tail()     # Show last 5 rows
```

+ 🔍 Access Columns

```
df["Name"]    # Show the "Name" column
df["Age"].mean()   # Average age

```

+ 🔎 Filter Rows

```
df[df["Grade"] == "A"]    # Students who got an A
```

### 4. 💾 Step 4: Save Modified Data

+ ✍️ Add a new column and save
```
df["Passed"] = df["Grade"].isin(["A", "B"])
df.to_csv("updated_students.csv", index=False)
```

+ 📥 Download to your computer

```
from google.colab import files
files.download("updated_students.csv")
```

### Summary

| Concept          | Function                 |
| ---------------- | ------------------------ |
| Load from GitHub | `pd.read_csv(url)`       |
| Access column    | `df["Age"]`              |
| Filter           | `df[df["Grade"] == "A"]` |
| Save file        | `df.to_csv("file.csv")`  |
| Download         | `files.download()`       |
