---
title: 新一代RedTeam启发式内网扫描工具
url: https://www.secpulse.com/archives/202616.html
source: 安全脉搏
date: 2023-07-06
fetch_date: 2025-10-04T11:52:38.248532
---

# 新一代RedTeam启发式内网扫描工具

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

# 新一代RedTeam启发式内网扫描工具

[工具](https://www.secpulse.com/archives/category/tools)

[hackctf](https://www.secpulse.com/newpage/author?author_id=34005)

2023-07-05

25,085

#### **0x01 免责声明**

本工具旨在提供安全评估和漏洞扫描等相关服务，但使用本工具时请注意以下事项：

* 本工具的使用者应对其使用产生的结果和后果负全部责任。本工具仅作为辅助工具提供，不对使用者所进行的操作和决策承担责任。
* 本工具尽力提供准确、及时的信息和评估，但无法保证其完全无误。使用者应自行判断和验证本工具提供的信息，并对使用本工具所产生的结果进行独立评估。

请在使用本工具之前仔细阅读并理解上述免责声明。使用本工具即表示您同意遵守上述条款，并自行承担相应责任。

## **0x02 工具优势**

* 所有模块皆采用生产者消费者模型,即生即消.

> 在端口扫描一组数据后将数据发送到队列中,由爆破模块和指纹模块即刻进行消费,随时结束扫描进程拿到扫描结果.摆脱传统的等待端口扫描结束进行后续的模型.

* 所有模块皆采用启发式扫描,诣在最少的发包探测目标

> 在端口扫描时,通过协议识别的方式识别TOP15协议,对其协议进行探测.漏洞探测是通过对WEB指纹进行识别后进行探测.摆脱传统的端口绑定以及漏洞探测发包量大的问题.

* 强大的WEB指纹支撑

> 感谢棱角社区对本工具WEB指纹的支撑、目前指纹900+,指纹识别快人一步.

* 极致的应用并发

> 在爆破模块以及漏洞探测、指纹识别、端口扫描所有模块采用数据原子化的方式进行极致的并发.

## **0x03 参数说明**

##

* ```
  ❯ ./App-arm64darwin-noupx
   _____                    _       _|_   _|                  | |     | |  | | ___ _ __ ___  _ __ | | __ _| |_ ___  | |/ _ \ '_'  _ \| '_ \| |/ _' | __/ _ \  | |  __/ | | | | | |_) | | (_| | ||  __/  \_/\___|_| |_| |_| .__/|_|\__,_|\__\___|                   | |  by 1n7erface                   |_|[=] Load Success Usage of ./App-arm64darwin-noupx:  -bt int      BruteModule threadNum (default 200)  -c string      auto check 192 or 172 or 10  -e  print error log  -i string      IP address of the host you want to scan,for example: 192.168.11.11-255 or 192.168.1.1/24 or /22 /15...  -it int      InfoModule threadNum (default 200)  -nobrute      skip brute  -noping      skip icmp alive  -nopoc      skip poc  -onping      only ping  -p string      custom port example: 80,8088,1-3000  -pw string      Define a password dictionary for blasting  -t int      Timeout (default 4)  -us string      Define a user dictionary for blasting[=] end......
  ```

* bt参数说明

  > 此参数期望接收一个数值类型,用于爆破模块开启的协程数量,默认的数量为200
* c参数说明

> 此参数期望接收一个字符串，存在于"192、172、10"三个字符串之间,程序会自动的探测网段存活，并对其进行扫描。包括192的192.168.0.1-192.168.255.255、172的172.16.0.1-172.31.255.255、10的10.0.0.1-10.255.255.255.值得一提的是,网段探测存活的算法是从每一个c段选择1,255 以及期间的随机3个ip进行检测,如果一个存活将判定为网段存活.在一定几率下存在漏段的可能无法避免.(10段不建议使用,网段太大可能产生预期之外的错误).

* e参数说明

> 此参数不接收任何值,打印期间的错误日志,用于排查扫描的问题.

* i参数说明

> 此参数接收一个字符串,字符串用于声明要扫描的网段,例如192.168.11.11-255 or 192.168.1.1/24 or /22 /15... ,此参数支持CIDR的表达式.

* it参数说明

> 此参数期望接收一个数值类型,用于信息探测模块开启的协程数量,例如ip存活、端口扫描、web指纹.

* nobrute参数说明

> 此参数不接收任何值,不对信息探测的结果进行暴力破解模块.

* noping参数说明

> 此参数不接收任何值,在目标网段不支持ICMP协议时,通过TCP进行探测.

* nopoc参数说明

> 此参数不接收任何值,不对探测的WEB服务进行漏洞探测的模块。

* onping参数说明

> 此参数不接收任何值,对目标网段只进行ICMP的ip存活探测,其余一律不做.

* p参数说明

> 此参数接收一个字符串,指定端口扫描的端口.例如,80,8088,1-3000 (注:此参数一经指定则不进行程序自带端口的扫描)

* pw参数说明

> 此参数接收一个字符串,指定爆破的密码字典,例如 -pw ffnxjfl123,fgmgergn334 （注:此参数一经指定则不进行程序自带密码的扫描)

* t参数说明

> 此参数期望接收一个数值类型,用于在漏洞扫描,WEB识别时的超时时间设置.

* us参数说明

> 此参数期望接收一个字符串,指定爆破的用户名字典,例如 -us fwefwf,fwefwf (注:此参数一经指定则不进行程序自带用户名的扫描)

* 如果想指定端口、爆破的用户名和密码并且仍然使用程序自带的端口、密码、用户名进行扫描.可以在当前程序的同级目录上传名为"config.json"的文件

> 内容为: {"pass":["ffnxjfl123","fgmgergn334"],"user":["fwefwf","fwefwf"],"ports":[9999,8888]}

## **0x04 使用截图**

**![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-202616-1688545924.png)**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-202616-1688545926.png)

