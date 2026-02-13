---
title: 【供应链投毒】钓鱼站7zip[.]com分发木马文件
url: https://mp.weixin.qq.com/s/eV6WCOKm7So6RiJb2DCzwQ
source: Doonsec's feed
date: 2026-02-12
fetch_date: 2026-02-13T04:14:52.649964
---

# 【供应链投毒】钓鱼站7zip[.]com分发木马文件

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/UA4ABKCY6OyKaC0fG4Ix2rBjy3g5FopQmvvmltSucC3yenZ2Df2rPetxMghJxMwiam7sXORgBbV12FgDJvvFbt09JoC5o7MxUGSmyKhNIGvY/0?wx_fmt=jpeg)

# 【供应链投毒】钓鱼站7zip[.]com分发木马文件

原创

泼猴
泼猴

表哥带我

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/mmbiz_gif/pxKqYxJWy7MwqgqlfAHibBF3z5SG1jQ33gAZpcpSzNrDOcWqOwsflg9dtktFJDmQDp8S0zibEmjILNJGcxK9bAjA/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

> ❝
>
> 由于传播、利用本公众号"表哥带我"所提供的信息而造成的任何直接或者间接的后果及损失,均由使用者本人负责，本文仅供安全研究。

**威胁类型：域名抢注（TLD Squatting）+ 供应链投毒**
**恶意域名**：7zip.com（非官方）
**官方域名**：7-zip.org（Igor Pavlov维护）
**首次活跃**：2023年12月（根据Internet Archive记录）
**威胁等级**：高危（系统级持久化+住宅代理滥用）

