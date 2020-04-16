# Nginx
### 安装必要包
`yum -y install gcc zlib zlib-devel pcre-devel openssl openssl-devel`

### 下载Nginx
```
cd /usr/local
mkdir nginx
cd nginx/
wget http://nginx.org/download/nginx-1.13.7.tar.gz
tar -zxvf nginx-1.13.7.tar.gz 
cd nginx-1.13.7
./configure && make && make install
```
### 启动
`/usr/local/nginx/sbin/nginx`

### 重新加载服务
`/usr/local/nginx/sbin/nginx -s reload`

### 停止服务
`/usr/local/nginx/sbin/nginx -s stop`

### 查看nginx服务进程
`ps -ef | grep nginx`
