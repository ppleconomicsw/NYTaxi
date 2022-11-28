import argparse
import os
from pathlib import Path
#from pyspark.sql import *


if __name__=='__main__':

    # spark = SparkSession.builder \
    #     .master("local") \
    #     .appName("Word Count") \
    #     .config("spark.some.config.option", "some-value") \
    #     .getOrCreate()

    for x in os.listdir("/home/oracle/play/taxi_data"):
        if x.endswith(".parquet"):
            # Prints only text file present in My Folder
            filename="/home/oracle/play/taxi_data/"+x
            file = Path(filename).stat().st_size
            print("Size of file is :", file, "bytes")
            print((file / 1024 / 1024))
            print(x+"----"+str(round(file/1024/1024)))
            #print("--------------------------------------------------------------------"+x)
           # df = spark.read.load(filename, format='parquet',header=True)
            #df.toPandas().to_csv("my.csv", sep=',', header=True, index=False)
            #df.write.csv(x)
