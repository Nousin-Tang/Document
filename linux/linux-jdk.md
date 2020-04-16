# JDK
### 创建文件夹
```
mkdir /usr/local/java/
cd /usr/local/java/
```
### 下载
` wget https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html`

### 解压
`tar -zxvf jdk-8u231-linux-x64.tar.gz`

### 修改profile文件 ： 
* 修改文件：`vim /etc/profile`

* 追加信息
    ```
    export JAVA_HOME=/usr/local/java/jdk1.8.0_231
    export JRE_HOME=${JAVA_HOME}/jre
    export CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib:$CLASSPATH
    export JAVA_PATH=${JAVA_HOME}/bin:${JRE_HOME}/bin
    export PATH=$PATH:${JAVA_PATH}
    ```
  
* 使之生效：`source /etc/profile`
