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
        //
    }
};

/**如果是创建一个线程可以这样*/
Thread thread = new Thread(new Runnable() {
    @Override
    public void run() {
        //
    }
});
```
通过 Lambda 表达式创建
```java
/**创建一个Runnable接口的实例*/
Runnable runnable = () -> {
    //
};

/**如果是创建一个线程可以这样*/
Thread thread = new Thread(() -> {
    //
});
```
### Lambda 表达式定义

> 它们通过使用表达式来提供一种<font color="red">清晰简洁</font>的方式来表示<font color="red">方法接口</font>。

#### 格式

```java
// 1. 方法体内部只有一个表达式时，‘{}’ 可以省略
() -> System.out.print("Hello World!")

// 2. 接口方法只有一个参数时，‘()’可以省略
name -> System.out.print("Hello " + name + "!")

// 3. 参数的类型可以不用写
// 4. 可选的返回关键字return：如果主体只有一个表达式返回值则可以省略return和{}
(x, y) -> x – y
(int x, int y) -> x + y
```
#### 使用条件
- 接口中有且只能有一个抽象方法，默认方法静态方法不受影响

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

- lambda 表达式只能引用标记了 `final` 的外层局部变量，这就是说不能在 lambda 内部修改定义在域外的局部变量，否则会编译错误。如果未标记`final` ，会将变量当成 final 的。
- lambda 表达式的局部变量可以不用声明为 `final`，但是必须不可被后面的代码修改（即隐性的具有 `final` 的语义）。
- 在 Lambda 表达式当中不允许声明一个与局部变量同名的参数或者局部变量。


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
        System.err.println(
          "Arithmetic Exception occured : " + e.getMessage());
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
            System.err.println(
              "Arithmetic Exception occured : " + e.getMessage());
        }
    };
}

// 使用
integers.forEach(lambdaWrapper(i -> System.out.println(50 / i)));
```

### 方法引用
方法引用分为静态方法的方法引用和实例方法的方法引用。

语法形式如下:

```java
类型名:: 静态方法 // 静态方法的方法引用
类型名:: 实例方法 // 实例方法的方法引用
```
> 被引用方法的参数列表和返回值类型, 必须与函数式接口方法的参数列表和返回值类型一致.



### 函数式接口（Functional Interface）

>  是指指只有一个抽象方法的接口。（默认实现不算）

#### Java8内置函数式接口(java.util.function)
- **Predicate**：boolean test(T t);
- **Consumer**： void accept(T t);
- **Function**： R apply(T t);
- **Supplier** ：T get();
- **BiPredicate** ：boolean test(T t, U u);
- **BiConsumer** ：void accept(T t, U u);
- **BiFunction** ： R apply(T t, U u);


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
获取卡路里小于400的食物名称  - 使用串行流
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

获取卡路里小于400的食物名称 - 使用并行流
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

### 常用方法操作

1. Intermediate

    * map (mapToInt, flatMap 等): 类型转换
    * filter: 筛选出符合条件的元素
    * distinct: 去重(调用Object#equals)
    * sorted: 自然顺序排序, 如果该流的元件不是Comparable，抛出java.lang.ClassCastException
    * peek: 窥视, 这种方法主要存在于支持调试
    * limit: 限制流中的元素个数, 获取前n条数据
    * skip: 跳过前n个元素
    * parallel: 
    * sequential
    * unordered

1. Terminal

    * forEach
    * forEachOrdered
    * toArray
    * reduce
    * collect
    * min
    * max
    * count
    * anyMatch
    * allMatch
    * noneMatch
    * findFirst
    * findAny
    * iterator

1. Short-circuiting

    * anyMatch
    * allMatch
    * noneMatch
    * findFirst
    * findAny
    * limit


## 新的日期时间 API


## Optional 类



## 方法引用



## 函数式接口



## 接口支持默认方法
