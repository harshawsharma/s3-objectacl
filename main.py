import boto3
import os

def lambda_handler(event, context):
    bucket_name=event['Records'][0]['s3']['bucket']['name']
    object_key=event['Records'][0]['s3']['object']['key']
    print (bucket_name, object_key)
    return(put_object_acl(bucket_name, object_key))


def put_object_acl(bucketname, objectkey):
    client = boto3.client('s3')
    response = client.put_object_acl(
        AccessControlPolicy=
        {
            "Grants": [
                {
                "Grantee": {
                    "ID": os.environ['AccountAID'],
                    "Type": "CanonicalUser"
                },
                "Permission": "FULL_CONTROL"
                },
                {
                "Grantee": {
                    "ID": os.environ['AccountBID'],
                    "Type": "CanonicalUser"
                },
                "Permission": "READ"
                },
                {
                "Grantee": {
                    "ID": os.environ['ELBAccountID'],
                    "Type": "CanonicalUser"
                },
                "Permission": "FULL_CONTROL"
                },
            ],
            'Owner': {
            'DisplayName': 'BucketOwnerAccountA',
            'ID': os.environ['ELBAccountID']
        }
        },
            Bucket=bucketname,
            Key=objectkey
    )
    return response

