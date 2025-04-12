from fastapi import FastAPI
import pandas as pd
from typing import List, Optional
from fastapi.responses import JSONResponse

app = FastAPI()

# Load the data
df = pd.read_csv("indian_grocery_top1000_weighted.csv")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Indian Grocery API"}

@app.get("/products", response_class=JSONResponse)
def get_products(limit: Optional[int] = 100):
    return df.head(limit).to_dict(orient="records")

@app.get("/search")
def search_products(q: str):
    results = df[df["product_name"].str.contains(q, case=False, na=False)]
    return results.to_dict(orient="records")
