# Java8 新特性

[TOC]

## Lambda 表达式

### 什么是 Lambda ？
先感受下一个例子
```java
/**创建一个Runnable接口的实例*/
Runnable runnable = new Runnable() {
    @Override
    public void run() {
        System.out.print("Hello World!")
    }
};

/**如果是创建一个线程可以这样*/
Thread thread = new Thread(new Runnable() {
    @Override
    public void run() {
        System.out.print("Hello World!")
    }
});
```
通过 Lambda 表达式创建
```java
/**创建一个Runnable接口的实例*/
Runnable runnable = () -> {
    System.out.print("Hello World!")
};

/**如果是创建一个线程可以这样*/
Thread thread = new Thread(() -> {
    System.out.print("Hello World!")
});
```
### Lambda 表达式定义

> 它们通过使用表达式来提供一种<font color="red">清晰简洁</font>的方式来表示<font color="red">方法接口</font>。（又被成为“闭包”或“匿名方法”）

#### 格式

```java
// 1. 方法体内部只有一个表达式时，‘{}’ 可以省略
() -> System.out.print("Hello World!")

// 2. 接口方法只有一个参数时，‘()’可以省略
name -> System.out.print("Hello " + name + "!")

// 3. 参数的类型可以不用写(类型推断)
// 4. 可选的返回关键字return：如果主体只有一个表达式返回值则可以省略return和{}
(x, y) -> x – y
(int x, int y) -> x + y
```
#### 使用条件
- 接口中有且只能有一个抽象方法，默认方法静态方法不受影响
- lambda 表达式的参数和 `T` 的方法参数在数量和类型上一一对应
- lambda 表达式的返回值和 `T` 的方法返回值相兼容（Compatible）
- lambda 表达式内所抛出的异常和 `T` 的方法 `throws` 类型相兼容

再看一个例子

```java
/**
 * 函数式接口
 */
@FunctionalInterface
interface  A{
    void opration();
}

class B {
    void realOpration(A fi){
        fi.opration();
    }
}

public class Tests {
   @Test
   public void test(){
       /**创建接口A的实例*/
       A a = ()-> System.out.println("this is  A ");
       a.opration();
       /**再来试试这个支持Lambda表达式的方法*/
       B b = new B();
       b.realOpration(()-> System.out.println("use A print B"));
   }
}
```
#### 注意点：

- lambda 表达式基于词法作用域，也就是说 lambda 表达式函数体里面的变量和它外部环境的变量具有相同的语义（也包括 lambda 表达式的形式参数）。

- lambda 表达式只能引用*有效只读*（Effectively final）的局部变量。这就是说不能在 lambda 内部修改定义在域外的局部变量，否则会编译错误。

- lambda 表达式的局部变量可以不用声明为 `final`，但是必须不可被后面的代码修改（即隐性的具有 `final` 的语义）。

- 在 Lambda 表达式当中不允许声明一个与局部变量同名的参数或者局部变量。

```java
// 下面的代码，它会把 "Hello, world!" 打印两遍
public class Hello {
    
	  // lambda 表达式中的 this 指的是 Hello 对象 
  	Runnable r1 = () -> { System.out.println(this); }
  	Runnable r2 = () -> { System.out.println(toString()); }
    
  	public String toString() {
        return "Hello, world";
    }
    
  	public static void main(String... args) {
    		new Hello().r1.run();
    		new Hello().r2.run();
  	}
}
```

### 函数式接口（Functional Interface）

>  是指只有一个抽象方法的接口。（默认实现不算）

#### Java8内置函数式接口(java.util.function)
- **Predicate**：boolean test(T t);
- **Consumer**： void accept(T t);
- **Function**： R apply(T t);
- **Supplier** ：T get();
- **BiPredicate** ：boolean test(T t, U u);
- **BiConsumer** ：void accept(T t, U u);
- **BiFunction** ： R apply(T t, U u);


### 方法引用

#### 方法引用

>  方法引用就是通过类名或方法名引用已经存在的方法来简化lambda表达式。

