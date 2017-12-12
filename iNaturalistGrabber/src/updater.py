import datetime
import iNatUpdater
import csv
import Taxa_Getter
from collections import OrderedDict

def calculate_datetime_difference(past, requested_day=""):
    """
        Calculates the difference in the datetime of the previous update
        and the current update

        params:
            past: a string object that is a date of last update
            requested_day: an optional string object that is the newly requested day

        returns:
            a dictionary of dictionaries with an integer mapped to the dictionary
            that contains the month mapped to an integer (1-12) and a year mapped to an
            integer

    """
    past_year = int(past.split()[2])
    past_month = int(past.split()[0])
    past_day = int(past.split()[1])

    new_year = ''
    new_month = ''
    new_day = ''

    if requested_day == '':
        new_year = datetime.date.today().year
        new_month = datetime.date.today().month
        new_day = datetime.date.today().day

    else:
        new_year = int(requested_day.split()[2])
        new_month = int(requested_day.split()[0])
        new_day = int(requested_day.split()[1])

        new_date = datetime.date(int(new_year), int(new_month), int(new_day))

    date_lst = []
    index = 0

    while(True):

        if past_year >= new_year:

            if past_month >= new_month:
                return date_lst
        current_date_dict = {}
        current_date_dict['month'] = str(past_month)
        current_date_dict['year'] = str(past_year)

        past_month += 1

        if past_month >= 13:
            print("here")
            past_month = 1
            past_year += 1

        date_lst.append(current_date_dict)




def parse_tax_file(fname):
    """
    Parses the tax file to build a dictionary with the taxonomy ID
    This is an extremely hardcoded function and should not be used normally

    params:
        fname: a string representing a file name

    returns: a dictionary with the taxonomy id mapped to the species name
    """

    tax_spec = {}
    with open(fname, 'r') as ptr:
        ptr.readline() #skip the header line

        for line in ptr:
            lst = line.split()
            tax_spec[lst[0]] = ' '.join(lst[1:])

    return tax_spec


def clean_requests(request_lst):
    '''
        Cleans the request list and forms it into something that can be translated into a csv

        params:
            request_lst: the list that would be retrieved from iNatUpdater.ObsGrabber.get_all_obs_for_id()
            primary key: the string of the primary key, in this case it would be taxon id

        returns:
            a list of orderd dictionaries
    '''
    output_lst = []
    for i in request_lst:
        output_lst.extend(i)

    return output_lst

def write_to_csv(lst, fname_out):
    """
        Writes to a csv file containing the output. lst is the list that will be writen
        and must be a list of dictionarys/OrderedDicts

    """
    if len(lst) < 1:
        return None

    fieldnames = lst[0]
    with open(fname_out, 'w', newline='') as ptr:
        od_writer = csv.DictWriter(ptr, fieldnames=fieldnames)
        od_writer.writeheader()
        for i in lst:
            od_writer.writerow(i)

def read_from_input_file(fname, taxon_ids=True):
    """
    Taxon_Getter needs to be fixed so this will work. It kinda works, but can't deal with any
    inputs that aren't perfect
    """
    d = {}

    with open(fname, 'r') as ptr:
        for line in ptr:
            if taxon_ids:
                lst = line.split()
                temp = {lst[0]: ' '.join(lst[1:]).strip()}
                d.update(temp)
            else:
                d[Taxa_Getter.get_taxa_id(line)[0]] = line;

    return d

def read_config_file(fname):
    """
    Reads the config file in and outputs a dictionary for the
    program to run through.
    """
    d = {}
    with open(fname, 'r') as ptr:
        for line in ptr:
            splitline = line.split()
            key = splitline[0]
            value = ' '.join(splitline[1:])
            temp = {key: value}
            d.update(temp)

    return d

def main():
    """
    Runs this bad boy... Requires that one has a config file, if needed, the file pathname can be
    edited below. The first statement is a demo, it may be removed at some point, but for now
    it is going to stay that way.

    """
    config_file = '../config/config.txt'

    if len(config_file) == 0:
        date1 = '7 1 2017'
        date2 = '9 1 2017'

        calls_delta = .01
        fname = '../data/demo.txt'
        id_species = read_from_input_file(fname)

    else:

        config_options = read_config_file(config_file);

        #print(config_options)
        date1 = (config_options['date1'])
        date2 = (config_options['date2'])
        calls_delta = float(config_options['call_rate'])
        fname_in = config_options['input_file']
        fname_out = config_options['output_file']

        if config_options['taxon_id'].lower() == 'f':
            is_taxon_ids = False
        else:
            is_taxon_ids = True

        id_species = read_from_input_file(fname_in, taxon_ids=is_taxon_ids)


    print(date1)
    print(date2)
    lst_dates = calculate_datetime_difference(date1, date2)

    print(lst_dates)
    lst_all_taxon_obs = []
    for taxon_id in id_species:
        current = iNatUpdater.ObsGrabber(calls_delta, id_species[taxon_id], taxon_id)
        for date in lst_dates:
            lst_all_taxon_obs.append(current.get_all_obs_for_id(taxon_id, date['month'], date['year']))

    lst_all_taxon_obs = clean_requests(lst_all_taxon_obs)
    write_to_csv(lst_all_taxon_obs, '../data/out.csv')



main()
