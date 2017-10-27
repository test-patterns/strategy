""" Sample problem featuring the strategy pattern. """

from dough import Dough

class Pizza():
    def __init__(self, dough):
        self.dough = dough

    def get_dough_amount(self):
        return self.dough.get_amount()
