## 安装Redis
### 启动与停止Redis

```
docker start redis
docker stop redis
```

### 安装
#### 从Docker库中拉取镜像

`sudo docker pull redis`

#### 拉取完之后，运行该镜像（**可以开启多个数据库服务，只要端口和名称不同就可以**）

`docker run -p 6379:6379 -d --name redis redis:5.0.5 redis-server  --appendonly yes`

* `redis-server –appendonly yes` : 在容器执行redis-server启动命令，并打开redis持久化配置

#### 连接到Redis
进入容器：`docker exec -it redis redis-cli`
