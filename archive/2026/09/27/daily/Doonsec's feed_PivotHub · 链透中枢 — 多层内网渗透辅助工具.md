---
title: PivotHub · 链透中枢 — 多层内网渗透辅助工具
url: https://mp.weixin.qq.com/s/0toAaeDj0VQyrPoJY2YX4Q
source: Doonsec's feed
date: 2026-09-27
fetch_date: 2026-09-28T07:54:26.464677
---

# PivotHub · 链透中枢 — 多层内网渗透辅助工具

# PivotHub · 链透中枢 — 多层内网渗透辅助工具

ProbiusOfficial
ProbiusOfficial

陌笙不太懂安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

免责声明

```
由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号陌笙不太懂安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉，谢谢！
```

工具介绍

PivotHub（链透中枢）是一个面向CTF竞赛、授权靶场和教学演示场景的多层内网渗透辅助工具，它通过本地Web面板将资产探测、Shell管理、终端固化、代理链路编排（目前支持chisel/frp/Neo-reGeorg）、凭据与Flag收集、时间线记录及复盘导出等功能整合在一起，帮助渗透测试人员系统化地管理从入口打点到多级内网横向移动的完整流程，并生成结构化的Writeup报告。

工具使用

### 环境要求

| 项 | 要求 |
| --- | --- |
| Python | 3.10+（本机实测 3.13） |
| 依赖 | pip install -r requirements.txt（FastAPI / Uvicorn / SQLAlchemy / Pydantic…） |
| 可选 | Docker（跑 scripts/lab/ 靶场做全流程真机验证） |
| 浏览器 | 任意现代浏览器（前端零构建，Vue / ECharts 已本地化于 assets/vendor/） |

三步启动（后端一体化托管前端）

```
pip install -r requirements.txtpython run.py            # 等价 python -m pivothub，监听 127.0.0.1:8000# 浏览器打开 http://127.0.0.1:8000/
```

后端以 StaticFiles 原样托管前端，/api/\* 与 /ws 同源，**无需另起静态服务器**。 数据全部来自本地 SQLite；后端不可用时界面显式报错。

前端资源已本地化（离线可用）

`index.html` 引用的是 `assets/vendor/` 下的 Vue 3 与 ECharts，**不依赖 CDN**，断网环境可直接使用； ECharts 缺失时仅拓扑图降级，其余界面不受影响（`app.js` 另有 Vue 加载失败提示）。

界面预览

阶段看板 · 进度总览与链路健康

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTJUBpA9fJGG1TLbb4KNJf5SA5vfr6VepQSjxcnXDZALU884MLx2gLSGAa8Cvddru3icSvyWtEmNU3jO05o65rSmqwID6AF5lVE/640?wx_fmt=png&from=appmsg)

网络拓扑 · 跳板链（节点 = 主机，边 = 代理链路，按网段分区着色）

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQEmv2O3gj0hj9bN4UAxazolibEnWTNQbl9xXqz2prrdvDjvxbzb3HgPQKxkHkZDEy4iaGWtwERNsOkSmngficAFXsr69Vmia4vatM/640?wx_fmt=png&from=appmsg)

资产列表 · IP / OS / 层级 / 权限 / 服务，支持扫描导入与移除

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQYdwpd63gw3rd7mM7r9sEqlsr2U8qVyKNE64yk8hSRNIibhhSPRvGW6LoL9ibMO5v553vBibAib3VAXLcMicl6FEibsObJSeNY2vx2s/640?wx_fmt=png&from=appmsg)

Shell 管理 · 会话登记 / 心跳 / 虚拟终端 / 一键提权

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSnNYYux6Tc4Bqfoc8va0kACZ7rjjhB5RVFiaicibabHCmKVknLOBLIUWnr6N0T3UzYMegBsuQOBk4Dzauls2ddCpVu9SeZq04oVA/640?wx_fmt=png&from=appmsg)

SSH 会话 · 独立纳管 SSH 主机，与 Shell 管理并存

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRS7Jf9e1yklgsgCunFhI10Zj1Y0kxeiaibDmYVnRACzAzSvKUI51TwfTaqXecLL7cUctVqQsYBUStYFm9n1HB2wORljLVqZYnyE/640?wx_fmt=png&from=appmsg)

资产探测 · 内网信息收集 + 内置 fscan 扫描 + 结果导入

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSuMy33want8qZV2DSQQibyzBexABmJTdicb5KB9gXWOPiagsIicC8j9YdqT4qrH7ia5QgeHVGrj9ibzj0FWtCJlXVfF3YHs8sltypdE/640?wx_fmt=png&from=appmsg)

反弹 Shell · 攻击机监听 → 靶机回连 → 自动登记会话

