---
title: 告别脚本小子系列丨JAVA安全(8)——反序列化利用链（下）
url: https://www.4hou.com/posts/PK66
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-06-28
fetch_date: 2025-10-04T11:44:34.050066
---

# 告别脚本小子系列丨JAVA安全(8)——反序列化利用链（下）

告别脚本小子系列丨JAVA安全(8)——反序列化利用链（下） - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# 告别脚本小子系列丨JAVA安全(8)——反序列化利用链（下）

盛邦安全
[行业](https://www.4hou.com/category/industry)
2023-06-27 14:05:05

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)101040

收藏

导语：告别脚本小子系列丨JAVA安全(8)——反序列化利用链（下）

**0x01 前言**

在前面的文章中介绍了基于CC链的反序列化利用方式，并且通过最终调用Runtime类的exec方法达到命令执行的效果。在CC链中还可以通过xalan来执行命令。

xalan是java操作xml的库，属于java内置的官方库之一，在CC链中主要用到的是com.sun.org.apache.xalan.internal.xsltc.trax.TemplatesImpl类。与上篇文章中提到的利用链不同，xalan最终是通过加载字节码来达到代码执行的效果，所以xalan更适合于执行语句的场景，利用xalan来植入内存马会比其他链更加方便。如果目标同时可以使用多条CC链，通常会更倾向于使用xalan相关的链。

1