![](https://mmbiz.qpic.cn/mmbiz_png/UA4ABKCY6Oyw0rt9iaZ4pHL92a25Z6FVfxCR7iaY1ZrwWUy252efVz6vmLSU1EGAIEzdNNuEEzjicZiaAJP3wKAeGBXv4ibXcMHtYGbuZc4KxdHg/640?wx_fmt=png&from=appmsg)

| 时间节点 | 事件描述 |
| --- | --- |
| **2023年12月** | 7zip.com域名开始托管7-Zip下载文件，此前该域名长期处于待售状态 |
| **2024年5月** | 7-Zip作者Igor Pavlov在SourceForge发布警告："Do not trust 7zip.com website, and do not use it" |
| **2025年8月起** | 下载量显著增加，与WinRAR漏洞（CVE-2023-38831）曝光后用户寻找替代品的时间点吻合 |
| **2026年1月** | 日本安全研究人员首次公开标记该威胁 |
| **2026年2月9日** | Malwarebytes发布详细技术分析，揭露代理软件本质 |
| **至今** | 网站仍在线运营，持续分发木马安装程序 |

![](https://mmbiz.qpic.cn/mmbiz_png/UA4ABKCY6OyNddCnHo9IojjK69D12BOARlibE2dPpaHUrKJeEiaPbRtSeicVOXnKbm6F8coiac1uuibzV4KA7giblCV34nAcfsGJKDAJzicYDWzUKU/640?wx_fmt=png&from=appmsg)

该域名早在 1999 年就已注册，但近期被用于投毒传播。目前尚不清楚攻击者是直接收购域名，还是通过其他方式获得控制权。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UA4ABKCY6OwWkqiahnsJwa35mjchKcDrfNXVOicPE18GVl4UvH3JqOmX3Gja7v6mp7QQfuowdoXUOo97YCfdezW89eCbzsqBBXdtZlZ5N11SM/640?wx_fmt=png&from=appmsg)

该钓鱼网站几乎完整复制了 7-Zip 官方页面的界面设计，普通用户在未仔细核对域名的情况下，很容易误判为正规站点，直接下载安装所谓的“最新版”。

![](https://mmbiz.qpic.cn/mmbiz_png/UA4ABKCY6OxltG90B9RhnGCy7rL8eRPv68Wqo7enNXVXjeBXYA4LsQYKsb154UA8fdReL34PTicx0micwYibttMMv7mv5AxLiaiakFmRibywgicVmQ/640?wx_fmt=png&from=appmsg)

**主程序 7zfm.exe**（被修改的官方文件管理器，功能正常以降低警觉）

使用了反分析技术，虚拟机检测（检查VMware、VirtualBox、QEMU、Parallels痕迹）且每日更新载荷（通过JPHP库动态拉取，MD5每日变更2-3次）

## 检测指标（IoC）

```
#文件系统痕迹C:\Windows\SysWOW64\hero\Uphero.exeC:\Windows\SysWOW64\hero\hero.exe  C:\Windows\SysWOW64\hero\hero.dll
```

```
#文件系统痕迹Domain: 7zip[.]com（分发域）Domain: update.7zip[.]com（更新域）Domain: iplogger[.]org（监控域）Ports: 1000/tcp, 1002/tcp（代理通信）DoH: dns.google（DNS-over-HTTPS解析）
```

### 企业级检测规则（Sigma）

```
title: 7zipcom Proxyware Detectionlogsource:    product: windows    category:        - process_creation        - file_event        - network_connectiondetection:    selection_file:        TargetFilename|contains: '\Windows\SysWOW64\hero\'    selection_process:        Image|endswith:            - '\Uphero.exe'            - '\hero.exe'    selection_network:        DestinationPort:            - 1000            - 1002        Initiated: 'true'    condition: 1 of selection_*falsepositives:    - Unknownlevel: critical
```

### 终端狩猎查询（PowerShell）

```
# 检查恶意目录存在性Test-Path "C:\Windows\SysWOW64\hero\"
# 检查可疑服务Get-Service | Where-Object {$_.Name -match "hero|uphero|7zip"}
# 检查防火墙规则异常netsh advfirewall firewall show rule name=all | Select-String "hero"
# 检查网络连接Get-NetTCPConnection -LocalPort 1000,1002 -ErrorAction SilentlyContinue
```

###

其他阅读：

[Wechat RCE 复现](https://mp.weixin.qq.com/s?__biz=Mzg4NDg2NTM3NQ==&mid=2247487062&idx=1&sn=1c3dbc35632588f1d3e3ba4ed977d87f&scene=21#wechat_redirect)

[【网安音乐首发】泼猴之歌](https://mp.weixin.qq.com/s?__biz=Mzg4NDg2NTM3NQ==&mid=2247487036&idx=1&sn=cff35a8bf0ae85cd929738c8f2ad927a&scene=21#wechat_redirect)

[测绘引擎的真正用途是找小电影](https://mp.weixin.qq.com/s?__biz=Mzg4NDg2NTM3NQ==&mid=2247487024&idx=1&sn=614f6c835174bba18975eef2d48ceaa5&scene=21#wechat_redirect)

[绕过千问限制使用红包下单](https://mp.weixin.qq.com/s?__biz=Mzg4NDg2NTM3NQ==&mid=2247486980&idx=1&sn=cb43bdcddd4eecbaeea230d3f51d75e8&scene=21#wechat_redirect)

[丹麦情报机构重启"黑客学院"公开招募黑客](https://mp.weixin.qq.com/s?__biz=Mzg4NDg2NTM3NQ==&mid=2247486947&idx=1&sn=221b7f2c2648a9ac9c6d44b382d03daf&scene=21#wechat_redirect)

[网传BT面板突遭黑产批量攻击](https://mp.weixin.qq.com/s?__biz=Mzg4NDg2NTM3NQ==&mid=2247486920&idx=1&sn=4d07ffb5748ba4f62ef6cf9ccfb0758e&scene=21#wechat_redirect)

[用泄露的爱泼斯坦邮箱拿下微软365个人版](https://mp.weixin.qq.com/s?__biz=Mzg4NDg2NTM3NQ==&mid=2247486848&idx=1&sn=ea2645950f190e264ecc7092d5381690&scene=21#wechat_redirect)

[网传海角社区泄露1570万条用户数据](https://mp.weixin.qq.com/s?__biz=Mzg4NDg2NTM3NQ==&mid=2247486775&idx=2&sn=0460974909d1d3c15de929de44d69bc8&scene=21#wechat_redirect)

[【吃瓜】Telegram大量用户数据泄露](https://mp.weixin.qq.com/s?__biz=Mzg4NDg2NTM3NQ==&mid=2247486552&idx=1&sn=6e3fe989d90dcefc461261763bb1f100&scene=21#wechat_redirect)

[Notepad++遇国家级APT投毒定向百万设备](https://mp.weixin.qq.com/s?__biz=Mzg4NDg2NTM3NQ==&mid=2247486743&idx=1&sn=c9b0e8ed68b2a53e723f3e4453b2c9e4&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/UA4ABKCY6Ox7Z4PiakBVAniarSaJib8DVWFqk0KwomqkJSGShO43pp3gqG3lhUc4DDe3ibEJ4RyaMfqpXLwkZ0hnibGDDxx2bTjwcEl9EueWIUuY/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=wxpic#imgIndex=9)

**左侧长按加入**

**吃瓜交流群**

动态入群二维码

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/pxKqYxJWy7PW1JR7KU1wRqvaNyp3ESh9m1FzIau0Uqvh7DDnryFJCzq3u7sc2J8wAtOffybvhBgkQW1CfJs9sg/0?wx_fmt=png)

表哥带我

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/pxKqYxJWy7PW1JR7KU1wRqvaNyp3ESh9m1FzIau0Uqvh7DDnryFJCzq3u7sc2J8wAtOffybvhBgkQW1CfJs9sg/0?wx_fmt=png)

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