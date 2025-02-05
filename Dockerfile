FROM public.ecr.aws/docker/library/python:3.11.4-slim-bullseye

# Install os dependencies
RUN apt-get update && apt-get install -y curl

# Defining required environment variables
ENV POETRY_HOME="/opt/poetry"
ENV PATH="${PATH}:${POETRY_HOME}/bin"

ENV PYTHONDONTWRITEBYTECODE="1"
ENV PYTHONUNBUFFERED="1"
ENV PIP_NO_CACHE_DIR="off"
ENV PIP_DISABLE_PIP_VERSION_CHECK="on"
ENV PIP_DEFAULT_TIMEOUT="10"

# Change context folder to application
WORKDIR /usr/src/application

# Install poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Copy all source files
COPY . .

# Export poetry format to python standard
RUN poetry self add poetry-plugin-export 
RUN poetry export --without-hashes --format=requirements.txt > requirements.txt

# Install dependencies from standard python format
RUN pip install --no-cache-dir -r requirements.txt

# Start application with uvicorn
ENTRYPOINT ["opentelemetry-instrument", "python", "main.py"]
