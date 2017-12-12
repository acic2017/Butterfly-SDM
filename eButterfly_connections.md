## To connect to the eButterfly data base, 

1. Download the PostgreSQL Dump from: https://de.cyverse.org/dl/d/BA2D5507-1F85-4A75-8F11-5B537E44A2D9/ebutterfly-acic.sql 
2. Download pgAdmin 4 from: https://www.pgadmin.org/download/
3. Locate the server using this code:  `locate psql | grep /bin`
4. Export path: `PATH=[fill the path of psql]:$PATH`
5. Check the version: `psql --version`
6. To create the empty database locally: `sudo -u postgres createdb ebutterfly`
7. To load the data: `pg_dump -U localhost ebutterfly > dbexport.pgsql`
8. AND : `sudo psql -h localhost -U postgres -d ebutterfly -f ebutterfly-acic.sql`

#### After these steps, you can acess the data using pgAdmin

To extract the data as a CSV file run **eb_butterflies_to_CSV.py** on python.
