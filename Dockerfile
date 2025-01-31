#base image official python
FROM python:3.9

#set working directory in container
WORKDIR /irismlapp

#copy the files from local direcoty to MLAPI at container, . MEANS ALL FILES IN THIS FOLDER

COPY . .


#install dependencies

RUN pip install --no-cache-dir -r requirements.txt

#expose a port

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "irismlapp.main:app", "--reload", "--host","0.0.0.0","--port", "8000"]
