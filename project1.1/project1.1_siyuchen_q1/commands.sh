#!/bin/sh
s3cmd put process.py s3://Siyu_Bucket
s3cmd get s3://wikipediatraf/201407-gz/pagecounts-20140701-000000.gz
s3cmd get s3://Siyu_Bucket/process.py
gunzip pagecounts-20140701-000000.gz
echo running time: 
time python process.py
echo the number of lines before filtering
wc -l pagecounts-20140701-000000
echo the number of lines after filtering "(include one extra line)"
wc -l processed-pagecounts-20140701.txt
