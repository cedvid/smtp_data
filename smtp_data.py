import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('smtpdata.csv')
data['timestamp'] = pd.to_datetime(data['timestamp'], unit='s')
data['month'] = data['timestamp'].dt.strftime('%b')
month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
data['month'] = pd.Categorical(data['month'], categories=month_order, ordered=True)
grouped_data = data.groupby('month').mean()
grouped_data.plot(kind='bar')
plt.show()
