FROM python:2.7

RUN curl -L https://github.com/google/or-tools/releases/download/v5.0/or-tools_python_examples_v5.0.3919.tar.gz | \
	tar xvzf - && \
	cd ortools_examples && \
	python setup.py install --user

COPY . /app
RUN cd /app && pip install -r requirements.txt

CMD ["python", "/app/server.py"]
