from pickle import FALSE
from fastapi import FastAPI
from fastapi.responses import FileResponse, RedirectResponse
import json

file = open(r'myCake.txt', "r")
text = file.read().split('\n')
file.close()
print("TEXT",text)

st = {
    "office1":False,
    "office2":False,
    "office3":False,
    "office4":False
}

app = FastAPI()

@app.get("/")
def main():
    return FileResponse(r"index.html")

@app.get("/map")
def main():
    return FileResponse(r"img/map.png")

@app.get("/men")
def main():
    return FileResponse(r"img/men_icon.png")

@app.get("/pc")
def main():
    return FileResponse(r"img/pc_icon.png")

@app.get("/empty")
def mainx():
    file = open(r'myCake.txt', "r")
    text = file.read().split('\n')
    file.close()   
    print("TEXT",text)
    return text

@app.get("/open") #http://127.0.0.1:8000/open
def kopen():
    file = open(r"myCake.txt", 'w')
    file.write('0')
    file.close()
    print("Unbooked")

@app.get("/close") #http://127.0.0.1:8000/close
def kclose(o):
    st[f"office{str(o)}"]=not(st[f"office{str(o)}"])
    file = open(r"myCake.txt", 'w')
    file.write(json.dumps(st))
    file.close()
    print("Booked")
    return RedirectResponse("/")
