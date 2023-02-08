import pandas as pd
import matplotlib.pyplot as plt

def get_color(smtp_code):
    if smtp_code == 'other':
        return 'gray'
    elif 200 <= smtp_code < 400:
        return 'green'
    elif 400 <= smtp_code < 500:
        return 'orange'
    elif 500 <= smtp_code < 699:
        return 'red'
    else:
        return 'grey'

data = pd.read_csv('smtpdata.csv')
data['timestamp'] = pd.to_datetime(data['timestamp'], unit='s')
data['month'] = data['timestamp'].dt.strftime('%b')

month_order = ['Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug']
data['month'] = pd.Categorical(data['month'], categories=month_order, ordered=True)

grouped_data = data.groupby('month').mean()

smtp_codes = [col.split(',')[0] for col in grouped_data.columns]
smtp_codes = [int(code) if code.isdigit() else 'other' for code in smtp_codes]

grouped_data.plot(kind='bar', color=[get_color(code) for code in smtp_codes])

plt.show()
