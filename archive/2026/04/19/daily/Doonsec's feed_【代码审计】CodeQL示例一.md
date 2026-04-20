---
title: 【代码审计】CodeQL示例一
url: https://mp.weixin.qq.com/s/lYaV4OrfRAFEw-72YKKi3A
source: Doonsec's feed
date: 2026-04-19
fetch_date: 2026-04-20T04:52:27.449130
---

# 【代码审计】CodeQL示例一

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ocg1gpicEs1ttmUFbl4UNbib92Bibnfa3NAZRHtXuQUpklrpib8RlUbHaRbgw7e5WCp1yra0pEKJPc95xNgMMvyQibNic6KpapQCdQWPVxIXG2Mqc/0?wx_fmt=jpeg)

# 【代码审计】CodeQL示例一

原创

十月的进阶之路
十月的进阶之路

十月的进阶之路

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 千行代码稳如狗，一洞破防全白搭。

## 目录

1. 定位入口
2. 确定输入参数
3. 确认敏感调用点之谁在做认证
4. 从调用点到函数实现
5. 在实现里找真正的漏洞模式

---

## 1、定位入口

本文依旧基于WebGoat靶场，由于我们之前已经手动测试过了，很多信息我们熟知于心，已经知道该站点提交数据到接口`/HijackSession/login`进行处理，因此我们先通过`ql`定位该接口在代码中的位置，我们先理清如下条件：

1. 它是一个`Spring`控制器里的路由方法。
2. 它的注解里有`path` 属性。
3. 其中路由`path`的值必须是`/HijackSession/login`，并将这个方法本身和它所在的控制器类找出来。

那么我们可编写出如下的`ql`检索语句。

```
import java
import semmle.code.java.frameworks.spring.SpringController

from
  SpringControllerMethod m,Annotation a,string p
where
  m.getADeclaredAnnotation() = a and
  a.getAStringArrayValue("path") = p and
  p = "/HijackSession/login"
select
  m,m.getDeclaringType()
```

上述符号解释如下：

```
// 库导入
import java; // 标准Java分析库
import semmle.code.java.frameworks.spring.SpringController; // Spring专用模型库

// 变量类型说明
// SpringControllerMethod: Spring控制器路由方法
// Annotation: 注解实例
// string: 路径字符串

// 核心谓词作用
m.getADeclaredAnnotation()      // 获取方法m上直接声明的注解
a.getAStringArrayValue("path")  // 获取注解a中"path"属性的字符串数组值
m.getDeclaringType()             // 获取方法m所属的类/接口
```

运行结果如下。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1ulBhGo6KCgI49aCf3BY5ib9Rf04bEYPQWbsOibasb8nfbk8883K17eyLekcJnGfUXg1p2B85QZcibqRI6CvEZs2TdzTXwborWMXw/640?wx_fmt=png&from=appmsg)

并且通过这一步我们精确定位到了代码位置。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1uvKCwrkjjcAcvgs9JY6d9kO7P6NJX27ka6ruz3waolDpNNqf5q50PIX9wFuC8l5eIicgVRghnZMKUicQ8ESASzwKBtibjSyNmZgk/640?wx_fmt=png&from=appmsg)

## 2、确定输入参数

我们接着编写如下的代码：

```
import java
import semmle.code.java.frameworks.spring.SpringController

from
  SpringRequestMappingMethod m,SpringRequestMappingParameter p
where
  m.getName() = "login" and
  m.getARequestParameter() = p and
  p.isTaintedInput()
select
  m,p
```

上述符号含义：

```
// ================== 字符含义 ==================
// SpringRequestMappingMethod m: Spring路由方法
// SpringRequestMappingParameter p: Spring路由参数

// ================== 核心谓词与检索条件 ==================
m.getName()                   // 获取方法名，限定为 "login"
m.getARequestParameter()      // 获取方法m的请求参数，关联到p
p.isTaintedInput()            // 判断参数p是否为用户可控的污点输入
```

我们定位到如下的内容，当然这里面包含着不同的其他关卡的`login`以及来自于外部用户可控的输入，可以通过继续添加条件来进一步精确内容，譬如通过唯一值的注解路由确定。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ocg1gpicEs1vEU0JMjxhmQbRpF7052eZdyafoTz9iajJFRReAIsrygvxCsx50dp1d4VRaNF3RSkHVvV8HXHdkVRjWuxQZZW0sIKxmhuO0EoibI/640?wx_fmt=png&from=appmsg)