方法引用分为静态方法的方法引用和实例方法的方法引用。

##### 方法引用的三种语法格式

1. 对象::实例方法名

```java
// lambda 写法
@Test
void test1(){
    Consumer<String> con = x -> System.out.println(x);
}
// 方法引用
@Test
void test2(){
    Consumer<String> con = System.out::println;
}
```
2. 类::静态方法名

```java
// lambda 写法
@Test
void test3(){
    Comparator<Integer> com = (x, y) -> Integer.compare(x,y);
}
// 方法引用
@Test
void test4(){
    Comparator<Integer> com = Integer::compare;
}
// Integer 中部分源码
public final class Integer extends Number implements Comparable<Integer> { 
    public static int compare(int x, int y) {
        return (x < y) ? -1 : ((x == y) ? 0 : 1);
    }
}
```
3. 类::实例方法名

```java
// lambda 写法
@Test
void test5(){
    BiPredicate<String,String> bp = (x,y) -> x.equals(y);
}
// 方法引用
@Test
void test6(){
    BiPredicate<String,String> bp = String::equals;
}
```
> 被引用方法的参数列表和返回值类型, 必须与函数式接口方法的参数列表和返回值类型一致.

#### 构造器引用

语法格式：类::new
```java
// lambda 写法
@Test
void test7(){
    Supplier<Person> supplier = ()->new Person();
}
// 方法引用
@Test
void test8(){
    Supplier<Person> supplier = Person::new;
}
// Person 类
@Data
public class Person implements Serializable {
    private static final long serialVersionUID = -7008474395345458049L;
    private String name;
    private int age;
    public Person() {
    }
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
}
```
> 注意：person类中有两个构造器，要调用哪个构造器是函数式接口决定的，也就是Supplier接口中的get()方法是无参的，那么就调用的是person中的无参构造器。

#### 数组引用
语法格式：Type::new
```java
// lambda 写法
@Test
void test9(){
    Function<Integer,String[]> fun = x -> new String[x];
}
// 方法引用
@Test
void test10(){
    Function<Integer, String[]> fun = String[]::new;
}
```

### Lambda 异常处理

```java
List<Integer> integers = Arrays.asList(3, 9, 7, 6, 10, 20);
// void forEach(Consumer<? super T> action)
integers.forEach(i -> System.out.println(50 / i));
```
上面的代码当i为0时会引发`ArithmeticException`异常。通常的做法是通过`try…catch`来处理异常，防止系统崩溃。
```java
List<Integer> integers = Arrays.asList(3, 9, 7, 0, 10, 20);
integers.forEach(i -> {
    try {
        System.out.println(50 / i);
    } catch (ArithmeticException e) {
        System.err.println("Arithmetic Exception occured : " + e.getMessage());
    }
});
```
代码不再像以前一样简洁。我们可以通过写一个包装方法来进行处理。
```java
static Consumer<Integer> lambdaWrapper(Consumer<Integer> consumer) {
    return i -> {
        try {
            consumer.accept(i);
        } catch (ArithmeticException e) {
            System.err.println("Arithmetic Exception occured : " + e.getMessage());
        }
    };
}

// 使用
integers.forEach(lambdaWrapper(i -> System.out.println(50 / i)));
```


## Stream
Stream 是什么？  
a sequence of elements from a source that supports data processing operations.  
支持（集合、数组或者I/O）数据处理操作的一系列元素

### 示例

