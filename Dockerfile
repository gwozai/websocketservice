# 使用 Python 官方的 Alpine 镜像作为基础镜像
FROM python:3.9-alpine

# 设置工作目录
WORKDIR /app

# 复制当前目录下的所有文件到容器的 /app 目录中
COPY . .

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 启动 WebSocket 服务器
CMD ["python", "main.py"]
