## Databases (FastAPI)

It's much easier to deal with databases from other frameworks like django, flask, spring-boot but not in FastAPI. This is beacuase it wants you to configure everything from scratch to allow easy handiver takeover. This procedure is very boring at first but very easy to follow

## Steps To Follow

0. install sqlalchemy
1. create an engine
2. create a model
3. create a serialize through BaseModel

__Note that we will use id int field instead of uuid becuase it's complicated with FastAPI