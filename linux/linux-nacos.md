# Nacos
### 下载
```
cd /usr/local
wget https://github.com/alibaba/nacos/releases/download/1.2.1/nacos-server-1.2.1.tar.gz
tar -zxvf nacos-server-1.2.1.tar.gz
cd /usr/local/nacos/bin
```
### 启动
`bash startup.sh -m standalone`
### 调整naming模块的naming-raft.log的级别为error:
`curl -X PUT 'localhost:8848/nacos/v1/ns/operator/log?logName=naming-raft&logLevel=error'`
### 调整config模块的config-dump.log的级别为warn:
`curl -X PUT 'localhost:8848/nacos/v1/cs/ops/log?logName=config-dump&logLevel=warn'`
### 查看Nacos服务进程
`ps -ef | grep nacos`
### 停止
`bash shutdown.sh`
