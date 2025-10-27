---
title: 黑客假冒中国台湾税务局传播Winos 4.0恶意软件
url: https://www.freebuf.com/news/423120.html
source: FreeBuf网络安全行业门户
date: 2025-02-28
fetch_date: 2025-10-06T20:37:41.528843
---

# 黑客假冒中国台湾税务局传播Winos 4.0恶意软件

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

黑客假冒中国台湾税务局传播Winos 4.0恶意软件

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

黑客假冒中国台湾税务局传播Winos 4.0恶意软件

2025-02-27 17:28:31

所属地 上海

FortiGuard Labs发现针对中国台湾地区的钓鱼攻击，旨在传播Winos 4.0恶意软件。

Fortinet的FortiGuard Labs近日披露了一起针对中国台湾企业的新型恶意软件攻击活动的详细信息。研究人员在2025年1月发现了这一攻击活动，并在周四（2月27日）发布报告前与Hackread分享了这一发现。

该活动使用了高度先进的恶意软件框架，被称为Winos 4.0。攻击具有较高的严重性，采用了多阶段感染过程，最终目的是窃取敏感信息，以用于未来的恶意活动。

## 攻击手法：假冒税务局发送钓鱼邮件

进一步调查显示，该恶意软件专门针对Microsoft Windows平台展开攻击。攻击者精心设计了一封伪装成台湾国家税务局的钓鱼邮件，作为初始攻击媒介。该邮件谎称包含即将接受税务检查的公司名单，并要求收件人将信息转发给财务部门。邮件附件伪装成财政部的正式文件，实际包含一个用于下一攻击阶段的恶意DLL文件。

![](https://image.3001.net/images/20250228/1740679341281978_e6e9b5c002f64ab5803f7ac363f429f9.png!small)欺骗性PDF文件（来源：Fortinet）

攻击通过一系列可执行文件和动态链接库（DLL）文件展开。ZIP文件中包含按顺序执行的文件：20250109.exe、ApowerREC.exe以及lastbld2Base.dll。

研究人员在博客中解释道：“20250109.exe最初是一个启动器，用于执行./app/ProgramFiles中的实际ApowerREC.exe。攻击者在ZIP文件中创建了相同的文件夹结构，并使用加载器替换了ApowerREC.exe。假冒的ApowerREC.exe仅调用从lastbld2Base.dll导入的函数。”

该DLL解密并执行包含配置数据（如命令与控制（C2）服务器地址）的shellcode。shellcode进一步实现了可选功能，包括权限提升、反沙箱技术（例如，通过多次截图检测用户活动，若未检测到用户交互则延迟执行）以及隐藏进程窗口。恶意软件从C2服务器下载加密的shellcode和核心Winos 4.0模块，这些数据存储于系统注册表中，以备后续解密和执行。

![](https://image.3001.net/images/20250228/1740679342048875_b9b7f1898f60487097e51a0a9063406c.png!small)攻击流程（来源：Fortinet）

## 恶意软件功能：持久化与用户监控

该模块启动多个恶意任务，例如建立持久化、绕过用户账户控制（UAC）、收集系统信息（包括计算机名称、操作系统版本及已安装的杀毒软件）以及禁用受感染系统上的屏保和节能功能。

此外，该恶意软件还主动监控和操作用户活动，包括捕获截图、记录键盘输入和剪贴板内容（甚至记录连接的USB设备的插入和移除日志），并根据预定义规则修改剪贴板数据。它还可以禁用安全软件的网络连接。观察到的其他攻击链涉及Python脚本和进一步的shellcode注入技术，这些变化展示了Winos 4.0框架的灵活性和适应性。

## 防范措施：警惕钓鱼邮件与增强防护

要防范像Winos 4.0这类复杂的恶意软件，需要高度警惕未经请求的邮件，尤其是带有附件或链接的邮件，避免打开邮件附带的压缩文件（如ZIP、RAR），因为它们通常用于传播恶意软件。同时，启用实时扫描功能，可以在威胁感染系统之前进行检测和拦截。

### **专家观点**

“这次攻击遵循了经典的钓鱼模式，但在利用可信机构引发反应方面增添了一些趣味，”SlashNext的现场首席技术官J. Stephen Kowski解释道。“威胁行为者巧妙地利用了人类心理，通过制造紧迫感和好奇心，使收件人更有可能下载恶意内容。”

**参考来源：**

> [Hackers Impersonate Taiwan’s Tax Authority to Deploy Winos 4.0 Malware](https://hackread.com/hackers-impersonate-taiwans-tax-authority-winos-4-0-malware/)

# 终端安全 # 企业安全

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

攻击手法：假冒税务局发送钓鱼邮件

恶意软件功能：持久化与用户监控

防范措施：警惕钓鱼邮件与增强防护

* 专家观点

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