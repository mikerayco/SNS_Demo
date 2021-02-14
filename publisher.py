import boto3


sns = boto3.client('sns')

topic_arn = 'SNS TOPIC ARN HERE'

response = sns.publish(
        TopicArn = topic_arn,
        Subject = 'Message from SNS',
        Message = 'Hello from SNS!'
    )
    
print(response)
