from flask import Flask, request
import boto3

APP = Flask(__name__)

CLIENT = boto3.client(
    "sns",
    aws_access_key_id="AKIAV7MYWKUS5XEZHQOB",
    aws_secret_access_key="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",
    region_name="us-east-1"
)


@APP.route('/sendsms', methods=['POST'])
def sendsms():
    message = request.json["message"]
    print(message)

    arn = 'arn:aws:sns:us-east-1:411026478373:data-Alert-Dev-2'

    response = CLIENT.publish(
        TopicArn=arn,
        Message=message,
        MessageAttributes={
            'AWS.SNS.SMS.SenderID':
            {
                'DataType': 'String',
                'StringValue': 'Grafana'
            }
        }
    )
    return response


APP.run()
