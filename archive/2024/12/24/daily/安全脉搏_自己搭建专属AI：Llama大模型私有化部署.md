---
title: 自己搭建专属AI：Llama大模型私有化部署
url: https://www.secpulse.com/archives/205740.html
source: 安全脉搏
date: 2024-12-24
fetch_date: 2025-10-06T19:35:03.474833
---

# 自己搭建专属AI：Llama大模型私有化部署

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

# 自己搭建专属AI：Llama大模型私有化部署

[工具](https://www.secpulse.com/archives/category/tools)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2024-12-23

12,233

## 前言

AI新时代，提高了生产力且能帮助用户快速解答问题，现在用的比较多的是Openai、Claude，为了保证个人隐私数据，所以尝试本地（Mac M3）搭建Llama模型进行沟通。

## Gpt4all

安装比较简单，根据 <https://github.com/nomic-ai/gpt4all> 下载客户端软件即可，打开是这样的：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202412191643684.jpg)

然后选择并下载模型文件，这里以Llama为例：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202412191643685.jpg)

下载模型文件完，选择模型文件则可以进行对话了：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202412191643686.jpg)

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202412191643687.jpg)

也可以利用基于 nomic-embed-text嵌入模型，把文档转成向量方便语义检索和匹配。选择文档所在的目录：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202412191643688.jpg)

然后对话中选择对应的文档即可：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202412191643689.jpg)

如果文件太大，需要在设置适当添加token大小，太大也不好，处理会慢且机器会卡死：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202412191643690.jpg)

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202412191643691.jpg)

gpt4all使用起来还是比较方便的，但是有几个缺点：有些能在huggingface.co搜到的模型在gpt4all上面搜不到、退出应用后聊天记录会消失。

## Ollama

安装也很方便，下载 <https://ollama.com/download/Ollama-darwin.zip> ，然后运行如下命令即可启动Llama：

```
ollama run llama3.2
```

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202412191643692.jpg)

为了方便图形化使用，可以借助 <https://github.com/open-webui/open-webui> 完整图形化的使用，启动也很简单，直接使用官方仓库中的命令即可：

```
docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
```

然后访问本地的3000端口即可：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202412191643693.jpg)

open-webui的原理也比较简单，Ollama启动后会在本地监听11434端口，open-webui也是利用这个端口来和Ollama通信完成的图形化使用。open-webui还可以多选模型一起回答：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202412191643694.jpg)

整体测试下来，发现Llama3.2对于文档分析差点意思，给他提供一个pdf文档，也看不出个啥来。但是上面的gpt4all，然后通过nomic-embed-text模型嵌入后好点。

## 总结

本文演示了通过不同手段来运行Llama模型，来达到本地使用LLM的目的。

**本文作者：[蚁景网安实验室](newpage/author?author_id=37244)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/205740.html**](https://www.secpulse.com/archives/205740.html)

点赞：
0
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![pocsuite3安全工具源码分析](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202502171711874.png)

  pocsuite3安全工具源码分析](https://www.secpulse.com/archives/205913.html "详细阅读 pocsuite3安全工具源码分析")
* [![内网信息搜集神器—searchall](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/08/1693463314861-210x140.png)

  内网信息搜集神器—searc](https://www.secpulse.com/archives/203203.html "详细阅读 内网信息搜集神器—searchall")
* [![新一代RedTeam启发式内网扫描工具](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/07/1688546246784-210x140.png)

  新一代RedTeam启发式内网扫描工具](https://www.secpulse.com/archives/202616.html "详细阅读 新一代RedTeam启发式内网扫描工具")

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
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2024/12/logo-white.png)](https://www.secpulse.com/newpage/author?author_id=37244aaa) | [蚁景网安实验室 ![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)](https://www.secpulse.com/newpage/author?author_id=37244) | |
| 文章数：402 | 积分： 877 |
| 蚁景网安实验室（www.yijinglab.com）网络安全靶场练习平台，涉及CTF赛前指导、职业技能训练、网安专项技能提升等。 | |

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
* [Sec-Wiki](https://www.sec-wiki....