```java
import lombok.AllArgsConstructor;
import lombok.Data;

/**
 * 盘子
 *
 * @author Nousin
 * @since 2020/7/15
 */
@Data
@AllArgsConstructor
public class Dish {
    private String name; // 食物名称
    private boolean vegetarian; // 是否是素菜
    private int calories; // 卡路里
    private Type type; // 类别

    public enum Type { MEAT, FISH, OTHER }
}
```
数据准备
```java
import java.util.Arrays;
import java.util.List;

/**
 * Stream 测试类
 *
 * @author Nousin
 * @since 2020/7/15
 */
public class StreamTest {

    /**
     * 获取菜单信息
     *
     * @return 菜单集合
     */
    public static List<Dish> getData() {
        return Arrays.asList(
                new Dish("pork", false, 800, Dish.Type.MEAT),
                new Dish("beef", false, 700, Dish.Type.MEAT),
                new Dish("chicken", false, 400, Dish.Type.MEAT),
                new Dish("french fries", true, 530, Dish.Type.OTHER),
                new Dish("rice", true, 350, Dish.Type.OTHER),
                new Dish("season fruit", true, 120, Dish.Type.OTHER),
                new Dish("pizza", true, 550, Dish.Type.OTHER),
                new Dish("prawns", false, 300, Dish.Type.FISH),
                new Dish("salmon", false, 450, Dish.Type.FISH));
    }

    public static void main(String[] args) {
        List<Dish> menu = getData();
        // 操作...
    }
}
```
获取卡路里小于400的食物名称（ 使用串行流）
```java
List<String> lowCaloricDishesName = 
        // stream()
        menu.stream()
        // 过滤（中间操作）
        .filter(d -> {
            System.out.println(Thread.currentThread().getName());
            return d.getCalories() < 400;
        })
        // 排序（中间操作）
        .sorted(Comparator.comparing(Dish::getCalories))
        // 方法引用（中间操作）
        .map(Dish::getName)
        // 聚合数据（终端操作）（仅有一个）（触发整条“流水线”方法执行）
        .collect(Collectors.toList());

System.out.println(lowCaloricDishesName);
// main
// main
// main
// main
// main
// main
// main
// main
// main
// main
// [season fruit, prawns, rice]
```

获取卡路里小于400的食物名称（使用并行流）
```java
List<String> lowCaloricDishesName = 
        // parallelStream() 底层使用了 ForkJoin 框架
        menu.parallelStream()
        // 过滤（中间操作）
        .filter(d -> {
            System.out.println(Thread.currentThread().getName());
            return d.getCalories() < 400;
        })
        // 排序（中间操作）
        .sorted(Comparator.comparing(Dish::getCalories))
        // 方法引用（中间操作）
        .map(Dish::getName)
        // 聚合数据（终端操作）（仅有一个）（触发整条“流水线”方法执行）
        .collect(Collectors.toList());

System.out.println(lowCaloricDishesName);
// main
// ForkJoinPool.commonPool-worker-2
// main
// ForkJoinPool.commonPool-worker-3
// ForkJoinPool.commonPool-worker-6
// ForkJoinPool.commonPool-worker-7
// ForkJoinPool.commonPool-worker-4
// ForkJoinPool.commonPool-worker-5
// ForkJoinPool.commonPool-worker-1
// ForkJoinPool.commonPool-worker-2
// [season fruit, prawns, rice]
```

### 获取stream的四种方式
1. 通过`collection`系列集合的`stream()`或`parallelStream()`获取。

2. 通过`Arrays`中的静态方法`stream()`获取数组流。

3. 通过`Stream`中的静态方法`of()`。

4. 创建无限流

```java

// 通过 Arrays 中的静态方法 stream() 获取数组流
void test1(){
    Person[] person = new Person[10];
    Arrays.stream(person);
}
// 通过 Stream 中的静态方法 of()。
void test2(){
    Stream<String> stream = Stream.of("a", "b", "c");
}
// 创建无限流
void test3(){
    Stream<Integer> integerStream = Stream.iterate(0, x -> x + 2);
}
```

### 常用方法操作

1. Intermediate

    * map (mapToInt, flatMap 等)： 类型转换。接收一个函数作为参数，该函数会被应用到每个元素上，并将其映射成一个新的元素。
    * flatMap：接收一个函数作为参数，将流中的每个值都换成另一个流，然后把所有流生成一个流。
    * filter：筛选出符合条件的元素
    * distinct：筛选，通过生成元素的`hashCode()`和`equals()`，去除重复元素。
    * sorted：自然顺序排序，如果该流的元件不是Comparable，抛出java.lang.ClassCastException
    * peek：窥视，这种方法主要存在于支持调试
    * limit(n)：截断流，使其元素不超过给定数量
    * skip(n)：跳过元素，返回一个扔掉前n个元素的流，若不足n个，则返回一个空流。与`limit(n)`互补。
    * parallel：返回一个并行流
    * sequential：返回一个串行流
    * unordered：返回一个无序流

