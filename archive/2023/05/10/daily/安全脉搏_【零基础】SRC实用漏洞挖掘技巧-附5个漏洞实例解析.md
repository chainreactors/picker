---
title: 【零基础】SRC实用漏洞挖掘技巧-附5个漏洞实例解析
url: https://www.secpulse.com/archives/200077.html
source: 安全脉搏
date: 2023-05-10
fetch_date: 2025-10-04T11:37:43.272163
---

# 【零基础】SRC实用漏洞挖掘技巧-附5个漏洞实例解析

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

# 【零基础】SRC实用漏洞挖掘技巧-附5个漏洞实例解析

[漏洞](https://www.secpulse.com/archives/category/vul)

[公众号:安全女巫](https://www.secpulse.com/newpage/author?author_id=49672)

2023-05-09

16,913

********如果你喜欢我的文章，欢迎关注公众号：安全女巫
转载请注明出处：********https://mp.weixin.qq.com/s/-ebZn79irVCoSDBHL7iW1g

该篇文章针对SRC渗透测试过程中的技巧进行罗列与简要分析，旨在帮助大家快速开展工作。

渗透测试工作是个精细的工作，在什么功能场景之下易发哪些漏洞，若有这样的对照表，势必会加固安全防线。全文先进行整体梳理，后进行逐一解说，文末简要实例介绍，通俗易懂。

## 0x01 整体梳理

1.信息收集

ICP备案查询子域名-https://beian.miit.gov.cn/#/Integrated/recordQuery

whois数据信息收集-https://whois.chinaz.com/

子域名查询-https://chaziyu.com、https://site.ip138.com/xxx.com/domain.htm

2.平台功能

用户登录-弱密码、URL重定向、IP绕过

用户退出-CSRF退出、URL跳转

用户注册-短信/邮箱轰炸

找回密码-短信/邮箱轰炸、批量获取用户名对应昵称、批量获取已注册用户

信息搜索-XSS、SQL注入、CSRF

编辑-XSS、SQL注入、CSRF、文件上传、越权

删除-XSS、SQL注入、CSRF、越权

投票-并发、CSRF、修改响应包、（只允许投票5次，前端验证。但后端可通过接口直接投票）

充值-金额为负数

订单-并发突破下单次数、CSRF、越权

接口-并发、无限制、前端限制不可点击，接口可直接访问、修改响应包

验证码-重复使用、无效（未验证）、可爆破、无验证码

评论-XSS、SQL注入、CSRF、并发、越权

签到-XSS、SQL注入、CSRF、并发、csrf、越权

3.平台本身

敏感信息-Dirsearch、Webpack、URLFinder、FindSomething、Burp-clj、Swagger-exp

数据安全-敏感信息明文传输、敏感信息明文展示在平台、敏感信息明文存储数据库

域名解析-Host碰撞

## 0x02 信息收集

### 1.通过SSL证书查询

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200077-1683602930.png)

根据证书所有者查询使用者相关域名，IP信息。

### 2.ICP备案查询子域名

网站https://beian.miit.gov.cn/#/Integrated/recordQuery查询域名所属的主办单位名称：xxxxx有限公司

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200077-1683602931.png)

由主办单位名称：xxxxx有限公司继续反查子域名

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200077-1683602932.png)

点击详情子域名汇总：

xxx.com

xxx.cn

通过网络空间安全搜索引擎云悉资产、FOFA、Virustotal、Dnsdumpster、Threatcrow

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200077-1683602933.png)

### 3.whois数据信息收集

https://whois.chinaz.com/使用历史查询，查询出邮箱信息

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200077-1683602934.png)

邮箱反查查询出所绑定的域名信息

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200077-1683602935.png)

### 4.子域名查询

https://chaziyu.com/

https://site.ip138.com/xx.com/domain.htm

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200077-1683602937.png)

经确认与汇总去重得到xxx个子域名

## 0x02 平台功能

### 1.用户登录

弱密码：密码强度不够，易猜解。若是未限制错误次数，验证码无效的情况下可暴力破解进行登录

URL重定向：登录成功后一般自动跳转到其他页面。URL地址为：xxx.com?redirect=a\_url，通过更改a\_url的值可跳转任意页面

IP绕过：限制同一IP单位时间内的访问次数，可通过请求头加上x-forwarded-for:x.x.x.x\*绕过限制校验失败次数

### 2.用户退出

CSRF退出：退出功能未校验referer、Origin、csrftoken导致可csrf退出登录。若是发布在留言功能处易csrf退出

URL跳转：退出链接一般自动跳转至登录页面，此处若更改为任意url可用于恶意推广、钓鱼等

### 3.用户注册

短信/邮箱轰炸：短信/邮件发送接口可使用并发漏洞，无限制发送短信/邮件给接收人带来干扰，也使用付费接口加重企业次数消耗

SQL注入：用户名处拼接sql语句，在个人资料处展示或其他位置展示昵称处可查询出期望的内容

### 4.找回密码

