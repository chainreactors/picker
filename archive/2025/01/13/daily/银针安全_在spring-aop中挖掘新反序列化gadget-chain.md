---
title: 在spring-aop中挖掘新反序列化gadget-chain
url: https://mp.weixin.qq.com/s?__biz=Mzg2MDY2ODc5MA==&mid=2247484198&idx=1&sn=6b6a82bb543e879295b7cd2d85f3a37f&chksm=ce23953ff9541c29418831b4e192b385e5c92d59562b40a7a28283e8468773caac9ad9736b1c&scene=58&subscene=0#rd
source: 银针安全
date: 2025-01-13
fetch_date: 2025-10-06T20:09:59.045796
---

# 在spring-aop中挖掘新反序列化gadget-chain

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/HwHmjibphiaE3mJ1NPaWuBoCCR5IsiaXqbTca8PEeVvPX5cj5TUYfNuz8MmpUomdH0urEm5sJcGqTKv8yKrvNAAog/0?wx_fmt=jpeg)

# 在spring-aop中挖掘新反序列化gadget-chain

原创

Ape1ron

银针安全

#### 目录

* • 前言
* • 挖掘过程

+ • AbstractAspectJAdvice
+ • ReflectiveMethodInvocation
+ • JdkDynamicAopProxy

* • 调用链
* • 代码示例

## 前言

前阵子在某个安全会议面基，和@jsjcw和@杨悦师傅交流的时候，他们透露最近新挖了一条仅依赖spring-aop的java原生反序列化gadget-chain，但没提到详情。

前天笔者正好在整理今年的一些笔记，有部分资料也和反序列化相关，就想起来了这个事情。于是就想挑战一下自己是否也能独立从spring-aop挖一条反序列化gadget-chain，最终运气不错，发现了一条gadget-chain，所需依赖为：spring-aop + aspectjweaver，能力是反射调用方法。

## 挖掘过程

### AbstractAspectJAdvice

通过污点搜索和分析，注意到了`org.springframework.aop.aspectj.AbstractAspectJAdvice`这个类：即使在反序列化之后，也天然拥有反射调用方法的能力（因为Method本身并不能反序列化，所以这种情况并不多见）

1. 1. invokeAdviceMethodWithGivenArgs方法有反射调用方法的能力
2. 2. readObject之后通过反射重新实例化了aspectJAdviceMethod属性

```
// invokeAdviceMethodWithGivenArgs.java
privatefinal Class<?> declaringClass;
privatefinal String methodName;
privatefinal Class<?>[] parameterTypes;
protectedtransient Method aspectJAdviceMethod;

protected Object invokeAdviceMethodWithGivenArgs(Object[] args)throws Throwable {
    Object[] actualArgs = args;
    if (this.aspectJAdviceMethod.getParameterCount() == 0) {
        actualArgs = null;
    }
    try {
        ReflectionUtils.makeAccessible(this.aspectJAdviceMethod);
        returnthis.aspectJAdviceMethod.invoke(this.aspectInstanceFactory.getAspectInstance(), actualArgs);
    }
    ...
}

privatevoidreadObject(ObjectInputStream inputStream)throws IOException, ClassNotFoundException {
    inputStream.defaultReadObject();
    try {
        this.aspectJAdviceMethod = this.declaringClass.getMethod(this.methodName, this.parameterTypes);
    }
    ...
}
```

反射调用方法的三要素：Method、Object、Args，虽然还不清楚`invokeAdviceMethodWithGivenArgs`中传入的args是否可控，但可以先简化场景，对于无参方法肯定是可行的，而公开的无参利用方法中就有不少，可以暂时认为Method和Args都解决了。

现在还要解决Object的问题，代码中通过`this.aspectInstanceFactory.getAspectInstance()`获取反射对象。此时目标是找到一个同时实现`AspectInstanceFactory`和`Serializable`的子类，并且`getAspectInstance`方法可以返回指定的对象。

`org.springframework.aop.aspectj.SingletonAspectInstanceFactory`刚好满足。

