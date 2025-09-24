dates=['01/01/2020','15/03/2021','23/06/2019']
# final_dates=[]
# for date in dates:
#     formated_date='-'.join(reversed(date.split('/')))
#     final_dates.append(formated_date)
# print(final_dates)   

formated_date=['-'.join(reversed(date.split('/'))) for date in dates]  
print(formated_date)