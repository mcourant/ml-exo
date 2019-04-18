import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the datas
bankdf = pd.read_csv('bank.csv',sep=';') # check the csv file before to know that 'comma' here is ';'
# Read x lines in CSV
x = 10
print(bankdf.head(x))
# List in array all name of column
print(list(bankdf.columns))# show the features and label 
# Set tuple with dim
print(bankdf.shape) # instances vs features + label (4521, 17) 
sns.set(font_scale=1.5)
countplt=sns.countplot(x='y', data=bankdf, palette ='hls')
plt.show()