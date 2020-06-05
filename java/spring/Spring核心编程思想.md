# Spring 核心编程思想

[TOC]

## 第一章：Spring Framework 总览
### 课前准备
### Spring 特性总览
### Spring 版本特性
### Spring 模块化设计
### Spring 对 Java 语言特性运用
### Spring 对 JDK API 实践
### Spring 对 Java EE API 整合
### Spring 编程模型
### Spring 核心价值
### 面试题精选

## 第二章：重新认识 IoC
### IoC 发展简介
### IoC 主要实现策略
### IoC 容器的职责
### IoC 容器的实现
### 传统 IoC 容器实现
### 轻量级 IoC 容器
### 依赖查找 VS. 依赖注入
### 构造器注入 VS. Setter 注入
### 面试题精选

## 第三章：Spring IoC 容器概述
### Spring IoC 依赖查找
### Spring IoC 依赖注入
### Spring IoC 依赖来源
### Spring IoC 配置元信息
### Spring IoC 容器
### Spring 应用上下文
### 使用 Spring IoC 容器
### Spring IoC 容器生命周期
### 面试题精选

## 第四章：Spring Bean 基础
### 定义 Spring Bean
### BeanDefinition 元信息
### 命名 Spring Bean
### Spring Bean 的别名
### 注册 Spring Bean
### 实例化 Spring Bean
### 初始化 Spring Bean
### 延迟初始化 Spring Bean
### 销毁 Spring Bean
### 垃圾回收 Spring Bean
### 面试题精选

## 第五章：Spring IoC 依赖查找
### 依赖查找的今世前生
### 单一类型依赖查找
### 集合类型依赖查找
### 层次性依赖查找
### 延迟依赖查找
### 安全依赖查找
### 内建可查找的依赖
### 依赖查找中的经典异常 
### 面试题精选

## 第六章：Spring IoC 依赖注入
### 依赖注入的模式和类型
### 自动绑定(Autowiring)
### 自动绑定(Autowiring)模式
### 自动绑定(Autowiring)限制和不足
### Setter 方法依赖注入
### 构造器依赖注入
### 字段注入
### 方法注入
### 回调注入
### 依赖注入类型选择
### 基础类型注入
### 集合类型注入
### 限定注入
### 延迟依赖注入
### 依赖处理过程
### @Autowired 注入原理
### JSR-330 @Inject 注入原理
### Java通用注解注入原理
### 自定义依赖注入注解
### 面试题精选

## 第七章：Spring IoC 依赖来源
### 依赖查找的来源
### 依赖注入的来源
### Spring 容器管理和游离对象
### Spring BeanDefinition 作为依赖来源
### 单例对象作为依赖来源
### 非 Spring 容器管理对象作为依赖来源
### 外部化配置作为依赖来源
### 面试题精选

## 第八章：Spring Bean 作用域
### Spring Bean 作用域
### "singleton" Bean 作用域
### "prototype" Bean 作用域
### "request" Bean 作用域
### "session" Bean 作用域
### "application" Bean 作用域
### 自定义 Bean 作用域
### 课外资料
### 面试题精选

## 第九章：Spring Bean 生命周期
### Spring Bean 元信息配置阶段
### Spring Bean 元信息解析阶段
### Spring Bean 注册阶段
### Spring BeanDefinition 合并阶段
### Spring Bean Class 加载阶段
### Spring Bean 实例化前阶段
### Spring Bean 实例化阶段
### Spring Bean 实例化后阶段
### Spring Bean 属性赋值前阶段
### Spring Bean Aware接口回调阶段
### Spring Bean 初始化前阶段
### Spring Bean 初始化阶段
### Spring Bean 初始化后阶段
### Spring Bean 初始化完成阶段
### Spring Bean 销毁前阶段
### Spring Bean 销毁阶段
### Spring Bean 垃圾收集
### 面试题

## 第十章：Spring 配置元信息
### Spring 配置元信息
### Spring Bean 配置元信息
### Spring Bean 属性元信息
### Spring 容器配置元信息
### 基于 XML 文件装载 Spring Bean 配置元信息
### 基于 Properties 文件装载 Spring Bean 配置元信息
### 基于 Java 注解装载 Spring Bean 配置元信息
### Spring Bean 配置元信息底层实现
### 基于 XML 文件装载 Spring IoC 容器配置元信息
### 基于Java注解装载SpringIoC容器配置元信息
### 基于ExtensibleXMLauthoring扩展 Spring XML元素
### ExtensibleXMLauthoring扩展原理
### 基于Properties文件装载外部化配置
### 基于YAML文件装载外部化配置
### 面试题

## 第十一章：Spring 资源管理
### 引入动机
### Java 标准资源管理
### Spring 资源接口
### Spring 内建 Resource 实现
### Spring Resource 接口扩展
### Spring 资源加载器
### Spring 通配路径资源加载器
### Spring 通配路径资源扩展
### 依赖注入Spring Resource
### 依赖注入 ResourceLoader
### 面试题精选

## 第十二章：Spring 国际化
### Spring 国际化使用场景
### Spring 国际化接口
### 层次性 MessageSource
### Java 国际化标准实现
### Java 文本格式化
### MessageSource 开箱即用实现
### MessageSource 內建依赖
### 课外资料
### 面试题精选

## 第十三章：Spring 校验
### Spring 校验使用场景
### Validator 接口设计
### Errors 接口设计
### Errors 文案来源
### 自定义 Validator
### Validator 的救赎
### 面试题精选

## 第十四章：Spring 数据绑定
### Spring 数据绑定使用场景
### Spring 数据绑定组件
### Spring 数据绑定元数据
### Spring 数据绑定控制参数
### Spring 底层 Java Beans 替换实现
### BeanWrapper 的使用场景
### 课外资料
### DataBinder 数据校验
### 面试题精选

## 第十五章：Spring 类型转换
### Spring 类型转换的实现
### 使用场景
### 基于 JavaBeans 接口的类型转换
### Spring 內建 PropertyEditor 扩展
### 自定义 PropertyEditor 扩展
### Spring PropertyEditor 的设计缺陷
### Spring 3.0 通用类型转换接口
### Spring 內建类型转换器
### Converter 接口的局限性
### GenericConverter 接口
### 优化 GenericConverter 接口
### 扩展 Spring 类型转换器
### 统一类型转换服务
### ConversionService 作为依赖
### 面试题精选

## 第十六章：Spring 泛型处理
### Java 泛型基础
### Java 5 类型接口
### Spring 泛型类型辅助类
### Spring 泛型集合类型辅助类
### Spring 方法参数封装 - MethodParameter
### Spring 4.0 泛型优化实现 - ResolvableType
### ResolvableType 的局限性
### 面试题精选

## 第十七章：Spring 事件
## 第十八章：Spring 注解
## 第十九章：Spring Environment 抽象
## 第二十章：Spring 应用上下文生命周期
### Spring 应用上下文启动准备阶段
### IoC 底层容器（BeanFactory） 创建阶段
### IoC 底层容器（BeanFactory） 初始化阶段
### IoC 底层容器（BeanFactory） 自定义阶段
### IoC 底层容器（BeanFactory） 注册BeanProcessor阶段