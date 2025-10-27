---
title: 针对PLC的恶意软件发布，黑客或可发起远程震网式攻击
url: https://www.freebuf.com/news/393495.html
source: FreeBuf网络安全行业门户
date: 2024-03-07
fetch_date: 2025-10-06T17:09:16.858280
---

# 针对PLC的恶意软件发布，黑客或可发起远程震网式攻击

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

针对PLC的恶意软件发布，黑客或可发起远程震网式攻击

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

针对PLC的恶意软件发布，黑客或可发起远程震网式攻击

2024-03-06 15:47:01

所属地 上海

还记得2010年的“震网攻击事件”吗？以色列黑客通过将“震网（Stuxnet）病毒”植入核设施中，轻松破坏了伊朗准备了许久的核能研究实验。![](https://image.3001.net/images/20240306/1709711202_65e81f627d3532990a6d8.jpg!small)

Stuxnet是首个针对工业控制系统的蠕虫病毒，利用西门子公司控制系统（SIMATIC WinCC/Step7）存在的漏洞感染数据采集与监控系统（SCADA），能向可编程逻辑控制器（PLC）写入代码并将代码隐藏，极大地延缓了伊朗核电站的上线。

近日，来自佐治亚理工学院（GT）的安全研究人员发布了一篇论文，详细介绍了他们发现的一款****针对PLC的恶意软件****，黑客借此对工业控制系统（ICS）发起类似****远程震网式攻击****。

在传统的PLC的时代，攻击者可以针对控制逻辑层或固件层。固件攻击可以提供高级别的设备控制，并且难以被发现，但难点在于恶意软件难以部署。而控制逻辑层部署恶意软件更容易，但也更容易被发现。最关键的是，这两种方式都要求攻击者拥有对目标组织的工业网络的特权访问权限。

在现代PLC时代，PLC通常包含了网络服务器，它们可以远程配置、控制，以及通过专用API和人机界面（HMI）的常规网络浏览器进行监控。尽管这些现代PLC可以为组织带来许多好处，但佐治亚理工学院的安全研究人员警告说，它们也可以显著扩大ICS的攻击面。

为了证明这些风险，研究人员复现了一款基于网络的PLC恶意软件，该恶意软件隐藏在控制器的内存中。由于ICS环境中配备浏览器的设备在客户端执行，因此恶意软件可以滥用PLC的合法网络API来干扰工业过程或对机械设备造成损害。

这种新的PLC恶意软件易于部署且难以检测。最初的感染可以通过物理或网络访问目标的HMI来完成，但恶意软件也可以通过利用跨源漏洞直接通过互联网劫持HMI来部署。为了确保持久性，这种新型PLC恶意软件利允许JavaScript代码深入浏览器缓存并独立于安装它的网页执行。此外，即便文件已经从服务器上删除，它们也将继续运行长达24小时。通过这种方法，恶意软件可以在固件更新、新的HMI以及硬件更换后仍然存活。

可以预见，恶意软件一旦部署成功，其能力取决于所使用的合法的API能力，这就给攻击者更多的想象空间。例如它们可以被利用来直接覆盖输入/输出值，滥用HMI输入，更改设定点和安全设置，伪造HMI显示，更新管理员设置，甚至用于实时数据外泄。

更关键的是，研究人员还发现即使目标PLC处于隔离的网络中，恶意软件也可以建立命令和控制（C&C）连接。一旦攻击者完成了攻击，该恶意软件还可以通过自我销毁、良性载荷覆盖、注销账户信息，甚至是恢复出厂设置来掩盖其痕迹。

研究人员确定这种类型的PLC恶意软件可以用于西门子、艾默生、施耐德电气、三菱电机和艾伦·布拉德利PLC。而针对这些控制器的攻击涉及利用新发现或已知的漏洞，在某些情况下需要FTP密码、不安全的协议或内部人员进行攻击。

专家们已经创建了一个与供应商无关的框架，可以用来构建和分析基于网络的PLC恶意软件，并表示“这个框架探索了广泛适用策略的每个阶段，这些策略可以用于大多数现代PLC模型，并且呈现了恶意前端代码如何系统地破坏PLC的网络属性，颠覆工业控制系统环境的完整性。未来，该框架可以作为任何PLC供应商和模型研究中的参考案例。”

> 参考来源：https://www.securityweek.com/remote-stuxnet-style-attack-possible-with-web-based-plc-malware-researchers/

# 渗透测试 # 系统安全 # 数据安全

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