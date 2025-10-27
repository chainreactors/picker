---
title: gson参数走私浅析
url: https://forum.butian.net/share/3801
source: 奇安信攻防社区
date: 2024-10-12
fetch_date: 2025-10-06T18:49:15.115025
---

# gson参数走私浅析

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### gson参数走私浅析

* [渗透测试](https://forum.butian.net/topic/47)

Gson 是一个由 Google 开发的 Java 库，用于将 Java 对象序列化为 JSON 格式，以及将 JSON 字符串反序列化为 Java 对象。Gson 以其简单易用和高性能而闻名，它提供了一种非常直观的方式来处理 JSON 数据。浅析其中潜在的参数走私场景。

0x00 前言
=======
Gson 是一个由 Google 开发的 Java 库，用于将 Java 对象序列化为 JSON 格式，以及将 JSON 字符串反序列化为 Java 对象。Gson 以其简单易用和高性能而闻名，它提供了一种非常直观的方式来处理 JSON 数据。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-f675a7014d183f539603dceb53e4b004758dce77.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-3de6012b194a86c9cc2da595ee53f5af78d4474c.png)
0x01 解析过程
=========
以gson的fromJson(String,class)方法解析自定义User，以2.8.9版本为例，查看具体的解析过程：
```Java
Gson gson=new Gson();
User user= gson.fromJson(body, User.class);
```
沿着fromJson方法调用的路径，最终会调用到fromJson(JsonReader reader, Type typeOfT)：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-adc5110fa9547ab755817989e7db8dbd4419f0f7.png)
在peek()方法中，实际会调用doPeek进行处理，这里会对解析过程中的有效元素进行一些记录：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-20e05a376a6c51431a61c5d13fd1fe89cb40b627.png)
在doPeek方法中，会调用nextNonWhitespace，它的作用是跳过 JSON 流中的所有空白字符（如空格、制表符、换行符等），通过查阅源码可以知道，Gson中键值以及分隔符之间允许存在的无意义字符，包括`\n`、`空格`、`\t`、`\r`：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-e0ee7c542efca208abaacdaf6fe79f7d3953b3b1.png)
这里还会对注释符进行处理，可以看到gson支持`/\*\*/（多行）`、`//（单行）`、`#（单行）`这三类注释符：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-fe30c6befd125e820c0dd137a04628cab628958d.png)
处理完后会尝试获取合适的自定义的Adapter方法或者Gson自带的Adapter，然后调用对应的read方法进行JSON的解析：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-c6b7cd284a8d594620cfae0b93bf4bc961991794.png)
TypeAdapter 是Gson提供的一个抽象类，用于接管特定某种类型的序列化和反序列化过程，包含两个主要方法 write(JsonWriter,T) 和 read(JsonReader) 其它的方法都是final方法并最终调用这两个抽象方法。大部分基本类型的TypeAdapter都有一个TypeAdapterFactory：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-1bda8a35fdec2e4fe557da25676e9ae71fb0aa01.png)
例如MapTypeAdapterFactory主要用于解析map类型的数据：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-bd972d1644c066fe08ada36df1051b1cb57b2d41.png)
对于类似自定义User的解析，一般情况下会在ReflectiveTypeAdapterFactory进行处理，查看其read方法的实现，首先如果 JSON 值不为 NULL，方法使用 this.constructor.construct() 创建新、实例。这里的 constructor 是一个负责创建对象实例的函数：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-761e1d865dbabfbb206c23ccab7b9a91badc6536.png)
调用 in.beginObject() 标记 JSON 对象的开始。然后使用 while 循环遍历 JSON 对象中的所有字段。对于每个字段，使用 in.nextName() 获取字段名，并尝试从 boundFields 集合中获取对应的 ReflectiveTypeAdapterFactory.BoundField 对象：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-ab30a3bfc8d61bd9abd97d4f6486ef3b8cce4d6b.png)
如果找到了对应的 BoundField 并且该字段被标记为 deserialized，则调用 `field.read(in, instance)` 来从 JSON 读取值并将其设置到 Java 对象的相应字段中。否则调用 `in.skipValue()` 跳过该字段：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-43f7efe208846cd30bcf70e02cd60c5262dc8d7a.png)
最后调用 in.endObject() 标记 JSON 对象的结束。并返回反序列化后的 Java 对象实例：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-f47ca500331e79ceff2595770e94da8ed1211b06.png)
查看具体字段的解析实现，首先是nextName，从调用的方法可以知道，gson默认情况下支持`'`、`"`、无引号三种解析方式：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-a4b4dbe82ae817c96c02bd92f3a3bf19ce6b2db9.png)
以双引号为例，查看具体的解析逻辑，主要是通过 do-while 循环读取字符进行处理，直到遇到引用值的结束引号：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-3897f76a750b384307a71badd5f04097f67b2770.png)
当遇到转义字符后，会调用readEscapeCharacter方法进行处理：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-46a711785882760edca44a68ea3ef35d4d80f201.png)
例如会对`u`开头的进行具体的unicode解码操作：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-a20158aaa3c137343421df20189bd19547e818c6.png)
以上是对key的处理，对值的处理主要会通过nextString进行解析：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-5c2cd5b005188038227e5535824d3235e3d8d460.png)
在nextString中同样会根据`'`、`"`、无引号解析方式调用nextUnquotedValue进行处理，此外，还有类似Long.toString的处理：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-52c80ae4e6dd8e84976ca40ddae4f03bf76d456d.png)
以上是gson的大致解析流程。
0x02 参数走私场景
===========
当使用ReflectiveTypeAdapterFactory处理时，如果在set操作时使用了已存在的键,则新值会替换旧值,原有的键值对会被新的键值对覆盖。\*\*默认情况下在反序列化时，会取重复键值的后者\*\*。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-a8d815a8f14ed56bb68311c7c07d0eec1759c3d5.png)
除此之外，前面还提到，Gson可以通过MapTypeAdapterFactory对map类型的数据进行解析，看一个实际的例子：
```Java
Map map = gson.fromJson(body,HashMap.class);
map.forEach((k, v) -> {
//......
});
```
在实际解析的时候可以看到，gson在解析Map类型时对重复键值的情况做了校验，一定程度上规避了重复键值带来的参数走私风险：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-45a0b693bdb6a0424baf69f3663778571d094f2c.png)
可以看到当解析如下带有重复键值的JSON数据时，会抛出`com.google.gson.JsonSyntaxException`异常：
```Java
String body ="{\"activityId\":\"123\",\"activityId\":\"321\"}";
```
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-5adedcce7a5be91fbbb6677de6b85740426fe38d.png)
基于gson解析过程中的一些特点，在特定情况下可能会由于解析器的差异导致参数走私的风险，下面是一个实际的例子：
\*\*在fastjson的解析过程中，默认会去除键值外的空白符\*\*，主要是在com.alibaba.fastjson.parser.JSONLexerBase#skipWhitespace方法进行处理的，涉及`\b`、`\n`、`\r`、`\f`、`\t`还有空格：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-7222c2b072aa6991ef3d5250b881b491ed2657a1.png)
而gson在解析时，在键值以及分隔符之间同样允许存在的无意义字符，包括`\n`、`空格`、`\t`、`\r`，主要是通过com.google.gson.stream.JsonReader#nextNonWhitespace方法处理的：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-935f4ae9840d6dc38d9d2fe1af493102260f09e3.png)
跟fastjson相比，gson并没有处理键值以及分隔符之间无意义的`\b`、`\f`。
这里有一个关键的点，根据前面的分析，\*\*gson在解析时允许key/value首字母都允许不带引号\*\*。
那么也就是说如果特殊字符出现在value的第一个字符时gson仍可以正常解析，例如下面的例子，额外的字符$会作为键的一部分进行解析：
```Java
String body ="{$$\"activityId\":\"123\"}";
Gson gson=new Gson();
Map map = gson.fromJson(body,HashMap.class);
map.forEach((k, v) -> {
System.out.println(k+":"+v);
});
```
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-20513ff703fcdb60ef0e0defcff264f5461984c8.png)
由于gson在解释时并没有处理键值以及分隔符之间无意义的`\b`、`\f`。而fastjson在解析键值时会忽略对应的内容。利用这一点，在重复键值的场景下可以达到参数走私的效果。下面是实际的例子：
```Java
String body ="{\"activityId\":\"123\",\"activityId\":\"321\"}";
//gson
Gson gson=new Gson();
User userByGson= gson.fromJson(body, User.class);
System.out.println("gson parse result:"+userByGson.getActivityId());
//fastjson
User userByFastjson= com.alibaba.fastjson.JSONObject.parseObject(body, User.class);
System.out.println("fastjson parse result:"+userByFastjson.getActivityId());
```
可以看到默认情况下，fastjson跟gson都会取重复键值的后者：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-27c195dfb8d67767e56a5b79eaa5e525105aa430.png)
当修改解析的json body：
```Java
String body ="{\"activityId\":\"123\",\b\"activityId\":\"321\"}";
```
此时两者解析存在差异，gson会因为无法忽略额外的`\b`结合\*\*解析时允许key/value首字母都允许不带引号\*\*的特点将`\b"activityId"`额外认为是一个独立的键：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-b5f7e772021aed017406b77291e4f07f7199af85.png)
通过MapTypeAdapterFactory解析也印证了相关的猜想，gson确实因为将`\b"activityId"`额外认为是一个独立的键，而取到了前者，而fastjson因为忽略了无关的`\b`仍正常解析获取到了后者，利用这一点差异完成了参数走私：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/...