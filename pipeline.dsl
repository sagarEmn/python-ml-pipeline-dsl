LOAD data/fake_data.csv
SHOW head
DESCRIBE
TARGET Salary
TRAIN LinearRegression
EVALUATE r2
PREDICT data/fake_data.csv
