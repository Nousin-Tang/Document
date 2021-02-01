# Springboot 动态扩展 Mybatis 数据源

## 注册 SqlSessionTemplateProcessor 动态扩展 Mybatis 数据源

```java

import com.nousin.sqlsession.framework.dao.DataSourceDao;
import com.nousin.common.pojo.dto.DataSourceDto;
import com.nousin.common.pojo.dto.SystemModifyDto;
import com.nousin.common.util.SpringUtils;
import com.nousin.common.util.SqlSessionTemplateUtils;
import lombok.extern.slf4j.Slf4j;
import org.apache.commons.collections.CollectionUtils;
import org.springframework.beans.factory.InitializingBean;
import org.springframework.stereotype.Component;

import java.util.LinkedHashSet;
import java.util.List;
import java.util.Set;

/**
 * 动态创建 SqlSessionTemplate;
 *
 * @author nousin
 * @since 2021/1/4
 */
@Slf4j
@Component
public class SqlSessionTemplateProcessor implements InitializingBean {

    /**
     * Mybatis mapper 地址
     */
    public static final String mapperLocations = "nousin.mybatis.locations";
    public static final String packagePath = "nousin.mybatis.package";
    
    // 数据源接口集合
    private static final Set<Class<?>> interfaces = new LinkedHashSet<>();

    @Override
    public void afterPropertiesSet() {
        // 扫描接口信息
        SqlSessionTemplateUtils.scanInterface(SqlSessionTemplateUtils.getProperty(packagePath), interfaces);
        // 加载 Bean
        process(new SystemModifyDto());
    }

    /**
     * 动态添加 SqlSessionTemplate
     */
    public void process(SystemModifyDto systemModifyDto) {

        // 获取数据源信息，并按照系统只读属性过滤用户
        List<DataSourceDto> dataSourceList = SpringUtils.getBean(DataSourceDao.class).listDataSources();
        if (CollectionUtils.isEmpty(dataSourceList)) {
            return;
        }
        // 扫描接口信息
        if (CollectionUtils.isEmpty(interfaces)) {
            SqlSessionTemplateUtils.scanInterface(SqlSessionTemplateUtils.getProperty(packagePath), interfaces);
        }
        // 处理 Bean 注册
        dataSourceList = SqlSessionTemplateUtils.processBeanRegistry(dataSourceList, SqlSessionTemplateUtils.getProperty(mapperLocations), interfaces, systemModifyDto);

        // 缓存已添加的系统
        SqlSessionTemplateUtils.loadCache(dataSourceList, systemModifyDto, SpringUtils.getBean(DataSourceDao.class).listLoadedDataSouceInfo());
    }
}
```

## 添加Dto

```java
package com.nousin.common.pojo.dto;

import com.vanew.trade.erp.common.util.SqlSessionTemplateUtils;
import lombok.Getter;
import lombok.Setter;

/**
 * 系统修改Dto
 * 自动加载SqlSessionTemplate等Bean使用
 *
 * @author nousin
 * @since 2021/1/8
 */
@Getter
@Setter
public class SystemModifyDto {
    String dataSourceName; // 数据源名称
    Integer modifyType = SqlSessionTemplateUtils.MODIFY_TYPE_ALL; // 修改类型【0-刷新所有，1-添加，2-修改，3-删除】
}
```

## 添加工具类【获取加载的数据源映射的Mybatis的Mapper接口】

