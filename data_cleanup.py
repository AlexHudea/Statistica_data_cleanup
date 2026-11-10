import numpy as np
import pandas as pd

# 1. Load dataset
df = pd.read_csv("germany.csv")

# 2. Fix header alignment (corrects the 1-column shift starting at Column G)
df.columns = [
    "index_col",
    "brand",
    "model",
    "color",
    "registration_date",
    "year",
    "price_in_euro",
    "power_kw",
    "power_ps",
    "transmission_type",
    "fuel_type",
    "fuel_consumption_L_100km",
    "fuel_consumption_g_km",
    "mileage_in_km",
    "offer_description",
]

# 3. Drop unwanted columns immediately
cols_to_drop = [
    "index_col",
    "color",
    "registration_date",
    "power_kw",
    "power_ps",
    "fuel_consumption_L_100km",
    "fuel_consumption_g_km",
]
df = df.drop(columns=cols_to_drop, errors="ignore")

# 4. Clean and validate YEAR (coerces text like brand names to NaN)
df["year"] = pd.to_numeric(df["year"], errors="coerce")
df.loc[(df["year"] < 1950) | (df["year"] > 2027), "year"] = np.nan

# 5. Clean and validate MILEAGE
df["mileage_in_km"] = pd.to_numeric(df["mileage_in_km"], errors="coerce")
df.loc[
    (df["mileage_in_km"] < 1000) | (df["mileage_in_km"] > 1_500_000),
    "mileage_in_km",
] = np.nan

# 6. Clean and validate PRICE
df["price_in_euro"] = pd.to_numeric(df["price_in_euro"], errors="coerce")
df.loc[df["price_in_euro"] <= 0, "price_in_euro"] = np.nan

# 7. Clean and validate TRANSMISSION
valid_transmissions = ["Manual", "Automatic"]
df["transmission_type"] = (
    df["transmission_type"].astype(str).str.strip().str.title()
)
df.loc[
    ~df["transmission_type"].isin(valid_transmissions), "transmission_type"
] = np.nan

# 8. Clean and validate FUEL TYPE
valid_fuels = [
    "Petrol",
    "Diesel",
    "Hybrid",
    "Electric",
    "LPG",
]
df["fuel_type"] = df["fuel_type"].astype(str).str.strip().str.title()
df.loc[~df["fuel_type"].isin(valid_fuels), "fuel_type"] = np.nan

# 9. Clean brand & model strings
df["brand"] = df["brand"].astype(str).str.strip()
df["model"] = df["model"].astype(str).str.strip()

# 10. REMOVE ALL ROWS WITH ANY NULL / INVALID DATA
df = df.dropna().reset_index(drop=True)

# 11. Convert data types to clean formats
df["year"] = df["year"].astype(int)
df["price_in_euro"] = df["price_in_euro"].astype(float)
df["mileage_in_km"] = df["mileage_in_km"].astype(float)

# Save clean CSV
df.to_csv("car_data_cleaned.csv", index=False)
print(f"Rows after cleaning: {len(df)}")