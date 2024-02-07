# gpt-assistant
Gpt4free powered assistant that runs python code to accomplish tasks

## Example-1
```
> What is the battery percentage ?

Response:
import psutil

battery = psutil.sensors_battery()
percentage = battery.percent

print(f'The battery percentage is {percentage}%')
Execute (y/N) > y

Output:
The battery percentage is 100.0%
```

## Example-2
```
> What day of the week is today ?

Response:
import datetime

today = datetime.datetime.now()
day_of_week = today.strftime('%A')

print(f'Today is {day_of_week}.')
Execute (y/N) > y

Output:
Today is Wednesday.
```

### gpt4free
https://github.com/xtekky/gpt4free