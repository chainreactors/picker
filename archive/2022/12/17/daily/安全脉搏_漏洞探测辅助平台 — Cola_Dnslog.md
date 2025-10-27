---
title: 漏洞探测辅助平台 — Cola_Dnslog
url: https://www.secpulse.com/archives/193752.html
source: 安全脉搏
date: 2022-12-17
fetch_date: 2025-10-04T01:44:10.596537
---

# 漏洞探测辅助平台 — Cola_Dnslog

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

# 漏洞探测辅助平台 — Cola\_Dnslog

[工具](https://www.secpulse.com/archives/category/tools)

[Lemon](https://www.secpulse.com/newpage/author?author_id=5109)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng3.png)

2022-12-16

15,302

一、工具介绍

Cola Dnslog v1.2.1 更加强大的dnslog平台/无回显漏洞探测辅助平台，

完全开源 dnslog httplog ldaplog rmilog 支持dns http ldap rmi等协议 提供API调用方式便于与其他工具结合 支持钉钉机器人、Bark等提醒 后续更新docker一键部署 后端完全使用python实现

可帮助检测漏洞：

```
log4j2 fastjson ruoyi Spring RCE Blind SQL Bland XXE
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193752-1671176332.png)

二、安装与使用

1、下载源码

```
git clone https://github.com/Abelche/cola_dnslog.git
```

我习惯于将服务用tmux放到后台运行

2、启动webserver

安装python（python>=3.7）依赖

注意，需要用python3.7及以上版本，否则会有兼容性问题，多python推荐使用conda

```
cd cola_dnslog
pip install -r requirements.txt
```

修改根目录下的config.yaml

主要需要修改DNS\_DOMAIN NS1\_DOMAIN NS2\_DOMAIN SERVER\_IP

可选: 修改HTTP\_RESPONSE\_SERVER\_VERSION伪造http返回中Server字段

```
global:  DB_FILENAME: sqlite.db

logserver:  DNS_DOMAIN: example.com  NS1_DOMAIN: ns1.example.com  NS2_DOMAIN: ns2.example.com  SERVER_IP: 1.1.1.1  DNS_PORT: 53  HTTP_HOST: 0.0.0.0  HTTP_PORT: 80  HTTP_RESPONSE_SERVER_VERSION: nginx  LDAP_HOST: 0.0.0.0  LDAP_PORT: 1389  RMI_HOST: 0.0.0.0  RMI_PORT: 1099

webserver:  HOST: 0.0.0.0  PORT: 28001  PASSWORD_SALT: 随便一长串字符串，如：cuau89j2iifdas8
```

启动webserber端和logserver端，注意这里一定要先启动webserver端（因为要先通过webserver端初始化数据库，初始化之后会在终端输出账号、密码、token、logid等信息。

```
chmod +x start_webserver
./start_webserver
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193752-1671176333.png)

3、启动logserver

```
chmod +x start_logserver
./start_logserver
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193752-16711763331.png)

4、启动前端

现在来到前端（不一定要和webserver放在一起，你甚至可以通过electron打包成本地客户端），先修改配置文件.env.production

```
cd src/app/front
vim .env.production
```

```
# just a flag
ENV = 'production'
# base api
VUE_APP_BASE_API = 'http://1.1.1.1:28001'
TARGET_API = 'http://1.1.1.1:28001'
```

然后npm安装依赖、打包、启动http服务（这里可以随意选择http服务器，为了方便我直接用python启动）

```
cd src/frontnpm installnpm run build:prod
cd distpython3 -m http.server 18001
```

至此，三端（webserver端、logserver端、webui前端）已经全部开启！

这时，访问http://1.1.1.1:18001应该可以看到登录页面！

三、下载地址：

项目地址：https://github.com/AbelChe/cola\_dnslog

**侵权请私聊公众号删文**

**本文作者：[Lemon](newpage/author?author_id=5109)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/193752.html**](https://www.secpulse.com/archives/193752.html)

Tags: [Cola\_Dnslog](https://www.secpulse.com/archives/tag/cola_dnslog)、[漏洞探测辅助平台](https://www.secpulse.com/archives/tag/%E6%BC%8F%E6%B4%9E%E6%8E%A2%E6%B5%8B%E8%BE%85%E5%8A%A9%E5%B9%B3%E5%8F%B0)

点赞：
2
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![pocsuite3安全工具源码分析](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202502171711874.png)

  pocsuite3安全工具源码分析](https://www.secpulse.com/archives/205913.html "详细阅读 pocsuite3安全工具源码分析")
* [![自己搭建专属AI：Llama大模型私有化部署](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2024/12/images.png)

  自己搭建专属AI：Llama大模型私有化](https://www.secpulse.com/archives/205740.html "详细阅读 自己搭建专属AI：Llama大模型私有化部署")
* [![内网信息搜集神器—searchall](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/08/1693463314861-210x140.png)

  内网信息搜集神器—searc](https://www.secpulse.com/archives/203203.html "详细阅读 内网信息搜集神器—searchall")

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
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/f43a6447ea66cf84915afd0ca2631f09.png)](https://www.secpulse.com/newpage/author?author_id=5109aaa) | [Lemon ![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng3.png)](https://www.secpulse.com/newpage/author?author_id=5109) | |
| 文章数：68 | 积分： 647 |
|  | |

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

[看雪.安恒 2020 KCTF 春季赛](https://ctf....