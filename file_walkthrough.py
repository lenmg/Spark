import os
import glob
# import psycopg2
import pandas as pd
# from sql_queries import *

def get_files(filepath):
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.py'))
        for f in files :
            all_files.append(os.path.abspath(f))

    return all_files


myfiles = get_files("C:\\Python")
print(myfiles)