1. Terminal

    * forEach：遍历
    * forEachOrdered：按（原始数据）顺序遍历
    * toArray：转数组
    * reduce：可以将流中元素反复结合起来，得到一个值。
    * collect：将流转化为其他形式。接收一个`Collector`接口的实现。用于给`Stream`中元素做汇总的方法。
    * min：返回流中最小值
    * max：返回流中最大值
    * count：返回流中元素的总数
    * anyMatch：检查是否至少匹配一个元素
    * allMatch：检查是否匹配所有元素
    * noneMatch：检查是否所有元素都不匹配
    * findFirst：返回第一个元素
    * findAny：返回当前流中的任意元素

```java
// sequential 与 parallel
Stream<Integer> s = Stream.of(1, 2, 3, 4);
System.out.println(s.isParallel()); // false

s = s.parallel();
System.out.println(s.isParallel()); // true

s = s.sequential();
System.out.println(s.isParallel()); // false
```

使用 `parallelStream` 注意事项
```java
List<Integer> listOfIntegers = new ArrayList<Integer>(){{ addAll(Arrays.asList(1, 6, 7, 8, 2, 3, 4, 5));}};
List<Integer> parallelStorage = new ArrayList<>();
listOfIntegers.parallelStream()
    // Don't do this! It uses a stateful lambda expression.
    .map(e -> {
        // System.out.printf("线程 %s, 消费：%d \n", Thread.currentThread().getName(), e);
        parallelStorage.add(e);
        return e;
    }).forEachOrdered(e -> System.out.printf("=== 打印元素：%d \n", e));
System.out.println();
parallelStorage.stream().forEachOrdered(e -> System.out.printf("*** 打印元素：%d \n", e));
System.out.println();
// 原始数据打印结果：
// === 打印元素：1 
// === 打印元素：6 
// === 打印元素：7 
// === 打印元素：8 
// === 打印元素：2 
// === 打印元素：3 
// === 打印元素：4 
// === 打印元素：5 
// 结果1（出现空值）：
// *** 打印元素：null 
// *** 打印元素：null 
// *** 打印元素：null 
// *** 打印元素：8 
// *** 打印元素：2 
// *** 打印元素：1 
// *** 打印元素：5 
// *** 打印元素：4 
// 结果2（只有七个元素）：
// *** 打印元素：3 
// *** 打印元素：2 
// *** 打印元素：4 
// *** 打印元素：5 
// *** 打印元素：6 
// *** 打印元素：8 
// *** 打印元素：1 

// ArrayList 源码
/**
  * Appends the specified element to the end of this list.
  *
  * @param e element to be appended to this list
  * @return <tt>true</tt> (as specified by {@link Collection#add})
  */
public boolean add(E e) {
    // 进行扩容 
    // 底层方法：elementData = Arrays.copyOf(elementData, newCapacity);
    ensureCapacityInternal(size + 1);  
    elementData[size++] = e; // 添加元素（size同时被几个线程修改就可能出现null的数据）
    return true;
}

// 解决办法
List<Integer> parallelStorage = Collections.synchronizedList(new ArrayList<>());
```

### 示例
#### list 转 map
```java
public static void mapTest() {
    List<Dish> menu = getData();
    // list 转 map
    menu.stream().collect(Collectors.toMap(Dish::getName, Dish::getCalories, (k1, k2) -> k1))
        .forEach((k, v) -> System.out.printf("k: %s, v: %d \n", k, v));
    // k: season fruit, v: 120
    // k: chicken, v: 400
    // k: pizza, v: 550
    // k: salmon, v: 450
    // k: beef, v: 700
    // k: rice, v: 350
    // k: pork, v: 800
    // k: prawns, v: 300
    // k: french fries, v: 530
}
```

