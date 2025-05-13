# Technical Assessment Tasks

This repository contains solutions for three technical assessment tasks: a web application, API testing, and SQL data analysis.

## Project Structure

```
.
├── firstTask/          # Web Application: Expense Calculator
├── secondTask/         # API Testing: Product Data Validation
├── thirdTask/          # SQL Queries: Sales Data Analysis
└── README.md
```

## Task 1: Web Application - Expense Calculator

A client-side web application that calculates monthly expense indicators.

### Features
- Add, edit, and delete expenses
- Calculate total monthly expenses
- Calculate average daily expenses (fixed 30-day month)
- Display top 3 largest expenses
- Data persistence using browser localStorage

### Files
- `expense-calculator.html` - Complete web application (HTML/CSS/JavaScript)

### Usage
1. Open `expense-calculator.html` in any modern web browser
2. Add expenses by entering category and amount
3. Click "Calculate" to see results

### Technologies
- HTML5
- CSS3
- Vanilla JavaScript
- LocalStorage API

---

## Task 2: API Testing - Product Data Validation

Python script that validates product data from the FakeStore API to detect errors and anomalies.

### Features
- Verifies API response code (expects 200)
- Validates product attributes:
  - `title` must not be empty
  - `price` must not be negative
  - `rating.rate` must not exceed 5
- Generates detailed defect reports
- Tests with both real API data and synthetic defective data

### Files
- `api_product_validator.py` - Main testing script using requests library
- `api_test_results.json` - Output file with real API test results
- `synthetic_test_results.json` - Output file with synthetic data test results

### Installation
```bash
pip install requests
```

### Usage
```bash
python api_product_validator.py
# or
python api_product_validator_httpx.py
```

### Technologies
- Python 3.x
- requests/httpx library
- JSON for data storage

---

## Task 3: SQL Queries - Sales Data Analysis

SQL queries to analyze sales data for an online store using SQLite.

### Features
1. Calculate total sales volume for March 2024
2. Find the customer who spent the most overall
3. Calculate average order value

### Files
- `sales_analysis.sql` - Complete SQL script with:
  - Table creation
  - Data insertion
  - Analysis queries
  - Bonus queries for additional insights

### Usage
1. Go to [SQLite Online](https://sqliteonline.com/)
2. Copy and paste the SQL script
3. Execute queries to see results

### Expected Results
- Total sales for March 2024: 27,000
- Top customer: Alice (20,000)
- Average order value: 6,000

### Technologies
- SQL (SQLite dialect)
- SQLite Online for testing

---

## Requirements

### Task 1
- Any modern web browser (Chrome, Firefox, Safari, Edge)

### Task 2
- Python 3.7+
- pip (Python package manager)

### Task 3
- SQLite-compatible environment
- Web browser for SQLite Online

---

## Quick Start

1. **Clone the repository**
   ```bash
   git clone [repository-url]
   cd [repository-name]
   ```

2. **Task 1 - Expense Calculator**
   ```bash
   cd firstTask
   open expense-calculator.html  # macOS
   # or
   start expense-calculator.html  # Windows
   ```

3. **Task 2 - API Testing**
   ```bash
   cd secondTask
   pip install requests
   python api_product_validator.py
   ```

4. **Task 3 - SQL Analysis**
   - Copy content from `thirdTask/sales_analysis.sql`
   - Paste into [SQLite Online](https://sqliteonline.com/)
   - Run queries

---

## Testing

### Task 1
- Open in browser and test all CRUD operations
- Verify localStorage persistence by refreshing the page

### Task 2
- Run the script to test against live API
- Review synthetic test results for defect detection

### Task 3
- Execute all queries in SQLite Online
- Verify results match expected values

---

## License

This project is created for educational/assessment purposes.

---

## Author

Anton Pazniak

---

## Acknowledgments

- FakeStore API for providing test data
- SQLite Online for database testing environment