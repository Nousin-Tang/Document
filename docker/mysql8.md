## 安装Mysql8
### 启动与停止Mysql8

```
docker start mysql8
docker stop mysql8
```

### 安装
#### 从Docker库中拉取镜像

`sudo docker pull mysql8`

#### 拉取完之后，运行该镜像（**可以开启多个数据库服务，只要端口和名称不同就可以**）

`sudo docker run -it --rm --name mysql8 -e MYSQL_ROOT_PASSWORD=123qwe.T -p 3306:3306 -d hub.c.163.com/library/mysql:8`

#### 连接到mysql

进入容器：`sudo docker exec -it mysql8 "bash"`
链接：`mysql -uroot -p123qwe.T`

#### 使用navicat链接