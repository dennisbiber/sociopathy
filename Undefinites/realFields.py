from .integralFields import integralField
from .integerFields import integerField
from .posineutralFields import posineutralField
from .negaNeutralFields import negaNeutralField

__author__ = "Dennis Biber <decibelsTechnology>"


class RealField(integralField, integerField, posineutralField, negaNeutralField):

    def __init__(self, position, size, timeValue, orientation):
        self._fieldType = orientation
        super(RealField, self).__init__(position, size, self._fieldType)
        self._celerationRate = 1
        self._spinType = None
        self._time = timeValue

    def clock(self):
        time.sleep(self._time)

    def poseHandler(self):
        spinType = self._spinType
        position = int(self._position)
        if position <= 3:
            if spinType <= 1:
                spinType += 1
            elif spinType == 2:
                spinTpye = 0
                position += 1
            if position == 3:
                self.poseHandler()

    def spinForward(self):
        self._lastPosition = self._position
        if self._lastPosition == "3":
            self._lastPosition = "-1"
        self._position = str(int(self._lastPosition) + 1)
        self.buildField(self)