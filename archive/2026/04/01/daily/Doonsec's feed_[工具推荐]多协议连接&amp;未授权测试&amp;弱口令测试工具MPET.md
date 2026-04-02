---
title: [工具推荐]多协议连接&amp;未授权测试&amp;弱口令测试工具MPET
url: https://mp.weixin.qq.com/s/n3UA-cI8im6nPI021xRUFQ
source: Doonsec's feed
date: 2026-04-01
fetch_date: 2026-04-02T04:24:37.730124
---

# [工具推荐]多协议连接&amp;未授权测试&amp;弱口令测试工具MPET

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MSDUaqtwboQCejDnKR8rj4qcRsic2tfhC3edVlSZ10Mcss3T6hRRQLDWIsg4o3yVSiccf3VLVicicBfXuC4f9muvuJfH0rMZtZT42PyZLuVeyMc/0?wx_fmt=jpeg)

# [工具推荐]多协议连接&未授权测试&弱口令测试工具MPET

onewinner
onewinner

陌笙不太懂安全

![]()

在小说阅读器中沉浸阅读

免责声明

```
由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号陌笙不太懂安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉，谢谢！
```

工具简介

MPET (Multi-Protocol Exploitation Toolkit) 是一款专业的多协议安全测试工具，基于 Wails 框架构建的现代化桌面应用。它提供了对 25+ 种主流服务协议的连接测试、未授权访问检测、弱口令检测和漏洞利用能力，是安全研究人员和渗透测试工程师的得力助手。

核心功能

```
✅ 多协议支持: 覆盖 25+ 种主流服务协议（数据库、文件传输、消息队列、容器编排等）✅ 智能导入: 支持 CSV、Fscan 1.8.4、Fscan 2.1.1、Lightx 结果文件自动识别和导入✅ 批量操作: 批量导入、批量连接、批量删除、批量导出✅ 未授权检测: 自动检测 Redis、MongoDB、Docker、Kubernetes 等服务的未授权访问✅ 弱口令检测: 自动识别扫描工具结果中的弱口令，支持自定义凭据测试✅ 命令执行: SSH、Docker、Kubernetes 容器命令执行✅ 文件浏览: FTP、SFTP、SMB 文件浏览和下载✅ 远程桌面: VNC、RDP 屏幕截图获取✅ 实时监控: 实时显示连接状态和详细日志✅ 漏洞报告: 自动生成 Markdown 格式漏洞报告，包含截图和修复建议✅ 漏洞管理: 内置漏洞信息库，支持自定义编辑
```

工具使用

📥 五种导入方式

手动添加：点击“添加”，填写服务类型、IP、端口、用户名密码，测试连接后保存

扫描结果导入：点击“导入”，选择 Fscan/Lightx 的 .txt 或 .csv 文件，自动解析未授权访问和弱口令

CSV 批量导入：按指定格式准备 CSV 文件，一键导入批量目标

剪贴板导入：复制符合格式的文本，点击“剪贴板导入”即可解析

拖拽上传：直接将文件拖入应用窗口，自动识别格式并导入

🔌 连接测试

单个测试：点击列表中的“重连”按钮

批量测试：勾选目标后点击“批量连接”，系统并发执行

🔍 查看与交互

详情面板：点击“详情”展开，可查看连接日志、执行命令、浏览文件（FTP/SFTP/SMB）

容器管理：支持 Docker 容器 Shell、Kubernetes Pod 命令执行

屏幕截图：VNC/RDP 服务可获取远程桌面截图

📄 报告导出

勾选目标后点击“导出报告”，自动生成包含漏洞信息、截图和修复建议的 Markdown 报告，保存至 reports/ 目录。

⚙️ 辅助功能

漏洞信息管理：可自定义各服务的漏洞名称、等级、描述与修复建议

代理配置：支持 SOCKS5 代理，所有连接均可通过代理访问

筛选搜索：按服务类型、IP、用户名、状态等快速筛选目标

系统日志：查看运行日志，便于调试与审计

工具展示

主界面

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQ7ByJrcbrU58ibRxuUXlvEYGKa5Sw5fPgy1u03xOdAo61HejcAoxFd1W28YZz3lvmGXxKlTVfict9ppbceia5ypJ6F7ibuibbFMsCc/640?wx_fmt=png&from=appmsg)

