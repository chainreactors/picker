---
title: 为了云吸猫买了个智能摄像头，顺手挖出两个CNNVD二级贡献奖是什么体验？
url: https://mp.weixin.qq.com/s/mmR-JDbWAIA7Itib_yFmRQ
source: Doonsec's feed
date: 2026-09-23
fetch_date: 2026-09-24T07:05:29.805259
---

# 为了云吸猫买了个智能摄像头，顺手挖出两个CNNVD二级贡献奖是什么体验？

# 为了云吸猫买了个智能摄像头，顺手挖出两个CNNVD二级贡献奖是什么体验？

水滴实验室
水滴实验室

中国电信安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/Dh3fqSPAOWekCSIf3ffuFuiaBPl4BSArBsDhFEMSOTbeIfb7mdz4D0mDExZesv4PPicUdsOTxfRUx8QntAMTmTBA/640?wx_fmt=gif)

谢邀。人在重庆，刚在第16届VARA大会上领完奖下来，趁热乎劲唠唠这两张CNNVD二级贡献奖证书是怎么“顺手”拿到的。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/NicWxqLvw6Op6f5lMTwOX5VNpicsnNV8pr6omlFOHs1cPRjuiaIMR9l1ciaqZYvbfO3Q1KIbHhnrGAHhGxoT5S0hKyK72Ho4KtcWCJB6DsHfhRE/640?wx_fmt=jpeg)

今年2月，依托天翼安全（中国电信天翼安全科技有限公司）水滴实验室在攻防领域的多年积累，自研的灵鉴AI代码审计平台终于开发完成了。平台做出来了，总得验验效果。正好，实验室研究员家里养了只猫，就网购了一台智能摄像头，想随时“云吸猫”。

别人看摄像头，看画质清不清、夜视好不好、云台灵不灵；搞安全的第一反应是：这玩意儿安全吗？设备拿到实验室，一系列操作后成功拿到固件包，随后直接传到灵鉴平台上。半小时测试，挖出十几个漏洞，而且公网测绘数量巨大；挑出三个硬核漏洞上报CNNVD，后面的事大家都知道了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/NicWxqLvw6Oo2X41XXxtiaxDibvAJW1UvFjtt5b9J5dMYqicT8hHK8NazALbnY2tr3vZA3WEuiaK5FezPFNLTwL3KCpSmU2iaoKBvEhLRdfcv7HgY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/NicWxqLvw6Oo4xCPUS18ibPNM2jASOicS8picTHib097Qmuh96n4LGnJGWd0S8kmiaCbMXzrA7DGS01Qtq193xPJmHy2XtYDUiaprybzVFJN1SOll8/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/NicWxqLvw6Oqra00ic7tBA4EXxDebSYJLibA1zbv1RxSjovXWuxLwibkgDEYZkFkpsTcQbcraqOOiaeJakt6C2grX2YSe3nEdeAribXvfWroTahc8/640?wx_fmt=jpeg&from=appmsg)

权威性不用多“吹”。国家信息安全漏洞库（CNNVD），中国信息安全测评中心为切实履行漏洞分析和风险评估的职能，负责建设运维的国家信息安全漏洞库，对发现并报送的重大漏洞予以奖励。其一级、二级贡献奖每年评三次，只有高危漏洞才能入选。

**为什么我们能出手不凡？**

灵鉴AI代码审计平台稳定高效，加上AI赋能的自动化验证能力。针对二进制文件，支持自动化固件提取、自动化软件分析与逆向、自动化环境模拟与仿真程序验证；针对纯代码文件，覆盖主流语言代码审计能力，同样支持多种漏洞自动化检验与程序预处理，支持内部漏洞运营全流程落地。

