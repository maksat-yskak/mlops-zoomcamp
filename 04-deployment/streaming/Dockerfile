FROM public.ecr.aws/lambda/python:3.9

RUN pip install pipenv 

COPY [ "Pipfile", "Pipfile.lock", "./" ]


# Ensure entrypoints is installed for Lambda
RUN pipenv install --system && pip install entrypoints databricks_cli

COPY [ "lambda_function.py", "./" ]

CMD [ "lambda_function.lambda_handler" ]