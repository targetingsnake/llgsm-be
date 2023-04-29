import uvicorn
from fastapi import FastAPI
import os, subprocess
from pexpect import pxssh

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/start")
async def server_start():
    output = execute_linux_cmd("./sdtdserver st")
    return {"message": f"Starting Server", "stdout": output}

@app.get("/stop")
async def server_stop():
    output = execute_linux_cmd("./sdtdserver sp")
    return {"message": f"Stopping Server", "stdout": output}

@app.get("/update")
async def server_update():
    output = execute_linux_cmd("./sdtdserver u")
    return {"message": f"Updating Server", "stdout": output}

@app.get("/status")
async def server_status():
    output = execute_linux_cmd("./sdtdserver dt")
    return {"message": f"Status of Server", "stdout": output}

@app.get("/test")
async def server_test():
    return {"message": f"Test Sucessfully"}

def execute_linux_cmd(cmd: str):
    try:
        temp = subprocess.Popen(cmd.split(" "), stdout=subprocess.PIPE)
        output = temp.communicate()[0].decode('utf-8').replace('\n', '')
    except Exception as e:
        output = f"Error occured: {e}"
    return output

if __name__ == '__main__':
    uvicorn.run(app, port=8000, host='0.0.0.0')
