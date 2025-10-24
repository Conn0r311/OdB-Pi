# reading the OBD-II data
import obd

def connect_obd():
    """Connect to OBD-II adapter"""
    try:
        connection = obd.OBD()  # aut connect via usb 
        print("OBD Connected:", connection.is_connected())
        return connection
    except Exception as e:
        print("OBD connection failed:", e)
        return None

def get_dtc_codes(connection):
    """Return list of dtcs"""
    if not connection or not connection.is_connected():
        return []
    response = connection.query(obd.commands.GET_DTC)
    if response.value:
        return [code[0] for code in response.value]
    return []

def clear_codes(connection):
    """Clear dtcs codes"""
    if connection and connection.is_connected():
        connection.query(obd.commands.CLEAR_DTC)
