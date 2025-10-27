---
title: Awaken Likho恶意组织利用高级网络工具对俄罗斯政府发起“猛攻”
url: https://www.freebuf.com/news/412331.html
source: FreeBuf网络安全行业门户
date: 2024-10-10
fetch_date: 2025-10-06T18:52:59.062485
---

# Awaken Likho恶意组织利用高级网络工具对俄罗斯政府发起“猛攻”

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

Awaken Likho恶意组织利用高级网络工具对俄罗斯政府发起“猛攻”

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

Awaken Likho恶意组织利用高级网络工具对俄罗斯政府发起“猛攻”

2024-10-09 13:32:09

所属地 上海

![](https://image.3001.net/images/20241009/1728453728_67061c6062f2cbc617e66.png!small)

近日，俄罗斯政府机构和工业实体遭遇了一场名为“ Awaken Likho ”的网络活动攻击活动。 卡巴斯基表示，攻击者现在更倾向于使用合法MeshCentral平台的代理，而不是他们之前用来获得系统远程访问权限的UltraVNC模块。这家俄罗斯网络安全公司详细说明了一场始于2024年6月并至少持续到8月的新活动。该活动主要针对俄罗斯政府机构、其承包商和工业企业。

“ Awaken Likho ”组织，亦称作Core Werewolf或PseudoGamaredon，最初由BI.ZONE于2023年6月曝光，涉嫌针对国防和关键基础设施部门发动网络攻击。据悉，该组织的活动可追溯至2021年8月。其采用的鱼叉式钓鱼攻击手法包括发送伪装成Word或PDF文档的恶意可执行文件，这些文件带有双重扩展名，如“doc.exe”或“.pdf.exe”，使用户仅能看到看似无害的.docx或.pdf后缀。

然而，一旦受害者打开这些文件，便会触发UltraVNC的安装程序，进而导致攻击者能够完全接管受害者的计算机系统。此外，根据F.A.C.C.T.今年5月的报告，Core Werewolf还针对位于亚美尼亚的一个俄罗斯军事基地以及一家从事武器研究的俄罗斯研究所发动了攻击。在这些攻击中，攻击者使用了一种自解压存档（SFX）技术，以隐蔽的方式安装UltraVNC，同时向受害者展示看似无害的诱饵文档。

卡巴斯基最新揭露的攻击链条中，攻击者利用7-Zip创建了一个SFX存档文件。当受害者打开该文件时，会执行一个名为“MicrosoftStores.exe”的程序，进而解压并运行一个AutoIt脚本，最终激活开源的MeshAgent远程管理工具。卡巴斯基解释称，这一系列操作使得攻击者能够在受害者的系统中长期潜伏，并通过计划任务定时执行命令文件，以此来启动MeshAgent并与MeshCentral服务器建立连接。

据安全专家分析，“ Awaken Likho ”团伙使用了定制化的恶意软件和零日漏洞利用，以实现对目标系统的深度渗透。此外，他们还运用了复杂的网络钓鱼和社会工程学技巧，诱导目标用户点击恶意链接或下载病毒文件。

值得注意的是，该团伙的攻击目标主要集中在俄罗斯政府的敏感部门和关键基础设施领域。这些攻击不仅可能导致政府机密的泄露，还可能对国家安全和社会稳定造成严重影响。

为了应对这一威胁，俄罗斯政府已经加强了对网络安全的投入，并提升了相关机构的防御能力。同时，国际间的网络安全合作也在不断加强，以共同应对跨国网络攻击的挑战。

专家建议，政府机构和个人用户都应提高网络安全意识，定期更新系统和软件补丁，避免点击不明链接或下载来源不明的文件。此外，加强数据备份和恢复策略也是防范网络攻击的重要措施。

> 参考来源：<https://thehackernews.com/2024/10/cyberattack-group-awaken-likho-targets.html>

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