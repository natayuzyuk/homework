import datetime

def convert(seconds):
    seconds_in_day = 60 * 60 * 24
    seconds_in_hour = 60 * 60
    seconds_in_minute = 60
    days = seconds // seconds_in_day
    hours = (seconds - (days * seconds_in_day)) // seconds_in_hour
    minutes = (seconds - (days * seconds_in_day) - (hours * seconds_in_hour)) // seconds_in_minute
    seconds = (seconds - (days * seconds_in_day) - (hours * seconds_in_hour)) % seconds_in_minute
    print("{0} days, {1} hours, {2} minutes, {3} seconds".format(days, hours, minutes, seconds))
convert (3601)
