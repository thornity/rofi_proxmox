FROM python:latest 

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /usr/app/src
COPY main.py ./

CMD ["python", "./main.py"]