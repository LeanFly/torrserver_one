# torrserver_one 在docker里开设一趟小姐姐的高速列车



搭建教程：

#### 基于命令行的搭建

拉取镜像：

使用的是 combos 构建的 python_node 镜像

```bash
docker pull combos/python_node:3.10_12
```

创建容器：

```bash
docker run -dit --name torrserver_one -e one_api="" -e torr_api="" combos/python_node:3.10_12
```

注意：这里需要配置 one_api、torr_api 两个环境变量。one_api是某one four one 的网址，torr_api是你搭建好的torrserver容器的ip和端口：`http://172.17.0.1:8090`

进入容器启动任务

使用下面这命令进入容器

```bash
docker exec -it torrserver_one bash
```

使用下面这行命令下载脚本，如果网络不好的话，可能需要一定的魔法，或者代理

```bash
curl -O https://raw.githubusercontent.com/LeanFly/torrserver_one/main/app.py
```



使用下面这行命令安装依赖

```bash
pip install requests bs4 fastapi uvicorn apscheduler
```

如果网速不好，可以使用下面这行命令

```bash
pip install requests bs4 fastapi uvicorn apscheduler -i https://pypi.mirrors.ustc.edu.cn/simple
```



使用下面这行命令启动任务

```bash
npm i pm2 -g && pm2 start app.py
```



查看以下日志

```bash
pm2 logs 0
```


好了启动成功，可以去torrsever管理界面查看任务了。


#### 基于群晖 Container Manager 套件的搭建

下载映像
![image](https://github.com/LeanFly/torrserver_one/assets/18253047/e415a2a5-2f80-4a92-9278-c9cd4581ae06)

![image](https://github.com/LeanFly/torrserver_one/assets/18253047/9cbc5455-bee7-4564-87e4-5859efcaf14c)


创建容器
![image](https://github.com/LeanFly/torrserver_one/assets/18253047/9265c745-1982-4ed8-9faa-ccec38a244c5)

![image](https://github.com/LeanFly/torrserver_one/assets/18253047/326180ae-174f-4df7-8c3b-0feb82620102)

![image](https://github.com/LeanFly/torrserver_one/assets/18253047/697dbd1a-0c65-450f-9f5f-08d542a2e193)
![image](https://github.com/LeanFly/torrserver_one/assets/18253047/9edf5a06-34e3-45ff-b622-f22ce6b1fe19)


开始配置任务

![image](https://github.com/LeanFly/torrserver_one/assets/18253047/2c7dfeeb-582d-4f04-903f-ac2e985a7e62)

![image](https://github.com/LeanFly/torrserver_one/assets/18253047/764f2a33-5065-4946-ae25-a5a1e5349c03)

![image](https://github.com/LeanFly/torrserver_one/assets/18253047/d05f41a9-6424-4f7d-a94a-2dca8f879597)

输入命令下载脚本，复制后右键粘贴回车

```bash
curl -O https://raw.githubusercontent.com/LeanFly/torrserver_one/main/app.py
```


输入命令安装依赖

```bash
pip install requests bs4 fastapi uvicorn apscheduler -i https://pypi.mirrors.ustc.edu.cn/simple
```



启动任务

```bash
npm i pm2 -g && pm2 start app.py
```
![image](https://github.com/LeanFly/torrserver_one/assets/18253047/df87495c-7af6-4158-b5a1-05f0bed8899f)


查看一下日志，看看运行状态

```bash
pm2 logs 0
```
![image](https://github.com/LeanFly/torrserver_one/assets/18253047/55d8643a-e4d6-4bbf-b92f-ae793e4188d0)



好了，运行成功。

搞定，收工~