马生成器 · PHP/JSP/ASP/ASPX 一句话马与自定义加密马 + 写马姿势速查

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTe86tasmRnZibbZKDaialBKnia0nbS8D2dxY3uLPWJ03m50dYHEqd3pmPP1gcj2BcWjZ4dIVPf9PWnVEou837Y4Wm24ibqwYau4bg/640?wx_fmt=png&from=appmsg)

代理编排台 · 出网探测 → 隧道选型 → 部署命令 → 健康看板

凭据库 · 账号 / 哈希 / 密钥登记 + 跨层复用推荐打分

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSM2ypJWFqiayian5LS6duxebltjcrEBmtibKeJN2B3V9J98DgibXvOKXichGibZ10niajPrZlT9IIhFNxkuFUWcGVvb6tWsKUTRgIZKM/640?wx_fmt=png&from=appmsg)

Flag 收集墙 · 卡片墙 + 进度环 + 阶段进度 + 一键复制提交

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRP7ULx6qXtQw72GliaWLJD5SATia6icXROzicaONyGLc3xogmRSjFegqUibpV146YToh6CDMSEjHa7bibkicclgpX1wV2N8uPWmEDPPE/640?wx_fmt=png&from=appmsg)

操作时间线 · 自动事件 + Markdown 笔记，可回溯每步命令

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSHnHKulib131FLh8YsUxk98iaxwGBfw6DRp6ZeXUgc6RpWKgoc8Pr4kgyBKhWYibib3kVExMJgyzsg9bcic4OpFlJtXz4ApCrNIxxM/640?wx_fmt=png&from=appmsg)

命令速查 · 场景化命令模板 + 变量替换 + 提权智能匹配

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboR4TwAW5plTNUNQMkqSc9r0d2TvGILPOiaiaJ2mWm8QagZvcSMw8lcGmEfygLia2luJ8doxbo4BBMa4ejTNX6J14TcHTSoWpwicvK8/640?wx_fmt=png&from=appmsg)

插件市场 · 数据插件（命令库 / 技法 / 提权规则），安装即并入视图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRE3uQzSxjJ7mlmFVkXdpQFgibmUZjicF0CuzREtB7UHeUODQdT8y4QbmesJyg47Fyldg1SES3fTjw3xoibDvpF2c4HnKkkrpazoU/640?wx_fmt=png&from=appmsg)

复盘导出 · Markdown / HTML / JSON 三格式 + 实时预览

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQYPiad3awWu2DRMXnQuN0Bn7Q6p9xdwc8xJyHuctKzEENMticBRB6bibG9AzSdYHKfxncTUhbLFq45hicpkOLkbp5LF3KYzyFouQM/640?wx_fmt=png&from=appmsg)

功能一览

| 模块 | 内容 | 状态 |
| --- | --- | --- |
| M1 | Webshell生成、Shell管理、虚拟终端、文件管理、自定义马回传、写马辅助、终端固化 | 全部 ✅ |
| M2 | 出网探测、隧道推荐、两档自动化、多级编排、Socks映射、proxychains/msf联动、隧道类型覆盖 | 多 ✅，Adapter 3/8、断链重拉 🟡 |
| M3 | 资产列表与探测、拓扑图、凭据库、时间线、网段管理 | 全部 ✅ |
| M4 | Flag墙、Markdown笔记、计时看板、Writeup导出 | 全部 ✅ |
| M5 | 命令速查库、提权智能匹配 | 全部 ✅ |
| M6 | SQLite多项目、三格式导出、项目打包 | 多 ✅，打包仅界面 🟡 |

工具链接

```
https://github.com/ProbiusOfficial/pivothub
```

**后台回复加群加入交流群**

**广告：****cisp pte/pts &nisp1级2级低价报考**

**陌笙安全纷传圈子+陌笙src挖掘知识库+陌笙安全漏洞库+陌笙安全面试题库****简单介绍****（****加入纷传圈子****送****知识库+漏洞库+面试题库****）**

如果觉得合适可以加入,圈子目前价格39.9元，价格只会根据圈子内容和圈子人数进行上调，不会下跌。。。

**圈子福利**

**edu漏洞挖掘1v1指导出洞**

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRKQWHxLsRrPqpqdiceX76d7yExQIyOqFmmJAfHQh7qzKvPc2V5z6iaa0RY6Ib8AsGvgS5MKkAk5aaHnJBaSnI10LDKQYMLcQMmg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboR8pnPeapLBK4Jsa4ufCvFoGL66t7PKeZyA3AjNxsObjtnCibN2gzGX7NMS7Wo5sj3YYL2iboeRuQDcWqiapc8xuo5fticoBG4DsyY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRKIBNIQIVicRWJLbyGRmg92vPzc8375PJpcYVvfywzwqnaeBicZuEbfvuic9KRdjwkahSDic5VqrH2Mb4NkqtkADl5HLIh8gPex60/640?wx_fmt=png&from=appmsg)

