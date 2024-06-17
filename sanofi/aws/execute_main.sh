#!/bin/bash
echo "This is a file $1"
v=$1
echo "this is $v"
# python x_s3_transfer.py
aws s3 cp "s3://airflow-s3-bucket-sigmoid/code/$v" .
echo "File downloaded"
python $v
echo "file executed"