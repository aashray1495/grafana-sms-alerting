from flask import Flask, request
import boto3
import logging
import logging.handlers
app = Flask(__name__)




handler = logging.handlers.RotatingFileHandler(
        'log.txt',
        maxBytes=1024 * 1024)
logging.getLogger('werkzeug').setLevel(logging.DEBUG)
logging.getLogger('werkzeug').addHandler(handler)
app.logger.setLevel(logging.WARNING)
app.logger.addHandler(handler)

CLIENT = boto3.client(
    "sns",
    aws_access_key_id="your_access_key",
    aws_secret_access_key="your_secret_access_key",
    region_name="us-east-1"
)


@app.route('/sendsms', methods=['POST'])
def sendsms():
    arn = request.args.get('arn')
    print(arn)
    message = request.json["message"]
    print(message)

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

if __name__ == "__main__":
    app.run()
