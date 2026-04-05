import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle #joblib

# Sample dataset (you can replace with real CSV)
data = {
    "cylinders": [4, 4, 8, 4, 4, 8, 4, 4, 8, 8],
    "displacement": [307, 308, 310, 350, 450, 500, 550, 520, 200, 290],
    "horsepower": [75, 100, 150, 180, 220, 250, 280, 300, 320, 340],
    "weight": [900, 1100, 1300, 1500, 1800, 1200, 2000, 3000, 2500, 1200],
    "acceleration": [12, 11.9, 11.5, 10.9, 12.8, 12, 13.8, 12.7, 13, 12.9],
    "origin": [1, 1, 1, 1, 2, 2, 4, 3, 3, 2],
    "mpg": [35, 30, 25, 22, 18, 20, 25,28, 30, 50]
}

data = pd.DataFrame(data)

X = data[["cylinders","displacement", "horsepower", "weight", "acceleration", "origin"]]
y = data["mpg"]

model = LinearRegression()
model.fit(X, y)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained successfully!")