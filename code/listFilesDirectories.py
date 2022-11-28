import argparse
import os
from pathlib import Path
#from pyspark.sql import *
import subprocess

def runcmd(cmd, verbose = False, *args, **kwargs):

    process = subprocess.Popen(
        cmd,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
        text = True,
        shell = True
    )
    std_out, std_err = process.communicate()
    if verbose:
        print(std_out.strip(), std_err)
    pass



if __name__=='__main__':

    # spark = SparkSession.builder \
    #     .master("local") \
    #     .appName("Word Count") \
    #     .config("spark.some.config.option", "some-value") \
    #     .getOrCreate()
    dir="/home/oracle/data/taxi_data_csv"
    for df in os.listdir(dir):
        #if  os.path.isdir(dir+"/"+upperdir):
        if os.path.isdir(os.path.join(dir, df) ):
            for x in os.listdir(dir+"/"+df):
                fpath=os.path.join(dir, df,x)
                print(os.path.join(dir, df,x))
                files = Path(fpath).stat().st_size
                print("Size of file is :", files, "bytes")
                print((files / 1024 / 1024))
                print(x + "----" + str(round(files / 1024 / 1024)))
                if files>0 :
                    runcmd("scp "+fpath+" oracle@oradb:/mnt/volume_blr1_01/oradata/CDB1/pdb1/ext_data/.", verbose=True)
