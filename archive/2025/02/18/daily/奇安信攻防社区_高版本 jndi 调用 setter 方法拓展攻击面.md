---
title: 高版本 jndi 调用 setter 方法拓展攻击面
url: https://forum.butian.net/share/4142
source: 奇安信攻防社区
date: 2025-02-18
fetch_date: 2025-10-06T20:35:05.129500
---

# 高版本 jndi 调用 setter 方法拓展攻击面

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

### 高版本 jndi 调用 setter 方法拓展攻击面

* [漏洞分析](https://forum.butian.net/topic/48)

这篇文章主要说了 JavaBeanObjectFactory 工厂类的 getobjectinstance 方法可以调用一些类的 setter 方法，但是跟踪过程中发现有一些限制，调用 setter 方法的顺序是固定的，不能够设置，因为这个原因导致 JdbcRowSetImpl 利用失败，然后需要我们的类的构造函数为 public，最后成功的是 JtaTransactionConfig，但是因为传入的 ref 属性不是 string，需要使用 BinaryRefAddr

高版本 jndi 调用 setter 方法拓展攻击面
==========================
总结
--
这篇文章主要说了 JavaBeanObjectFactory 工厂类的 getobjectinstance 方法可以调用一些类的 setter 方法，但是跟踪过程中发现有一些限制，调用 setter 方法的顺序是固定的，不能够设置，因为这个原因导致 JdbcRowSetImpl 利用失败，然后需要我们的类的构造函数为 public，最后成功的是 JtaTransactionConfig，但是因为传入的 ref 属性不是 string，需要使用 BinaryRefAddr
前言
--
前端时间也是研究了一下高版本的 jndi，然后看见了一些 paylaod，其中一个 paylaod 是打的 c3p0 的反序列化，属于是新东西了，学到了，听说是 unam4 师傅分享的，<https://xz.aliyun.com/u/52701>
本地工厂类
-----
这里只讲本地工厂类
我们看到 RMI 这部分相关的代码部分
```java
private Object decodeObject(Remote r, Name name) throws NamingException {
try {
Object obj = (r instanceof RemoteReference)
? ((RemoteReference)r).getReference()
: (Object)r;
/\*
\* Classes may only be loaded from an arbitrary URL codebase when
\* the system property com.sun.jndi.rmi.object.trustURLCodebase
\* has been set to "true".
\*/
// Use reference if possible
Reference ref = null;
if (obj instanceof Reference) {
ref = (Reference) obj;
} else if (obj instanceof Referenceable) {
ref = ((Referenceable)(obj)).getReference();
}
if (ref != null &amp;&amp; ref.getFactoryClassLocation() != null &amp;&amp;
!trustURLCodebase) {
throw new ConfigurationException(
"The object factory is untrusted. Set the system property" +
" 'com.sun.jndi.rmi.object.trustURLCodebase' to 'true'.");
}
return NamingManager.getObjectInstance(obj, name, this,
environment);
// } catch (NamingException e) { ...
}
```
我们的目的就是能够成功的 `return NamingManager.getObjectInstance(obj, name, this, environment);`
我们还是回到代码部分，什么时候会抛出异常
```java
if (ref != null &amp;&amp; ref.getFactoryClassLocation() != null &amp;&amp;
!trustURLCodebase) {
throw new ConfigurationException(
"The object factory is untrusted. Set the system property" +
" 'com.sun.jndi.rmi.object.trustURLCodebase' to 'true'.");
}
```
不抛出异常的话就是
1、令 ref 为空，或者
2、令 ref.GetFactoryClassLocation() 为空
3、令 trustURLCodebase 为 true
我们之前一直使用的是 3，因为这个就是个配置，而且之前一直默认为 true，但是高版本就不行了
但是还有 1 和 2，就有两种思路
我们看到 1 ref 为空，我们看到给 ref 赋值的地方
```java
if (obj instanceof Reference) {
ref = (Reference) obj;
} else if (obj instanceof Referenceable) {
ref = ((Referenceable)(obj)).getReference();
}
```
需要我们的 ref 既不是 Reference 也不是 Referenceable，即不能是对象引用，只能是原始对象
第二种
Ref.GetFactoryClassLocation() 返回空，让 ref 对象的 classFactoryLocation 属性为空，这个属性表示引用所指向对象的对应 factory 名称，对于远程代码加载而言是 codebase，即远程代码的 URL 地址(可以是多个地址，以空格分隔)，这正是我们针对低版本的利用方法；如果对应的 factory 是本地代码，则该值为空，这是绕过高版本 JDK 限制的关键
第一种不好利用：客户端直接实例化本地对象，远程 RMI 没有操作的空间
我们这里是利用的第二种
继续看 NamingManager 的解析过程
```java
// javax/naming/spi/NamingManager.java
public static Object
getObjectInstance(Object refInfo, Name name, Context nameCtx,
Hashtable&lt;?,?&gt; environment)
throws Exception
{
// ...
if (ref != null) {
String f = ref.getFactoryClassName();
if (f != null) {
// if reference identifies a factory, use exclusively
factory = getObjectFactoryFromReference(ref, f);
if (factory != null) {
return factory.getObjectInstance(ref, name, nameCtx,
environment);
}
// No factory found, so return original refInfo.
// Will reach this point if factory class is not in
// class path and reference does not contain a URL for it
return refInfo;
} else {
// if reference has no factory, check for addresses
// containing URLs
answer = processURLAddrs(ref, name, nameCtx, environment);
if (answer != null) {
return answer;
}
}
}
// try using any specified factories
answer =
createObjectFromFactories(refInfo, name, nameCtx, environment);
return (answer != null) ? answer : refInfo;
}
```
在处理 Reference 对象时，会先调用 ref.GetFactoryClassName() 获取对应工厂类的名称，如果为空则通过网络去请求，即上述链接前文的情况；如果不为空则直接实例化工厂类，并通过工厂类去实例化一个对象并返回。
但是因为高版本，肯定是不能通过 Url 去获取了，我们只能找本地的 Factory
因此，我们实际上可以指定一个存在于目标 classpath 中的工厂类名称，交由这个工厂类去实例化实际的目标类(即引用所指向的类)，从而间接实现命令执行
JavaBeanObjectFactory&amp;C3P0JavaBeanObjectFactory
---------------------------------------------------
查看了众多的 getObjectInstance 后看到 JavaBeanObjectFactory 类，然后C3P0JavaBeanObjectFactory类也是可以的
![image-20241025181726097](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/01/attach-ec368c9ee3613e03fd0eb5647b3e79f1ee6382f5.png)
它的方法如下
```java
public Object getObjectInstance(Object refObj, Name name, Context nameCtx, Hashtable env)
throws Exception
{
if (refObj instanceof Reference)
{
Reference ref = (Reference) refObj;
Map refAddrsMap = new HashMap();
for (Enumeration e = ref.getAll(); e.hasMoreElements(); )
{
RefAddr addr = (RefAddr) e.nextElement();
refAddrsMap.put( addr.getType(), addr );
}
Class beanClass = Class.forName( ref.getClassName() );
Set refProps = null;
RefAddr refPropsRefAddr = (BinaryRefAddr) refAddrsMap.remove( JavaBeanReferenceMaker.REF\_PROPS\_KEY );
if ( refPropsRefAddr != null )
refProps = (Set) SerializableUtils.fromByteArray( (byte[]) refPropsRefAddr.getContent() );
Map propMap = createPropertyMap( beanClass, refAddrsMap );
return findBean( beanClass, propMap, refProps );
}
else
return null;
}
```
其实我们光从类名上去理解是一个 javabean，而 javabean 最常见的就是属性的 setter 和 getter 方法了
我们跟进 findBean 方法
```java
protected Object findBean(Class beanClass, Map propertyMap, Set refProps ) throws Exception
{
Object bean = createBlankInstance( beanClass );
BeanInfo bi = Introspector.getBeanInfo( bean.getClass() );
PropertyDescriptor[] pds = bi.getPropertyDescriptors();
for (int i = 0, len = pds.length; i &lt; len; ++i)
{
PropertyDescriptor pd = pds[i];
String propertyName = pd.getName();
Object value = propertyMap.get( propertyName );
Method setter = pd.getWriteMethod();
if (value != null)
{
if (setter != null)
setter.invoke( bean, new Object[] { (value == NULL\_TOKEN ? null : value) } );
else
{
//System.err.println(this.getClass().getName() + ": Could not restore read-only property '" + propertyName + "'.");
if (logger.isLoggable( MLevel.WARNING ))
logger.warning(this.getClass().getName() + ": Could not restore read-only property '" + propertyName + "'.");
}
}
else
{
if (setter != null)
{
if (refProps == null || refProps.contains( propertyName ))
{
//System.err.println(this.getClass().getName() +
//": WARNING -- Expected writable property '" + propertyName + "' left at default value");
if (logger.isLoggable( MLevel.WARNING ))
logger.warning(this.getClass().getName() + " -- Expected writable property ''" + propertyName + "'' left at default value");
}
}
}
}
return bean;
}
}
```
代码有点小长，但是调用 setter 方法的逻辑确实很清晰的
获取属性名称并从 propertyMap 中查找对应的值。
获取属性的写方法（setter）。
如果找到对应的值且不为 null：
如果有写方法，则调用该方法将值赋给 Bean 的相应属性。如果值是 NULL\\_TOKEN（一个假定的常量，表示应赋值为 null），则将属性设置为 null。
Jndi+c3p0 组合拳
-------------
### 原理分析
我们知道出口类无非就是可以调用方法，或者加载恶意字节码，在 c3P0 中有一个方法可以加载 16 进制的字节，并且可以反序列化它
这里给一个链子的大概路径，方便分析
首先还是需要我们 fastjson 调用一个 setter 方法
```java
WrapperConnectionPoolDataSourceBase.setUserOverridesAsString---VetoableChangeSupport.fireVetoableChange--- WrapperConnectionPoolDataSource.VetoableChangeListener.vetoableChange---C3P0ImplUtils.parseUserOverridesAsString---SerializableUtils.fromByteArray---SerializableUtils.deserializeFromByteArray---readObject
```
这就是完整的路径了
### 漏洞复现
客户端代码
```java
package JNDI\_RMI;
import javax.naming.InitialContext;
public class RMI\_Cilent\_ByPass {
public static void main(String[]args) throws...