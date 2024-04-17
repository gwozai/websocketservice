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


#
