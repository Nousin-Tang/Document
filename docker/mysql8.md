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

`sudo docker run -it --rm --name mysql8 -e MYSQL_ROOT_PASSWORD=123qwe.T -p 3306:3306 -d mysql:8`

#### 连接到mysql

进入容器：`sudo docker exec -it mysql8 "bash"`
链接：`mysql -uroot -p123qwe.T`

#### 使用navicat链接

### 虚拟机与主机文件交换
把docker容器中的配置文件复制到主机中: `docker cp mysql8:/etc/mysql/mysql.conf.d/mysqld.cnf D:\mysql_conf`

把主机中的配置文件复制到docker容器中: `docker cp D:\mysql_conf mysql8:/etc/mysql/mysql.conf.d/mysqld.cnf`

### 忽略大小写问题设置
配置文件中追加:`lower_case_table_names=1`
