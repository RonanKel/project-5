"""
Nose tests for acp_times.py

Write your tests HERE AND ONLY HERE.
"""

import sys

sys.path.append("/brevets")

from acp_times import open_time, close_time
import arrow
import nose    # Testing framework
import logging

logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)



def assert_loop(dist, checkpoints, start_time):
    for km, time_tuple in checkpoints.items():
        checkpoint_open, checkpoint_close = time_tuple
        assert open_time(km, dist, start_time) == checkpoint_open
        assert close_time(km, dist, start_time) == checkpoint_close
    pass

def test_brevet1():
    start_time = arrow.get("2022-02-22 00:00", "YYYY-MM-DD HH:mm")
    dist = 200
    checkpoints = {
        0: (start_time, start_time.shift(hours=1,minutes=0)),
        50: (start_time.shift(hours=1,minutes=28), start_time.shift(hours=3,minutes=30)),
        150: (start_time.shift(hours=4, minutes=25), start_time.shift(hours=10, minutes=0)),
        200: (start_time.shift(hours=5, minutes=53), start_time.shift(hours=13, minutes=30))
    }
    assert_loop(dist, checkpoints, start_time)

def test_brevet2():
    start_time = arrow.get("2022-02-22 00:00", "YYYY-MM-DD HH:mm")
    dist = 400
    checkpoints = {
        20: (start_time.shift(hours=0,minutes=35), start_time.shift(hours=2,minutes=0)),
        250: (start_time.shift(hours=7,minutes=27), start_time.shift(hours=16,minutes=40)),
        400: (start_time.shift(hours=12, minutes=8), start_time.shift(hours=27, minutes=0)),
        410: (start_time.shift(hours=12, minutes=8), start_time.shift(hours=27, minutes=0))
    }
    assert_loop(dist, checkpoints, start_time)

def test_brevet3():
    start_time = arrow.get("2022-02-22 00:00", "YYYY-MM-DD HH:mm")
    dist = 600
    checkpoints = {
        10: (start_time.shift(hours=0,minutes=18), start_time.shift(hours=1,minutes=30)),
        334: (start_time.shift(hours=10,minutes=4), start_time.shift(hours=22,minutes=16)),
        445: (start_time.shift(hours=13, minutes=38), start_time.shift(hours=29, minutes=40)),
        720: (start_time.shift(hours=18, minutes=48), start_time.shift(hours=40, minutes=0))
    }
    assert_loop(dist, checkpoints, start_time)

def test_brevet4():
    start_time = arrow.get("2022-02-22 00:00", "YYYY-MM-DD HH:mm")
    dist = 1000
    checkpoints = {
        100: (start_time.shift(hours=2,minutes=56), start_time.shift(hours=6,minutes=40)),
        300: (start_time.shift(hours=9,minutes=0), start_time.shift(hours=20,minutes=0)),
        500: (start_time.shift(hours=15, minutes=28), start_time.shift(hours=33, minutes=20)),
        700: (start_time.shift(hours=22, minutes=22), start_time.shift(hours=48, minutes=45))
    }
    assert_loop(dist, checkpoints, start_time)

def test_brevet5():
    start_time = arrow.get("2022-02-22 00:00", "YYYY-MM-DD HH:mm")
    dist = 200
    checkpoints = {
        100: (start_time.shift(hours=2,minutes=56), start_time.shift(hours=6,minutes=40)),
        150: (start_time.shift(hours=4,minutes=25), start_time.shift(hours=10,minutes=0)),
        40: (start_time.shift(hours=1, minutes=11), start_time.shift(hours=3, minutes=0)),
        190: (start_time.shift(hours=5, minutes=35), start_time.shift(hours=12, minutes=40))
    }
    assert_loop(dist, checkpoints, start_time)


