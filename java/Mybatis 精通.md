

# Mybatis 精通

[官方文档](https://mybatis.org/mybatis-3/zh/index.html)

## Mybatis 介绍

### 什么是 Mybatis

> MyBatis 是一款优秀的持久层框架，它支持自定义 SQL、存储过程以及高级映射。MyBatis 免除了几乎所有的 JDBC 代码以及设置参数和获取结果集的工作。MyBatis 可以通过简单的 XML 或注解来配置和映射原始类型、接口和 Java POJO（Plain Old Java Objects，普通老式 Java 对象）为数据库中的记录。



### 传统 JDBC 操作数据库

使用JDBC API 连接和访问数据库，一般分为以下5个步骤

(1)加载驱动程序

(2)建立连接对象

(3)创建Statement

(4)获得SQL语句的执行结果

(5)关闭建立的对象，释放资源

```java
public class MySQLDemo {
    public static void main(String[] args) throws Exception{
        // 加载数据库驱动程序，并实例化
        try{
            Class.forName("com.mysql.cj.jdbc.Driver");
        }catch (ClassNotFoundException cne){
            cne.printStackTrace();
        }
        String url = "jdbc:mysql://127.0.0.1:3306/test?&useSSL=false&serverTimezone=UTC";
        String sql = "SELECT * FROM t_user";
        try(
            // 通过 ServiceLoader 加载 java.sql.Driver 实现类驱动程序，这样他们可以被实例化。
            Connection conn = DriverManager.getConnection(url,"root","123456");
            Statement stmt = conn.createStatement();
            ResultSet rst = stmt.executeQuery(sql)
        ) {
            while (rst.next()) {
                System.out.println(rst.getInt(1) + "\t" + rst.getString(2) + "\t" + rst.getString(3));
            }
        } catch (SQLException se) {
            se.printStackTrace();
        }
    }
}
```







## Mybatis 架构

### 整体架构

![](https://www.processon.com/view/5832cf29e4b06bc83a41b68c)

<img src="https://img-blog.csdnimg.cn/20181105201946646.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjI5NTcxNw==,size_16,color_FFFFFF,t_70" style="zoom: 67%;" />

说明：

1. Mybatis 配置

   SqlMapConfig.xml，此文件作为mybatis的全局配置文件，配置了mybatis的运行环境等信息。

   mapper.xml文件即sql映射文件，文件中配置了操作数据库的sql语句。此文件需要在SqlMapConfig.xml中加载。

   SqlMapConfig.xml是mybatis的核心文件。mybatis将dao层与sql语句分离开来，虽然写的时候分离开来了，但是执行的时候还是要依靠sql语句，所以我们的sql语句写在Mapper.xml中。我们在加载核心的时候，会加载他下面的Mapper.xml，所以sql语句便会加载进去了。我们只需要在SqlMapConfig.xml中引入Mapper.xml就可以了，所以最后只需要加载SqlMapConfig.xml这一个核心配置文件。

2. 通过mybatis环境等配置信息构造SqlSessionFactory即会话工厂。工厂能帮我们去加载核心配置文件。加载了核心配置文件后就创建session,通过session可以对数据库进行操作。

3. 由会话工厂创建sqlSession即会话，操作数据库需要通过sqlSession进行。

4. Mybatis 底层自定义了Executor执行器接口操作数据库，Executor接口有两个实现，一个是基本执行器、一个是缓存执行器。Executor是执行者，我们不需要管，因为 Mybatis 已经为我们封装好了。mybatis直接执行sql语句。

5. Mapped Statement也是mybatis一个底层封装对象，它包装了mybatis配置信息及sql映射信息等。mapper.xml文件中一个sql对应一个Mapped Statement对象，sql的id即是Mapped statement的id。

6. Mapped Statement对sql执行输入参数进行定义，包括HashMap、基本类型、pojo，Executor通过Mapped Statement在执行sql前将输入的java对象映射至sql中，输入参数映射就是jdbc编程中对preparedStatement设置参数。

7. Mapped Statement对sql执行输出结果进行定义，包括HashMap、基本类型、pojo，Executor通过Mapped Statement在执行sql后将输出结果映射至java对象中，输出结果映射过程相当于jdbc编程中对结果的解析处理过程。

8. Mapped Statement是输入与输出中间过程中产生的一些对象，通过这些对象去访问数据库。

### 核心处理层



![](https://segmentfault.com/img/bVcK1eH)

#### 配置解析

在Mybatis初始化过程中，会加载mybatis-config.xml配置文件、映射配置文件以及Mapper接口中的注解信息，解析后的配置信息会形成相应的对象并保存到Configration对象中。之后，根据该对象创建SqlSessionFactory对象。待Mybatis初始化完成后，可以通过SqlSessionFactory创建SqlSession对象并开始数据库操作。

#### SQL解析与scripting模块

Mybatis实现的动态SQL语句，几乎可以编写出所有满足需要的SQL。

Mybatis中scripting模块会根据用户传入的参数，解析映射文件中定义的动态SQL节点，形成数据库能执行的sql语句。

#### SQL执行

SQL语句的执行涉及多个组件，其中比较重要的是Executor、StatementHandler、ParameterHandler和ResultSetHandler。Executor主要维护一级缓存和二级缓存，并提供事务管理的相关操作，它会将数据库相关操作委托给StatementHandler完成。StatementHandler首先通过ParameterHandler完成SQL语句的实参绑定，然后通过java.sql.Statement对象执行SQL语句并得到结果集，最后通过ResultSetHandler完成结果集映射，得到结果对象并返回。



<img src="https://img-blog.csdn.net/20180719211941654?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMyNjQ3ODkz/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70" style="zoom:50%;" />







## Mybatis 源码







## Mybatis - Spring 源码






## Mybatis - Springboot 源码



