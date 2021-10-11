### 打包(跳过单元测试)
`mvn clean package -Dmaven.test.skip=true -P prod`

### 导入到本地仓库
`mvn clean install`

### jar包提交到远程仓库

#### maven setting.xml 中添加 server 配置
```xml
</servers>
  <server>    
    <id>nexus</id>    
    <username>${username}</username>    
    <password>${password}</password>    
  </server>  
</servers>
```
#### 镜像中添加私服地址
```xml
<mirrors>
  <mirror>
    <id>nexus</id>
    <name>private-maven</name>
    <url>http://${host}:${port}/repository/maven-releases/</url>
    <mirrorOf>central</mirrorOf>
  </mirror>
</mirrors>
```

#### 项目中添加私服地址
```xml
<project>
  <repositories>
    <!--阿里云代理-->
    <repository>
      <id>aliyun</id>
      <name>aliyun</name>
      <url>http://maven.aliyun.com/nexus/content/groups/public</url>
    </repository>

    <repository>
      <id>nexus</id><!--repository里的id需要和第一步里的server id名称保持一致-->
      <name>private-maven</name>
      <url>http://${host}:${port}/repository/maven-releases</url>
    </repository>
  </repositories>
	
  <distributionManagement>
    <repository>
      <id>nexus</id><!--repository里的id需要和第一步里的server id名称保持一致-->
      <name>private-maven</name><!--仓库名称-->
      <url>http://${host}:${port}/repository/maven-releases/</url><!--私服仓库地址-->
    </repository>
  </distributionManagement>
</project>
```
