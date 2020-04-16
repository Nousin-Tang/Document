## 安装Mysql5.7 
### 启动与停止Mysql5

```
docker start mysql5
docker stop mysql5
```

### 安装
#### 从Docker库中拉取镜像

`sudo docker pull mysql5`

#### 拉取完之后，运行该镜像（**可以开启多个数据库服务，只要端口和名称不同就可以**）

`sudo docker run -it --rm --name mysql5 -e MYSQL_ROOT_PASSWORD=123456 -p 3306:3306 -d hub.c.163.com/library/mysql:5.7.18`

#### 连接到mysql

进入容器：`sudo docker exec -it mysql5 "bash"`
链接：`mysql -uroot -p123456`

#### 使用navicat链接