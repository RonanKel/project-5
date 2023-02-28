import sys

sys.path.append("/brevets")

from mypymongo import brevet_insert, brevet_find
import nose    # Testing framework
import logging

logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)


def test_brevet1():
    start_time = "2022-02-22 00:00"
    distance = 400
    checkpoints = [100,200,300,400]
    brevet_insert(start_time, distance, checkpoints)

    assert brevet_find() == {"begin_date": start_time, "distance": distance, "checkpoints": checkpoints}


def test_brevet2():
    start_time = "2023-01-01 00:00"
    distance = 100
    checkpoints = [50,250,600,900,1000]
    brevet_insert(start_time, distance, checkpoints)

    assert brevet_find() == {"begin_date": start_time, "distance": distance, "checkpoints": checkpoints}