#!/usr/bin/env python3
# Student ID: mhamilton-edwards

class Time:
    """Simple object type for time of the day.
       data attributes: hour, minute, second
    """
    def __init__(self, hour=12, minute=0, second=0):
        """Constructor for time object""" 
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def sum_times(t1, t2):
    """Add two time objects and return the sum with proper carry-over."""
    sum_time = Time(0, 0, 0)
    sum_time.hour = t1.hour + t2.hour
    sum_time.minute = t1.minute + t2.minute
    sum_time.second = t1.second + t2.second

    # Handle carry-over
    if sum_time.second >= 60:
        sum_time.minute += sum_time.second // 60
        sum_time.second %= 60  # Keep only the remainder seconds

    if sum_time.minute >= 60:
        sum_time.hour += sum_time.minute // 60
        sum_time.minute %= 60  # Keep only the remainder minutes

    return sum_time

def change_time(time, seconds):
    time.second += seconds
    if not valid_time(time):
        while time.second < 0:  # Adjust seconds when they are negative
            time.second += 60
            time.minute -= 1
        while time.second >= 60:  # Adjust seconds when they are over 60
            time.second -= 60
            time.minute += 1
        while time.minute < 0:  # Adjust minutes when they are negative
            time.minute += 60
            time.hour -= 1
        while time.minute >= 60:  # Adjust minutes when they are over 60
            time.minute -= 60
            time.hour += 1
        while time.hour < 0:  # Adjust hours when they are negative
            time.hour += 24
        while time.hour >= 24:  # Adjust hours when they are over 24
            time.hour -= 24
    return None

def valid_time(t):
    """Check for the validity of the time object attributes."""
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.minute >= 60 or t.second >= 60 or t.hour >= 24:
        return False
    return True

