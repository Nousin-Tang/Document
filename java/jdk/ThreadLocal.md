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

使用场景：Spring 处理 @Transactional 事务处理场景（JDBCTemplate,...等模板Bean访问底层数据）；Mybatis 分页处理场景；

### ThreadLocal 在 Java doc 解释

这个类提供线程局部变量。这些变量与普通的变量不同，因为每个访问的线程(通过其get或set方法)都有自己的**独立初始化**的变量副本。ThreadLocal实例通常是（希望将状态与线程关联的）类中的**私有静态(private static)**变量，(如:一个用户ID或事务ID)。

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

### 类成员变量

```java
ThreadLocals依靠每线程线性探针哈希映射附连到每个线程（Thread.threadLocals和inheritableThreadLocals）。 ThreadLocal的对象作为钥匙，通过搜索threadLocalHashCode。 这是自定义的散列码（仅在ThreadLocalMaps有用），其连续地在那里构成ThreadLocals由相同的线程中使用，而其余的在通常情况下消除在碰撞不太常见的情况下表现良好。

/**
 * ThreadLocals 依赖每一个线程
 * ThreadLocals rely on per-thread linear-probe hash maps attached
 * to each thread (Thread.threadLocals and
 * inheritableThreadLocals).  The ThreadLocal objects act as keys,
 * searched via threadLocalHashCode.  This is a custom hash code
 * (useful only within ThreadLocalMaps) that eliminates collisions
 * in the common case where consecutively constructed ThreadLocals
 * are used by the same threads, while remaining well-behaved in
 * less common cases.
 */
private final int threadLocalHashCode = nextHashCode();

/**
 * The next hash code to be given out. Updated atomically. Starts at
 * zero.
 */
private static AtomicInteger nextHashCode = new AtomicInteger();

/**
 * The difference between successively generated hash codes - turns
 * implicit sequential thread-local IDs into near-optimally spread
 * multiplicative hash values for power-of-two-sized tables.
 */
private static final int HASH_INCREMENT = 0x61c88647; // (十进制)1640531527 = 2^32*0.618（0.618，既黄金比例，斐波拉契数列）

/**
 * Returns the next hash code.
 */
private static int nextHashCode() {
    return nextHashCode.getAndAdd(HASH_INCREMENT);
    // 每次的执行结果在 Integer.MIN_VALUE 与 Integer.MAX_VALUE 之间
  	// 1253254570
  	// -1401181199
  	// 239350328
  	// 1879881855
}

// ------------- 引用方法 -------------
// AtomicInteger 中的 getAndAdd()
public final int getAndAdd(int delta) { // delta == 1640531527
    return unsafe.getAndAddInt(this, valueOffset, delta); // valueOffset == 12
}

// Unsafe 类中的 getAndAddInt() 
public final int getAndAddInt(Object var1, long var2, int var4) {
    int var5;
    do {
        var5 = this.getIntVolatile(var1, var2);
    } while(!this.compareAndSwapInt(var1, var2, var5, var5 + var4));

    return var5;
}
```

### set() 方法

```java
/**
 * 设置当前线程的关联的这个ThreadLocal变量的副本到指定的值。
 * 大部分子类将不需要重写这个方法，专靠initialValue方法来设置线程局部变量的值
 * Sets the current thread's copy of this thread-local variable
 * to the specified value.  Most subclasses will have no need to
 * override this method, relying solely on the {@link #initialValue}
 * method to set the values of thread-locals.
 *
 * @param value the value to be stored in the current thread's copy of this thread-local.
 */
public void set(T value) {
    // 获取当前线程
    Thread t = Thread.currentThread();
    // 获取线程中的 ThreadLocalMap
    ThreadLocalMap map = getMap(t); // thread.threadLocals;
    // ThreadLocalMap 已经初始化
    if (map != null)
        map.set(this, value); // 调用 ThreadLocal 中的静态类 ThreadLocalMap 中的 set() 方法
    // ThreadLocalMap 未初始化
    else
        createMap(t, value);
}

/**
 * 创建一个关联当前 ThreadLocal 的 ThreadLocalMap 对象；初始化时并设值
 */
void createMap(Thread t, T firstValue) {
    t.threadLocals = new ThreadLocalMap(this, firstValue);
}
```


### get() 方法

```java
/**
 * Returns the value in the current thread's copy of this
 * thread-local variable.  If the variable has no value for the
 * current thread, it is first initialized to the value returned
 * by an invocation of the {@link #initialValue} method.
 *
 * @return the current thread's value of this thread-local
 */
public T get() {
    Thread t = Thread.currentThread();
    ThreadLocalMap map = getMap(t);
    if (map != null) {
        ThreadLocalMap.Entry e = map.getEntry(this);
        if (e != null) {
            @SuppressWarnings("unchecked")
            T result = (T)e.value;
            return result;
        }
    }
    return setInitialValue();
}

/**
 * Variant of set() to establish initialValue. Used instead
 * of set() in case user has overridden the set() method.
 *
 * @return the initial value
 */
private T setInitialValue() {
    T value = initialValue();
    Thread t = Thread.currentThread();
    ThreadLocalMap map = getMap(t);
    if (map != null)
        map.set(this, value);
    else
        createMap(t, value);
    return value;
}

protected T initialValue() {
    return null;
}
```



### remove() 方法

```java
/**
 * Removes the current thread's value for this thread-local
 * variable.  If this thread-local variable is subsequently
 * {@linkplain #get read} by the current thread, its value will be
 * reinitialized by invoking its {@link #initialValue} method,
 * unless its value is {@linkplain #set set} by the current thread
 * in the interim.  This may result in multiple invocations of the
 * {@code initialValue} method in the current thread.
 *
 * @since 1.5
 */
public void remove() {
    ThreadLocalMap m = getMap(Thread.currentThread());
    if (m != null)
        m.remove(this); // 调用 ThreadLocal 中的静态类 ThreadLocalMap 中的 remove() 方法
}
```



### **ThreadLocalMap**

#### 内部类与成员变量与简单方法

```java
/**
 * The entries in this hash map extend WeakReference, using
 * its main ref field as the key (which is always a ThreadLocal object).  
 * Note that null keys (i.e. entry.get() == null) mean that the key is no longer referenced, so the
 * entry can be expunged（清除） from table.  Such entries are referred to
 * as "stale entries" in the code that follows.
 */
static class Entry extends WeakReference<ThreadLocal<?>> {
    /** The value associated with this ThreadLocal. */
    Object value;

    Entry(ThreadLocal<?> k, Object v) {
        super(k);
        value = v;
    }
}

/**
 * 初始化容量 -- 必须为2的指数
 */
private static final int INITIAL_CAPACITY = 16;

/**
 * Entry 数组，数组长度必须为2的指数.
 */
private Entry[] table;

/**
 * The number of entries in the table.
 */
private int size = 0;

/**
 * The next size value at which to resize.
 */
private int threshold; // Default to 0

/**
 * Set the resize threshold to maintain at worst a 2/3 load factor.
 */
private void setThreshold(int len) {
    threshold = len * 2 / 3;
}

/**
 * Increment i modulo len.
 */
private static int nextIndex(int i, int len) {
    return ((i + 1 < len) ? i + 1 : 0);
}

/**
 * Decrement i modulo len.
 */
private static int prevIndex(int i, int len) {
    return ((i - 1 >= 0) ? i - 1 : len - 1);
}
```

#### 构造方法

#### getEntry() 方法

#### set() 方法

#### resize() 方法

#### remove() 方法





