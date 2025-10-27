---
title: Azure AI被黑客越狱，提供“黑客即服务”
url: https://www.freebuf.com/news/419701.html
source: FreeBuf网络安全行业门户
date: 2025-01-14
fetch_date: 2025-10-06T20:10:36.743983
---

# Azure AI被黑客越狱，提供“黑客即服务”

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

Azure AI被黑客越狱，提供“黑客即服务”

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

Azure AI被黑客越狱，提供“黑客即服务”

2025-01-13 13:42:27

所属地 上海

微软近日宣布，正在对一个“外国黑客组织”提起诉讼。该组织运营“黑客即服务“的基础设施，故意绕过微软生成式人工智能（AI）服务的安全控制来制作冒犯性和有害内容。

![](https://image.3001.net/images/20250113/1736746939_6784a7bbc7cc25fba6c42.png!small)

微软的数字犯罪部门（DCU）称，他们发现威胁行为者“开发了复杂软件，利用从公共网站抓取暴露的客户凭据”，并且“试图识别并违法访问拥有某些生成式AI服务的账户，还故意改变这些服务的能力”。

之后，这些对手利用如Azure OpenAI Service等服务，通过将这些访问权限出售给其他恶意行为者来变现，同时为他们提供详细说明如何运用这些定制工具生成有害内容。

微软还表示，在此之后已经撤销了攻击者的访问权限，实施了新的应对措施，并且强化了安全措施以防止类似活动再次发生。此外，微软还获得了一项法院命令，查封了对该集团犯罪活动至关重要的网站（“aitism[.]net”）。

法庭文件显示，至少有三名未知个人参与了此次行动，他们利用被盗的Azure API密钥和客户Entra ID身份验证信息侵入微软系统，并且使用DALL - E违反可接受使用政策创建有害图像。

目前尚不清楚API密钥是如何被收集的，不过微软表示，被告从多个客户（其中包括几家位于宾夕法尼亚州和新泽西州的美国公司）进行了“系统性API密钥盗窃”。

微软公司在一份文件中指出：“使用被盗的属于美国微软客户的Microsoft API密钥，被告创建了一种黑客即服务方案——可通过‘rentry.org/de3u’和‘aitism.net’这样的基础设施访问——专门用于滥用微软的Azure基础设施和软件。”

据一个现已被删除的GitHub存储库描述，de3u被称作“具有反向代理支持的DALL - E 3前端”，该GitHub账户于2023年11月8日创建。

据说，威胁行为者采取措施“掩盖他们的踪迹，包括试图删除某些Rentry.org页面、de3u工具的GitHub存储库以及部分反向代理基础设施”，随后“aitism[.]net”被查封。

微软指出，威胁行为者使用de3u和一个名为oai反向代理的定制反向代理服务，借助被盗的API密钥通过Azure OpenAl Service API调用来非法生成数千张使用文本提示的有害图像，但不清楚创建的是何种冒犯性图像。

运行在服务器上的oai反向代理服务旨在将通过Cloudflare隧道的de3u用户计算机通信引入Azure OpenAI Service，并把响应传回用户设备。

雷德蒙解释说：“de3u软件允许用户通过利用Azure API访问Azure OpenAI Service的简单用户界面发出使用DALL - E模型生成图像的Microsoft API调用。”

“被告的de3u应用程序使用未经记录的Microsoft网络API与Azure计算机通信，发送旨在模仿合法Azure OpenAPI Service API请求的请求，并且使用被盗的API密钥和其他身份验证信息进行身份验证。”

值得注意的是，Sysdig在2024年5月与针对AI产品（包括Anthropic、AWS Bedrock、Google Cloud Vertex AI、Microsoft Azure、Mistral和OpenAI）的LLMjacking攻击活动相关联时，强调了使用代理服务非法访问LLM服务。

微软表示：“被告通过协调一致的持续非法活动模式实施针对Azure企业的滥用行为，以实现他们共同的非法目的。被告的非法活动模式不限于对微软的攻击。到目前为止，微软所揭示的证据表明，Azure滥用企业一直在针对其他AI服务提供商并且遭受其害。”

参考来源：<https://thehackernews.com/2025/01/microsoft-sues-hacking-group-exploiting.html>

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