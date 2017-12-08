'''
ISTA 422 Final Project
Team Name: Monarch 2.0
Code Author: Phillip Johnson
Purpose of script:
	This Python script is used to clean and organize data from iNaturalist Gbif dump 
	and eButterfly Database dump and integrate it into a singular file in a format needed
	to run the R Species Distribution Model program. For additional information about specific 
	functionality of this code, please see additional comments included in the code below.
'''
#import csv utilizes the Python library that specializes in CSV manipulation and file writing.
import csv
import string
import os
'''
Global Variables:
	This predetermines items that will been to be reference throughout the different functions
	without having to explicitely return them from each function.
'''

year_keys=[]
month_list=['01','02','03','04','05','06','07','08','09','10','11','12','all']
data_dict={}


'''
Function get_iNat:
	This function opens and reads data from iNaturalist, in the form of the Gbif data dump. Once 
	open, it traverses the file, creating a dictionary association of each entry by scientificName,
	year, month, latitude, and longitude. While accomplishing this, it also does not transcribe
	any data that is not marked as 'Research Grade' or any data that is missing information in the areas
	needed. This function returns None, but rather fills the data_dict global variable.

	This code is optimized to pull out ONLY butterfly and moth observations from this file, but having a
	requirement of the 'order' in the dataset to be Lepidoptera. 
	
	If you would prefer to pull ALL observations for the purpose of cleaning and analysis. Please remove
	the portion (row['order'] == 'Lepidoptera' and) from line 44 and 69.
	
'''
def get_iNat(filename):
	with open(filename,  encoding='utf8') as csvfile:
		reader = csv.DictReader(csvfile)
		data_keys=data_dict.keys()
		for row in reader:
			if row['order'] == 'Lepidoptera' and row['scientificName'] not in data_keys and row['datasetName'] == 'iNaturalist research-grade observations':
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
					
					
			elif row['order'] == 'Lepidoptera' and row['datasetName'] == 'iNaturalist research-grade observations':	
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
				

			
'''
Function get_eButterfly:
	This function opens and reads data from a csv file created from the eButterfly sql data dump 
	(this datadump is partially cleaned and extracted via a seperate script). Once open, it traverses 
	the file, creating a dictionary association of each entry by scientificName 
	(in this files case, it is labeled latin_name), year, month, latitude, and longitude. While 
	accomplishing this, it also does not transcribe any data that is missing information in the areas
	needed. This function returns None, but rather fills/augments the data_dict global variable.
'''
def get_eButterfly(filename):
	with open(filename,  encoding='utf8') as csvfile:
		reader = csv.DictReader(csvfile)
		data_keys=data_dict.keys()
		for row in reader:
		#row['ColumnID'] = total_rows['ColumnID'].astype(str)
			if row['latin_name'] not in data_keys:
				data_dict[row['latin_name']]= {}				
				'''
				organizing dictionary input into format {{year}, {month}, [lat, long]}
				'''
				
				if len(row['year_created'])==4:
					data_dict[row['latin_name']][row['year_created']]={}
					data_dict[row['latin_name']][row['year_created']]['01']=[]
					data_dict[row['latin_name']][row['year_created']]['02']=[]
					data_dict[row['latin_name']][row['year_created']]['03']=[]
					data_dict[row['latin_name']][row['year_created']]['04']=[]
					data_dict[row['latin_name']][row['year_created']]['05']=[]
					data_dict[row['latin_name']][row['year_created']]['06']=[]
					data_dict[row['latin_name']][row['year_created']]['07']=[]
					data_dict[row['latin_name']][row['year_created']]['08']=[]
					data_dict[row['latin_name']][row['year_created']]['09']=[]
					data_dict[row['latin_name']][row['year_created']]['10']=[]
					data_dict[row['latin_name']][row['year_created']]['11']=[]
					data_dict[row['latin_name']][row['year_created']]['12']=[]
					#cleaning month formatting vvv
					if len(row['month_created']) == 1:
						row['month_created']='0' + row['month_created']
					#format is Latitude, longitude
					data_dict[row['latin_name']][row['year_created']][row['month_created']].append([row['latitude'],row['longitude']])
					
					
			else :	
				
				year_key = data_dict[row['latin_name']].keys()
				if row['year_created'] not in year_key:
					year_keys.append([row['year_created']])
					data_dict[row['latin_name']][row['year_created']]={}
					data_dict[row['latin_name']][row['year_created']]['01']=[]
					data_dict[row['latin_name']][row['year_created']]['02']=[]
					data_dict[row['latin_name']][row['year_created']]['03']=[]
					data_dict[row['latin_name']][row['year_created']]['04']=[]
					data_dict[row['latin_name']][row['year_created']]['05']=[]
					data_dict[row['latin_name']][row['year_created']]['06']=[]
					data_dict[row['latin_name']][row['year_created']]['07']=[]
					data_dict[row['latin_name']][row['year_created']]['08']=[]
					data_dict[row['latin_name']][row['year_created']]['09']=[]
					data_dict[row['latin_name']][row['year_created']]['10']=[]
					data_dict[row['latin_name']][row['year_created']]['11']=[]
					data_dict[row['latin_name']][row['year_created']]['12']=[]
					#cleaning month formatting vvv
					if len(row['month_created']) == 1:
						row['month_created']='0' + row['month_created']
					'''
					Checking that entries have Lat/long coords, not transcribing entries if they do not.
					'''
						
					if len(row['latitude']) > 1 or len(row['longitude']) > 1:
						data_dict[row['latin_name']][row['year_created']][row['month_created']].append([row['latitude'],row['longitude']])

				else:
					if len(row['month_created']) == 1:
						row['month_created']='0' + row['month_created']
					if len(row['latitude']) > 1 or len(row['longitude']) > 1:

						data_dict[row['latin_name']][row['year_created']][row['month_created']].append([row['latitude'],row['longitude']])
			


