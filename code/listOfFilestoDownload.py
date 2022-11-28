
import argparse


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--sy', type=int, required=True)
    parser.add_argument('--ey', type=int, required=True)
    parser.add_argument('--sm', type=int, required=True)
    parser.add_argument('--em', type=int, required=True)
    args = parser.parse_args()

    start_url="https://d37ci6vzurychx.cloudfront.net/trip-data/fhvhv_tripdata_"

    with open("url_to_download.txt", "a") as file1:
        # Writing data to a file
        for year in range(args.sy, args.ey+1):
            for month in range(args.sm, args.em+1):
                month_year = str(year) + "-" + str(month).rjust(2, '0')
                full_url = start_url + month_year+".parquet"
                print(full_url)
                file1.write(full_url+"\n")




