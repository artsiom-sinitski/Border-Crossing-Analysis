"""
Border crossing analysis coding challenge
"""
import csv
# from operator import itemgetter
# from enum import Enum


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
            #extract the date only, no time
            date = date[:10]  
            measure = row[5]
            value = int(row[6])
            key = border + ',' + date + ',' + measure
            crossing_entity = {
                    "date": date,
                    "border" : border,
                    "measure" : measure,
                    "value" : value
                   }

            if key in idx_list:
                #print("key exists!!")
                idx = idx_list.index(key)
                crossings_list[idx]["value"] += value
            else:
                #print("key NOT found!!")
                idx_list.append(key)
                crossings_list.append(crossing_entity)

    print("\n# of crossing entries: ", len(crossings_list))
    print_list(crossings_list)

    return crossings_list


def print_list(to_print):
    for item in to_print:
        print(item)


def sort_data(to_sort):
    # sort the list of crossing entities by the
    # date, value, border & measure in desc order

    sorted_list = to_sort
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

    print("\nSorted list:")
    print_list(sorted_list)

    return sorted_list


def calc_moving_avg():
    #calculate moving avg
    print()


def generate_report():
    #gen data report
    print()


if __name__ == '__main__':
    print('Border crossing analysis report:\n')
    crossings_list = []
    sorted_crossings_list = []

    path = "./input/Border_Crossing_Entry_Data-DEV-11.csv"
    # path = "./input/Border_Crossing_Entry_Data-DEV-TieSort.csv"
    crossings_list = load_data(path)
    sorted_crossings_list = sort_data(crossings_list)