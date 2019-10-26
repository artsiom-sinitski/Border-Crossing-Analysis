#!/bin/bash
#!/bin/env python
#
# Use this shell script to compile (if necessary) your code and then execute it. Below is an example of what might be found in this file if your program was written in Python 3.7. If the system complains about 'python' not being recognized as executable program, investigate where your "$PYTHON" env variable is pointing to and use call it appropriately.
python ./src/border_analytics.py ./input/Border_Crossing_Entry_data.csv ./output/report.csv
