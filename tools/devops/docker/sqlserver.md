## 安装SqlServer
### 启动与停止Redis
```
docker start sqlserver
docker stop sqlserver
```

### 安装
#### 从Docker库中拉取镜像
`sudo docker pull microsoft/mssql-server-linux:2017-latest`

#### 运行该镜像（**可以开启多个数据库服务，只要端口和名称不同就可以**)
```
sudo docker run -e 'ACCEPT_EULA=Y' -e 'MSSQL_SA_PASSWORD=UnNous741953.t' \
    -p 1433:1433 --name sqlserver \
    -d microsoft/mssql-server-linux:2017-latest
```
#### 连接到SQL Server

 * 进入容器：`sudo docker exec -it sqlserver "bash"`
 * 链接：`/opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P 'UnNous741953.t'`

#### 使用navicat链接

### 还原数据库
#### 创建镜像sqlserver的文件目录
`sudo docker exec -it sqlserver mkdir /var/opt/mssql/backup`
#### 拷贝文件
`sudo docker cp CZSBGL3.bak sqlserver:/var/opt/mssql/backup`
#### 还原数据库
```
sudo docker exec -it sqlserver /opt/mssql-tools/bin/sqlcmd -S localhost \
    -U SA -P 'UnNous741953.t' \
    -Q 'RESTORE FILELISTONLY FROM DISK = "/var/opt/mssql/backup/CZSBGL3.bak"' \
        | tr -s ' ' | cut -d ' ' -f 1-2
```
#### 调用RESTORE DATABASE命令才能还原在容器内的数据库。 为每个文件上一步中指定新路径。
```
sudo docker exec -it sqlserver /opt/mssql-tools/bin/sqlcmd \
    -S localhost -U SA -P 'UnNous741953.t' \
    -Q 'RESTORE DATABASE CZSBGL3 FROM DISK = "/var/opt/mssql/backup/CZSBGL3.bak" \ 
    WITH MOVE "CZSBGL_NEW" TO "/var/opt/mssql/data/CZSBGL3.mdf", \
    MOVE "CZSBGL_NEW_log" TO "/var/opt/mssql/data/CZSBGL3.ldf"'
```
