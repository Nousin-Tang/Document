# Mysql8

## 获取镜像
```bash
docker pull mysql:8
```


## 运行镜像

```bash
docker run --name mysql8_4306 -p 4306:3306 -e MYSQL_ROOT_PASSWORD=123qwe. -d mysql:8 --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci --lower_case_table_names=1


docker run --name mysql8_4306 -p 4306:3306 -v F:/My/data/docker/mysql8_4306/data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=123qwe. -d mysql:8 --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci --lower_case_table_names=1
```
	
## 启动容器
```bash
docker start mysql8_4306
docker stop mysql8_4306
```

## 操作容器
```bash
# 进入容器内部: 
docker exec -it mysql8_4306 bash
# 链接mysql: 
mysql -u root -p123qwe.
```

## 文件复制
```bash
# 把docker容器中的配置文件复制到主机中: 
docker cp mysql8_4306:/etc/mysql/my.cnf F:/My/data/docker/mysql8_4306/conf/my.cnf

# 把主机中的配置文件复制到docker容器中: 
docker cp F:/My/data/docker/mysql8_4306/conf/my.cnf mysql8_4306:/etc/mysql/my.cnf
```


# 设置主从

## 主数据库

### 获取 Master 参数
```mysql
show master status

# --------------------------------------------------------------------------------------
# | File              | Position  | inlog_Do_DB | Binlog_Ignore_DB | Executed_Gtid_Set |
# --------------------------------------------------------------------------------------
# | mysql-bin.000001  | 156       |             |                  |                   |
# --------------------------------------------------------------------------------------
```


### 主服务器 my.cnf 配置
```properties
############ 主服务器 ############
############ my.cnf ############
# Copyright (c) 2017, Oracle and/or its affiliates. All rights reserved.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301 USA

#
# The MySQL  Server configuration file.
#
# For explanations see
# http://dev.mysql.com/doc/mysql/en/server-system-variables.html

[mysqld]
pid-file        = /var/run/mysqld/mysqld.pid
socket          = /var/run/mysqld/mysqld.sock
datadir         = /var/lib/mysql
secure-file-priv= NULL
lower-case-table-names = 1

# 主从复制-主机配置
# 主服务器唯一ID
server-id = 1
# 启用二进制日志
log-bin=mysql-bin
gtid_mode=ON
enforce-gtid-consistency=true


# Custom config should go here
!includedir /etc/mysql/conf.d/

```

## 从数据库


### 运行镜像

```bash
docker run --name mysql8_4307 -p 4307:3306 -e MYSQL_ROOT_PASSWORD=123qwe. -d mysql:8 --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci --lower_case_table_names=1


docker run --name mysql8_4307 -p 4307:3306 -v F:/My/data/docker/mysql8_4307/data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=123qwe. -d mysql:8 --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci --lower_case_table_names=1
```
	
### 启动容器
```bash
docker start mysql8_4307
docker stop mysql8_4307
```

### 操作容器
```bash
# 进入容器内部: 
docker exec -it mysql8_4307 bash
# 链接mysql: 
mysql -u root -p123qwe.
```

### 文件复制
```bash
# 把docker容器中的配置文件复制到主机中: 
docker cp mysql8_4307:/etc/mysql/my.cnf F:/My/data/docker/mysql8_4307/conf/my.cnf

# 把主机中的配置文件复制到docker容器中: 
docker cp F:/My/data/docker/mysql8_4307/conf/my.cnf mysql8_4307:/etc/mysql/my.cnf
```


### 连接 master 服务器 （MASTER_LOG_FILE，MASTER_LOG_POS 通过主库 show master status 获取）

```mysql
# 连接主库
CHANGE MASTER TO MASTER_HOST='IP地址', MASTER_PORT=4306, MASTER_USER='root', MASTER_PASSWORD='123qwe.',MASTER_LOG_FILE='mysql-bin.000001',  MASTER_LOG_POS=156;

# 开始同步
start slave;

# 若之前设置过同步，请先重置
stop slave;
reset slave;

# 若出现错误，则停止同步，重置后再次启动

# 查询Slave状态
show slave status\G

```

### 从服务器 my.cnf 配置
```properties
############ 从服务器 ############
############ my.cnf ############
# Copyright (c) 2017, Oracle and/or its affiliates. All rights reserved.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301 USA

#
# The MySQL  Server configuration file.
#
# For explanations see
# http://dev.mysql.com/doc/mysql/en/server-system-variables.html

[mysqld]
pid-file        = /var/run/mysqld/mysqld.pid
socket          = /var/run/mysqld/mysqld.sock
datadir         = /var/lib/mysql
secure-file-priv= NULL
lower-case-table-names = 1

# 主从复制-从机配置
# 从服务器唯一ID
server-id = 2
log-bin=slavebin
gtid_mode=ON
enforce-gtid-consistency=true


# Custom config should go here
!includedir /etc/mysql/conf.d/

```