![](https://mmbiz.qpic.cn/mmbiz_png/HwHmjibphiaE3mJ1NPaWuBoCCR5IsiaXqbTUkCUTuQQbmCbibD6PPSvXBOHficIb3biaWox091aynPxjC7vbwz3iaw6OQ/640?wx_fmt=png&from=appmsg "null")

到这里，`org.springframework.aop.aspectj.AbstractAspectJAdvice#invokeAdviceMethodWithGivenArgs`可以作为污点方法就基本定下来了。

### ReflectiveMethodInvocation

接下来往上找调用链，多条调用链都会经过`org.springframework.aop.framework.ReflectiveMethodInvocation#proceed`走到`org.springframework.aop.aspectj.AbstractAspectJAdvice#invokeAdviceMethodWithGivenArgs`。例如：

```
org.springframework.aop.framework.ReflectiveMethodInvocation#proceed->
org.springframework.aop.aspectj.AspectJAroundAdvice#invoke->
org.springframework.aop.aspectj.AbstractAspectJAdvice#invokeAdviceMethod(org.aspectj.lang.JoinPoint, org.aspectj.weaver.tools.JoinPointMatch, java.lang.Object, java.lang.Throwable)->
org.springframework.aop.aspectj.AbstractAspectJAdvice#invokeAdviceMethodWithGivenArgs
```

`ReflectiveMethodInvocation#proceed`方法如下：

![](https://mmbiz.qpic.cn/mmbiz_png/HwHmjibphiaE3mJ1NPaWuBoCCR5IsiaXqbTnsgV3Rs1S5iaNNhZ6ceu26CvOUYdWQznjV4gbicUXVTy1ge23WofxQsw/640?wx_fmt=png&from=appmsg "null")

第一个点是`interceptorOrInterceptionAdvice`的获取，是从`interceptorsAndDynamicMethodMatchers`中拿到的，该属性本身定义就是一个List，可以序列化，而索引currentInterceptorIndex本身也只是int类型。因此可以认为`interceptorOrInterceptionAdvice`是可控的。

第二个点是`interceptorOrInterceptionAdvice`的类型，按照笔者上面的调用链，这个对象的类型是`org.springframework.aop.aspectj.AspectJAroundAdvice`（`AbstractAspectJAdvice`的子类），那么`proceed`代码是走下面的分支，省去了一部分麻烦：）

![](https://mmbiz.qpic.cn/mmbiz_png/HwHmjibphiaE3mJ1NPaWuBoCCR5IsiaXqbTPyqQopUCOxjjasssuPYbjHKBkTz5cGNrvBHibyCw8F3KNqjyWjdC4PA/640?wx_fmt=png&from=appmsg "null")

第三个点是`ReflectiveMethodInvocation`本身并没有实现Serializable接口，想要在反序列化过程中使用，只能依赖于动态创建。直接往上找到创建`ReflectiveMethodInvocation`的地方，发现正是熟悉的老朋友`org.springframework.aop.framework.JdkDynamicAopProxy#invoke`。并且在创建后刚好就调用proceed方法，完美符合要求。

![](https://mmbiz.qpic.cn/mmbiz_png/HwHmjibphiaE3mJ1NPaWuBoCCR5IsiaXqbTFDNicKUhEbtiavoibJ7v5oicus34LuY9LJulR473p7DRaLpNxCz4LqPBYw/640?wx_fmt=png&from=appmsg "null")

分析`ReflectiveMethodInvocation`的构造方法，需要控制传入的`interceptorsAndDynamicMethodMatchers`，也即对应了上面`JdkDynamicAopProxy#invoke`中的chain。

![](https://mmbiz.qpic.cn/mmbiz_png/HwHmjibphiaE3mJ1NPaWuBoCCR5IsiaXqbTwsRcU6YeqTh0OOI4sNMyCpkYoqUxPDzibl3j4RiaO1VWG1lOkMahibiciag/640?wx_fmt=png&from=appmsg "null")

到这里为止，梳理一下目前的思路：

1. 1. 通过反序列化触发`JdkDynamicAopProxy#invoke`方法，这个简单，本身就是动态代理。
2. 2. 在`JdkDynamicAopProxy#invoke`方法中，控制chain的生成，需要让List放入目标对象`AspectJAroundAdvice`
3. 3. 通过chain创建出`ReflectiveMethodInvocation`实例，并调用其proceed方法

```
...
List<Object> chain = this.advised.getInterceptorsAndDynamicInterceptionAdvice(method, targetClass);
if (chain.isEmpty()) {
    Object[] argsToUse = AopProxyUtils.adaptArgumentsIfNecessary(method, args);
    retVal = AopUtils.invokeJoinpointUsingReflection(target, method, argsToUse);
}
else {
    MethodInvocation invocation =
            new ReflectiveMethodInvocation(proxy, target, method, args, targetClass, chain);
    retVal = invocation.proceed();
}
...
```

1. 4. 通过`ReflectiveMethodInvocation#proceed` -> `AspectJAroundAdvice#invoke`->`AbstractAspectJAdvice#invokeAdviceMethodWithGivenArgs`，走到最后的污点函数，反射调用执行代码。

### JdkDynamicAopProxy

接下来就是解决在`JdkDynamicAopProxy#invoke`方法中，控制chain变量的生成过程。

```
List<Object> chain = this.advised.getInterceptorsAndDynamicInterceptionAdvice(method, targetClass);
```

目标是让`getInterceptorsAndDynamicInterceptionAdvice`返回一个List，List里面有一个元素，是我们指定的任意对象。

分析`org.springframework.aop.framework.AdvisedSupport#getInterceptorsAndDynamicInterceptionAdvice`方法，实际上有两个获取方式：

1. 1. 从缓存的methodCache中获取
2. 2. 通过getInterceptorsAndDynamicInterceptionAdvice方法

```
public List<Object> getInterceptorsAndDynamicInterceptionAdvice(Method method, @Nullable Class<?> targetClass) {
    MethodCacheKey cacheKey = new MethodCacheKey(method);
    List<Object> cached = this.methodCache.get(cacheKey);
    if (cached == null) {
        cached = this.advisorChainFactory.getInterceptorsAndDynamicInterceptionAdvice(
                this, method, targetClass);
        this.methodCache.put(cacheKey, cached);
    }
    return cached;
}
```

先看了一下methodCache属性，本身加了`transient`修饰符，并且在`readObject`方法中是直接新建的，没有任何元素，判断这条路是不可行的。

![](https://mmbiz.qpic.cn/mmbiz_png/HwHmjibphiaE3mJ1NPaWuBoCCR5IsiaXqbTQDLajaIZ65UL3rTlR8qyzpKia3tVDLm4oQoNO21PL0kzzT0Libm74nLw/640?wx_fmt=png&from=appmsg "null")

然后再分析`getInterceptorsAndDynamicInterceptionAdvice`是否可用，在这个方法中，三个入参都是可控的，`Advised config`实际上就是`AdvisedSupport`实例。

这个方法最终返回的就是`interceptorList`对象，核心是分析这个对象如何添加元素，然后往上找这个元素是怎么生成的。

```
public List<Object> getInterceptorsAndDynamicInterceptionAdvice(
        Advised config, Method method, @Nullable Class<?> targetClass) {

    AdvisorAdapterRegistryregistry= GlobalAdvisorAdapterRegistry.getInstance();
    Advisor[] advisors = config.getAdvisors();
    List<Object> interceptorList = newArrayList<>(advisors.length);
    Class<?> actualClass = (targetClass != null ? targetClass : method.getDeclaringClass());
    BooleanhasIntroductions=null;

    for (Advisor advisor : advisors) {
        if (advisor instanceof PointcutAdvisor) {
            if (config.isPreFiltered() || pointcutAdvisor.getPointcut().getClassFilter().matches(actualClass)) {
                MethodMatchermm= pointcutAdvisor.getPointcut().getMethodMatcher();
                boolean match;
                if (mm instanceof IntroductionAwareMethodMatcher) {
                    if (hasIntroductions == null) {
                        hasIntroductions = hasMatchingIntroductions(advisors, actualClass);
                    }
                    match = ((IntroductionAwareMethodMatcher) mm).matches(method, actualClass, hasIntroductions);
                }
                else {
                    match = mm.matches(method, actualClass);
                }
                if (match) {
                    MethodInterceptor[] interceptors = registry.getInterceptors...