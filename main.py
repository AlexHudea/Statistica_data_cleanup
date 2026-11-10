import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# 1. Load data
df = pd.read_csv("car_data_cleaned.csv")

# 2. Convert numeric columns explicitly
df["price_in_euro"] = pd.to_numeric(df["price_in_euro"], errors="coerce")
df["mileage_in_km"] = pd.to_numeric(df["mileage_in_km"], errors="coerce")
df["year"] = pd.to_numeric(df["year"], errors="coerce")

# Set global visual style
sns.set_theme(style="whitegrid")

# --- Plot 1: Top 20 Car Makes ---
plt.figure(figsize=(10, 6))
top_brands = df["brand"].value_counts().head(20).index
sns.countplot(
    data=df[df["brand"].isin(top_brands)],
    x="brand",
    order=top_brands,
    hue="brand",
    legend=False,
    palette="viridis",
)
plt.title("Top 10 Car Makes", fontsize=14, fontweight="bold")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# --- Plot 2: Cars by Manufacturing Year ---
plt.figure(figsize=(12, 6))
valid_years = df.dropna(subset=["year"]).copy()
valid_years["year"] = valid_years["year"].astype(int)
sns.countplot(
    data=valid_years,
    x="year",
    hue="year",
    legend=False,
    palette="crest",
)
plt.title("Cars by Manufacturing Year", fontsize=14, fontweight="bold")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# --- Plot 3: Price Distribution ---
plt.figure(figsize=(10, 6))
# Exclude the top 1% highest values (outliers) causing the single-spike issue
price_cap = df["price_in_euro"].quantile(0.99)
filtered_price = df[df["price_in_euro"] <= price_cap]["price_in_euro"].dropna()

sns.histplot(filtered_price, bins=40, kde=True, color="teal")
plt.title(
    "Price Distribution (€) [Excl. Top 1% Outliers]",
    fontsize=14,
    fontweight="bold",
)
plt.xlabel("Price in Euro")
plt.ylabel("Count")
plt.tight_layout()
plt.show()


# --- Plot 4: Fuel Type Percentage ---
plt.figure(figsize=(8, 8))
fuel_counts = df["fuel_type"].dropna().value_counts()
plt.pie(
    fuel_counts,
    labels=fuel_counts.index,
    autopct="%1.1f%%",
    startangle=140,
    colors=sns.color_palette("pastel"),
)
plt.title("Fuel Type Percentage", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.show()


# --- Plot 5: Mileage Distribution ---
plt.figure(figsize=(10, 6))
# Exclude the top 1% highest values (outliers) causing the single-spike issue
mileage_cap = df["mileage_in_km"].quantile(0.99)
filtered_mileage = df[df["mileage_in_km"] <= mileage_cap][
    "mileage_in_km"
].dropna()

sns.histplot(filtered_mileage, bins=40, kde=True, color="purple")
plt.title(
    "Mileage Distribution (km) [Excl. Top 1% Outliers]",
    fontsize=14,
    fontweight="bold",
)
plt.xlabel("Mileage in km")
plt.ylabel("Count")
plt.tight_layout()
plt.show()


# --- Plot 6: Cars by Transmission Type ---
plt.figure(figsize=(8, 6))
sns.countplot(
    data=df.dropna(subset=["transmission_type"]),
    x="transmission_type",
    hue="transmission_type",
    legend=False,
    palette="Set2",
)
plt.title("Cars by Transmission Type", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.show()