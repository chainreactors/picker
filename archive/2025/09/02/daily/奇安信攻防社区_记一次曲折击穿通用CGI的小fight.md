---
title: 记一次曲折击穿通用CGI的小fight
url: https://forum.butian.net/share/4523
source: 奇安信攻防社区
date: 2025-09-02
fetch_date: 2025-10-02T19:30:31.012177
---

# 记一次曲折击穿通用CGI的小fight

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
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### 记一次曲折击穿通用CGI的小fight

by AugustTheodor & 千堆雪与长街
文章太长了，有稍微的删改。

和朋友一起看的，respect~
![](https://mmbiz.qlogo.cn/mmbiz\_png/LN229gZh2CAEauTTl3uyTdod3IjrdxL8JoY4sQVKDliaiaATAIxcocxMr9hMbtzmNUicNQyyCwzrxUJ5ZS96f9HOA/0?wx\_fmt=png&from=appmsg "null")
1 小发现
-----
无聊的下午和无聊的保老师对着无聊的资产列表随便打了打。由于登录包is encrypted，顺理成章的打开控制台。
一开始吸引我的是这个抽象中带着马脚的前端script：
![](https://mmbiz.qlogo.cn/mmbiz\_png/LN229gZh2CAEauTTl3uyTdod3IjrdxL8eClWMm2OianNMBEZF0wsCoPGiaaRAkHb9uIl8kplAvAMX9V59FRqrAjA/0?wx\_fmt=png&from=appmsg "null")
可真是要混淆有混淆要安全有混淆呐，该给安全的都给了，该不给程序员的都不给了。
既然有打包器源码，要做的第一步自然也是把扒个API小扫一扫。扒API的时候注意到，这居然是个CGI应用（AKA玩二进制的）。
![](https://mmbiz.qlogo.cn/mmbiz\_png/LN229gZh2CAEauTTl3uyTdod3IjrdxL8hFwcmAPJslm0v8xXHsaKveJIHpDrAtibnicEHJF044ia6VdZu6F4PKL9A/0?wx\_fmt=png&from=appmsg "null")
这有意思啊，必须拿下~于是小测一波API，也是发现了个未授权任意文件读取：
![](https://mmbiz.qlogo.cn/mmbiz\_png/LN229gZh2CAEauTTl3uyTdod3IjrdxL8KibYO3vjpnBUracFgq4QuqBPfnsSptjKtQxFdJmo5uCImwFk8suFGow/0?wx\_fmt=png&from=appmsg "null")
2 意料之中的困难
---------
### 2.1 系统，但是阉割版
这个系统毋庸置疑是个linux。但小试了一下很多文件不存在，比如.bash\\_history，比如www，比如cmdline。所以一开始我以为是docker或者k8s，但由于苯人linux和虚拟容器方面学得极其不过关，只能找朋友帮忙看看。
朋友上来一波操作，感觉不太对劲，docker和k8s容器的目录也不存在，我俩一合计这可能是个一体机之类的硬件小玩意，基本上啥都访问不了。
比如cpuinfo是空这一块：
![](https://mmbiz.qlogo.cn/mmbiz\_png/LN229gZh2CAEauTTl3uyTdod3IjrdxL8GG6ibepSUzTiagrP1Dstu3bR7zMlibzo1OCdcaUZas17yb8Af4Ruu6MpA/0?wx\_fmt=png&from=appmsg "null")
比如工控这一块：
![](https://mmbiz.qlogo.cn/mmbiz\_png/LN229gZh2CAEauTTl3uyTdod3IjrdxL8GmJMPQjXdg6mSxEdzIania5IEHzafSrtmPm1vniaCbX2X3LgLNo5KrmA/0?wx\_fmt=png&from=appmsg "null")
![](https://mmbiz.qlogo.cn/mmbiz\_png/LN229gZh2CAEauTTl3uyTdod3IjrdxL8zWWIB4ufBLzsm4AF4bYsu3g9lOSUvGvgW9d9hTU6icsheWQRsJibt30A/0?wx\_fmt=png&from=appmsg "null")
给我看傻了，这辈子第一次黑板子好吧。
但是有个良好的渗透习惯是黑盒出来之后找找测绘，毕竟又是CGI又是定制硬件系统，不是通用的可能性无限趋近于零：
![](https://mmbiz.qlogo.cn/mmbiz\_png/LN229gZh2CAEauTTl3uyTdod3IjrdxL8c81OhcOwmed0ZpLUktj42YoHG5nmlTplpVEGlTOUB3rUtjoITYlQOQ/0?wx\_fmt=png&from=appmsg "null")
那么就衍生出了一个额外的选择：横向。
### 2.2 外网横向也是横向
横向过程略，总之也是找到了个幸运儿：
![](https://mmbiz.qlogo.cn/mmbiz\_png/LN229gZh2CAEauTTl3uyTdod3IjrdxL8rPia1na7JFknLMeHPX7vAqtbsiclO7Y8gF5PRGMLKtyYj9yOH6THEAyg/0?wx\_fmt=png&from=appmsg "null")
之后也是直接send系统to朋友，先找bash\\_history再爆破cmdline。遗憾的是cmdline还是啥都没有，幸运的是这次总算有了个丰盛的历史记录：
![](https://mmbiz.qlogo.cn/mmbiz\_png/LN229gZh2CAEauTTl3uyTdod3IjrdxL8RMDteqdUMC649z6RhmAVMWN9FN3WM9wCAXVcOpNFicuBPB7ibGzkos2Q/0?wx\_fmt=png&from=appmsg "null")
根据history，总算也是找到了网站路径，在/home/\\*\\*\\*/下。
3 摸象术
-----
### 3.1 摸一摸配置和日志
继续利用bash\\_history里出现的文件进行猜测，朋友找到了requestlog和几个conf文件。
先看requestlog，这个log不同于往常的日志文件，大多数路径并不显示，应该是自定义过。
![](https://mmbiz.qlogo.cn/mmbiz\_png/LN229gZh2CAEauTTl3uyTdod3IjrdxL8ia3cG5aUvCBaZofTAaSHKIPJOpZBKjDCNiaoicwxvTeZ83p9Y7tJEe8Ww/0?wx\_fmt=png&from=appmsg "null")
里面有一个疑似上传接口的东西，但是并不能真的上传东西，这一点其实让我挺疑惑的，后续会再次提到。
然后再看这些conf文件，其余略过，倒是有一个conf文件比较特别：
![](https://mmbiz.qlogo.cn/mmbiz\_png/LN229gZh2CAEauTTl3uyTdod3IjrdxL8KFMckccx9f2RYVlxiccOA21dhlFCfjOYuQMI6FfIXWaEMFLXrvR29jQ/0?wx\_fmt=png&from=appmsg "null")
看上去是个用户配置文件，里面居然出现了密码字样，格式还有些奇怪，难道用户密码是在配置文件里存储的？
其实真有可能，首先这种情况我已经见过不止一次了。而且小系统没有为了几个用户设置数据库的必要（sqlite是有可能的，但这里没有）。
但看上去，密码并不是明文，不过也无所谓，忽略红色的Null先把能读取的部分丢一圈cmd5，和枪兵爱好者非常符合的运气自然是让我得到了一个大大的未找到：
![](https://mmbiz.qlogo.cn/mmbiz\_png/LN229gZh2CAEauTTl3uyTdod3IjrdxL8rqxmts8ALBrzLGZeTjBJCsQNJ9NfiaBhTaZLicMyfhAQBpkDwT1D0iaKA/0?wx\_fmt=png&from=appmsg "null")
但是话又说回来，有很小的概率下登录包里使用的密码就是MD5。这里小小抓下登陆请求包：
![](https://mmbiz.qlogo.cn/mmbiz\_png/LN229gZh2CAEauTTl3uyTdod3IjrdxL8pnzq788MibQUxxZQEQUeyibSlTAAdOe9vuJIYdPVIjqMQsic2PBlAJc7w/0?wx\_fmt=png&from=appmsg "null")
看来是加密，下个断点还原一下：
![](https://mmbiz.qlogo.cn/mmbiz\_png/LN229gZh2CAEauTTl3uyTdod3IjrdxL8mLOkqsbmc5U4AU7DrqK2A1KA3hacBm9ZzvjpU7g8LFprBcDiaDpLHeQ/0?wx\_fmt=png&from=appmsg "null")
这里居然用的是md5，看来也是天助我也，下断改个值直接登陆：
![](https://mmbiz.qlogo.cn/mmbiz\_png/LN229gZh2CAEauTTl3uyTdod3IjrdxL8YDKeXZwpc6PKAMj3Qhft0OIR7ozjV6ykjA73yT0tEEMPbAjsiaz4Pvg/0?wx\_fmt=png&from=appmsg "null")
进入系统，也算是拿下一个里程碑^ ^。
### 3.2 上天入地
好消息：进后台了；坏消息：进的并非目标后台。
本来说进了后台，也算是个不错的洞了。但是拿不到目标的权限我总觉得难受。但由于找不到目标系统的web路径，读不到配置文件也进不去——我们下一步的目标就变成了读目标系统的web路径。
最后以构造response报错的情况找到了系统路径，真的是运气好：
![](https://mmbiz.qlogo.cn/mmbiz\_png/LN229gZh2CAEauTTl3uyTdod3IjrdxL8gGCIaCltibPzfxHLwBOjyETunIciacyN9HfCtNITQtVrCzZh4JUtlxlw/0?wx\_fmt=png&from=appmsg "null")
那么直接一顿依葫芦画瓢，也是成功进入目标系统。
4 突破总在意料之外
----------
过了几天，还是放不下这个系统，总觉得还能更进一步。于是又开始看代码。首先，把之前bash\\_history中出现的fcgi文件下下来看看源码。
### 4.1 IDA实在不是我的强项
真不喜欢二进制，看得我都快脑浆溢出了。由于之前没逆向过fcgi程序，这次完全是硬着头皮硬上。
进入入口，简单的初始化，读了下文件，没发现啥有用的东西：
![](https://mmbiz.qlogo.cn/mmbiz\_png/LN229gZh2CAEauTTl3uyTdod3IjrdxL8a6BOT2l1pyCyCY7wckZkXOWQLaN8JqT0nlLO0EHS6zXWFbKEN3qnJg/0?wx\_fmt=png&from=appmsg "null")
继续往下走，这里是一开始看见的任意文件下载点，由于见过这个包，刚好用它作为分析程序运行方式的样板：
![](https://mmbiz.qlogo.cn/mmbiz\_png/LN229gZh2CAEauTTl3uyTdod3IjrdxL8yy6CjH5MmG5RaHloZvDmXLErmE6CucyW3KEefW3NL4rEnfI0pZl8hg/0?wx\_fmt=png&from=appmsg "null")
可以看到是直接拼接了两个参数，然后在三个参数都不为空的时候进入sub\\_441040，直接读取返回文件。
看完这个sub我大概已经明白这个FCGI文件的运行原理了。于是开启快速搜索模式，找找fopen（文件上传）和system（命令执行）的引用：
![](https://mmbiz.qlogo.cn/mmbiz\_png/LN229gZh2CAEauTTl3uyTdod3IjrdxL8BBcCqwdqyGEKCqd16w9599SNEr1jcTwu96nt43MdEnC4PwXrtyHN5A/0?wx\_fmt=png&from=appmsg "null")
后面就是一堆烦人的看代码时间，略。总而言之fopen（a/a+）和system里找不到啥可利用的点，好悬没给我气死，算了算了- -。
溢出不看，下班！
![](https://mmbiz.qlogo.cn/mmbiz\_png/LN229gZh2CAEauTTl3uyTdod3IjrdxL8icWSGicoRdkSKnglcAXqLBSt9Yz5g9oiagpb67BM2kJKnhLib6eyMh3f1w/0?wx\_fmt=png&from=appmsg "null")
### 4.2 但是横向可以
又横了几个系统，终于在一个系统里找到了个额外的功能：
![](https://mmbiz.qlogo.cn/mmbiz\_png/LN229gZh2CAEauTTl3uyTdod3IjrdxL8nVv6ERvmiaiaLnppLQCtHicARBkKVC6CkjFxD3BBnBSPJEic2l8CogPyzA/0?wx\_fmt=png&from=appmsg "null")
网络调试好啊，网络调试可是RCE多发地段~
这里直接切换到后端看看包：
![](https://mmbiz.qlogo.cn/mmbiz\_png/LN229gZh2CAEauTTl3uyTdod3IjrdxL8mvqA2ojeKXwBYWCOznCdu4sWRuQIcRX5WoNmKLibEPjkkBl2HTMyibzQ/0?wx\_fmt=png&from=appmsg "null")
一个handle一个arguments，对应的自然是命令和参数。先试试handle部分：
![](https://mmbiz.qlogo.cn/mmbiz\_png/LN229gZh2CAEauTTl3uyTdod3IjrdxL8SA6X0QVW4xUNU95yOOHYRMNTL9MlicNCj5yTdaGk233Qnyyic1jGejng/0?wx\_fmt=png&from=appmsg "null")
看来是不能改？那就从arguments这里出手。arguments内容很明显是经过一定编码或者加密的，由于这个站好像是不同的版本，虽然系统跟目标结构差不多但前台的js这次是真加密没有包了，秉承着能不看代码就不看代码的懒人原则，打开Cyberchef简单试一下常见的编码。
![](https://mmbiz.qlogo.cn/mmbiz\_png/LN229gZh2CAEauTTl3uyTdod3IjrdxL8PxoRRGpLUHgzYFoLib8CaiaX4EK9u1HXE3ibPVCw93piajDRHoBTSKrmMg/0?wx\_fmt=png&from=appmsg "null")
HEX，ez~直接改包发送，参数为`| whoami`：
![](https://mmbiz.qlogo.cn/mmbiz\_png/LN229gZh2CAEauTTl3uyTdod3IjrdxL8ZqWpEzg5zibWbjhyKw8iarN8L0hiap2rmicPrtaR2qHt4vQaEWlQxhqmwQ/0?wx\_fmt=png&from=appmsg "null")
shell~

* 发表于 2025-09-01 10:06:14
* 阅读 ( 1992 )
* 分类：[漏洞分析](https://forum.butian.net/community/Vul_analysis)

1 推荐
 收藏

## 0 条评论

请先 [登录](https://forum.butian.net/login) 后评论

[![阿斯特](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/b99df3b5f15d200a029ce5360cf8966dca8278b.jpg)](https://forum.butian.net/people/13618)

[阿斯特](https://forum.butian.net/people/13618)

公众号：重生之成为赛博女保安

11 篇文章

[奇安信攻防社区](https://forum.butian.net)|
联系我们

|
[sitemap](https://forum.butian.net/sitemap)

Copyright © 2013-2023 BUTIAN.NET 版权所有 [京ICP备18014330号-2](https://beian.miit.gov.cn/#/Integrated/index)

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

#### ![阿斯特](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/b99df3b5f15d200a029ce5360cf8966dca8278b.jp...