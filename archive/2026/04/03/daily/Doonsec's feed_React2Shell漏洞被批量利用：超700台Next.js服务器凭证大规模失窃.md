---
title: React2Shell漏洞被批量利用：超700台Next.js服务器凭证大规模失窃
url: https://mp.weixin.qq.com/s/Sl224HcVcNLF5Ou9LTCMMQ
source: Doonsec's feed
date: 2026-04-03
fetch_date: 2026-04-04T04:13:17.632671
---

# React2Shell漏洞被批量利用：超700台Next.js服务器凭证大规模失窃

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K1hV8T5ibCVgOjoDZaNWQtTswl05iaA2fnc1ia7GFzq7U26B30zp3qYNFyGs7ax7Q6qWKfldazEq0iaSte9truqB4K8Er3XE4tia6ias/0?wx_fmt=jpeg)

# React2Shell漏洞被批量利用：超700台Next.js服务器凭证大规模失窃

看雪学苑
看雪学苑

看雪学苑

![]()

在小说阅读器中沉浸阅读

近期，思科Talos团队披露一起大规模自动化凭证窃取事件。黑客组织UAT-10608利用编号CVE-2025-55182的远程代码执行漏洞（安全社区称React2Shell），对公网Next.js服务器进行批量扫描与入侵。目前已有超过700台服务器被确认失陷，攻击者通过自建的“NEXUS Listener”面板集中管理窃取到的敏感数据。

**漏洞本质**

CVE-2025-55182存在于React Server Components中，攻击者可构造特制HTTP请求，在无需认证、无需用户交互的情况下执行任意代码。由于输入校验不足，利用难度较低，因此被自动化工具大规模利用。

**攻击流程**

1. 自动化扫描公网未修复漏洞的Next.js实例

2. 通过React2Shell投递恶意脚本

3. 脚本遍历文件系统、访问云元数据接口、扫描进程内存，提取数据库凭证、SSH私钥、AWS/Stripe/GitHub令牌等

4. 将窃取数据加密回传至C2服务器

**失窃规模**

**（基于NEXUS Listener 24小时数据）**

* 766台主机被记录为失陷

* >90%数据库凭证被盗
* ~80%SSH私钥被提取
* 大量主机同时失窃AWS密钥、Stripe活动密钥、GitHub访问令牌

可能后果

- 数据库直连导致用户数据批量泄露

- SSH私钥用于内网横向移动

- 云凭证被用于接管云资源

- GitHub令牌用于向合法仓库植入后门

**处置建议**

1. 立即升级Next.js及相关依赖至修复版本（参考React/Next.js官方公告）

2. 全量轮换数据库密码、SSH私钥、云平台Access Key、Stripe密钥、GitHub令牌

3. 云环境启用IMDSv2，限制元数据服务访问

4. 排查异常后台进程、crontab及systemd服务

请相关团队尽快自查并修复。

资讯来源：Cisco Talos – UAT-10608利用CVE-2025-55182(React2Shell)批量入侵Next.js服务器事件报告

﹀

﹀

﹀

![](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg)

**球分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg)

**球点赞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg)

**球在看**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

看雪学苑

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

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