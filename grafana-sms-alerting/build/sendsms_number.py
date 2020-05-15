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
    number = "+" + request.args.get('number')
    print(number)
    message = request.json["message"]
    print(message)

    response = CLIENT.publish(
        PhoneNumber=number,
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
