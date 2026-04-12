---
title: Nginx曝新漏洞，特定配置下可实现任意文件读写
url: https://mp.weixin.qq.com/s/EaFeQ0CPPY1emzIYYDFrAw
source: Doonsec's feed
date: 2026-04-11
fetch_date: 2026-04-12T04:44:17.952003
---

# Nginx曝新漏洞，特定配置下可实现任意文件读写

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/fFyp1gWjicMKRfkOibMss786PqPwUGjHu4siboRiaqI4mguqRmR09PN8XVEaw2KnV8ORyrCRF8ZQz35agEmw3yebIQ/0?wx_fmt=jpeg)

# Nginx曝新漏洞，特定配置下可实现任意文件读写

原创

微步情报局
微步情报局

微步在线研究响应中心

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMKNkm4Pg1Ed6nv0proxQLEKJ2CUCIficfAwKfClJ84puialc9eER0oaibMn1FDUpibeK1t1YvgZcLYl3A/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

漏洞概况

Nginx是一款轻量级的高性能Web服务器和反向代理服务器。ngx\_http\_dav\_module 是 Nginx 的一个内置 HTTP WebDAV 模块，用来让客户端通过 HTTP 方法直接操作服务器上的文件和目录。

微步情报局于今日监控到Ngnix ngx\_http\_dav\_module模块缓冲区溢出漏洞（CVE-2026-27654）。微步情报局已成功复现。当Nginx配置同时满足以下条件时，攻击者可以通过特制请求触发缓冲区溢出：

1. location 是普通前缀块
2. 开启 dav\_methods COPY/MOVE
3. 使用alias指令来映射本地目录

经分析，ngx\_http\_dav\_module模块非默认安装，且漏洞依赖特殊配置，可能实际影响资产数量较为有限。但由于该漏洞aarch64架构上的利用脚本已公开，且能造成任意文件读写，建议用户自查当前Nginx配置是否满足上述利用条件，如果确认受影响请尽快修复。

（完整自查方案请查阅微步漏洞情报：https://x.threatbook.com/v5/vul/XVE-2026-9305）

漏洞处置优先级(VPT)

**综合处置优先级：中**风险

|  |  |  |
| --- | --- | --- |
| 基本信息 | 微步编号 | XVE-2026-9305 |
| CVE编号 | CVE-2026-27654 |
| 漏洞类型 | 缓冲区溢出 |
| 利用条件评估 | 利用漏洞的网络条件 | 远程 |
| 是否需要绕过安全机制 | 否 |
| 对被攻击系统的要求 | 1.需要使用ngx\_http\_dav\_module模块 2. 必须允许COPY或MOVE方法 3. 必须使用alias指令来映射本地目录 4. location配置中必须存在一个普通的、非正则表达式的URI前缀匹配块 |
| 利用漏洞的权限要求 | 无需用户权限 |
| 是否需要受害者配合 | 否 |
| 利用情报 | POC是否公开 | 是 |
| 已知利用行为 | 暂无 |

漏洞影响范围

|  |  |
| --- | --- |
| 产品名称 | F5 | NGINX |
| 受影响版本 | 开源版 0.5.13 <= version <= 0.9.7 1.0.0 <= version < 1.28.3 1.29.0 <= version < 1.29.7  商业版  R36 分支：R36 <= version < R36 P3 R35 分支：R35 <= version < R35 P2 R34 分支：所有版本 R33 分支：所有版本 R32 分支：R32 <= version < R32 P5 |
| 有无修复补丁 | 有 |

漏洞复现

![image.png](https://mmbiz.qpic.cn/mmbiz_png/T4OSm0sXdEMu32CWIFc0Zw2leDsibAtQiaQs0GyjduclCL2OiaVgZ3f7SV9J7qYbWtgDVZreVh0sKONAejOCg7EIAxBYwFdVhGUZFFN0cibEDfs/640?wx_fmt=png&from=appmsg)

由上图可见成功读取/etc/passwd文件

修复方案

### 官方修复方案

官方已发布修复方案，请访问链接下载：
https://my.f5.com/manage/s/article/K000160382

### 临时缓解措施

修改nginx.conf中对应的location块，在dav\_methods中禁用COPY和MOVE方法，配置方式如下所示：

1. 将nginx.conf中dav\_methods COPY; 修改为 dav\_methods PUT DELETE MKCOL;
2. 检查Nginx配置：nginx -t -c /tmp/lab/nginx.conf -p /tmp/lab/
3. 重启 Nginx：nginx -s reload

微步产品支撑

微步漏洞情报于2026-03-24收录该漏洞。

微步下一代威胁情报平台NGTIP及X情报社区已于漏洞收录时向漏洞订阅用户推送该漏洞情报，并将持续推送后续更新；对于已经录入资产的用户，支持实时自动化排查受影响资产。

微步威胁感知平台TDP通用规则默认可检出。

- END -

**微步漏洞情报订阅服务**

微步提供漏洞情报订阅服务，精准、高效助力企业漏洞运营：

* 提供高价值漏洞情报，具备及时、准确、全面和可操作性，帮助企业高效应对漏洞应急与日常运营难题；
* 可实现对高威胁漏洞提前掌握，以最快的效率解决信息差问题，缩短漏洞运营MTTR；
* 提供漏洞完整的技术细节，更贴近用户漏洞处置的落地；
* 将漏洞与威胁事件库、APT组织和黑产团伙攻击大数据、网络空间测绘等结合，对漏洞的实际风险进行持续动态更新。

扫码在线沟通

↓↓↓

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hQl5bZ5Mx6PTAQg6tGLiciarvXajTdDnQiacxmwJFZ0D3ictBOmuYyRk99bibwZV49wbap77LibGQHdQPtA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hTIdM9koHZFkrtYe5WU5rHxSDicbiaNFjEBAs1rojKGviaJGjOGd9KwKzN4aSpnNZDA5UWpY2E0JAnNg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

点此电话咨询

**X漏洞奖励计划**

“X漏洞奖励计划”是微步X情报社区推出的一款针对未公开漏洞的奖励计划，我们鼓励白帽子提交挖掘到的0day漏洞，并给予白帽子可观的奖励。我们期望通过该计划与白帽子共同努力，提升0day防御能力，守护数字世界安全。

活动详情：https://x.threatbook.com/v5/vulReward

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicML0NlKR16SxQGjNPSYVoUxGgXhXvI4Z8ia5h8C9TGibEic1ABv6fniame8h0dh6zGX8ndXT8icjQocVh8A/0?wx_fmt=png)

微步在线研究响应中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicML0NlKR16SxQGjNPSYVoUxGgXhXvI4Z8ia5h8C9TGibEic1ABv6fniame8h0dh6zGX8ndXT8icjQocVh8A/0?wx_fmt=png)

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