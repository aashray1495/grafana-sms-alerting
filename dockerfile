#Dated 03/31/2020-DIGEST:sha256:9d43bebe9f3a5d27647231e1fa760644fafcc09a1ad85eeae1df40c491841bd9
# FROM python:alpine AS dashboard-generator


FROM grafana/grafana
USER root
# RUN chown -R grafana:grafana "$GF_PATHS_PROVISIONING" && chmod 777 "$GF_PATHS_PROVISIONING"
# # USER grafana
# RUN chmod -R 777 /media
RUN apk add py-pip python3-dev

RUN pip install grafanalib && \
pip install flask && \
pip install boto3
COPY sendsms.py /var/lib/grafana/
#ENTRYPOINT [ "python", "/usr/share/grafana/sendsms.py" ]

# CMD python /media/sendsms.py
