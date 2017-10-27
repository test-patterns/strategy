""" Sample problem featuring the strategy pattern. """

class Dough():
    """ An interface for dough """

    def get_amount(self):
        raise NotImplementedError
