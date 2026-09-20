import pgeocode

def map_zip_to_state(zip_code):
    nomi = pgeocode.Nominatim('us')
    result = nomi.query_postal_code(zip_code)
    if result.state_name is None or str(result.state_name) == 'nan':
        return None
    return result.state_name