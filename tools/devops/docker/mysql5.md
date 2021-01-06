## 安装Mysql5.7 

## 从Docker库中拉取镜像

`docker pull mysql:5`

### 拉取完之后，运行该镜像（**可以开启多个数据库服务，只要端口和名称不同就可以**）
```bash
docker run --name mysql5 -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123qwe. -d mysql:5 --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci --lower_case_table_names=1`

```
### 启动容器
```bash
docker start mysql5
docker stop mysql5
```

### 操作容器
```bash
# 进入容器内部: 
docker exec -it mysql5 bash
# 链接mysql: 
mysql -u root -p123qwe.
```


### 文件复制
```bash
# 把docker容器中的配置文件复制到主机中: 
docker cp mysql5:/etc/mysql/my.cnf F:/My/data/docker/mysql/conf/my.cnf

# 把主机中的配置文件复制到docker容器中: 
docker cp F:/My/data/docker/mysql/conf/my.cnf mysql5:/etc/mysql/my.cnf
```
