import csv

# Install required packages [Numpy, Pandas]

try:
    import numpy as np
    import pandas as pd
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'numpy'])
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'pandas'])
finally:
    import numpy as np
    import pandas as pd

# Disable Pandas chained assignments
pd.options.mode.chained_assignment = None
# Print entire Pandas DataFrame
pd.set_option('display.max_rows', None, 'display.max_columns', None)

# Importing csv as data
df_1 = pd.read_csv('data/of_1000.csv', sep = '\t', engine = 'python', header=None)
df_2 = pd.read_csv('data/what_the_code_1000.csv', sep = '\t', engine = 'python', header=None)
df_3 = pd.read_csv('data/does_1000.csv', sep = '\t', engine = 'python', header=None)

# Creating a Decision Support System (DSS) to score unstructured data
# True Positive = 1, False Positive = 0, Negative/Anomaly = 0
# Baseline = ' ', empty string for what-if analysis

print('Explanation [of][what the code][does] in natural language one by one 1.')
print('Above prompt was data mined 3000+ times for sensitivity analysis')
print()

# Scoring [of]
# [of] baseline scored 0
# If listed words in output, score 1
search_of_1 = ['loop', 'index', 'length', 'value', 'check', 'checks']
score_of_1 = df_1[df_1[1].str.contains('|'.join(search_of_1))]
score_of_1['Score'] = 1
size_score_of_1 = score_of_1.shape[0]

search_of_fp = ['i = 0\n# 2.']
score_of_fp = df_1[df_1[1].str.contains('|'.join(search_of_fp))]
score_of_fp['Score'] = 0
size_score_of_fp = score_of_fp.shape[0]

search_of_0 = ['10.\n# \n# 11.\n# \n# 12.\n# \n#']
score_of_0 = df_1[df_1[1].str.contains('|'.join(search_of_0))]
score_of_0['Score'] = 0
size_score_of_0 = score_of_0.shape[0]

# If listed words are not in output, score Anomaly
search_of_anomaly = ['10.\n# \n# 11.\n# \n# 12.\n# \n#', 'i = 0\n# 2.', 'loop', 'index']
score_of_anomaly= df_1[~df_1[1].str.contains('|'.join(search_of_anomaly))]
score_of_anomaly['Score'] = 0
size_score_of_anomaly = score_of_anomaly.shape[0]

# Combine [of] dataframes
of_frames = [score_of_1, score_of_fp, score_of_0, score_of_anomaly]
of_results = pd.concat(of_frames)

print('[of] scoring:')
print(size_score_of_1, '/ 10001 : Scored 1')
print(size_score_of_fp, '/ 10001 : Scored False Positive')
print(size_score_of_0, '/ 10001 : Scored 0')
print(size_score_of_anomaly, '/ 10001 : Scored 0 (Anomaly)')
print()

# Scoring [what the code]
# [what the code] baseline scored False Positive
# If listed words in output, score 1
search_wtc_1 = ['index', 'condition', 'execute', 'We repeat', 'start with i = 0 and j = 0.', 'implementation', 'above', 'range of the length', 'office']
score_wtc_1 = df_2[df_2[1].str.contains('|'.join(search_wtc_1))]
score_wtc_1['Score'] = 1
size_score_wtc_1 = score_wtc_1.shape[0]

search_wtc_fp = ['i = 0\n# 2.']
score_wtc_fp = df_2[df_2[1].str.contains('|'.join(search_wtc_fp))]
# Drop value scored twice
score_wtc_fp.drop(index=826, inplace=True)
score_wtc_fp['Score'] = 0
size_score_wtc_fp = score_wtc_fp.shape[0]

search_wtc_0 = ['10.\n# \n# 11.\n# \n# 12.\n# \n#']
score_wtc_0 = df_2[df_2[1].str.contains('|'.join(search_wtc_0))]
score_wtc_0['Score'] = 0
size_score_wtc_0 = score_wtc_0.shape[0]

# If listed words are not in output, score Anomaly
search_wtc_anomaly = ['10.\n# \n# 11.\n# \n# 12.\n# \n#', 'i = 0\n# 2.', 'index', 'condition', 'execute', 'We repeat', 'start with i = 0 and j = 0.', 'implementation', 'above', 'range of the length', 'office']
score_wtc_anomaly = df_2[~df_2[1].str.contains('|'.join(search_wtc_anomaly))]
score_wtc_anomaly['Score'] = 0
size_score_wtc_anomaly = score_wtc_anomaly.shape[0]

