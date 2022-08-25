# Prueba de la clase
from typing import Tuple

class EuclideanMetric:

    def __init__(self, x=Tuple, y=Tuple):
        self.x = x
        self.y = y

    def distance(self) -> float:
        return ((self.y[0] - self.x[0])**2 + (self.y[1] - self.x[1])**2)**(1/2)

distancia = EuclideanMetric((2, 3), (4, 7))
print(distancia.distance())