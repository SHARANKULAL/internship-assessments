import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "Size_sqft": [500, 800, 1000, 1200, 1500],
    "Price":     [1000000, 1600000, 2000000, 2400000, 3000000]
}

df = pd.DataFrame(data)

X = df[["Size_sqft"]]
y = df["Price"]

model = LinearRegression()
model.fit(X, y)

predicted_prices = model.predict(X)

print("Predicted Prices:")
for size, price in zip(df["Size_sqft"], predicted_prices):
    print(f"House size: {size} sqft -> Predicted Price: {round(price, 2)}")

new_house_size = [[1100]]
predicted_price = model.predict(new_house_size)

print("\nPrediction for new house:")
print(f"House size: 1100 sqft -> Estimated Price: {round(predicted_price[0], 2)}")
