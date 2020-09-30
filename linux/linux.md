# Linux 常用命令

## `iptables` 开启防火墙端口号

### 查看开放的端口号
`iptables -L -n`

### 关闭端口号
```
iptables -A INPUT -p tcp --drop 端口号 -j DROP
iptables -A OUTPUT -p tcp --dport 端口号 -j DROP
```

### 打开端口号
```
iptables -I INPUT -ptcp --dport 端口号 -j ACCEPT
iptables -I OUTPUT -ptcp --dport 端口号 -j ACCEPT
```

### 保存修改
`service iptables save`

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
