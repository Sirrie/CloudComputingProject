#!/bin/sh
s3cmd put process.py s3://Siyu_Bucket
cd ..
ssh -i project11.pem ubuntu@ec2-54-165-79-175.compute-1.amazonaws.com
cd project1_siyu
s3cmd get s3://wikipediatraf/201407-gz/pagecounts-20140701-000000.gz
s3cmd get s3://Siyu_Bucket/process.py
unzip pagecounts-20140701-000000.gz
python process.py
wc -l pagecounts-20140701-000000
wc -l processed-pagecounts-20140701.txt
quit
