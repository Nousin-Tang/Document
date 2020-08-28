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

- 弱引用

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

## ThreadLocal

