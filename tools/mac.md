## 强制退出应用程序
使用快捷键：`Command+Option+Esc` 来打开“强制退出应用程序”的窗口，然后选中你需要退出的程序，再点右下方的“强制退出”即可。


## 查案端口占用
```bash
# netstat命令
netstat -an | grep 8080

# lsof命令
lsof -i:8080
```


## 恢复原始 .base_profile 
### 编辑
```bash
vim ~/.base_profile
```
### 添加
```bash
export PATH=/bin:/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
```
### 生效
```bash
source ~/.base_profile
```