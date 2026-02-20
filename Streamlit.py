import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Supply Chain Management Dashboard",
    layout="wide"
)

# -----------------------------
# LOAD DATA
# -----------------------------
@st.cache_data
def load_data():
    return pd.read_csv("supply_chain_data.csv")

df = load_data()

# -----------------------------
# TITLE
# -----------------------------
st.title("Supply Chain Management Dashboard")
st.markdown("**End-to-End Supply Chain Analysis & Demand Insights**")

# -----------------------------
# KPI SECTION
# -----------------------------
st.subheader(" Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Revenue",
    f"₹ {df['Revenue generated'].sum():,.0f}"
)

col2.metric(
    "Total Products Sold",
    f"{df['Number of products sold'].sum():,}"
)

col3.metric(
    "Avg Lead Time",
    f"{df['Lead times'].mean():.2f} days"
)

col4.metric(
    "Avg Shipping Cost",
    f"₹ {df['Shipping costs'].mean():.2f}"
)

# -----------------------------
# FILTERS
# -----------------------------
st.sidebar.header("🔍 Filters")

product_filter = st.sidebar.multiselect(
    "Select Product Type",
    df["Product type"].unique(),
    default=df["Product type"].unique()
)

location_filter = st.sidebar.multiselect(
    "Select Location",
    df["Location"].unique(),
    default=df["Location"].unique()
)

filtered_df = df[
    (df["Product type"].isin(product_filter)) &
    (df["Location"].isin(location_filter))
]

# -----------------------------
# ROW 1: REVENUE & SALES
# -----------------------------
st.subheader(" Revenue & Sales Analysis")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Revenue by Product Type**")
    fig, ax = plt.subplots()
    sns.barplot(
        x="Product type",
        y="Revenue generated",
        palette='Set2',
        saturation=1,
        data=filtered_df,
        ax=ax
    )
    plt.xticks(rotation=45)
    st.pyplot(fig)

with col2:
    st.markdown("**Sales by Product Type**")
    fig, ax = plt.subplots()
    sns.barplot(
        x="Product type",
        y="Number of products sold",
        data=filtered_df,
        ax=ax
    )
    plt.xticks(rotation=45)
    st.pyplot(fig)

# -----------------------------
# ROW 2: INVENTORY & DEMAND
# -----------------------------
st.subheader(" Inventory & Demand Insights")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Stock Level vs Sales**")
    fig, ax = plt.subplots()
    sns.scatterplot(
        x="Stock levels",
        y="Number of products sold",
        data=filtered_df,
        ax=ax
    )
    st.pyplot(fig)

with col2:
    st.markdown("**Production Volume vs Order Quantity**")
    fig, ax = plt.subplots()
    sns.scatterplot(
        x="Production volumes",
        y="Order quantities",
        data=filtered_df,
        ax=ax
    )
    st.pyplot(fig)

# -----------------------------
# ROW 3: SUPPLIER & COST
# -----------------------------
st.subheader(" Supplier & Cost Analysis")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Manufacturing Cost by Supplier**")
    fig, ax = plt.subplots()
    sns.barplot(
        x="Supplier name",
        y="Manufacturing costs",
        data=filtered_df,
        ax=ax
    )
    plt.xticks(rotation=45)
    st.pyplot(fig)

with col2:
    st.markdown("**Price vs Manufacturing Cost**")
    fig, ax = plt.subplots()
    sns.scatterplot(
        x="Price",
        y="Manufacturing costs",
        hue="Product type",
        data=filtered_df,
        ax=ax
    )
    st.pyplot(fig)

# -----------------------------
# ROW 4: LOGISTICS
# -----------------------------
st.subheader(" Logistics & Shipping")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Shipping Cost by Carrier**")
    fig, ax = plt.subplots()
    sns.boxplot(
        x="Shipping carriers",
        y="Shipping costs",
        palette="deep",
        data=filtered_df,
        ax=ax
    )
    st.pyplot(fig)

with col2:
    st.markdown("**Average Lead Time by Product Type**")
    fig, ax = plt.subplots()
    sns.barplot(
        x="Product type",
        y="Lead times",
        data=filtered_df,
        ax=ax
    )
    plt.xticks(rotation=45)
    st.pyplot(fig)

# -----------------------------
# ROW 5: QUALITY & RISK
# -----------------------------
st.subheader(" Quality & Risk Analysis")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Defect Rate by Product Type**")
    fig, ax = plt.subplots()
    sns.barplot(
        x="Product type",
        y="Defect rates",
        data=filtered_df,
        ax=ax
    )
    plt.xticks(rotation=45)
    st.pyplot(fig)

with col2:
    st.markdown("**Inspection Results Distribution**")
    fig, ax = plt.subplots()
    filtered_df["Inspection results"].value_counts().plot(
        kind="pie",
        autopct="%1.1f%%",
        ax=ax
    )
    ax.set_ylabel("")
    st.pyplot(fig)

