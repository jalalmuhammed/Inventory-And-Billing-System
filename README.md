# 📦 Inventory & Billing System (CLI-Based)

### 🔧 Built with Python | Role-Based Access | Real-World Simulation

---

## 📌 Project Overview

This is a CLI-based **Retail Inventory & Billing Management Software** that simulates a full-fledged billing system. It includes:

- 🔐 Role-based Authentication (Manager, Cashier, Analyst)
- 📦 Inventory Management (Add/Update/Delete/View products)
- 🧾 Billing System with GST, Discounts & Total Calculation
- 📊 Sales Reporting for Analysts
- 📁 JSON for data persistence
- 📤 CSV export for external analysis
- 📆 Filter sales by date

---

## 👤 User Roles & Access

| Role     | Access                                 |
|----------|----------------------------------------|
| Manager  | Add/update/remove products             |
| Cashier  | Process sales, manage carts, generate bills |
| Analyst  | View insights, filter by date, export reports |
| Admin    | Registers new users and roles          |

---

## 🚀 Features

- **Authentication**: Secure role-based login
- **Inventory**:
  - Add new products
  - Update price or stock
  - Remove discontinued items
  - Show full product list
- **Billing**:
  - Add items to cart
  - Calculate total with GST (18%) and discount (5%)
  - Save sales to JSON
  - Generate readable receipts
- **Reports**:
  - Overview: Revenue, Bill Count, Average Bill
  - Top-Selling Products (using `collections.Counter`)
  - Filter sales by date (e.g., "2025-07-15")
  - Export all sales to `.csv` format

---

## 🗂️ Folder Structure

```
📦project-root
 ┣ 📁data/
 ┃ ┣ authentication.json
 ┃ ┣ inventory.json
 ┃ ┣ sales.json
 ┃ ┗ sales_export.csv
 ┣ authentication.py
 ┣ inventory.py
 ┣ products.py
 ┣ billing.py
 ┣ constants.py
 ┣ analyst_report.py  ← (optional future addition)
 ┗ main.py
```

---

## ⚙️ Technologies Used

- **Python 3**
- `json` (for persistence)
- `csv` (for exporting)
- `datetime` (timestamping)
- `collections.Counter` (product ranking)
- **Modular OOP** (Classes: `Product`, `Inventory`, `Bill`, `SalesReport`)

---

## 🧪 How to Run

1. Clone the repo or download the files
2. Make sure Python 3 is installed
3. Run:

```bash
python main.py
```

4. Register a user, choose a role, and start interacting

---

## 📊 Sample CSV Output

```csv
bill_id,sales_date_time,product_id,product_name,product_quantity,product_price,line_total,bill_total
1001,2025-07-15 12:45:00,103,Comb,3,30,90,246.62
```

---

## ✅ What You Learn From This

- Real-world file-based inventory system
- How to use JSON & CSV in projects
- Managing multiple user roles
- Applying Object-Oriented Programming (OOP)
- Building testable, modular systems
- CLI design thinking for user experience

---

## 🙌 Creator

**Jalal_muhammed**