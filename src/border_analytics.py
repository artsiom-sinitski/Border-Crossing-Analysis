"""
Border crossing analysis coding challenge
"""
import csv
# from operator import itemgetter
# from enum import Enum


# TODO: - handle the header of the CSV file
#       - pass the path as command line arguments
def load_data(path="./input/Border_Crossing_Entry_Data-DEV-11.csv"):
    # read from csv file - Border, Date, Measure, Value fields
    # "idx_list" keeps track of indicies of crossing entity objects in 'crossings_list'
    idx_list = []
    # each item in 'crossings_list' is a crossing entity object (as dictionary)
    crossings_list = []

    with open(path) as csvFile:
        csvData = csv.reader(csvFile)
        for row in csvData:
            border = row[3]
            date = row[4] 
            measure = row[5]
            value = int(row[6])
            key = border + ',' + date + ',' + measure

            if key in idx_list:
                #print("key exists!!")
                idx = idx_list.index(key)
                crossings_list[idx]["value"] += value
            else:
                #print("key NOT found!!")
                idx_list.append(key)
                crossing_entity = {
                                    "date"   : date,
                                    "border" : border,
                                    "measure": measure,
                                    "value"  : value
                                  }
                crossings_list.append(crossing_entity)

    print("\n# of crossing entries: ", len(crossings_list))
    print_list(crossings_list)

    return crossings_list


def print_list(to_print):
    for item in to_print:
        print(item)


def sort_data(lst_to_sort):
    # sort the list of crossing entities by the
    # date, value, border & measure in desc order
    sorted_list = list(lst_to_sort)

    # Need to call sort() in reverse order of "sortby" fields.
    # First, do a sort by "border", then - by "measure",
    # then - by "value" and lastly, sort by the "date".
    sorted_list.sort(key=lambda k: k["border"])
    sorted_list.sort(key=lambda k: k["measure"])
    sorted_list.sort(key=lambda k: k["value"], reverse=True)
    sorted_list.sort(key=lambda k: k["date"], reverse=True)
    # sorted(list_2_sort, key=itemgetter("date", "value"), reverse=True)
    # sorted_list.sort(key=lambda k: (k["measure"], k["border"]))
    # sorted_list.sort(key=lambda k: (k["date"], k["value"]), reverse=True)

    print("\n\n*** Sorted list ***")
    print_list(sorted_list)

    return sorted_list


def calc_moving_avg(input_list):
    #calculate moving averages
    avg_list = list(input_list)
    avg_list_len = len(avg_list)

    # each element of 'pk_entity_list' list is a dictionary with 2 fields:
    # the primary key (PK) := "border || measure" string
    # the moving average value
    pk_entity_list = []

    # each element of element of 'pk_entity_list' list is a PK string
    pk_list = []

    # traverse list in reverse order
    for i in range(avg_list_len-1, -1, -1):
        border = avg_list[i].get("border")
        measure = avg_list[i].get("measure")
        value = avg_list[i].get("value")
        key = border  + ',' + measure

        if key not in pk_list:
            avg_list[i].update({"average": 0})
            pk_entity = {
                         "prim_key"    : key,
                         "running_avg" : value
                        }
            pk_list.append(key)
            pk_entity_list.append(pk_entity)
        else:
            idx = pk_list.index(key)
            run_average = pk_entity_list[idx]["running_avg"]
            new_run_average = round( (value + run_average)/2 )

            avg_list[i].update({"average": run_average})
            pk_entity_list[idx]["running_avg"] = new_run_average
        
    print("\n\n*** List with moving averages ***")
    print("Avg list len:", avg_list_len)
    print_list(avg_list)

    return avg_list


def generate_report():
    #gen data report
    print()


if __name__ == '__main__':
    print('Border crossing analysis report:\n')
    crossings_list = []
    sorted_crossings_list = []
    averages_list = []

    # path = "./input/Border_Crossing_Entry_Data-DEV-11.csv"
    # path = "./input/Border_Crossing_Entry_Data-DEV-TieSort.csv"
    path = "./input/Border_Crossing_Entry_Data-DEV-Avg.csv"
    crossings_list = load_data(path)
    sorted_crossings_list = sort_data(crossings_list)
    averages_list = calc_moving_avg(sorted_crossings_list)