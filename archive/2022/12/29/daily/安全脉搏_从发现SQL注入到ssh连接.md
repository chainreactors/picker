---
title: 从发现SQL注入到ssh连接
url: https://www.secpulse.com/archives/194173.html
source: 安全脉搏
date: 2022-12-29
fetch_date: 2025-10-04T02:38:47.324447
---

# 从发现SQL注入到ssh连接

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

# 从发现SQL注入到ssh连接

[漏洞](https://www.secpulse.com/archives/category/vul)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2022-12-28

7,967

**声明：本文仅限于技术讨论与分享，严禁用于非法途径。若读者因此作出任何危害网络安全行为后果自负，与本号及原作者无关。**

**前言：**

某天，同事扔了一个教育站点过来，里面的url看起来像有sql注入。正好最近手痒痒，就直接开始。

#### 一、发现时间盲注和源码

后面发现他发的url是不存在SQL注入的，但是我在其他地方发现了SQL盲注。然后改站点本身也可以下载试用源代码，和该站点是同一套系统：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194173-1672211762.jpeg "null")

一开始的思路是直接用时间盲注写马，然后遇到的问题就是如何获取站点的绝对路径。通过sqlmap自带的字典去爆破，发现都失效了。（但是其实只是没写成功，不代表路径是不对。）那么接下来的思路就在源码上了。从源码里面没有找到啥可以直接未授权getshell的点。后面在本地搭建这套系统时，发现了其配置信息都在网站目录下的configure.php，后面就是尝试使用sqlmap读取文件。通过猜测，发现了站点的路径为/var/www/html/{站点域名}下面。然后再回头尝试写马，还是失败。但是可以读取文件。然后写了个脚本去跑，成功获取数据库账号密码：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194173-1672211763.jpeg "null")

Nmap一试，3306开放，心中窃喜。使用mysql连接的时候，发现root登录被做了限制，只能使用localhost进行登录。然后也通过sqlmap获取到其他账号，有的可以登录，但是都因为权限小，无法写马。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194173-1672211763.png "null")

#### 二、惊现上传漏洞

写马失败后，想着查询下数据库里面的管理员密码，登录后台看看有没有可利用的点。后面又回过头来看源码了。一边放着dump数据，一边又发现了新东西，这站点存在ckfinder和ckeditor编辑器，但是一个无法访问，一个无法上传木马。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194173-1672211764.jpeg "null")

就在我想破脑袋也没想到还有啥办法之时，我同事那边来了个好消息。他从旁站获取到了测试账号密码：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194173-1672211765.jpeg "null")

然后他在个人资料处发现了一些功能点，发现了一堆xss和csrf、会话固定后，最后测了一下上传点

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194173-1672211765.png "null")

这个上传点如果你直接上传php是可以上传成功的，但是路径找不到。很奇怪。

不过如果你先上传一个jpg文件，就会发现图片路径为upload/fileimages/ew00000000040/user\_photoa009.jpg

然后再通过bp修改文件扩展名为php，重新上传，就可以成功在前端看到php的路径：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194173-1672211766.jpeg "null")

通过抓包分析，我们发现他存在一个http\_user字段可控，并且只在前端校验文件类型得到重命名组合为user\_photo[http\_user][传入的文件后缀(.php)]

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194173-1672211767.jpeg "null")

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194173-1672211768.jpeg "null")

直接写入phpinfo()，发现解析了，上蚁剑：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194173-1672211769.jpeg "null")

成功getshell。

#### 三、脏牛提权

虽然成功获取权限，但是这权限很低，有执行权限，但是很多操作都被限制。前面有获取数据库账号密码，在获取webshell后，可直接连接mysql数据库：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194173-1672211770.jpeg "null")

这时候可以考虑udf提权，但是尝试发现没有/usr/lib64/mysql/plugin/路径的上传权限。那么久只能通过常规的提权了。使用工具linux-exploit-suggester：https://github.com/mzet-/linux-exploit-suggester

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194173-1672211771.jpeg "null")

发现很多种方式可以提权，但是我用kali编译完的程序上传到目标机上，发现运行不了。后面直接在目标机编译，也出现确实一些库文件，好像因为目标机版本太低了。后面参考了这篇文章，成功进行提权。

https://www.jianshu.com/p/df72d1ee1e3e

Exp：https://github.com/FireFart/dirtycow

#### 四、SSH连接

这个提权会删除root用户，新建一个用户firefart。本来还在考虑使用内网穿透把22端口代理出来，然后直接ssh连接。但是渗透步骤不规范就会导致我这样的结果：他的ssh并不是22端口，而是999端口。我信息收集的时候没有发现到位。当时一开始看没有22端口，所以才顺势觉得要穿透进去。但是其实人家999端口就是ssh。接下来就是成功使用ssh连接。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194173-1672211772.png "null")

但是有个问题又出现了：如果我想连接ssh，那么久只能使用这个账户登录，因为我不知道root密码。但是这样的话，人家登录不了root就会发现异常。但是如果我把root恢复了，我就没有root权限了。

诶，后面我在想，如果我把原始的passwd文件恢复，然后不断开ssh连接是不是我还能有权限操作呢？说干就干，使用firefart执行`mv /tmp/passwd.bak /etc/passwd`恢复原本的账户。然后ssh不断开，我发现我还是root权限。这就好办了。useradd新建账号edu，然后把新建的账户加入管理员组。具体操作可以参考：https://blog.csdn.net/llm\_hao/article/details/118031154

使用新账号edu进行登录，发现为root权限，成功！

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194173-1672211772.jpeg "null")

这时候才把原本firefart账号的窗口关闭。重新再使用firefart账户登录，发现已经无法登录了。看来这应该是系统的一种机制吧，哈哈哈。

**结尾**

这次渗透其实走了很多弯路，到最后都没用上数据库。很多时候一个点打不进去的时候，适当的放弃，去打新的点，不要太头铁，特别是攻防的时候。

总结一下：发现盲注，源码到跑取站点账号密码（时间盲注效率低到我现在还没跑出后台管理账户密码），无果。到从旁站上传木马，获取网站服务器权限，权限较低，使用脏牛提权，到后面的恢复原本的账户，并新建一个管理员。其实这个站点是还有内网在，貌似是教育局办公内网，但目前还在尝试，后续会随缘更新。

**本文作者：[蚁景网安实验室](newpage/author?author_id=37244)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/194173.html**](https://www.secpulse.com/archives/194173.html)

Tags: [SQL注入](https://www.secpulse.com/archives/tag/SQL%E6%B3%A8%E5%85%A5)、[SSH连接](https://www.secpulse.com/archives/tag/ssh%E8%BF%9E%E6%8E%A5)、[漏洞](https://www.secpulse.com/archives/tag/%E6%BC%8F%E6%B4%9E)、[盲注](https://www.secpulse.com/archives/tag/%E7%9B%B2%E6%B3%A8)、[脏牛提权](https://www.secpulse.com/archives/tag/%E8%84%8F%E7%89%9B%E6%8F%90%E6%9D%83)

点赞：
0
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
* [![从2023蓝帽杯0解题heapSpary入门堆喷](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/08/1693450185258-300x157.png)

  从2023蓝帽杯0解题heapSpary…](https://www.secpulse.com/archives/203218.html "详细阅读 从2023蓝帽杯0解题heapSpary入门堆喷")

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
| --- | --- ...