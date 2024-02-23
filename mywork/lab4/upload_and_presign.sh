#!/bin/bash

#Define Variables
FILE="uva_logo.png"
BUCKET="ds2002-asg2rg"

# Upload file to bucket
aws s3 cp $FILE s3://$BUCKET/

# Generate presign URL with expiration of 10 days
URL=$(aws s3 presign --expires-in 604800 s3://$BUCKET/$FILE)

# Display URL
echo "Presigned URL: $URL"
