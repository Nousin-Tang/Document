# Java 开发手册（泰山版）

[TOC]

## 前言
《Java 开发手册》是阿里巴巴集团技术团队的集体智慧结晶和经验总结，经历了多次大规模一 线实战的检验及不断完善，公开到业界后，众多社区开发者踊跃参与，共同打磨完善，系统化地整理 成册，当前的版本是泰山版。现代软件行业的高速发展对开发者的综合素质要求越来越高，因为不仅 是编程知识点，其它维度的知识点也会影响到软件的最终交付质量。比如:数据库的表结构和索引设 计缺陷可能带来软件上的架构缺陷或性能风险;工程结构混乱导致后续维护艰难;没有鉴权的漏洞代 码易被黑客攻击等等。所以本手册以 Java 开发者为中心视角，划分为**编程规约、异常日志、单元测 试、安全规约、MySQL数据库、工程结构、设计规约**七个维度，再根据内容特征，细分成若干二级子目录。另外，依据约束力强弱及故障敏感性，规约依次分为强制、推荐、参考三大类。在延伸信息 中，“<font color='yellow'>说明</font>”对规约做了适当扩展和解释；“<font color='green'>正例</font>”提倡什么样的编码和实现方式；“<font color='red'>反例</font>”说明需 要提防的雷区，以及真实的错误案例。

手册的愿景是**码出高效，码出质量**。现代软件架构的复杂性需要协同开发完成，如何高效地协 同呢?无规矩不成方圆，无规范难以协同，比如，制订交通法规表面上是要限制行车权，实际上是保 障公众的人身安全，试想如果没有限速，没有红绿灯，谁还敢上路行驶?对软件来说，适当的规范和 标准绝不是消灭代码内容的创造性、优雅性，而是限制过度个性化，以一种普遍认可的统一方式一起 做事，提升协作效率，降低沟通成本。代码的字里行间流淌的是软件系统的血液，质量的提升是尽可 能少踩坑，杜绝踩重复的坑，切实提升系统稳定性，码出质量。

我们已经在 2017 杭州云栖大会上发布了配套的 Java 开发规约 IDE 插件，下载量达到 152 万人 次，阿里云效也集成了代码规约扫描引擎。次年，发布 36 万字的配套详解图书《码出高效》，本书 秉持“图胜于表，表胜于言”的理念，深入浅出地将计算机基础、面向对象思想、JVM 探源、数据 结构与集合、并发与多线程、单元测试等知识客观、立体地呈现出来。紧扣学以致用、学以精进的目 标，结合阿里巴巴实践经验和故障案例，与底层源码解析融会贯通，娓娓道来。《码出高效》和《Java 开发手册》书籍版所得收入均捐赠公益事情，希望用技术情怀帮助更多的人。

## 一、 编程规约

### (一) 命名风格

1. <font color='red'>【强制】</font>代码中的命名均不能以<font color='darkblue'>下划线或美元符号</font>开始，也不能以<font color='darkblue'>下划线或美元符号</font>结束。 
  <font color='red'>反例：_name / __name / $name / name_ / name$ / name__ </font>
  
1. <font color='red'>【强制】</font>所有编程相关的命名严禁使用拼音与英文混合的方式，更不允许直接使用中文的方式。 
  <font color='orange'>说明</font>：正确的英文拼写和语法可以让阅读者易于理解，避免歧义。注意，纯拼音命名方式更要避免采用。
  <font color='green'>正例</font>：ali / alibaba / taobao / cainiao/ aliyun/ youku / hangzhou 等国际通用的名称，可视同英文。 
  <font color='red'>反例</font>：DaZhePromotion [打折] / getPingfenByName() [评分] / int 某变量 = 3 

1. <font color='red'>【强制】</font>类名使用`UpperCamelCase`风格，但以下情形例外:DO/BO/DTO/VO/AO/ PO / UID 等。 
  <font color='green'>正例</font>：ForceCode / UserDO / HtmlDTO / XmlService / TcpUdpDeal / TaPromotion 
  <font color='red'>反例</font>：forcecode / UserDo / HTMLDto / XMLService / TCPUDPDeal / TAPromotion 
  
1. <font color='red'>【强制】</font>方法名、参数名、成员变量、局部变量都统一使用`lowerCamelCase`风格。
  <font color='green'>正例</font>： localValue / getHttpMessage() / inputUserId 
  
1. <font color='red'>【强制】</font>常量命名全部大写，单词间用下划线隔开，力求语义表达完整清楚，不要嫌名字长。
  <font color='green'>正例</font>：MAX_STOCK_COUNT / CACHE_EXPIRED_TIME
  <font color='red'> 反例</font>：MAX_COUNT / EXPIRED_TIME 

