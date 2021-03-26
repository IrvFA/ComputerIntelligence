import pandas as pd
from datetime import datetime


conn_df = pd.read_csv('conn.log', sep="\t", header=None,
                      names=['ts', 'uid', 'id_orig_h', 'id_orig_p', 'id_resp_h',
                             'id_resp_p', 'proto', 'service', 'duration', 'orig_bytes',
                             'resp_bytes', 'conn_state', 'local_orig', 'missed_bytes',
                             'history', 'orig_pkts', 'orig_ip_bytes', 'resp_pkts',
                             'resp_ip_bytes', 'tunnel_parents', 'threat', 'sample'])

conn_df = conn_df.sample(frac=1/1000)
conn_df['ts'] = [datetime.fromtimestamp(float(date))for date in conn_df['ts'].values]
conn_df.set_index("ts", inplace=True)

query = (conn_df.loc[(conn_df.service == 'http') & (conn_df.id_resp_p != 80)]).groupby(['id_orig_h','id_resp_p'])['id_resp_p'].count()

result = conn_df.groupby('id_orig_h')["id_orig_p"].unique()
print(result)
print(query)
