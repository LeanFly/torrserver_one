# torrserver_one 在docker里开设一趟小姐姐的高速列车

书接上回，在上一篇文章里，我们讲到，不用搭建emby、jellyfin，也不用搞什么qbittorrent、transmission、aria2等等下载器，只需要搭建一个Torrserver就可以构建起自己的流媒体服务器了。

现在，我们接着上一次的内容，弄一个好玩儿，而且好看的。


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

![image](assets/image-20240510175909-nc8rmat.png)


使用下面这行命令安装依赖

```bash
pip install requests bs4 fastapi uvicorn apscheduler
```

如果网速不好，可以使用下面这行命令

```bash
pip install requests bs4 fastapi uvicorn apscheduler -i https://pypi.mirrors.ustc.edu.cn/simple
```

![image](assets/image-20240510175849-f5g9vsv.png)


使用下面这行命令启动任务

```bash
npm i pm2 -g && pm2 start app.py
```

![image](assets/image-20240510174056-fl75zmh.png)


查看以下日志

```bash
pm2 logs 0
```

![image](assets/image-20240510174132-umcfo36.png)

好了启动成功，可以去torrsever管理界面查看任务了。


#### 基于群晖 Container Manager 套件的搭建

下载映像

![image](assets/image-20240510174510-63j7oin.png)

![image](assets/image-20240510180049-oqfkqsw.png)

创建容器

![image](assets/image-20240510181656-jucup1y.png)

![image](assets/image-20240510181711-knqwu0i.png)

![image](assets/image-20240510181748-p5emof2.png)

![image](assets/image-20240510181855-joj86if.png)

开始配置任务


![image](assets/image-20240510181949-pldpb6j.png)


![image](assets/image-20240510182026-js4l0gi.png)

![image](assets/image-20240510182048-640l7gq.png)

输入命令下载脚本，复制后右键粘贴回车

```bash
curl -O https://raw.githubusercontent.com/LeanFly/torrserver_one/main/app.py
```

![image](assets/image-20240510182220-lk71ajc.png)

输入命令安装依赖

```bash
pip install requests bs4 fastapi uvicorn apscheduler -i https://pypi.mirrors.ustc.edu.cn/simple
```

![image](assets/image-20240510182548-rw4ipt2.png)

启动任务

```bash
npm i pm2 -g && pm2 start app.py
```

![image](assets/image-20240510182721-d3n65f7.png)

查看一下日志，看看运行状态

```bash
pm2 logs 0
```

![image](assets/image-20240510182809-uaib4o6.png)

好了，运行成功。

搞定，收工~
