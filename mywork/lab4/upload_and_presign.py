#!/usr/bin/env python3

import boto3
import requests

if __name__ == "__main__":
    bucket_name = 'ds2002-asg2rg'
    url = "https://i.pinimg.com/originals/57/61/5b/57615b8c0092a66c1d4058b1692955cc.gif"
#    url = "https://news.virginia.edu/sites/default/files/article_image/rotunda_night_summer_17_ss_header_5-2.jpg"
    local_file_name = "Walking.gif"
    object_name = 'uploaded_file.gif'
    expires_in = 604800

    # Download file
    r = requests.get(url, allow_redirects=True)
    open(local_file_name, 'wb').write(r.content)

    # Upload File to s3
    s3 = boto3.client('s3')
    file_content = open(local_file_name, 'rb').read()
    s3.put_object(
        Body = file_content,
        Bucket = bucket_name,
        Key = local_file_name,
        ACL = 'public-read',
        ContentType='image/gif'  
    )

    # Generate presigned url
    presign_url = s3.generate_presigned_url(
        'get_object',
        Params = {'Bucket': bucket_name, 'Key': object_name},
        ExpiresIn = expires_in
    )

    print("Presigned URL: ", presign_url)
