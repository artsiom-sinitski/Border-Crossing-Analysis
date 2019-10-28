"""
'Border crossing analysis' coding challenge for 
Insight data engeneering program.

Author: Artsiom Sinitski
Email:  artsiom.vs@gmail.com
Date:   10/28/2019
"""
import csv
import time
from math import floor
from argparse import ArgumentParser


def load_data(path="./input/Border_Crossing_Entry_Data.csv"):
    """
    Reads data from the input csv file. The header with column names is skipped.
    Columns that are selected - Border, Date, Measure & Value fields.
    Also, counts total monthly border crossings per border/measure and saves it
    to a list as 'Crossing Entity' dictionary for further processing.
    """
    print("---> Loading data...")

    # "idx_list" keeps track of indicies of crossing entity objects in 'crossings_list'
    idx_list = []
    # each item in 'crossings_list' is a dictionary that holds a crossing entity object
    crossings_list = []

    try:
        with open(path) as csvFile:
            csvData = csv.reader(csvFile)
            #skip the header
            next(csvData, None) 
            for row in csvData:
                border = row[3]
                date = row[4] 
                measure = row[5]
                value = int(row[6])

                key = border + ',' + date + ',' + measure

                if key in idx_list:
                    idx = idx_list.index(key)
                    crossings_list[idx]["Value"] += value
                else:
                    idx_list.append(key)
                    crossing_entity = {
                                        "Date"   : date,
                                        "Border" : border,
                                        "Measure": measure,
                                        "Value"  : value
                                      }
                    crossings_list.append(crossing_entity)
    except OSError as e:
        print("Failed to read the input csv file!")
        print("I/O error({0}): {1}".format(e.errno, e.strerror))
        return

    # print("\n# of crossing entries: ", len(crossings_list))
    # print_list(crossings_list)
    print("     Finished!\n")
    return crossings_list



def sort_data(lst_to_sort):
    """
    Sorts the list of crossing entities by fields:
    date, value, border & measure in descending order
    """
    print("---> Sorting the data...")

    sorted_list = list(lst_to_sort)

    # Need to call sort() in reverse order of "sortby" fields.
    # First, do a sort by "border", then - by "measure",
    # then - by "value" and lastly, sort by the "date".
    sorted_list.sort(key=lambda k: k["Border"])
    sorted_list.sort(key=lambda k: k["Measure"])
    sorted_list.sort(key=lambda k: k["Value"], reverse=True)
    sorted_list.sort(key=lambda k: k["Date"], reverse=True)
    # sorted(list_2_sort, key=itemgetter("date", "value"), reverse=True)
    # sorted_list.sort(key=lambda k: (k["measure"], k["border"]))
    # sorted_list.sort(key=lambda k: (k["date"], k["value"]), reverse=True)

    # print("\n\n*** Sorted list ***")
    # print_list(sorted_list)
    print("     Finished!\n")
    return sorted_list



def calc_moving_avg(input_list):
    """
    Calculates monthly moving averages by Border & Measure fields
    """
    print("---> Calculating moving averages...")

    avg_list = list(input_list)
    avg_list_len = len(avg_list)

    # each element of 'pk_entity_list' list is a dictionary with 2 fields:
    # (1) primary key (PK) := "border || measure" string
    # (2) moving average value
    pk_entity_list = []

    # this list elements positions are used as index hooks into 'pk_entity_list'
    # each element of 'pk_entity_list' list is a PK string
    pk_list = []

    # traverse list in reverse order
    for i in range(avg_list_len-1, -1, -1):
        border = avg_list[i].get("Border")
        measure = avg_list[i].get("Measure")
        value = avg_list[i].get("Value")
        key = border  + ',' + measure

        if key not in pk_list:
            avg_list[i].update({"Average": 0})
            pk_entity = {
                         "prim_key"    : key,
                         "running_avg" : value
                        }
            pk_list.append(key)
            pk_entity_list.append(pk_entity)
        else:
            idx = pk_list.index(key)
            run_average = pk_entity_list[idx]["running_avg"]

            n = (value + run_average)/2
            # need to do the check below to avoid inconsistent roun() function behaviour
            # due to the "round half to even" approach when rounding numbers
            if n-floor(n) == 0.5:
                new_run_average = int(floor(n+0.5)) 
            else:
                new_run_average = round(n)

            avg_list[i].update({"Average": run_average})
            pk_entity_list[idx]["running_avg"] = new_run_average
        
    # print("\n\n*** List with moving averages ***")
    # print_list(avg_list)
    print("     Finished!\n")
    return avg_list



def generate_report(input_list, path="./output/report.csv"):
    """
    Generates the 'report.csv' file and saves it to 'output' folder
    """
    print("---> Generating the report...")

    try:
        with open(path, 'w', encoding='utf8', newline='') as csvFile:
            csv_columns = ['Border','Date','Measure','Value','Average']
            writer = csv.DictWriter(csvFile, fieldnames=csv_columns)
            writer.writeheader()
            for data in input_list:
                writer.writerow(data)
    except OSError as e:
            print("Failed to generate the report file!")
            print("I/O error({0}): {1}".format(e.errno, e.strerror))
            return

    print("     Finished!\n")   
    return



def print_list(to_print):
    """
    Prints each element of a list on a new line
    Used this function for debugging purposes only.
    """
    for item in to_print:
        print(item)



if __name__ == '__main__':
    print('\n========== Border crossing analysis started ==========\n')

    # initialize the command line arguments parser
    parser = ArgumentParser(description='Border crossing analysis app.')
    parser.add_argument('input_path', help='Input data csv file path')
    parser.add_argument('output_path', help='Output path for the report')
    args = parser.parse_args()

    # retrieve input/output pathes from the command line
    in_path = args.input_path
    out_path = args.output_path

    # initialize the list variables
    crossings_list = []
    sorted_crossings_list = []
    averages_list = []

    start_time = time.time()

    # load the data, sort it, calculate avgs & generate the report
    crossings_list = load_data(in_path)
    sorted_crossings_list = sort_data(crossings_list)
    averages_list = calc_moving_avg(sorted_crossings_list)
    generate_report(averages_list, out_path)

    end_time = time.time()

    print("----------------------------------")
    print("Execution time: %s seconds\n" % round(end_time - start_time, 2))
    print('========== Border crossing analysis completed! ==========\n')