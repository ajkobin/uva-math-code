import pandas as pd
url = './grad.html'

for i, df in enumerate(pd.read_html(url)):
    df.to_csv('b-myfile_%s.csv' % i)
