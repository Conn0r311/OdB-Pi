# fake_obd.py
class MockResponse:
    """Mimic the obd.Response object"""
    def __init__(self, value=None):
        self.value = value


class FakeOBD:
    """Fake OBD-II connection"""
    def __init__(self):
        self._connected = True
        self._dtcs = [("P0301", "Cylinder 1 Misfire"), ("P0420", "Catalyst Efficiency Low")]

    def is_connected(self):
        return self._connected

    def query(self, command):
        # simulate GET_DTC command
        if command == "GET_DTC":
            return MockResponse(self._dtcs)
        elif command == "CLEAR_DTC":
            self._dtcs.clear()
            return MockResponse([])
        else:
            return MockResponse(None)

# Simulate obd.commands namespace
class commands:
    GET_DTC = "GET_DTC"
    CLEAR_DTC = "CLEAR_DTC"


def OBD(portstr=None, **kwargs):
    """Return a FakeOBD instance"""
    return FakeOBD()