1. <font color='red'>【强制】</font>抽象类命名使用`Abstract`或`Base`开头;异常类命名使用`Exception`结尾;测试类 命名以它要测试的类的名称开始，以 Test 结尾。 

1. <font color='red'>【强制】</font>类型与中括号紧挨相连来表示数组。
   <font color='green'>正例</font>：定义整形数组 `int[] arrayDemo`;
   <font color='red'>反例</font>：在 `main `参数中，使用 `String args`

1. <font color='red'>【强制】</font>POJO类中的任何布尔类型的变量，都不要加is前缀，否则部分框架解析会引起序列 化错误。 
  <font color='darkorange'>说明</font>：在本文 MySQL 规约中的建表约定第一条，表达是与否的值采用 is_xxx 的命名方式，所以，需要在` <resultMap>`设置从 is_xxx 到 xxx 的映射关系。 
  <font color='red'>反例</font>：定义为基本数据类型 Boolean isDeleted 的属性，它的方法也是` isDeleted()`，框架在反向解析的时“误以为”对应的属性名称是 deleted，导致属性获取不到，进而抛出异常。

1. <font color='red'>【强制】</font>包名统一使用小写，点分隔符之间有且仅有一个自然语义的英语单词。包名统一使用 单数形式，但是类名如果有复数含义，类名可以使用复数形式。
  <font color='green'>正例</font>：应用工具类包名为`com.alibaba.ei.kunlun.aap.util`、类名为`MessageUtils`(此规则参考`spring`的框架结构)

1. <font color='red'>【强制】</font>避免在子父类的成员变量之间、或者不同代码块的局部变量之间采用完全相同的命名，使可读性降低。
  <font color='darkorange'>说明</font>：子类、父类成员变量名相同，即使是 public 类型的变量也是能够通过编译，而局部变量在同一方法内的不同代码块中同名也是合法的，但是要避免使用。对于非 setter/getter 的参数名称也要避免与成员变量名称相同。
  <font color='red'>反例</font>：
  
  ```java
  public class ConfusingName { 
    public int stock;
    // 非 setter/getter 的参数名称，不允许与本类成员变量同名
    public void get(String alibaba) { if (condition) {
      final int money = 666;
        // ...
      }
      for (int i = 0; i < 10; i++) {
        // 在同一方法体中，不允许与其它代码块中的 money 命名相同 
        final int money = 15978;
        // ...
      } 
    }
  }
  class Son extends ConfusingName {
      // 不允许与父类的成员变量名称相同
      public int stock;
  }
  ```
  
1. <font color='red'>【强制】</font>杜绝完全不规范的缩写，避免望文不知义。
  <font color='red'>反例</font>：AbstractClass“缩写”命名成 AbsClass;condition“缩写”命名成 condi，此类随意缩写严重降 低了代码的可阅读性。

1. <font color='orange'>【推荐】</font>为了达到代码自解释的目标，任何自定义编程元素在命名时，使用尽量完整的单词组 合来表达。
  <font color='green'>正例</font>：在 JDK 中，对某个对象引用的 volatile 字段进行原子更新的类名为:AtomicReferenceFieldUpdater。
 <font color='red'> 反例</font>：常见的方法内变量为 int a;的定

1. <font color='orange'>【推荐】</font>在常量与变量的命名时，表示类型的名词放在词尾，以提升辨识度。
  <font color='green'>正例</font>：startTime / workQueue / nameList / TERMINATED_THREAD_COUNT
  <font color='red'>反例</font>：startedAt / QueueOfWork / listName / COUNT_TERMINATED_THREAD

1. <font color='orange'>【推荐】</font>如果模块、接口、类、方法使用了设计模式，在命名时需体现出具体模式。 <font color='darkorange'>说明</font>：将设计模式体现在名字中，有利于阅读者快速理解架构设计理念。
  <font color='green'>正例</font>： 
  
  ```java
  public class OrderFactory;
  public class LoginProxy;
  public class ResourceObserver;
  ```

1. <font color='orange'>【推荐】</font>接口类中的方法和属性不要加任何修饰符号(`public` 也不要加)，保持代码的简洁 性，并加上有效的 Javadoc 注释。尽量不要在接口里定义变量，如果一定要定义变量，确定 与接口方法相关，并且是整个应用的基础常量。
  <font color='green'>正例</font>：接口方法签名 void commit();接口基础常量 String COMPANY = "alibaba";
  <font color='red'> 反例</font>：接口方法定义 public abstract void f();
  <font color='darkorange'>说明</font>：JDK8 中接口允许有默认实现，那么这个 default 方法，是对所有实现类都有价值的默认实现。

