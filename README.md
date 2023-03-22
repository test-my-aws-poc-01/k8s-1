# k8s-service-1

This repository is used for deploying microservice k8s-service-1. It is possible to use files from this directory to deploy service.

## Regex option

If you need to change the value of regex parameter, it's necessary to edit Simloudfile.yaml.
There are 2 possible options for regex value:
- true - for service, the regex rules will be applied based on the already set and specifically configured regex rules in Simloudfile.yaml. It could be a custom value that suits a cust>
- false - service will be deployed without any regex rules and according to already specified configuration in URL path.

Example of code block:

```
regex:
    enabled: false
    rewrite-target: /$2$3$4
````
```
regex:
    enabled: true
    rewrite-target: /$2$3$4
```
## Passing secrets from vault via simloid_ci.sh file

Follow these steps to output vault secrets through a simloud_ci.sh file in a Jenkins job:

Add the following commands to your simloud_ci file, where <path_to_secret> is a path to required secret in vault:

```sh
  username=$(vault kv get -field=username  <path_to_secret>)
  password=$(vault kv get -field=password  <path_to_secret>)
```
You can view the values by navigating to the job build output after building the service from the branch.

>NOTE: It is possible to provide custom steps using simloud_ci file.


## Additional options for cloud_resources block

>NOTE: It is possible to deploy k8s-service-1 with additional options for cloud_resources block in Simloudfile.yaml, such as `S3` and `SQS`.

For deploying **S3**, it is necessary to add following code snippet to `cloud_resources` block at Simloudfile.yaml:

```yaml
- name: s3_1
    env_name_prefix: S31l
    type: s3
    params:
     region: eu-west-1                    # also change region value in CreateBucketConfiguration: {LocationConstraint: some region}
     config:
       Bucket: some-unique-name983742398
       CreateBucketConfiguration:
         LocationConstraint: eu-west-1    # if you change value of region above, this one also must be changed
     static_hosting_config:
       Bucket: some-unique-name983742398
       WebsiteConfiguration:
         ErrorDocument:
           Key: error.html
         IndexDocument:
           Suffix: index.html
     policy_config:
       Bucket: some-unique-name983742398
       Policy: '{
       "Version": "2012-10-17",
       "Statement": [{
          "Sid": "PublicReadGetObject",
          "Effect": "Allow",
          "Principal": "*",
          "Action": "s3:GetObject",
          "Resource": "arn:aws:s3:::some-unique-name983742398/*"
       }]
}'
     tags_config:
       Bucket: some-unique-name983742398
       Tagging:
         TagSet:
           - Key: user_tag
             Value: user_value

```
S3 segment is parsed using the S3 module from the boto. More information <a href="https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.create_bucketz" target="_blank">here</a>.

For deploying **SQS**, it is necessary to add following code snippet to `cloud_resources` block at Simloudfile.yaml:

```yaml
 - name: sqs_1
    env_name_prefix: SQS1
    type: sqs
    params:
     QueueName: 2347918-43728.fifo        # If FifoQueue: True, the name of a FIFO queue can only include alphanumeric characters, hyphens, or underscores, must end with .fifo suffix a>
     # attrituptes must be strings -> ''
     Attributes:
       DelaySeconds: '5'                  # 0 to 900 seconds
       MaximumMessageSize: '2048'         # from 1,024 bytes (1 KiB) to 262,144 bytes
       MessageRetentionPeriod: '7200'     # from 60 seconds (1 minute) to 1,209,600 seconds
       Policy: '{
   "Version": "2012-10-17",
   "Id": "Policy2374982789374987",
   "Statement" : [{
      "Sid": "Stmt1345234234",
      "Effect": "Deny",
      "Principal": {
         "AWS": [
            "322219090568"
         ]
      },
      "Action": [
         "sqs:SendMessage",
         "sqs:ReceiveMessage"
      ],
      "Resource": "arn:aws:sqs:ap-southeast-1:322219090568:sqs_name1"
   }]
}'
       ReceiveMessageWaitTimeSeconds: '3' # from 0 to 20 (seconds)
       VisibilityTimeout: '300'           # from 0 to 43,200 (12 hours)
       FifoQueue: 'True'                  # If True, the name of a FIFO queue can only include alphanumeric characters, hyphens, or underscores, must end with .fifo suffix and be 1 to >
     tags:
       user_tag: user_value
```
SQS segment is parsed using the SQS module from the boto. More information <a href="https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.create_queue" target="_blank">here</a>.


You can see the snippets of code for deploying these services in [Simloudfile.yaml](https://gitlab.com/simloud-demo/k8s-service-2/-/blob/main/Simloudfile.yaml) in this repository or by the following <a href="https://prod--simloud-docs.netlify.app/en/examples-of-simloud-files/#creating-and-deploying-databases" target="_blank">link</a>.


**Additional documentation is placed by links:**
- [**"Simloudfile.yaml"**](https://prod--simloud-docs.netlify.app/en/simloudfile.yaml/)

- [**"How to use Simloud files"**](https://prod--simloud-docs.netlify.app/en/how-to-use-simloud-files/)

- [**"How to create and manage your SSH keys"**](https://stage--simloud-docs.netlify.app/en/getting-started/#managing-the-ssh-keys)

- [**"How to work with repositories"**](https://stage--simloud-docs.netlify.app/en/getting-started/#add-new-git-repositories-services)
