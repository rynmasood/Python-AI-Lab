import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("OnlineRetail.csv",encoding="ISO-8859-1")


Q1 = data['Quantity'].quantile(0.25)
Q3 = data['Quantity'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = data[(data['Quantity'] < lower_bound) | (data['Quantity'] > upper_bound)]


plt.boxplot(data['Quantity'])
plt.title('Boxplot of Quantity')
plt.show()


data = data[(data['Quantity'] >= lower_bound) & (data['Quantity'] <= upper_bound)]


print("Updated dataset without outliers:")
print(data)

# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# # Load the CSV file
# df = pd.read_csv('OnlineRetail.csv')

# # Select the column of interest (e.g., 'age' or 'bmi')
# column_name = 'Quantity'
# data = df[column_name]

# # Calculate the IQR
# q1 = np.quantile(data, 0.25)
# q3 = np.quantile(data, 0.75)
# iqr = q3 - q1

# # Calculate the upper and lower bounds
# upper_bound = q3 + 1.5 * iqr
# lower_bound = q1 - 1.5 * iqr

# # Identify outliers
# outliers = data[(data < lower_bound) | (data > upper_bound)]

# # Visualize the outliers using a boxplot
# plt.boxplot(data)
# plt.title("Boxplot of " ,column_name)
# plt.show()

# # Remove outliers from the dataset
# df_clean = df[~((df[column_name] < lower_bound) | (df[column_name] > upper_bound))]

# # Print the shape of the original and cleaned datasets
# print("Original dataset shape:", df.shape)
# print("Cleaned dataset shape:", df_clean.shape)