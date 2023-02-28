"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_acp.html
and https://rusa.org/pages/rulesForRiders
"""

import arrow
import math


#  You MUST provide the following two functions
#  with these signatures. You must keep
#  these signatures even if you don't use all the
#  same arguments.

time_limits = {200: 13.5, 300: 20, 400: 27, 600: 40, 1000: 75}
# max_speed = {200: 34, 400: 32, 600: 30, 1000: 28}



def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
       brevet_dist_km: number, nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  An arrow object
    Returns:
       An arrow object indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """

    hours = 0
    if (control_dist_km == 0):
        pass
    elif (control_dist_km <= 200):
        hours += control_dist_km/34
    elif (brevet_dist_km == 200 and control_dist_km >= 200):
        hours += 200 / 34
    elif (brevet_dist_km == 300 and control_dist_km >= 300):
        hours += 200 / 34
        control_dist_km -= 200
        hours += 100 / 32
    elif (control_dist_km <= 400):
        hours += 200/34
        control_dist_km -= 200
        hours += control_dist_km/32
    elif (brevet_dist_km == 400 and control_dist_km >= 400):
        hours += 200 / 34
        hours += 200 / 32
    elif (control_dist_km <= 600):
        hours += 200 / 34
        hours += 200 / 32
        control_dist_km -= 400
        hours += control_dist_km / 30
    elif (brevet_dist_km == 600 and control_dist_km >= 600):
        hours += 200 / 34
        hours += 200 / 32
        hours += 200 / 30
    elif (control_dist_km <= 1000):
        hours += 200 / 34
        hours += 200 / 32
        hours += 200 / 30
        control_dist_km -= 600
        hours += control_dist_km / 28
    elif (brevet_dist_km == 1000 and control_dist_km >= 1000):
        hours += 200 / 34
        hours += 200 / 32
        hours += 200 / 30
        hours += 400 / 28

    hours = round_hours(hours)
    return brevet_start_time.shift(hours=+hours)


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
          brevet_dist_km: number, nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  An arrow object
    Returns:
       An arrow object indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    hours = 0
    if (control_dist_km == 0):
        hours = 1
    elif (control_dist_km >= brevet_dist_km and control_dist_km <= brevet_dist_km * 1.2):
        hours = time_limits[brevet_dist_km]
    elif (control_dist_km < 60):
        hours = (control_dist_km/20) + 1
    elif (control_dist_km < 600):
        hours = control_dist_km/15
    elif (control_dist_km < 1000):
        hours += 600 / 15
        control_dist_km -= 600
        hours += control_dist_km/11.428
    elif (control_dist_km < 1300):
        hours += 600 / 15
        hours += 400 / 11.428
        control_dist_km -= 1000
        hours += control_dist_km / 13.333

    hours = round_hours(hours)
    return brevet_start_time.shift(hours=+hours)


def round_hours(hours):
    minutes = (round((hours - math.floor(hours)) * 60)) / 60
    hours = math.floor(hours) + minutes
    return hours