[![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/NicWxqLvw6Oo97Rl8F6vIXw6zh1T4icicE5OZ6XDes8cHTIGiatRpBCceHHxa2kSR1ibxO2I0PnLbXK8elepV9zPEgxVgOc9aY4nlfXuHmJ1yYjE/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxNDY0MjMxNQ==&mid=2247542590&idx=2&sn=8252c140894bcd6df0b7d88dd0f6c754&scene=21#wechat_redirect)

研发至今，灵鉴经历了几十轮迭代更新，目前已经审计累计发现16000+漏洞

有图有真相👇👇👇

![](https://mmbiz.qpic.cn/mmbiz_png/NicWxqLvw6OroJS81cuWH3e0k6iabqo905ojVZvEGsiaic5QmTa5F89qjRrf49utlYQoLe4KOe2H9GqX5CTnYia06DlwvhrjcfoQzEYvbtnCiaLvo/640?wx_fmt=png&from=appmsg)

这次获奖，看起来轻轻松松、歪打正着，实则是水滴实验室团队成员无数次深夜鏖战与系统化协作的必然结果。武器库研发团队日复一日默默打磨“弹药库”，漏洞研究团队在实战中不断挑战和突破自我，产品团队敏锐捕捉市场需求，把晦涩的漏洞能力转化为客户愿意买单的亮点产品……每一位“攻防人”的汗水和专业，都凝聚在这两张“轻轻”的证书中。从一个智能摄像头中挖出高危漏洞，或许有偶然因素；但水滴实验室始终把前沿安全技术研究作为战略核心，以网信安全为己任，将一次次漏洞发现、武器打磨和产品转化沉淀为体系化攻防能力，最终获得CNNVD认证，这绝非偶然。

本次获奖不仅是团队实力的证明，更是天翼安全坚持技术报国、服务国家网络空间安全战略的生动注脚。未来，水滴实验室将持续专注漏洞挖掘、武器库研究与自研平台研发，坚定守护我国关键信息基础设施安全。天翼安全将始终肩负维护网信安全重任，持续深耕攻防对抗技术创新，为国家网络空间安全贡献电信力量。

供稿：安全技术研究实验室、集团SOC

排版：马子豪

编辑：陈师慧

校对：李雪

执行主编：田金英

主编：冯晓冬

**推荐阅读**

[![图片](https://mmbiz.qpic.cn/mmbiz_jpg/NicWxqLvw6OoyWnw75iakNQGskibf3CYJR6qrdlf67GkS5lSJuicSPJ9TtTlWqBRbcCj4XUT195G7tGttES3G4FJRkLkRSUb1Z5GRgEl1iaoibfI8/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxNDY0MjMxNQ==&mid=2247540380&idx=1&sn=7ec2ca604be6acfcf5ff49770fe0db83&scene=21#wechat_redirect)

**[喜报 | 水滴实验室勇夺智能渗透挑战赛全国亚军](https://mp.weixin.qq.com/s?__biz=MzkxNDY0MjMxNQ==&mid=2247540380&idx=1&sn=7ec2ca604be6acfcf5ff49770fe0db83&scene=21#wechat_redirect)**

[![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/NicWxqLvw6OoyHY3ccb4TCc2Ncve9G1z4OCHfxPRpcBRicRlm5CgFwGHA05UYN42EsXvgRxttdpiaRWDUhK0y3GacD46XUxGgm5qWicWOfFMhcs/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxNDY0MjMxNQ==&mid=2247542590&idx=1&sn=82fecdd9879a26356dcc5d7df8385c45&scene=21#wechat_redirect)

**[云啸 | 又获奖了！评委是真人，对手也是](https://mp.weixin.qq.com/s?__biz=MzkxNDY0MjMxNQ==&mid=2247542590&idx=1&sn=82fecdd9879a26356dcc5d7df8385c45&scene=21#wechat_redirect)**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/z7xPqlc0GbBZdrnibkon0HxogO9iazwQy5cqsw6fRdkPujrZZCuVnk7ywgyYA7yTfRIIkEXpdpDfQlkFMENO9P0Q/640?wx_fmt=gif&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/z7xPqlc0GbC3cIApABcXfaD12bCIj4WHOcdz4fokYeBmVOoaLxHlWaQ3kVGIStn99wpn50qfLrj2NlibFSnDkIw/0?wx_fmt=png)

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