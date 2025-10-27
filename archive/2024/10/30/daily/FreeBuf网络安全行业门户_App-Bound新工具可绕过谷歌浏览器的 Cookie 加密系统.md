---
title: App-Bound新工具可绕过谷歌浏览器的 Cookie 加密系统
url: https://www.freebuf.com/news/413901.html
source: FreeBuf网络安全行业门户
date: 2024-10-30
fetch_date: 2025-10-06T18:52:04.402381
---

# App-Bound新工具可绕过谷歌浏览器的 Cookie 加密系统

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

App-Bound新工具可绕过谷歌浏览器的 Cookie 加密系统

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

App-Bound新工具可绕过谷歌浏览器的 Cookie 加密系统

2024-10-29 09:53:33

所属地 上海

![1730166710_67203fb6ee20f5913e941.png!small](https://image.3001.net/images/20241029/1730166710_67203fb6ee20f5913e941.png!small)

最近，网络安全研究员亚历山大-哈根纳（Alexander Hagenah） 发布了一款工具，该工具名为 “Chrome-App-Bound-Encryption-Decryption ”， 可以绕过谷歌新的应用程序绑定加密 cookie 防护系统，并从 Chrome 浏览器中提取已保存的凭据。

虽然该工具实现了多个信息窃取者已经在其恶意软件中添加的功能，但它的公开可用性提高了继续在浏览器中存储敏感数据的 Chrome 浏览器用户的风险。

## 谷歌的应用程序绑定加密问题

谷歌在 7 月份推出了应用程序绑定（App-Bound）加密技术（Chrome 127），作为一种新的保护机制，它使用具有系统权限的 Windows 服务对 cookies 进行加密。

其目的是保护敏感信息免受信息窃取恶意软件的攻击，因为恶意软件以登录用户的权限运行，如果不首先获得 SYSTEM 权限，就无法解密窃取的 Cookie，从而可能引起安全软件的警报。

谷歌在 7 月份解释说：由于 App-Bound 服务以系统权限运行，攻击者需要做的不仅仅是诱骗用户运行恶意应用程序。

现在，恶意软件必须获得系统权限，或者向 Chrome 浏览器注入代码，而这是合法软件不应该做的事情。

然而，到了 9 月份，多名信息窃取者找到了绕过新安全功能的方法，并为他们的网络犯罪客户提供了再次从谷歌 Chrome 浏览器中窃取和解密敏感信息的能力。

谷歌当时告诉《BleepingComputer》，信息窃取开发者与谷歌工程师之间的 “猫捉老鼠 ”游戏一直在预料之中，他们从不认为自己的防御机制会刀枪不入。

相反，随着 App-Bound 加密技术的推出，他们希望最终能为逐步建立更完善的系统奠定基础。以下是谷歌当时的回应：

> “正如我们在博客中所说，我们预计这种保护措施将导致攻击者的行为转向更易观察的技术，如注入或内存刮擦。这与我们看到的新行为相吻合。
>
> 我们将继续与操作系统和反病毒软件厂商合作，尝试更可靠地检测这些新型攻击，并不断改进加固防御措施，为用户提供更好的信息窃取保护。- 谷歌发言人

## 旁路工具现已公开

昨天，Hagenah 在 GitHub 上公开了他的 App-Bound 加密旁路工具，并分享了源代码，允许任何人学习和编译该工具。

该工具使用 Chrome 浏览器内部基于 COM 的 IElevator 服务，对存储在 Chrome 浏览器本地状态文件中的 App-Bound 加密密钥进行解密。

该工具提供了一种检索和解密这些密钥的方法，Chrome 浏览器通过 App-Bound Encryption (ABE) 对这些密钥进行保护，以防止未经授权访问 cookie 等安全数据（将来还有可能访问密码和支付信息）。

![1730166778_67203ffac3aee6c9c49ed.png!small](https://image.3001.net/images/20241029/1730166778_67203ffac3aee6c9c49ed.png!small)

要使用该工具，用户必须将可执行文件复制到通常位于 C:\Program Files\Google\Chrome\Application 下的 Google Chrome 目录中。该文件夹受保护，因此用户必须首先获得管理员权限才能将可执行文件复制到该文件夹。

不过，这通常很容易实现，因为许多 Windows 用户，尤其是消费者，都使用具有管理权限的账户。

就其对 Chrome 浏览器安全性的实际影响而言，研究人员 g0njxa 告诉 BleepingComputer，Hagenah 的工具展示了一种基本方法，现在大多数信息窃取者已经超越了这种方法，可以从所有版本的谷歌 Chrome 浏览器中窃取 cookies。

eSentire恶意软件分析师Russian Panda也向BleepingComputer证实，Hagenah的方法看起来与谷歌首次在Chrome浏览器中实施App-Bound加密时，信息窃取者所采取的早期绕过方法类似。

Russian Panda 表示，Lumma使用的就是这种方法：通过COM实例化Chrome IElevator接口，访问Chrome的提升服务来解密cookie，但这种方法很容易被发现。

Russian Panda 称他们现在使用间接解密，而不直接与 Chrome 浏览器的提升服务交互。不过，g0njxa 评论说，谷歌仍然没有跟上，因此使用新工具可以轻易窃取存储在 Chrome 浏览器中的用户秘密。

针对该工具的发布，谷歌与 BleepingComputer 分享了以下声明：

这段代码（xaitax 的代码）需要管理员权限，这表明我们已经成功提升了成功实施此类攻击所需的访问量。虽然确实需要管理员权限，但这似乎并没有影响恶意软件的信息窃取行动，在过去六个月里，恶意软件的数量只增不减，它们通过零日漏洞、GitHub 问题的虚假修复，甚至 StackOverflow 上的答案来锁定用户。

> 参考来源：<https://www.bleepingcomputer.com/news/security/new-tool-bypasses-google-chromes-new-cookie-encryption-system/>

# 谷歌浏览器 # 谷歌 Chrome

本文为 独立观点，未经授权禁止转载。
如需授权、对文章有疑问或需删除稿件，请联系 FreeBuf
客服小蜜蜂（微信：freebee1024）

被以下专辑收录，发现更多精彩内容

+ 收入我的专辑

+ 加入我的收藏

展开更多

相关推荐

![]()

关 注

* 0 文章数
* 0 关注者

文章目录

谷歌的应用程序绑定加密问题

旁路工具现已公开

![](/images/logo_b.png)

本站由阿里云 提供计算与安全服务

### 用户服务

* [有奖投稿](https://www.freebuf.com/write)
* [提交漏洞](https://www.vulbox.com/bounties/detail-72)
* [参与众测](https://www.vulbox.com/projects/list)
* [商城](https://shop.freebuf.com)

### 企业服务

* [安全咨询](https://company.freebuf.com)
* [产业全景图](https://www.freebuf.com/news/307349.html)
* [企业SRC](https://www.vulbox.com/service/src)
* [安全众测](https://www.vulbox.com/)

### 合作信息

* [斗象官网](https://www.tophant.com/)
* [广告投放](https://www.freebuf.com/articles/444331.html)
* [联系我们](https://www.freebuf.com/articles/444332.html)

### 关于我们

* [关于我们](https://www.freebuf.com/news/others/864.html)
* 微信公众号
* [新浪微博](http://weibo.com/freebuf)

### 战略伙伴

* [![](https://image.3001.net/images/20191017/1571306518_5da83c1686dd9.png)](http://www.aliyun.com/?freebuf)

### FreeBuf知识大陆

![](https://image.3001.net/images/20250703/1751535036_68664dbcae34ac40bb9e7.png)

扫码把安全装进口袋

* [斗象科技](https://www.tophant.com/)
* [FreeBuf](https://www.freebuf.com)
* [漏洞盒子](https://www.vulbox.com/)
* [斗象智能安全](https://ai.tophant.com/)
* [免责条款](https://www.freebuf.com/dis)
* [协议条款](https://my.freebuf.com/AgreeProtocol/duty)

Copyright © 2025 WWW.FREEBUF.COM All Rights Reserved
[沪ICP备2024099014号](https://beian.miit.gov.cn/#/Integrated/index) | [沪公安网备
![](https://image.3001.net/images/20200106/1578291342_5e12d08ec2379.png)](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=31011502009321)