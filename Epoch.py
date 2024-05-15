# This function converts the number of days in a year to the corresponding month and day.
# It takes two parameters: days (the number of days) and leap (a boolean indicating if it's a leap year).
# It returns a tuple containing the month and day.
def days_to_month(days, leap:bool):

    if days > 366:
        raise ValueError('Insert valid day number. Less than 366.')
    
    if leap:
        days_in_month = [31,29,31,30,31,30,31,31,30,31,30,31]    
    else:
        days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    
    _days = days
    month = 1
    for i in range(12):
        if _days <= days_in_month[i]:
            break
        _days -= days_in_month[i]
        month += 1
    
    return month, _days




# This function converts the given epoch time to UTC time.
# It takes one parameter: epoch (the epoch time).
# It returns a tuple containing the formatted time string and a dictionary with individual time components.
def epochToUTC(epoch):

    # Split the epoch time into two sections: before and after the decimal point
    first_section, second_section = epoch.split('.')
    first_section = int(first_section)
    second_section = float('.'+second_section)

    # Extract the year, month, and day from the first section of the epoch time
    year = first_section // 1000
    month, days = days_to_month(first_section % 1000, year % 4 == 0)
    
    # Calculate the hours, minutes, seconds, and milliseconds from the second section of the epoch time
    hours = second_section * 24.
    minutes = (hours - int(hours)) * 60
    seconds = (minutes - int(minutes)) * 60
    milliseconds = (seconds - int(seconds)) * 1000

    # Format the time string in UTC format
    time = f'time: {year}-{month}-{days} {int(hours)}:{int(minutes)}:{int(seconds)}::{int(milliseconds)} UTC'

    # Create a dictionary with individual time components
    time_d = {'year': year, 'month': month, 'days': days, 'hours': int(hours), 'minutes': int(minutes), 'seconds': int(seconds), 'milliseconds': int(milliseconds)}
    
    return time, time_d