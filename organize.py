'''
ISTA 422 Final Project
Team Name: Monarch 2.0
Code Author: Phillip Johnson
Purpose of script:
	This Python script is used to clean and organize data from iNaturalist Gbif dump 
	and eButterfly Database dump and integrate it into a singular file in a format needed
	to run the R Species Distribution Model program. For additional information about specific 
	functionalityof this code, please see additional comments included in the code below.
'''

import csv

#Global Variables
year_keys=[]
month_list=['01','02','03','04','05','06','07','08','09','10','11','12','all']
data_dict={}


#Complete
def get_iNat(filename):
	with open(filename,  encoding='utf8') as csvfile:
		reader = csv.DictReader(csvfile)
		data_keys=data_dict.keys()
		for row in reader:
			if row['scientificName'] not in data_keys and row['datasetName'] == 'iNaturalist research-grade observations':
				data_dict[row['scientificName']]= {}				
				'''
				organizing dictionary input into format {{year}, {month}, [lat, long]}
				'''
				if row['eventDate'][4]=='-':
					data_dict[row['scientificName']][row['eventDate'][0:4]]={}
					data_dict[row['scientificName']][row['eventDate'][0:4]]['01']=[]
					data_dict[row['scientificName']][row['eventDate'][0:4]]['02']=[]
					data_dict[row['scientificName']][row['eventDate'][0:4]]['03']=[]
					data_dict[row['scientificName']][row['eventDate'][0:4]]['04']=[]
					data_dict[row['scientificName']][row['eventDate'][0:4]]['05']=[]
					data_dict[row['scientificName']][row['eventDate'][0:4]]['06']=[]
					data_dict[row['scientificName']][row['eventDate'][0:4]]['07']=[]
					data_dict[row['scientificName']][row['eventDate'][0:4]]['08']=[]
					data_dict[row['scientificName']][row['eventDate'][0:4]]['09']=[]
					data_dict[row['scientificName']][row['eventDate'][0:4]]['10']=[]
					data_dict[row['scientificName']][row['eventDate'][0:4]]['11']=[]
					data_dict[row['scientificName']][row['eventDate'][0:4]]['12']=[]
					
					
					#format is Latitude, longitude
					data_dict[row['scientificName']][row['eventDate'][0:4]][row['eventDate'][5:7]].append([row['decimalLatitude'],row['decimalLongitude']])
					
					
			elif row['datasetName'] == 'iNaturalist research-grade observations':	
				'''
				This gets rid of all non research grade observations
				'''	
				if len(row['eventDate'])>0 and row['eventDate'][4]=='-':
					year_key = data_dict[row['scientificName']].keys()
					if row['eventDate'][0:4]not in year_key:
						year_keys.append([row['eventDate'][0:4]])
						data_dict[row['scientificName']][row['eventDate'][0:4]]={}
						data_dict[row['scientificName']][row['eventDate'][0:4]]['01']=[]
						data_dict[row['scientificName']][row['eventDate'][0:4]]['02']=[]
						data_dict[row['scientificName']][row['eventDate'][0:4]]['03']=[]
						data_dict[row['scientificName']][row['eventDate'][0:4]]['04']=[]
						data_dict[row['scientificName']][row['eventDate'][0:4]]['05']=[]
						data_dict[row['scientificName']][row['eventDate'][0:4]]['06']=[]
						data_dict[row['scientificName']][row['eventDate'][0:4]]['07']=[]
						data_dict[row['scientificName']][row['eventDate'][0:4]]['08']=[]
						data_dict[row['scientificName']][row['eventDate'][0:4]]['09']=[]
						data_dict[row['scientificName']][row['eventDate'][0:4]]['10']=[]
						data_dict[row['scientificName']][row['eventDate'][0:4]]['11']=[]
						data_dict[row['scientificName']][row['eventDate'][0:4]]['12']=[]
						'''
						Checking that entries have Lat/long coords, not transcribing entries if they do not.
						'''
						if len(row['decimalLatitude']) > 1 or len(row['decimalLongitude']) > 1:
							data_dict[row['scientificName']][row['eventDate'][0:4]][row['eventDate'][5:7]].append([row['decimalLatitude'],row['decimalLongitude']])

					else:
						if len(row['decimalLatitude']) > 1 or len(row['decimalLongitude']) > 1:

							data_dict[row['scientificName']][row['eventDate'][0:4]][row['eventDate'][5:7]].append([row['decimalLatitude'],row['decimalLongitude']])
				

			
