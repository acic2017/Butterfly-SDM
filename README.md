# iNaturalist SDM

## Basic Overview

This application provides a full data pipeline for getting and cleaning iNaturalist butterfly data and eButterfly data, and running this data through Jeff Oliver's species distribution models and algorithms, which creates rasters and image files that help scientists visualize how different butterfly species are distributed across the country, given the month of the year, as well as a stacked image to see the total distribution of butterflies in North America

# VIS TEAM ***********************************************************************************
![input output](https://github.com/ckhoward/iNat-SDM/blob/master/imgs/inputoutput.jpg?raw=true "Input to output")

## System Requirements:
    Software: Python 3.6, R, Git, Anaconda(install as Admin), Bash on Ubuntu
    R packages: dismo, sp, raster, maptools

[Install Ubuntu Bash on Windows](https://msdn.microsoft.com/en-us/commandline/wsl/install-win10)

[Install R on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-install-r-on-ubuntu-16-04-2)

Install R Packages by typing the following into Bash:
1. R
2. install.packages('raster')
3. install packages('sp')
4. install.packages('maptools')
5. install.packages('dismo')
    



## Getting started:

1. Clone the required projects
 * Get Jeff Oliver's SDM with ```git clone https://github.com/jcoliver/ebutterfly-sdm.git```
 * Get this program with ```git clone https://github.com/acic2017/Butterfly-SDM.git```

2. Get your data
 * If downloading [GBIF Observations](http://www.inaturalist.org/observations/gbif-observations-dwca.zip), unzip the downloaded file, and move observations.csv into the directory with organize.py (warning: many input files will be generated here)
* Download [eButterfly Data Dump](https://de.cyverse.org/dl/d/BA2D5507-1F85-4A75-8F11-5B537E44A2D9/ebutterfly-acic.sql), use the SQL to csv file, and move the csv (in this case eb_butterflies_new.csv) into the directory with organize.py 

3. Organize your files
 * ?????
 * Where the organize.py, observations.csv, and eb_butterflies_new.csv are located will create an output file for each species of butterfly that is cleaned through the organize.py file and will have a large folder count (DO NOT PLACE ON DESKTOP)


## How to use:
Run organize.py with ```python organize.py``` from the command line. This script:
 * Cleans the observations.csv and eb_butterflies_new.csv data by removing extraneous and/or missing data ;
 * Creates a user-friendly file, data_for_sdm.csv, containing all observations, with data for Scientific Name, year, month, latitude, and longitude. A text copy is able to be created too, just in case it is preferred. This makes it easier for users to sift through the data of interest, to find any glaring issues;
 * Creates a csv for every species listed in data_for_sdm.csv, that is located in North America, and has a minimum of 13 observations, one for each month, and one for all months, to be used as input for the SDM, as the format [scientific_name_month.csv].


# JUPYPTER NOTEBOOK INFO

# VIS TEAM *********************************************************************************

## Output:

# Vis teams image display*******************************************************************

Final file output from Organize.py will create a file structure as follows:
    Species_Name(folder)/Jan   Feb   Mar  etc.... all/species_name_jan.csv 
            
![Organize.py Output Folder Structure](https://github.com/acic2017/Butterfly-SDM/blob/master/Images%20For%20ReadMe/organize%20output%20file%20structure.png "Organize.py Output File Structure")

![Species Distributions](https://github.com/ckhoward/iNat-SDM/blob/master/imgs/species.png?raw=true "October, November, December, All")



## Warnings

#### Data integrity:

The data_for_sdm.csv that is created contains ALL Lepidoptera observations with valid inputs from both databases, worldwide, regardless of number of observations. The final output is put through a series of filters to ensure only North American species and a minimum number of observations (13) is obtained. This was done to allow researchers the ability to access a clean, combined version of the observations, and be used on any number of unforeseen future analysis

#### Runtimes:

Approximate run time for organization.py to clean and organize/write needed files for the SDM : ~45minutes (data_for_sdm.csv is veiwable after ~5 minutes)

# COMPUTATION TEAM***************************************************************************************************
Approximate run time for SDM/R Script to fully run 5 Taxon ID's and recieve Raster Images: ~3minutes
Estimated run time for SDM/R Script to fully run all 760-780 Taxon ID's and recieve Raster Images: ~6.5hours


#### Space requirement:

# COMPUTATION TEAM/VIS TEAM****************************************************************************************


## License

This program is released under the [MIT License](https://opensource.org/licenses/MIT).

## Contribution

Have an issue? The repository is currently public, but this may change in the future. If you suddenly find that you do not have access to make alterations, file an issue and we will quickly respond. 


 
#### Contributors


Eric Tsetsi, Phillip Johnson, Jorge Barrios, Chris Howard
Janice Walsh, Adrianna Salazar, Asa Myrvik, Megha Agarwal
Jasmin Khan Niazi, Daniel Phillips, Jeremiah Hanson
Isaiah Hanson, Ryan Watson, Sina Ehsani
 
 







