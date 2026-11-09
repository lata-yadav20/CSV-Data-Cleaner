# 🐍 CSV Data Cleaner

A Python-based CSV Data Cleaning Tool that automatically detects missing values, identifies duplicate records, cleans datasets, and generates a cleaning summary.

## 🚀 Features

- Read CSV files.
- Detect missing values in each column.
- Identify duplicate rows.
- Remove duplicate records.
- Replace missing values with "Unknown".
- Allow custom input and output filenames.
- Validate CSV file extensions.
- Handle file errors using exception handling.
- Generate a final cleaning report.

## 🛠️ Technologies Used

- Python 3
- CSV Module
- File Handling
- Exception Handling
- Git & GitHub

## 📂 Project Structure

```text
CSV-Data-Cleaner/
│
├── cleaner.py
├── input.csv
├── my_cleaned_data.csv
└── README.md
```

## ⚙️ Installation and Usage

**Step 1: Clone the repository**

```bash
git clone https://github.com/lata-yadav20/CSV-Data-Cleaner.git
```

**Step 2: Open the project folder**

```bash
cd CSV-Data-Cleaner
```

**Step 3: Run the program**

```bash
python3 cleaner.py
```

**Step 4: Enter your filenames**

- Input file: `input.csv`
- Output file: `my_cleaned_data.csv`

## 📊 Sample Cleaning Results

| Metric | Result |
|---|---:|
| Original rows | 7 |
| Missing values detected | 3 |
| Duplicate rows detected | 1 |
| Duplicate rows removed | 1 |
| Missing values replaced | 3 |
| Final cleaned rows | 6 |

## 💡 Example

**Before cleaning:**

| Name | Age | City | Salary |
|---|---|---|---:|
| Lata | 19 | Bengaluru | 30000 |
| Priya | Missing | Mumbai | 50000 |
| Aman | 21 | Missing | 35000 |

**After cleaning:**

| Name | Age | City | Salary |
|---|---|---|---:|
| Lata | 19 | Bengaluru | 30000 |
| Priya | Unknown | Mumbai | 50000 |
| Aman | 21 | Unknown | 35000 |

## 🎯 Project Objective

To simplify basic dataset cleaning and demonstrate practical Python programming concepts through an automated CSV cleaning tool.

## 👩‍💻 Author

Created as a Python portfolio project.

GitHub: https://github.com/lata-yadav20

---

⭐ If you find this project useful, consider giving the repository a star!
