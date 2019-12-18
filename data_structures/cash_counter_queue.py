"""Simulate Banking Cash Counter
This is a Program which creates Banking Cash Counter where people
come in to deposit Cash and withdraw Cash. Have an input panel to add people
to Queue to either deposit or withdraw money and dequeue the people. Maintain
the Cash Balance.
"""
from data_structures_util import Queue

queue_object = Queue()
banking = queue_object.cash_counter()