##

## **0x05 Template工具获取**

下载地址1：

链接：https://pan.quark.cn/s/8b2a2462b5b9

项目地址：

https://github.com/1n7erface/Template

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-202616-1688545928.jpeg)

**本文作者：[hackctf](newpage/author?author_id=34005)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/202616.html**](https://www.secpulse.com/archives/202616.html)

Tags: [参数](https://www.secpulse.com/archives/tag/%E5%8F%82%E6%95%B0)、[工具](https://www.secpulse.com/archives/tag/%E5%B7%A5%E5%85%B7)、[应用](https://www.secpulse.com/archives/tag/%E5%BA%94%E7%94%A8)、[指纹识别](https://www.secpulse.com/archives/tag/%E6%8C%87%E7%BA%B9%E8%AF%86%E5%88%AB)、[模块](https://www.secpulse.com/archives/tag/%E6%A8%A1%E5%9D%97)、[漏洞](https://www.secpulse.com/archives/tag/%E6%BC%8F%E6%B4%9E)、[端口](https://www.secpulse.com/archives/tag/%E7%AB%AF%E5%8F%A3)

点赞：
5
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![代码审计 | 同源策略的绕过](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/09/a799223d33bd92e8b0620d8ad38ecd2.jpg)

  代码审计 | 同源策略的绕过](https://www.secpulse.com/archives/203439.html "详细阅读 代码审计 | 同源策略的绕过")
* [![云原生安全联防联抗策略玩转微隔离](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/09/1694157547520-300x155.png)

  云原生安全联防联抗策略玩转微隔离](https://www.secpulse.com/archives/203414.html "详细阅读 云原生安全联防联抗策略玩转微隔离")
* [![内网信息搜集神器—searchall](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/08/1693463314861-300x167.png)

  内网信息搜集神器—searc…](https://www.secpulse.com/archives/203203.html "详细阅读 内网信息搜集神器—searchall")

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
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2020/06/04/6bfc834beda6e9debb9f6b48a215b4bc-290x290.jpeg)](https://www.secpulse.com/newpage/author?author_id=34005aaa) | [hackctf](https://www.secpulse.com/newpage/author?author_id=34005) | |
| 文章数：40 | 积分： 80 |
| 微信公众号：hackctf | |

* [![阿波罗主机安全管理](/wp-content/themes/secpulse2017/img/product-agent.png)](https://linkage.duoyinsu.com)
* [![伏特漏洞扫描云平台](/wp-content/themes/secpulse2017/img/product-fute.png)](https://v.duoyinsu.com)

### 安全问答社区

![安全问答社区](https://www.secpulse.com/wp-content/themes/secpulse2017/img/xcx.png)

### 脉搏官方公众号

![脉搏公众号](https://www.secpulse.com/wp-content/themes/secpulse2017/img/SecPulse.png)

### 活动日程

[显示更多](https://www.secpulse.com/newpage/activity)

#### 2022-06-17

[Gdevops 全球敏捷运维峰会](h...