---
title: 正在被恶意利用的 Gitea 容器高危漏洞，可泄露代码仓库与密钥
url: https://mp.weixin.qq.com/s/RxBW807IwVO2BUviAPQsWQ
source: Doonsec's feed
date: 2026-07-08
fetch_date: 2026-07-09T05:59:31.676134
---

# 正在被恶意利用的 Gitea 容器高危漏洞，可泄露代码仓库与密钥

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/DYqn7TU9icq1E3W2NCFhDibsIyp7GB5kmaMH8UH1dLY3e03TiaicOBrxJZwX5nXWNTroeFmMhCfy4UCpaSymoAozSic3jyfBCROaKMec36VEGCy0/0?wx_fmt=jpeg)

# 正在被恶意利用的 Gitea 容器高危漏洞，可泄露代码仓库与密钥

鹏鹏同学
鹏鹏同学

黑猫安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DYqn7TU9icq0gsbzDicQVDPJUrEKG4rHJSRKuiabNvwlH8wGKyScQiaN2yRSH4YXPSffWu6kD3Agibv2fiaDgKw0oxAaXib8HUGtjEk4G9KmQ23Y6g/640?wx_fmt=png&from=appmsg)

Sysdig 研究人员发出警告：攻击者正在积极利用一枚高危身份验证绕过漏洞，漏洞编号 CVE-2026-20896（CVSS 评分 9.8 分），该漏洞影响 1.26.3 版本之前所有官方 Gitea Docker 镜像。

Sysdig 威胁研究高级总监迈克尔・克拉克表示：“漏洞披露仅 13 天就出现野外利用，仅需一条 HTTP 请求头，就能访问所有公网暴露的 Gitea 服务。无需密码、无需令牌，仅靠单个请求头即可入侵。漏洞公告发布 13 天后，Sysdig 监测传感器捕获到首起真实野外攻击，一台 VPN 出口扫描器借此非法获取访问权限。”

攻击者只需携带合法用户名构造一条特制 HTTP 请求头，就能绕过身份校验，侵入公网部署的 Gitea 实例，读取全部代码仓库与各类敏感密钥。该漏洞根源为不安全默认配置：系统允许任意 IP 接入，未限制仅可信反向代理可访问。

漏洞发现者、安全研究员阿里・穆斯塔法介绍：“1.26.2 及更早版本的 Gitea 官方 Docker 镜像，默认配置中`REVERSE_PROXY_TRUSTED_PROXIES`参数值设为通配符`*`。一旦开启反向代理登录功能，该通配符会将所有来源 IP 判定为可信代理。任意能连通服务端口的攻击者，只需传入`X-WEBAUTH-USER`请求头，就能伪装成任意账号登录，全程不用密码、不用身份令牌。”

Gitea 支持通过反向代理，依靠`X-WEBAUTH-USER`请求头完成用户鉴权，但该机制仅信任可信代理发来的请求。标准原生配置依靠 IP 白名单防护，默认仅信任本地本机地址。但官方 Gitea Docker 镜像存在配置缺陷：默认信任全部 IP 来源。因此只要启用反向代理鉴权，任何可访问 Gitea 服务的外部人员，都能通过伪造请求头冒充任意用户，甚至获取管理员权限。此漏洞**仅影响官方 Docker 镜像**，采用安全默认配置的原生安装、自行编译部署的 Gitea 不受影响。

该研究员补充道：“任何能直连 Gitea 容器 HTTP 端口（不走合规鉴权反向代理）的程序，只要知晓或能猜出用户名，就能冒充该账号登录，管理员账号是攻击者首要目标。”

Gitea 1.26.3、1.26.4 版本将反向代理鉴权功能改为手动可选启用，彻底修复该漏洞。

据 Sysdig 统计，通过 Shodan 检索全网约有 6200 台公网暴露的 Gitea 服务，但其中存在漏洞的设备数量暂无法统计。相关用户需立即升级版本，防止代码与密钥泄露。

克拉克最后总结：“Gitea 的用户权限绝非普通后台面板权限，背后是企业全部源代码。Gitea 账号可读写所有仓库（含私有仓库）：包括上线业务代码、开发人员不慎提交的密钥（API 密钥、数据库凭证、部署令牌）、CI/CD 流水线配置以及部署密钥。”

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/DYqn7TU9icq0Cqr2KYoUfur4KLeiclhRqlnu9g0qWMQJVEPqRicnicZzBdbaER3Jd1tI4NootkSwZiaruC4ATIbibbuM0riaianEiaRt0dVicRsfUhmI8/0?wx_fmt=png)

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