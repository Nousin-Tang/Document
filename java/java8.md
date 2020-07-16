# Java8 新特性

[TOC]

## Lambda 表达式



## Stream
Stream 是什么？  
a sequence of elements from a source that supports data processing operations.  
支持（集合、数组或者I/O）数据处理操作的一系列元素

示例：
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
获取卡路里小于400的食物名称
```java
List<String> lowCaloricDishesName = 
        // parallelStream() 底层使用了 ForkJoin 框架
        menu.parallelStream()
        // 过滤（中间操作）
        .filter(d -> d.getCalories() < 400) 
        // 排序（中间操作）
        .sorted(Comparator.comparing(Dish::getCalories))
        // 方法引用（中间操作）
        .map(Dish::getName)
        // 聚合数据（终端操作）（仅有一个）（触发整条“流水线”方法执行）
        .collect(Collectors.toList());

System.out.println(lowCaloricDishesName);
// [season fruit, prawns, rice]
```

### 常用方法操作

1. Intermediate

    * map (mapToInt, flatMap 等): 类型转换
    * filter: 筛选出符合条件的元素
    * distinct: 去重(调用Object#equals)
    * sorted: 自然顺序排序, 如果该流的元件不是Comparable，抛出java.lang.ClassCastException
    * peek: 窥视, 
    * limit
    * skip
    * parallel
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
