# https://www.geeksforgeeks.org/use-pandas-to-calculate-stats-from-an-imported-csv-file/

# Import Pandas library
import pandas as pd

# Read the CSV file
df=pd.read_csv('student_data2.csv')

# Calculate and print mean value
mean_value=df['fees'].mean()
print('Mean Value: '+str(mean_value))

# Calculate and print median value
median_value=df['fees'].median()
print('Median Value: '+str(median_value))

# Calculate and print mode value
# mode_value=df['fees'].mode()
# print('Mode Value: '+str(mode_value))

# Calculate and print min value
min_value=df['fees'].min()
print('Minimum Value: '+str(min_value))

# Calculate and print max value
max_value=df['fees'].max()
print('Maximum Value: '+str(max_value))

# Calculate and print sum value
sum_value = df['fees'].sum()
print('Sum Value: '+str(sum_value))

# Calculate and print count value
count_value=df['fees'].count()
print('Count Value: '+str(count_value))

# Calculate and print standard deviation value
std_value=df['fees'].std()
print('Standard Deviation Value: '+str(std_value))

# Calculate and print variance value
var_value=df['fees'].var()
print('Variance Value: '+str(var_value))