**skill+grok辅助挖掘某企业sr****c****实战效果，能出但是重复多，agent独立挖掘也可以，见仁见智，看个人习惯，好的模型是最重要的。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQwyn779TTwY7vZkePQCL8k3K8dYxNdyzfgADL4dJcNUvpmodLeDVCZ6xDC4RJXEBmO2tcWqgUNdTVicKTW0jpdsg7X6xwP5gIQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQnIqagDL2A4BUIXrib9YVmATWuaIDqETqYd9ToHib52mDyoMyqc6Wzh733FRnbsDsGgey7B8s8jr72UtkPY6ich58niaPJqoItKcE/640?wx_fmt=png&from=appmsg)

**企业src边缘&核心资产实战效果&&有重复但是证明好模型+AI确实够用**

**（图片仅供参考，我出不等于你出，见识**到**ai神力即可，多去用AI!!!）**

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboT1YNI9U6r6NMO4UMUBROoWeC4XQC4Dge94ODZ7tXY6tbxqb3IJoghve0u1SfkygE5UJ5HTdUBvLZKrn5ps13F71piax5dlHnOE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTGjdxKy4nllaLXIznTvRqicichITccuB8psYFRYakw6ViauCk6iccziahfPw4fnrqhyCp7Zkq7lRI0DOicyrZlNyicYibTVibfGFZVaG0c/640?wx_fmt=png&from=appmsg)

**不是P图,单洞1.2w记录**

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQQpQdR2Ttwqxibyr75Is0kBG2N2tLYQIaau7SS278oyQ4RDpNScviaMt4wtlfgDCibE05WgoMhE5kZUrP8ciaYIdnxA594wsmoAAs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSRn2EsfFkA5mG6dcn7JLQMroc2dy3EQb3ueY2Cspd0WYgicXEnSF68UD43nNd4plkxmkTpEOh2kkQMEWZZIjE0ibA8r1q4IfiaxI/640?wx_fmt=png&from=appmsg)

**陌笙src挖掘知识库介绍（内容持续更新中!!!)**

```
信息收集(主域名信息收集,子域名信息收集等&会永久提供fofa-key助力)弱口令漏洞&未授权访问漏洞挖掘任意文件读取&删除&下载&上传漏洞sql注入漏洞url重定向漏洞csrf&ssrf漏洞挖掘XSS&XXE漏洞挖掘等等常见漏洞cors&目录遍历&越权漏洞挖掘EDUSRC(证书站挖掘案例分享&edusrc挖掘技巧分享)CNVD挖掘技巧分享&实战案例报告编写公益漏洞挖掘（公益src挖掘漏洞分享&提供补天1权重资产）SRC挖掘实战(针对各种常见功能总结的常见测试思路等快速提升)经典常见Nday漏洞(常见中间件&以及各种常见框架)复现云安全相关漏洞挖掘（云key扫盲&云存储桶&快速识别云环境&云攻防）AI相关学习（AI基础&AI代码审计实战测试&webLLM攻击等）APP&小程序漏洞挖掘等各模块不在一一介绍
```

信息收集

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTu9DGyTubluhYicFynwVBKa4V06sDfEVKOyk5Q4ghZzLMDAuLb1M1oR4RJumGWrADPapFjTrOjpksKQ8q0YYCnl3ZWLof8Knzg/640?wx_fmt=png&from=appmsg)

src挖掘基础

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboR45bibbJEb28a1gS5yth3r5HyOsgPiaOUHHYriahZyIyrk0LMOsHW4VoDibyBRibTNzptGiaLWX62UwykicwvbxCJPopvklqiaxML8lS8/640?wx_fmt=png&from=appmsg)

src挖掘实战

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTKWnTsN6CXf3djhXIlMKNRjVmJn3g5b23ur9E6Cx3O68f0hXVjCiaj8J4RYeTGBecqf1k99phG0ice2wtd5lKgR46OeqeLQfMpk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRbZ1HYm7R7YEiaxRVQibGWyricx9l7HpGjS4ZfWRdlft8iacwkpzYyZfmYEkWdJgYRORPkNFR6dADR5MyE524tWX6cAwN8MmrCZu0/640?wx_fmt=png&from=appmsg)

edusrc

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQVVlTXhibjR8UiakZBQicXRZrQ7hdoOz5G8MQrcuDBGbqJdO0kIz6R9IU4ObAeOiabT8pr6lc7jibdIkKoTjiaXNHPLAwAB3BV2UvLM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSCrvarBbzP4L9kS6P0LVH9JMdmcbFDKiaicHqMFgTxq3x4iatjDJQicmc7NPC14C9Fk3icFjrouSgNVaN8Byuf0C0Iq9O6D1XPvFvY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRALwXmgZ4mh2LW0RdicrKjBCP7P1iaF14G0Eq2v3KRnTJORpwXZlF58WEz6QicxLJpyJaA5i...