#IN PROGRESS
def get_eButterfly(filename):
	with open(filename,  encoding='utf8') as csvfile:
		reader = csv.DictReader(csvfile)
		data_keys=data_dict.keys()
		for row in reader:
			if row['latin_name'] not in data_keys:
				data_dict[row['latin_name']]= {}				
				'''
				organizing dictionary input into format {{year}, {month}, [lat, long]}
				'''
				
				if len(row['year'])==4:
					data_dict[row['latin_name']][row['year']]={}
					data_dict[row['latin_name']][row['year']]['01']=[]
					data_dict[row['latin_name']][row['year']]['02']=[]
					data_dict[row['latin_name']][row['year']]['03']=[]
					data_dict[row['latin_name']][row['year']]['04']=[]
					data_dict[row['latin_name']][row['year']]['05']=[]
					data_dict[row['latin_name']][row['year']]['06']=[]
					data_dict[row['latin_name']][row['year']]['07']=[]
					data_dict[row['latin_name']][row['year']]['08']=[]
					data_dict[row['latin_name']][row['year']]['09']=[]
					data_dict[row['latin_name']][row['year']]['10']=[]
					data_dict[row['latin_name']][row['year']]['11']=[]
					data_dict[row['latin_name']][row['year']]['12']=[]
					
					
					#format is Latitude, longitude
					data_dict[row['latin_name']][row['year']][row['month']].append([row['latitude'],row['longitude']])
					
					
			else :	
				
				year_key = data_dict[row['latin_name']].keys()
				if row['year'] not in year_key:
					year_keys.append([row['year']])
					data_dict[row['latin_name']][row['year']]={}
					data_dict[row['latin_name']][row['year']]['01']=[]
					data_dict[row['latin_name']][row['year']]['02']=[]
					data_dict[row['latin_name']][row['year']]['03']=[]
					data_dict[row['latin_name']][row['year']]['04']=[]
					data_dict[row['latin_name']][row['year']]['05']=[]
					data_dict[row['latin_name']][row['year']]['06']=[]
					data_dict[row['latin_name']][row['year']]['07']=[]
					data_dict[row['latin_name']][row['year']]['08']=[]
					data_dict[row['latin_name']][row['year']]['09']=[]
					data_dict[row['latin_name']][row['year']]['10']=[]
					data_dict[row['latin_name']][row['year']]['11']=[]
					data_dict[row['latin_name']][row['year']]['12']=[]
					'''
					Checking that entries have Lat/long coords, not transcribing entries if they do not.
					'''
					if len(row['latitude']) > 1 or len(row['longitude']) > 1:
						data_dict[row['latin_name']][row['year']][row['month']].append([row['latitude'],row['longitude']])

				else:
					if len(row['latitude']) > 1 or len(row['longitude']) > 1:

						data_dict[row['latin_name']][row['year']][row['month']].append([row['latitude'],row['longitude']])
			


#Runs get_data function and organizes/cleans observations.csv file from the Gbif Datadump (iNaturalist)
get_iNat('observations.csv')

####get_eButterfly('eb_butterflies.csv')

print('Processing Complete, beginning file creation')

''' Writing data in format needed to new TXT file for SDM format

***************************************************************************************************
	If preferred format is TXT and not CSV please uncomment out this function. 
		To do this, please move contents from below "print('data_for_sdm.txt created successfully')" 
		to directly under the astrics line below.
***************************************************************************************************

with open('data_for_sdm.txt','w', encoding='utf-8') as csv_file:
	csvwriter = csv.writer(csv_file, delimiter=',')

	csvwriter.writerow(['scientificName','year','month','latitude','longitude'])

	for id in data_dict:
		for year in data_dict[id]:
			for month in data_dict[id][year]:
				for coords in data_dict[id][year][month]:
					csvwriter.writerow([id,year, month,coords[0], coords[-1]])

					
print('data_for_sdm.txt created successfully')
'''


'''					
Writing data in format needed to new CSV file for easier user viewing
'''
#Format of CSV is scientificName, year, month, latitude, longitude
#Complete
with open('data_for_sdm.csv','w', encoding='utf-8') as csv_file:
	csvwriter = csv.writer(csv_file, delimiter=',' )

	csvwriter.writerow(['scientificName','year','month','latitude','longitude'])

	for id in data_dict:
		for year in data_dict[id]:
			for month in data_dict[id][year]:
				for coords in data_dict[id][year][month]:
					csvwriter.writerow([id,year, month,coords[0], coords[-1]])

open('data_for_sdm.csv', 'w', newline='')
print('data_for_sdm.csv created successfully. This is useful for visualizing the data in a clean excel form')




