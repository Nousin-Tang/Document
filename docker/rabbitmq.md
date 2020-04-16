## 安装RabbitMQ
### 启动与停止RabbitMQ

```
docker start rabbitmq
docker stop rabbitmq
```

### 安装
#### 从Docker库中拉取镜像

`sudo docker pull rabbitmq`

#### 拉取完之后，运行该镜像（**可以开启多个数据库服务，只要端口和名称不同就可以**）

`docker run -d --hostname my-rabbit --name rabbitmq -p 15672:15672 rabbitmq:management`

#### [登录](http://localhost:15672)
* 用户名和密码都guest

#### 连接到RabbitMQ
进入容器：`sudo docker exec -it mysql8 "bash"`
链接：`mysql -uroot -p123qwe.T`