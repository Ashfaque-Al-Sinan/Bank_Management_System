# 🏦 Bank Management System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![JSON](https://img.shields.io/badge/Storage-JSON-yellow?style=for-the-badge&logo=json&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**A full-featured, modern bank management system built with Python and Streamlit.**  
Manage accounts, deposits, withdrawals, and more — all through a clean, responsive web UI.

[Features](#-features) • [Demo](#-demo) • [Installation](#-installation) • [Usage](#-usage) • [Project Structure](#-project-structure)

</div>

---

## 📸 Demo

![Bank Management System Screenshot](screenshot.png)

> Dark-mode friendly UI with sidebar navigation and live account statistics.

---

## ✨ Features

| Feature | Description |
|---|---|
| 📝 **Create Account** | Register with name, age, email, and a 4-digit PIN |
| 💰 **Deposit Money** | Add funds (up to ₹10,000 per transaction) |
| 💸 **Withdraw Money** | Withdraw with automatic balance validation |
| 📋 **Account Details** | View full account info securely |
| ✏️ **Update Details** | Change name, email, or PIN anytime |
| 🗑️ **Delete Account** | Permanently remove an account with confirmation |
| 📊 **All Accounts** | Admin dashboard with stats and balance charts |

### 🔐 Security
- PIN-protected access for every operation
- PINs masked in all views (displayed as `****`)
- Age verification (18+ required to open an account)
- Deletion requires explicit checkbox confirmation

### 🎨 UI Highlights
- Fully responsive layout using Streamlit columns
- Light & dark mode support via CSS media queries
- Live sidebar metrics (total accounts & total balance)
- Interactive bar chart for account balance visualization
- Color-coded feedback boxes (success / error / info / warning)

---

## 🛠️ Tech Stack

- **Frontend & Backend:** [Streamlit](https://streamlit.io/)
- **Language:** Python 3.8+
- **Data Storage:** JSON flat-file (`data.json`)
- **Libraries:** `pandas`, `pathlib`, `random`, `string`, `json`

---

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/bank-management-system.git
cd bank-management-system
```

### 2. Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install streamlit pandas
```

### 4. Run the app
```bash
streamlit run app.py
```

The app will open automatically at `http://localhost:8501`.

---

## 🚀 Usage

### Creating an Account
1. Select **📝 Create Account** from the sidebar
2. Fill in your full name, age, email, and a 4-digit PIN
3. Click **Create Account** — your unique account number will be displayed

### Depositing / Withdrawing
1. Navigate to **💰 Deposit Money** or **💸 Withdraw Money**
2. Enter your account number and PIN
3. Enter the amount and submit

> ⚠️ Maximum deposit per transaction: ₹10,000

### Viewing Account Details
Go to **📋 Account Details**, enter your credentials, and view your profile and current balance.

### Admin View
The **📊 All Accounts** section provides a full overview of all accounts, summary statistics, and a balance distribution chart.

---

## 📁 Project Structure

```
bank-management-system/
│
├── app.py           # Main Streamlit application
├── data.json        # Auto-generated account database (created on first run)
└── README.md        # Project documentation
```

---

## ⚙️ Configuration & Constraints

| Rule | Value |
|---|---|
| Minimum age | 18 years |
| PIN length | Exactly 4 digits |
| Max deposit per transaction | ₹10,000 |
| Minimum deposit | ₹1 |
| Storage format | JSON (local file) |

---

## 🔮 Future Improvements

- [ ] Transaction history / statement generation
- [ ] Fund transfer between accounts
- [ ] Admin login with role-based access
- [ ] Password hashing (bcrypt) for PIN security
- [ ] Database backend (SQLite / PostgreSQL)
- [ ] Export account data to CSV / PDF
- [ ] Email notifications for transactions

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

Developed with ❤️ using [Streamlit](https://streamlit.io/)  
© 2024 Bank Management System | Secure & Reliable Banking Solution

</div>
