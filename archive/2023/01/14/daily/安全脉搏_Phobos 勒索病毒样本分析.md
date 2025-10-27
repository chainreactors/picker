---
title: Phobos 勒索病毒样本分析
url: https://www.secpulse.com/archives/195053.html
source: 安全脉搏
date: 2023-01-14
fetch_date: 2025-10-04T03:49:59.312061
---

# Phobos 勒索病毒样本分析

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

# Phobos 勒索病毒样本分析

[Web安全](https://www.secpulse.com/archives/category/articles/web)

[ChaMd5安全团队](https://www.secpulse.com/newpage/author?author_id=3747)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2023-01-13

17,728

> > 招新小广告CTF组诚招re、crypto、pwn、misc、合约方向的师傅,长期招新IOT+Car+工控+样本分析多个组招人有意向的师傅请联系邮箱
> >
> > admin@chamd5.org(带上简历和想加入的小组)

Phobos勒索病毒在近年来的热度不断上升，感染率不断提升，该病毒执行后会加密各种文件，并以zip.id[number].[hudsonL@cock.li].Devos命名。

下面对该家族样本进行分析，主要分析该病毒特征和行为。

勒索信：

```
!!!All of your files are encrypted!!!
To decrypt them send e-mail to this address: hudsonL@cock.li.
If you have not received a response within 24 hours, write to us at Jabber: helprecovery@gnu.gr
```

勒索图片：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195053-1673589372.png)

勒索图片

### 一、CRC32进行校验

该样本开局使用CRC32算法检测样本完整性，该算法在病毒中多次使用。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195053-1673589374.png)

1.png

### 二、对样本进行提权操作

判断样本权限，若没有权限，则进行提权操作。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195053-1673589375.png)

提权

### 三、使用AES进行消息解密

使用AES对密钥进行解密后，根据节表进行读取。

节表一区间为0xC，依次为索引、偏移、长度。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195053-1673589376.png)

aes1

资源解密密钥如下：

```
00AAF128  87 8F 65 5E 1B 30 7D E2 97 4B 8C 35 E4 46 B5 01  ..e^.0}â.K.5äFµ.
00AAF138  00 00 00 00 38 F1 F2 75 00 28 E3 00 18 F6 0F 01  ....8ñòu.(ã..ö..
```

资源解密向量如下：

```
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
```

解密成功后部分：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195053-1673589379.png)

Untitled

### 四、网络通信

由于该样本未配置IP，故未产生网络连接

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195053-1673589382.png)

网络.png

### 五、持久化驻留

在下列目录中对勒索病毒进行拷贝留存

C:Users86173AppDataLocal

C:Users86173AppDataRoamingMicrosoftWindowsStart MenuProgramsStartup;

C:ProgramDataMicrosoftWindowsStart MenuProgramsStartup

注册表中设置开机自启动项

SoftwareMicrosoftWindowsCurrentVersionRun

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195053-1673589383.png)

持久化驻留

### 六、创建线程终止占据文件的进程

拍摄进程快照，依次判断进程是否有文件占用。

尝试终止进程，尽可能加密更多文件。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195053-1673589384.png)

terminal

### 七、对文件进行勒索加密

1、通过随机数生成密钥，包括获取进程pid、tid、获取运行时间，获取本地时间等

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195053-1673589385.png)

随机生成密钥

2、判断文件是否为空，若不为空，设置文件属性，根据文件大小加密文件。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195053-1673589386.png)

加密

总结：

样本通过采用CRC32校验+AES加解密进行制作勒索样本。

1. 进行CRC32校验
2. 判断是否提权，若未提权则进行提权的相关操作
3. AES解密相关消息，后面根据节表信息进行内容读取
4. 建立网络通信，发送连接请求
5. 持久化驻留，拷贝留存相关信息
6. 创建线程终止占据文件的进程
7. 随机创建加密密钥，对文件进行加密

由于使用作者公钥进行加密，故无私钥的情况下，AES暂时无法解密。

防范建议：

可以使用安装杀毒软件的方法进行防范。

该样本并未做太多对抗行为，特征明显，可以被传统杀软有效拦截。

C2：

33d32078ebe0c9429e405fdeb347dfb1ba5543e61d1179d13edffc7943b57640

**本文作者：[ChaMd5安全团队](newpage/author?author_id=3747)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/195053.html**](https://www.secpulse.com/archives/195053.html)

Tags: [AES](https://www.secpulse.com/archives/tag/aes)、[CRC32](https://www.secpulse.com/archives/tag/crc32)、[Phobos](https://www.secpulse.com/archives/tag/phobos)、[勒索病毒](https://www.secpulse.com/archives/tag/%E5%8B%92%E7%B4%A2%E7%97%85%E6%AF%92)、[持久化驻留](https://www.secpulse.com/archives/tag/%E6%8C%81%E4%B9%85%E5%8C%96%E9%A9%BB%E7%95%99)

点赞：
0
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![Tellyouthepass结合高危漏洞实施攻击：产品联动保护用户数据安全！](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/05/1684727919925-300x216.png)

  Tellyouthepass结合高危漏洞…](https://www.secpulse.com/archives/200779.html "详细阅读 Tellyouthepass结合高危漏洞实施攻击：产品联动保护用户数据安全！")
* [![【勒索防护】BabLock，游离于主流杀软之外的新型勒索病毒](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200456-1684221051-300x175.png)

  【勒索防护】BabLock，游离于主流杀…](https://www.secpulse.com/archives/200456.html "详细阅读 【勒索防护】BabLock，游离于主流杀软之外的新型勒索病毒")
* [![【勒索防护】MSI 等多个企业已遭受攻击！MoneyMessage 勒索软件突现](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199280-1681978319-300x158.png)

  【勒索防护】MSI 等多个企业已遭受攻击…](https://www.secpulse.com/archives/199280.html "详细阅读 【勒索防护】MSI 等多个企业已遭受攻击！MoneyMessage 勒索软件突现")

评论  (0)

昵称

必填
您当前尚未登录。
[登录？](https://www.secpulse.com/user_login "登录")
[注册](https://www.secpulse.com/user-register)

邮箱

必填（保密）

快来写下你的想法吧！

upload

|  |  |  |
| --- | --- | --- |
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2017/09/t01e080bff5276476f11.jpg)](https://www.secpulse.com/newpage/author?author_id=3747aaa) | [ChaMd5安全团队 ![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)](https://www.secpulse.com/newpage/author?author_id=3747) | |
| 文章数：85 | 积分： 181 |
| www.chamd5.org 专注解密MD5、Mysql5、SHA1等 | |

* [![阿波罗主机安全管理](/wp-content/themes/secpulse2017/img/product-agent.png)](https://linkage.duoyinsu.com)
* [![伏特漏洞扫描云平台](/wp-content/themes/secpulse2017/img/product-fute.png)](https://v.duoyinsu.com)

### 安全问答社区

![安全问答社区](https://www.secpulse.com/wp-content/themes/secpulse2017/img/xcx.png)

### 脉搏官方公众号

![脉搏公众号](https://www.secpulse.com/wp-content/themes/secpulse2017/img/SecPulse.png)

### 活动日程

[显示更多](https://www.secpulse.com/newpage/activity)

#### 2022-06-17

[Gdevops 全球敏捷运维峰会](https://www.bagevent.com/event/8022600?bag_track=AQMB)

#### 2022-05-12

[Mastering the Challenge！——来自The 3rd AutoCS 2022智能汽车信息安全大会的邀请函](https://autocs2022.artisan-event.com/)

#### 2021-11-18

[AutoSW 2021智...