import pgeocode

def map_zip_to_state(zip_code):
    nomi = pgeocode.Nominatim('us')
    result = nomi.query_postal_code(zip_code)
    return result.state_name