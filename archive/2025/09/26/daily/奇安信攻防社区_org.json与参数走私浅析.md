---
title: org.json与参数走私浅析
url: https://forum.butian.net/share/4571
source: 奇安信攻防社区
date: 2025-09-26
fetch_date: 2025-10-02T20:41:10.411319
---

# org.json与参数走私浅析

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

### org.json与参数走私浅析

* [渗透测试](https://forum.butian.net/topic/47)

在Java Web生态中，org.json是一个轻量级的json构造和解析工具包，其提供了简洁的API进行相关JSON的反序列化操作。浅谈其解析过程与参数走私案例。

0x00 前言
=======
在Java Web生态中，org.json是一个轻量级的json构造和解析工具包，其还包含JSON与XML, HTTP headers, Cookies等各种转换。
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-359779a743299fab146e2b8d07fab29c7ad33fa2.png)
其提供了简洁的API进行相关JSON的反序列化操作。例如可以通过new JSONObject(String json)的方式解析 JSON 字符，通过对应的方法来获取对应的属性值：
```php
JSONObject jsonobj = new JSONObject("{'name':'test','age':20}");
String name = jsonobj.getString("name");
```
下面简单看看具体的解析过程：
0x01 org.json解析过程
=================
以org.json.JSONObject为例，查看具体的解析过程，本质上调用的是对应的构造方法进行进行处理：
首先通过nextClean方法获取下一个有效字符，首先会检查解析的JSON 字符串是否以左花括号 { 开头。如果不符合，会抛出 JSONException 异常，提示 JSON 格式错误。：
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-899da045c40c22bc989c07c19a64c1b247b382a7.png)
nextClean方法具体实现如下，作用是从输入流中跳过所有的空白字符（如空格、制表符、换行符等）：
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-b6bfff63e0fb2935ff73031eaa0888bb112164cb.png)
然后进入while循环中，这里会从头到尾对json的逐个字符进行读取，根据不同的内容进行相应的处理，接下来逐个情况进行解析：
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-bfbe4b3afc44dbc95aec33d47022b3dced8c32e7.png)
- case '\\u0000':：如果读到了 null 字符，抛出异常。
- case '}':：如果遇到了右花括号，结束解析并返回。
- default:这里主要是对json字符串中的键值对进行处理，也是核心解析逻辑。
在对应键值对解析逻辑中，首先会通过nextSimpleValue方法解析出 JSON 对象中的键。然后获取下一个字符，并检查是否是`:`,如果不是则抛出异常。
中途会对key进行对应的检查，如果包含重复key的话，会抛出syntaxError异常，然后解析出对应属性的值，病存储到当前的JSONObject中：
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-f3cddd976df29a6d8ee66d7384432cf6b9fa6b9e.png)
获取属性值主要在nextValue中实现，处理了嵌套json以及Array的情况，其余均通过nextSimpleValue方法处理：
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-c1933046cb609912878ad8ca6513125dcbcd439e.png)
最后检查后续字符是 , 或 ;（分隔符）还是 }，重复上述流程直到解析结束：
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-af0eb68875ce1e1a8422725438455ddb054dff4b.png)
从前面的分析可知，对应属性key&amp;value的解析是通过nextSimpleValue方法处理的，主要分两种情况：
- 如果对应的字符为单/双引号，则调用nextString方法获取对应的值
- 若非单/双引号开头，则构造StringBuilder，循环读取后续字符，直到遇到JSON结构分隔符或控制字符，然后回退一个字符，清理字符串并转换为对应的JSON值并返回。
![](https://cdn.nlark.com/yuque/0/2025/png/2494546/1757152765758-765a0ba6-5473-48b5-8824-ee5231e18d94.png)
在nextString方法中，主要是从输入流中读取字符，并处理转义字符（如 \\n、\\t 等）和普通字符，覆盖了常见的转义字符场景，直到遇到与开头引号匹配的结束引号，同时对应空白符等内容会抛出相关的解析异常：
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-1e84e9e15e2d586723d587b43a0f0af3bcc2517d.png)
同时支持对unicode字符进行处理：
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-d0b82f31721f1c7bb5a4aa2a01a5189cf3fa6549.png)
对于非单/双引号开头的情况，最终org.json会调用stringToValue对获取到的内容进行规整。例如检查字符串是否为空，是否为布尔值"true"或"false"，是否为"null"，或者是否是一个数字。根据检查结果，它会返回对应的布尔值、特殊值NULL、数字或者原字符串：
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-88f1fc341f9582cb4254b103c519c40e2d08b0ff.png)
以上是org.json的具体解析过程。可以看到整体解析比较宽松，例如允许属性不使用双引号包裹，使用单引号等。但是本身不支持重复键的处理，一定程度上解决了重复键差异解析。
0x02 参数走私场景
===========
看一个实际的案例：
Web application的User实体中包含一个roleId的属性（类型为String），用于表示当前用户的角色类型。
```php
public class User {
private String roleId;
......
public String getRoleId() {
return roleId;
}
public void setRoleId(String roleId) {
this.roleId = roleId;
}
......
}
```
在认证拦截器中，对请求的JSONBody中的roleId字段进行了拦截，当roleId为1时，会进行相应的鉴权处理（通过org.json获取对应的内容进行处理）：
```php
JSONObject jsonObj = new JSONObject(body);
if(jsonObj.getString("roleId").equals("1")){
//具体鉴权逻辑，限制roleId的更新操作
}
```
若后端接口在参数解析时使用的是Fastjson进行处理，这里明显存在JSON解析器的差异，那么如何绕过当前的防护逻辑呢？
结合前面对org.json的过程解析，可以Json隐式数据类型转换来达到对应的目的。下面是具体的思路：
在Fastjson的的核心逻辑JSONScanner 部分，有对类似'-'或者'+'开头的内容进行处理，会把以正号（+）、负号（-）或者数字开头的字符串识别为数值来进行解析：
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-dcbbed860028eddc21afb1bc0e63299bd9ba154a.png)
例如下面的例子,最后输出的value结果会是1：
```php
String json = "{\"value\":+1}";
JSONObject jsonObject = JSON.parseObject(json);
System.out.println(jsonObject.get("value")); // 输出结果是 "1"
```
对于org.json，结合前面的分析，若解析的内容没有被单双引号包裹，会调用stringToValue对获取到的内容进行规整，对于数字型输入，只有0-9以及-的情况才会进行额外处理，那么也就是说对于+1的情况，org.json会进行原样输出：
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-c1be4f140eaa614af6acb468df44f4bb115d4fbc.png)
那么也就是说可以利用+号，来达到参数走私绕过的效果。证明对应的猜想：
```php
String body = "{\"roleId\":+1}";
JSONObject jsonobj = new JSONObject(body);
System.out.println("org.json parse result:"+jsonobj.getString("roleId"));
User userByFastjson= com.alibaba.fastjson.JSONObject.parseObject(body, User.class);
System.out.println("fastjson parse result:"+userByFastjson.getRoleId());
```
从结果可以看到，成功绕过了对应的检测逻辑：
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-99fe8f498c970836704d200b4b7cf778ed93f579.png)
除了以上案例外，当json的key中出现unicode空字符时，`json-c`对空字符会做截断，但`org.json-json`库会保留。借助这点差异，可以通过在对应属性增加unicode空字符，结合重复key的手法同样可以达到绕过的效果。
并且，org.json跟gson一样，在正常情况下`;`会识别成键值以外的分隔符，而部分json解析组件则会因为错误解析进入兜底逻辑，在特定场景下也可能由于解析差异导致参数走私的风险。在后续审计工作中可以额外关注。

