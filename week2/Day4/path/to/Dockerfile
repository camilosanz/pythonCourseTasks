FROM python:3.10

WORKDIR /path/to

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./python-demo ./python-demo

CMD ["python", "./python-demo/app.py"]