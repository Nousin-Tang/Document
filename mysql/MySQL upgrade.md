# Mysql 升级履历

## 8.0

[下载地址](https://dev.mysql.com/downloads/mysql/8.0.html)

[详细说明](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/news-8-0-11.html)

### 新特性

[官方文档](https://mysqlserverteam.com/whats-new-in-mysql-8-0-generally-available/)

1. NoSql存储

    Mysql从5.7 版本提供了NoSQL的存储功能,在8.0中这部分得到一些修改,不过这个在实际中用的极少

2. **隐藏索引**

    在8.0 中,索引可以被隐藏和显示，当一个索引隐藏时，它不会被查询优化器所使用。

    隐藏索引的特性对于性能调试非常有用。也就是说可以隐藏一个索引,然后观察对数据库的影响.如果性能下降,就说明这个索引是有效的,于是将其”恢复显示”即可;如果数据库性能看不出变化,说明这个索引是多于的,可以删掉了

    ![](https://img-blog.csdnimg.cn/20190730104257425.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5Nzg3MzY3,size_16,color_FFFFFF,t_70)

    隐藏一个索引的语法：

    ```mysql
    ALTER TABLE t ALTER INDEX i INVISIBLE;
    ```

    恢复显示该索引的语法是：

    ```mysql
    ALTER TABLE t ALTER INDEX i VISIBLE;
    ```

    当一个索引被隐藏时，我们可以从`show index`命令的输出汇总看出，该索引visible属性值为No

    > 当索引被隐藏时,他的内容仍然是和正常索引一样实时更新的,这个特性本身是专门为了优化调试而使用的,如果你长期隐藏一个索引,那还不如干掉,因为索引的存在会影响数据的插入\更新和删除功能

3. 设置持久化

    MySQL 8 新增了 SET PERSIST 命令：

    ```mysql
    SET PERSIST max_connections = 500;
    ```

    MySQL 会将该命令的配置保存到数据目录下的 mysqld-auto.cnf 文件中，下次启动时会读取该文件，用其中的配置来覆盖缺省的配置文件。

    `SET GLOBAL` 命令来更改只会临时生效。

4. **UTF-8 编码**

    从 MySQL 8 开始，数据库的缺省编码将改为 utf8mb4，这个编码包含了所有 emoji 字符。

5. 通用表表达式（Common Table Expressions）

    复杂的查询会使用嵌入式表，例如：

    ```mysql
    SELECT t1.*, t2.* FROM
    	 (SELECT col1 FROM table1) t1,
    	 (SELECT col2 FROM table2) t2;
    ```

    而有了 CTE，我们可以这样写：

    ```mysql
    WITH
    	 t1 AS (SELECT col1 FROM table1),
    	 t2 AS (SELECT col2 FROM table2)
    SELECT t1.*, t2.* 
    FROM t1, t2;
    ```

6. 性能

    MySQL 8.0 的速度要比 MySQL 5.7 快 2 倍。MySQL 8.0 在以下方面带来了更好的性能：**读/写工作负载、IO 密集型工作负载、以及高竞争（”hot spot”热点竞争问题）工作负载**。

    ![](https://static.oschina.net/uploads/space/2018/0420/014526_i6nC_2720166.png)

7. **JSON**：MySQL 8 大幅改进了对 JSON 的支持，添加了基于路径查询参数从 JSON 字段中抽取数据的 `JSON_EXTRACT()` 函数，以及用于将数据分别组合到 JSON 数组和对象中的 `JSON_ARRAYAGG()` 和 `JSON_OBJECTAGG()` 聚合函数。

8. **账户与安全**

    MySQL8.0创建用户和用户授权的命令需要分开执行

    ```mysql
    -- 创建用户
    create user 'root'@'%' identified by '123456'; 
    
    -- 用户授权【给予所有权限】
    grant all privileges on *.* to 'root'@'%';
    ```

    MySQL5.7创建用户和用户授权命令可以同时执行

    ```mysql
    grant all privileges on *.* to root@'%' identified by '123456'; flush privileges;
    ```

    角色管理

    MySQL8.0提供了角色管理的新功能，角色是一组权限的集合，角色也是一个用户，用角色去模拟用户，可以对角色去进行权限授权

    ```mysql
    -- 创建数据库
    create database mytest;
    
    -- 创建数据库表
    create table mytest.tl(id int)
     
    -- 创建一个角色【新创建出来的角色无任何权限】
    create role 'my_role';
     
    -- 给角色授予增、删、改的权限
    grant insert,update,delete on mytest.* to 'my_role';
     
    -- 创建一个用户
    create user 'user1' identified by '123456';
     
    -- 将角色授予给用户
    grant 'my_role' to 'user1';
     
    -- 显示用户权限
    show grants for 'user1';
     
    show grants for 'user1' using 'my_role';
    ```

9. 在mysql8之后,加密规则是caching_sha2_password。

    mysql8 之前的版本中加密规则是mysql_native_password。[参照修改成mysql8 之前的加密规则](https://blog.csdn.net/weixin_42403773/article/details/80602603)

### Springboot 升级 Mysql 8.0

1. pom 修改      

    ```xml
    <dependency>
    	<groupId>mysql</groupId>
    	<artifactId>mysql-connector-java</artifactId>
    	<version>8.0.16</version>
    </dependency>
    ```

    

2. 配置文件

    db-type：（变量和之前不一样）

    driverClassName： `com.mysql.cj.jdbc.Driver`（和之前不一样）

    url：需要加入`serverTimezone=UTC`以及`allowPublicKeyRetrieval=true`。或者设置全局默认时区`set global time_zone='+8:00';`也可以使用持久化的方式。

    ```yaml
    spring:
      datasource:
        druid:
          db-type: com.alibaba.druid.pool.DruidDataSource
          driverClassName: com.mysql.cj.jdbc.Driver
          url: jdbc:mysql://localhost:3306/dbblog?serverTimezone=UTC&allowMultiQueries=true&useUnicode=true&characterEncoding=UTF-8&useSSL=false&allowPublicKeyRetrieval=true
          username: root
          password: root
          initial-size: 5
          max-active: 20
          min-idle: 5
          max-wait: 60000
          pool-prepared-statements: true
          max-pool-prepared-statement-per-connection-size: 20
          time-between-eviction-runs-millis: 60000
          min-evictable-idle-time-millis: 300000
          #validation-query: SELECT 1 FROM DUAL
          test-while-idle: true
          test-on-borrow: false
          test-on-return: false
          stat-view-servlet:
            enabled: true
            url-pattern: /druid/*
            #login-username: admin
            #login-password: admin
          filter:
            stat:
              log-slow-sql: true
              slow-sql-millis: 1000
              merge-sql: false
            wall:
              config:
                multi-statement-allow: true
    ```

3. 有些字段变为关键字，目前发现的有：rank，为关键字

    更改方式：

    - 重新更改表字段、代码等，可以从根本解决问题，但是如果项目很大且已经部署，更改需要小心；

    - 用 "`" 这个符号将涉及到的关键字包起来。如：