[告别脚本小子系列丨JAVA安全(1)——JAVA本地调试和远程调试技巧](https://mp.weixin.qq.com/s?__biz=MzkzNjMxNDM0Mg==&mid=2247483768&idx=1&sn=36ff6d279fa7dbd7d5ae00b06a3c3ddc&chksm=c2a1d5f1f5d65ce701e1f73ce0f584412bfc38a507622758f2acabce370cdcc4bb4af2270045&token=1637952127&lang=zh_CN&scene=21#wechat_redirect)

2

[告别脚本小子系列丨JAVA安全(2)——JAVA反编译技巧](https://mp.weixin.qq.com/s?__biz=MzkzNjMxNDM0Mg==&mid=2247483803&idx=1&sn=1af141cd5623b2682cfbdc2c12a53309&chksm=c2a1d512f5d65c04bc046ee83de4ba98881d086837f05cef581b39323026195b504bb5635c4c&token=1637952127&lang=zh_CN&scene=21#wechat_redirect)

3

[告别脚本小子系列丨JAVA安全(3)——JAVA反射机制](https://mp.weixin.qq.com/s?__biz=MzkzNjMxNDM0Mg==&mid=2247483830&idx=1&sn=39c08c61cbab36ace4ac691e0756948b&chksm=c2a1d53ff5d65c29f9b8310c324c67568fe27e61720baffff8af19ef9cb94f5096d73df0c69f&token=1637952127&lang=zh_CN&scene=21#wechat_redirect)

4

[告别脚本小子系列丨JAVA安全(4)——ClassLoader机制与冰蝎Webshell分析](https://mp.weixin.qq.com/s?__biz=MzkzNjMxNDM0Mg==&mid=2247483971&idx=1&sn=13bc478b9bad8c40279f4a2b22c7e29e&chksm=c2a1d6caf5d65fdc4c76043ba0650ca947722c69bfd4bca69a4ef35d3fb318b5cf26fa557c6d&token=1295938837&lang=zh_CN&scene=21#wechat_redirect)

5

[告别脚本小子系列丨JAVA安全(5)——序列化与反序列化](https://mp.weixin.qq.com/s?__biz=MzkzNjMxNDM0Mg==&mid=2247484384&idx=1&sn=675a280b04097ab115a98b623ffc9957&chksm=c2a1d769f5d65e7ff06adba1117ee14d1d772baedcd822302c5827b77fd6177a55f1c6add46b&token=1295938837&lang=zh_CN&scene=21#wechat_redirect)

6

[告别脚本小子系列丨JAVA安全(6)——反序列化利用链（上）](https://mp.weixin.qq.com/s?__biz=MzkzNjMxNDM0Mg==&mid=2247485071&idx=1&sn=830634ad6a570e08a1b5d6780175f028&chksm=c2a1d206f5d65b10f9a731195f726d2885aec965d9ba37551113b81c9afa045a4079480360d3&token=1452276723&lang=zh_CN&scene=21#wechat_redirect)

7

[告别脚本小子系列丨JAVA安全(7)——反序列化利用链（中）](https://mp.weixin.qq.com/s?__biz=MzkzNjMxNDM0Mg==&mid=2247485935&idx=1&sn=1ea3b73a420f788dfda878f367a3b4b0&chksm=c2a1dd66f5d654707dd6a554a80f99710faf10229df5059ed8a754b90a424e016b8cffaf94c6&token=193222565&lang=zh_CN&scene=21#wechat_redirect)

**0x02 Xalan链分析**

java.lang.ClassLoader是java中负责类加载的抽象类，类中包含一个特别重要的方法defineClass，defineClass方法接受一组字节，然后将其具体化为一个Class类型实例，它一般从磁盘上加载一个文件，然后将文件的字节传递给JVM，通过JVM（native 方法）对于Class的定义，将其具体化，实例化为一个Class类型实例。目前流行的jsp的webshell冰歇和哥斯拉均是采用这种方式来传递的恶意代码。

在TemplatesImpl类的defineTransletClasses方法中，存在对defineClass方法的调用，如图2.1所示。并且传递的参数来源于类私有的属性\_bytecodes。

![1687845301474328.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230627/1687845612109778.png "1687845301474328.png")

图2.1 在defineTransletClasses方法中调用defineClass方法

除了通过defineClass来生成Class对象之外，还需要通过newInstance方法来生成类对应的实例。向上查找调用了defineTransletClasses方法的其他方法，如图2.2所示。

![1687845269198783.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230627/1687845613345606.png "1687845269198783.png")

图2.2 在getTransletInstance方法中调用了目标方法，并进行实例化

由于getTransletInstance方法是private类型的方法，不利于在反序列化利用链中进行调用，继续向上查找调用了getTransletInstance方法的其他方法，如图2.3所示。

![1687845350185100.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230627/1687845614183046.png "1687845350185100.png")

图2.3 通过newTransformer方法调用getTransletInstance方法

这里的newTransformer方法已经是一个public类型的方法了，可以直接在反序列化利用链中进行调用。但是在TemplatesImpl类中还存在对newTransformer方法调用的另外的方法，如图2.4所示。

![1687845399247875.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230627/1687845615115862.png "1687845399247875.png")

图2.4 通过getOutputProperties方法调用newTransformer方法

在TemplatesImpl类中提供了通过defineClass动态加载字节码并进行实例化的方式，这是TemplatesImpl类能够在多种不同类型反序列化利用链中出现的根本原因。并且由于自身内部方法间相互调用的关系，可以总结只要满足下面表的条件之一，则可以达到通过TemplatesImpl类执行命令的效果。

表2.1 TemplatesImpl类提供的调用方式

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230627/1687845616995730.png "1687845466735170.png")

在TemplatesImpl类中调用对应的方法，可以达到命令执行的效果，如图2.5所示。方法一和方法二均能达到一样的命令执行效果。

![1687845484212715.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230627/1687845617932912.png "1687845484212715.png")

图2.5 通过TemplatesImpl来执行命令

**0x03 基于Xalan的CC链**

在CC3的利用链中最终是通过Xalan来执行命令，CC3的利用链和通过com.sun.org.apache.xalan.internal.xsltc.trax.TrAXFilter类的构造方法来调用newTransformer方法，达到通过Xalan执行命令的效果，如图3.1所示。

![1687845561172637.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230627/1687845618211279.png "1687845561172637.png")

图3.1 在TrAXFilter类的构造方法中调用newTransformer方法

下一步的关键是看如何调用TrAXFilter类的构造方法，ysoserial的作者并没有直接找TrAXFilter类的构造方法调用，而是通InstantiateTransformer类的transform方法中存在调用任意类的getConstructor方法来调用TrAXFilter类。如图3.2所示。

![1687845587189085.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230627/1687845618168369.png "1687845587189085.png")

图3.2 在InstantiateTransformer类的transform方法中调用TrAXFilter类的构造方法

剩下如何调用InstantiateTransformer类的transform方法与CC1利用链完全一致，如图3.3所示。这里不对其中完全一致的内容再做分析。

![1687845616110107.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230627/1687845616110107.png "1687845616110107.png")

图3.3 CC3利用链和CC1利用链对比

除了CC3的链以外，还有CC2、CC4、CB链均与Xalan有关，Xalan提供了一种执行复杂语句的方式，掌握Xalan链有助于编写高级复杂的反序列化利用代码。

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?09shiCpU)

#### 你可能感兴趣的

* [![]()

  Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)
* [![]()

  【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)
* [![]()

  蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)
* [![]()

  聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)
* [![]()

  2025第五届太原网络安全高峰论坛成功举办](https://www.4hou.com/posts/8gJl)
* [![]()

  特勤局手册 | 监听办公室](https://www.4hou.com/posts/42B2)

![](https://img.4hou.com/portraits/3c8d3af7c49c95c16dd14518142759d6.png)

# [盛邦安全](https://www.4hou.com/member/9ZO4)

让网络空间更有序

#### 最新文章

* [Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)
  2025-09-29 17:48:04
* [【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)
  2025-09-29 14:55:37
* [蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)
  2025-09-29 14:23:50
* [聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)
  2025-09-28 17:20:40

[查看更多](...