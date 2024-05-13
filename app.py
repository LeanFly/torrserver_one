
import json
import os
import requests
from bs4 import BeautifulSoup
from apscheduler.schedulers.background import BackgroundScheduler
from fastapi import FastAPI
import uvicorn


# 首先从环境变量里获取
host =  os.getenv("one_host")
torr_api = f"{os.getenv('torr_api')}/torrents"
# 如果获取不到就走默认值
host = host if host else "https://one.52378.fun"
torr_api = torr_api if os.getenv('torr_api') else "http://172.17.0.1/torrents"


def get_page_list() -> list:
    """ 从网站主页获取详情页，返回一个详情页链接的列表 """
    with requests.get(host) as req:
        if req.status_code != 200:
            return
    
    soup = BeautifulSoup(req.text, "html.parser")
    page_list = soup.findAll(name="a", attrs={"class": "thumbnail-link"})
    page_list = [host + i.get("href") for i in page_list]
    return page_list    

def get_magnet(url) -> str:
    """ 传入一个页面地址，获取该页的 magnet """
    with requests.get(url) as req:
        if req.status_code != 200:
            return
    
    soup = BeautifulSoup(req.text, "html.parser")
    try:
        magnet = soup.find(name="a", attrs={"class": "button is-primary is-fullwidth"}).get("href")
        return magnet
    except:
        return

def add_download(magnet: str):
    """ 传入 magnet 链接，访问 torrserver api，添加内容 """
    payloads = {
        "action": "add",
        "category": "",
        "data": "",
        "hash": "",
        "link": magnet,
        "poster": "",
        "save_to_db": True,
        "title": ""
    }
    payloads = json.dumps(payloads)
    with requests.post(torr_api, data=payloads) as req:
        print(req.json())

def main_handle():
    """ 最后的任务处理 """
    pages = get_page_list()
    if pages:
        for i in pages:
            try:
                magnet = get_magnet(i)
                
                add_download(magnet)
            except:
                continue


## 开始构建定时任务
scheduler = BackgroundScheduler()

scheduler.add_job(
    main_handle,
    "interval",
    hours=6
)

app = FastAPI()

@app.on_event("startup")
def job_on():
    job = scheduler.get_jobs()[0]
    print(job)

@app.on_event("shutdown")
def job_down():
    print("job removed")


if __name__ == "__main__":
    
    uvicorn.run(app="app:app", reload=True)
    
