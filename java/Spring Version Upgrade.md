# Spring 版本升级

前提

1. JDK 升级到 1.8
2. Tomcat 升级到 8.5
   1. 使用get请求 并且参数中包含**特殊字符 |[]** 等, 需要进行 encodeURIComponent() 转义

## 配置

- ### pom.xml

```xml
<!-- 更新版本 -->
<spring.version>5.2.9.RELEASE</spring.version>
<jdk.version>1.8</jdk.version>
<validator.version>6.1.5.Final</validator.version>
<mybatis.version>3.5.5</mybatis.version>
<mybatis-spring.version>2.0.5</mybatis-spring.version>
<druid.version>1.1.24</druid.version>
<ehcache.version>2.6.11</ehcache.version>
<shiro.version>1.5.3</shiro.version>

<slf4j.version>1.7.30</slf4j.version>
<commons-lang3.version>3.10</commons-lang3.version>
<commons-codec.version>1.14</commons-codec.version>
<jackson.version>2.11.2</jackson.version>
<guava.version>29.0-jre</guava.version>
```

- ### spring-context-quartz.xml

修改前 location

```xml
<bean class="org.springframework.scheduling.quartz.SchedulerFactoryBean">
		<property name="triggers">
			<list>
				<!-- 采购管理_修正月销量变化提醒, 该表数据由夜间Batch在每个月第一个周二（凌晨0点）生成 -->
			    <ref location="cronServiceProductMonthlySalesModifyRemind"/>
		    	<!-- 采购合同交期提前推迟提醒 -->
			    <ref location="cronServiceProductContractDeliveryDateChangedRemind"/>
				<!-- 实验室提醒 -->
			    <ref location="cronServiceUseTestResult"/>
				<!-- 每周五17:00发送任务提醒计划员，计划经理，叶凯宇查阅有效实物库存比例统计 -->
				<ref location="notifyCalculateEffectStockTaskBean"/>
            </list>
    </property>
</bean>	
```

修改后 bean

```xml
<bean class="org.springframework.scheduling.quartz.SchedulerFactoryBean">
		<property name="triggers">
			<list>
			<!-- 采购管理_修正月销量变化提醒, 该表数据由夜间Batch在每个月第一个周二（凌晨0点）生成 -->
			    <ref bean="cronServiceProductMonthlySalesModifyRemind"/>
		    <!-- 采购合同交期提前推迟提醒 -->
			    <ref bean="cronServiceProductContractDeliveryDateChangedRemind"/>
			<!-- 实验室提醒 -->
			    <ref bean="cronServiceUseTestResult"/>
			<!-- 每周五17:00发送任务提醒计划员，计划经理，叶凯宇查阅有效实物库存比例统计 -->
			<ref bean="notifyCalculateEffectStockTaskBean"/>
            </list>
    </property>
</bean>	
```


## 代码

- ### `UserfilesDownloadServlet#fileOutputStream`

```java
// 修改前
try {
	filepath = UriUtils.decode(filepath, "UTF-8");
} catch (UnsupportedEncodingException e1) {
	logger.error(String.format("解释文件路径失败，URL地址为%s", filepath), e1);
}

// 修改后
// try {
		filepath = UriUtils.decode(filepath, "UTF-8");
// } catch (UnsupportedEncodingException e1) {
//		logger.error(String.format("解释文件路径失败，URL地址为%s", filepath), e1);
// }
```

- ### **静态资源被拦截**: 注册拦截器时 需要过滤到静态资源路径 

```java
/**
 * 配置静态访问资源
 * @param registry
 */
@Override
public void addResourceHandlers(ResourceHandlerRegistry registry) {
    //  只配置这个 访问会被拦截
    registry.addResourceHandler("/**").addResourceLocations("file:" + basedir + File.separator);
}

// 修改前
public void addInterceptors(InterceptorRegistry registry) {
    // 注册拦截器
    registry.addInterceptor(ipInterceptor).addPathPatterns("/**");
    registry.addInterceptor(authInterceptor).addPathPatterns("/**");
}

// 修改后
public void addInterceptors(InterceptorRegistry registry) {
	List<String> ignoreUrl = Arrays.asList("/crm/**", "/files/**");
    // 注册拦截器
    registry.addInterceptor(ipInterceptor).addPathPatterns("/**").excludePathPatterns(ignoreUrl);
    registry.addInterceptor(authInterceptor).addPathPatterns("/**").excludePathPatterns(ignoreUrl);
}
```

- **MetaObject.forObject**(animal, new DefaultObjectFactory(), new DefaultObjectWrapperFactory(), new DefaultReflectorFactory());
- builderAssistant.useNewCache(typeClass, evictionClass, flushInterval, size, readWrite,**false**, props);
- org.apache.ibatis.scripting.LanguageDriverRegistry#setDefaultDriverClass(Class<**? extends LanguageDriver**> defaultDriverClass)



## 外部化配置



## 其他问题







# Spring Boot 版本升级

## 配置

- pom.xml

```xml
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>2.2.10.RELEASE</version>
    <relativePath/> <!-- lookup parent from repository -->
</parent>


<!-- upgrade -->
<pagehelper.version>1.3.0</pagehelper.version>
<mysql-connector.version>5.1.48</mysql-connector.version>
<jedis.version>2.9.0</jedis.version>

<!-- spring boot 2.2.10.RELEASE 默认的 mysql 版本是8.0 -->
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
    <version>${mysql-connector.version}</version>
</dependency>
```