1. 接口和实现类的命名有两套规则：
  1)<font color='red'>【强制】</font>对于 Service 和 DAO 类，基于 SOA 的理念，暴露出来的服务一定是接口，内部的实现类用 Impl 的后缀与接口区别。
  <font color='green'>正例</font>：CacheServiceImpl 实现 CacheService 接口。
  2)<font color='orange'>【推荐】</font>如果是形容能力的接口名称，取对应的形容词为接口名(通常是–able 的形容词)。 
  <font color='green'>正例</font>：AbstractTranslator 实现 Translatable 接口。

1. <font color='darkgreen'>【参考】</font>枚举类名带上 Enum 后缀，枚举成员名称需要全大写，单词间用下划线隔开。 
  <font color='darkorange'>说明</font>：枚举其实就是特殊的常量类，且构造方法被默认强制是私有。
  <font color='green'>正例</font>：枚举名字为 ProcessStatusEnum 的成员名称:SUCCESS / UNKNOWN_REASON。

1. <font color='darkgreen'>【参考】</font>各层命名规约:
  A) Service/DAO 层方法命名规约
    1) 获取单个对象的方法用 get 做前缀。
    2) 获取多个对象的方法用 list 做前缀，复数结尾，如:listObjects。       3) 获取统计值的方法用 count 做前缀。
    4) 插入的方法用 save/insert 做前缀。
    5) 删除的方法用 remove/delete 做前缀。
    6) 修改的方法用 update 做前缀。
  B) 领域模型命名规约
    1) 数据对象:xxxDO，xxx 即为数据表名。
    2) 数据传输对象:xxxDTO，xxx 为业务领域相关的名称。

### (二) 常量定义

1. <font color='red'>【强制】</font>不允许任何魔法值(即未经预先定义的常量)直接出现在代码中。 
  <font color='red'>反例</font>：
  //本例中同学 A 定义了缓存的 key，然后缓存提取的同学 B 使用了 Id#taobao 来提取，少了下划线，导致故障。
  String key = "Id#taobao_" + tradeId; cache.put(key, value);

2. <font color='red'>【强制】</font>在long或者Long赋值时，数值后使用大写的L，不能是小写的l，小写容易跟数字 混淆，造成误解。
   <font color='darkorange'>说明</font>：Long a = 2l; 写的是数字的 21，还是 Long 型的 2。

3. <font color='orange'>【推荐】</font>不要使用一个常量类维护所有常量，要按常量功能进行归类，分开维护。 
   <font color='darkorange'>说明</font>：大而全的常量类，杂乱无章，使用查找功能才能定位到修改的常量，不利于理解，也不利于维护。 
   <font color='green'>正例</font>：缓存相关常量放在类 CacheConsts 下;系统配置相关常量放在类 ConfigConsts 下。

4. <font color='orange'>【推荐】</font>常量的复用层次有五层:跨应用共享常量、应用内共享常量、子工程内共享常量、包内共享常量、类内共享常量。
   1) 跨应用共享常量：放置在二方库中，通常是 `client.jar` 中的 `constant` 目录下。
   2) 应用内共享常量：放置在一方库中，通常是子模块中的 `constant` 目录下。 
     <font color='red'>反例</font>：易懂变量也要统一定义成应用内共享常量，两位工程师在两个类中分别定义了“YES”的变量：
     类 A 中:public static final String YES = "yes";
     类 B 中:public static final String YES = "y";
     A.YES.equals(B.YES)，预期是 true，但实际返回为 false，导致线上问题。
   3) 子工程内部共享常量：即在当前子工程的 constant 目录下。 
   4) 包内共享常量：即在当前包下单独的 constant 目录下。
   5) 类内共享常量：直接在类内部 private static final 定义。

5. <font color='orange'>【推荐】</font>如果变量值仅在一个固定范围内变化用 enum 类型来定义。

   <font color='darkorange'>说明</font>：如果存在名称之外的延伸属性应使用 enum 类型，下面正例中的数字就是延伸信息，表示一年中的第几个季节。
   <font color='green'>正例</font>：
   ```java
public enum SeasonEnum {
     SPRING(1), SUMMER(2), AUTUMN(3), WINTER(4);
     private int seq;
     SeasonEnum(int seq) {
       this.seq = seq; 
     }
     public int getSeq() {
       return seq; 
     }
   }
   ```

### (三) 代码格式

