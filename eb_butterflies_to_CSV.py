#!/usr/bin/env python
#latin_name, english_name, year, month, latitude, longitude


import pandas as pd
from sqlalchemy import create_engine

query = """

WITH Location AS (SELECT * 
FROM eb_butterflies.observations o JOIN  eb_central.checklists c on c.checklist_id=o.checklist_id
JOIN eb_central.sites s ON s.site_id=c.site_id)

Select o.observation_id, s.english_name, s.latin_name,  Extract(Year from o.created) as "year_created" , Extract(month from o.created) as "month_created", l.latitude, l.longitude
FROM eb_butterflies.observations o Join  eb_butterflies.species s on o.species_id=s.species_id
JOIN Location l on  l.observation_id=o.observation_id

;


"""

e = create_engine(\
        'postgresql://postgres:postgres@localhost:5432/ebutterfly')

c = e.connect()

pd.read_sql_query(query,c).to_csv('eb_butterflies.csv', index = False)

