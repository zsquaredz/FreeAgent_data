import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn as sklearn
import seaborn as sns

path = os.path.join(os.getcwd(), 'data', 'engagement_report.log')
log = open(path,'r')
line = log.readline()
log_data = {}
while line :
    #print line
    company = line.split(' ')[1]
    log_time = line.split(' ')[4]
    day = line.split(' ')[-1]
    #print "{},{},{}".format(company, log_time, day)




    line = log.readline()
log.close()