# Combine [what the code] dataframes
wtc_frames = [score_wtc_1, score_wtc_fp, score_wtc_0, score_wtc_anomaly]
wtc_results = pd.concat(wtc_frames).sort_index()

print('[what the code] scoring:')
print(size_score_wtc_1, '/ 10001 : Scored 1')
print(size_score_wtc_fp, '/ 10001 : Scored False Positive')
print(size_score_wtc_0, '/ 10001 : Scored 0')
print(size_score_wtc_anomaly, '/ 10001 : Scored 0 (Anomaly)')
print()

# Scoring [does]
# [does] baseline scored False Positive
# If listed words in output, score 1
search_does_1 = ['length', 'value', 'check', 'checks']
score_does_1 = df_3[df_3[1].str.contains('|'.join(search_does_1))]
score_does_1['Score'] = 1
size_score_does_1 = score_does_1.shape[0]

search_does_fp = ['i = 0\n# 2.']
score_does_fp = df_3[df_3[1].str.contains('|'.join(search_does_fp))]
score_does_fp['Score'] = 0
size_score_does_fp = score_does_fp.shape[0]

# If listed words are not in output, score Anomaly
search_does_0 = ['10.\n# \n# 11.\n# \n# 12.\n# \n#']
score_does_0 = df_3[df_3[1].str.contains('|'.join(search_does_0))]
score_does_0['Score'] = 0
size_score_does_0 = score_does_0.shape[0]

search_does_anomaly = ['10.\n# \n# 11.\n# \n# 12.\n# \n#', 'i = 0\n# 2.', 'length', 'value', 'check', 'checks']
score_does_anomaly= df_3[~df_3[1].str.contains('|'.join(search_does_anomaly))]
score_does_anomaly['Score'] = 0
size_score_does_anomaly = score_does_anomaly.shape[0]

# Combine [does] dataframes
does_frames = [score_does_1, score_does_fp, score_does_0, score_does_anomaly]
does_results = pd.concat(does_frames)

print('[does] scoring:')
print(size_score_does_1, '/ 10001 : Scored 1')
print(size_score_does_fp, '/ 10001 : Scored False Positive')
print(size_score_does_0, '/ 10001 : Scored 0')
print(size_score_does_anomaly, '/ 10001 : Scored 0 (Anomaly)')
print()

# Combining [of][what the code][does] results
size_combined_1 = size_score_of_1 + size_score_wtc_1 + size_score_does_1
size_combined_fp = size_score_of_fp + size_score_wtc_fp + size_score_does_fp
size_combined_0 = size_score_of_0 + size_score_wtc_0 + size_score_does_0
size_combined_anomaly = size_score_of_anomaly + size_score_wtc_anomaly + size_score_does_anomaly

print('Combined [of][what the code][does] scoring:')
print(size_combined_1, '/ 30003 : Scored 1')
print(size_combined_fp, '/ 30003 : Scored False Positive')
print(size_combined_0, '/ 30003 : Scored 0')
print(size_combined_anomaly, '/ 30003 : Scored 0 (Anomaly)')
print()

combined_df = [of_results, wtc_results, does_results]
combined_results = pd.concat(combined_df)

# Displaying scored results
print('8 Words scored 2 or more:')
combined_1 = combined_results[combined_results['Score'] == 1]
frequency_combined = combined_1[0].value_counts()
head_frequency_combined = frequency_combined.head(8)
print(head_frequency_combined.to_string())
print()
print('All', size_combined_1, 'words that scored atleast 1:')

# Display list of scored results
min_combined = combined_1.drop([1, 'Score'], axis = 1)
print(min_combined.sort_index(ascending=True))
print()

# Users input can expand results
print('Additional information can be gathered below!')
print('Enter exit to exit. (Index\'s match .csv file)')
user_input = ''
while user_input != 'exit':
    user_input = input('Enter index of word for expanded results: ')
    # Print row of user input
    print(combined_results.loc[int(user_input)])
    print()

#print_csv = combined_results.to_csv('scored_data.csv', sep='\t')