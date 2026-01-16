import pandas as pd
import requests
import json
import sys


# loading test dataset
df_test = pd.read_csv('data/raw/test.csv')


#df_pred = df_test.sample(3)
list_aux = sys.argv[1:]
first_client = int(list_aux[0])
num_clients = int(list_aux[1])


df_pred = df_test.loc[df_test['id'] >= first_client, :].head(num_clients)


data = json.dumps( df_pred.to_dict( orient='records') )


# API Call
#url = 'http://0.0.0.0:5000/predict'
url = 'https://healthinsurance-app.onrender.com/predict'
header = {'Content-type': 'application/json'}

r = requests.post(url, data=data, headers=header )
print( 'Status Code {}'.format( r.status_code) )


d1 = pd.DataFrame( r.json(), columns=r.json()[0].keys() )

d1 = d1.sort_values( 'score', ascending=False ).reset_index()
d1 = d1.loc[:,['id', 'score']]

print(d1)



#for i in range( len(d2) ):
#    print('Store Number {} will sell R${:,.2f} in the next 6 weeks'.format(
#            d2.loc[i, 'store'],
#            d2.loc[i, 'prediction'] ) )