连接详情

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRvMu4QqvPyTFYjEZqFDSYOGKk8tBHrdiajWbZZJjPAMYkys5nvqQGibez5Qn8vNsyJtRqq7NZJFUgX7Q08vMC25RLcSbPawIIK4/640?wx_fmt=png&from=appmsg)

文件浏览器

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSXaZHrHdvQXZ0xryw5ngI4yl1LJXrNRrP3WnwYdsYbjN0JcCiaTCuw4GHpTKv2PKKqAZH3Ikyt14E7cOQ140NljRnntwKaib1ks/640?wx_fmt=png&from=appmsg)

Docker Shell

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRfFfibTiaOPOXOc2ZQo8fre6I6cVaBkmpg1SHNy0eibsbPt7cD1tnhmR27wqrnb1UQpKrZZvKOO2WD9a2s5sJkSB3d6TbbPGuQBM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTcvibvO0XpfkgvErZibvefXuQIRrVPlDA6GibQKiaxQia9SavnVxMFvunVrYG0iaMNxlFmD74koQU7bc8YJF3iaIt1TXlQbQDnqoLzyI/640?wx_fmt=png&from=appmsg)

漏洞报告

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTovsPloeE0wQSc7E1OCEFj2NAEXjY4OJ4Wq6NMlyLLooQ8KtVbQ9S1kMjxVVFBsYZuarPXOI5CVxqvHCcGYrw3sTugQkbibBB4/640?wx_fmt=png&from=appmsg)

后台回复加群即可加入交流群

广告：  cisp pte/pts &nisp1级2级低价报考。

陌笙安全纷传圈子+陌笙src挖掘知识库+陌笙安全漏洞库+陌笙安全面试题库介绍（加入圈子送知识库+漏洞库+面试题库）

如果觉得合适可以加入,圈子的价格只会根据圈子内容和圈子人数进行上调，不会下跌。。。

圈子福利

漏洞挖掘1v1指导,我给指定站,你测试之后出报告,我根据报告总结你不出洞的问题,以及看漏洞点和总结，当然你可以自己找站，我来帮你完善总结思路。（不包过，思路为主，主要针对小白，大师傅就没必要了，主打性价比，帮师傅们快速提升，挖到第一个edu洞。）

