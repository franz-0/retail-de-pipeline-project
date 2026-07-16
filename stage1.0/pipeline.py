import requests
import pandas as pd
from sqlalchemy import create_engine

# Define the API endpoint
url = "https://dummyjson.com/products?limit=0" # fetch all products

# send a GET request to the API
response = requests.get(url)

# check if the request was successful
if response.status_code == 200:
    data = response.json()["products"]
    print(f"Successfully fetched {len(data)} products.")
    print("Data Extract was successful.")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
    data = None

if data:
    # convert the data to a pandas DataFrame
    # #df = pd.DataFrame(data['products'])
    df = pd.json_normalize(data)  # flatten the nested JSON structure
else:
    print("No data to display.")

# Clean column names
df["tags"] = df["tags"].apply(", ".join)
df["images"] = df["images"].apply(", ".join)

#Explode into multiple rows
reviews = df.explode("reviews")

# Then flatten: normalize the 'reviews' column and reset index to avoid non-unique index errors
review_details = pd.json_normalize(reviews["reviews"].reset_index(drop=True)).reset_index(drop=True)

# Finally: concat left side (without 'reviews') and the flattened review details,
# ensuring both DataFrames have a unique RangeIndex
reviews = pd.concat(
    [
        reviews.drop(columns="reviews").reset_index(drop=True),
        review_details
    ],
    axis=1
)

# Clean column names
df.columns = (
    df.columns
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
        .str.replace(".", "_")
)

print("Data transformation was successful.")

# Load the data into a MySQL database using SQLAlchemy

engine = create_engine(
    "mysql+pymysql://{your_db_user}:{your_db_password}@localhost:3306/{your_db_name}"
)

# Save the products DataFrame (without reviews column)
df.drop(columns=["reviews"]).to_sql(
    name="TABLE_NAME",
    con=engine,
    if_exists="replace",
    index=False
)

print("Data load was successful.")

print("ETL process completed successfully.")