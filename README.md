# Building Python Microservices with FastAPI

Build secure, scalable, and structured Python microservices from design concepts to infrastructure

## About

In python FastAPI is the fastest framework. It provides many in build features like swagger in build, default 404 json url for unknown urls, and it's easy to implement

## To View Endpoinds
To view all API endponts with swagger docs visit
```bash
<web-ip>/docs
# or
<domain>/docs

# e.g <localhost:8000>/docs
```

## Is Flask == FastAPI?

The answer is no. FastAPI doesnot event use Flask in the background also the analogue of build urls is quite similar but not the same

1. FastAPI does have jinja dependency pre-installed but it does not have itsdangerous and other similar dependencies

2. Flask uses it's in build WebServer FastAPI uses uvicorn out of the box. FastAPI can actually scale faster although this is a subject of exposure and skills. 

3. FastAPI comes with websockets installed which I assume comes with uvicorn but this is my opinion.

4. Access to urls is different but similar to Flask

5. FastAPI has some sintax from django like defination of models with which is also there in Flask.

6. In conclusion FastAPI is not Flask at all. They are all python frameworks

7. 