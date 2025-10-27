---
title: Java方法设计原则与实践：从Effective Java到团队案例
url: https://www.freebuf.com/consult/414276.html
source: FreeBuf网络安全行业门户
date: 2024-11-02
fetch_date: 2025-10-06T19:17:00.086525
---

# Java方法设计原则与实践：从Effective Java到团队案例

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

Java方法设计原则与实践：从Effective Java到团队案例

* ![]()
* 关注

* [咨询](https://www.freebuf.com/consult)

Java方法设计原则与实践：从Effective Java到团队案例

2024-11-01 15:31:22

所属地 北京

作者：京东物流 京东物流

# 背景

本文通过阅读《Effective Java》、《Clean Code》、《京东JAVA代码规范》等代码质量书籍，结合团队日常代码实践案例进行整理，抛砖引玉、分享一些在编写高质量代码方面的见解和经验。这些书籍提供了丰富的理论知识，而团队的实际案例则展示了这些原则在实际开发中的应用。希望通过这篇文章，能够帮助大家更好地理解和运用这些编程最佳实践，提高代码质量和开发效率。

# 什么是一个好的方法

在 Java 中，方法是类的一部分，定义了类的行为。方法通常包含方法头和方法体。方法头包括访问修饰符、返回类型、方法名和参数列表，而方法体包含实现方法功能的代码。

> 方法的基本结构 [访问修饰符] [返回类型] [方法名](https://juejin.cn/editor/drafts/%5B%E5%8F%82%E6%95%B0%E5%88%97%E8%A1%A8%5D){ // 方法体 // 实现方法功能的代码 }

**如果一个方法在满足业务需求本身的基础上，职责单一，清晰明了，重点是团队其他成员可以简单看懂及维护，这就是一个好的方法。**如果只有自己看得懂，其他人看不太懂，则不是一个好的方法。具体原则细节从以下【入参】【方法体】【出参】维度详细描述

# 一、入参

## 1）入参不要太多

理想情况下，方法的参数应尽量少。最佳情况是没有参数，其次是一个参数，再次是两个或三个参数，尽量避免超过四个参数。参数越多，方法通常越复杂。从测试的角度来看，编写各种参数组合的单元测试场景也会变得复杂。

设定四个或更少的参数，因为大多数程序员记不住更长的参数列表。**同类型的参数尤其有害，如果不小心弄反了参数的顺序，程序可以正常编译和运行，但结果可能不正确，这极易导致错误。**

如果方法确实需要多个参数，这通常意味着这些参数应该封装为一个类，通过创建参数对象来减少参数的数量。

> **❌**错误案例：重量/体积 同类型参数顺序错误导致问题

```
// 错误的方法定义，参数过多且容易混淆public void calculateShippingCost(double weight, double volume, double length,double width, double height, String destination) {// 假设这里有计算运费的逻辑}// 这里将重量和体积的顺序弄反了service.calculateShippingCost(30.0, 50.0, 10.0, 5.0, 3.0, "New York");// 实际上应该是：service.calculateShippingCost(50.0, 30.0, 10.0, 5.0, 3.0, "New York");
```

> ✅正确案例：在这个示例中，由于重量和体积的顺序弄反，计算出来的运费会有误。为了避免这种错误，可以将这些参数封装成一个类：

```
public class ShippingDetails {private double weight;private double volume;private double length;private double width;private double height;private String destination;// 构造方法、getter和setter省略}// 使用参数对象来简化方法签名public void calculateShippingCost(ShippingDetails details) {// 假设这里有计算运费的逻辑}
```

通过将参数封装成一个类，可以有效减少方法的参数数量，避免参数顺序错误的问题，提高代码的可读性和可维护性。

## 2）谨慎使用可变参数

可变参数数量，它接受0个或者N个指定类型的参数。可变参数的原理是根据调用位置传入的参数数量，先创建一个数组，然后将参数放入这个数组中，最后将数值传递给该方法。

**注意：在对性能要求很高的情况下，使用可变参数要特别小心，每次调用可变参数方法都会导致一次数组的分配和初始化。**

> **❌错误**案例：循环中调用可变参数方法

```
public class Logger {// 可变参数方法public void log(String level, String... messages) {StringBuilder sb = new StringBuilder();sb.append(level).append(": ");for (String message : messages) {sb.append(message).append(" ");}System.out.println(sb.toString());}}// 模拟高频调用for (int i = 0; i < 1000000; i++) {logger.log("INFO", "Message", "number", String.valueOf(i));}
```

在这个案例中，`log`方法每次调用都会创建一个新的数组来保存可变参数`messages`。在高频调用的场景下，这种数组分配和初始化的开销会显著影响性能。

> ✅优化案例：避免可变参数带来的性能开销 我们使用了`List`来传递日志消息。虽然在每次调用时仍然会创建一个`List`对象，但相比于每次创建一个数组，这种方式的性能开销更小，特别是在高频调用的场景下。

```
public class Logger {// 使用List代替可变参数public void log(String level, List<String> messages) {StringBuilder sb = new StringBuilder();sb.append(level).append(": ");for (String message : messages) {sb.append(message).append(" ");}System.out.println(sb.toString());}}// 模拟高频调用for (int i = 0; i < 1000000; i++) {logger.log("INFO", List.of("Message", "number", String.valueOf(i)));}
```

> ✅进一步优化：使用StringBuilder直接拼接 在这种情况下，我们完全避免了数组或集合的创建，直接通过`StringBuilder`拼接字符串，从而最大限度地减少了性能开销。

```
public class Logger {// 使用StringBuilder直接拼接public void log(String level, String message1, String message2, String message3) {StringBuilder sb = new StringBuilder();sb.append(level).append(": ").append(message1).append(" ").append(message2).append(" ").append(message3).append(" ");System.out.println(sb.toString());}}// 模拟高频调用for (int i = 0; i < 1000000; i++) {logger.log("INFO", "Message", "number", String.valueOf(i));}
```

如果无法承受上面的性能开销，但又需要可变参数的便利性，可以有一种兼容的做法，假设方法95%的调用参数不超过3个，那么我们可以声明该方法的5个重载版本，分别包含（0，1，2，3）个参数和一个（3，可变参数），这样只有最后一个方法才需要付出创建数组的开销，而这只占用5%的调用。

> ✅案例：org.slf4j.Logger 每个日志级别都有多个重载的方法，支持不同数量的参数,通过这些方法，SLF4J 提供了灵活且高效的日志记录接口，可以适应各种不同的日志记录需求。

```
package org.slf4j;public interface Logger {public boolean isInfoEnabled();public void info(String msg);public void info(String format, Object arg);public void info(String format, Object arg1, Object arg2);public void info(String format, Object... arguments);public void info(String msg, Throwable t);}
```

## 3）校验参数的有效性

大部分方法都会对入参的值有一定限制，比如String字符串长度，类型转换，对象不能为null，订单运单唯一性，批量接口List个数限制等。首先我们应该在**API中详细描述入参的各种限制条件，并且在方法体的入口进行校验检查，以强制实施这些限制。**

对参数的检查，原则是尽早检查，否则整个链路被检测的可能性降低，并且一旦检测到，定位起源头比较复杂。反过来思考，如果不在开头进行检查，则可能发生如下情况：方法在接下来链路处理过程中抛出错误的结果，但方法可能是正常返回，比如接口返回正常，但数据库保持的时候，由于字段越界导致保存数据库异常。

参数校验 应该反应到 技术指标还是业务指标？

> 技术指标：个人理解入参非法不应该体现到UMP技术可用率指标，因为这是API正常的一种体现，如果入参非法不合理，返回上游对应的错误码CODE，本身的技术可用率正常。 业务指标：但方法对应的业务指标可以反映入参非法的情况。例如，可以记录非法入参的次数，以便分析和改进整个链路的业务逻辑。

> ✅案例：链路校验一致 比如某个入参，从上游到整个链路下游，包括方法内部链路，最终到数据库存储，校验规则是一致的。在下面这个例子中，`userName`的长度限制在方法入口和数据库存储过程中保持一致，确保链路校验一致。

```
public class UserService {// 用户信息保存方法public void saveUser(String userName) {// 参数校验if (userName == null || userName.length() > 20) {throw new IllegalArgumentException("User name cannot be null and must be less than 20 characters");}// 假设数据库字段长度限制为 20saveToDatabase(userName);}private void saveToDatabase(String userName) {// 数据库保存逻辑// ...}}
```

> **❌错误**案例：链路校验规则不一致 零售C端/B端用户可以填写20个字符串，整个链路校验也是20，但底层数据库是varchar(10)

```
// 假设数据库字段长度限制为 10private void saveToDatabase(String userName) {// 数据库保存逻辑// ...}
```

探讨：链路重复校验

> 比如物流链路运单合法性校验，N个系统都进行校验是否有必要？是否应该只在入口处校验，其他链路保持信任机制？

# 二、方法体

## 1）方法要短小

方法的第一规则是短小，正如行业很多代码规约，比如阿里规约方法总行数不超过80行，京东代码规范中方法体的行数不能多于70行，否则降低编码效率，不方便阅读和理解。

其实个人理解不用太关注多少行，核心是方法的职责要单一，分清楚方法主干和分支，，看方法里的代码是否还可以再抽取一个方法，分清代码个性和共性，把共性的代码抽取方法，用于复用，让方法主干更清晰。

## 2）无副作用

> 在Java 编程语言中，术语“副作用”(side effects) 指的是一个函数或表达式在计算结果以外对程序状态（如修改全局变量、改变输入参数的值、进行I/O 操作等）产生的影响。

> **❌**副作用案例： 如下`filterBusinessType`方法的主要作用是返回一个`业务类型int`类型的值，但它也修改了传入的`response`对象的A值作为一个副作用。在外面链路使用了A属性值做逻辑判断 副作用问题：在`filterBusinessType方法中`如果是在response之前return了数据，从方法角度看不出问题，但整个链路会出现问题。

```
public int filterBusinessType( Request request,Response response) {if(...){return ... }boolean flag = isXXX(request, response); }
```

正如上面说的方法职责单一，只做一件事，但副作用就是一个谎言，方法还会做其他隐藏起来的事情，我们需要理解副作用的存在，并采取合适的策略来管理和控制它们。

**如何规避这种现象**

为了避免这种情况，可以采用以下几种策略：

1.**分离关注点**: 可以将获取业务类型和响应设置分离成两个不同的方法。这样，调用者就可以清晰地看到每个方法的职责。

```
public int filterBusinessType(String logPrefix,Request request){// 过滤逻辑...int businessType=...;return businessType;}public void setResponseData(int filterResult,Response response){// 根据过滤结果设置响应数据...response.setFilteredData(...);}
```

1.**返回复合对象（上下文context）**: 如果业务类型结果和响应数据是紧密相关的，可以考虑创建一个包含这两个信息的复合对象，并将其作为方法的返回值。

```
public FilterResultAndResponse filterBusinessType(String logPrefix,Request request){// 过滤逻辑...int result=...;Response response=new Response();response.setFilteredData(...);return new FilterResultAndResponse(result, response);}class FilterResultAndResponse{private int filterResult;private Response response;public FilterResultAndResponse(int filterResult,Response response){this.filterResult = filterResult;this.response = response;}// Getters and setters for filterResult and response}
```

## 3）控制语句（if/else/while/for等）

不要在条件判断中执行复杂的语句，将复杂逻辑判断的结果赋值给一个有意义的布尔变量，以提高可读性。团队中也存在很多if语句内的逻辑相当复杂，阅读者需要分析条件表达式的最终结果，才能明确什么样的条件执行什么样的语句。复杂逻辑表达式，与、或、取反混合运算，甚至各种方法纵深调用，理解成本非常高。如果赋值一个非常好理解的布尔变量名字，则是件令人爽心悦目的事情

> **❌**错误案例：if/else if语句中条件逻辑复杂，并且还存在！取反混合运算，导致这段代码理解成本比较高

```
boolean flagA = isKaWhiteFlag(logPrefix, request);boolean flagB = PlatformTypeEnum.JD_STATION.getValue() == request.getPlatformType();boolean flagC = KaPromiseUccSwitch.isPopJDDeliverySwitch(request.getDict(),request.ge...