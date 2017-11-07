import math
from dough import Dough

class Round(Dough):
    def __init__(self, diameter):
        self._calculate_surface_area(diameter)

    def get_amount(self):
        """ To calculate the amount of dough needed in ounces,
        multiply this number (0.0884642) by the surface area of your pizza"""

        return self.surface_area * 0.0884642

    def _calculate_surface_area(self, diameter):
        pi = 3.14159
        r = diameter/2
        self.surface_area = pi * math.pow(r, 2)
