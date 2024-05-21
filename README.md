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

The answer is no. FastAPI does not even use Flask in the background also the analogue of build urls is quite similar but not the same

1. FastAPI does have jinja dependency pre-installed but it does not have itsdangerous and other similar dependencies

2. Flask uses it's in build WebServer FastAPI uses uvicorn out of the box. FastAPI can actually scale faster although this is a subject of exposure and skills. 

3. FastAPI comes with websockets installed which I assume comes with uvicorn but this is my opinion.

4. Access to urls is different but similar to Flask

5. FastAPI has some sintax from django like defination of models with which is also there in Flask.

6. In conclusion FastAPI is not Flask at all. They are all python frameworks

7. The default ports are also different

## Similarities

While Flask is not FastAPI it does have dataclasses with can be used to convent it's models into serialized database models for API related queries for example

```python
class Product:
    id: int
    name: str
    price: float

    .....
    # Implementation condition as needed
```

Flask also uses gunicorn web-server in production which is a synchronous web server gateway unlike unicorn an asynchronous web-server possible of handling async request.

Mind you while theses are out of the box differences, and advanced developer can actually work around all these and make it quite similar though different but this will or might require extra time to add functionality which is already out of the box in another framework.