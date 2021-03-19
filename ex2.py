# Encoding: UTF-8
# Exercise 2 for Home Assignment 1
#   A01374866 - Roberto Tellez Perezyera
#   A01745759 - Irving Fuentes Aguilera
#   A01375925 - Javier Pascal Flores


import pandas as pd
import matplotlib.pyplot as plt

from datetime import datetime


http_df = pd.read_csv('http.log', sep='\t', header=None, names=['ts', 'uid', 'id_orig_h', 'id_orig_p', 'id_resp_h', 'id_resp_p',
'trans_depth', 'method', 'host', 'uri', 'referrer', 'user_agent',
'request_body_len', 'response_body_len', 'status_code', 'status_msg',
'info_code', 'info_msg', 'filename', 'tags', 'username',
'password', 'proxied', 'orig_fuids', 'orig_mime_types', 'resp_fuids',
'resp_mime_types', 'sample'])

print('---- Getting acquainted with the dataset ----')
print('Head:\n', http_df.head())
print('Shape:\n', http_df.shape)
print()



min_numeric_date = min(http_df['ts'])
max_numeric_date = max(http_df['ts'])
min_date = datetime.fromtimestamp(float(min_numeric_date))
max_date = datetime.fromtimestamp(float(max_numeric_date))
print('---')
print('Find the oldest and newest date to see which is the oldest and newest quarters to include in plots:')
print(min_date)
print(max_date)

# change date datatype
http_df['ts'] = [
    datetime.fromtimestamp(float(date))
    for date in http_df['ts'].values
]

# resample dataset so it is indexed by timestamp
http_df = http_df.set_index('ts')
http_df.index = pd.to_datetime(http_df.index)
http_df = http_df.sort_index()


print('---')
print('Display a list of unique port numbers in dataset:')
print(http_df['id_resp_p'].unique())


filtered_http_df = http_df.loc[(http_df['id_resp_p'] != 80) & (http_df['id_resp_p'] != 8080)]
print('---')
print('Same list. Now should NOT include ports 80 or 8080 as we filtered them out')
print(filtered_http_df['id_resp_p'].unique())

entry_values = []
# 2011
Q3_2011_entries = filtered_http_df['2011-07-01':'2011-09-30']
Q3_2011_row_count = int(Q3_2011_entries.count().iloc[0])
entry_values.append(Q3_2011_row_count)


Q4_2011_entries = filtered_http_df['2011-10-01':'2011-12-31']
Q4_2011_row_count = int(Q4_2011_entries.count().iloc[0])
entry_values.append(Q4_2011_row_count)


# 2012
Q1_2012_entries = filtered_http_df['2012-01-01':'2012-03-31']
Q1_2012_row_count = int(Q1_2012_entries.count().iloc[0])
entry_values.append(Q1_2012_row_count)


Q2_2012_entries = filtered_http_df['2012-04-01':'2012-06-30']
Q2_2012_row_count = int(Q2_2012_entries.count().iloc[0])
entry_values.append(Q2_2012_row_count)


Q3_2012_entries = filtered_http_df['2012-07-01':'2012-09-30']
Q3_2012_row_count = int(Q3_2012_entries.count().iloc[0])
print(Q3_2012_row_count)
entry_values.append(Q3_2012_row_count)


Q4_2012_entries = filtered_http_df['2012-10-01':'2012-12-31']
Q4_2012_row_count = int(Q4_2012_entries.count().iloc[0])
entry_values.append(Q4_2012_row_count)


# 2013
Q1_2013_entries = filtered_http_df['2013-01-01':'2013-03-31']
Q1_2013_row_count = int(Q1_2013_entries.count().iloc[0])
entry_values.append(Q1_2013_row_count)


Q2_2013_entries = filtered_http_df['2013-04-01':'2013-06-30']
Q2_2013_row_count = int(Q2_2013_entries.count().iloc[0])
entry_values.append(Q2_2013_row_count)


Q3_2013_entries = filtered_http_df['2013-07-01':'2013-09-30']
Q3_2013_row_count = int(Q3_2013_entries.count().iloc[0])
entry_values.append(Q3_2013_row_count)


Q4_2013_entries = filtered_http_df['2013-10-01':'2013-12-31']
Q4_2013_row_count = int(Q4_2013_entries.count().iloc[0])
entry_values.append(Q4_2013_row_count)

# 2014
Q1_2014_entries = filtered_http_df['2014-01':'2014-03']
Q1_2014_row_count = int(Q1_2014_entries.count().iloc[0])
entry_values.append(Q1_2014_row_count)


Q2_2014_entries = filtered_http_df['2014-04-01':'2014-06-30']
Q2_2014_row_count = int(Q2_2014_entries.count().iloc[0])
entry_values.append(Q2_2014_row_count)


