# Linux 常用命令

## `iptables` 开启防火墙端口号

### 查看开放的端口号
`iptables -L -n`

### 打开端口号
```
# iptable
iptables -I INPUT -ptcp --dport 端口号 -j ACCEPT
iptables -I OUTPUT -ptcp --dport 端口号 -j ACCEPT

# firewall
firewall-cmd --zone=public --add-port=9930/tcp --permanent
```

### 关闭端口号
```
# iptable
iptables -A INPUT -p tcp --drop 端口号 -j DROP
iptables -A OUTPUT -p tcp --dport 端口号 -j DROP

# firewall
firewall-cmd --zone=public --remove-port=9930/tcp --permanent
```

### 保存修改
```
# iptables
service iptables save

# firewall
firewall-cmd --reload
```

## 文件操作

### `rm` 命令
```
rm -rf /var/log/httpd/access
rm -f /var/log/httpd/access.log
```
> -r 就是向下递归，不管有多少级目录，一并删除; -f 就是直接强行删除，不作任何提示的意思

## 请求
`curl 127.0.0.1:8080/sys/user -X POST -d '{"start":0,"limit":20}' --header "Content-Type: application/json;language: 1; `

## 查看端口号占用情况
`netstat -pan | grep 8080`


## 发布 jar
```
# 输出日志到 /home/jar/xxx.log 中
nohup java -jar /home/jar/xxx.jar  > /home/jar/xxx.log 2>&1 &

# 不输出日志
nohup java -jar /home/jar/xxx.jar  > /dev/null 2>&1 &
```
