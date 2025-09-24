files=['log_day1.txt', 'log_day2.txt', 'log_day3.txt','log.csv','marcher.csv','log_day4.csv','notes.txt']

# log_files = []
# csv_files = []
# for file in files:
#     if file.startswith('log_'):
#         log_files.append(file)
# for file in files:
#     if file.endswith('.csv'):
#         csv_files.append(file)



log_files=[file for file in files if file.startswith('log_')]
csv_files=[file for file in files if file.endswith('.csv')]
print(log_files)
print(csv_files)