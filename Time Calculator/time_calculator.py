def add_time(start, duration, day=None):
    new_time = ""
    start_time = start.split(" ")
    hour_start = start_time[0].split(":")[0]
    minute_start = start_time[0].split(":")[1]
    am_pm = start_time[1]

    hour_duration = duration.split(":")[0]
    minute_duration = duration.split(":")[1]

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_index = 0
    if (day != None):
        day = day.lower().capitalize()
        day_index = days.index(day)

    minute_result = (int(minute_start) + int(minute_duration)) % 60
    minute_save = (int(minute_start) + int(minute_duration)) // 60

    hour_start_convert = int(hour_start) % 12
    if (am_pm == "PM"):
        hour_start_convert += 12
    
    hour_result = hour_start_convert + int(hour_duration) + minute_save
    day_after = hour_result // 24
    hour_result = hour_result % 24

    am_pm_result = "AM"
    if hour_result >= 12:
        am_pm_result = "PM"
        hour_result = hour_result % 12
    if hour_result == 0:
        hour_result = 12

    str_minute = str(minute_result)
    if minute_result < 10:
        str_minute = "0" + str(minute_result)
    
    temp = (day_after % 7)
    while(temp):
        day_index += 1
        day_index %= 7
        temp -= 1
    
    if day_after == 0:
        day_after = None
    elif day_after == 1:
        day_after = "(next day)"
    else:
        day_after = "({} days later)".format(day_after)

    if day != None:
        new_time = "{}:{} {}, {}".format(hour_result, str_minute, am_pm_result, days[day_index])
    else:
        new_time = "{}:{} {}".format(hour_result, str_minute, am_pm_result)
    if day_after != None:
        new_time = new_time + " " + day_after

    return new_time
