# websocketservice
websocketservice


websocket做服务，

docker
docker run -e SERVER_ADDRESS=0.0.0.0 -e SERVER_PORT=8765 -e LOG_LEVEL=INFO gwozai/websocketserver:latest
docker run -e SERVER_ADDRESS=0.0.0.0 -e SERVER_PORT=8765 -e LOG_LEVEL=INFO -p 8765:8765 gwozai/websocketserver:latest

使用github action 自动打包镜像上传到github。
## 配置docker 仓库的变量
DOCKER_USERNAME 
DOCKER_USERNAME 
DOCKER_PASSWORD 

## 项目初始化
git clone
执行 [generate_requirements.bat](generate_requirements.bat) 文件，初始化项目
python server.py

## docker 部署
docker run -it -d -e SERVER_ADDRESS=0.0.0.0 -e SERVER_PORT=8765 -e LOG_LEVEL=INFO -p 8765:8765 gwozai/websocketserver:latest

mkdir websocketserver
vim start.sh
~~~
#!/bin/bash

# 定义容器名称
CONTAINER_NAME="websocket_server"

# 停止容器
docker stop $CONTAINER_NAME

# 删除容器
docker rm $CONTAINER_NAME

# 删除旧镜像
docker rmi gwozai/websocketserver:latest

# 拉取最新镜像
docker pull gwozai/websocketserver:latest

# 运行新容器
docker run -it -d -e SERVER_ADDRESS=0.0.0.0 -e SERVER_PORT=8765 -e LOG_LEVEL=INFO -p 8765:8765 --name $CONTAINER_NAME gwozai/websocketserver:latest
~~~
chmod 777 websocketserver
./start.sh
docker logs -f websocket_server

## 下一个项目
一个消息通知的应用，用webhook，  参考: 极简云来搭建