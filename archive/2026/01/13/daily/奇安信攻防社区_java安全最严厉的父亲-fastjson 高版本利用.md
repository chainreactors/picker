---
title: java安全最严厉的父亲-fastjson 高版本利用
url: https://forum.butian.net/share/4715
source: 奇安信攻防社区
date: 2026-01-13
fetch_date: 2026-01-14T03:33:03.412074
---

# java安全最严厉的父亲-fastjson 高版本利用

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

### java安全最严厉的父亲-fastjson 高版本利用

* [渗透测试](https://forum.butian.net/topic/47)

fastjson 写文件

### 0x01 简介
​ 主要还是看killer那个 ctf，然后以前实战也没怎么认真去打（坑太多了）。这次正好学习一下。
### 0x02 fastjson 加载
com.alibaba.fastjson.parser.ParserConfig#checkAutoType(java.lang.String, java.lang.Class&lt;?&gt;, int)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-835ee73c4f3c6da0506064b16510cd1af2237249.png)
主要就是检查@type 指定的类
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-e2916423a62fd6ec3b4993a0d69495faf14ed338.png)
然后在判断时候在在反序化的map、缓存的map中，然后判断是不是白名单。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-5d60f5e5d0205ea6027424a159e56d35084150a2.png)
要是获取到就判断这些。不是期望类直接就包type not match。基本高版本要是不指定期望类,这一步就g了
### 0x03 写class后fastjson 加载机制（docbase）
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-8733f47febbd1ea101b4af930c9aefb9076dbbe5.png)
如果我们利用cmonsio写入文件后, 这里都会获取不到，不再缓存 不是白名单，且这个classloader为null
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-e5e0fb356b6014563aa276c6d2e6f2dbbf2e78b0.png)
这个时候就会调用classloader去获取这个class的流
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-3b50f306f7f13f25bcf0442c15409b4073763dbc.png)
这里清楚可以看到是sun.misc.Launcher$AppClassLoader
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-680130d07d1e92b3ef84c90cd152dbca627c7c43.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-e523fac399fcc9450f3eed950185e1f55c8cb5f1.png)
他的classpath路径jre的lib，jre下的class（默认没有）和项目的lib目录。
我们要是写文件在docbase目录下, 使用这个classloader是加载不到的。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-9f8632467b55d81f20bdd7940023ecef9cd89f31.png)
最后来到这里
若果他是白名单类、jsonType，期望类的话。就会调用TypeUtils.loadClass(typeName, this.defaultClassLoader, cacheClass)，要是这个类是白名单或者jsonType就会进行缓存
com.alibaba.fastjson.util.TypeUtils#loadClass(java.lang.String, java.lang.ClassLoader, boolean)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-3d10aa783dbaa5f24df9b8174e97fc4cf2e59ff6.png)
来到这里，这个defaulrclassloder是null，所以这里都是加载不到我们写入到docbase的类。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-1f3f6350644f9a270f1f725469650975e61735fe.png)
最后会来到这里。使用当前线程的classloader来加载
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-25f9adace5b1fc15cc3cb3df96bedd8fe7f1782b.png)
可以看到是webappclassloader
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-1d1940c8e24608569f17067f6e9c5bcdbb20406b.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-855134307ec493afd706c1e2e861d2ca20376c78.png)
这里可以清楚看到docbase的目录。也就是说写入到docbase下的类要用webappclassloader才能加载到。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-c68fe62e5810b5a24488e8fc49776aa854535643.png)
根据cache标志位，是否加入缓存。这cache就是前面提到的
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-a677baf6a3d259d5b6c6984e4232d308a1d17ad1.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-8e4b3266396a57a807fc2365efb475b3624e7273.png)
最后又再次判断。
这也是为什么我写入到docbase后，要使用
```http
{
"@type":"java.lang.Exception",
"@type":"org.example.Exception"
}
```
这种形式来加载，expectClassFlag这样为true，然后使用webappclassloaer加载。
### 0x04 fastjson 1.x 全版本饶过
再回到上面
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-a40824876d2a5b43b67a79586d716ffe77be55f1.png)
如果我们获取到class的流，然后调用ClassReader读入，在字节信息中获取到jsonType信息，jsonType就会改为true。也就是完全可以写一个后门类，类打上@JSONType就行。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-a91e143aba0d9284bd0c1132c927c4a16149f03a.png)
这样就能符合它的判断，jsontype标志位也变为true
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-da4695d330d2c86ce6daee3e3552b2f8e5ce1cc4.png)
最后加入缓存。这样1.2.83也能触发。
但是在cmonsio写文件下这种情况下没什么意义, 写docbase 继承期望类就能正常加载，不继承在过不了判断，无法使用webappclassload加载，也就获取不到类，写到jre/lib需要替换懒加载的jar包，毫无意义。
### 0x05 1.2.83 fastjson利用
在1.2.83的情况下，类名结尾为Exception或Error会直接返回null。
这个时候只能在sun.misc.Launcher$AppClassLoade来加载，也就是在jre下找利用，就是最经典的写懒加载jar包替换。
一般以chaset.jar、nashorn.jar,dnsns.jar 为主。
需要结合目录穿越写文件写到jre/lib目录。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-2110c0087b1f1a72e745147917f3332337fad754.png)
一般在源码写上然后编译，这样不影响正常功能。
为了方便复现。这里只打包一个类
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-fd45e6bbac616f8770ed06106aff6328c8c73c63.png)
改成83 手动替换jar
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-4cb9b8acdf9ef8f57a65a8bdbbed8c4e9209ef67.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-22abd5481c4dfa89f2713308f8aea7202bbfcf7c.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-63224ac661a7ac948ffbe409a27b97a553353ae2.png)
### 0x06 commonsio 优化
org.apache.commons.io.input.CharSequenceInputStream
在commons-io 2.0-2.1上是没有的, 以及在高低版本上字节信息不同。c/cs
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-1557d76205b47783ad458f437203b25b0b1b3ba6.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-75c590a5549af0600b9a6fe251132770298d5c44.png)
所以这里我套娃了一下，用org.apache.commons.io.input.CharSequenceReader的是配，这样io在2.0-2.7上都能利用。
再就是在不同系统os上，类随机到构造方法不同，导致写不了二进制数据。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-6e754977b72ef761ae9f47d69e9016ac21d648db.png)
io低版本会在linux随到decoder这个构造，不给decoder赋值，在解码流就会包空异常，
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-cccdfd62d6c3afa2aa235fdba489d3395d5446af.png)
能利用的就是utf8，写不了二机制，只能利用ascii jar写入。实战千万别用，要是没打下目录，lib替换了影响服务。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-72700e613698d6867272ea2e2b096a8e630abcfe.png)
随到这个就正常对charset赋值可以二进制数据。其余都没什么好说的了。
### 0x07 加入chains
​ 不得不说，fastjson真是java安全绕不过的大山。为此我也加入到chains。支持1.2.68 ，1.2.75-1.2.80.
io 2.0-2.7写文件
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-4ef642de9638b388a3a995d370c32d5d30285bfd.png)
在能写二进制的情况下直接选就行
不能写二进制的话，使用
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-963c14463cf14ca0ab17b960afdc5b88cb0be586.png)
进行上传你要写的文件。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-a13f21e0b66a8c5bbfbde540adb930a1e30cc4ad.png)
然后根据情况选择payload。
### rerference
<https://su18.org/post/fastjson-1.2.68/>
<https://flowerwind.github.io/2025/02/28/%E5%88%86%E4%BA%AB%E4%B8%80%E6%AC%A1%E7%BB%84%E5%90%88%E6%BC%8F%E6%B4%9E%E6%8C%96%E6%8E%98%E6%8B%BF%E4%B8%8B%E7%9B%AE%E6%A0%87/>
​

* 发表于 2026-01-13 09:00:00
* 阅读 ( 1126 )
* 分类：[漏洞分析](https://forum.butian.net/community/Vul_analysis)

1 推荐
 收藏

## 0 条评论

请先 [登录](https://forum.butian.net/login) 后评论

[![Unam4](https://forum.butian.net/static/images/default_avatar.jpg)](https://forum.butian.net/people/17413)

[Unam4](https://forum.butian.net/people/17413)

4 篇文章

[奇安信攻防社区](https://forum.butian.net)|
联系我们

|
[sitemap](https://forum.butian.net/sitemap)

Copyright © 2013-2026 BUTIAN.NET 版权所有 [京ICP备18014330号-2](https://beian.miit.gov.cn/#/Integrated/index)

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

#### ![Unam4](https:/...