---
title: 浅谈Java Spring Web中“隐蔽”的入口点——Spring参数转换器
url: https://forum.butian.net/share/3787
source: 奇安信攻防社区
date: 2024-09-30
fetch_date: 2025-10-06T18:20:09.015101
---

# 浅谈Java Spring Web中“隐蔽”的入口点——Spring参数转换器

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

### 浅谈Java Spring Web中“隐蔽”的入口点——Spring参数转换器

* [渗透测试](https://forum.butian.net/topic/47)

在 Spring Web 应用程序中，参数转换器（Converter 和 Formatter）在处理传入的数据时起着至关重要的作用。尤其是在对处理用户输入进行数据转换时。在日常代码审计中，这些转换器往往会被忽略，可能存在一些潜在的安全风险。

0x00 前言
=======
在 Spring Web 中，Controller 负责接收和响应 HTTP 请求。任何从用户或客户端传入的数据都会首先经过 Controller，是输入验证和处理的关键点。因此在日常的代码审计中，一般会重点关注Controller这类的入口点。
除此之外，当用户通过 HTTP 请求发送数据时，Spring MVC 还可以使用 `Converter` 和 `Formatter` 这类转换器将请求参数（通常是字符串）转换为控制器方法期望的类型，以满足特定的业务场景，这里也会对用户的输入进行相关的处理。在Spring参数处理过程中也充当了很重要的角色。下面看看具体的内容。
0x01 Spring参数处理过程
=================
在Spring参数处理过程中，如果缓存中不存在适用的解析器，则遍历已配置的解析器列表。对于每个解析器，它会调用supportsParameter方法来判断是否支持给定的参数类型。如果找到了支持的解析器，则将其缓存，并返回该解析器。得到解析器后就可以调用参数解析器的 resolveArgument() 方法解析参数的值：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-5520ec2c73afa2ca8baf30bcc3d61b687b271c53.png)
在 resolveArgument() 方法中，首先调用 getArgumentResolver() 方法获取与方法参数类型相对应的参数解析器。 如果解析器为 null，表示不支持当前参数类型，抛出异常并指明不支持的参数类型，如果解析器存在，则调用解析器的 `resolveArgument()` 方法来解析参数的值：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-746d0cdcb58b2a350bbe12853bb638a240dad9fd.png)
其中有一个参数WebDataBinderFactory，在拿到参数解析器后，在内部属性中可以看到定义了多个converter（默认是124个），在参数赋值的步骤中会被调用，从多个converter里面找到能处理当前的请求参数和Controller参数之间关系的转换器converter，拿到后用它将请求参数解析并完成最终的赋值操作：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-6cd85bb8e0802c15e27968a2dee6f0732263fb2f.png)
其中`Converter` 和 `Formatter` 是两个用于类型转换的接口，它们在数据绑定和格式化方面发挥着重要作用。可以通过实现对应的接口实现自定义转换器。只需要在在WebConfiguration中添加自定义的转换器，重写addFormatter(FormatterRegistry registry)即可。
例如下面的例子，可以看到此时converter总数为125:
```Java
@Override
public void addFormatters(FormatterRegistry registry) {
registry.addConverter(new MySpringConverter());
}
```
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-2832d5c5936d24b5731a82c665efbe4f3bd2201e.png)
1.1 Converter
-------------
Converter 是 Spring 框架中用于类型转换的通用接口，它属于 org.springframework.core.convert 包。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-2af4d414076bf368a585c4973739c978721aeec3.png)
- 其用于在任何两个类型之间进行转换，而不仅仅是字符串和其他类型。例如，你可以使用 Converter 将日期对象转换为字符串，或者将字符串转换为自定义的复杂类型。
- Converter 通常在 Spring 的 ConversionService 中注册，这是一个中央转换服务，用于管理和执行类型转换。
- Converter 接口定义了两个方法：convert 方法用于类型转换，getConvertibleSourceTypes 和 getConvertibleTargetTypes 方法用于指定转换器能够处理的源类型和目标类型。
1.2 Formatter
-------------
Formatter 是 Spring 的 org.springframework.format 包中的一个接口，它专门用于格式化和解析字符串表示形式的对象。
- Formatter 是 Spring 的 org.springframework.format 包中的一个接口，它专门用于格式化和解析字符串表示形式的对象。
- Formatter 通常用于 Web 应用程序，特别是在 Spring MVC 中，用于将字符串请求参数转换为特定的类型，以及将对象转换为字符串以用于响应。
- Formatter 接口继承自 Printer 和 Parser 两个接口，这意味着它必须实现将对象转换为字符串（print 方法）和将字符串解析为对象（parse 方法）的逻辑。
- Formatter 通常在 Spring MVC 的 FormatterRegistry 中注册，这是一个用于管理和注册格式化器的注册表。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-88f08851f5e3b4fc4e81549736c70a93ed039496.png)
1.3 两者区别
--------
Converter 更通用，适用于任何类型的转换。而Formatter只能将String转成成另一种java类型。这类转换器在审计时往往会是一个“盲点”，自定义的 Converter 或 Formatter 这些“隐蔽”的入口点可能包含复杂的逻辑，这些逻辑可能成为攻击者利用的入口点。
0x02 转换器中常见安全风险
===============
跟Controller的参数传递一样，参数转换器只是在实际赋值前多做了一层处理。关注具体的实现逻辑即可。在特定情景下也会有类似SQL注入等安全风险。例如下面的例子,对传入的id进行了对应的SQL查询转换成Book对象的操作，如果存在SQL拼接的话，也会存在SQL注入的风险：
```Java
public class BookFormatter implements Formatter<Book> {
private BookRepository repository;
public BookFormatter(BookRepository repository) {
this.repository = repository;
}
@Override
public Book parse(String bookIdentifier, Locale locale) throws ParseException {
Book book = repository.findBookByIsbn(bookIdentifier);
return book != null ? book : repository.findOne(bookIdentifier);
}
@Override
public String print(Book book, Locale locale) {
return book.getIsbn();
}
}
```
除了常见的漏洞风险以外，当应用程序需要与第三方服务（如社交媒体、支付网关等）集成时，Spring 的 `Converter` 和 `Formatter` 可以发挥重要作用。例如如果第三方服务使用非标准的数据格式或字段命名约定，可以通过实现自定义的 Converter 或 Formatter 来处理这些特殊情况。包括定义如何在第三方服务的 JSON 数据和你的应用程序域对象之间进行转换。
下面看一个实际的例子：
在对应的转换器中，通过json-smart对传入的JSON字符串进行了转换：
```Java
JSONParser parser = new JSONParser();
JSONObject jsonObject = (JSONObject) parser.parse(new StringReader(text));
```
简单看一下json-smart的实现，本质上调用的是net.minidev.json.parser.JSONParser#parse方法进行解析：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-6bfb7477dbffee82a74b4a52eba670b80ccb3b36.png)
首先会在getPString方法做一些初始化的配置：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-52ae75810bd4794edf0d7b148bd7ceb568ff38b6.png)
在解析前会根据DEFAULT\\_PERMISSIVE\\_MODE属性做一些初始化的配置，默认情况下如果没有配置系统变量JSON\\_SMART\\_SIMPLE则该属性值为-1:
```Java
public static int DEFAULT\_PERMISSIVE\_MODE = System.getProperty("JSON\_SMART\_SIMPLE") != null ? 4032 : -1;
```
在JSONParserString类的构造方法中，会逐层调用其父类的构造方法根据permissiveMode（通过DEFAULT\\_PERMISSIVE\\_MODE属性获取）进行处理：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-7f8e6546f6f49ba8daa5a9c2c29bc0777f6a52db.png)
最终实际调用了JSONParserBase的构造方法，在该构造方法中，主要根据传入的 `permissiveMode` 参数来设置解析器的各种解析行为。`permissiveMode` 是一个整数，它的二进制位表示了不同的解析选项：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-99b3c5c553d0c4772694bca09e231bc5b8af2dd6.png)
这些设置项共同定义了解析器的行为，使得它可以在不同的宽松模式下工作，举几个例子：
- acceptSimpleQuote表示允许使用单引号来表示字符串
- ignoreControlChar表示忽略控制字符，如换行符、回车符等
- reject127表示拒绝解析127个ASCII控制字符之外的字符
- ......
处理后默认情况下的解析选项配置如下：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-69d5b39c4a7e9a855fed20bb13f3dc071743683e.png)
完成对应的初始化后，从net.minidev.json.parser.JSONParserBase#parse开始解析，并返回解析后的对象。其中pos用于跟踪解析过程中的字符位置，然后在readFirst 方法解析 JSON 数据。readFirst 方法会根据 JSON 数据的起始字符（例如 { ）来决定解析路径，并返回解析后的结果：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-51edd0092efdd8ab29d5eb41649bea834b5bd82b.png)
获取到解析结果后，如果启用了尾部数据检查（checkTaillingData 为 true，默认为false），则进行一系列检查。例如如果checkTaillingSpace为false，则调用 `skipSpace` 方法跳过尾部的空格。最终返回解析的结果。
在key-value值解析的逻辑，会调用 readString2 方法来处理包含转义字符的字符串这里会通过循环，不断地读取字符，直到字符串结束：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-572fd37098f1c34d326ee99515175627f0ce4d35.png)
主要是以下处理：
- 控制字符（如 ASCII 码 0 到 31 的字符），若设置忽略控制字符（ignoreControlChar 为 false，默认为true），则抛出 ParseException。如果读取到的是转义字符（\\u001a，即 ESC），则抛出 ParseException：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-53af8915ca39c74b4a8a5fa364b2ee8a97eee567.png)
- 如果读取到的字符与起始分隔符相匹配（双引号或单引号），则读取下一个字符，并把已经构建好的字符串（sb.toString()）赋值给 xs，然后返回：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-75170fa57205920c4199d0be8eadc85ace81d169.png)
- 如果读取到的是反斜杠（`\`），则继续读取下一个字符以确定转义序列，例如是 `\u` 则读取 Unicode 转义序列，如果是 `\x` 则读取 Hex 转义序列：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-d020e9e5da949c8dfd6c477b49f3f41e0de217b8.png)
- 如果遇到文件结束符（`\u007f`），会根据ignoreControlChar以及reject127的配置判断是否需要抛出ParseException异常：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-7cd936ab9a840bcac3f4c8ef209e6471f70c4ecb.png)
- 对于其他所有字符，直接追加到字符串构建器 `sb` 中：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-a7a68a1c285d7bc686b5739388222b47e4c96481.png)
也就是说，\*\*若解析的内容中包含转义字符，无论是key还是value里的值，对于类似\\u007f、\\u0000等字符，在parse解析时会忽略掉\*\*。
结合当前的业务场景，解析完成后转发到其他三方平台时可能会存在参数走私的风险。举个实际的例子：
```Java
String test ="{\"\\u0061ctivityId\u0000\":\"321\"}";
JSONParser parser = new JSONParser();
JSONObjec...