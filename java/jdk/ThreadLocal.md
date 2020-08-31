# ThreadLocal

[参考视频](https://www.bilibili.com/video/BV1fA411b7SX?from=search&seid=4906623059542053557)

重写 finalize 会导致 FGC，原因是导致对象回收时间变



## Java 中的引用类型

- 强引用：变量不可达时进行回收

```java
Object o = new Object(); // 强引用
```

- 软引用：内存不够时进行回收

```java
// sf -> new SoftReference<>() 是强引用
// new SoftReference<>() -> new Object() 来说是软引用
SoftReference<Object> sf = new SoftReference<>(new Object());
```

使用场景：做缓存

- 弱引用：**GC 时直接被回收**

```java
// wf -> new WeakReference<>() 是强引用
// new WeakReference<>() -> Object 来说是软引用，GC 时直接被回收
WeakReference<Object> wf = new WeakReference<>(new Object());
```

- 虚引用：直接管理内存

```java
// pr -> new PhantomReference<>() 是强引用
// new PhantomReference<>() -> Object 来说是虚引用
PhantomReference<> pr = new PhantomReference(new Object());
```

## ThreadLocal 源码分析

### 类说明


```java
/**
 * This class provides thread-local variables.  These variables differ from
 * their normal counterparts in that each thread that accesses one (via its
 * {@code get} or {@code set} method) has its own, independently initialized
 * copy of the variable.  {@code ThreadLocal} instances are typically private
 * static fields in classes that wish to associate state with a thread (e.g.,
 * a user ID or Transaction ID).
 *
 * <p>For example, the class below generates unique identifiers local to each
 * thread.
 * A thread's id is assigned the first time it invokes {@code ThreadId.get()}
 * and remains unchanged on subsequent calls.
 * <pre>
 * import java.util.concurrent.atomic.AtomicInteger;
 *
 * public class ThreadId {
 *     // Atomic integer containing the next thread ID to be assigned
 *     private static final AtomicInteger nextId = new AtomicInteger(0);
 *
 *     // Thread local variable containing each thread's ID
 *     private static final ThreadLocal&lt;Integer&gt; threadId =
 *         new ThreadLocal&lt;Integer&gt;() {
 *             &#64;Override protected Integer initialValue() {
 *                 return nextId.getAndIncrement();
 *         }
 *     };
 *
 *     // Returns the current thread's unique ID, assigning it if necessary
 *     public static int get() {
 *         return threadId.get();
 *     }
 * }
 * </pre>
 * <p>Each thread holds an implicit reference to its copy of a thread-local
 * variable as long as the thread is alive and the {@code ThreadLocal}
 * instance is accessible; after a thread goes away, all of its copies of
 * thread-local instances are subject to garbage collection (unless other
 * references to these copies exist).
 *
 * @author  Josh Bloch and Doug Lea
 * @since   1.2
 */
public class ThreadLocal<T> {
  // ...
}
```

翻译：

这个类提供线程局部变量。这些变量与普通的变量不同，因为每个访问的线程(通过其get或set方法)都有自己的**独立初始化**的变量副本。ThreadLocal实例通常是希望将状态与线程关联的类中的**私有静态(private static)**字段(例如:一个用户ID或事务ID)。

例如，类下面生成本地给每个线程的唯一标识符。 线程的ID被分配在第一次调用ThreadId.get()并在后续调用不变。

```java
import java.util.concurrent.atomic.AtomicInteger;

public class ThreadId {
    // Atomic integer containing the next thread ID to be assigned
    private static final AtomicInteger nextId = new AtomicInteger(0);
    // Thread local variable containing each thread's ID
    private static final ThreadLocal<Integer> threadId = new ThreadLocal<Integer>() {
         @Override 
         protected Integer initialValue() {
             return nextId.getAndIncrement();
        }       
    };
      
    // Returns the current thread's unique ID, assigning it if necessary
    public static int get() {
        return threadId.get();
    }
}
```
只要线程存活并且ThreadLocal实例可以访问，每个线程都保存对其线程局部变量副本的**弱引用**; 线程结束之后，线程本地实例的所有副本都将被垃圾回收（除非存在对这些副本的其他引用）。

### 使用










为什么 Entry 使用弱引用 ？

使用场景：Spring 处理 @Transactional 事务处理场景（JDBCTemplate,...等模板Bean访问底层数据）；Mybatis 分页处理场景；