#Runs get_iNat function and organizes/cleans observations.csv file from the Gbif Datadump (iNaturalist)
print('Beginning cleaning of iNaturalist Data')
get_iNat('observations.csv')
print('Cleaning of iNaturalist Data Complete')
print('Beginning cleaning of eButterfly Data')
#Runs get_eButterfly function and organizes/cleans eb_butterflies_new.csv file from the eButterfly Datadump.
get_eButterfly('eb_butterflies_new.csv')
print('Processing Complete, beginning file creation and integration of data sources')

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
This portion of code takes the filled global variable data_dict and creates a
	csv file which will be used by the Species Distribution Model (SDM) as well
	as allowing easier user viewing if further or seperate analysis is needed on 
	the combined, cleaned datasets.
'''
#Format of CSV is scientificName, year, month, latitude, longitude
with open('data_for_sdm.csv','w', encoding='utf-8') as csv_file:
	csvwriter = csv.writer(csv_file, delimiter=',' )

	csvwriter.writerow(['scientificName','year','month','latitude','longitude'])

	for id in data_dict:
		for year in data_dict[id]:
			for month in data_dict[id][year]:
				for coords in data_dict[id][year][month]:
					for m in range(len(coords)):
						coords[m]=coords[m].strip()
						coords[m]=coords[m].replace('N' ,'')
						coords[m]=coords[m].replace('+' ,'')
						coords[m]=coords[m].replace(' ' ,'.',1)
						coords[m]=coords[m].replace('\\' ,'')
						coords[m]=coords[m].replace("'" ,'.')
						coords[m]=coords[m].replace('"' ,'.')
						coords[m]=coords[m].replace("′" ,'.')
						coords[m]=coords[m].replace('″' ,'.')
						coords[m]=coords[m].replace(';' ,'.')
						coords[m]=coords[m].replace(',' ,'')
						coords[m]=coords[m].replace('_' ,'')
						coords[m]=coords[m].replace('>' ,'.')
						coords[m]=coords[m].replace(':' ,'.')
						if len(coords[m])>1:
							coords[m]=coords[m].replace('°' ,'')
							for n in range(len(coords[m])):
								if coords[m][n].isalpha():
									coords[m]=coords[m].replace(coords[m][n] ,' ')
							
							decimal_counter=0
							for o in range(len(coords[m])):
								if o <= len(coords[m]):
									if coords[m][o]=='.':
										decimal_counter+=1
										if decimal_counter > 1:
											coords[m][o]
											coords[m]=coords[m][0:o]+coords[m][o+1:]+' '
											decimal_counter-=1

							for p in range(len(coords[m])):
								if coords[m][p]=='-' and p!=0:
										coords[m][p]
										coords[m]=coords[m][0:p]+coords[m][p+1:]+' '

							
							coords[m]=coords[m].replace(' ' ,'')
					csvwriter.writerow([id,year, month,coords[0], coords[-1]])

	
print('data_for_sdm.csv created successfully. This is useful for visualizing the data in a clean excel form')



'''
This portion of code seperates each Species into their own files, containing all
of the data for that species in the format scientificName, year, month, latitude, 
longitude. When this code finishes running there will be a singular csv for each 
and every species. This code has a threshold requirement of 20 total observations 
for the species to be considered, and written. This portion also write individual
files for each species for each month, containing all observations for that species
for all years during that month. All written files will be contained within a folder
named the species scientificName.