#### 分组与求和
统计，按照是否是素菜分组后菜品卡路里总和
- 方法一
```java
public static void groupTest() {
    List<Dish> menu = getData();
    // 按照是否是 素菜 进行分组
    Map<Boolean, List<Dish>> vegetarianGroup = menu.stream()
        .collect(Collectors.groupingBy(Dish::isVegetarian));
    // 遍历
    vegetarianGroup.forEach((vegetarian, list) -> {
        // 当前组是否是 素菜
        String isVegetarian = vegetarian ? "yes" : "no";
        // 当前组菜单名称
        String names = list.stream().map(Dish::getName).collect(Collectors.joining(","));
        // 当前组卡路里总和
		//int allCalories = list.stream().map(Dish::getCalories).reduce(Integer::sum).orElse(0);
        int allCalories = list.stream().mapToInt(Dish::getCalories).sum();
        System.out.printf("is vegetarian ? %s, they are %s, full calories is %d \n", isVegetarian, names, allCalories);
    });
    // is vegetarian ? no, they are pork,beef,chicken,prawns,salmon. sum calories is 2650
    // is vegetarian ? yes, they are french fries,rice,season fruit,pizza. sum calories is 1550
}
```
- 方法二
```java
public static void groupTest2() {
    List<Dish> menu = getData();
    // 求素菜与荤菜的卡路里总和
    Map<Boolean, Integer> vegetarianSum = menu.stream()
    		.collect(Collectors.groupingBy(Dish::isVegetarian, Collectors.summingInt(Dish::getCalories)));
    // 遍历
    vegetarianSum.forEach((vegetarian, sum) -> {
        // 当前组是否是 素菜
        String isVegetarian = vegetarian ? "yes" : "no";
        System.out.printf("is vegetarian ? %s, sum calories is %d\n", isVegetarian, sum);
    });
    // is vegetarian ? no, sum calories is 2650
    // is vegetarian ? yes, sum calories is 1550
}
```
- 方法三
```java
public static void groupTest3() {
    List<Dish> menu = getData();
    // 求素菜与荤菜的卡路里总和 平均值...
    Map<Boolean, IntSummaryStatistics> vegetarianGroup = menu.stream()
            .collect(Collectors.groupingBy(Dish::isVegetarian, Collectors.summarizingInt(Dish::getCalories)));
    // 遍历
    vegetarianGroup.forEach((vegetarian, statistics) -> {
        // 当前组是否是 素菜
        String isVegetarian = vegetarian ? "yes" : "no";
        System.out.printf("is vegetarian ? %s, sum calories is %d, average is %d\n",
                isVegetarian, statistics.getSum(), (int)statistics.getAverage());
    });
    // is vegetarian ? no, sum calories is 2650, average is 530
    // is vegetarian ? yes, sum calories is 1550, average is 387
}
```
#### 排序
排序-按照素菜、卡路里与名称进行顺序排序
```java
public static void sortTest() {
    List<Dish> menu = getData();
    menu.sort(Comparator.comparing(Dish::isVegetarian)
                .thenComparing(Dish::getCalories)
              	.thenComparing(Dish::getName));
    menu.forEach(System.out::println);
}
// Dish(name=prawns, vegetarian=false, calories=300, type=FISH)
// Dish(name=chicken, vegetarian=false, calories=400, type=MEAT)
// Dish(name=salmon, vegetarian=false, calories=450, type=FISH)
// Dish(name=beef, vegetarian=false, calories=700, type=MEAT)
// Dish(name=pork, vegetarian=false, calories=800, type=MEAT)
// Dish(name=season fruit, vegetarian=true, calories=120, type=OTHER)
// Dish(name=rice, vegetarian=true, calories=350, type=OTHER)
// Dish(name=french fries, vegetarian=true, calories=530, type=OTHER)
// Dish(name=pizza, vegetarian=true, calories=550, type=OTHER) 
```

