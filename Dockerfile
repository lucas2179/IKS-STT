FROM python:3.6
ENV PYTHONBUFFERED=1
COPY . /app
WORKDIR /app
 
RUN pip install -r requirements.txt
EXPOSE 8080
RUN ls

RUN chmod +x entrypoint.sh
CMD ["/bin/bash","entrypoint.sh"]