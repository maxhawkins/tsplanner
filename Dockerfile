FROM python:2.7

RUN wget https://github.com/google/or-tools/releases/download/v2016-04/Google.OrTools.python.examples.3574.tar.gz && \
	tar xvf Google.OrTools.python.examples.3574.tar.gz && \
	cd ortools_examples && \
	python setup.py install --user

COPY . /app
RUN cd /app && pip install -r requirements.txt

CMD ["python", "/app/server.py"]
