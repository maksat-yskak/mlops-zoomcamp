FROM python:3.10.9-slim

COPY [ "Pipfile", "Pipfile.lock", "batch.py", "model.bin", "./" ]

RUN pip install -U pip && pip install pipenv && pipenv install --system

ENTRYPOINT [ "python", "batch.py" ]