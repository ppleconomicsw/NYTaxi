from pyspark.sql import *

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Hiiiiii...  Spark.....')

    spark = SparkSession.builder \
        .master("local") \
        .appName("Word Count") \
        .config("spark.some.config.option", "some-value") \
        .getOrCreate()

    with open("url_to_download.txt") as fp:
        for line in fp:
            print(line[48:])
            filename="/home/oracle/data/taxi_data/"+line[48:]
            outfilename=line[48:70]
            df = spark.read.load(filename, format='parquet',header=True)
            df.write.csv(outfilename)







