import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
x = np.array([[25,30,0],[30,40,1],[20,35,0],[35,45,1]])
y = np.array([0,1,0,1])
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)
model = LogisticRegression()
model.fit(x_train, y_train)
accuracy = model.score(x_test, y_test)
print(f"Model Accuracy: {accuracy}")
user_age = float(input("Enter Customer age: "))
user_time_spent = float(input("Enter Time spent on website: "))
user_added_to_cart = int(input("Enter 1 if added to cart, else enter 0: "))
user_data = np.array([[user_age, user_time_spent, user_added_to_cart]])
prediction = model.predict(user_data)
if prediction[0] == 1:
    print("The customer is likely to purchase")
else:
    print("The customer is unlikely to purchase")
