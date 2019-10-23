"""
Border crossing analysis coding challenge
"""

from enum import Enum


class TransportMode(Enum):
    TRUCK = "Trucks"
    TRAIN = "Trains"
    BUS = "Buses"
    PV = "Personal Vehicles"
    TCF = "Truck Containers Full"
    TCE = "Truck Containers Empty"
    RCF = "Rail Containers Full"
    RCE = "Rail Containers Empty"
    TP = "Train Passengers"
    BP = "Bus Passengers"
    PEDESTRIAN = "Pedestrians"
    PVP = "Personal Vehicle Passengers"


def load_data():
    # read csv file
    print("load_data() =>")


def calcualate_totals():
    #calc totals
    print()


def calculate_avgs():
    #calc avg
    print()


def generate_report():
    #gen data report
    print()


if __name__ == '__main__':
    print('Border Corssing analysis resutls:')