- ### 配置文件

  - #### 应用上下文

  ```yaml
  # 修改前
  server:
    application-display-name: ProjectTemplate-Web
    context-path: /project
  # 修改后
  server:
    servlet:
      application-display-name: ProjectTemplate-Web
      context-path: /project
  ```

  - #### 文件上传

  ```yaml
  # 修改前
  spring:
    http:
      multipart:
        location: E:/home/data  #文件临时目录
        max-request-size: 40MB
        max-file-size: 40MB
  # 修改后
  spring:
     servlet:
       multipart:
         location: E:/home/data # 文件临时目录
         max-request-size: 40MB
         max-file-size: 40MB
  ```

  - #### mysql

  ```yaml
  # 修改前
  spring:
     datasource:  
  	  url: jdbc:mysql://localhost:3306/database?...
  	  username: root
  	  password: root
  	  type: com.alibaba.druid.pool.DruidDataSource
  	  driver-class-name: com.mysql.cj.jdbc.Driver
  # 修改后
   spring:
     datasource:  
        druid:
           url: jdbc:mysql://localhost:3306/database?...
           username: root
           password: root
           db-type: com.alibaba.druid.pool.DruidDataSource
           driver-class-name: com.mysql.cj.jdbc.Driver
  ```
  - #### redis

  ```yaml
  # 修改前
  spring:
    redis:   # REDIS (RedisProperties)
      database: 0
      host: 127.0.0.1
      port: 6379
      timeout: 2000
      pool:
        max-active: 8
        max-wait: -1
        max-idle: 8
        min-idle: 0
  # 修改后
  spring:
     redis:   # REDIS (RedisProperties)
       database: 0
       host: 127.0.0.1
       port: 6379
       timeout: 2000
       jedis:
         pool:
           max-idle: 8
           max-wait: -1
  ```
  





## 代码

- DispatcherServletAutoConfiguration

org.springframework.boot.autoconfigure.web.DispatcherServletAutoConfiguration 

移动到

org.springframework.boot.autoconfigure.web.servlet.DispatcherServletAutoConfiguration

- **WebMvcConfigurerAdapter** 在 spring 5.0  中标记删除  

推荐 实现 **WebMvcConfigurer**。继承 WebMvcConfigurationSupport  会出现 IllegalStateException: No ServletContext set 错误

- **PageHelper** 分页查询问题

如果不传递参数 新升级的默认查出的数据为空(总数是有值的)，解决办法 实体类中**添加默认值** pageNum = 1; pageSize = Integer.MAX_VALUE

- **配置文件中的属性以及`@ConfigurationProperties` 的`prefix`属性不在支持驼峰命名**

配置文件中的 所有**前缀** 必须是**小写(或加上 '-' 组合的)路径.** 最后的属性可以是 '-'连接, 开头小写的驼峰或者 '_'连接的字符 

```
例: spring.datasource.druid.erpweb.driverClassName
    1). 非法: 
        spring.dataSource.druid.erpweb.driverClassName, 
        spring.datasource.druid.erpWeb.driverClassName, 
        spring.data_source.druid.erpweb.driverClassName
    2). 合法: 
        spring.datasource.druid.erpweb.driverClassName, 
        spring.data-source.druid.erpweb.driverClassName, 
        spring.data-source.druid.erp-web.driverClassName, 
        spring.data-source.druid.erp-web.driver-class-name, 
```

- TomcatEmbeddedServletContainerFactory 修改为 ServletWebServerFactory
- JsonMapper 中 对于**空值**的字段 序列化时 使用 **Include.ALWAYS** 返回数据(前端可以接收到该字段,不然会出现 undefined 错误)
- **静态资源被拦截**: 注册拦截器时 需要过滤到静态资源路径  (参照 Spring 升级中的方法)

## 外部化配置

- –spring.config.location 修改为 --spring.config.additional-location

## 其他问题

- ### druid-spring-boot-starter 低版本报错 升级为1.1.10版本即可

- ### SpringSecurity

  - AuthenticationManager 异常：

  ```
  A component required a bean of type 'org.springframework.security.authentication.AuthenticationManager' that could not be found
  ```

  在 SpringSecurity 文件中重写即可

  ```java
  @Bean(name = BeanIds.AUTHENTICATION_MANAGER)
  @Override
  public AuthenticationManager authenticationManagerBean() throws Exception {
  	return super.authenticationManagerBean();
  }
  ```

  - userDetailsServiceImpl

  ```
  The bean 'userDetailsServiceImpl', defined in class path resource [com/itmacy/dev/auth/security/SecurityConfig.class], could not be registered. A bean with that name has already been defined in file [/Users/chenmeixuan/macy/dev/project/study/webBack/project-template/target/project-template-1.0.0-SNAPSHOT_20200215-1336/classes/com/itmacy/dev/auth/security/UserDetailsServiceImpl.class] and overriding is disabled.
  ```

  在yml文件中添加以下配置即可

  ```yaml
  spring:
     main:
       allow-bean-definition-overriding: true
  ```
