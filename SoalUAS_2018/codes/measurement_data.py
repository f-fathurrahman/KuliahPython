import numpy as np
import time
import requests

def gen_rand_data(minT, maxT, prec=50):
    deltaT = (maxT - minT)/prec
    return minT + (np.random.randint(1,prec+1)-1)*deltaT

while True:
    dat_T = gen_rand_data(30,50)
    print("Sending data by GET method ...")
    rec_str = "http://localhost:5000?data=" + str(dat_T)
    requests.get(rec_str)
    time.sleep(1.0)
