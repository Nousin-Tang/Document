## 安装Kafka
### 启动与停止Kafka

```
docker start redis
docker stop redis
```

### 安装
#### 从Docker库中拉取镜像

```
# 获取 zookeeper
docker pull wurstmeister/zookeeper

# 获取 kafka
docker pull wurstmeister/kafka
```

#### 拉取完之后，运行该镜像（**可以开启多个数据库服务，只要端口和名称不同就可以**）

```
# 运行 zookeeper
docker run -d --name zookeeper -p 2181:2181 -v /etc/localtime:/etc/localtime wurstmeister/zookeeper
# 运行 kafka
docker run  -d --name kafka -p 9092:9092 -e KAFKA_BROKER_ID=0 -e KAFKA_ZOOKEEPER_CONNECT=本机IP地址:2181 -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://本机IP地址:9092 -e KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9092 -t wurstmeister/kafka
```


> -e KAFKA_BROKER_ID=0 在kafka集群中，每个kafka都有一个BROKER_ID来区分自己
>
> -e KAFKA_ZOOKEEPER_CONNECT=本机IP地址:2181/kafka 配置zookeeper管理kafka的路径本机IP地址:2181/kafka
>
> -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://本机IP地址:9092 把kafka的地址端口注册给zookeeper
>
> -e KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9092 配置kafka的监听端口
>
> -v /etc/localtime:/etc/localtime 容器时间同步虚拟机的时间

`docker run -p 6379:6379 -d --name redis redis:5.0.5 redis-server  --appendonly yes`

* `redis-server –appendonly yes` : 在容器执行redis-server启动命令，并打开redis持久化配置

#### 连接到Redis
进入容器：`docker exec -it redis redis-cli`