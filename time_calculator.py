def add_time(start, duration, starting_day =""): 
    parts = start.split()
    time = parts[0].split(":")
    ending = parts[1] 

    # Convert to 24-hour clock format
    if ending == "PM" :
        hour = int(time[0]) + 12
        time[0] = str(hour)
    # Split the duration into hours and minutes
    dur_time = duration.split(":")

    #Calculate the ending hour
    end_hour = int(time[0]) + int(dur_time[0])
    end_minutes = int(time[1]) + int(dur_time[1])

    if end_minutes >= 60 :
        hours_add = end_minutes // 60
        end_minutes -= hours_add * 60
        end_hour += hours_add
    additional_days = 0
    if end_hour > 24 :
        additional_days  = end_hour // 24
        end_hour -= additional_days * 24
    
    # Convert back to 12-hour clock format
    if end_hour > 0 and end_hour < 12 :
        ending = "AM"
    elif end_hour == 12 :
        ending = "PM"
    elif end_hour > 12 :
        ending = "PM"
        end_hour -= 12
    else : # new_hour == 0
        ending = "AM"
        end_hour += 12

    if additional_days > 0 : 
            days_later = " (next day)" if additional_days == 1 else " (" + str(additional_days) + " days later)"
    else :
        days_later = ""

    week_days = ("Sunday","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

    if starting_day:
        weeks = additional_days // 7
        i = week_days.index(starting_day.capitalize()) + (additional_days - 7 * weeks)
        if i > 6 :
            i -= 7
        day = ", " + week_days[i]
    else :
        day = ""
    
    new_time= str(end_hour) + ":" + \
        (str(end_minutes) if end_minutes > 9 else ("0" + str(end_minutes))) + \
        " " + ending + day + days_later
    
    return new_time 