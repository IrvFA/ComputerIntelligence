import pandas as pd

http_df = pd.read_csv("data/http.log",
                      sep="\t", header=None,
                      names=['ts', 'uid', 'id_orig_h', 'id_orig_p', 'id_resp_h', 'id_resp_p',
                             'trans_depth', 'method', 'host', 'uri', 'referrer', 'user_agent',
                             'request_body_len', 'response_body_len', 'status_code', 'status_msg',
                             'info_code', 'info_msg', 'filename', 'tags', 'username',
                             'password', 'proxied', 'orig_fuids', 'orig_mime_types', 'resp_fuids',
                             'resp_mime_types', 'sample'])



print(http_df.shape)
print("---------------------\n")
print(http_df.info())
print("---------------------\n")
print(http_df.head())
print("---------------------\n")
print(http_df.dtypes)
print("---------------------\n")
print("Mean Request body Lenght\n", http_df["request_body_len"].mean())
print("---------------------\n")
print("Mean Response body Lenght\n", http_df["response_body_len"].mean())
print("---------------------\n")
print("Description of the Bodies\n", http_df[["response_body_len", "request_body_len"]].describe())
print("---------------------\n")

from datetime import datetime
http_df['ts'] = [
    datetime.fromtimestamp(float(date))
    for date in http_df['ts'].values
]
http_df = http_df.set_index('ts')
http_df.index = pd.to_datetime(http_df.index)
http_df = http_df.sort_index()
print(http_df)
print("---------------------\n")

http_df['Year'] = http_df.index.year
http_df['Month'] = http_df.index.month
print(http_df.sample(5, random_state=0))
print("---------------------\n")
print("Counts of Months: \n", http_df["Month"].value_counts())
print("---------------------\n")
print("Counts of Years: \n", http_df["Year"].value_counts())
print("---------------------\n")
print("Counts of Status Codes: \n", http_df["status_code"].value_counts())