'''

print('Beginning species specific csv file creation.')
species=list(data_dict.keys())
with open('species_list.csv','w', encoding='utf-8') as csv_file:
	csvwriter_species = csv.writer( csv_file, delimiter=',' )
	for each in species:
		#print(each)
		if len(each)<3 :
			del each
		else:
			csvwriter_species.writerow([each])
		
for i in range(len(species)):
	nameset=species[i]
	naming=nameset.split()
	for j in range(len(naming)):
		naming[j]=naming[j].strip('"')
		for char in naming[j]:
			if char in " ?.!/;:":
				naming[j] = naming[j].replace(char,'')
	join_name='_'.join(naming)
	filename = str(join_name )

	
	if len(filename)>3:
		if not os.path.exists(filename) :
			os.makedirs(filename)
		file_output =os.path.join(filename , filename +'_all.csv')
		with open(file_output,'w', encoding='utf-8') as csv_file:
			csvwriter = csv.writer(csv_file, delimiter=',' )
			csvwriter.writerow(['scientific_name','year','month','latitude','longitude'])
			for year in data_dict[nameset]:
				for month in data_dict[nameset][year]:
					for coords in data_dict[nameset][year][month]:
						coords[0]=coords[0].replace('°' ,'')
						coords[-1]=coords[-1].replace('°' ,'')	
						if len(coords[0]) >1 and coords[0][-1]=='.' :
							coords[0]=coords[0][0:-1]
						if len(coords[-1]) >1 and coords[-1][-1]=='.' :
							coords[-1]=coords[-1][0:-1]
							
						if len(coords[0]) >1 and ',' not in coords[0] and float(coords[0]) >= 15 and float(coords[0]) <= 75:
							if float(coords[-1])>= -165 and float(coords[-1]) <= -52:
								observations_threshold=0
								observations_threshold=len(data_dict[nameset]) + len(data_dict[nameset][year]) + len(data_dict[nameset][year][month])
								if observations_threshold >= 20:
									csvwriter.writerow([nameset, year, month,coords[0], coords[-1]])
									observations_threshold=0
		file_output =filename + '\\' + filename +'_jan.csv'
		with open(file_output,'w', encoding='utf-8') as csv_file:
			csvwriter = csv.writer(csv_file, delimiter=',' )
			csvwriter.writerow(['scientific_name','year','month','latitude','longitude'])
			for year in data_dict[nameset]:
				for month in data_dict[nameset][year]:
					if month == '1':
						for coords in data_dict[nameset][year][month]:
							coords[0]=coords[0].replace('°' ,'')
							coords[-1]=coords[-1].replace('°' ,'')	
							if len(coords[0]) >1 and coords[0][-1]=='.' :
								coords[0]=coords[0][0:-1]
							if len(coords[-1]) >1 and coords[-1][-1]=='.' :
								coords[-1]=coords[-1][0:-1]
							if len(coords[0]) >1 and ',' not in coords[0] and float(coords[0]) >= 15 and float(coords[0]) <= 75:
								if float(coords[-1])>= -165 and float(coords[-1]) <= -52:						
									observations_threshold=0
									observations_threshold=len(data_dict[nameset]) + len(data_dict[nameset][year]) + len(data_dict[nameset][year][month])
									if observations_threshold >= 20:
										csvwriter.writerow([nameset, year, month,coords[0], coords[-1]])
										observations_threshold=0	
		file_output =filename + '\\' + filename +'_feb.csv'
		with open(file_output,'w', encoding='utf-8') as csv_file:
			csvwriter = csv.writer(csv_file, delimiter=',' )
			csvwriter.writerow(['scientific_name','year','month','latitude','longitude'])
			for year in data_dict[nameset]:
				for month in data_dict[nameset][year]:
					if month == '2':
						for coords in data_dict[nameset][year][month]:
							coords[0]=coords[0].replace('°' ,'')
							coords[-1]=coords[-1].replace('°' ,'')	
							if len(coords[0]) >1 and coords[0][-1]=='.' :
								coords[0]=coords[0][0:-1]
							if len(coords[-1]) >1 and coords[-1][-1]=='.' :
								coords[-1]=coords[-1][0:-1]
							if len(coords[0]) >1 and ',' not in coords[0] and float(coords[0]) >= 15 and float(coords[0]) <= 75:
								if float(coords[-1])>= -165 and float(coords[-1]) <= -52:						
									observations_threshold=0
									observations_threshold=len(data_dict[nameset]) + len(data_dict[nameset][year]) + len(data_dict[nameset][year][month])
									if observations_threshold >= 20:
										csvwriter.writerow([nameset, year, month,coords[0], coords[-1]])
										observations_threshold=0	
		file_output =filename + '\\' + filename +'_mar.csv'
		with open(file_output,'w', encoding='utf-8') as csv_file:
			csvwriter = csv.writer(csv_file, delimiter=',' )
			csvwriter.writerow(['scientific_name','year','month','latitude','longitude'])
			for year in data_dict[nameset]:
				for month in data_dict[nameset][year]:
					if month == '3':
						for coords in data_dict[nameset][year][month]:
							coords[0]=coords[0].replace('°' ,'')
							coords[-1]=coords[-1].replace('°' ,'')	
							if len(coords[0]) >1 and coords[0][-1]=='.' :
								coords[0]=coords[0][0:-1]
							if len(coords[-1]) >1 and coords[-1][-1]=='.' :
								coords[-1]=coords[-1][0:-1]
							if len(coords[0]) >1 and ',' not in coords[0] and float(coords[0]) >= 15 and float(coords[0]) <= 75:
								if float(coords[-1])>= -165 and float(coords[-1]) <= -52:						
									observations_threshold=0
									observations_threshold=len(data_dict[nameset]) + len(data_dict[nameset][year]) + len(data_dict[nameset][year][month])
									if observations_threshold >= 20:
										csvwriter.writerow([nameset, year, month,coords[0], coords[-1]])
										observations_threshold=0	
		file_output =filename + '\\' + filename +'_apr.csv'
		with open(file_output,'w', encoding='utf-8') as csv_file:
			csvwriter = csv.writer(csv_file, delimiter=',' )
			csvwriter.writerow(['scientific_name','year','month','latitude','longitude'])
			for year in data_dict[nameset]:
				for month in data_dict[nameset][year]:
					if month == '4':
						for coords in data_dict[nameset][year][month]:
							coords[0]=coords[0].replace('°' ,'')
							coords[-1]=coords[-1].replace('°' ,'')	
							if len(coords[0]) >1 and coords[0][-1]=='.' :
								coords[0]=coords[0][0:-1]
							if len(coords[-1]) >1 and coords[-1][-1]=='.' :
								coords[-1]=coords[-1][0:-1]
							if len(coords[0]) >1 and ',' not in coords[0] and float(coords[0]) >= 15 and float(coords[0]) <= 75:
								if float(coords[-1])>= -165 and float(coords[-1]) <= -52:						
									observations_threshold=0
									observations_threshold=len(data_dict[nameset]) + len(data_dict[nameset][year]) + len(data_dict[nameset][year][month])
									if observations_threshold >= 20:
										csvwriter.writerow([nameset, year, month,coords[0], coords[-1]])
										observations_threshold=0	
		file_output =filename + '\\' + filename +'_may.csv'
		with open(file_output,'w', encoding='utf-8') as csv_file:
			csvwriter = csv.writer(csv_file, delimiter=',' )
			csvwriter.writerow(['scientific_name','year','month','latitude','longitude'])
			for year in data_dict[nameset]:
				for month in data_dict[nameset][year]:
					if month == '5':
						for coords in data_dict[nameset][year][month]:
							coords[0]=coords[0].replace('°' ,'')
							coords[-1]=coords[-1].replace('°' ,'')	
							if len(coords[0]) >1 and coords[0][-1]=='.' :
								coords[0]=coords[0][0:-1]
							if len(coords[-1]) >1 and coords[-1][-1]=='.' :
								coords[-1]=coords[-1][0:-1]
							if len(coords[0]) >1 and ',' not in coords[0] and float(coords[0]) >= 15 and float(coords[0]) <= 75:
								if float(coords[-1])>= -165 and float(coords[-1]) <= -52:						
									observations_threshold=0
									observations_threshold=len(data_dict[nameset]) + len(data_dict[nameset][year]) + len(data_dict[nameset][year][month])
									if observations_threshold >= 20:
										csvwriter.writerow([nameset, year, month,coords[0], coords[-1]])
										observations_threshold=0	
		file_output =filename + '\\' + filename +'_jun.csv'
		with open(file_output,'w', encoding='utf-8') as csv_file:
			csvwriter = csv.writer(csv_file, delimiter=',' )
			csvwriter.writerow(['scientific_name','year','month','latitude','longitude'])
			for year in data_dict[nameset]:
				for month in data_dict[nameset][year]:
					if month == '6':
						for coords in data_dict[nameset][year][month]:
							coords[0]=coords[0].replace('°' ,'')
							coords[-1]=coords[-1].replace('°' ,'')	
							if len(coords[0]) >1 and coords[0][-1]=='.' :
								coords[0]=coords[0][0:-1]
							if len(coords[-1]) >1 and coords[-1][-1]=='.' :
								coords[-1]=coords[-1][0:-1]
							if len(coords[0]) >1 and ',' not in coords[0] and float(coords[0]) >= 15 and float(coords[0]) <= 75:
								if float(coords[-1])>= -165 and float(coords[-1]) <= -52:						
									observations_threshold=0
									observations_threshold=len(data_dict[nameset]) + len(data_dict[nameset][year]) + len(data_dict[nameset][year][month])
									if observations_threshold >= 20:
										csvwriter.writerow([nameset, year, month,coords[0], coords[-1]])
										observations_threshold=0	
		file_output =filename + '\\' + filename +'_jul.csv'
		with open(file_output,'w', encoding='utf-8') as csv_file:
			csvwriter = csv.writer(csv_file, delimiter=',' )
			csvwriter.writerow(['scientific_name','year','month','latitude','longitude'])
			for year in data_dict[nameset]:
				for month in data_dict[nameset][year]:
					if month == '7':
						for coords in data_dict[nameset][year][month]:
							coords[0]=coords[0].replace('°' ,'')
							coords[-1]=coords[-1].replace('°' ,'')	
							if len(coords[0]) >1 and coords[0][-1]=='.' :
								coords[0]=coords[0][0:-1]
							if len(coords[-1]) >1 and coords[-1][-1]=='.' :
								coords[-1]=coords[-1][0:-1]
							if len(coords[0]) >1 and ',' not in coords[0] and float(coords[0]) >= 15 and float(coords[0]) <= 75:
								if float(coords[-1])>= -165 and float(coords[-1]) <= -52:						
									observations_threshold=0
									observations_threshold=len(data_dict[nameset]) + len(data_dict[nameset][year]) + len(data_dict[nameset][year][month])
									if observations_threshold >= 20:
										csvwriter.writerow([nameset, year, month,coords[0], coords[-1]])
										observations_threshold=0	
		file_output =filename + '\\' + filename +'_aug.csv'
		with open(file_output,'w', encoding='utf-8') as csv_file:
			csvwriter = csv.writer(csv_file, delimiter=',' )
			csvwriter.writerow(['scientific_name','year','month','latitude','longitude'])
			for year in data_dict[nameset]:
				for month in data_dict[nameset][year]:
					if month == '8':
						for coords in data_dict[nameset][year][month]:
							coords[0]=coords[0].replace('°' ,'')
							coords[-1]=coords[-1].replace('°' ,'')	
							if len(coords[0]) >1 and coords[0][-1]=='.' :
								coords[0]=coords[0][0:-1]
							if len(coords[-1]) >1 and coords[-1][-1]=='.' :
								coords[-1]=coords[-1][0:-1]
							if len(coords[0]) >1 and ',' not in coords[0] and float(coords[0]) >= 15 and float(coords[0]) <= 75:
								if float(coords[-1])>= -165 and float(coords[-1]) <= -52:						
									observations_threshold=0
									observations_threshold=len(data_dict[nameset]) + len(data_dict[nameset][year]) + len(data_dict[nameset][year][month])
									if observations_threshold >= 20:
										csvwriter.writerow([nameset, year, month,coords[0], coords[-1]])
										observations_threshold=0	
		file_output =filename + '\\' + filename +'_sep.csv'
		with open(file_output,'w', encoding='utf-8') as csv_file:
			csvwriter = csv.writer(csv_file, delimiter=',' )
			csvwriter.writerow(['scientific_name','year','month','latitude','longitude'])
			for year in data_dict[nameset]:
				for month in data_dict[nameset][year]:
					if month == '9':
						for coords in data_dict[nameset][year][month]:
							coords[0]=coords[0].replace('°' ,'')
							coords[-1]=coords[-1].replace('°' ,'')	
							if len(coords[0]) >1 and coords[0][-1]=='.' :
								coords[0]=coords[0][0:-1]
							if len(coords[-1]) >1 and coords[-1][-1]=='.' :
								coords[-1]=coords[-1][0:-1]
							if len(coords[0]) >1 and ',' not in coords[0] and float(coords[0]) >= 15 and float(coords[0]) <= 75:
								if float(coords[-1])>= -165 and float(coords[-1]) <= -52:						
									observations_threshold=0
									observations_threshold=len(data_dict[nameset]) + len(data_dict[nameset][year]) + len(data_dict[nameset][year][month])
									if observations_threshold >= 20:
										csvwriter.writerow([nameset, year, month,coords[0], coords[-1]])
										observations_threshold=0		
		file_output =filename + '\\' + filename +'_oct.csv'
		with open(file_output,'w', encoding='utf-8') as csv_file:
			csvwriter = csv.writer(csv_file, delimiter=',' )
			csvwriter.writerow(['scientific_name','year','month','latitude','longitude'])
			for year in data_dict[nameset]:
				for month in data_dict[nameset][year]:
					if month == '10':
						for coords in data_dict[nameset][year][month]:
							coords[0]=coords[0].replace('°' ,'')
							coords[-1]=coords[-1].replace('°' ,'')	
							if len(coords[0]) >1 and coords[0][-1]=='.' :
								coords[0]=coords[0][0:-1]
							if len(coords[-1]) >1 and coords[-1][-1]=='.' :
								coords[-1]=coords[-1][0:-1]
							if len(coords[0]) >1 and ',' not in coords[0] and float(coords[0]) >= 15 and float(coords[0]) <= 75:
								if float(coords[-1])>= -165 and float(coords[-1]) <= -52:						
									observations_threshold=0
									observations_threshold=len(data_dict[nameset]) + len(data_dict[nameset][year]) + len(data_dict[nameset][year][month])
									if observations_threshold >= 20:
										csvwriter.writerow([nameset, year, month,coords[0], coords[-1]])
										observations_threshold=0		
		file_output =filename + '\\' + filename +'_nov.csv'
		with open(file_output,'w', encoding='utf-8') as csv_file:
			csvwriter = csv.writer(csv_file, delimiter=',' )
			csvwriter.writerow(['scientific_name','year','month','latitude','longitude'])
			for year in data_dict[nameset]:
				for month in data_dict[nameset][year]:
					if month == '11':
						for coords in data_dict[nameset][year][month]:
							coords[0]=coords[0].replace('°' ,'')
							coords[-1]=coords[-1].replace('°' ,'')	
							if len(coords[0]) >1 and coords[0][-1]=='.' :
								coords[0]=coords[0][0:-1]
							if len(coords[-1]) >1 and coords[-1][-1]=='.' :
								coords[-1]=coords[-1][0:-1]
							if len(coords[0]) >1 and ',' not in coords[0] and float(coords[0]) >= 15 and float(coords[0]) <= 75:
								if float(coords[-1])>= -165 and float(coords[-1]) <= -52:						
									observations_threshold=0
									observations_threshold=len(data_dict[nameset]) + len(data_dict[nameset][year]) + len(data_dict[nameset][year][month])
									if observations_threshold >= 20:
										csvwriter.writerow([nameset, year, month,coords[0], coords[-1]])
										observations_threshold=0		
		file_output =filename + '\\' + filename +'_dec.csv'
		with open(file_output,'w', encoding='utf-8') as csv_file:
			csvwriter = csv.writer(csv_file, delimiter=',' )
			csvwriter.writerow(['scientific_name','year','month','latitude','longitude'])
			for year in data_dict[nameset]:
				for month in data_dict[nameset][year]:
					if month == '12':
						for coords in data_dict[nameset][year][month]:
							coords[0]=coords[0].replace('°' ,'')
							coords[-1]=coords[-1].replace('°' ,'')	
							if len(coords[0]) >1 and coords[0][-1]=='.' :
								coords[0]=coords[0][0:-1]
							if len(coords[-1]) >1 and coords[-1][-1]=='.' :
								coords[-1]=coords[-1][0:-1]
							if len(coords[0]) >1 and ',' not in coords[0] and float(coords[0]) >= 15 and float(coords[0]) <= 75:
								if float(coords[-1])>= -165 and float(coords[-1]) <= -52:						
									observations_threshold=0
									observations_threshold=len(data_dict[nameset]) + len(data_dict[nameset][year]) + len(data_dict[nameset][year][month])
									if observations_threshold >= 20:
										csvwriter.writerow([nameset, year, month,coords[0], coords[-1]])
										observations_threshold=0		
													
print('Individual species csv file creation complete.')
