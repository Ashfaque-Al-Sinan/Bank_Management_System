import streamlit as st
import json
import random
import string
from pathlib import Path
import pandas as pd

# Page configuration - MUST be first Streamlit command
st.set_page_config(
    page_title="Bank Management System",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better UI (works in both light and dark mode)
st.markdown("""
    <style>
    /* Main container styling */
    .main {
        padding: 0rem 1rem;
    }
    
    /* Button styling */
    .stButton > button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
        padding: 10px;
        border-radius: 10px;
        border: none;
        transition: all 0.3s;
    }
    .stButton > button:hover {
        background-color: #45a049;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    
    /* Success box - works in both modes */
    .success-box {
        background-color: #d4edda;
        color: #155724;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #28a745;
        margin: 10px 0;
    }
    
    /* Error box */
    .error-box {
        background-color: #f8d7da;
        color: #721c24;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #dc3545;
        margin: 10px 0;
    }
    
    /* Info box */
    .info-box {
        background-color: #d1ecf1;
        color: #0c5460;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #17a2b8;
        margin: 10px 0;
    }
    
    /* Warning box */
    .warning-box {
        background-color: #fff3cd;
        color: #856404;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #ffc107;
        margin: 10px 0;
    }
    
    /* Card styling */
    .card {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        margin: 10px 0;
    }
    
    /* Dark mode adjustments */
    @media (prefers-color-scheme: dark) {
        .success-box {
            background-color: #1e4620;
            color: #d4edda;
        }
        .error-box {
            background-color: #4a1c1c;
            color: #f8d7da;
        }
        .info-box {
            background-color: #1c3a4a;
            color: #d1ecf1;
        }
        .warning-box {
            background-color: #4a3e1c;
            color: #fff3cd;
        }
        .card {
            background-color: #2d2d2d;
            color: white;
        }
    }
    
    /* Header styling */
    h1 {
        text-align: center;
        margin-bottom: 20px;
    }
    
    /* Balance text */
    .balance-text {
        font-size: 24px;
        font-weight: bold;
        color: #28a745;
    }
    
    /* Metric cards */
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin: 10px 0;
    }
    
    /* Divider */
    hr {
        margin: 20px 0;
    }
    </style>
""", unsafe_allow_html=True)

class Bank:
    database = 'data.json'
    data = []
    
    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            data = []
    except Exception as err:
        st.error(f"An exception occurred: {err}")
        data = []
    
    @classmethod
    def __update(cls):
        with open(cls.database, 'w') as fs:
            fs.write(json.dumps(cls.data, indent=2))
    
    @classmethod
    def __account_gen(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        specialchar = random.choices("@#$%&", k=1)
        id = alpha + num + specialchar
        random.shuffle(id)
        return "".join(id)
    
    def CreateAccount(self, name, age, email, pin):
        data = {
            "Name": name,
            "Age": age,
            "Email": email,
            "Pin": pin,
            "Account_no": Bank.__account_gen(),
            "balance": 0
        }
        
        if data['Age'] < 18 or len(str(data['Pin'])) != 4:
            return False, "Age must be 18+ and PIN must be 4 digits", None
        else:
            Bank.data.append(data)
            Bank.__update()
            return True, "Account created successfully!", data
    
    def deposit(self, acc_number, pin, amount):
        userdata = [i for i in Bank.data if str(i['Account_no']) == acc_number and int(i['Pin']) == pin]
        
        if len(userdata) == 0:
            return False, "No account found", None
        else:
            if amount > 10000 or amount < 0:
                return False, "Amount must be between 0 and 10,000", None
            else:
                userdata[0]['balance'] += amount
                Bank.__update()
                return True, f"₹{amount} deposited successfully!", userdata[0]['balance']
    
    def withdraw(self, acc_number, pin, amount):
        userdata = [i for i in Bank.data if str(i['Account_no']) == acc_number and int(i['Pin']) == pin]
        
        if len(userdata) == 0:
            return False, "No account found", None
        else:
            if userdata[0]['balance'] < amount:
                return False, f"Insufficient balance! Your balance is ₹{userdata[0]['balance']}", None
            else:
                userdata[0]['balance'] -= amount
                Bank.__update()
                return True, f"₹{amount} withdrawn successfully!", userdata[0]['balance']
    
    def showdetails(self, acc_number, pin):
        userdata = [i for i in Bank.data if str(i['Account_no']) == acc_number and int(i['Pin']) == pin]
        
        if len(userdata) == 0:
            return False, None
        else:
            return True, userdata[0]
    
    def updateDetails(self, acc_number, pin, new_name, new_email, new_pin):
        userdata = [i for i in Bank.data if str(i['Account_no']) == acc_number and int(i['Pin']) == pin]
        
        if len(userdata) == 0:
            return False, "No account found"
        else:
            if new_name and new_name.strip():
                userdata[0]['Name'] = new_name
            if new_email and new_email.strip():
                userdata[0]['Email'] = new_email
            if new_pin and len(str(new_pin)) == 4:
                userdata[0]['Pin'] = new_pin
            
            Bank.__update()
            return True, "Details updated successfully!"
    
    def Delete(self, acc_number, pin):
        userdata = [i for i in Bank.data if str(i['Account_no']) == acc_number and int(i['Pin']) == pin]
        
        if len(userdata) == 0:
            return False, "No account found"
        else:
            Bank.data.remove(userdata[0])
            Bank.__update()
            return True, "Account deleted successfully!"

# Initialize Bank object
bank = Bank()

# Sidebar navigation
with st.sidebar:
    st.markdown("# 🏦 Bank Management System")
    st.markdown("---")
    
    # Logo/Icon
    st.markdown("### Welcome! 👋")
    
    # Navigation menu
    menu = st.radio(
        "Select an option",
        ["📝 Create Account", "💰 Deposit Money", "💸 Withdraw Money", "📋 Account Details", "✏️ Update Details", "🗑️ Delete Account", "📊 All Accounts"]
    )
    
    st.markdown("---")
    
    # Account stats in sidebar
    if Bank.data:
        total_accounts = len(Bank.data)
        total_balance = sum(user['balance'] for user in Bank.data)
        st.metric("Total Accounts", total_accounts)
        st.metric("Total Balance", f"₹{total_balance:,.2f}")
    
    st.markdown("---")
    st.caption("Developed with ❤️ using Streamlit")

# Main content area
st.markdown("<h1>🏦 Welcome to Our Bank</h1>", unsafe_allow_html=True)
st.markdown("---")

# Create Account Section
if menu == "📝 Create Account":
    st.header("📝 Create New Account")
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.form("create_account_form", clear_on_submit=True):
            name = st.text_input("Full Name", placeholder="Enter your full name")
            age = st.number_input("Age", min_value=1, max_value=120, step=1, value=18)
            email = st.text_input("Email Address", placeholder="example@email.com")
            pin = st.text_input("4-Digit PIN", type="password", max_chars=4, placeholder="****")
            
            submit = st.form_submit_button("Create Account", use_container_width=True)
            
            if submit:
                if not name or not email or not pin:
                    st.markdown('<div class="error-box">❌ Please fill all fields!</div>', unsafe_allow_html=True)
                elif not pin.isdigit() or len(pin) != 4:
                    st.markdown('<div class="error-box">❌ PIN must be 4 digits!</div>', unsafe_allow_html=True)
                else:
                    success, message, account_data = bank.CreateAccount(name, age, email, int(pin))
                    if success:
                        st.markdown(f'<div class="success-box">✅ {message}</div>', unsafe_allow_html=True)
                        st.balloons()
                        with st.expander("View Account Details", expanded=True):
                            col_a, col_b = st.columns(2)
                            with col_a:
                                st.write("**Name:**", account_data['Name'])
                                st.write("**Age:**", account_data['Age'])
                                st.write("**Email:**", account_data['Email'])
                            with col_b:
                                st.write("**Account Number:**", account_data['Account_no'])
                                st.write("**PIN:**", "****")
                                st.write("**Balance:**", f"₹{account_data['balance']}")
                    else:
                        st.markdown(f'<div class="error-box">❌ {message}</div>', unsafe_allow_html=True)

# Deposit Section
elif menu == "💰 Deposit Money":
    st.header("💰 Deposit Money")
    
    with st.form("deposit_form"):
        col1, col2 = st.columns(2)
        with col1:
            acc_number = st.text_input("Account Number")
            pin = st.text_input("PIN", type="password", max_chars=4)
        with col2:
            amount = st.number_input("Amount to Deposit", min_value=1, max_value=10000, step=100, value=100)
        
        submit = st.form_submit_button("Deposit", use_container_width=True)
        
        if submit:
            if not acc_number or not pin:
                st.markdown('<div class="error-box">❌ Please enter account number and PIN!</div>', unsafe_allow_html=True)
            elif not pin.isdigit():
                st.markdown('<div class="error-box">❌ PIN must be digits!</div>', unsafe_allow_html=True)
            else:
                success, message, new_balance = bank.deposit(acc_number, pin, amount)
                if success:
                    st.markdown(f'<div class="success-box">✅ {message}</div>', unsafe_allow_html=True)
                    st.markdown(f'<div class="info-box">💰 New Balance: ₹{new_balance}</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="error-box">❌ {message}</div>', unsafe_allow_html=True)

# Withdraw Section
elif menu == "💸 Withdraw Money":
    st.header("💸 Withdraw Money")
    
    with st.form("withdraw_form"):
        col1, col2 = st.columns(2)
        with col1:
            acc_number = st.text_input("Account Number")
            pin = st.text_input("PIN", type="password", max_chars=4)
        with col2:
            amount = st.number_input("Amount to Withdraw", min_value=1, step=100, value=100)
        
        submit = st.form_submit_button("Withdraw", use_container_width=True)
        
        if submit:
            if not acc_number or not pin:
                st.markdown('<div class="error-box">❌ Please enter account number and PIN!</div>', unsafe_allow_html=True)
            elif not pin.isdigit():
                st.markdown('<div class="error-box">❌ PIN must be digits!</div>', unsafe_allow_html=True)
            else:
                success, message, new_balance = bank.withdraw(acc_number, pin, amount)
                if success:
                    st.markdown(f'<div class="success-box">✅ {message}</div>', unsafe_allow_html=True)
                    st.markdown(f'<div class="info-box">💰 Remaining Balance: ₹{new_balance}</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="error-box">❌ {message}</div>', unsafe_allow_html=True)

# Account Details Section
elif menu == "📋 Account Details":
    st.header("📋 Account Details")
    
    with st.form("details_form"):
        col1, col2 = st.columns(2)
        with col1:
            acc_number = st.text_input("Account Number")
            pin = st.text_input("PIN", type="password", max_chars=4)
        
        submit = st.form_submit_button("Show Details", use_container_width=True)
        
        if submit:
            if not acc_number or not pin:
                st.markdown('<div class="error-box">❌ Please enter account number and PIN!</div>', unsafe_allow_html=True)
            elif not pin.isdigit():
                st.markdown('<div class="error-box">❌ PIN must be digits!</div>', unsafe_allow_html=True)
            else:
                success, user_data = bank.showdetails(acc_number, int(pin))
                if success:
                    st.markdown('<div class="success-box">✅ Account Details</div>', unsafe_allow_html=True)
                    
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Name", user_data['Name'])
                        st.metric("Age", user_data['Age'])
                    with col2:
                        st.metric("Email", user_data['Email'])
                        st.metric("Account Number", user_data['Account_no'])
                    with col3:
                        st.metric("Balance", f"₹{user_data['balance']}")
                        st.metric("PIN", "****")
                else:
                    st.markdown('<div class="error-box">❌ No account found! Please check your credentials.</div>', unsafe_allow_html=True)

# Update Details Section
elif menu == "✏️ Update Details":
    st.header("✏️ Update Account Details")
    
    with st.form("update_form"):
        st.info("💡 Leave fields empty if you don't want to change them")
        
        acc_number = st.text_input("Account Number")
        pin = st.text_input("Current PIN", type="password", max_chars=4)
        
        st.markdown("---")
        st.subheader("Update Information")
        
        new_name = st.text_input("New Name (Optional)", placeholder="Leave empty to keep current")
        new_email = st.text_input("New Email (Optional)", placeholder="Leave empty to keep current")
        new_pin = st.text_input("New PIN (Optional)", type="password", max_chars=4, placeholder="Leave empty to keep current")
        
        submit = st.form_submit_button("Update Details", use_container_width=True)
        
        if submit:
            if not acc_number or not pin:
                st.markdown('<div class="error-box">❌ Please enter account number and current PIN!</div>', unsafe_allow_html=True)
            else:
                new_pin_int = int(new_pin) if new_pin and new_pin.isdigit() else None
                success, message = bank.updateDetails(acc_number, int(pin), new_name, new_email, new_pin_int)
                if success:
                    st.markdown(f'<div class="success-box">✅ {message}</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="error-box">❌ {message}</div>', unsafe_allow_html=True)

# Delete Account Section
elif menu == "🗑️ Delete Account":
    st.header("🗑️ Delete Account")
    st.markdown('<div class="warning-box">⚠️ This action is irreversible! All your data will be permanently deleted.</div>', unsafe_allow_html=True)
    
    with st.form("delete_form"):
        acc_number = st.text_input("Account Number")
        pin = st.text_input("PIN", type="password", max_chars=4)
        
        confirm = st.checkbox("✅ I understand that this action cannot be undone")
        
        submit = st.form_submit_button("Delete Account", use_container_width=True)
        
        if submit:
            if not acc_number or not pin:
                st.markdown('<div class="error-box">❌ Please enter account number and PIN!</div>', unsafe_allow_html=True)
            elif not confirm:
                st.markdown('<div class="error-box">❌ Please confirm account deletion!</div>', unsafe_allow_html=True)
            else:
                success, message = bank.Delete(acc_number, int(pin))
                if success:
                    st.markdown(f'<div class="success-box">✅ {message}</div>', unsafe_allow_html=True)
                    st.balloons()
                else:
                    st.markdown(f'<div class="error-box">❌ {message}</div>', unsafe_allow_html=True)

# All Accounts Section (Admin View)
elif menu == "📊 All Accounts":
    st.header("📊 All Bank Accounts")
    
    if Bank.data:
        # Convert to DataFrame for better display
        df = pd.DataFrame(Bank.data)
        df['PIN'] = "****"  # Hide PIN
        df = df[['Name', 'Age', 'Email', 'Account_no', 'balance', 'PIN']]
        df.columns = ['Name', 'Age', 'Email', 'Account Number', 'Balance', 'PIN']
        
        # Format balance
        df['Balance'] = df['Balance'].apply(lambda x: f"₹{x:,.2f}")
        
        st.dataframe(df, use_container_width=True, height=400)
        
        # Summary statistics
        st.markdown("---")
        st.subheader("📊 Summary Statistics")
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Accounts", len(Bank.data))
        with col2:
            total_balance = sum(user['balance'] for user in Bank.data)
            st.metric("Total Balance", f"₹{total_balance:,.2f}")
        with col3:
            avg_balance = total_balance / len(Bank.data) if Bank.data else 0
            st.metric("Average Balance", f"₹{avg_balance:,.2f}")
        with col4:
            max_balance = max(user['balance'] for user in Bank.data) if Bank.data else 0
            st.metric("Highest Balance", f"₹{max_balance:,.2f}")
        
        # Bar chart for balances
        st.markdown("---")
        st.subheader("💰 Account Balances Chart")
        chart_data = pd.DataFrame({
            'Account Holder': [user['Name'] for user in Bank.data],
            'Balance': [user['balance'] for user in Bank.data]
        })
        st.bar_chart(chart_data.set_index('Account Holder'))
        
    else:
        st.markdown('<div class="info-box">📭 No accounts found in the system! Create your first account using the "Create Account" option.</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>© 2024 Bank Management System | Secure & Reliable Banking Solution</p>", unsafe_allow_html=True)