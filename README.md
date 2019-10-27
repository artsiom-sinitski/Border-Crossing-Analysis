# Insight Data Engineering Program coding challenge

## Border Crossing Analysis application

### Table of Contents:
* [Description](https://github.com/artsiom-sinitski/Border-Crossing-Analysis#description)
* [Instructions](https://github.com/artsiom-sinitski/Border-Crossing-Analysis#instructions)
* [Running Tests](https://github.com/artsiom-sinitski/Border-Crossing-Analysis#running-tests)
* [Author](https://github.com/artsiom-sinitski/Border-Crossing-Analysis#author)
* [License](https://github.com/artsiom-sinitski/Border-Crossing-Analysis#license)

### Description
The Bureau of Transportation Statistics regularly makes available data on the number of vehicles, equipment, passengers and pedestrians crossing into the United States by land.

For this challenge, I needed to create an application that calculates the total number of times vehicles, equipment, passengers and pedestrians cross the U.S.-Canadian and U.S.-Mexican borders each month. Also, the app needs to calculate the running monthly average of total number of crossings for that type of crossing and border.

### Instructions

App requires [Python](https://www.python.org/downloads/) v3.7+ to run.

NOTE:
- To run the app in Windows environment `run.sh` shell script needs to execute
"python ..." line.
- To run the app in Unix environment `run.sh` shell script needs to execute "python3 ..." line.
Locate the run.sh script file in `<app_root_dir>`, uncomment the line appropriate for your environment and save the script file.

1) Put the csv file containing border crossings data inside the `<app_root_dir>/input/` folder.

2) Open up Terminal window and type:
```sh
$ cd <app_root_dir_path>
$ run.sh
```
3) The result of the app's execution will be "report.csv" file under the `<app_root_dir>/output/` folder.

### Running Tests
To run unit tests open up Terminal window and type:
```sh
$ cd <app_root_dir_path>\unit_tests\
$ run_unit_tests.sh
```

Author
---
Artsiom Sinitski
I can be reached via email: artsiom.vs@gmail.com

License
----
GPL