当然我们希望检索的内容也赫然在列，其中`username，``password，``cookieValue`均为外部输入，也就是所谓的污点输入。不过也不是所有内容都值得去追，谁进入了认证分支，谁就值得继续追进。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1sK9icpDqXDuN2eljEoIRrKplWPbsyGse0368IgwUmMQxibfZ8Zfz24gxP4YJUia1LPIjFdgjD5CbysJuh3Vmdpk8W0JibENicNqsQM/640?wx_fmt=png&from=appmsg)

## 3、确认敏感调用点之谁在做认证

接下来查的是调用点，不是实现点，先锁定`login`方法内部所有调用，再把目标缩到目标方法，先给出检索的条件：

1. 方法名`login`
2. 调用发生在`login`方法内部
3. login方法所属的类名`HijackSessionAssignment已经通过第二步已经得到。`

结合条件给出如下的参考代码。

```
import java

from
  Method m,MethodCall c
where
  m.getName() = "login" and
  c.getEnclosingCallable() = m and
  m.getDeclaringType().getName() = "HijackSessionAssignment"
select
  c,c.getArgument(0)
```

其中详细的解释如下。

```
// ================== 核心谓词作用 ==================
m.getName()                   // 获取方法名称
c.getEnclosingCallable()      // 获取包含该调用的外层方法
m.getDeclaringType().getName()// 获取方法所属类的类名
c.getArgument(0)              // 获取方法调用的第1个参数
```

上述检索语句运行结果如下。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1s4EOBYEAnicZcLFeQiadUeuzedYyibialjRicMBZeMOj8Yw9cmoAdXOlZl4wmbz9Pp1hbZJZymfv16MucIkxhtRGNGVu6ibFkUwUmgA/640?wx_fmt=png&from=appmsg)

同时通过`vscode`的跳转功能也能直接定位到代码点，如下图所示。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1sSlFicke9H8p3e8I90Xbc5eEa00bTbxQZ7UkRqDK4Hq166tywicicHbQQ7DwMibXKUIEvHw17mA03gfvo4qGpNeT6mBnpLicGIJHYo/640?wx_fmt=png&from=appmsg)

当然又可以根据上述检索结果进一步完善检索语句获得更加精准的结果，譬如这里我们只想检索`authenticate`函数，因为本关卡的漏洞点就在这个函数中，因此我们可以给出如下的检索语句。

```
import java

from
  Method m,MethodCall c
where
  m.getName() = "login" and
  c.getEnclosingCallable() = m and
  c.getMethod().getName() = "authenticate"
select
  c,c.getArgument(0)
```

这样我们就能直接定位到我们在意的`authenticate`函数位置。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ocg1gpicEs1uyLRZSibEnos5yWUasZpIa1W2q6d7vUI0lE2qgqictnhyxEoicHUnY8XzKzuPWgR5oNIVXtNH531Gyxots3KiaKcyP6ImGdv73DNY/640?wx_fmt=png&from=appmsg)

但是匹配了两处，其实我们知道只需要匹配`else`分支中的调用，此时需要利用`codeql`的抽象语法树（`AST`）`api，`判断`MethodCall`是否位于`IfStmt`（`If`语句）的`else`分支内，先分析条件：

1. 定位类中名为`login`的方法。
2. 筛选`login`方法内对`authenticate`的调用。
3. 仅保留位于`if-else`语句`else`分支中的调用。
4. 输出符合条件的调用语句及其第一个参数。

参考如下代码。

```
import java

from
  Method m,MethodCall c,IfStmt ifs,Stmt s
where
  m.getName() = "login" and
  c.getEnclosingCallable() = m and
  c.getMethod().getName() = "authenticate" and
  c.getAnEnclosingStmt() = s and
  ifs.getElse() = s
select
  c,c.getArgument(0)
```

运行结果如下，通过`AST`我们精准的定位到了目标函数。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ocg1gpicEs1sOJqRDwBSJAj886DZmZykfQxR4z4hZLtorvmibOrJR04jI8YF6rT4Xub5OJH4qzYic8b3N24vP8hiaCjdCrBkPpOlSnuk7Vj3t4o/640?wx_fmt=png&from=appmsg)

