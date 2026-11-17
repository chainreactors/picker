---
title: 银狐木马C2资产黑名单解构，50IP与165域名防线部署
url: https://mp.weixin.qq.com/s/mfo6Vqq07bPPHa7O8nNCRQ
source: Doonsec's feed
date: 2026-11-16
fetch_date: 2026-11-17T09:55:59.865837
---

# 银狐木马C2资产黑名单解构，50IP与165域名防线部署

# 银狐木马C2资产黑名单解构，50IP与165域名防线部署

子午猫
子午猫

网络侦查研究院

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

银狐木马画像，瞄准财务运维的潜伏式窃密

银狐木马（别名游蛇、谷堕大盗）持续活跃，主要瞄准财务、运维、业务岗，通过仿冒软件下载站、加密压缩包钓鱼、社交群文件投递传播。木马落地后优先做进程注入、新增计划任务、篡改杀毒软件排除项，回连境外C2服务器长期潜伏窃密，后续利用被控主机冒充内部人员实施转账诈骗。须注意变种哈希频繁变动，单靠文件哈希拦截效果差，网络层阻断C2通信是当前最有效基线防御。

C2资产清单，50个恶意IP与重点网段

本批清单整合CNCERT/CCTGA五期披露，共**50个**恶意IP。重点网段中**177.4.3.0/24**（巴西）五期出现**15+**个IP，建议重点封禁；另含**194.41.37.0/24**、**38.190.0.0/16**、**206.119.0.0/16**（香港/美国）及**8.210.0.0/16**、**47.242.0.0/16**、**47.243.0.0/16**、**148.66.0.0/16**（阿里云香港）。红色警示：**104.21.x**、**172.67.x**属Cloudflare共享CDN，按IP封禁会大规模误杀，只走域名黑洞。

域名黑名单，165个恶意域名与9条通配

清单含**165个**恶意域名，仿冒Microsoft的错别字域"mlcrosoft"为重灾区。用**9条**通配（\*.mlcrosoft.vip、\*.mlcro.net、\*.mlcrosoft.me、\*.mlcrosoft.my、\*.claudfront.net、\*.app939bet.com、\*.yyy16888.vip、\*.webcamcn.xyz、\*.preech.top）即可覆盖绝大多数mlcrosoft家族域名，比逐个域名更耐换绑。

防御部署要点，网络层阻断优先

防御优先级为域名DNS黑洞拦截 大于 防火墙IP地址组拦截 大于 终端杀毒特征库。中毒主机标准处置：**1**断网不断电保留内存取证；**2**导出网络日志/进程/计划任务；**3**离线修改全部账号密码；**4**全盘查杀或重装；**5**内部通知防冒充钓鱼；**6**线索上报CNCERT **010-82990999**/**96110**、邮箱**silverfox@cert.org.cn**。重点自查计划任务、Defender排除项、HOSTS篡改、进程注入，财务与运维岗优先。

情报价值：银狐IOC已体系化披露，企业应将50IP/165域名及9通配批量导入防火墙与DNS黑洞，并以"网络层阻断C2"为基线，配套中毒6步处置与CNCERT上报链路。

来源：AIIT数字工坊（2026年10月3日，福建）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mQFl6fQOc0oplp7nPyjqNiaH2UU1jRRK1ib2ibn9mibMRnnfhGqCcBfyPOjXbt91ulfYibap0fJ0fzeAqnazotP9HoicFFXPVahkibxCVNEMAVYUVw/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mQFl6fQOc0pFMJoZSTzxBzUoccZic69QVkmwFAylFs3GPL7eAe42cVnKYic0S9I7IGxYWprfxBo17ks1PjMU60UVBeLql0leFO24fYeDGXF5A/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/mQFl6fQOc0qn9ZMmy2TnVO3IpGicffuGughgtQxQCsSKsdd29HUZvslsDDMoUT5ZusGRwiachXrlyic1A0XlcFY4X8rM3HzgpZFFj5TBWibjPoo/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/mQFl6fQOc0pX5UdvW4DDh632R7gSBKIfPOlFTC03SaaNDFvw6ucQ9TZFBrJukKTUvJHhLQDOic4R8JAtYFoh7QG9uiakmkJtL4pQm1Jf9MQ0Y/640?from=appmsg)

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/4kCmTUe2v2b9Dn5TZppcYVNqtewpGLM6TUkWg29ayK9yWAJbqViaE15Ltf8AprRumW3Lmw3ibHOAsMYMnhNqcfiaA/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过