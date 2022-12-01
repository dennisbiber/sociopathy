import threading


__author__ = "Dennis Biber <decibelsTechnology>"

class Field:
    def __init__(self, position, size):
        self._position = f"{position}"
        self._size = size
        self._field = None
        self._FieldStructure = None
        self._middlelLayer = None
        self._frontLayer = None
        self._backLayer = None
        self.patterns()

    def patterns(self):
        def _integralPattern(): 
            _field = {
                "sides": {"left": f"i{self._size}",
                        "right": f"{self._size}i"},
                "0": {"top": f"-{self._size}i+",
                    "bottom": f"+{self._size}i-",
                    "front": f"o{self._size}",
                    "back": f"{self._size}o"},
                "1": {"top": f"o{self._size}",
                    "bottom": f"{self._size}o",
                    "front": f"-{self._size}i+",
                    "back": f"+{self._size}i-"},
                "2": {"top": f"+{self._size}i-",
                    "bottom": f"-{self._size}i+",
                    "front": f"{self._size}o",
                    "back": f"o{self._size}"},
                "3": {"top": f"{self._size}o",
                    "bottom": f"o{self._size}",
                    "front": f"+{self._size}i-",
                    "back": f"-{self._size}i+"}
            }

            return _field

        def _integerPattern():
            _field = {
                "sides": {"left": f"o{self._size}",
                        "right": f"{self._size}o"},
                "0": {"top": f"-{self._size}+",
                    "bottom": f"+{self._size}-",
                    "front": f"i{self._size}",
                    "back": f"i{self._size}i"},
                "1": {"top": f"i{self._size}",
                    "bottom": f"{self._size}i",
                    "front": f"-{self._size}i+",
                    "back": f"+{self._size}i-"},
                "2": {"top": f"+{self._size}-",
                    "bottom": f"-{self._size}+",
                    "front": f"{self._size}i",
                    "back": f"i{self._size}"},
                "3": {"top": f"{self._size}i",
                    "bottom": f"i{self._size}",
                    "front": f"+{self._size}i-",
                    "back": f"-{self._size}i+"}
            }

            return _field

        def _posineutralPattern():
            _field = {
                "sides": {"left": f"-{self._size}+",
                        "right": f"-{self._size}+"},
                "0": {"top": f"o{self._size}",
                    "bottom": f"{self._size}o",
                    "front": f"i{self._size}",
                    "back": f"{self._size}i"},
                "1": {"top": f"i{self._size}",
                    "bottom": f"{self._size}i",
                    "front": f"o{self._size}",
                    "back": f"{self._size}o"},
                "2": {"top": f"{self._size}o",
                    "bottom": f"o{self._size}",
                    "front": f"{self._size}i",
                    "back": f"i{self._size}"},
                "3": {"top": f"{self._size}i",
                    "bottom": f"i{self._size}",
                    "front": f"{self._size}o",
                    "back": f"o{self._size}"}
            }

            return _field

        

        @property
        def fetchIntegralPattern():
            return _integralPattern()

        @property
        def fetchIntegerPattern():
            return _integerPattern()

        @property
        def fetchPosineutralPattern():
            return _posineutralPattern()

        if self._fieldType == "integer":
            self._field = fetchIntegerPattern
        elif self._fieldType == "integral":
            self._field = fetchIntegralPattern
        elif self._fieldType == "posineutral":
            self._field = fetchPosineutralPattern

    def postLayer(self):
        top = self._field.fget()[self._position]["top"]
        bottom = self._field.fget()[self._position]["bottom"]
        back = self._field.fget()[self._position]["back"]
        front = self._field.fget()[self._position]["front"]
        left = self._field.fget()["sides"]["left"]
        right = self._field.fget()["sides"]["right"]

        self._middlelLayer = [
            [[None], [top], [None]],
            [[left], ["o0o"], [right]],
            [[None], [bottom], [None]]
            ]
        
        self._backLayer = [
            [[None], [None], [None]],
            [[None], [back], [None]],
            [[None], [None], [None]]
            ]

        self._frontLayer = [
            [[None], [None], [None]],
            [[None], [front], [None]],
            [[None], [None], [None]]
            ]

    def buildField(self):
        self.postLayer()
        self._FieldStructure = [self._backLayer, self._middlelLayer, self._frontLayer]

    @property
    def fetchFieldType(self):
        return self._fieldType

    @property
    def fetchField(self):
        return self._FieldStructure
