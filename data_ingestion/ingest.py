#Logic for data ingestion

#For each document scan and retrieve data

import pdfplumber
import psycopg2
import us

files = {
    "collision":     "/Users/kylekoh/Desktop/insurance-project/data/car-insurance-collision-data.pdf",
    "comprehensive": "/Users/kylekoh/Desktop/insurance-project/data/car-insurance-comprehensive-data.pdf",
    "liability":     "/Users/kylekoh/Desktop/insurance-project/data/car-insurance-liability-data.pdf"
}

# connect to PostgreSQL
conn = psycopg2.connect(
    database="insurance",
    user="kylekoh",
    password="rolf12345",
    host="localhost"
)
cursor = conn.cursor()

# create table once
cursor.execute("""
    CREATE TABLE IF NOT EXISTS premiums (
        state   TEXT,
        year    INTEGER,
        premium DECIMAL,
        type    TEXT
    )
""")

# loop through each insurance type
for insurance_type, path in files.items():
    with pdfplumber.open(path) as pdf:
        lines = pdf.pages[0].extract_text().split('\n')
        data_lines = lines[5:]

        for line in data_lines:
            matched_state = None
            for state in us.states.STATES:
                if line.startswith(state.name):
                    matched_state = state.name
                    rest = line[len(state.name):].strip()
                    break

            if matched_state:
                parts = rest.split()
                for year, idx in [("2021", 2), ("2022", 1), ("2023", 0)]:
                    cursor.execute("""
                        INSERT INTO premiums (state, year, premium, type)
                        VALUES (%s, %s, %s, %s)
                    """,
                    (matched_state, int(year), float(parts[idx].replace(',', '')), insurance_type)
                    )

# save and close
conn.commit()
conn.close()