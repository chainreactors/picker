---
title: 最新高危漏洞威胁情报合集 (2026-01-21）
url: https://mp.weixin.qq.com/s/hVSCK-VKXjF3gexImuTLjA
source: Doonsec's feed
date: 2026-01-21
fetch_date: 2026-01-22T03:33:58.965103
---

# 最新高危漏洞威胁情报合集 (2026-01-21）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/AXRefkPRWsFhUzrqzZUH5mn4roHNYVoJlcMPO4yBhWtf30mvqibSkcDBG2ibvtk7kGGSCYqDy6p6PPAMluOurSnQ/0?wx_fmt=jpeg)

# 最新高危漏洞威胁情报合集 (2026-01-21）

原创

0xSecDebug
0xSecDebug

0xSecDebug

![]()

在小说阅读器中沉浸阅读

>     请勿利用文章内的相关技术从事**非法渗透测试**，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。**工具和内容均来自网络，仅做学习和记录使用，安全性自测，如有侵权请联系删除**。

# GNU InetUtils Telnetd 远程身份验证绕过漏洞

* CVE编号: CVE-2026-24061
* 危害定级: 严重
* 漏洞标签: 发布预警 公开漏洞
* 披露日期: 2026-01-21
* 推送原因: 漏洞创建
* 信息来源: https://www.oscs1024.com/hd/MPS-xs1v-brme

### 漏洞描述

    GNU InetUtils 是 GNU 项目发布的互联网实用工具集合，包含 telnet、ftp、rsh 等网络服务程序及客户端工具，主要用于类 UNIX 系统的网络连接与远程管理。其中 telnetd 为 telnet 协议的服务端实现，负责处理远程登录请求。 telnetd服务存在不同实现，在Ubuntu/CentOS系统中，telnetd默认为netkit实现，而非InetUtils。 受影响版本中，telnetd/telnetd.c 定义的 login 调用模板使用 PATH\_LOGIN " -p -h %h %?u{-f %u}{%U}" 格式，telnetd/utility.c 中的 \_var\_short\_name() 函数在展开 %U 变量时直接返回 getenv("USER") 的值。当客户端使用 -a 参数发送 USER 环境变量值为 -f root 时，telnetd 将该值未经校验传递给 login 程序，而 login 程序将 -f 参数解析为跳过密码认证选项，导致攻击者绕过正常身份验证流程直接获取 root 权限。 修复版本中通过在 telnetd/utili...

### 修复方案

1. 官方暂未发布修复版本，由于telnet协议为明文传输，建议停用 telnetd 服务，改为sshd服务。

### 参考链接

1. https://www.oscs1024.com/hd/MPS-xs1v-brme
2. https://www.openwall.com/lists/oss-security/2026/01/20/2
3. https://codeberg.org/inetutils/inetutils/commit/fd702c02497b2f398e739e3119bed0b23dd7aa7b
4. https://nvd.nist.gov/vuln/detail/CVE-2026-24061

### 开源检索

暂未找到

![img](https://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsFhUzrqzZUH5mn4roHNYVoJ7chiceFIej4z6PFVw2WYV2MvbdF31Dibr77MLcIcEWWU3tOmf0H7JBOw/640?wx_fmt=png&from=appmsg)

# GNU InetUtils Telnetd 远程认证绕过漏洞

* CVE编号: 暂无
* 危害定级: 严重
* 漏洞标签: 有Poc 有漏洞分析 有修复方案
* 披露日期: 2026-01-21
* 推送原因: 标签更新: [有Poc 有漏洞分析] => [有Poc 有漏洞分析 有修复方案]
* 信息来源: https://x.threatbook.com/v5/vulIntelligence

![img](https://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsFhUzrqzZUH5mn4roHNYVoJmMozmk4O9cysWpxDgS290EYhL0Ky5l8yzQ6atucFxhvCBNoYwy8M5w/640?wx_fmt=png&from=appmsg)

## 💻 威胁情报推送群

>   如果师傅们想要第一时间获取到**最新的威胁情报**，可以添加下面我创建的**钉钉漏洞威胁情报群**，便于师傅们可以及时获取最新的**IOC**。
>
>  如果师傅们想要获取**网络安全相关知识内容**，可以添加下面我创建的**网络安全全栈知识库**，便于师傅们的学习和使用：
>
>     覆盖渗透、安服、运营、代码审计、内网、移动、应急、工控、AI/LLM、数据、业务、情报、黑灰产、SOC、溯源、钓鱼、区块链等  方向，**内容还在持续整理中......**。

![img](https://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsGvpzTbNZamyJCmibbqwBWzgKUY4QqOTUNjibmmSiaNJibkPXMznRsC3eia8e4v7wcsibDepNqTft4aB2qw/640?wx_fmt=png&from=appmsg)![img](https://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsGvpzTbNZamyJCmibbqwBWzg8cDB2ibsdhJVnLBBlicLYjMtyTmOicUQbia7oIMS0Fia7uYtDrKXzULJVgQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnAqueibZX8s1IJDIlA8UJmu3uWsZUxqahoolciaqq65A30ia93jCyEwTLA/640?wx_fmt=gif&from=appmsg)

**点分享**

![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJniaq4LXsS43znk18DicsT6LtgMylx4w69DNNhsia1nyw4qEtEFnADmSLPg/640?wx_fmt=gif&from=appmsg)

**点收藏**

![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnev2xbu5ega5oFianDp0DBuVwibRZ8Ro1BGp4oxv0JOhDibNQzlSsku9ng/640?wx_fmt=gif&from=appmsg)

**点在看**

![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnwVncsEYvPhsCdoMYkI6PAHJQq4tEiaK3fcm3HGLialEMuMwKnnwwSibyA/640?wx_fmt=gif&from=appmsg)

**点点赞**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsGzSr4HnmUgiaibhvSicNIVAsdBq15vPEccY009wRZpHIJlvBl1ACks8gAYQYKicZwEKje2mMc1cia8ibGg/0?wx_fmt=png)

0xSecDebug

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsGzSr4HnmUgiaibhvSicNIVAsdBq15vPEccY009wRZpHIJlvBl1ACks8gAYQYKicZwEKje2mMc1cia8ibGg/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过