```java
package com.nousin.common.util;

import com.nousin.common.constant.GlobalConstant;
import com.nousin.common.pojo.dto.SystemModifyDto;
import lombok.extern.slf4j.Slf4j;
import org.apache.commons.collections.CollectionUtils;
import org.apache.ibatis.session.SqlSessionFactory;
import org.mybatis.spring.SqlSessionFactoryBean;
import org.mybatis.spring.SqlSessionTemplate;
import org.mybatis.spring.boot.autoconfigure.SpringBootVFS;
import org.mybatis.spring.mapper.MapperFactoryBean;
import org.springframework.beans.factory.BeanDefinitionStoreException;
import org.springframework.beans.factory.support.DefaultListableBeanFactory;
import org.springframework.boot.jta.atomikos.AtomikosDataSourceBean;
import org.springframework.context.ApplicationContext;
import org.springframework.core.env.Environment;
import org.springframework.core.io.Resource;
import org.springframework.core.io.support.PathMatchingResourcePatternResolver;
import org.springframework.core.io.support.ResourcePatternResolver;
import org.springframework.core.type.ClassMetadata;
import org.springframework.core.type.classreading.CachingMetadataReaderFactory;
import org.springframework.core.type.classreading.MetadataReader;
import org.springframework.util.ClassUtils;

import javax.sql.DataSource;
import java.util.*;
import java.util.stream.Collectors;

/**
 * 自动生成 SqlSessionTemplate 工具类
 *
 * @author nousin
 * @since 2021/1/19
 */
@Slf4j
public class SqlSessionTemplateUtils {

    // 应用上下文
    public static final ApplicationContext applicationContext = SpringUtils.getApplicationContext();
    // 应用上下文环境
    public static final Environment environment = SpringUtils.getEnvironment();

    public static final DefaultListableBeanFactory beanFactory = (DefaultListableBeanFactory) applicationContext.getAutowireCapableBeanFactory();
    
    public static final String MYSQL_DRIVER_5 = "com.mysql.jdbc.Driver";
    public static final String MYSQL_DRIVER_8 = "com.mysql.cj.jdbc.Driver";
    public static final String MYSQL_URL_PREFIX = "jdbc:mysql://";
    public static final String MYSQL_VERSION_8_PARAM = "?useUnicode=true&characterEncoding=utf8&allowMultiQueries=true" +
            "&useSSL=false&useLegacyDatetimeCode=false&useAffectedRows=true&serverTimezone=GMT%2B8&rewriteBatchedStatements=true&allowPublicKeyRetrieval=true";
    public static final String MYSQL_VERSION_5_PARAM = "?useUnicode=true&characterEncoding=utf8&allowMultiQueries=true" +
            "&useSSL=false&useLegacyDatetimeCode=false&useAffectedRows=true";

    // 数据源加载类型【0-刷新所有，1-添加，2-修改，3-删除】
    public static final int MODIFY_TYPE_ALL = 0;
    public static final int MODIFY_TYPE_ADD = 1;
    public static final int MODIFY_TYPE_UPDATE = 2;
    public static final int MODIFY_TYPE_DELETE = 3;
    /**
     * 连接池属性
     */
    public static final String type = environment.getProperty("spring.datasource.type");
    //public static final String driverClassName = environment.getProperty("spring.datasource.driverClassName");
    public static final String initialSize = environment.getProperty("spring.datasource.initialSize");
    public static final String minIdle = environment.getProperty("spring.datasource.minIdle");
    public static final String maxActive = environment.getProperty("spring.datasource.maxActive");
    public static final String maxWait = environment.getProperty("spring.datasource.maxWait");
    public static final String timeBetweenEvictionRunsMillis = environment.getProperty("spring.datasource.timeBetweenEvictionRunsMillis");
    public static final String minEvictableIdleTimeMillis = environment.getProperty("spring.datasource.minEvictableIdleTimeMillis");
    public static final String validationQuery = environment.getProperty("spring.datasource.validationQuery");
    public static final String testWhileIdle = environment.getProperty("spring.datasource.testWhileIdle");
    public static final String testOnBorrow = environment.getProperty("spring.datasource.testOnBorrow");
    public static final String testOnReturn = environment.getProperty("spring.datasource.testOnReturn");
    public static final String filters = environment.getProperty("spring.datasource.filters");

    public static final String dataSourceSuffix = "DataSource";
    public static final String sqlSessionFactorySuffix = "SqlSessionFactory";
    public static final String sqlSessionTemplateSuffix = "SqlSessionTemplate";

    public static String getProperty(String key) {
        return environment.getProperty(key);
    }
    
    public static Properties properties;
    public static final AtomicBoolean flag = new AtomicBoolean(false);

    static {
        if (flag.compareAndSet(false, true)) {
            properties = new Properties();
            properties.setProperty("DEL_FLAG_NORMAL", String.valueOf(GlobalConstant.DEL_FLAG_NORMAL));
            properties.setProperty("DEL_FLAG_DELETE", String.valueOf(GlobalConstant.DEL_FLAG_DELETE));
            properties.setProperty("VERSION_NO", String.valueOf(GlobalConstant.VERSION_NO));
            properties.setProperty("SYS_YES", String.valueOf(GlobalConstant.YES));
            properties.setProperty("SYS_NO", String.valueOf(GlobalConstant.NO));
        }
    }

    /**
     * 动态添加 SqlSessionTemplate
     *
     * @param dataSourceList  数据源列表
     * @param mapperLocations Mapper 地址
     * @param interfaces      接口信息
     * @param systemModifyDto 参数
     */
    public static List<DataSourceDto> processBeanRegistry(List<DataSourceDto> dataSourceList, String mapperLocations, Set<Class<?>> interfaces, SystemModifyDto systemModifyDto) {
        List<DataSourceDto> usedDataSource = new ArrayList<>();
        // 判断是否为空
        if (CollectionUtils.isEmpty(dataSourceList) || CollectionUtils.isEmpty(interfaces))
            return usedDataSource;

        // 卸载相关 Bean
        if (systemModifyDto.getModifyType() == SqlSessionTemplateUtils.MODIFY_TYPE_ALL) {
            dataSourceList.forEach(e -> unRegisteredBean(e.getDataSourceName(), interfaces));
        } else {
            // 卸载Bean
            unRegisteredBean(systemModifyDto.getDataSourceName(), interfaces);
        }

        // 分组取一条符合条件的数据
        Map<String, DataSourceDto> systemDataSourceMap = dataSourceList.stream().collect(Collectors.groupingBy(DataSourceDto::getDataSourceName,
                Collectors.collectingAndThen(Collectors.toList(), list -> list.stream().findFirst().orElse(null))));
        // 初始化
        if (systemModifyDto.getModifyType() == SqlSessionTemplateUtils.MODIFY_TYPE_ALL) {
            Collection<DataSourceDto> dataSourceDtos = systemDataSourceMap.values();
            if (dataSourceDtos.stream().allMatch(Objects::isNull)) {
                throw new RuntimeException();
            } else {
                usedDataSource.addAll(dataSourceDtos);
                registeredBean(dataSourceDtos, mapperLocations, interfaces);
            }
        }
        // 添加、修改系统
        else if (systemModifyDto.getModifyType() == SqlSessionTemplateUtils.MODIFY_TYPE_ADD ||
                systemModifyDto.getModifyType() == SqlSessionTemplateUtils.MODIFY_TYPE_UPDATE) {
            DataSourceDto systemDataSourceDto = systemDataSourceMap.get(systemModifyDto.getDataSourceName());
            if (null == systemDataSourceDto) {
                String format = String.format("系统【%s】加载失败", systemModifyDto.getDataSourceName());
                MailUtils.sendCommonMail("unnous1@163.com", format, format);
            } else {
                usedDataSource.add(systemDataSourceDto);
                registeredBean(systemDataSourceDto, mapperLocations, interfaces);
            }
        }
        // 删除系统
        else {
        }
        return usedDataSource;
    }

    /**
     * 注册Bean
     *
     * @param dataSources 数据源信息
     */
    public static void registeredBean(DataSourceDto dataSources, String mapperLocations, Set<Class<?>> interfaces) {
        registeredBean(Collections.singletonList(dataSources), mapperLocations, interfaces);
    }

    public static void registeredBean(Collection<DataSourceDto> dataSources, String mapperLocations, Set<Class<?>> interfaces) {
        if (CollectionUtils.isEmpty(dataSources)) {
            return;
        }
        for (DataSourceDto dataSource : dataSources) {
            String dataSourceName = dataSource.getDataSourceName().toLowerCase();
            if (exist(dataSourceName)) {
                continue;
            }
            log.error("开始装配【{}】相关组件", dataSourceName);
            DataSource dataSourceBean = processDataSource(dataSource, dataSourceName);
            SqlSessionFactory sqlSessionFactory = processSqlSessionFactory(dataSourceBean, dataSourceName, mapperLocations);
            SqlSessionTemplate sqlSessionTemplate = processSqlSessionTemplate(sqlSessionFactory, dataSourceName);
            // 注册Bean
            beanFactory.registerSingleton(capitalizeTheFirstLetter(dataSourceName), dataSourceName);
            beanFactory.registerSingleton(dataSourceName + dataSourceSuffix, dataSourceBean);
            beanFactory.registerSingleton(dataSourceName + sqlSessionFactorySuffix, sqlSessionFactory);
            beanFactory.registerSingleton(dataSourceName + sqlSessionTemplateSuffix, sqlSessionTemplate);
            registerMapper(sqlSessionTemplate, dataSourceName, interfaces);
            log.error("【{}】相关组件，装配完成", dataSourceName);
        }
    }

    /**
     * 卸载Bean
     *
     * @param dataSourceName 标识
     */
    public static void unRegisteredBean(String dataSourceName, Set<Class<?>> interfaces) {
        if (StringUtils.isEmpty(dataSourceName)) {
            return;
        }
        if (!exist(dataSourceName)) {
            return;
        }
        log.error("开始卸载【{}】相关组件", dataSourceName);
        for (Class<?> anInterface : interfaces) {
            beanFactory.destroySingleton(getTargetDaoName(anInterface, dataSourceName));
        }
        // 销毁 Bean
        beanFactory.destroySingleton(capitalizeTheFirstLetter(dataSourceName));
        beanFactory.destroySingleton(dataSourceName + dataSourceSuffix);
        beanFactory.destroySingleton(dataSourceName + sqlSessionFactorySuffix);
        beanFactory.destroySingleton(dataSourceName + sqlSessionTemplateSuffix);
        log.error("【{}】相关组件，卸载完成", dataSourceName);
    }


    /**
     * 查看当前数据源是否被创建过
     *
     * @param dataSourceName 标识
     * @return 是否已经创建过该数据源
     */
    private static boolean exist(String dataSourceName) {
        if (StringUtils.isEmpty(dataSourceName)) {
            return false;
        }
        try {
            SpringUtils.getBean(capitalizeTheFirstLetter(dataSourceName));
            return true;
        } catch (Exception e) {
            return false;
        }
    }

    /**
     * 创建数据源
     *
     * @param dataSourceDto   数据源信息
     * @param dataSourceName  标识
     * @return 数据源信息
     */
    private static DataSource processDataSource(DataSourceDto dataSourceDto, String dataSourceName) {
        Properties prop = new Properties();
        prop.put("url", dataSourceDto.getUrl());
        prop.put("username", dataSourceDto.getUsername());
        prop.put("password", dataSourceDto.getPassword());
        prop.put("driverClassName", getSqlDriver(dataSourceDto.getMysqlVersion()));
        prop.put("filters", filters);
        prop.put("maxActive", maxActive);
        prop.put("initialSize", initialSize);
        prop.put("maxWait", maxWait);
        prop.put("minIdle", minIdle);
        prop.put("timeBetweenEvictionRunsMillis", timeBetweenEvictionRunsMillis);
        prop.put("minEvictableIdleTimeMillis", minEvictableIdleTimeMillis);
        prop.put("validationQuery", validationQuery);
        prop.put("testWhileIdle", testWhileIdle);
        prop.put("testOnBorrow", testOnBorrow);
        prop.put("testOnReturn", testOnReturn);
        AtomikosDataSourceBean ds = new AtomikosDataSourceBean();
        ds.setXaDataSourceClassName(type);
        ds.setPoolSize(5);
        ds.setXaProperties(prop);
        ds.setUniqueResourceName(dataSourceName + "DataSource");
        ds.setTestQuery("select 1");
        return ds;
    }

    /**
     * 获取 Mysql 驱动
     *
     * @param mysqlVersion mysql 版本
     * @return 驱动类
     */
    private static String getSqlDriver(Integer mysqlVersion) {
        return mysqlVersion == MYSQL_VERSION_8 ? MYSQL_DRIVER_8 : MYSQL_DRIVER_5;
    }

    /**
     * 创建 SqlSessionFactory
     *
     * @param dataSource     数据源信息
     * @param dataSourceName 标识
     * @return SqlSessionFactory
     */
    private static SqlSessionFactory processSqlSessionFactory(DataSource dataSource, String dataSourceName, String mapperLocations) {
        try {
            SqlSessionFactoryBean bean = new SqlSessionFactoryBean();
            bean.setDataSource(dataSource);
            //如果重写了 SqlSessionFactory 需要在初始化的时候手动将 mapper 地址 set到 factory 中，否则会报错：
            //org.apache.ibatis.binding.BindingException: Invalid bound statement (not found)
            assert mapperLocations != null;
            bean.setMapperLocations(new PathMatchingResourcePatternResolver().getResources(mapperLocations));
            bean.setVfs(SpringBootVFS.class);
            // bean.setPlugins(new MybatisInterceptor());
            bean.setConfigurationProperties(properties);

            // ---------- 执行生命周期方法 ----------
            // 手动调用 Bean 生命周期 InitializingBean
            bean.afterPropertiesSet();
            SqlSessionFactory object = bean.getObject();
            // 手动执行 ApplicationListener 的 ContextRefreshedEvent 事件
            assert object != null;
            object.getConfiguration().getMappedStatementNames();
            return bean.getObject();
        } catch (Exception e) {
            e.printStackTrace();
            throw new RuntimeException(String.format("Error create SqlSessionFactoryBean, by %s", dataSourceName));
        }
    }

    /**
     * 创建 SqlSessionTemplate
     *
     * @param sqlSessionFactory SqlSessionFactory
     * @param dataSourceName    标识
     * @return SqlSessionTemplate
     */
    private static SqlSessionTemplate processSqlSessionTemplate(SqlSessionFactory sqlSessionFactory, String dataSourceName) {
        return new SqlSessionTemplate(sqlSessionFactory);
    }

    /**
     * 注册Mapper
     */
    private static void registerMapper(SqlSessionTemplate sqlSessionTemplate, String dataSourceName, Set<Class<?>> interfaces) {
        if (CollectionUtils.isEmpty(interfaces)) {
            return;
        }
        // 注册Mapper
        for (Class<?> anInterface : interfaces) {
            MapperFactoryBean mapperFactoryBean = new MapperFactoryBean();
            mapperFactoryBean.setMapperInterface(anInterface);
            mapperFactoryBean.setSqlSessionTemplate(sqlSessionTemplate);
            String beanName = getTargetDaoName(anInterface, dataSourceName);
            beanFactory.registerSingleton(beanName, mapperFactoryBean);
        }
    }

    /**
     * 扫描接口信息
     */
    public static void scanInterface(String packagePath, Set<Class<?>> interfaces) {
        try {
            assert packagePath != null;
            String packageSearchPath = ResourcePatternResolver.CLASSPATH_ALL_URL_PREFIX +
                    ClassUtils.convertClassNameToResourcePath(environment.resolveRequiredPlaceholders(packagePath)) + "/**/*.class";
            Resource[] resources = new PathMatchingResourcePatternResolver().getResources(packageSearchPath);
            CachingMetadataReaderFactory cachingMetadataReaderFactory = new CachingMetadataReaderFactory();
            for (Resource resource : resources) {
                if (resource.isReadable()) {
                    try {
                        MetadataReader metadataReader = cachingMetadataReaderFactory.getMetadataReader(resource);
                        ClassMetadata classMetadata = metadataReader.getClassMetadata();
                        interfaces.add(Class.forName(classMetadata.getClassName()));
                    } catch (Throwable ex) {
                        throw new BeanDefinitionStoreException("Failed to read candidate component class: " + resource, ex);
                    }
                }
            }
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }
    
    /**
     * 首字母大写
     */
    public static String capitalizeTheFirstLetter(String str) {
        if (org.apache.commons.lang3.StringUtils.isBlank(str))
            return "";
        if (str.length() == 1)
            return str.toUpperCase();
        return str.substring(0, 1).toUpperCase() + str.substring(1);
    }
    
    /**
     * 获取 Dao 名称
     *
     * @param clazz  类字节码
     * @param prefix 类前缀
     * @param <T>    泛型
     * @return Dao 名称
     */
    public static <T> String getTargetDaoName(Class<T> clazz, String prefix) {
        return prefix.toLowerCase() + clazz.getSimpleName();
    }

    /**
     * 缓存加载的数据源信息
     *
     * @param dataSources     已使用的数据源信息
     * @param systemModifyDto 请求条件
     * @param cachedInfoList  缓存信息
     */
    public static void loadCache(List<DataSourceDto> dataSources, SystemModifyDto systemModifyDto, List<CachedInfoDto> cachedInfoList) {
        // 添加缓存
    }
}
```

## 数据源实体类

```java
import com.nousin.common.constant.GlobalConstant;
import lombok.Getter;
import lombok.Setter;

/**
 * 动态数据源 Dto
 *
 * @author nousin
 * @since 2020/9/22
 */
@Getter
@Setter
public class DataSourceDto {
    private String dataSourceName; // 数据源名称
    private Integer enabled = 0; // 系统启用
    private String ipAddress; // IP地址
    private String port; // 端口号
    private String databaseName; // 数据库名称
    private String username; // 用户名
    private String password; // 密码
    private Integer mysqlVersion = SqlSessionTemplateUtils.MYSQL_VERSION_8; // Mysql版本 [5, 8]

    // 基础池使用数据

    // String url; // url 参数不用加
    public String getUrl() {
        return SqlSessionTemplateUtils.MYSQL_URL_PREFIX + ipAddress + ":" + port + "/" + databaseName +
                (mysqlVersion == SqlSessionTemplateUtils.MYSQL_VERSION_5 ? SqlSessionTemplateUtils.MYSQL_VERSION_5_PARAM : SqlSessionTemplateUtils.MYSQL_VERSION_8_PARAM);
    }
}
```
