
## 拦截器（版本2.0 及以上）

```java
public class MDCInterceptor implements HandlerInterceptor {

    // 日志文件key
    public static final String TRACE_ID = "traceId";

    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
        MDC.put(TRACE_ID, UUID.randomUUID().toString().replace("-", "").substring(0, 6));
        return true;
    }

    @Override
    public void postHandle(HttpServletRequest request, HttpServletResponse response, Object handler, ModelAndView modelAndView) throws Exception {
    }

    @Override
    public void afterCompletion(HttpServletRequest request, HttpServletResponse response, Object handler, Exception ex) throws Exception {
        MDC.remove(TRACE_ID);
    }
}

@Configuration
public class MyWebMvcConfig implements WebMvcConfigurer {

    @Autowired
    MDCInterceptor mdcInterceptor;

    /**
     * 注册 MDCInterceptor 拦截器
     */
    @Override
    public void addInterceptors(InterceptorRegistry registry) {
        registry.addInterceptor(mdcInterceptor).addPathPatterns("/**"); //所有路径都被拦截
    }
}
```

# Springboot 配置相关
## log 相关配置（版本2.2）
```yaml
logging:
  file:
    # 文件大小最大 100MB
    max-size: 100Mb
    # 文件最长保存90天
    max-history: 90
  # 日志保存路径，默认日志名称为 spring.log；如果指定了 logging.file.name （可以用绝对路径）则，该配置失效
  path: E:/logs
  pattern:
    # 指定在控制面板输出的 log 信息格式
    console: "[%X{traceId}] %d{yyyy-MM-dd HH:mm:ss.SSS} [%thread] %-5level %logger: %msg%n"
    # 指定在文件中日志的输出格式
    file: "[%X{traceId}] %d{yyyy-MM-dd HH:mm:ss.SSS} [%thread] %-5level %logger: %msg%n"
    # 文件滚动更新机制
    rolling-file-name: ${LOG_FILE}.%d{yyyy-MM}.%i.log
  # 日志级别设置
  level:
    com.springboot.nousin: DEBUG
    com.atomikos: ERROR
```

## 外部配置（优先级高的会覆盖优先级低的配置）
> 如果指定了 profile 则：application-{profile}.properties/yml文件的优先级高于application.properties/yml配置

优先级：
1. 在jar包的同一目录下，建一个config文件夹，然后放置配置文件。
2. 在jar包的同一目录下，放置配置文件。
3. 在classpath下，建一个config文件夹，然后放置配置文件。
4. 在classpath下，放置配置文件。


## springboot 使用maven打jar， 执行Java -jar XXX.jar 提示 “XXX中没有主清单属性”
pom.xml中需要添加以下配置：
```xml
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
```

# YML
## 多行输入
```yaml
tang: >
  随便输入内容
  可以换行
```
