# Mysql8 [官网](https://dev.mysql.com/downloads/mysql/)
### 下载、解压、目录重命名
```bash
cd /usr/local
wget https://cdn.mysql.com//Downloads/MySQL-8.0/mysql-8.0.19-linux-glibc2.12-x86_64.tar.xz
tar  -Jxvf  mysql-8.0.19-linux-glibc2.12-x86_64.tar.xz
mv mysql-8.0.19-linux-glibc2.12-x86_64 mysql8
```

### 先检查是否有mysql用户组和mysql用户,没有就添加有就忽略
```bash
# 检查mysql用户组和mysql用户
groups mysql
# 添加用户组和用户
groupadd mysql && useradd -r -g mysql mysql
```

### 创建mysql数据目录并修改权限
```bash
mkdir /home/mysql/data
chown mysql:mysql -R /home/mysql/data
chmod 750 /home/mysql/data/ -R
```

### 将/usr/local/mysql8/bin 目录添加到PATH变量中
```bash
export PATH=$PATH:/usr/local/mysql8/bin
```

### 拷贝 my.cnf 文件到 /etc 目录下

> 默认读取配置文件的顺序:
> 1. /etc/my.cnf
> 2. /etc/mysql/my.cnf
> 3. /usr/local/mysql/etc/my.cnf
> 4. ~/.my.cnf

### 初始化
```bash
/usr/local/mysql8/bin/mysqld --defaults-file=/etc/my.cnf --basedir=/usr/local/mysql8 --datadir=/home/mysql/data --user=mysql --initialize
# 从 /home/mysql/data/mysql.log 中获取 密码：root@localhost: FFXu+fiD44>+
```


### 启动
```bash
/usr/local/mysql8/bin/mysqld_safe --defaults-file=/etc/my.cnf &
```

### 进入 mysql
```bash
mysql -uroot -p
```


## 数据库操作
### 创建数据库
```mysql
CREATE DATABASE IF NOT EXISTS 数据库名 DEFAULT CHARACTER SET utf8mb4 DEFAULT COLLATE utf8mb4_general_ci;
```

### 数据库备份
```bash
/usr/local/mysql/bin/mysqldump -h IP地址 -u用户名 -p'密码' -R -E 数据库名 > /home/mysqlBak/数据库名_bak_`date +"%Y%m%d_%H%M%S"`.sql
```

### 数据库还原
```mysql
use 数据名; 
source /home/mysqlBak/xxx.sql;
```

## 创建用户
### 修改root用户密码
```mysql
ALTER USER 'root'@'localhost' IDENTIFIED with mysql_native_password BY '密码'; 
flush privileges;
```

### 新建用户
```mysql
CREATE USER '用户名'@'%' IDENTIFIED with mysql_native_password BY '密码'; 
FLUSH PRIVILEGES;
```

### 授权

授权所有数据库给用户（远程访问）
```mysql
GRANT ALL ON *.* TO '用户名'@'%';
flush privileges;
```

授权指定的数据库给用户（远程访问）
```mysql
GRANT ALL PRIVILEGES ON 数据库名.* TO '用户名'@'%';
flush privileges;
```

### 设置用户密码
```mysql
SET PASSWORD FOR '用户名'@'%' = PASSWORD('用户密码');
```



## 打开端口号
```bash
firewall-cmd --zone=public --remove-port=3306/tcp --permanent
firewall-cmd --reload
```

## my.cnf 文件内容
```properties

[mysql]
# 设置mysql客户端默认字符集
default-character-set=utf8mb4
[client]
port       = 3306
socket     = /tmp/mysql.sock
 
[mysqld]
port       = 3306
server-id  = 3306
user       = mysql
socket     = /tmp/mysql.sock
# 设置mysql的安装目录
basedir    = /usr/local/mysql8
# 设置mysql数据库的数据的存放目录
datadir    = /home/mysql/data
log-bin    = /home/mysql/data/mysql-bin
innodb_data_home_dir      =/home/mysql/data
innodb_log_group_home_dir =/home/mysql/data
#设置mysql数据库的日志及进程数据的存放目录
log-error =/home/mysql/data/mysql.log
pid-file  =/home/mysql/data/mysql.pid
# 服务端使用的字符集默认为8比特编码
character-set-server=utf8mb4
lower_case_table_names=1
autocommit =1
##################以上要修改的########################
skip-external-locking
key_buffer_size = 256M
max_allowed_packet = 1M
table_open_cache = 1024
sort_buffer_size = 4M
net_buffer_length = 8K
read_buffer_size = 4M
read_rnd_buffer_size = 512K
myisam_sort_buffer_size = 64M
thread_cache_size = 128
#query_cache_size = 128M
tmp_table_size = 128M
explicit_defaults_for_timestamp = true
max_connections = 500
max_connect_errors = 100
open_files_limit = 65535
 
binlog_format=mixed
 
binlog_expire_logs_seconds =864000
# 创建新表时将使用的默认存储引擎
default_storage_engine = InnoDB
innodb_data_file_path = ibdata1:10M:autoextend
innodb_buffer_pool_size = 1024M
innodb_log_file_size = 256M
innodb_log_buffer_size = 8M
innodb_flush_log_at_trx_commit = 1
innodb_lock_wait_timeout = 50
transaction-isolation=READ-COMMITTED
 
[mysqldump]
quick
max_allowed_packet = 16M
 
[myisamchk]
key_buffer_size = 256M
sort_buffer_size = 4M
read_buffer = 2M
write_buffer = 2M
 
[mysqlhotcopy]
interactive-timeout
```
