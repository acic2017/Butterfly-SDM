WITH Location AS (SELECT * 
				  FROM eb_butterflies.observations o 
				  JOIN  eb_central.checklists c 	ON c.checklist_id=o.checklist_id
				  JOIN eb_central.sites s 			ON s.site_id=c.site_id)

Select o.observation_id, s.english_name, s.latin_name,  Extract(Year from o.created) as "year_created" , Extract(month from o.created) as "month_created", l.latitude, l.longitude
FROM eb_butterflies.observations o 
Join  eb_butterflies.species s 	ON o.species_id=s.species_id
JOIN Location l 				ON  l.observation_id=o.observation_id 
;