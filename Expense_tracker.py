import streamlit as st
from datetime import datetime, date
import pandas as pd


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Mahesh • Expense Tracker",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');


/* ==========================================================
   GLOBAL
========================================================== */

* {
    font-family: 'Inter', sans-serif;
}

.stApp {

    background:
        radial-gradient(
            circle at 10% 10%,
            rgba(99, 102, 241, 0.15),
            transparent 30%
        ),

        radial-gradient(
            circle at 90% 10%,
            rgba(139, 92, 246, 0.12),
            transparent 30%
        ),

        radial-gradient(
            circle at 50% 100%,
            rgba(59, 130, 246, 0.08),
            transparent 35%
        ),

        #070a13;

    color: #f8fafc;
}


#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    background: transparent !important;
}


.block-container {

    max-width: 1200px;

    padding-top: 35px;
    padding-bottom: 50px;
}


/* ==========================================================
   HERO
========================================================== */

.hero {

    padding: 30px;

    border-radius: 24px;

    background:
        rgba(255, 255, 255, 0.055);

    border:
        1px solid rgba(255, 255, 255, 0.10);

    box-shadow:
        0 25px 70px rgba(0, 0, 0, 0.35),

        inset
        0 1px 0
        rgba(255, 255, 255, 0.06);

    backdrop-filter:
        blur(20px);

    margin-bottom: 25px;
}


.hero-icon {

    width: 58px;
    height: 58px;

    border-radius: 17px;

    display: flex;

    align-items: center;
    justify-content: center;

    background:
        linear-gradient(
            135deg,
            #6366f1,
            #8b5cf6
        );

    font-size: 28px;

    box-shadow:
        0 12px 35px
        rgba(99, 102, 241, 0.35);

    margin-bottom: 16px;
}


.hero-title {

    font-size: 36px;

    font-weight: 800;

    letter-spacing: -1px;

    color: white;
}


.hero-subtitle {

    margin-top: 7px;

    color: #94a3b8;

    font-size: 14px;
}


/* ==========================================================
   SECTION TITLE
========================================================== */

.section-title {

    color: white;

    font-size: 19px;

    font-weight: 700;

    margin-top: 25px;

    margin-bottom: 14px;
}


/* ==========================================================
   STAT CARDS
========================================================== */

.stat-card {

    padding: 21px;

    min-height: 105px;

    border-radius: 18px;

    background:
        rgba(255, 255, 255, 0.045);

    border:
        1px solid rgba(255, 255, 255, 0.09);

    box-shadow:
        0 12px 35px
        rgba(0, 0, 0, 0.18);

    transition:
        all 0.25s ease;
}


.stat-card:hover {

    transform:
        translateY(-4px);

    border-color:
        rgba(129, 140, 248, 0.40);

    box-shadow:
        0 18px 45px
        rgba(0, 0, 0, 0.28);
}


.stat-label {

    color: #94a3b8;

    font-size: 12px;

    font-weight: 500;
}


.stat-value {

    color: white;

    font-size: 27px;

    font-weight: 800;

    margin-top: 7px;
}


/* ==========================================================
   FORM CARD
========================================================== */

.form-card {

    padding: 25px;

    border-radius: 20px;

    background:
        rgba(255, 255, 255, 0.045);

    border:
        1px solid rgba(255, 255, 255, 0.09);

    box-shadow:
        0 18px 50px
        rgba(0, 0, 0, 0.22);
}


/* ==========================================================
   INPUTS
========================================================== */

.stTextInput input,
.stNumberInput input,
.stTextArea textarea,
.stDateInput input {

    background:
        rgba(255, 255, 255, 0.055) !important;

    color:
        white !important;

    border:
        1px solid
        rgba(255, 255, 255, 0.12) !important;

    border-radius:
        11px !important;
}


.stTextInput input:focus,
.stNumberInput input:focus,
.stTextArea textarea:focus,
.stDateInput input:focus {

    border-color:
        rgba(129, 140, 248, 0.65) !important;

    box-shadow:
        0 0 0 1px
        rgba(129, 140, 248, 0.25) !important;
}


.stSelectbox div[data-baseweb="select"] > div {

    background:
        rgba(255, 255, 255, 0.055) !important;

    color:
        white !important;

    border:
        1px solid
        rgba(255, 255, 255, 0.12) !important;

    border-radius:
        11px !important;
}


.stTextInput label,
.stNumberInput label,
.stTextArea label,
.stSelectbox label,
.stDateInput label {

    color:
        #cbd5e1 !important;

    font-size:
        12px !important;

    font-weight:
        600 !important;
}


/* ==========================================================
   BUTTONS
========================================================== */

