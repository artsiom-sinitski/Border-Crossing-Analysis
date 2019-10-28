"""
Unit tests for the Insight coding challenge solution.

Author: Artsiom Sinitski
Email:  artsiom.vs@gmail.com
Date:   10/28/2019
"""
import unittest
import src.border_analytics as ba

class TestBorderAnalyticsMethods(unittest.TestCase):

    # the main purpose of this is to test that there is only a single entry per border/date/measure combo.
    # test the load_data() method, input csv file has 15 unordered records
    def test_load_data(self):
        crossings_15_list = ba.load_data("./input/Border_Crossing_Entry_Data-TEST-15.csv")
        cl_15_len = len(crossings_15_list)

        # TEST SET #1. Expected content of 'crossings_list':
        #  {'Date': '06/01/2019 12:00:00 AM', 'Border': 'US-Canada Border', 'Value': 133, 'Measure': 'Truck Containers Full'}
        #  {'Date': '06/01/2019 12:00:00 AM', 'Border': 'US-Canada Border', 'Value': 480, 'Measure': 'Truck Containers Empty'}
        #  {'Date': '06/01/2019 12:00:00 AM', 'Border': 'US-Canada Border', 'Value': 619, 'Measure': 'Buses'}
        #  {'Date': '06/01/2019 12:00:00 AM', 'Border': 'US-Canada Border', 'Value': 118, 'Measure': 'Bus Passengers'}
        #  {'Date': '06/01/2019 12:00:00 AM', 'Border': 'US-Mexico Border', 'Value': 98, 'Measure': 'Pedestrians'}
        #  {'Date': '06/01/2019 12:00:00 AM', 'Border': 'US-Mexico Border', 'Value': 9, 'Measure': 'Personal Vehicle Passengers'}
        #  {'Date': '06/02/2019 12:00:00 AM', 'Border': 'US-Mexico Border', 'Value': 16, 'Measure': 'Personal Vehicle Passengers'}
        #  {'Date': '06/02/2019 12:00:00 AM', 'Border': 'US-Canada Border', 'Value': 615, 'Measure': 'Buses'}
        #  {'Date': '05/01/2019 12:00:00 AM', 'Border': 'US-Mexico Border', 'Value': 7, 'Measure': 'Truck Containers Empty'}
        #  {'Date': '05/01/2019 12:00:00 AM', 'Border': 'US-Canada Border', 'Value': 774, 'Measure': 'Trucks'}
        #  {'Date': '06/03/2019 12:00:00 AM', 'Border': 'US-Mexico Border', 'Value': 31, 'Measure': 'Truck Containers Empty'}

        # verify number of records in the list after monthly sum per border/date/measure combo.
        self.assertEqual(cl_15_len, 11, "Not expected number of entries in the list!")

        # verify the entity's content with monthly count value == 133
        date133 = border133 = value133 = measure133 = ''

        for i in range(cl_15_len):
            if crossings_15_list[i]["Value"] == 133:
                date133 =  crossings_15_list[i]["Date"]
                border133 = crossings_15_list[i]["Border"]
                value133 = crossings_15_list[i]["Value"]
                measure133 = crossings_15_list[i]["Measure"]
                break

        self.assertEqual(date133, "06/01/2019 12:00:00 AM", "Wrong date!")
        self.assertEqual(border133, "US-Canada Border", "Wrong border!")
        self.assertEqual(value133, 133, "Wrong value!")
        self.assertEqual(measure133, "Truck Containers Full", "Wrong measure!")

        # verify the 2nd entity, count is the sum of two entries of same date, border & measure
        date480 = border480 = value480 = measure480 = ''

        for i in range(cl_15_len):
            if crossings_15_list[i]["Value"] == 480:
                date480 =  crossings_15_list[i]["Date"]
                border480 = crossings_15_list[i]["Border"]
                value480 = crossings_15_list[i]["Value"]
                measure480 = crossings_15_list[i]["Measure"]
                break
        
        self.assertEqual(date480, "06/01/2019 12:00:00 AM", "Wrong date!")
        self.assertEqual(border480, "US-Canada Border", "Wrong border!")
        self.assertEqual(value480, 480, "Wrong value!")
        self.assertEqual(measure480, "Truck Containers Empty", "Wrong measure!")

        # verify entity, which value should've remained the same
        date7 = border7 = value7 = measure7 = ''

        for i in range(cl_15_len):
            if crossings_15_list[i]["Value"] == 7:
                date7 =  crossings_15_list[i]["Date"]
                border7 = crossings_15_list[i]["Border"]
                value7 = crossings_15_list[i]["Value"]
                measure7 = crossings_15_list[i]["Measure"]
                break
        
        self.assertEqual(date7, "05/01/2019 12:00:00 AM", "Wrong date!")
        self.assertEqual(border7, "US-Mexico Border", "Wrong border!")
        self.assertEqual(value7, 7, "Wrong value!")
        self.assertEqual(measure7, "Truck Containers Empty", "Wrong measure!")

        # verify the last entity, count is the sum of two entries of same date, border & measure
        date31 = border31 = value31 = measure31 = ''

        for i in range(cl_15_len):
            if crossings_15_list[i]["Value"] == 31:
                date31 =  crossings_15_list[i]["Date"]
                border31 = crossings_15_list[i]["Border"]
                value31 = crossings_15_list[i]["Value"]
                measure31 = crossings_15_list[i]["Measure"]
                break
        
        self.assertEqual(date31, "06/03/2019 12:00:00 AM", "Wrong date!")
        self.assertEqual(border31, "US-Mexico Border", "Wrong border!")
        self.assertEqual(value31, 31, "Wrong value!")
        self.assertEqual(measure31, "Truck Containers Empty", "Wrong measure!")



    # test sorting method, espicially when there is date/border/measure tie.
    def test_sort_data(self):
        crossings_list = ba.load_data("./input/Border_Crossing_Entry_Data-TEST-TieToSort.csv")
        crossings_len = len(crossings_list)
        
        # Test Set #2. After calculating montly value sum per border/date/measure combo.
        # {'Date': '06/01/2019 12:00:00 AM', 'Border': 'US-Canada Border', 'Value': 13, 'Measure': 'Truck Containers Full'}
        # {'Date': '06/01/2019 12:00:00 AM', 'Border': 'US-Canada Border', 'Value': 13, 'Measure': 'Truck Containers Empty'}
        # {'Date': '06/01/2019 12:00:00 AM', 'Border': 'US-Canada Border', 'Value': 13, 'Measure': 'Buses'}
        # {'Date': '06/01/2019 12:00:00 AM', 'Border': 'US-Canada Border', 'Value': 13, 'Measure': 'Bus Passengers'}
        # {'Date': '06/01/2019 12:00:00 AM', 'Border': 'US-Mexico Border', 'Value': 13, 'Measure': 'Pedestrians'}
        # {'Date': '06/02/2019 12:00:00 AM', 'Border': 'US-Canada Border', 'Value': 13, 'Measure': 'Rail Containers Full'}
        # {'Date': '06/02/2019 12:00:00 AM', 'Border': 'US-Mexico Border', 'Value': 13, 'Measure': 'Personal Vehicle Passengers'}
        # {'Date': '06/01/2019 12:00:00 AM', 'Border': 'US-Canada Border', 'Value': 13, 'Measure': 'Trucks'}
        # {'Date': '06/01/2019 12:00:00 AM', 'Border': 'US-Canada Border', 'Value': 13, 'Measure': 'Personal Vehicles'}
        # {'Date': '06/01/2019 12:00:00 AM', 'Border': 'US-Canada Border', 'Value': 13, 'Measure': 'Rail Containers Empty'}
        # {'Date': '04/01/2019 12:00:00 AM', 'Border': 'US-Mexico Border', 'Value': 13, 'Measure': 'Personal Vehicles'}
        # {'Date': '04/01/2019 12:00:00 AM', 'Border': 'US-Canada Border', 'Value': 13, 'Measure': 'Personal Vehicles'}

        sorted_list = ba.sort_data(crossings_list)
        sorted_len = len(sorted_list)

        self.assertEqual(sorted_len, crossings_len, "Wrong sorted list length!")
        self.assertEqual(sorted_list[0], {'Date': '06/02/2019 12:00:00 AM', 'Border': 'US-Mexico Border', 'Value': 13, 'Measure': 'Personal Vehicle Passengers'}, "Sorting order is wrong!")
        self.assertEqual(sorted_list[1], {'Date': '06/02/2019 12:00:00 AM', 'Border': 'US-Canada Border', 'Value': 13, 'Measure': 'Rail Containers Full'}, "Sorting order is wrong!")
        self.assertEqual(sorted_list[2], {'Date': '06/01/2019 12:00:00 AM', 'Border': 'US-Canada Border', 'Value': 13, 'Measure': 'Bus Passengers'}, "Sorting order is wrong!")
        self.assertEqual(sorted_list[3], {'Date': '06/01/2019 12:00:00 AM', 'Border': 'US-Canada Border', 'Value': 13, 'Measure': 'Buses'}, "Sorting order is wrong!")
        self.assertEqual(sorted_list[4], {'Date': '06/01/2019 12:00:00 AM', 'Border': 'US-Mexico Border', 'Value': 13, 'Measure': 'Pedestrians'}, "Sorting order is wrong!")
        self.assertEqual(sorted_list[5], {'Date': '06/01/2019 12:00:00 AM', 'Border': 'US-Canada Border', 'Value': 13, 'Measure': 'Personal Vehicles'}, "Sorting order is wrong!")
        self.assertEqual(sorted_list[6], {'Date': '06/01/2019 12:00:00 AM', 'Border': 'US-Canada Border', 'Value': 13, 'Measure': 'Rail Containers Empty'}, "Sorting order is wrong!")
        self.assertEqual(sorted_list[7], {'Date': '06/01/2019 12:00:00 AM', 'Border': 'US-Canada Border', 'Value': 13, 'Measure': 'Truck Containers Empty'}, "Sorting order is wrong!")
        self.assertEqual(sorted_list[8], {'Date': '06/01/2019 12:00:00 AM', 'Border': 'US-Canada Border', 'Value': 13, 'Measure': 'Truck Containers Full'}, "Sorting order is wrong!")
        self.assertEqual(sorted_list[9], {'Date': '06/01/2019 12:00:00 AM', 'Border': 'US-Canada Border', 'Value': 13, 'Measure': 'Trucks'}, "Sorting order is wrong!")
        self.assertEqual(sorted_list[10], {'Date': '04/01/2019 12:00:00 AM', 'Border': 'US-Canada Border', 'Value': 13, 'Measure': 'Personal Vehicles'}, "Sorting order is wrong!")
        self.assertEqual(sorted_list[11], {'Date': '04/01/2019 12:00:00 AM', 'Border': 'US-Mexico Border', 'Value': 13, 'Measure': 'Personal Vehicles'}, "Sorting order is wrong!")

        
    def test_calc_moving_avg(self):
        crossings_list = ba.load_data("./input/Border_Crossing_Entry_Data-TEST-CalcAverages.csv")
        
        sorted_list = ba.sort_data(crossings_list)
        sorted_len = len(sorted_list)

        avgs_list = ba.calc_moving_avg(sorted_list)
        avgs_len = len(avgs_list)

        #ba.print_list(avgs_list)

        # Test Set #3 after being sorted.
        # {'Date': '11/01/2017 12:00:00 AM', 'Border': 'US-Mexico Border', 'Value': 4, 'Measure': 'Truck Containers Empty'}
        # {'Date': '10/01/2017 12:00:00 AM', 'Border': 'US-Mexico Border', 'Value': 15, 'Measure': 'Truck Containers Empty'}
        # {'Date': '10/01/2017 12:00:00 AM', 'Border': 'US-Mexico Border', 'Value': 8, 'Measure': 'Personal Vehicles'}
        # {'Date': '09/01/2017 12:00:00 AM', 'Border': 'US-Canada Border', 'Value': 38, 'Measure': 'Personal Vehicles'}
        # {'Date': '09/01/2017 12:00:00 AM', 'Border': 'US-Mexico Border', 'Value': 7, 'Measure': 'Personal Vehicles'}
        # {'Date': '09/01/2017 12:00:00 AM', 'Border': 'US-Mexico Border', 'Value': 2, 'Measure': 'Truck Containers Empty'}
        # {'Date': '08/01/2017 12:00:00 AM', 'Border': 'US-Mexico Border', 'Value': 1, 'Measure': 'Truck Containers Empty'}
        # {'Date': '03/01/2017 12:00:00 AM', 'Border': 'US-Canada Border', 'Value': 20, 'Measure': 'Rail Containers Full'}
        # {'Date': '02/01/2017 12:00:00 AM', 'Border': 'US-Canada Border', 'Value': 1, 'Measure': 'Rail Containers Full'}
        # {'Date': '01/01/2017 12:00:00 AM', 'Border': 'US-Canada Border', 'Value': 39, 'Measure': 'Rail Containers Full'}
        
        self.assertEqual(sorted_len, avgs_len, "Wrong averages list length!")
        self.assertEqual(avgs_list[0]["Average"], 9, "Average value is incorrect!")
        self.assertEqual(avgs_list[1]["Average"], 2, "Average value is incorrect!")
        self.assertEqual(avgs_list[2]["Average"], 7, "Average value is incorrect!")
        self.assertEqual(avgs_list[3]["Average"], 0, "Average value is incorrect!")
        self.assertEqual(avgs_list[4]["Average"], 0, "Average value is incorrect!")
        self.assertEqual(avgs_list[5]["Average"], 1, "Average value is incorrect!")
        self.assertEqual(avgs_list[6]["Average"], 0, "Average value is incorrect!")
        self.assertEqual(avgs_list[7]["Average"], 20, "Average value is incorrect!")
        self.assertEqual(avgs_list[8]["Average"], 39, "Average value is incorrect!")
        self.assertEqual(avgs_list[9]["Average"], 0, "Average value is incorrect!")


if __name__ == '__main__':
    unittest.main()