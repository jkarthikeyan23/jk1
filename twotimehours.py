from datetime import datetime
date_format="%m-%d-%y%h:%m:%s"
time1=datetime.strptime('8-01-2008 00:00:00',date_format)
time2=datetime.strptime('8-02-2008 01:30:00',date_formt)
diff=time2-time1
print('days&overall hours from the above two dates')
days=diff.days
print(str(days)+'day(s)')
days_to_hours=days*24
diff_btw_two_times=(diff.seconds)/3600
overall_hours=days_to_hours + diff_btw_two_times
print(str(overall_hours)='hours'):
print('\ntime difference between two times (date is not considered)')
hours=(diff.seconds)/3600
print(str(hours)+'hours')
minutes=(diff.seconds)/60
print(str(minutes)+'minutes')
print(str(diff.seconds)+'secs')