1. <font color='red'>【强制】</font>如果是大括号内为空，则简洁地写成{}即可，大括号中间无需换行和空格;如果是非 空代码块则:

   1) 左大括号前不换行。
   2) 左大括号后换行。
   3) 右大括号前换行。
   4) 右大括号后还有 else 等代码则不换行;表示终止的右大括号后必须换行。

2. <font color='red'>【强制】</font>左小括号和右边相邻字符之间不出现空格;右小括号和左边相邻字符之间也不出现空 格;而左大括号前需要加空格。详见第 5 条下方正例提示。
   <font color='red'>反例</font>：if (空格 a == b 空格)

3. <font color='red'>【强制】</font>if/for/while/switch/do等保留字与括号之间都必须加空格。

4. <font color='red'>【强制】</font>任何二目、三目运算符的左右两边都需要加一个空格。

   <font color='darkorange'>说明</font>：包括赋值运算符=、逻辑运算符&&、加减乘除符号等。

5. <font color='red'>【强制】</font>采用 4 个空格缩进，禁止使用 tab 字符。
   <font color='darkorange'>说明</font>：如果使用 tab 缩进，必须设置 1 个 tab 为 4 个空格。IDEA 设置 tab 为 4 个空格时，请勿勾选 Use tab character 。
   <font color='green'>正例</font>：(涉及 1-5 点)
   
   ```java
   public static void main(String[] args) { 
     // 缩进 4 个空格
     String say = "hello";
     // 运算符的左右必须有一个空格
     int flag = 0;
     // 关键词 if 与括号之间必须有一个空格，括号内的 f 与左括号，0 与右括号不需要空格 if (flag == 0) {
     System.out.println(say); }
     // 左大括号前加空格且不换行;左大括号后换行
     if (flag == 1) {
       System.out.println("world");
       // 右大括号前换行，右大括号后有 else，不用换行
     } else {
       System.out.println("ok");
     	// 在右大括号后直接结束，则必须换行
   	} 
   }
   ```

6. 【强制】注释的双斜线与注释内容之间有且仅有一个空格。
  正例:
  // 这是示例注释，请注意在双斜线之后有一个空格
  String commentString = new String();

7. 【强制】在进行类型强制转换时，右括号与强制转换值之间不需要任何空格隔开。
  正例:long first = 1000000000000L; int second = (int)first + 2;
  
8. 【强制】单行字符数限制不超过 120 个，超出需要换行。换行时遵循如下原则: 
  1)第二行相对第一行缩进 4 个空格，从第三行开始，不再继续缩进，参考示例。 
  2)运算符与下文一起换行。
  3)方法调用的点符号与下文一起换行。 
  4)方法调用中的多个参数需要换行时，在逗号后进行。
  5)在括号前不要换行，见反例。 
  正例:
  ```java
  StringBuilder sb = new StringBuilder();
  // 超过 120 个字符的情况下，换行缩进 4 个空格，并且方法前的点号一起换行 
  sb.append("zi").append("xin")...
    .append("huang")... 
    .append("huang")... 
    .append("huang");
  ```
  反例:
  ```java
  StringBuilder sb = new StringBuilder();
  // 超过 120 个字符的情况下，不要在括号前换行 
  sb.append("you").append("are")...append
  ("lucky");
  // 参数很多的方法调用可能超过 120 个字符，逗号后才是换行处
  method(args1, args2, args3, ... , argsX);
  ```
9. 【强制】方法参数在定义和传入时，多个参数逗号后边必须加空格。 
  正例:下例中实参的 args1，后边必须要有一个空格。
  method(args1, args2, args3); 10.
10. 【强制】IDE 的 text file encoding 设置为 UTF-8; IDE 中文件的换行符使用 Unix 格式，不要
  使用 Windows 格式。
11. 【推荐】单个方法的总行数不超过 80 行。
  说明:除注释之外的方法签名、左右大括号、方法内代码、空行、回车及任何不可见字符的总行数不超过80 行。
  正例:代码逻辑分清红花和绿叶，个性和共性，绿叶逻辑单独出来成为额外方法，使主干代码更加清晰;共
  性逻辑抽取成为共性方法，便于复用和维护。
12. 【推荐】没有必要增加若干空格来使变量的赋值等号与上一行对应位置的等号对齐。
  正例:
  int one = 1;
  long two = 2L;
  float three = 3F;
  StringBuilder sb = new StringBuilder();
  说明:增加 sb 这个变量，如果需要对齐，则给 one、two、three 都要增加几个空格，在变量比较多的情 况下，是非常累赘的事情。
13. 【推荐】不同逻辑、不同语义、不同业务的代码之间插入一个空行分隔开来以提升可读性。 说明:任何情形，没有必要插入多个空行进行隔开。