from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from zip_to_state import map_zip_to_state
from db_logic import get_data

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/insurance")                                                      #grabs zip code from url
def insurance(zip: str):
    state = map_zip_to_state(zip)                                           # "95032" → "California"
    if state is None:                                           
        return []
    data = get_data(state)                                                  # "California" → queried rows
    return [
        {"year": row[0], "type": row[1], "premium": float(row[2]), "state": state}
        for row in data
    ]
