---
title: 摄像头贴很有必要，黑客可不激活指示器而调用摄像头
url: https://www.freebuf.com/news/416480.html
source: FreeBuf网络安全行业门户
date: 2024-11-30
fetch_date: 2025-10-06T19:15:36.900137
---

# 摄像头贴很有必要，黑客可不激活指示器而调用摄像头

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

摄像头贴很有必要，黑客可不激活指示器而调用摄像头

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

摄像头贴很有必要，黑客可不激活指示器而调用摄像头

2024-11-29 10:22:37

所属地 上海

在你的笔记本电脑上贴上摄像头并不是一个愚蠢的想法。一位安全工程师发现，通过刷新联想ThinkPad X230笔记本电脑上的摄像头固件，可在摄像头本身激活的情况下独立控制其LED。换句话说，可以在摄像头指示器不亮的情况下，悄悄调用笔记本的摄像头。

![](https://image.3001.net/images/20241129/1732849151_67492dff76313f222646f.jpg!small)

Andrey Konovalov，一位以xairy为名在GitHub上的Linux内核安全工程师，发布了一个工具，可以在商务笔记本ThinkPad X230上获得对摄像头LED指示器的软件控制。虽然这款笔记本型号已经超过十年历史，但该代码在社区上引发了热烈讨论：为什么摄像头和指示器不是硬连接？

Andrey发现X230的摄像头是通过USB连接器连接，基于Ricoh R5U8710 USB摄像头控制器。这在当时并不是特例，其他品牌的笔记本电脑也有类似操作。这就留下了一个隐患，控制器可以独立启用或禁用LED。这一发现存在一个比较敏感的场景，当黑客悄悄调用了摄像头，但用户却无法发现，因为摄像头LED指示灯没有亮起来。

在实验中，xairy成功开发并刷新了自定义固件。为了实现这一点，工程师不得不转储并分析控制器的SROM（只读存储器）的十六进制代码，并在没有任何文档的情况下反汇编代码，以找到负责流式传输视频和启用LED引脚的位置。

Xairy展示了USB设备固件可以使用软件重写，然后由损坏的代码控制，并指出，“笔记本电脑的摄像头通常通过USB内部连接，许多USB设备的固件可以通过USB刷新。”他认为，许多摄像头的LED可以通过软件和固件的组合以类似的方式控制。

对此，联想表示，这是因为X230这类旧的、停产的系统没有包含固件更新的验证。自2019年以来，联想的图像处理器“已经包含了摄像头固件的数字签名检查，支持带有写保护的安全胶囊更新。”

## 许多人更倾向于物理开关

Cybernews的研究人员表示，类似的攻击可以绕过摄像头指示器LED，在过去已经发生过许多次。“这种类型的攻击的意义在于，它允许攻击者通过在受影响的笔记本型号上安装恶意软件，未被察觉地监视他们的受害者。虽然我更倾向于将摄像头指示器LED硬连接到摄像头启用/活动/电源信号，但并非所有内置摄像头都这样工作。”

Nazarovas指出，用于演示概念验证的联想X230笔记本已经超过10年历史（发布于2012年）。在那个时候，通过软件控制摄像头指示器LED的做法更普遍和被接受，因为这类攻击并不那么常见和已知。

与此同时，GitHub上该项目已经引起了很多关注。人们担心，演示的方法可能影响许多其他通过USB连接摄像头并允许刷新固件的笔记本电脑。用户强烈表示，LED指示器应该连接到摄像头的电源，或者是摄像头的“启用”信号，而不应该通过任何固件操作。LED还必须通过单次触发器（一个晶体管+一个电容器）连接，以便它至少亮起500毫秒，防止制作难以察觉的单次射击。

一些人认为，现代计算机有更强大的基于硬件的解决方案，以确保LED在摄像头使用时始终亮起。但也有许多人更倾向于设置摄像头物理硬件开关，以绕过任何基于软件的指示器。

参考来源：<https://cybernews.com/security/hackers-can-access-laptop-webcams-without-activating-the-led/>

# 漏洞 # 安全漏洞 # 漏洞利用

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

许多人更倾向于物理开关

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