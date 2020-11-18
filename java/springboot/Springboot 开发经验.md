

# Springboot 配置相关
## log 相关配置
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