.stButton button {

    min-height: 42px;

    border-radius:
        11px !important;

    border:
        1px solid
        rgba(255, 255, 255, 0.10) !important;

    background:
        linear-gradient(
            135deg,
            #6366f1,
            #8b5cf6
        ) !important;

    color:
        white !important;

    font-weight:
        600 !important;

    transition:
        all 0.2s ease !important;
}


.stButton button:hover {

    transform:
        translateY(-2px);

    box-shadow:
        0 10px 28px
        rgba(99, 102, 241, 0.30);
}


/* ==========================================================
   EXPENSE CARD
========================================================== */

.expense-card {

    padding: 19px;

    margin-bottom: 12px;

    border-radius: 18px;

    background:
        rgba(255, 255, 255, 0.045);

    border:
        1px solid
        rgba(255, 255, 255, 0.09);

    box-shadow:
        0 12px 35px
        rgba(0, 0, 0, 0.18);

    transition:
        all 0.2s ease;
}


.expense-card:hover {

    transform:
        translateY(-2px);

    background:
        rgba(255, 255, 255, 0.06);

    border-color:
        rgba(129, 140, 248, 0.30);
}


.expense-title {

    color: white;

    font-size: 15px;

    font-weight: 700;
}


.expense-description {

    color: #94a3b8;

    font-size: 12px;

    margin-top: 5px;
}


.expense-amount {

    color: white;

    font-size: 18px;

    font-weight: 800;

    text-align: right;
}


/* ==========================================================
   CATEGORY BADGES
========================================================== */

.category-badge {

    display: inline-block;

    padding: 5px 10px;

    border-radius: 20px;

    background:
        rgba(99, 102, 241, 0.12);

    color:
        #a5b4fc;

    font-size: 10px;

    font-weight: 700;
}


/* ==========================================================
   EMPTY STATE
========================================================== */

.empty-card {

    padding: 55px 20px;

    border-radius: 20px;

    background:
        rgba(255, 255, 255, 0.045);

    border:
        1px solid
        rgba(255, 255, 255, 0.09);

    text-align: center;

    box-shadow:
        0 18px 50px
        rgba(0, 0, 0, 0.20);
}


.empty-icon {

    width: 60px;
    height: 60px;

    margin:
        0 auto 15px;

    border-radius: 17px;

    background:
        rgba(99, 102, 241, 0.12);

    display: flex;

    align-items: center;

    justify-content: center;

    font-size: 27px;

    color: #a5b4fc;
}


.empty-title {

    color: white;

    font-size: 18px;

    font-weight: 700;
}


.empty-text {

    color: #94a3b8;

    font-size: 13px;

    margin-top: 7px;
}


/* ==========================================================
   DIVIDER
========================================================== */

.divider {

    height: 1px;

    background:
        rgba(255,255,255,0.07);

    margin:
        18px 0;
}


/* ==========================================================
   FOOTER
========================================================== */

