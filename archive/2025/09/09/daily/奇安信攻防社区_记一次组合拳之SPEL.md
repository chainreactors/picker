---
title: 记一次组合拳之SPEL
url: https://forum.butian.net/share/4532
source: 奇安信攻防社区
date: 2025-09-09
fetch_date: 2025-10-02T19:49:07.200031
---

# 记一次组合拳之SPEL

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

### 记一次组合拳之SPEL

* [渗透测试](https://forum.butian.net/topic/47)

感觉整个渗透过程特别有意思，从扫描到 heapdump 泄露，到得敏感信息的泄露，再到观察请求包，思考参数表达的意思，为什么是这样的，从而发现隐藏的表达式注入点，到 getshell

\*\*记一次组合拳之SPEL(重在思路分享+payload)\*\*
前言
--
感觉整个渗透过程特别有意思，从扫描到 heapdump 泄露，到得敏感信息的泄露，再到观察请求包，思考参数表达的意思，为什么是这样的，从而发现隐藏的表达式注入点，到 getshell
笔记记录了全部详细的过程，包括思考的过程，思路的转变，看很多文章，就只有渗透的结果，感觉学不到东西，毕竟思考的过程才是能力，如果遇到对应的场景知道如何思考，找到漏洞点就轻轻松松了
真的就是一步一步记录的自己的思路
其中还有自己看源码发现的绕过方法，真的，java 的神奇之处就在于，如果你仔细看源码，会发现更多的巧思路
凭据获取
----
首先一波信息收集来到如下的站点
![](https://gitee.com/nn0nkey/picture/raw/master/img/20250810022624.png "null")
弱密码尝试一波
![](https://gitee.com/nn0nkey/picture/raw/master/img/20250810022650.png "null")
尝试了很多都不行，准备下播了
看了一眼前台的接口
发现前台几乎没有什么有作用的接口
![](https://gitee.com/nn0nkey/picture/raw/master/img/20250810022829.png "null")
也没有什么敏感信息，于是决定目录扫描一波
结果有 heapdump 泄露，这个可是一个好东西
Heap Dump（堆转储）是指在程序运行时，将应用程序的堆内存（Heap）中的所有对象及其状态完整地保存到一个文件中的过程或文件。
而在这个内存中会有很多很多的敏感信息
[https://github.com/wyzxxz/heapdump\\_tool](https://github.com/wyzxxz/heapdump\_tool)
```php
0. (search data, may can't find some data, can't use function num=,len=).
1. (load all object, need wait a few minutes).
> 0
[-] please input keyword value to search, example: password,re=xxx,len=16,num=0-10,id=0x123a,class=org.xx,all=true,geturl,getfile,getip,shirokey,systemproperties,allproperties,hashtable input q/quit to quit.
> password
[-] Start find keyword: password
>> password -> xxxxxxxxxxx
```
这应该就是管理员的密码吧，然后找了个用户的字典
最后管理员账号用户名是 manager
快速寻找可利用接口
---------
最后进入到内部界面的时候接口就太多了
![](https://gitee.com/nn0nkey/picture/raw/master/img/20250810024109.png "null")
70 多个接口
常规思路就是在界面各种点，然后把接口都丢进去爆破一下
![](https://gitee.com/nn0nkey/picture/raw/master/img/20250810024509.png "null")
GET，POST 都去跑一遍
然后这时候只需要在一堆历史包中去找了
然后发现了一些可以获取数据的包，但是 id 都是随机算法的，不可以遍历
不过找了一个很有趣的接口
![](https://gitee.com/nn0nkey/picture/raw/master/img/20250810024741.png "null")
首先我们看这个接口，有什么思路呢？
接口名称就是查询票据的信息应该是，但是我们看传入的参数呢，当然原数据还需要传入其他的没有作用的参数，没有用
这个参数名称就很值得思考啊，expr，表达式啊，而且我们看参数的数值
```php
expr=#ticket
```
常见表达式的基础语法
\*\*SpEL\*\*
- 以 `#` 开头引用变量：`#variable`
- 使用 `T()` 调用类和静态方法：`T(java.lang.Math).max(1,2)`
- 支持 `new` 关键字创建对象：`new java.lang.String('abc')`
- 支持访问 Map，既能用 `.key` 又能用 `['key']`
- 支持调用方法链和属性访问：`#obj.getName()`、`#obj.name`
- 支持三元运算符和 Elvis 运算符：`condition ? trueVal : falseVal`，`#var ?: 'default'`
- 支持集合和数组访问：`#list[0]`、`#map['key']`
\*\*EL\*\*
- 表达式写在 `${}` 或 `#{}` 里面
- 使用 `eq`、`ne`、`lt`、`gt`、`le`、`ge` 代替 `==`、`!=`、`<`、`>`、`<=`、`>=`
- 支持 `empty` 关键字判断空值：`${empty list}`
- 函数调用通常用 `fn:` 命名空间前缀：`${fn:length(list)}`
- 不支持 `new` 和直接类调用（没有 `T()`）
- 访问属性用点号 `.`，访问 Map 用 `['key']`
\*\*OGNL\*\*
- 变量和属性直接用点号访问：`user.name`
- 支持方法调用并省略括号：`user.getName`（括号可省略）
- 支持集合访问用 `[index]`：`list[0]`
- 逻辑表达式中可用 `==`、`!=` 等标准操作符
- 支持 `@class@method()` 形式调用静态方法：`@java.lang.Math@max(1,2)`
- 支持链式调用：`user.address.street.toUpperCase()`
- 支持三元运算符
\*\*MVEL\*\*
- 语法类似 Java，支持方法调用和属性访问：`user.name`、`user.getName()`
- 支持三元运算符
- 支持集合访问用 `[index]`：`list[0]`
- 支持静态方法调用用 `@` 符号：`@java.lang.Math@max(1,2)`
- 支持简写形式的变量赋值和表达式求值
- 支持 Lambda 表达式和闭包（高级特性）
这里可以看出来应该是 spel 表达式注入，我们尝试一下
全局绕过 payload+思维逻辑分析
-------------------
### 表达式确定
于是当我开始尝试 spel 表达式的时候
![](https://gitee.com/nn0nkey/picture/raw/master/img/20250810025841.png "null")
???，我一开始以为是这个不是 spel 表达式，可能表达式错了，然后我去尝试其他表达式
![](https://gitee.com/nn0nkey/picture/raw/master/img/20250810030143.png "null")
el 表达式回显的是计算失败??
我当时以为是计算了，证明应该是 el 表达式
但是当我更深入一步利用的时候
![](https://gitee.com/nn0nkey/picture/raw/master/img/20250810030257.png "null")
我发现了，不管你输入啥，都没有作用，都是这个回显??
我猜测可能是因为数据类型有问题，然后又一直尝试，发现这样才可以
![](https://gitee.com/nn0nkey/picture/raw/master/img/20250810030440.png "null")
回显 9
证明计算成功了，然后我再次使用内置对象的时候
![](https://gitee.com/nn0nkey/picture/raw/master/img/20250810030514.png "null")我真服了，又是这样，最后无限尝试中，摸索出来了，应该是 spel 表达式，因为 `#` 这样代变量也只能是 spel 表达式了吧
### 恶心的黑名单
为什么会报 400，那估计是有黑名单了
一般黑名单都会禁止直接实例化，我们测试一下
![](https://gitee.com/nn0nkey/picture/raw/master/img/20250810031154.png "null")
确定了，就是被 waf 了
![](https://gitee.com/nn0nkey/picture/raw/master/img/20250810031718.png "null")
但是 spel还支持 T 直接实例化对象
直接一个 T 是没有问题，但是
![](https://gitee.com/nn0nkey/picture/raw/master/img/20250810032009.png "null")
就是 T( 也被过滤了
想了好久，应该直接能够实例化的方法都不行了
别急，我还有办法
![](https://gitee.com/nn0nkey/picture/raw/master/img/20250810032238.png "null")
通过反射的方法来这样获取类，然后调用 getRuntime 方法
但是最后发现
![](https://gitee.com/nn0nkey/picture/raw/master/img/20250810032352.png "null")
![](https://gitee.com/nn0nkey/picture/raw/master/img/20250810032406.png "null")
全被 ban 了，哎，好不容易有发现，决定死磕到底
### getClass 审计源码 绕过
首先去翻了一下，spel 还有什么实例化的方法，比如 new 大小写绕过
![](https://gitee.com/nn0nkey/picture/raw/master/img/20250810033655.png "null")
还是不行啊
但是我就是不甘心，然后第二天再次去干，思考了一下，实例化方法是可能没办法了，因为表达式只有这几种实例化的方法，我还是决定从反射入手，但是必须先获取一个类啊，我于是去看了 getClass 的源码，看看还有什么方法能够获取类的
![](https://gitee.com/nn0nkey/picture/raw/master/img/20250810034326.png "null")
看到这个想到是不是可以先获取类加载器，然后再去加载类，我靠决定去尝试一手
但是获取类加载器得要一个类啊，尝试了一会都没有成功
最后看到了一个方法
```php
public Class<?>[] getClasses() {
checkMemberAccess(Member.PUBLIC, Reflection.getCallerClass(), false);
// Privileged so this implementation can look at DECLARED classes,
// something the caller might not have privilege to do. The code here
// is allowed to look at DECLARED classes because (1) it does not hand
// out anything other than public members and (2) public member access
// has already been ok'd by the SecurityManager.
return java.security.AccessController.doPrivileged(
new java.security.PrivilegedAction<Class<?>[]>() {
public Class<?>[] run() {
List<Class<?>> list = new ArrayList<>();
Class<?> currentClass = Class.this;
while (currentClass != null) {
Class<?>[] members = currentClass.getDeclaredClasses();
for (int i = 0; i < members.length; i++) {
if (Modifier.isPublic(members[i].getModifiers())) {
list.add(members[i]);
}
}
currentClass = currentClass.getSuperclass();
}
return list.toArray(new Class<?>[0]);
}
});
}
```
首先我们看这里是如何获取类的
currentClass = currentClass.getSuperclass()
于是我好奇的，是不是 getSuperclass 也可以啊
![](https://gitee.com/nn0nkey/picture/raw/master/img/20250810034800.png "null")
![](https://gitee.com/nn0nkey/picture/raw/master/img/20250810034907.png "null")
懂了，String 没有，这里我又弄了半天，于是看原代码，我发现了
```php
Class<?> currentClass = Class.this;
```
所以我们需要一个 class 呗
![](https://gitee.com/nn0nkey/picture/raw/master/img/20250810035028.png "null")
谁懂这个感觉，我靠真获取到了兄弟，于是开始杀起来
### 获取 Runtime 类
![](https://gitee.com/nn0nkey/picture/raw/master/img/20250810035453.png "null")
本地这样是没有问题的，但是
![](https://gitee.com/nn0nkey/picture/raw/master/img/20250810035526.png "null")
估计是因为+拼接字符串是因为在 idea 的语法是正确的，不是 java 的语法
然后想着用
![](https://gitee.com/nn0nkey/picture/raw/master/img/20250810041746.png "null")
但是发现在表达式可能是语法问题
![](https://gitee.com/nn0nkey/picture/raw/master/img/20250810041816.png "null")
直接就报错了
最后修改如下
```php
import org.springframework.expression.spel.standard.SpelExpressionParser;
import org.springframework.expression.spel.support.StandardEvaluationContext;
public class Test {
public void run() throws InterruptedException {
String expr="''.class.getSuperclass().forName('java.lang.suntime'.replace('s', 'R'))";
SpelExpressionParser parser = new SpelExpressionParser();
StandardEvaluationContext context = new StandardEvaluationContext();
Object calcResult = parser.parseExpression(expr).getValue(context);
System.out.println(calcResult);
}
public static void main(String[] args) throws InterruptedException {
new Tes...