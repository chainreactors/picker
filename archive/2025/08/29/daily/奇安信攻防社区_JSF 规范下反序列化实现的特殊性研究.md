---
title: JSF 规范下反序列化实现的特殊性研究
url: https://forum.butian.net/share/4519
source: 奇安信攻防社区
date: 2025-08-29
fetch_date: 2025-10-07T00:13:16.266115
---

# JSF 规范下反序列化实现的特殊性研究

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

### JSF 规范下反序列化实现的特殊性研究

* [漏洞分析](https://forum.butian.net/topic/48)

讲解jsf框架的成因，以及jsf框架下的gadget构造，最后以现实世界列子来突出漏洞风险。

### 0x01 简介
​ JSF（JavaServer Faces）是Java EE平台上的一个标准Web框架，采用组件化和事件驱动模型，简化了Java Web应用的用户界面开发。Apache MyFaces是JSF的一个开源实现，提供了完整的JSF功能和扩展，支持Facelets视图技术，增强了组件库和性能，广泛应用于企业级Java网页开发中。MyFaces与JSF规范兼容，帮助开发者快速构建可维护、可扩展的Web应用，同时支持EL表达式等现代特性，提升开发效率和代码清晰度。
### 0x02 反序列化漏洞
​ jSF应用中存在的不安全反序列化漏洞，主要源于JSF框架对视图状态（ViewState）的处理机制。ViewState用于保存页面组件的状态，通常以序列化对象形式存储在客户端（隐藏字段）或服务器端。当JSF框架（如Apache MyFaces或Mojarra）在反序列化ViewState时，如果没有对传入的数据进行充分验证或加密保护，攻击者可以构造恶意的序列化数据，利用反序列化过程执行任意代码或破坏应用逻辑，导致远程代码执行（RCE）等严重安全风险。
以xhtml和jsf等结尾，具体看配置
### 0x03 漏洞分析
在jsf的接口中如果传入\*\*javax.faces.ViewState\*\*就会进去流程
org.apache.myfaces.renderkit.html.HtmlResponseStateManager#getSavedState
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-44c8a1aac7f0eb5f47d8750f6000d2ccfe8e11fc.png)
从facesContext获取RequestParame传值。然后调用decode进行解码。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-7a687ea0f31146769c995d803c02a800c9179475.png)
解码过程中会调用StateUtils.reconstruct(token, facesContext.getExternalContext()) 进行还原对象
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-4e27c984a9b68a25715da307134b2b82a47a6ab9.png)
然后会得到数组，然后在ctx中获取配置，看是否设置了加密和开启了gzip压缩，不设置就是开启加密，不实用gzip。
开启加密就会下面的方法
org.apache.myfaces.shared.util.StateUtils#decrypt
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-2bdd8d825337bc6b3c24803b38d8f879e83757f8.png)
这个方法主要就是从ctx获取配置（加密key、iv、模式，algorithmParams）
```java
private static void testConfiguration(ExternalContext ctx) {
String algorithmParams = ctx.getInitParameter("org.apache.myfaces.ALGORITHM.PARAMETERS");
if (algorithmParams == null) {
algorithmParams = ctx.getInitParameter("org.apache.myfaces.ALGORITHM.PARAMETERS".toLowerCase());
}
String iv = ctx.getInitParameter("org.apache.myfaces.ALGORITHM.IV");
if (iv == null) {
iv = ctx.getInitParameter("org.apache.myfaces.ALGORITHM.IV".toLowerCase());
}
if (algorithmParams != null &amp;&amp; algorithmParams.startsWith("CBC") &amp;&amp; iv == null) {
throw new FacesException("org.apache.myfaces.ALGORITHM.PARAMETERS parameter has been set with CBC mode, but no initialization vector has been set with org.apache.myfaces.ALGORITHM.IV");
}
}
private static byte[] findInitializationVector(ExternalContext ctx) {
byte[] iv = null;
String ivString = ctx.getInitParameter("org.apache.myfaces.ALGORITHM.IV");
if (ivString == null) {
ivString = ctx.getInitParameter("org.apache.myfaces.ALGORITHM.IV".toLowerCase());
}
if (ivString != null) {
iv = (new Base64()).decode(ivString.getBytes());
}
return iv;
}
private static String findAlgorithm(ExternalContext ctx) {
String algorithm = ctx.getInitParameter("org.apache.myfaces.ALGORITHM");
if (algorithm == null) {
algorithm = ctx.getInitParameter("org.apache.myfaces.ALGORITHM".toLowerCase());
}
return findAlgorithm(algorithm);
}
private static String findAlgorithmParams(ExternalContext ctx) {
String algorithmParams = ctx.getInitParameter("org.apache.myfaces.ALGORITHM.PARAMETERS");
if (algorithmParams == null) {
algorithmParams = ctx.getInitParameter("org.apache.myfaces.ALGORITHM.PARAMETERS".toLowerCase());
}
if (algorithmParams == null) {
algorithmParams = "ECB/PKCS5Padding";
}
if (log.isLoggable(Level.FINE)) {
log.fine("Using algorithm paramaters " + algorithmParams);
}
return algorithmParams;
}
private static SecretKey getMacSecret(ExternalContext ctx) {
Object secretKey = (SecretKey)ctx.getApplicationMap().get("org.apache.myfaces.MAC\_SECRET.CACHE");
if (secretKey == null) {
String cache = ctx.getInitParameter("org.apache.myfaces.MAC\_SECRET.CACHE");
if (cache == null) {
cache = ctx.getInitParameter("org.apache.myfaces.MAC\_SECRET.CACHE".toLowerCase());
}
if (!"false".equals(cache)) {
throw new NullPointerException("Could not find SecretKey in application scope using key 'org.apache.myfaces.MAC\_SECRET.CACHE'");
}
String secret = ctx.getInitParameter("org.apache.myfaces.MAC\_SECRET");
if (secret == null) {
secret = ctx.getInitParameter("org.apache.myfaces.MAC\_SECRET".toLowerCase());
}
if (secret == null) {
throw new NullPointerException("Could not find secret using key 'org.apache.myfaces.MAC\_SECRET'");
}
String macAlgorithm = findMacAlgorithm(ctx);
secretKey = new SecretKeySpec(findMacSecret(ctx, macAlgorithm), macAlgorithm);
}
if (!(secretKey instanceof SecretKey)) {
throw new ClassCastException("Did not find an instance of SecretKey in application scope using the key 'org.apache.myfaces.MAC\_SECRET.CACHE'");
} else {
return (SecretKey)secretKey;
}
}
private static String findMacAlgorithm(ExternalContext ctx) {
String algorithm = ctx.getInitParameter("org.apache.myfaces.MAC\_ALGORITHM");
if (algorithm == null) {
algorithm = ctx.getInitParameter("org.apache.myfaces.MAC\_ALGORITHM".toLowerCase());
}
return findMacAlgorithm(algorithm);
}
```
就是从web.xml 配置中获取值
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-a4757d0b2aba37cadd168efd96cea2f30b985eb9.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-2316666bbee81291bdbad53e0713cd8f6e074787.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-400b904c260d636a8d94fc687eb248766ad3bf97.png)
不设置就设置这几个模式，DES/ECB/PKCS5Padding， macAlgorithm, DES key , HmacSHA1 key 随机生成。
在继续就是传入的数据还原成数组后取分隔最后20位，然后用最后20位对前面的数组数据进行验签，保证数据没有串改。
签证通过就调用cipher.doFinal(secure, 0, secure.length - macLenght) 对前面的数据就行解码。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-3f647c5f1438256d17206bb8d6ed8202d88d935e.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-6e77d170768d4228efc78b7ef123b144ef2dd4dd.png)
解码后判断ctx是否使用gzip，是就解码，默认不使用
最后就来到最重要的漏洞出发点。
org.apache.myfaces.shared.util.StateUtils#getAsObject
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-e2b63f618501d421726fd6139bde0dd9b1461144.png)
默认就是jdk 反序列化，除非你自己接口实现，应该没人蛋疼去实现hessian吧
获取反序列化类型，然后进行反序列化。
### 0x04 myface 自带 gadegt
​ myface框架自带一条gadget。
org.apache.myfaces.view.facelets.el.ValueExpressionMethodExpression
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-26d5d1ab49cd11514db5c60662a6b66f592feca9.png)
equals和hashcode回调用getMethodExpression
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-3f5730112eace4c945b65e30b3eb92c33d5e0a2a.png)
从当前facecontext中获取elcontext，然后直接getvalue，el表达式出发。
注意这里是facecontext，所以构造要用FacesContext构造。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-2d40638f737ab136647a4813f126f1ac6a9184e0.png)
其中属性限制是javax.el.ValueExpression的类型，从FacesContext获取，也就是用FacesContextImpl进行构造
### 0x05 gadget构造
```java
public static Object generatePayload(String payloads) throws Exception {
// 初始化 FacesContext 及 ELContext
FacesContextImpl fc = new FacesContextImpl((ServletContext) null, (ServletRequest) null, (ServletResponse) null);
//
FacesELContext elContext = new FacesELContext(new CompositeELResolver(), fc);
// 使用反射将 elContext 写入 FacesContextImpl 中
Field field = FacesContextImplBase.class.getDeclaredField("\_elContext");
field.setAccessible(true);
field.set(fc, elContext);
ExpressionFactory expressionFactory = ExpressionFactory.newInstance();
ValueExpression harmlessExpression = expressionFactory....