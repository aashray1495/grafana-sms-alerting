from flask import Flask, request
import boto3

app = Flask(__name__)

CLIENT = boto3.client(
    "sns",
    aws_access_key_id="your_access_key",
    aws_secret_access_key="your_secret_access_key",
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


app.run()
