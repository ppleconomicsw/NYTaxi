Downlaod the NYTaxi Data from the below URL...
https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page

To automate the above download to local system  follow the below steps...

1. Clone the Repository 
https://github.com/ppleconomicsw/NYTaxi.git


python listOfFilestoDownload.py --sy 2021 --ey 2021 --sm 1 --em 2 > ../log/listOfFilestoDownload.log
 
python taxiDataDownload.py  > ../log/taxiDataDownload.log