## 4、从调用点到函数实现

先把入口方法里的`authenticat`调用抓出来，再拿到它指向的目标`callable，`最后审这个`callable`的内部逻辑，`MethodCall.getMethod()`可以直接得到目标方法。

```
import java

from
  Method m,MethodCall c,IfStmt ifs,Stmt s
where
  m.getName() = "login" and
  c.getEnclosingCallable() = m and
  c.getMethod().getName() = "authenticate" and
  c.getAnEnclosingStmt() = s and
  ifs.getElse() = s
select
  c.getMethod(),c.getMethod().getDeclaringType(),c.getArgument(0)
```

通过上述代码即可定位到具体的实现，与前一小节没什么区别。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ocg1gpicEs1tQicCqcgibquybq8bP6bxBYmhaRtSic8CbibdaUaVscKyGO1ZbtsOEDTqtQ6vo0FbSWQxMJrcvk2Xg701RLP5zF3llkNVIlKhvicrg/640?wx_fmt=png&from=appmsg)

## 5、在实现里找真正的漏洞模式

这里实现的关键逻辑分为两段，如果`authentication.getId()`不为空，并且生成的userid在`sessions`队列里，那么就直接设置`setAuthenticated(true)`。如果`authentication.getId()`为空，就分配一个新`id`，但这个`id`的生成方式包含`Random.nextLong()`、递增计数和`Instant.now().toEpochMilli()`，按照如下条件查询。

1. 查找代码库中名为`authenticate`的方法
2. 筛选同时包含`contains`成员检查和`setAuthenticated`直接设权的方法
3. 输出符合条件的方法及预设的安全审计说明字符串

编写的参考代码如下。

```
import java

from
  Method auth
where
  auth.getName() = "authenticate" and
  exists(
    MethodCall c|
    c.getEnclosingCallable() = auth and
    c.getMethod().getName() = "contains"
  ) and
  exists(
    MethodCall c|
    c.getEnclosingCallable() = auth and
    c.getMethod().getName() = "setAuthenticated"
  )
select
  auth,"authentication depends on membership check + direct auth flag"
```

部分谓词（`Predicate`）说明如下

```
// ================== 核心谓词作用 ==================
auth.getName()                   // 获取方法名称
exists(...)                      // 判断括号内的条件是否至少存在一个匹配
c.getEnclosingCallable()         // 获取包含调用c的外层方法
c.getMethod().getName()          // 获取被调用方法的名称
```

通过上述规则，我们能直接定位到集合命中就认证的内部认证策略上。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1uc8jBdTmLJMooic0PXFpibsvmjwDtn9sZH7FgaicUHhfv5BkN79LbRoL8GSz0K27qGpDlj3qI724hF7vAQuzaALDK6Z7YeCyXtaw/640?wx_fmt=png&from=appmsg)

当然这个漏洞的核心逻辑是`++id`使得每次调用`GENERATE_SESSION_ID`生成的值都比上一次大`1，`即便拼接了时间戳，攻击者只需知道任意一个有效`session ID`就能枚举出其他值，先给出检测逻辑：

1. 查找代码库中的静态`long`类型字段。
2. 筛选对该字段进行前置自增的操作。
3. 筛选该自增操作直接参与加法的场景。
4. 输出符合条件的加法表达式及`session ID`可预测的安全风险提示。

编写查询规则如下。

```
import java

from AddExpr add, PreIncExpr inc, Field f
where
  f.isStatic() and
  f.getType().hasName("long") and
  inc.getOperand().(FieldAccess).getField() = f and
  (
    add.getLeftOperand() = inc or
    add.getRightOperand() = inc
  )
select add, "静态 long 字段 '" + f.getName() + "' 自增后拼接，session ID 可预测"
```

部分谓词含义如下。

```
// ================== 核心谓词作用 ==================
f.isStatic()                          // 判断字段是否为静态
f.getType().hasName("long")          // 获取字段类型并判断是否为long
inc.getOperand().(FieldAccess).getField() // 获取前置自增操作的字段
add.getLeftOperand() / add.getRightOperand() // 获取加法的左右操作数
f.getName()
```

通过运行该规则可以直接检测到本关卡的核心漏洞点。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ocg1gpicEs1sJfk3wU0AWpqzvEFGw9mAb4QeFiaoT3fq...