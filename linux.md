# Linux 常用命令

## ==iptables== 开启防火墙端口号

### 查看开放的端口号
```
iptables -L -n
```

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
```
service iptables save
```
