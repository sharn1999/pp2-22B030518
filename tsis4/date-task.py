import datetime

current = datetime.datetime.now()
date2 = datetime.timedelta(days=5)

print(f'Date 5 days ago: {current-date2}')


currentPast = current - datetime.timedelta(days=1)
currentFuture = current + datetime.timedelta(days=1)
print(f'Yesterday was {currentPast.strftime("%d")} of {currentPast.strftime("%B")}')
print(f'Today is {current.strftime("%d")} of {current.strftime("%B")}')
print(f'Tomorrow will {currentFuture.strftime("%d")} of {currentFuture.strftime("%B")}')

withoutMc = current.replace(microsecond=0)
print(withoutMc)

def date_diff_in_Seconds(dt2, dt1):
  timedelta = dt2 - dt1
  return timedelta.days * 24 * 3600 + timedelta.seconds
date1 = datetime.datetime.strptime('2022-12-11 23:59:59', '%Y-%m-%d %H:%M:%S')
date2 = datetime.datetime.now()
print(f'{date_diff_in_Seconds(date2, date1)} Seconds')

