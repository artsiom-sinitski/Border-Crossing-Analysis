"""
Unit tests for the Insight coding challenge solution.

Author: Artsiom Sinitski
Email:  artsiom.vs@gmail.com
Date:   10/28/2019
"""
import unittest
import border_analytics as ba


class TestBorderAnalyticsMethods(unittest.TestCase):

    # the main purpose of this is to test that there is only a single entry per border/date/measure combo.
    # test the load_data() method, input csv file has 15 unordered records
    def test_load_data(self):
        crossings_15_list = ba.load_data("../input/Border_Crossing_Entry_Data-TEST-15.csv")
        cl_15_len = len(crossings_15_list)

        # TEST SET #1. Expected content of 'crossings_list':
        #  {'date': '06/01/2019 12:00:00 AM', 'border': 'US-Canada Border', 'value': 133, 'measure': 'Truck Containers Full'}
        #  {'date': '06/01/2019 12:00:00 AM', 'border': 'US-Canada Border', 'value': 480, 'measure': 'Truck Containers Empty'}
        #  {'date': '06/01/2019 12:00:00 AM', 'border': 'US-Canada Border', 'value': 619, 'measure': 'Buses'}
        #  {'date': '06/01/2019 12:00:00 AM', 'border': 'US-Canada Border', 'value': 118, 'measure': 'Bus Passengers'}
        #  {'date': '06/01/2019 12:00:00 AM', 'border': 'US-Mexico Border', 'value': 98, 'measure': 'Pedestrians'}
        #  {'date': '06/01/2019 12:00:00 AM', 'border': 'US-Mexico Border', 'value': 9, 'measure': 'Personal Vehicle Passengers'}
        #  {'date': '06/02/2019 12:00:00 AM', 'border': 'US-Mexico Border', 'value': 16, 'measure': 'Personal Vehicle Passengers'}
        #  {'date': '06/02/2019 12:00:00 AM', 'border': 'US-Canada Border', 'value': 615, 'measure': 'Buses'}
        #  {'date': '05/01/2019 12:00:00 AM', 'border': 'US-Mexico Border', 'value': 7, 'measure': 'Truck Containers Empty'}
        #  {'date': '05/01/2019 12:00:00 AM', 'border': 'US-Canada Border', 'value': 774, 'measure': 'Trucks'}
        #  {'date': '06/03/2019 12:00:00 AM', 'border': 'US-Mexico Border', 'value': 31, 'measure': 'Truck Containers Empty'}

        # verify number of records in the list after monthly sum per border/date/measure combo.
        self.assertEqual(cl_15_len, 11, "Not expected number of entries in the list!")

        # verify the entity's content with monthly count value == 133
        date133 = border133 = value133 = measure133 = ''

        for i in range(cl_15_len):
            if crossings_15_list[i]["value"] == 133:
                date133 =  crossings_15_list[i]["date"]
                border133 = crossings_15_list[i]["border"]
                value133 = crossings_15_list[i]["value"]
                measure133 = crossings_15_list[i]["measure"]
                break

        self.assertEqual(date133, "06/01/2019 12:00:00 AM", "Wrong date!")
        self.assertEqual(border133, "US-Canada Border", "Wrong border!")
        self.assertEqual(value133, 133, "Wrong value!")
        self.assertEqual(measure133, "Truck Containers Full", "Wrong measure!")

        # verify the 2nd entity, count is the sum of two entries of same date, border & measure
        date480 = border480 = value480 = measure480 = ''

        for i in range(cl_15_len):
            if crossings_15_list[i]["value"] == 480:
                date480 =  crossings_15_list[i]["date"]
                border480 = crossings_15_list[i]["border"]
                value480 = crossings_15_list[i]["value"]
                measure480 = crossings_15_list[i]["measure"]
                break
        
        self.assertEqual(date480, "06/01/2019 12:00:00 AM", "Wrong date!")
        self.assertEqual(border480, "US-Canada Border", "Wrong border!")
        self.assertEqual(value480, 480, "Wrong value!")
        self.assertEqual(measure480, "Truck Containers Empty", "Wrong measure!")

        # verify entity, which value should've remained the same
        date7 = border7 = value7 = measure7 = ''

        for i in range(cl_15_len):
            if crossings_15_list[i]["value"] == 7:
                date7 =  crossings_15_list[i]["date"]
                border7 = crossings_15_list[i]["border"]
                value7 = crossings_15_list[i]["value"]
                measure7 = crossings_15_list[i]["measure"]
                break
        
        self.assertEqual(date7, "05/01/2019 12:00:00 AM", "Wrong date!")
        self.assertEqual(border7, "US-Mexico Border", "Wrong border!")
        self.assertEqual(value7, 7, "Wrong value!")
        self.assertEqual(measure7, "Truck Containers Empty", "Wrong measure!")

        # verify the last entity, count is the sum of two entries of same date, border & measure
        date31 = border31 = value31 = measure31 = ''

        for i in range(cl_15_len):
            if crossings_15_list[i]["value"] == 31:
                date31 =  crossings_15_list[i]["date"]
                border31 = crossings_15_list[i]["border"]
                value31 = crossings_15_list[i]["value"]
                measure31 = crossings_15_list[i]["measure"]
                break
        
        self.assertEqual(date31, "06/03/2019 12:00:00 AM", "Wrong date!")
        self.assertEqual(border31, "US-Mexico Border", "Wrong border!")
        self.assertEqual(value31, 31, "Wrong value!")
        self.assertEqual(measure31, "Truck Containers Empty", "Wrong measure!")



    # test sorting method, espicially when there is date/border/measure tie.
    def test_sort_data(self):
        crossings_list = ba.load_data("../input/Border_Crossing_Entry_Data-TEST-TieToSort.csv")
        crossings_len = len(crossings_list)
        
        # Test Set #2. After calculating montly value sum per border/date/measure combo.
        # {'date': '06/01/2019 12:00:00 AM', 'border': 'US-Canada Border', 'value': 13, 'measure': 'Truck Containers Full'}
        # {'date': '06/01/2019 12:00:00 AM', 'border': 'US-Canada Border', 'value': 13, 'measure': 'Truck Containers Empty'}
        # {'date': '06/01/2019 12:00:00 AM', 'border': 'US-Canada Border', 'value': 13, 'measure': 'Buses'}
        # {'date': '06/01/2019 12:00:00 AM', 'border': 'US-Canada Border', 'value': 13, 'measure': 'Bus Passengers'}
        # {'date': '06/01/2019 12:00:00 AM', 'border': 'US-Mexico Border', 'value': 13, 'measure': 'Pedestrians'}
        # {'date': '06/02/2019 12:00:00 AM', 'border': 'US-Canada Border', 'value': 13, 'measure': 'Rail Containers Full'}
        # {'date': '06/02/2019 12:00:00 AM', 'border': 'US-Mexico Border', 'value': 13, 'measure': 'Personal Vehicle Passengers'}
        # {'date': '06/01/2019 12:00:00 AM', 'border': 'US-Canada Border', 'value': 13, 'measure': 'Trucks'}
        # {'date': '06/01/2019 12:00:00 AM', 'border': 'US-Canada Border', 'value': 13, 'measure': 'Personal Vehicles'}
        # {'date': '06/01/2019 12:00:00 AM', 'border': 'US-Canada Border', 'value': 13, 'measure': 'Rail Containers Empty'}
        # {'date': '04/01/2019 12:00:00 AM', 'border': 'US-Mexico Border', 'value': 13, 'measure': 'Personal Vehicles'}
        # {'date': '04/01/2019 12:00:00 AM', 'border': 'US-Canada Border', 'value': 13, 'measure': 'Personal Vehicles'}

        sorted_list = ba.sort_data(crossings_list)
        sorted_len = len(sorted_list)

        self.assertEqual(sorted_len, crossings_len, "Wrong sorted list length!")
        self.assertEqual(sorted_list[0], {'date': '06/02/2019 12:00:00 AM', 'border': 'US-Mexico Border', 'value': 13, 'measure': 'Personal Vehicle Passengers'}, "Sorting order is wrong!")
        self.assertEqual(sorted_list[1], {'date': '06/02/2019 12:00:00 AM', 'border': 'US-Canada Border', 'value': 13, 'measure': 'Rail Containers Full'}, "Sorting order is wrong!")
        self.assertEqual(sorted_list[2], {'date': '06/01/2019 12:00:00 AM', 'border': 'US-Canada Border', 'value': 13, 'measure': 'Bus Passengers'}, "Sorting order is wrong!")
        self.assertEqual(sorted_list[3], {'date': '06/01/2019 12:00:00 AM', 'border': 'US-Canada Border', 'value': 13, 'measure': 'Buses'}, "Sorting order is wrong!")
        self.assertEqual(sorted_list[4], {'date': '06/01/2019 12:00:00 AM', 'border': 'US-Mexico Border', 'value': 13, 'measure': 'Pedestrians'}, "Sorting order is wrong!")
        self.assertEqual(sorted_list[5], {'date': '06/01/2019 12:00:00 AM', 'border': 'US-Canada Border', 'value': 13, 'measure': 'Personal Vehicles'}, "Sorting order is wrong!")
        self.assertEqual(sorted_list[6], {'date': '06/01/2019 12:00:00 AM', 'border': 'US-Canada Border', 'value': 13, 'measure': 'Rail Containers Empty'}, "Sorting order is wrong!")
        self.assertEqual(sorted_list[7], {'date': '06/01/2019 12:00:00 AM', 'border': 'US-Canada Border', 'value': 13, 'measure': 'Truck Containers Empty'}, "Sorting order is wrong!")
        self.assertEqual(sorted_list[8], {'date': '06/01/2019 12:00:00 AM', 'border': 'US-Canada Border', 'value': 13, 'measure': 'Truck Containers Full'}, "Sorting order is wrong!")
        self.assertEqual(sorted_list[9], {'date': '06/01/2019 12:00:00 AM', 'border': 'US-Canada Border', 'value': 13, 'measure': 'Trucks'}, "Sorting order is wrong!")
        self.assertEqual(sorted_list[10], {'date': '04/01/2019 12:00:00 AM', 'border': 'US-Canada Border', 'value': 13, 'measure': 'Personal Vehicles'}, "Sorting order is wrong!")
        self.assertEqual(sorted_list[11], {'date': '04/01/2019 12:00:00 AM', 'border': 'US-Mexico Border', 'value': 13, 'measure': 'Personal Vehicles'}, "Sorting order is wrong!")


        
    def test_calc_moving_avg(self):
        crossings_list = ba.load_data("../input/Border_Crossing_Entry_Data-TEST-CalcAverages.csv")
        
        sorted_list = ba.sort_data(crossings_list)
        sorted_len = len(sorted_list)

        avgs_list = ba.calc_moving_avg(sorted_list)
        avgs_len = len(avgs_list)

        # Test Set #3 after being sorted.
        # {'date': '11/01/2017 12:00:00 AM', 'border': 'US-Mexico Border', 'value': 4, 'measure': 'Truck Containers Empty'}
        # {'date': '10/01/2017 12:00:00 AM', 'border': 'US-Mexico Border', 'value': 15, 'measure': 'Truck Containers Empty'}
        # {'date': '10/01/2017 12:00:00 AM', 'border': 'US-Mexico Border', 'value': 8, 'measure': 'Personal Vehicles'}
        # {'date': '09/01/2017 12:00:00 AM', 'border': 'US-Canada Border', 'value': 38, 'measure': 'Personal Vehicles'}
        # {'date': '09/01/2017 12:00:00 AM', 'border': 'US-Mexico Border', 'value': 7, 'measure': 'Personal Vehicles'}
        # {'date': '09/01/2017 12:00:00 AM', 'border': 'US-Mexico Border', 'value': 2, 'measure': 'Truck Containers Empty'}
        # {'date': '08/01/2017 12:00:00 AM', 'border': 'US-Mexico Border', 'value': 1, 'measure': 'Truck Containers Empty'}
        # {'date': '03/01/2017 12:00:00 AM', 'border': 'US-Canada Border', 'value': 20, 'measure': 'Rail Containers Full'}
        # {'date': '02/01/2017 12:00:00 AM', 'border': 'US-Canada Border', 'value': 1, 'measure': 'Rail Containers Full'}
        # {'date': '01/01/2017 12:00:00 AM', 'border': 'US-Canada Border', 'value': 39, 'measure': 'Rail Containers Full'}
        
        self.assertEqual(sorted_len, avgs_len, "Wrong averages list length!")
        self.assertEqual(avgs_list[0]["average"], 8, "Average value is incorrect!")
        self.assertEqual(avgs_list[1]["average"], 1, "Average value is incorrect!")
        self.assertEqual(avgs_list[2]["average"], 7, "Average value is incorrect!")
        self.assertEqual(avgs_list[3]["average"], 0, "Average value is incorrect!")
        self.assertEqual(avgs_list[4]["average"], 0, "Average value is incorrect!")
        self.assertEqual(avgs_list[5]["average"], 1, "Average value is incorrect!")
        self.assertEqual(avgs_list[6]["average"], 0, "Average value is incorrect!")
        self.assertEqual(avgs_list[7]["average"], 20, "Average value is incorrect!")
        self.assertEqual(avgs_list[8]["average"], 39, "Average value is incorrect!")
        self.assertEqual(avgs_list[9]["average"], 0, "Average value is incorrect!")


if __name__ == '__main__':
    unittest.main()