Q3_2014_entries = filtered_http_df['2014-07-01':'2014-09-30']
Q3_2014_row_count = int(Q3_2014_entries.count().iloc[0])
entry_values.append(Q3_2014_row_count)

x_ticks = ['Q311', 'Q411', 'Q112', 'Q212', 'Q312', 'Q412', 'Q113', 'Q213', 'Q313', 'Q413', 'Q114', 'Q214', 'Q314']

no_standard_port_graph = plt.figure(1)
plt.plot(entry_values)
plt.title('HTTP traffic not using standard ports\nOccurrences per quarter')
plt.ylabel('Occurrences per quarter')
plt.xticks(range(len(x_ticks)), labels=x_ticks)
no_standard_port_graph.show()





# -----
# Exercise C
print('\n\n\n--- EXERCISE C ---\n')
print('Original dataframe:')
print(http_df)

# create a blacklist for executable and common exploit types, perform filtering on the dataframe
resp_mime_type_blackilst = ['application/x-dosexec', 'application/octet-stream', 'binary', 'application/vnd.ms-cab-compressed', 'application/x-java-applet', 'application/pdf', 'application/zip', 'application/jar', 'application/x-shockwave-flash']
suspicious_traffic_booleans = http_df['resp_mime_types'].isin(resp_mime_type_blackilst)
suspicious_traffic = http_df[suspicious_traffic_booleans]

print('---')
print('Filtered dataframe sample:')
print(suspicious_traffic.head())


entry_values = []
# 2011 (partial)
Q3_2011_entries = suspicious_traffic['2011-07-01':'2011-09-30']
Q3_2011_row_count = int(Q3_2011_entries.count().iloc[0])
entry_values.append(Q3_2011_row_count)


Q4_2011_entries = suspicious_traffic['2011-10-01':'2011-12-31']
Q4_2011_row_count = int(Q4_2011_entries.count().iloc[0])
entry_values.append(Q4_2011_row_count)


# 2012
Q1_2012_entries = suspicious_traffic['2012-01-01':'2012-03-31']
Q1_2012_row_count = int(Q1_2012_entries.count().iloc[0])
entry_values.append(Q1_2012_row_count)


Q2_2012_entries = suspicious_traffic['2012-04-01':'2012-06-30']
Q2_2012_row_count = int(Q2_2012_entries.count().iloc[0])
entry_values.append(Q2_2012_row_count)


Q3_2012_entries = suspicious_traffic['2012-07-01':'2012-09-30']
Q3_2012_row_count = int(Q3_2012_entries.count().iloc[0])
entry_values.append(Q3_2012_row_count)


Q4_2012_entries = suspicious_traffic['2012-10-01':'2012-12-31']
Q4_2012_row_count = int(Q4_2012_entries.count().iloc[0])
entry_values.append(Q4_2012_row_count)


# 2013
Q1_2013_entries = suspicious_traffic['2013-01-01':'2013-03-31']
Q1_2013_row_count = int(Q1_2013_entries.count().iloc[0])
entry_values.append(Q1_2013_row_count)


Q2_2013_entries = suspicious_traffic['2013-04-01':'2013-06-30']
Q2_2013_row_count = int(Q2_2013_entries.count().iloc[0])
entry_values.append(Q2_2013_row_count)


Q3_2013_entries = suspicious_traffic['2013-07-01':'2013-09-30']
Q3_2013_row_count = int(Q3_2013_entries.count().iloc[0])
entry_values.append(Q3_2013_row_count)


Q4_2013_entries = suspicious_traffic['2013-10-01':'2013-12-31']
Q4_2013_row_count = int(Q4_2013_entries.count().iloc[0])
entry_values.append(Q4_2013_row_count)

# 2014
Q1_2014_entries = suspicious_traffic['2014-01':'2014-03']
Q1_2014_row_count = int(Q1_2014_entries.count().iloc[0])
entry_values.append(Q1_2014_row_count)


Q2_2014_entries = suspicious_traffic['2014-04-01':'2014-06-30']
Q2_2014_row_count = int(Q2_2014_entries.count().iloc[0])
entry_values.append(Q2_2014_row_count)


Q3_2014_entries = suspicious_traffic['2014-07-01':'2014-09-30']
Q3_2014_row_count = int(Q3_2014_entries.count().iloc[0])
entry_values.append(Q3_2014_row_count)


suspicious_traffic_graph = plt.figure(2)
plt.plot(entry_values)
plt.title('HTTP traffic containing executables or common exploits\nOccurrences per quarter')
plt.ylabel('Occurrences per quarter')
plt.xticks(range(len(x_ticks)), labels=x_ticks)
suspicious_traffic_graph.show()

