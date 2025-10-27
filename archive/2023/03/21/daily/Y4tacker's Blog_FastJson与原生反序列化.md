---
title: FastJson与原生反序列化
url: https://y4tacker.github.io/2023/03/20/year/2023/3/FastJson%E4%B8%8E%E5%8E%9F%E7%94%9F%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96/
source: Y4tacker's Blog
date: 2023-03-21
fetch_date: 2025-10-04T10:07:01.368972
---

# FastJson与原生反序列化

* [Home](/)
* [Writing](/archives/)
* [Topics](/tags/)
* [Search](/search/)
* [About](/about/)
* [Friends](/link/)

Previous post Next post Back to top Share post

1. [1. FastJson与原生反序列化](#FastJson%E4%B8%8E%E5%8E%9F%E7%94%9F%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96)
   1. [1.1. 前言](#%E5%89%8D%E8%A8%80)
   2. [1.2. 利用与限制](#%E5%88%A9%E7%94%A8%E4%B8%8E%E9%99%90%E5%88%B6)
   3. [1.3. 寻找](#%E5%AF%BB%E6%89%BE)
   4. [1.4. 如何触发getter方法](#%E5%A6%82%E4%BD%95%E8%A7%A6%E5%8F%91getter%E6%96%B9%E6%B3%95)
   5. [1.5. 组合利用链](#%E7%BB%84%E5%90%88%E5%88%A9%E7%94%A8%E9%93%BE)
      1. [1.5.1. fastjson1](#fastjson1)
      2. [1.5.2. fastjson2](#fastjson2)
   6. [1.6. 为什么fastjson1的1.2.49以后不再能利用](#%E4%B8%BA%E4%BB%80%E4%B9%88fastjson1%E7%9A%841-2-49%E4%BB%A5%E5%90%8E%E4%B8%8D%E5%86%8D%E8%83%BD%E5%88%A9%E7%94%A8)

# FastJson与原生反序列化

Y4tacker

2023-03-20 (Updated: 2024-08-04)

[Java](/categories/Java/)

[Fastjson](/tags/Fastjson/), [Java](/tags/Java/)

# FastJson与原生反序列化

## 前言

这其实是我很早前遇到的一个秋招面试题，问题大概是如果你遇到一个较高版本的FastJson有什么办法能绕过AutoType么？我一开始回答的是找黑名单外的类，后面面试官说想考察的是FastJson在原生反序列化当中的利用。因为比较有趣加上最近在网上也看到类似的东西，今天也就顺便在肝毕设之余来谈谈这个问题。

## 利用与限制

Fastjson1版本小于等于1.2.48

Fastjson2目前通杀(目前最新版本2.0.26)

## 寻找

既然是与原生反序列化相关，那我们去fastjson包里去看看哪些类继承了Serializable接口即可，最后找完只有两个类，JSONArray与JSONObject，这里我们就挑第一个来讲(实际上这两个在原生反序列化当中利用方式是相同的)

首先我们可以在IDEA中可以看到，虽然JSONArray有implement这个Serializable接口但是它本身没有实现readObject方法的重载，并且继承的JSON类同样没有readObject方法，那么只有一个思路了，通过其他类的readObject做中转来触发JSONArray或者JSON类当中的某个方法最终实现串链

在Json类当中的toString方法能触发toJsonString的调用，而这个东西其实我们并不陌生，在我们想用JSON.parse()触发get方法时，其中一个处理方法就是用JSONObject嵌套我们的payload

![image-20230320134010936](/2023/03/20/year/2023/3/FastJson%E4%B8%8E%E5%8E%9F%E7%94%9F%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96/image-20230320134010936.png)

那么思路就很明确了，触发toString->toJSONString->get方法，

## 如何触发getter方法

这里多提一句为什么能触发get方法调用

因为是toString所以肯定会涉及到对象中的属性提取，fastjson在做这部分实现时，是通过ObjectSerializer类的write方法去做的提取

![image-20230320134844206](/2023/03/20/year/2023/3/FastJson%E4%B8%8E%E5%8E%9F%E7%94%9F%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96/image-20230320134844206.png)

这部分流程是先判断serializers这个HashMap当中有无默认映射

![image-20230320134927354](/2023/03/20/year/2023/3/FastJson%E4%B8%8E%E5%8E%9F%E7%94%9F%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96/image-20230320134927354.png)

我们可以来看看有哪些默认的映射关系

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 ``` | ``` private void initSerializers() {         this.put((Type)Boolean.class, (ObjectSerializer)BooleanCodec.instance);         this.put((Type)Character.class, (ObjectSerializer)CharacterCodec.instance);         this.put((Type)Byte.class, (ObjectSerializer)IntegerCodec.instance);         this.put((Type)Short.class, (ObjectSerializer)IntegerCodec.instance);         this.put((Type)Integer.class, (ObjectSerializer)IntegerCodec.instance);         this.put((Type)Long.class, (ObjectSerializer)LongCodec.instance);         this.put((Type)Float.class, (ObjectSerializer)FloatCodec.instance);         this.put((Type)Double.class, (ObjectSerializer)DoubleSerializer.instance);         this.put((Type)BigDecimal.class, (ObjectSerializer)BigDecimalCodec.instance);         this.put((Type)BigInteger.class, (ObjectSerializer)BigIntegerCodec.instance);         this.put((Type)String.class, (ObjectSerializer)StringCodec.instance);         this.put((Type)byte[].class, (ObjectSerializer)PrimitiveArraySerializer.instance);         this.put((Type)short[].class, (ObjectSerializer)PrimitiveArraySerializer.instance);         this.put((Type)int[].class, (ObjectSerializer)PrimitiveArraySerializer.instance);         this.put((Type)long[].class, (ObjectSerializer)PrimitiveArraySerializer.instance);         this.put((Type)float[].class, (ObjectSerializer)PrimitiveArraySerializer.instance);         this.put((Type)double[].class, (ObjectSerializer)PrimitiveArraySerializer.instance);         this.put((Type)boolean[].class, (ObjectSerializer)PrimitiveArraySerializer.instance);         this.put((Type)char[].class, (ObjectSerializer)PrimitiveArraySerializer.instance);         this.put((Type)Object[].class, (ObjectSerializer)ObjectArrayCodec.instance);         this.put((Type)Class.class, (ObjectSerializer)MiscCodec.instance);         this.put((Type)SimpleDateFormat.class, (ObjectSerializer)MiscCodec.instance);         this.put((Type)Currency.class, (ObjectSerializer)(new MiscCodec()));         this.put((Type)TimeZone.class, (ObjectSerializer)MiscCodec.instance);         this.put((Type)InetAddress.class, (ObjectSerializer)MiscCodec.instance);         this.put((Type)Inet4Address.class, (ObjectSerializer)MiscCodec.instance);         this.put((Type)Inet6Address.class, (ObjectSerializer)MiscCodec.instance);         this.put((Type)InetSocketAddress.class, (ObjectSerializer)MiscCodec.instance);         this.put((Type)File.class, (ObjectSerializer)MiscCodec.instance);         this.put((Type)Appendable.class, (ObjectSerializer)AppendableSerializer.instance);         this.put((Type)StringBuffer.class, (ObjectSerializer)AppendableSerializer.instance);         this.put((Type)StringBuilder.class, (ObjectSerializer)AppendableSerializer.instance);         this.put((Type)Charset.class, (ObjectSerializer)ToStringSerializer.instance);         this.put((Type)Pattern.class, (ObjectSerializer)ToStringSerializer.instance);         this.put((Type)Locale.class, (ObjectSerializer)ToStringSerializer.instance);         this.put((Type)URI.class, (ObjectSerializer)ToStringSerializer.instance);         this.put((Type)URL.class, (ObjectSerializer)ToStringSerializer.instance);         this.put((Type)UUID.class, (ObjectSerializer)ToStringSerializer.instance);         this.put((Type)AtomicBoolean.class, (ObjectSerializer)AtomicCodec.instance);         this.put((Type)AtomicInteger.class, (ObjectSerializer)AtomicCodec.instance);         this.put((Type)AtomicLong.class, (ObjectSerializer)AtomicCodec.instance);         this.put((Type)AtomicReference.class, (ObjectSerializer)ReferenceCodec.instance);         this.put((Type)AtomicIntegerArray.class, (ObjectSerializer)AtomicCodec.instance);         this.put((Type)AtomicLongArray.class, (ObjectSerializer)AtomicCodec.instance);         this.put((Type)WeakReference.class, (ObjectSerializer)ReferenceCodec.instance);         this.put((Type)SoftReference.class, (ObjectSerializer)ReferenceCodec.instance);         this.put((Type)LinkedList.class, (ObjectSerializer)CollectionCodec.instance);     } ``` |

这里面基本上没有我们需要的东西，唯一熟悉的就是MiscCodec(提示下我们fastjson加载任意class时就是通过调用这个的TypeUtils.loadClass)，但可惜的是他的write方法同样没有什么可利用的点，再往下去除一些不关键的调用栈，接下来默认会通过createJavaBeanSerializer来创建一个ObjectSerializer对象

![image-20230320135558815](/2023/03/20/year/2023/3/FastJson%E4%B8%8E%E5%8E%9F%E7%94%9F%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96/image-20230320135558815.png)

它会提取类当中的`BeanInfo`（包括有getter方法的属性）并传入`createJavaBeanSerializer`继续处理

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` public final ObjectSerializer createJavaBeanSerializer(Class<?> clazz) {     SerializeBeanInfo beanInfo = TypeUtils.buildBeanInfo(clazz, (Map)null, this.propertyNamingStrategy, this.fieldBased);     return (ObjectSerializer)(beanInfo.fields.length == 0 && Iterable.class.isAssignableFrom(clazz) ? MiscCodec.instance : this.createJavaBeanSerializer(beanInfo)); } ``` |

这个方法也最终会将二次处理的beaninfo继续委托给createASMSerializer做处理，而这个方法其实就是通过ASM动态创建一个类(因为和Java自带的ASM框架长的很“相似”所以阅读这部分代码并不复杂)

![image-20230320140024393](/2023/03/20/year/2023/3/FastJson%E4%B8%8E%E5%8E%9F%E7%94%9F%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96/image-20230320140024393.png)

getter方法的生成在`com.alibaba.fastjson.serializer.ASMSerializerFactory#generateWriteMethod`当中

它会根据字段的类型调用不同的方法处理，这里我们随便看一个(以第一个\_long为例)

![image-20230320141614997](/2023/03/20/year/2023/3/FastJson%E4%B8%8E%E5%8E%9F%E7%94%9F%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96/image-20230320141614997.png)

通过`_get`方法生成读取filed的方法

![image-20230320141732427](/2023/03/20/year/2023/3/FastJson%E4%B8%8E%E5%8E%9F%E7%94%9F%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96/image...