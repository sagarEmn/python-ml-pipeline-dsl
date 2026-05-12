import csv
import random

# Define column headers
headers = ['Age', 'Salary', 'Department']

# Generate 50 rows of fake data
data = []
for _ in range(50):
    age = random.randint(22, 60)
    
    # Make salary slightly dependent on age for bivariate correlation
    salary = age * 1000 + random.randint(-5000, 5000)
    department = random.choice(['HR', 'IT', 'Sales', 'Marketing'])
    
    data.append([age, salary, department])
    
# Write to CSV
filename = 'data/fake_data.csv'
with open(filename, mode='w', newline='') as file: 
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(data)

print(f"Successfully created {filename}")