## 新的日期时间 API
### 认识新的日期API类
- Instant：时间戳
- Duration：持续时间、时间差
- LocalDate：只包含日期，比如：2020-08-01
- LocalTime：只包含时间，比如：10:32:10
- LocalDateTime：包含日期和时间，比如：2020-08-01 10:32:10
- Peroid：时间段
- ZoneOffset：时区偏移量，比如：+8:00
- ZonedDateTime：带时区的日期时间
- Clock：时钟，可用于获取当前时间戳
- java.time.format.DateTimeFormatter：时间格式化类

#### 构造

```java
public static void main(String[] args) {
    // 系统时间
    System.out.println(LocalDate.now()); // 2020-08-01
    System.out.println(LocalDateTime.now()); // 2020-08-01T00:33:27.743
    // 指定时间
    System.out.println(LocalDate.of(2020, 1, 1)); // 2020-01-01
    System.out.println(LocalDateTime.of(2020, 1, 1, 0, 0, 0)); // 2020-01-01T00:00
}
```
#### 时间推移
```java
public static void main(String[] args) {
    // 当前时间
    System.out.println(LocalDate.now()); // 2020-08-01
    // 当前时间向后推一个月零4天
    System.out.println(LocalDate.now().plusMonths(1).plusDays(4)); // 2020-09-05
}
```
#### 时区
```java
public static void main(String[] args) {
    // 上海时间
    ZoneId shanghaiZoneId = ZoneId.of("Asia/Shanghai");// 时区参数参照：java.time.ZoneId#SHORT_IDS
    ZonedDateTime shanghaiZonedDateTime = ZonedDateTime.now(shanghaiZoneId);
    // 东京时间
    ZoneId tokyoZoneId = ZoneId.of("Asia/Tokyo");
    ZonedDateTime tokyoZonedDateTime = ZonedDateTime.now(tokyoZoneId);
    // 格式化
    DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
    System.out.println("上海时间: " + shanghaiZonedDateTime.format(formatter)); // 上海时间: 2020-08-01 00:38:08
    System.out.println("东京时间: " + tokyoZonedDateTime.format(formatter)); // 东京时间: 2020-08-01 01:38:08
}
```
#### 解析日期
```java
public static void main(String[] args) {
    // 解析日期
    String dateText = "20200801";
    LocalDate date = LocalDate.parse(dateText, DateTimeFormatter.BASIC_ISO_DATE);
    System.out.println("格式化之后的日期=" + date); // 格式化之后的日期=2020-08-01
}
```

### `LocalDateTime` 与 ` Date` 相互转化
```java
public static void main(String[] args) {
    // 方法一：
    LocalDateTime localDateTime = new Date().toInstant().atZone(ZoneId.systemDefault()).toLocalDateTime();
    System.out.println(localDateTime); // 2020-08-01T00:47:15.327
    
    // 方法二：
    LocalDateTime localDateTime1 = LocalDateTime.ofInstant(new Date().toInstant(), ZoneId.systemDefault());
    System.out.println(localDateTime1); // 2020-08-01T00:47:15.327
}
```
```java
public static void main(String[] args) {
    Date date = Date.from(LocalDateTime.now().atZone(ZoneId.systemDefault()).toInstant());
    System.out.println(date); // Sat Aug 01 00:51:56 CST 2020
}
```

## Optional 类

Optional类是一个容器类，代表一个值存在或不存在，原来用null表示一个值不存在，现在Optional可以更好的表达这个概念。并且可以避免空指针异常。
### 常用方法
1. Optional.of(T t) ——创建一个Optional实例
2. Optional.empty()——创建一个空的optional实例
3. **Optional.ofNullable(T t)**——若t不为null，创建optional实例，否则创建空实例
4. isPresent()——判断是否包含值
5. **orElse(T t)**——如果调用对象包含值，返回该值，否则返回 t
6. orElseGet(Supplier s)——如果调用对象包含值，返回该值，否则返回 s 获取的值
7. map(Function f)——如果有值对其处理，并返回处理后的Optional，否则返回Optional.empty()
8. flatMap(Function mapper)——与map类似，要求返回值必须是Optional

```java
Integer i = null;
System.out.println(Optional.ofNullable(i).orElse(0));
```
