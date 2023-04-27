#using pydantic to create a schema
#purpose here is to use pydantic to design a data scheme that
#we would pass in an object and specify data as needed
#similar to graphql?

#benefits are error handling?

from pydantic import BaseModel

class Item(BaseModel):
    task: str


