---
title: Android逆向前期准备
url: https://www.secpulse.com/archives/195484.html
source: 安全脉搏
date: 2023-02-14
fetch_date: 2025-10-04T06:30:37.617628
---

# Android逆向前期准备

[![](https://www.secpulse.com/wp-content/themes/secpulse2017/img/logo-header.png)](https://www.secpulse.com "安全脉搏")

* [首页](https://www.secpulse.com/)
* [分类阅读](https://www.secpulse.com/archives/category/category)

  #### 脉搏文库

  - [内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)
  - |
  - [代码审计](https://www.secpulse.com/archives/category/articles/code-audit)
  - |
  - [安全文献](https://www.secpulse.com/archives/category/articles/sec-doc)
  - |
  - [Web安全](https://www.secpulse.com/archives/category/articles/web)
  - |
  - [移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)
  - |
  - [系统安全](https://www.secpulse.com/archives/category/articles/system)
  - |
  - [工控安全](https://www.secpulse.com/archives/category/articles/industrial-safety)
  - |
  - [CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)
  - |
  - [IOT安全](https://www.secpulse.com/archives/category/iot-security)
  - |

#### 安全建设

+ [业务安全](https://www.secpulse.com/archives/category/construction/businesssecurity)
+ |
+ [安全管理](https://www.secpulse.com/archives/category/construction/securityissue)
+ |
+ [数据分析](https://www.secpulse.com/archives/category/construction/bigdata)
+ |

#### 其他

+ [资讯](https://www.secpulse.com/archives/category/news)
+ |
+ [漏洞](https://www.secpulse.com/archives/category/vul)
+ |
+ [工具](https://www.secpulse.com/archives/category/tools)
+ |
+ [人物志](https://www.secpulse.com/archives/category/people)
+ |
+ [区块链安全](https://www.secpulse.com/archives/category/exclusive/block_chain_security)
+ |
+ [安全招聘](https://www.secpulse.com/archives/category/hiring)
+ |

- [安全问答](https://www.secpulse.com/newpage/question_list)
- [金币商城](https://www.secpulse.com/shop?donotcachepage=c010349fd98847cb9d6e07d3cbc19288)
- [安全招聘](https://www.secpulse.com/archives/category/hiring)
- [活动日程](https://www.secpulse.com/newpage/activity)
- [live课程](https://www.secpulse.com/live)
- [企业服务](https://duoyinsu.com/service.html)
- [插件社区](https://x.secpulse.com/)

小程序

![脉搏小程序](https://www.secpulse.com/wp-content/themes/secpulse2017/img/wxchat.jpg)
[登录](https://www.secpulse.com/user_login)
|
[注册](https://www.secpulse.com/user-register)

# Android逆向前期准备

[移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)

[公众号坚毅猿](https://www.secpulse.com/newpage/author?author_id=49456)

2023-02-13

20,492

[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/image6-1024x576.png "image6-1024x576.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/image6.png)

> **本公众号分享的所有技术仅用于学习交流，请勿用于其他非法活动，如果错漏，欢迎留言指正**

> 《Android软件安全与逆向分析》丰生强
>
> 《 Android应用安全防护和逆向分析》姜维

# Android逆向前期准备

## 一、前置知识

### 为什么学习安卓逆向

1. 学习研究

* 去广告
* 破解内购
* 自动化

+ 臧航准备网自动登陆
+ 车智赢自动登陆
+ 大姨妈自动登陆
+ 京东价格监控
+ 酒仙网自动登陆，预约茅台
+ 大商天狗自动登陆，预约茅台
+ 司小宝自动登陆

* 刷播放量

+ 刷B站完播率，批量注册B站账号

* 获取评论

+ 抓取得物的推荐区的评论
+ 抓取抖音评论

* 根据关键词搜索商品

+ 识货搜索型号，获取到尺码和价格
+ 唯品会搜索商品
+ 知乎搜索

* ......

### 学习安卓逆向需要准备什么

#### 学安卓逆向的前置知识

* 逆向分为：安卓逆向，win逆向

+ 逆功能：破解内购道具，去广告等等
+ 逆协议：比如，某APP注册的时候有一个`Sign`的加密。这时候app逆向`逆的是协议`(让爬虫爬到app的数据)
  需要学习的内容：

+ java开发环境
+ Android开发环境
+ c开发环境
+ python开发环境
+ JavaScript开发环境
+ 真机(解BL锁，刷Magisk，装Xpose)
+ 其他工具

* 1. 环境搭建：

+ java：基础语法，面向对象、接口，反射机制等。各类常见加密算法的java层实现和破解方法
+ 四大组件( activity,service,provider,broadcast)，界面控件，消息事件处理、网络通信等

* 2. Android应用开发：

+ 回编译(AndroidKiller)
+ smali汇编
+ 静态逆向分析(jadx)
+ 动态调试(jeb、AndroidStudio）
+ java层的反调试与反反调试

* 3. java层逆向：

+ `C`语言：数据类型，语法糖，指针，常见加密算法native层实现。
+ NDK开发(linux下的`so`类似win下的`dll`)
+ ARM汇编(寄存器，指令码，立即值，常量)。
+ 静态分析、动态调试(双IDA调试)。
+ native层中反调试与反反调试
+ unicorn/unidbg

* 4. native层逆向：

+ xposed(java、Android Studio)
+ Frida(python、JavaScript、pycharm)
+ 特征检测与绕过
+ 沙箱

* 5. HOOK与注入技术框架:

+ hHTTP/S、TCP、Websocket详解
+ 各种反抓包原理及破解方法

* 6. APP协议分析(抓包)
* 7. 加壳与脱壳

+ ollvm

* 8. 定制rom

+ Android源码编译
+ root检测绕过
+ @Todo

#### 硬件配置

* 电脑: 主流电脑配置即可，内存尽量大，主频尽可能高

+ 如果有条件的话，电脑安装虚拟机装linux系统

* 手机: 安卓手机

+ 如果有条件上谷歌的亲儿子(nexus或者pixel)，国产的手机推荐红米9A(经济实惠，缺点就是cpu是arm 32的，未来无法调试arm64的程序，入门足够了)

* 暂时没有真机可以先用模拟器一段时间

+ 夜神模拟器(最新支持Android 9)、雷电模拟器、逍遥模拟器
+ 但尽量还是使用真机，安卓模拟器存在兼容性的问题，有些app无法在模拟器上运行，因为模拟器是基于x86的架构，而有些app只认v7或者v8架构的cpu。

## 二、 打造属于自己的anroid逆向环境

### 1. 开发环境(以windows平台为例)

* 开发系统可以是Win10、linux(kali)、mac

#### java 开发环境(学习Java，Android开发时候用)

##### JDK

* **JRE**，（ Java Runtime Envrionment ），Java 运行时环境。

+ 含JVM和运行必备的类库。
+ 电脑上想要运行java程序，就必须安装JRE。

* **JDK**，（ Java Development Kit ），Java开发工具。

+ 含**JRE** 和 开发必备的工具(编译工具javac.exe 和 运行工具java.exe)
+ 想要开发Java应用程序，就必须安装JDK。

> JDK下载地址： https://www.oracle.com/java/technologies/downloads/#jdk18-windows

* jdk-19\_windows-x64\_bin.exe 必须去安装 否则无法运行依赖Java环境的软件或者工具

  [![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/image7-1024x576.png "image7-1024x576.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/image7.png)
* 配置环境变量

+ **JAVA\_HOME**：jdk安装的目录
+ **CLASSPATH**：`.;%JAVA_HOME%\lib;%JAVA_HOME%\lib\tools.jar`(注意前面是有一个点的)
+ **path**：添加`%JAVA_HOME%\bin`

* 验证配置环境变量是否生效：打开cmd，输入`java --version`，`javac`

  [![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/image8-1024x576.png "image8-1024x576.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/image8.png)

##### IDAE

> 下载地址： https://www.jetbrains.com/idea/download/#section=windows
>
> [![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/image9-1024x576.png "image9-1024x576.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/image9.png)[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/image10-1024x576.png "image10-1024x576.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/image10.png)

#### Android开发环境(root、Android正向开发、编写Xposed插件的时候用)

##### Android Studio

###### 安装Android Studio

> 下载地址： https://developer.android.google.cn/studio/

* ==要安装Android studio首先要配置好jdk环境==

  [![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/image11-1024x576.png "image11-1024x576.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/image11.png)[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/image12-1024x576.png "image12-1024x576.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/image12.png)
* 安装Android studio的过程中会下载SDK[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/image13-1024x576.png "image13-1024x576.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/image13.png)

  [![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/image14-1024x576.png "image14-1024x576.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/image14.png)

###### 创建工程测试一下

* MininumSDK先保持默认，后续有需要可以手动修改`minSdkVersion`的字段

  [![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/image15-1024x576.png "image15-1024x576.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/image15.png)[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/image16-1024x576.png "image16-1024x576.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/image16.png)[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/image17-1024x576.png "image17-1024x576.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/image17.png)
* #坑/逆向/app逆向/AndroidStudio/模拟器 `HAXM`的插件只支持`Intel`的cpu，只有安装这个插件才可以运行Android Studio 自带的模拟器。该插件不支持`AMD`的cpu(AMD的cpu只能使用Genymotion模拟器，首先需要安装virtualBox虚拟机，然后再安装Genymotion模拟器，有需要请自行百度)。

  [![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/image18-1024x576.png "image18-1024x576.png")](https://secpulse...