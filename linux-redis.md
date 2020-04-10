# Redis

### 下载 (http://download.redis.io/releases)
```
cd /usr/local
wget http://download.redis.io/releases/redis-5.0.8.tar.gz
tar -zvxf redis-5.0.8.tar.gz
cd redis-5.0.8
make
make PREFIX=/usr/local/redis-5.0.8 install
```

### 修改配置文件
`vi /usr/local/redis-5.0.8/redis.conf`
#### 后台进程启动
> `daemonize  yes`
#### 密码
> `requirepass 123qwe.`
#### 注释 ip限制
> `bind 127.0.0.1`

### 启动
`/usr/local/redis-5.0.8/bin/redis-server usr/local/redis-5.0.8/redis.conf`

### 停止
`/usr/local/redis-5.0.8/bin/redis-cli shutdown`

### 查看Redis是否正在运行
`ps -aux | grep redis`
