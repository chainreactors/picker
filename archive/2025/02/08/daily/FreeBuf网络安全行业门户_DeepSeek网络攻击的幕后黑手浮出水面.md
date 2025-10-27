---
title: DeepSeek网络攻击的幕后黑手浮出水面
url: https://www.freebuf.com/articles/neopoints/421203.html
source: FreeBuf网络安全行业门户
date: 2025-02-08
fetch_date: 2025-10-06T20:37:35.559297
---

# DeepSeek网络攻击的幕后黑手浮出水面

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

DeepSeek网络攻击的幕后黑手浮出水面

* ![]()
* 关注

* [其他](https://www.freebuf.com/articles/others-articles)

DeepSeek网络攻击的幕后黑手浮出水面

2025-02-07 14:13:54

所属地 上海

2025年开年，由国人研发的AI大模型DeepSeek火出天际。

尤其是自DeepSeek-R1发布，十余天内，在全球范围内快速掀起关注热潮，成为AI发展历史上的现象级事件之一。上至各国政要，下至十几亿普通用户，以及大量创投、AI和科技型公司，都在讨论、研究和热议DeepSeek。![](https://image.3001.net/images/20250207/1738908828_67a5a49c88442d71ac324.jpg!small)

但与此同时，DeepSeek也深陷网络攻击的风暴之中，遭遇了持续、大规模、高密度的恶意网络攻击，导致其服务时常处于中断状态，显示为“服务器繁忙，请稍后再试”，严重影响正常用户的使用体验。

针对DeepSeek 的攻击可以划分为两个阶段。在1月27日之前，网络攻击主要以NTP、SSDP、CLDAP等反射放大攻击，影响范围尚可控制。自1月27日开始，大量的HTTP代理攻击开始出现，以及专业的僵尸网络团伙集中火力，对DeepSeek的AI服务和数据发起了密集攻击。

![](https://image.3001.net/images/20250207/1738909504_67a5a740df34f54600d1c.png!small)

**具体事件时间线如下**

> 1月27日：DeepSeek宣布，由于基础设施遭受“大规模恶意攻击”，决定暂停新用户注册。
>
> 1月28日：网络安全公司Wiz.io报告称，发现一个与DeepSeek有关的ClickHouse数据库发生泄露。该数据库包含大量敏感用户数据，例如聊天记录和API密钥。
>
> 1月29日：《环球时报》披露，自1月初起，DeepSeek就一直在遭受定期的分布式拒绝服务（DDoS）攻击。这些攻击运用了反射放大技术，同时还伴有来自美国IP地址的HTTP代理攻击以及暴力破解尝试。
>
> 1月30日：XLab发布报告称，两种Mirai僵尸网络变体——“HailBot”和“RapperBot”是近期这波攻击的幕后黑手。这些僵尸网络利用16个命令与控制（C2）服务器以及100多个C2端口，发起了协同攻击。

## **DeepSeek网络攻击幕后黑手**

ANY.RUN也发布报告称，在后期针对DeepSeek的恶意攻击中，最为典型的就是两种Mirai僵尸网络变体——“HailBot”和“RapperBot”。由于这两大僵尸网络一直“接单”，因此可以认为此次攻击是有针对性目的，而非一次单纯的网络攻击行为。

### 1、HailBot

HailBot基于Mirai源码开发而来，其命名源自于运行后输出的字符串信息“hail china mainland”（中国大陆万岁），独特的表达方式很可能是栽赃陷害。HailBot的攻击平均每天攻击指令上千条、攻击上百个目标。攻击目标分布在中国、美国、英国、中国香港、德国等地区。

HailBot的攻击方式主要包括以下几种：

* 基于TCP和UDP协议的DDoS攻击：HailBot支持基于TCP和UDP协议的多种DDoS攻击方式，能够通过漏洞利用和弱口令扫描爆破进行传播。
* 漏洞利用：HailBot利用了CVE-2017-17215漏洞进行传播，尽管当前版本仅内置了这一种漏洞，但不排除未来可能增加更多漏洞利用模块。
* 弱口令扫描爆破：HailBot通过扫描23端口，利用弱口令进行爆破攻击，感染更多的设备加入其僵尸网络。
* 分布式拒绝服务（DDoS）攻击：HailBot通过控制大量被感染的设备，向目标服务器发起DDoS攻击，耗尽目标服务器的网络带宽和系统资源，使其无法正常服务。

有意思的是，HailBot的C&C基础设施5.181.80.120和5.181.80.115早期还曾传播过多个搭载CVE-2017-11882漏洞的诱饵文档，这些诱饵文档以“INVOICE.xlsx”，“Product\_requetslist.xlsx”，“CIF WMS REF NO 451RFQ ARN-DT-2021-06-29.xlsx”等作为文件名，诱导受害者打开文档以触发漏洞，从而下载执行Lokibot和Formbook在内的多款商业化窃密型银行木马。

### 2、RapperBot

RapperBot也是一款基于Mirai源代码二次开发的僵尸网络恶意软件，主要针对物联网（IoT）设备，自2022年6月以来一直保持活跃。它通过SSH暴力破解和Telnet默认口令探测进行传播，感染设备后，攻击者可以执行多种分布式拒绝服务（DDoS）攻击。

RapperBot的C&C协议进行了改良，采用双层异或加密和随机字节填充，增强了隐蔽性。通过控制大量被感染的设备，向目标服务器发起DDoS攻击，可能导致目标服务器的网络带宽和系统资源耗尽，无法正常服务

**传播方式**

* SSH暴力破解：RapperBot通过硬编码的SSH凭据列表或从C&C服务器下载凭据列表，对支持Diffie-Hellmann密钥交换的SSH服务进行暴力破解。
* Telnet默认口令探测：部分变种通过Telnet基于设备默认口令的方式进行探测，目标设备关键词、默认用户名称以及密码被硬编码在文件中。

**攻击方式**

* DDoS攻击：RapperBot支持多种DDoS攻击方式，包括TCP STOMP攻击、UDP泛洪攻击等，能够对非HTTP目标发起攻击。
* 持久化访问：成功入侵后，RapperBot会替换受害设备的~/.ssh/authorized\_keys文件，并创建一个名为“suhelper”的超级用户账户，以此确保对设备的持久访问。

## DeepSeek深陷风暴之中

除了针对性的网络攻击，DeepSeek同样也成了黑产眼中的“肥肉”，大量网络犯罪分子发布山寨版本传播恶意软件，或骗取用户的订阅费用。例如ESET就曾发现，/deepseek-6phm9gg3zoacooy.app-tools.info网站传播被标识为Win32/Packed.NSIS.A的恶意软件。由于该恶意软件经过数字签名，因此更具欺骗性，容易让毫无戒心的用户放松警惕。

ESET的研究人员指出，这些假冒网站通常会设置一个醒目的“立即下载”按钮，而真正的DeepSeek官网并不需要用户下载任何软件即可正常使用其服务。

![](https://image.3001.net/images/20250206/1738824043_67a4596b67c2c29f3a750.png!small)

除了假冒网站和恶意软件分发，网络犯罪分子还利用DeepSeek的知名度进行加密货币和投资领域的诈骗。一些不法分子在各种区块链网络上创建了虚假的DeepSeek加密货币代币。此外，还有一些骗子声称出售DeepSeek的IPO前股票，试图以此为幌子骗取投资者的资金。

事实上，这类黑产模式并不是首次出现，此前大量火爆的现象级产品都曾遭遇类似经历。基于此，DeepSeek发布官方声明，称目前，DeepSeek 仅在以下社交媒体平台拥有唯一官方账号：

* 微信公众号：DeepSeek
* 小红书：@DeepSeek（deepseek\_ai)
* X (Twitter) : DeepSeek (@deepseek\_ai)

除以上官方账号外，其他任何以 DeepSeek或相关负责人名义对外发布公司相关信息的，均为仿冒账号。

DeepSeek所遭遇的网络攻击，反映出需要在网络安全领域投入更多的资源。除上述外部攻击外，其模型的安全性与健壮性也有待提升。

基于云的网络安全、合规性和漏洞管理解决方案提供商Qualys对DeepSeek-R1 LLaMA 8B变体进行了安全分析，发现该模型在使用Qualys TotalAI（一个专为AI安全评估设计的平台）进行的安全测试中，表现不佳，未能通过大部分测试。

不少媒体也报道，DeepSeek比较容易遭受提示词干扰。思科研究团队使用自动越狱算法对DeepSeek R1、OpenAI的o1-preview和其他前沿模型进行了测试，应用了来自HarmBench数据集的50个提示。

结果令人震惊：DeepSeek R1的攻击成功率为100%，未能阻止任何一个有害提示，这与其它领先模型形成鲜明对比。

![image](https://image.3001.net/images/20250204/1738602158692364_1980e63ffbdb4c248c83401222eacf8a.jpg!small)

毫无疑问，DeepSeek的出现将AI大模型推向了一个新的高度，堪称AI史上的里程碑事件。但快速技术进步所带来的希望与危险总是如影随形，大量的恶意攻击者正在暗中凝视，需要投入更多的资源，提高重视程度，构筑新的安全防线。

## 参考来源

<https://cybersecuritynews.com/hail-and-rapper-botnet-is-the-mastermind-behind-the-deepseek-cyberattack/>

[https://mp.weixin.qq.com/s?\_\_biz=Mzg2Nzg0NDkwMw==∣=2247491690&idx=1&sn=bd5f4d9fb8dcaf281a0363c25512c50f&chksm=cf81711596f57e9501e114dc14706f2bde2a25a007b435b76ca42466380510a18a2e6540bed7#rd](https://mp.weixin.qq.com/s?__biz=Mzg2Nzg0NDkwMw==&mid=2247491690&idx=1&sn=bd5f4d9fb8dcaf281a0363c25512c50f&chksm=cf81711596f57e9501e114dc14706f2bde2a25a007b435b76ca42466380510a18a2e6540bed7#rd)

# AI安全

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

DeepSeek网络攻击幕后黑手

* 1、HailBot
* 2、RapperBot

DeepSeek深陷风暴之中

参考来源

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