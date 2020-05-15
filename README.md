# grafana-sms-alerting
Added feature to be able to send sms alerts to mobile phone using AWS SNS

Create sns topic and use arn in grafana alert notification

Name the notification channel
Select webhook
Use POST method
In URL: http://127.0.0.1:5000/sendsms?arn='your_arn_from_sns'
Click on Test
Check your mobile number linked to sns

You can also use phone_number using sendsms_number.py
URL: http://127.0.0.1:5000/sendsms?number='your_arn_from_sns'
or use topic directly using sendsms_topic.py where url will look like
URL: http://127.0.0.1:5000/sendsms

Inspired by https://medium.com/@sean_bradley/create-sms-alert-channel-using-a-custom-webhook-and-aws-sns-27e03d55524b
