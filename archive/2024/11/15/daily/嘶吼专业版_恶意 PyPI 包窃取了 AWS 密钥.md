---
title: 恶意 PyPI 包窃取了 AWS 密钥
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247579611&idx=1&sn=c03873ed1cb5852d79d3cb4046bec984&chksm=e91467e1de63eef733c414232c897c202c290cd4effa10af9d0aa882741cc0d1f42eff192ab6&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2024-11-15
fetch_date: 2025-10-06T19:19:59.704488
---

# 恶意 PyPI 包窃取了 AWS 密钥

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o290gVu2kEAOZ6ApBvOFzKicoYIPwcsiam34AoiadRucLiaDveonEDvpz4TUInd50hJhCrwFcPZCSkmj1g/0?wx_fmt=jpeg)

# 恶意 PyPI 包窃取了 AWS 密钥

胡金鱼

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

自 2021 年以来，一个名为“fabrice”的恶意 Python 包一直出现在 Python 包索引 (PyPI) 中，从开发人员那里窃取 Amazon Web Services 凭证。

据应用安全公司 Socket 称，该软件包已被下载超过 37,000 次，并执行 Windows 和 Linux 平台特定的脚本。

大量下载是由于fabrice 对合法的SSH 远程服务器管理包“fabric”进行错字造成的，这是一个非常受欢迎的库，下载量超过2 亿次。

该 Fabrice 之所以长期未被检测到，是因为在 PyPI 上首次提交后就部署了先进的扫描工具，而且很少有解决方案进行追溯扫描。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o290gVu2kEAOZ6ApBvOFzKico9uD7E4fNiaxNdZY05rM0kCfDHQtysuAZ21pxYp0czXaMTICnexicpaCg/640?wx_fmt=png&from=appmsg)操作系统特定的行为

Fabrice 包旨在根据其运行的操作系统执行操作。

在 Linux 上，它在“~/.local/bin/vscode”处设置一个隐藏目录，用于存储分割成多个文件的编码 shell 脚本，这些文件是从外部服务器 (89.44.9[.]227) 检索的。

研究人员解释说，shell 脚本被解码并授予执行权限，让攻击者能够以用户权限执行命令。

在 Windows 上，fabrice 下载编码的有效负载 (base64)，该有效负载是为启动隐藏的 Python 脚本 (d.py) 而创建的 VBScript (p.vbs)。Python 脚本负责获取恶意可执行文件（“chrome.exe”），该可执行文件被放入受害者的下载文件夹中。

其目的是安排 Windows 任务每 15 分钟执行一次，以确保重新启动后的持久性。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o290gVu2kEAOZ6ApBvOFzKico9uD7E4fNiaxNdZY05rM0kCfDHQtysuAZ21pxYp0czXaMTICnexicpaCg/640?wx_fmt=png&from=appmsg)AWS凭证被盗

无论使用哪种操作系统，fabrice 的主要目标都是使用“boto3”（Amazon Web Services 的官方 Python SDK）窃取 AWS 凭证，从而允许与平台进行交互和会话管理。

Boto3 会话初始化后，它会自动从环境、实例元数据或其他配置的源中提取 AWS 凭证。然后，攻击者将窃取的密钥泄露到 VPN 服务器（由巴黎的 M247 运营），这使得追踪目的地变得更加困难。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o290gVu2kEAOZ6ApBvOFzKico9sgnIzG6vy6Iho3GG9tILO2Wj3giaG0dcUo4ZCdQMxkMcicAsvSVxcmA/640?wx_fmt=png&from=appmsg)

Python函数窃取AWS凭证

当用户检查从 PyPI 下载的包时，可以降低拼写错误的风险。另一种选择是专门为检测和阻止此类威胁而创建的工具。

在保护 AWS 存储库免遭未经授权的访问方面，管理员应考虑使用 AWS Identity and Access Management (IAM) 来管理资源权限。

参考及来源：https://www.bleepingcomputer.com/news/security/malicious-pypi-package-with-37-000-downloads-steals-aws-keys/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o290gVu2kEAOZ6ApBvOFzKico6CxfaPgduaP10ibuez7hPKmhhHSFgrHEuszhk6Yicekjyu4D1z1R13nw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o290gVu2kEAOZ6ApBvOFzKicoZCFXibbf5a1FQYvnnjLQib60XVMg59ibmqhNeicWm1XlG459jE6k9svuSQ/640?wx_fmt=png&from=appmsg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

嘶吼专业版

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

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