* 发表于 2025-09-25 09:00:01
* 阅读 ( 647 )
* 分类：[代码审计](https://forum.butian.net/community/code%20audit)

0 推荐
 收藏

## 0 条评论

请先 [登录](https://forum.butian.net/login) 后评论

[![tkswifty](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/bbd1e36f58e6f1fbc8288cd604117e9dd4f286d.jpeg)](https://forum.butian.net/people/8019)

[tkswifty](https://forum.butian.net/people/8019)

66 篇文章

[奇安信攻防社区](https://forum.butian.net)|
联系我们

|
[sitemap](https://forum.butian.net/sitemap)

Copyright © 2013-2023 BUTIAN.NET 版权所有 [京ICP备18014330号-2](https://beian.miit.gov.cn/#/Integrated/index)

×

#### 发送私信

请先 [登录](https://forum.butian.net/login) 后发送私信

×

#### 举报此文章

垃圾广告信息：
广告、推广、测试等内容

违规内容：
色情、暴力、血腥、敏感信息等内容

不友善内容：
人身攻击、挑衅辱骂、恶意行为

其他原因：
请补充说明

举报原因:

取消
举报

×

#### ![tkswifty](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/bbd1e36f58e6f1fbc8288cd604117e9dd4f286d.jpeg)

如果觉得我的文章对您有用，请随意打赏。你的支持将鼓励我继续创作！

![]()

---