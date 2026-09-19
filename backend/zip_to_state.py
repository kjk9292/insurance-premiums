import uszipcode 

def map_zip_to_state(zip_code):
    search = uszipcode.SearchEngine()
    result = search.by_zipcode(zip_code)
    return result.state_long

