
FROM python:3.7.13 as base

WORKDIR /carebear

COPY requirements.txt .

# installs libraries using this command
RUN pip install -r requirements.txt

COPY ./ .
# ADD main.py .

CMD ["python", "main.py"]