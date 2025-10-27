---
title: 免杀！绕过EDR隐秘执行shellcode
url: https://www.secpulse.com/archives/200227.html
source: 安全脉搏
date: 2023-05-12
fetch_date: 2025-10-04T11:38:23.875579
---

# 免杀！绕过EDR隐秘执行shellcode

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

# 免杀！绕过EDR隐秘执行shellcode

[脉搏文库](https://www.secpulse.com/archives/category/category/secdocs)

[潇湘信安](https://www.secpulse.com/newpage/author?author_id=37983)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng3.png)

2023-05-11

13,262

|  |
| --- |
| **声明：**该公众号分享的安全工具和项目均来源于网络，仅供安全研究与学习之用，如用于其他用途，由使用者承担全部法律及连带责任，与工具作者和本公众号无关。 |

现在只对常读和星标的公众号才展示大图推送，建议大家把Hack分享吧“设为星标”，否则可能看不到了！

**工具介绍**

Freeze.rs 是一个有效载荷创建工具，用于绕过 EDR 安全控制以隐秘方式执行 shellcode。Freeze.rs 利用多种技术，不仅可以删除 Userland EDR 挂钩，还可以以绕过其他端点监控控件的方式执行 shellcode。

###

### **创建暂停进程**

创建进程时，Ntdll.dll 是第一个加载的 DLL；这发生在加载任何 EDR DLL 之前。这意味着在加载 EDR 并开始挂钩和修改系统 DLL 的程序集之前会有一点延迟。查看 Ntdll.dll 中的 Windows 系统调用，我们可以看到还没有任何东西被挂钩。

如果我们创建一个处于挂起状态（及时冻结的进程）的进程，我们可以看到除了 Ntdll.dll 之外没有其他 DLL 被加载。您还可以看到没有加载任何 EDR DLL，这意味着位于 Ntdll.dll 中的系统调用未被修改。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200227-1683791323.png)

**工具使用**

执行以下命令安装好rust环境，然后CS或MSF生成一个raw shellcode，最后用Freeze.rs进行免杀即可。

```
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200227-16837913231.png)

**免杀效果**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200227-1683791324.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200227-1683791326.png)

**下载地址**

**点击下方名片进入公众号（Hack分享吧）**

**回复关键字【****23****0508****】获取**下载链接****

**本文作者：[潇湘信安](newpage/author?author_id=37983)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/200227.html**](https://www.secpulse.com/archives/200227.html)

Tags: [dll](https://www.secpulse.com/archives/tag/dll)、[Freeze.rs](https://www.secpulse.com/archives/tag/freeze-rs)、[SHELLCODE](https://www.secpulse.com/archives/tag/shellcode)、[免杀](https://www.secpulse.com/archives/tag/%E5%85%8D%E6%9D%80)

点赞：
6
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![【高级威胁追踪(APT)】响尾蛇组织使用DLL劫持加载Cobalt Strike攻击巴基斯坦政府](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201630-1686282004-300x188.png)

  【高级威胁追踪(APT)】响尾蛇组织使用…](https://www.secpulse.com/archives/201630.html "详细阅读 【高级威胁追踪(APT)】响尾蛇组织使用DLL劫持加载Cobalt Strike攻击巴基斯坦政府")
* [![简单操作实现冰蝎jsp webshell 阿里云免杀](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/1671523633377-300x219.png)

  简单操作实现冰蝎jsp webshell…](https://www.secpulse.com/archives/193780.html "详细阅读 简单操作实现冰蝎jsp webshell 阿里云免杀")
* [![webshell免杀-从0改造你的AntSword](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/11/1669626892222-300x172.png)

  webshell免杀-从0改造你的Ant…](https://www.secpulse.com/archives/192415.html "详细阅读 webshell免杀-从0改造你的AntSword")

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
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2020/11/12/5abbd29a2ce13702d20784fb420161da-290x290.png)](https://www.secpulse.com/newpage/author?author_id=37983aaa) | [潇湘信安 ![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng3.png)](https://www.secpulse.com/newpage/author?author_id=37983) | |
| 文章数：57 | 积分： 15 |
| 关注微信公众号【潇湘信安】，一起学习网络安全知识！ | |

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

[AutoSW 2021智能汽车软件开发大会](https://autosw2021.artisan-event.com)

#### 2021-06-27

[2021中国国际网络安全博览会暨高峰论坛](http://www.sins-expo.com)

#### 2021-05-27

[The 2nd AutoCS 2021智能汽车信息安全大会](https://artisan-event.com/AutoCS2021/)

#### 2020-12-18

[贝壳找房2020 ICS安全技术峰会](https://www.4hou.com/tickets/bmZO)

#### 2020-12-11

[全球敏捷运维峰会（Gdevops2020）](https://www.bagevent.com/event/6243820?bag_track=AQMB)

#### 2020-12-04

[2020京麒网络安全大会](https://www.huodongxing.com/event/5569026023500)

#### 2020-11-29

[OPPO技术开放日第六期|聚焦应用与数据安全防护](https://mp.weixin.qq.com/s/kXt5PAD3bPcHUZjl6rziCw)

#### 2020-11-27

[EISS-2020企业信息安全峰会之上海站 11.27](https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx187be17d5a2961cf&redirect_uri=httpswww.bagevent.comevent6531722&response_type=code&scope=snsapi_userinfo&state=STATE#wechat_redirect)

#### 2020-09-24

[CSDI summit中国软件研发管理行业技术峰会](https://www.bagevent.com/event/csdisummit)

#### 2020-09-23

[2020中国国际智慧能源暨能源数据中心与网络信息安全装备展览会](http://www.energydataexpo.cn)

#### 2020-07-31

[EISS-2020企业信息安全峰会之北京站 | 7.31（周五线上）](http://www.anquanjia.net.cn/main/detail?postId=83)

#### 2020-04-15

[看雪.安恒 2020 KCTF 春季赛](https://ctf.pediy.com)

#### 2020-01-09

[相约本地生活安全沙龙暨白帽子颁奖典礼](https://www.bagevent.com/event/6241320)

### 安全问答社区

![安全问答社区](https://www.secpulse.com/wp-content/themes/secpulse2017/img/xcx.png)

### 脉搏官方公众号

![脉搏公众号](https://www.secpulse.com/wp-content/themes/secpulse2017/img/SecPulse.png)

### 友情链接

---

* [网络尖刀](http://www.ijiandao.com/)
* |
* [Sec-Wiki](https://www.sec-wiki.com/)
* |
* [独自等待](https://www.waitalone.cn/)
* |
* [中国红客联盟](https://www.ihonker.org/)
* |
* [娜迦信息](http://www.nagain.com/)
* |
* [SecSilo](https://www.secsilo.com/)
* |
* [易安在线](http://www.e365.org/)
* |
* [i春秋](https://www.ichunqiu.com)
* |
* [铁匠运维网](http://www.tiejia...