.footer {

    text-align: center;

    color: #475569;

    font-size: 11px;

    margin-top: 45px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# SESSION STATE
# ============================================================

if "expenses" not in st.session_state:

    st.session_state.expenses = []


if "editing_id" not in st.session_state:

    st.session_state.editing_id = None


# ============================================================
# FUNCTIONS
# ============================================================

def create_expense(
    title,
    amount,
    category,
    expense_date,
    payment_method,
    description
):

    if not title.strip():

        st.warning("Please enter an expense title.")

        return False


    if amount <= 0:

        st.warning("Amount must be greater than zero.")

        return False


    expense = {

        "id": datetime.now().timestamp(),

        "title": title.strip(),

        "amount": float(amount),

        "category": category,

        "date": expense_date,

        "payment_method": payment_method,

        "description": description.strip(),

        "created_at":
            datetime.now().strftime(
                "%d %b %Y %I:%M %p"
            )
    }


    st.session_state.expenses.append(expense)

    return True


def update_expense(
    expense_id,
    title,
    amount,
    category,
    expense_date,
    payment_method,
    description
):

    for expense in st.session_state.expenses:

        if expense["id"] == expense_id:

            expense["title"] = title.strip()

            expense["amount"] = float(amount)

            expense["category"] = category

            expense["date"] = expense_date

            expense["payment_method"] = payment_method

            expense["description"] = description.strip()

            break


def delete_expense(expense_id):

    st.session_state.expenses = [

        expense

        for expense in st.session_state.expenses

        if expense["id"] != expense_id
    ]


def get_expense(expense_id):

    for expense in st.session_state.expenses:

        if expense["id"] == expense_id:

            return expense

    return None


# ============================================================
# HERO
# ============================================================

st.markdown(
    """
<div class="hero">
<div class="hero-icon">💰</div>
<div class="hero-title">Mahesh Expense Tracker</div>
<div class="hero-subtitle">
Track your spending, understand your habits, and manage your money smarter.
</div>
</div>
""",
    unsafe_allow_html=True
)


# ============================================================
# STATISTICS
# ============================================================

expenses = st.session_state.expenses


total_expense = sum(
    expense["amount"]
    for expense in expenses
)


transaction_count = len(expenses)


average_expense = (
    total_expense / transaction_count
    if transaction_count > 0
    else 0
)


if expenses:

    highest_expense = max(
        expense["amount"]
        for expense in expenses
    )

else:

    highest_expense = 0


c1, c2, c3, c4 = st.columns(4)


with c1:

    st.markdown(
        f"""
<div class="stat-card">
<div class="stat-label">Total Spending</div>
<div class="stat-value">₹{total_expense:,.2f}</div>
</div>
""",
        unsafe_allow_html=True
    )


with c2:

    st.markdown(
        f"""
<div class="stat-card">
<div class="stat-label">Transactions</div>
<div class="stat-value">{transaction_count}</div>
</div>
""",
        unsafe_allow_html=True
    )


with c3:

    st.markdown(
        f"""
<div class="stat-card">
<div class="stat-label">Average Expense</div>
<div class="stat-value">₹{average_expense:,.2f}</div>
</div>
""",
        unsafe_allow_html=True
    )


with c4:

    st.markdown(
        f"""
<div class="stat-card">
<div class="stat-label">Highest Expense</div>
<div class="stat-value">₹{highest_expense:,.2f}</div>
</div>
""",
        unsafe_allow_html=True
    )


# ============================================================
# ADD / EDIT EXPENSE
# ============================================================

st.markdown(
    '<div class="section-title">Add Expense</div>',
    unsafe_allow_html=True
)


editing_expense = None


if st.session_state.editing_id is not None:

    editing_expense = get_expense(
        st.session_state.editing_id
    )


if editing_expense:

    st.info(
        f"Editing: {editing_expense['title']}"
    )


form_col1, form_col2 = st.columns([2, 1])


with form_col1:

    title = st.text_input(
        "Expense Title",
        value=(
            editing_expense["title"]
            if editing_expense
            else ""
        ),
        placeholder="e.g. Groceries"
    )


    description = st.text_area(
        "Description",
        value=(
            editing_expense["description"]
            if editing_expense
            else ""
        ),
        placeholder="Add a short description...",
        height=90
    )


with form_col2:

    amount = st.number_input(
        "Amount (₹)",
        min_value=0.0,
        step=50.0,
        value=(
            float(editing_expense["amount"])
            if editing_expense
            else 0.0
        )
    )


    categories = [
        "Food",
        "Transport",
        "Shopping",
        "Bills",
        "Entertainment",
        "Education",
        "Health",
        "Travel",
        "Other"
    ]


    category_index = 0


    if editing_expense:

        if editing_expense["category"] in categories:

            category_index = categories.index(
                editing_expense["category"]
            )


    category = st.selectbox(
        "Category",
        categories,
        index=category_index
    )


date_col, payment_col = st.columns(2)


with date_col:

    expense_date = st.date_input(
        "Expense Date",
        value=(
            editing_expense["date"]
            if editing_expense
            else date.today()
        )
    )


with payment_col:

    payment_methods = [
        "Cash",
        "UPI",
        "Credit Card",
        "Debit Card",
        "Bank Transfer",
        "Other"
    ]


    payment_index = 0


    if editing_expense:

        if (
            editing_expense["payment_method"]
            in payment_methods
        ):

            payment_index = payment_methods.index(
                editing_expense["payment_method"]
            )


    payment_method = st.selectbox(
        "Payment Method",
        payment_methods,
        index=payment_index
    )


button1, button2, button3 = st.columns(
    [2, 1, 5]
)


with button1:

    if editing_expense:

        save_button = st.button(
            "✓ Save Changes",
            use_container_width=True
        )

    else:

        save_button = st.button(
            "＋ Add Expense",
            use_container_width=True
        )


with button2:

    if editing_expense:

        cancel_button = st.button(
            "Cancel",
            use_container_width=True
        )

    else:

        cancel_button = False


if save_button:

    if editing_expense:

        if title.strip() and amount > 0:

            update_expense(
                editing_expense["id"],
                title,
                amount,
                category,
                expense_date,
                payment_method,
                description
            )

            st.session_state.editing_id = None

            st.success(
                "✓ Expense updated successfully!"
            )

            st.rerun()

    else:

        success = create_expense(
            title,
            amount,
            category,
            expense_date,
            payment_method,
            description
        )

        if success:

            st.success(
                "✓ Expense added successfully!"
            )

            st.rerun()


if cancel_button:

    st.session_state.editing_id = None

    st.rerun()


# ============================================================
# ANALYTICS
# ============================================================

st.markdown(
    '<div class="section-title">Spending Analytics</div>',
    unsafe_allow_html=True
)


if expenses:

    df = pd.DataFrame(expenses)


    chart_col1, chart_col2 = st.columns(2)


    # --------------------------------------------------------
    # CATEGORY CHART
    # --------------------------------------------------------

    with chart_col1:

        category_data = (
            df.groupby("category")["amount"]
            .sum()
            .sort_values(ascending=False)
        )


        st.subheader("Spending by Category")


        st.bar_chart(
            category_data,
            use_container_width=True
        )


    # --------------------------------------------------------
    # MONTHLY CHART
    # --------------------------------------------------------

    with chart_col2:

        df["month"] = pd.to_datetime(
            df["date"]
        ).dt.strftime("%b %Y")


        monthly_data = (
            df.groupby("month")["amount"]
            .sum()
        )


        st.subheader("Monthly Spending")


        st.line_chart(
            monthly_data,
            use_container_width=True
        )


else:

    st.info(
        "Add expenses to see your spending analytics."
    )


# ============================================================
# EXPENSE HISTORY
# ============================================================

st.markdown(
    '<div class="section-title">Expense History</div>',
    unsafe_allow_html=True
)


if expenses:

    # --------------------------------------------------------
    # SEARCH + FILTER
    # --------------------------------------------------------

    filter1, filter2, filter3 = st.columns(
        [2, 1, 1]
    )


    with filter1:

        search = st.text_input(
            "Search",
            placeholder="Search expenses..."
        )


    with filter2:

        filter_categories = [
            "All"
        ] + categories


        selected_category = st.selectbox(
            "Category Filter",
            filter_categories
        )


    with filter3:

        sort_option = st.selectbox(
            "Sort By",
            [
                "Newest",
                "Oldest",
                "Highest Amount",
                "Lowest Amount"
            ]
        )


    # --------------------------------------------------------
    # FILTER DATA
    # --------------------------------------------------------

    filtered_expenses = expenses.copy()


    if search:

        search_lower = search.lower()


        filtered_expenses = [

            expense

            for expense in filtered_expenses

            if (
                search_lower
                in expense["title"].lower()
            )

            or (
                search_lower
                in expense["description"].lower()
            )
        ]


    if selected_category != "All":

        filtered_expenses = [

            expense

            for expense in filtered_expenses

            if (
                expense["category"]
                == selected_category
            )
        ]


    # --------------------------------------------------------
    # SORT
    # --------------------------------------------------------

    if sort_option == "Newest":

        filtered_expenses.sort(
            key=lambda x: x["date"],
            reverse=True
        )


    elif sort_option == "Oldest":

        filtered_expenses.sort(
            key=lambda x: x["date"]
        )


    elif sort_option == "Highest Amount":

        filtered_expenses.sort(
            key=lambda x: x["amount"],
            reverse=True
        )


    elif sort_option == "Lowest Amount":

        filtered_expenses.sort(
            key=lambda x: x["amount"]
        )


    # --------------------------------------------------------
    # DISPLAY
    # --------------------------------------------------------

    if filtered_expenses:

        for expense in filtered_expenses:

            st.markdown(
                f"""
<div class="expense-card">
<div style="display:flex;justify-content:space-between;gap:20px;">
<div style="flex:1;">
<div class="expense-title">
{expense["title"]}
</div>

<div class="expense-description">
{expense["description"] or "No description provided."}
</div>

<div style="margin-top:10px;">
<span class="category-badge">
{expense["category"]}
</span>
</div>
</div>

<div>
<div class="expense-amount">
₹{expense["amount"]:,.2f}
</div>
</div>
</div>

<div class="divider"></div>

<div style="color:#94a3b8;font-size:11px;">
📅 {expense["date"].strftime("%d %b %Y")}
&nbsp;&nbsp; • &nbsp;&nbsp;
💳 {expense["payment_method"]}
</div>
</div>
""",
                unsafe_allow_html=True
            )


            edit_col, delete_col, space = st.columns(
                [1, 1, 8]
            )


            with edit_col:

                if st.button(
                    "✏️ Edit",
                    key=f"edit_{expense['id']}"
                ):

                    st.session_state.editing_id = (
                        expense["id"]
                    )

                    st.rerun()


            with delete_col:

                if st.button(
                    "🗑️ Delete",
                    key=f"delete_{expense['id']}"
                ):

                    delete_expense(
                        expense["id"]
                    )

                    st.success(
                        "Expense deleted."
                    )

                    st.rerun()


    else:

        st.info(
            "No expenses match your search/filter."
        )


else:

    st.markdown(
        """
<div class="empty-card">
<div class="empty-icon">💸</div>
<div class="empty-title">No expenses yet</div>
<div class="empty-text">
Start adding your expenses to track your spending.
</div>
</div>
""",
        unsafe_allow_html=True
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
<div class="footer">
Mahesh Expense Tracker • Built with Python + Streamlit
</div>
""",
    unsafe_allow_html=True
)