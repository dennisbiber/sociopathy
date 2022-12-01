from .base.numberAccelerator import Field


__author__ = "Dennis Biber <decibelsTechnology>"

class posineutralField(Field):
    def __init__(self, position, size, fieldType):
        super(posineutralField, self).__init__(position, size, fieldType)
        self.buildField(self)

    def accelerationFactor(self):
        self._celerationRate = 0.9