短信/邮箱轰炸：短信/邮件发送接口可使用并发漏洞，无限制发送短信/邮件给接收人带来干扰，也使用付费接口加重企业次数消耗

批量获取手机号对应昵称：接口用于验证手机号对应的昵称以确认是否存在，若不限制查询次数可通过该接口泄露用户信息

### 5.搜索

XSS：用户可在搜索框搜索关键字并提交查询，未对输入进行过滤和转义，导致攻击者将恶意语句注入到搜索框中，可获取用户cookie

SQL注入：用户搜索' OR '1'='1，将原始查询语句闭合' OR '1'='1',可进行删除修改等恶意操作

### 6.编辑

XSS：触发点一般在列表展示页面，点击或加载触发。url链接：javascript:alert(1)，图片加载：

SQL注入：一般在编辑页面编辑，触发点在列表展示页面展示（拼接后期望获得的内容）

CSRF：未添加referer、origin、token可诱导已登录用户点击，执行期望的编辑内容

文件上传：未限制上传文件类型、文件内容未过滤、文件名未进行重命名等，导致上传木马等

越权：可编辑更高权限接口、越权更改他人编辑页面

### 7.删除

XSS：触发点一般在删除接口，访问时触发。url链接：<a href="/delete?id=<script>alert('XSS');</script>">删除</a>

SQL注入：通过提交 ID 号码来删除指定记录，url链接：?delete\_id=1; DROP TABLE users; *--*

CSRF：未添加referer、origin、token可诱导已登录用户点击，执行期望的删除操作

越权：可直接调用管理员接口进行删除，可删除其他用户的平行权限

### 8.投票

并发：使用burp插件Turbo Intruder进行并发操作，可突破每人每日投票次数限制，无限制投票

CSRF：构造csrf请求，可诱导对方点击后投票

修改响应包：使用burp-拦截请求-拦截执行-此请求的响应修改响应包可绕过限制成功发包

### 9.充值

金额为负数：修改充值接口中金额为负数，不花钱反而可提现金额增多

金额绕过最低限制：修改接口中数值，绕过前端限制最低金额

### 10.订单

并发突破下单次数：使用burp插件Turbo Intruder进行并发操作，一次付款下多次订单

CSRF：构造csrf请求，可诱导对方点击后下订单

越权：通过更改订单id可查看他人订单详情或取消订单

### 11.接口

并发：使用burp插件Turbo Intruder进行并发操作

无限制：短信/邮箱/身份证号验证等付费接口，无限制使用可致资源消耗

接口可直接访问：接口后端未校验，虽前端无按钮点击触发，仍可通过接口直接访问

修改响应包：抓取正常响应包内容，用于替代不满足条件时响应内容，再次发包，可修改响应包

### 12.验证码

重复使用：验证码验证后一次使用不作废，可重复使用

无效（未验证）：有验证码字段但未进行校验正确性，将之删除也可直接使用接口

可爆破：验证码位数较少爆破较为容易，且无过期时间，使用爆破手段可验证通过

无验证码：平台无验证码且未限制单个IP单位时间内访问次数，存在爆破风险

### 13.评论

XSS：一般在评论处进行评论，评论展示处加载/点击触发

SQL注入：测试时易插入多条数据易导致容易数据，建议在测试环境测试或者正式环境测试后删除。

CSRF：构造csrf请求，可诱导用户发表评论

并发：未限制单位时间内评论次数易造成无效评论占用资源、造成数据冗余、影响用户体验

越权：更改评论者id可代提他人成功留言

### 14.签到

并发：签到一般是一天只能签到一次，调用接口进行并发可一次签到多天，从而领取签到奖励

## 0x03 平台本身

### 1.敏感信息

#### 1》js中敏感信息-webpack

chrome浏览器F12-源代码查看webpack打包的前端源代码

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200077-16836029371.png)

#### 2》js中敏感信息-URLFinder

https:*//github.com/pingc0y/URLFinder*

针对网站逐一扫描E:toolsURLFinder-windows-amd64.exe -u http://xxxxxx.com -s 200 -m 2

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200077-1683602939.png)

逐一扫描url文本中url，使用进程50，将结果输出到js\_result文件夹。将E:toolsURLFinder-windows-amd64.exe -f url.txt -s 200 -m 2 -f url.txt -t 50 -o ./js\_result。注意扫描之前要自己创建空文件夹js\_result，此为文件夹内容

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200077-1683602940.png)

#### 3》html/js敏感信息-FindSomething

浏览器输入chrome://extensions/

将crx格式文件拖到浏览器，进行安装扩展

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200077-16836029401.png)

访问网站可见信息

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200077-1683602941.png)

#### 4》获取url和子域名以及后台网站越权访问敏感接口-burpsuite插件burp-clj

github地址：https://github.com/ntestoc3/burp-clj/releases/tag/v0.5.2

https://github.com/ntestoc3/burp-scripts下载并更新下面的脚本源，重新加载脚本

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200077-1683602944.png)

使用该插件记得把浏览器缓存清掉不然不会加载js...