import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv('company-sales_data.csv')

# Extract data for toothpaste, shampoo, and facecream
months = df['month_number']
toothpaste = df['toothpaste']
shampoo = df['shampoo']
facecream = df['facecream']

# Plot the line chart
plt.figure(figsize=(10, 6))
plt.plot(months, toothpaste, label='Toothpaste', marker='o')
plt.plot(months, shampoo, label='Shampoo', marker='o')
plt.plot(months, facecream, label='Facecream', marker='o')

plt.xlabel('Month')
plt.ylabel('Units Sold')
plt.title('Monthly Sales of Toothpaste, Shampoo, and Facecream')
plt.xticks(months)
plt.legend()
plt.grid(True)
plt.show()
