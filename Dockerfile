FROM python:2.7.16

ADD inversorRB_version2.py /

RUN pip install Pillow
RUN pip install numpy==1.16.2

CMD [ "python", "./inversorRB_version2.py" ]
