import os
import time
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
from http import HTTPStatus
import psycopg2
from psycopg2.extras import RealDictCursor




password = os.getenv('DB_PASSWORD')

while True:

    try:
        connect = psycopg2.connect(host = 'localhost',
                                database='apidb', 
                                user='alex',
                                password=password,
                                cursor_factory=RealDictCursor)
        cursor = connect.cursor()
        print("Database connection was succesfull")

        break

    except Exception as error:
        print("Connecting to database failed")
        print("Error: ", error)
        time.sleep(3)

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None



for p in range(44):
    insert_title = 'DUMMY-TITLE'
    insert_content= 'DUMMY-CONTENT'

    my_model = {
    "title": f'insert_title ' + str(p),
    "content": f'insert_content ' + str(p),
}
    

    cursor.execute(""" INSERT INTO   posts (title, content)
                   VALUES (%s, %s) RETURNING * """,(insert_title, insert_content))
    new_post = cursor.fetchone()
    connect.commit()