![](https://mmbiz.qpic.cn/mmbiz_jpg/MSDUaqtwboR7v3GgENCXPfzwrkTKCyTu5CqOHyDR8OYWSXCfN1PmCjibjGpF1eMPfTuyXy3Am2v80V9c2JPI24C22dZq7KamHjG1XDzVmndw/640?wx_fmt=jpeg&from=appmsg)

陌笙src挖掘知识库介绍（内容持续更新中）

```
信息收集弱口令漏洞任意文件读取&删除sql注入漏洞各种逻辑漏洞url重定向漏洞命令执行漏洞反序列漏洞未授权访问漏洞挖掘XSS漏洞挖掘CSRF漏洞挖掘dns域传送漏洞SSRF漏洞挖掘EDUSRC挖掘案例分享经典常见漏洞复现等各模块不在一一介绍
```

edusrc

![](https://mmbiz.qpic.cn/mmbiz_jpg/MSDUaqtwboSwuCOUvOm2WZT3MnI5l6ZOojicRNTiaFZkfWkhxynkkrj7VumBFeAPzHOSyLcM8VicaHLvgnDHMlC3KNtuB4gP1eMEfPRlVthueY/640?wx_fmt=jpeg&from=appmsg)

src挖掘基础

![](https://mmbiz.qpic.cn/mmbiz_jpg/MSDUaqtwboS9kKcajTImhgUVrJJ1MMrsfGdzF3W6JwKVZegAjCjmTcEoYUT9rN94ZB8ibzUtPdeueOgelkicHfia23cCuWx2tKnS45JibNPRhxE/640?wx_fmt=jpeg&from=appmsg)

src挖掘实战（具体功能的相关测试思路）

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MSDUaqtwboSNlpw0LQ9mJIXOvAFopAF2jqLzBxzNWiclyeBgA2GFUzystCMuoB7Pe8vkFQqr15ErC9icP0XpQo2VzibEOmZUZkicdpyNDIJjpfo/640?wx_fmt=jpeg&from=appmsg)

经典Nday复现

![](https://mmbiz.qpic.cn/mmbiz_jpg/MSDUaqtwboRORzib6XBkTuR1vYz2O7rSMFibO8rPY7VGJVqn3pkJKGr6OwHQda7zXNRQ8GnibWZF1n1CibOfbdbSQ3QkIiaAsfiaD4AuXQltiawlkI/640?wx_fmt=jpeg&from=appmsg)

陌笙安全漏洞库介绍

```
1day&0day分享EDUWeb应用漏洞CMS漏洞OA产品漏洞中间件漏洞云安全漏洞人工智能漏洞其他漏洞开发框架漏洞开发语言漏洞操作系统漏洞数据库漏洞网络设备漏洞等
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/MSDUaqtwboSjhecIm4q8dcViaaJlWghsZJlCvXLqC7XefiagLgOq2ichXia5sQWOuDI9EsAgwXehOWUwVwu5OJcXt67PTOReM34v8JA2En2FyV4/640?wx_fmt=jpeg&from=appmsg)

陌笙安全面试库

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MSDUaqtwboREhHx7QdruJm0IjDmwhpr0VHrlNicQ5qu1350EvBJ0AEujLgTBuydD6rC6DS8TbBoWrLd6w4MuDn02mkI06Cc1tOOXKWsJ5Bm4/640?wx_fmt=jpeg&from=appmsg)

圈子介绍

```
1、src挖掘思维导图，信息收集思维导图，edusrc挖掘思维导图，以及后续的红队&面试思维导图&自己网安笔记等持续更新2、2025-2026的edusrc实战报告包含证书站和非证书站以及2025之前的各种优质报思路分享3、各种src报告思路分享（内部&外部）4、分享各种src挖掘&edusrc挖掘培训资料&视频5、不定期分享通杀、0day6、有圈子群可以技术交流以及不定期抽取证书&免费rank7.分享各种护网资料各家安全厂商讲解视频&精选实战面试题目8、各种框架漏洞技巧分享9、各种源码分享（泛微、正方系统、用友等）10、漏洞挖掘工具&信息收集工具&内网渗透免杀等网安工具分享11、各种ctf资料以及题目分享12、cnvd挖掘技巧&CNVD资产&src资产分享&补天1权重资产分享&fofakey共用13、免杀、逆向、红队攻内网防渗透等课程分享14、漏洞库&字典以各种内容不在一一说明15、cisp-pte/pts&nisp一级&nisp二级&edusrc证书内部价格15、如果有漏洞挖掘问题或者工具资料需求可以找群主(尽量满足)
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSY2pbvbP3qGAlW8O43bRvAISCxZm4UDTRsaMVbJKTsjfTMTDlq6qNBcVs4tkl4UzgqGz5ag81baU1rusKE09J9T6cMVliaibibwQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MSDUaqtwboTrLRQpTicOR7bzyNiajiapVJgyMiaYlEDBVU87YXMnanOFWsCYN3cCVGsKkibzV9dMryvbFXBb4Z3472ib27RJ1Xq1HnKJIp5u49GYQ/640?wx_fmt=jpeg&from=appmsg)

目前620多条内容，扫码查看详情，持续更新中。。

如果觉得合适可以加入，价格不定期会根据圈子内容和圈子人数进行上调.

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQAD39Tr6hXUIic3ruKMtCkPcUQPfbat6V7d6EUdC26Ntn053G07hnsdSWVuU6nShEv7rOsP1GwQtticGgD5ic8VJMziaNhn1njvibo/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO4n1wSEsRXe9I7EjtXDn7f7PcEQBD0X8ly0heoXcFtjhDqXg5kHxicuwfL8iaT0nVFGEaibvK3Gib0Ovw/0?wx_fmt=png)

陌笙不太懂安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO4n1wSEsRXe9I7EjtXDn7f7PcEQBD0X8ly0heoXcFtjhDqXg5kHxicuwfL8iaT0nVFGEaibvK3Gib0Ovw/0?wx_fmt=png)

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