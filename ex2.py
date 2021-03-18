# Encoding: UTF-8

import pandas as pd
import matplotlib.pyplot as plt

from datetime import datetime


http_df = pd.read_csv('http.log', sep='\t', header=None, names=['ts', 'uid', 'id_orig_h', 'id_orig_p', 'id_resp_h', 'id_resp_p',
'trans_depth', 'method', 'host', 'uri', 'referrer', 'user_agent',
'request_body_len', 'response_body_len', 'status_code', 'status_msg',
'info_code', 'info_msg', 'filename', 'tags', 'username',
'password', 'proxied', 'orig_fuids', 'orig_mime_types', 'resp_fuids',
'resp_mime_types', 'sample'])

print('head\n', http_df.head())
print('shape\n', http_df.shape)
print('ts cols', http_df['ts'])


min_numeric_date = min(http_df['ts'])
max_numeric_date = max(http_df['ts'])

min_date = datetime.fromtimestamp(float(min_numeric_date))
max_date = datetime.fromtimestamp(float(max_numeric_date))
print('---')
print('min date and max date i guess')
print(min_date)
print(max_date)

# change date datatype
http_df['ts'] = [
    datetime.fromtimestamp(float(date))
    for date in http_df['ts'].values
]
print('---')
print(http_df.head())

# resample dataset so it is indexed by timestamp
http_df = http_df.set_index('ts')
http_df.index = pd.to_datetime(http_df.index)
http_df = http_df.sort_index()
print('---')
print(http_df.head())


print('---')
print(http_df['id_resp_p'].unique())

print('---')
print(http_df['method'].unique())

filtered_http_df = http_df.loc[(http_df['id_resp_p'] != 80) & (http_df['id_resp_p'] != 8080)]
print('---')
print(filtered_http_df['id_resp_p'].unique())

entry_values = []
# print entries of Q3 2011 using filtered data
print('---')
# 2011 (partial)
Q3_2011_entries = filtered_http_df['2011-07-01':'2011-09-30']
Q3_2011_row_count = int(Q3_2011_entries.count().iloc[0])
print(Q3_2011_row_count)
entry_values.append(Q3_2011_row_count)


Q4_2011_entries = filtered_http_df['2011-10-01':'2011-12-31']
Q4_2011_row_count = int(Q4_2011_entries.count().iloc[0])
print(Q4_2011_row_count)
entry_values.append(Q4_2011_row_count)


# 2012
Q1_2012_entries = filtered_http_df['2012-01-01':'2012-03-31']
Q1_2012_row_count = int(Q1_2012_entries.count().iloc[0])
print(Q1_2012_row_count)
entry_values.append(Q1_2012_row_count)


Q2_2012_entries = filtered_http_df['2012-04-01':'2012-06-30']
Q2_2012_row_count = int(Q2_2012_entries.count().iloc[0])
print(Q2_2012_row_count)
entry_values.append(Q2_2012_row_count)


Q3_2012_entries = filtered_http_df['2012-07-01':'2012-09-30']
Q3_2012_row_count = int(Q3_2012_entries.count().iloc[0])
print(Q3_2012_row_count)
entry_values.append(Q3_2012_row_count)


Q4_2012_entries = filtered_http_df['2012-10-01':'2012-12-31']
Q4_2012_row_count = int(Q4_2012_entries.count().iloc[0])
print(Q4_2012_row_count)
entry_values.append(Q4_2012_row_count)


# 2013
Q1_2013_entries = filtered_http_df['2013-01-01':'2013-03-31']
Q1_2013_row_count = int(Q1_2013_entries.count().iloc[0])
print(Q1_2013_row_count)
entry_values.append(Q1_2013_row_count)


Q2_2013_entries = filtered_http_df['2013-04-01':'2013-06-30']
Q2_2013_row_count = int(Q2_2013_entries.count().iloc[0])
print(Q2_2013_row_count)
entry_values.append(Q2_2013_row_count)


Q3_2013_entries = filtered_http_df['2013-07-01':'2013-09-30']
Q3_2013_row_count = int(Q3_2013_entries.count().iloc[0])
print(Q3_2013_row_count)
entry_values.append(Q3_2013_row_count)


Q4_2013_entries = filtered_http_df['2013-10-01':'2013-12-31']
Q4_2013_row_count = int(Q4_2013_entries.count().iloc[0])
print(Q4_2013_row_count)
entry_values.append(Q4_2013_row_count)

# 2014
Q1_2014_entries = filtered_http_df['2014-01':'2014-03']
Q1_2014_row_count = int(Q1_2014_entries.count().iloc[0])
print(Q1_2014_row_count)
entry_values.append(Q1_2014_row_count)


Q2_2014_entries = filtered_http_df['2014-04-01':'2014-06-30']
Q2_2014_row_count = int(Q2_2014_entries.count().iloc[0])
print(Q2_2014_row_count)
entry_values.append(Q2_2014_row_count)


