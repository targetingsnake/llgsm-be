import uvicorn
from fastapi import FastAPI
import os, subprocess
from pexpect import pxssh

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/start/{server}")
async def say_hello(server: str):
    return {"message": f"Starting {server}"}

@app.get("/stop/{server}")
async def say_hello(server: str):
    return {"message": f"Stopping {server}"}

@app.get("/update/{server}")
async def say_hello(server: str):
    return {"message": f"Updating {server}"}

@app.get("/status/{server}")
async def say_hello(server: str):
    output = execute_linux_cmd("date")
    return {"message": f"Status of {server}", "Time": output}


def execute_linux_cmd(cmd: str):
    temp = subprocess.Popen([cmd], stdout=subprocess.PIPE)
    output = temp.communicate()[0].decode('utf-8').replace('\n', '')
    return output

if __name__ == '__main__':
    uvicorn.run(app, port=8000, host='0.0.0.0')