Q3_2014_entries = filtered_http_df['2014-07-01':'2014-09-30']
Q3_2014_row_count = int(Q3_2014_entries.count().iloc[0])
print(Q3_2014_row_count)
entry_values.append(Q3_2014_row_count)

x_ticks = ['Q311', 'Q411', 'Q112', 'Q212', 'Q312', 'Q412', 'Q113', 'Q213', 'Q313', 'Q413', 'Q114', 'Q214', 'Q314']

no_standard_port_graph = plt.figure(1)
plt.plot(entry_values)
plt.ylabel('number of entries per quarter')
plt.xticks(range(len(x_ticks)), labels=x_ticks)
no_standard_port_graph.show()





# -----
# Exercise C
print('--- EXERCISE C ---')
print(http_df)


resp_mime_type_blackilst = ['application/x-dosexec', 'application/octet-stream', 'binary', 'application/vnd.ms-cab-compressed', 'application/x-java-applet', 'application/pdf', 'application/zip', 'application/jar', 'application/x-shockwave-flash']
suspicious_traffic_booleans = http_df['resp_mime_types'].isin(resp_mime_type_blackilst)
print()
print('-----------')
print(suspicious_traffic_booleans)
print('-----------*')
print(http_df[suspicious_traffic_booleans])

suspicious_traffic = http_df[suspicious_traffic_booleans]

print(suspicious_traffic.head())
print(suspicious_traffic.dtypes)


entry_values = []
# 2011 (partial)
Q3_2011_entries = suspicious_traffic['2011-07-01':'2011-09-30']
print()
print('**********')
print(Q3_2011_entries)
print('count',Q3_2011_entries.count())
print(type(Q3_2011_entries))

Q3_2011_row_count = int(Q3_2011_entries.count().iloc[0])
print(Q3_2011_row_count)
entry_values.append(Q3_2011_row_count)


Q4_2011_entries = suspicious_traffic['2011-10-01':'2011-12-31']
Q4_2011_row_count = int(Q4_2011_entries.count().iloc[0])
print(Q4_2011_row_count)
entry_values.append(Q4_2011_row_count)


# 2012
Q1_2012_entries = suspicious_traffic['2012-01-01':'2012-03-31']
Q1_2012_row_count = int(Q1_2012_entries.count().iloc[0])
print(Q1_2012_row_count)
entry_values.append(Q1_2012_row_count)


Q2_2012_entries = suspicious_traffic['2012-04-01':'2012-06-30']
Q2_2012_row_count = int(Q2_2012_entries.count().iloc[0])
print(Q2_2012_row_count)
entry_values.append(Q2_2012_row_count)


Q3_2012_entries = suspicious_traffic['2012-07-01':'2012-09-30']
Q3_2012_row_count = int(Q3_2012_entries.count().iloc[0])
print(Q3_2012_row_count)
entry_values.append(Q3_2012_row_count)


Q4_2012_entries = suspicious_traffic['2012-10-01':'2012-12-31']
Q4_2012_row_count = int(Q4_2012_entries.count().iloc[0])
print(Q4_2012_row_count)
entry_values.append(Q4_2012_row_count)


# 2013
Q1_2013_entries = suspicious_traffic['2013-01-01':'2013-03-31']
Q1_2013_row_count = int(Q1_2013_entries.count().iloc[0])
print(Q1_2013_row_count)
entry_values.append(Q1_2013_row_count)


Q2_2013_entries = suspicious_traffic['2013-04-01':'2013-06-30']
Q2_2013_row_count = int(Q2_2013_entries.count().iloc[0])
print(Q2_2013_row_count)
entry_values.append(Q2_2013_row_count)


Q3_2013_entries = suspicious_traffic['2013-07-01':'2013-09-30']
Q3_2013_row_count = int(Q3_2013_entries.count().iloc[0])
print(Q3_2013_row_count)
entry_values.append(Q3_2013_row_count)


Q4_2013_entries = suspicious_traffic['2013-10-01':'2013-12-31']
Q4_2013_row_count = int(Q4_2013_entries.count().iloc[0])
print(Q4_2013_row_count)
entry_values.append(Q4_2013_row_count)

# 2014
Q1_2014_entries = suspicious_traffic['2014-01':'2014-03']
Q1_2014_row_count = int(Q1_2014_entries.count().iloc[0])
print(Q1_2014_row_count)
entry_values.append(Q1_2014_row_count)


Q2_2014_entries = suspicious_traffic['2014-04-01':'2014-06-30']
Q2_2014_row_count = int(Q2_2014_entries.count().iloc[0])
print(Q2_2014_row_count)
entry_values.append(Q2_2014_row_count)


Q3_2014_entries = suspicious_traffic['2014-07-01':'2014-09-30']
Q3_2014_row_count = int(Q3_2014_entries.count().iloc[0])
print(Q3_2014_row_count)
entry_values.append(Q3_2014_row_count)


suspicious_traffic_graph = plt.figure(2)
plt.plot(entry_values)
plt.ylabel('number of entries per quarter')
plt.xticks(range(len(x_ticks)), labels=x_ticks)
suspicious_traffic_graph.show()

