---
title: 关于TpoScan v3.2.4：专业版和高级版
url: https://mp.weixin.qq.com/s/bkVlBbUzemPY_VOPWoDsvQ
source: Doonsec's feed
date: 2026-05-25
fetch_date: 2026-05-26T06:00:26.151542
---

# 关于TpoScan v3.2.4：专业版和高级版

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/op0UsH3vuJ1hicEcic4OG6M8FVmbn1tyevQ2ibkFe7dRKLQ8Lib0fpMpBafPibiawI96iaysibLofxBoxtoOYAO37FVBicH1Ursy22zkh6SibNLrV0Rtg/0?wx_fmt=jpeg)

# 关于TopoScan v3.2.4：专业版和高级版

原创

meeyou
meeyou

three安全之路

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

TopoScan v3.2.4 不是单纯加功能，而是把专业版和高级版的边界重新整理了一遍。

之前有个问题：专业版里虽然不能使用高级版功能，但帮助信息、补全脚本或配置入口里还能看到部分高级版参数。用户看到参数，就会以为能用；交付时也容易解释不清。

所以这次做了收敛：专业版只保留专业版该有的参数和入口，高级版功能只在高级版里出现。横向移动、分布式、弱口令批量验证 WebUI、高级告警、基础合规报告等入口，不再出现在专业版里。

---

## TopoScan 和 fscan 的关系：

TopoScan 确实是在 fscan 这类优秀工具的基础上继续扩展出来的。fscan 本身很好用，轻量、直接、上手快，如果只是临时扫端口、扫服务、验证弱口令，它依然很适合。

TopoScan 做的不是把 fscan 换个名字重新卖一遍，而是继续往这些方向扩展：

* 拓扑图
* HTML / Excel 报告
* 攻击路径分析
* 大网段扫描稳定性
* 专业版 / 高级版构建隔离
* 弱口令批量验证 WebUI
* 分布式扫描
* 告警、基础合规报告、历史趋势等高级能力

收费主要来自这些后续开发和长期维护，而不是基础扫描本身。

简单说：专业版偏“扫清楚、能交付”，高级版偏“看路径、看关系、能运营”。

---

## TopoScan 能做什么

![](https://mmbiz.qpic.cn/mmbiz_png/op0UsH3vuJ0gyl7t1v3D3jgoeQ7uy5muMplHWlR41kl0c9NoF2e69uhdwoB5JIUgyvH6KhHSULxXiaB64cQcvqYkvj1seGFX7NibAdPUu3VSs/640?wx_fmt=png&from=appmsg)

TopoScan 是一款偏内网安全评估和拓扑测绘的扫描工具。它采用“先扫描、后报告”的模式：

```
命令扫描 → 自动收集资产 → 构建拓扑 → 输出报告
```

扫描阶段会收集主机、端口、服务、漏洞、凭据、Web 指纹等信息；扫描结束后，可以生成拓扑数据、HTML 交互报告和 Excel 报表。

常见用法：

```
# 快速存活和基础资产探测
toposcan.exe -h192.168.1.0/24 -preset quick

# 全量资产扫描，包含常规 POC 检测
toposcan.exe -h192.168.1.0/24 -preset full

# 渗透测试模式，聚焦高危服务和弱口令
toposcan.exe -h192.168.1.0/24 -preset pentest

# 生成拓扑图和 HTML 报告
toposcan.exe -h192.168.1.0/24 -netgraph-report

# 生成 Excel 报表
toposcan.exe -h192.168.1.0/24 -excel
```

如果需要截图、操作系统识别、拓扑报告和 Excel 一起输出，可以组合使用：

```
toposcan.exe -h192.168.1.0/24 -netgraph-screenshot-report-os-excel
```

---

## v3.2.4 主要变化

这次主要改了这些地方：

* 专业版和高级版的参数边界重新整理。
* 专业版不再显示高级版专属参数。
* 高级功能继续通过构建标签隔离。
* 弱口令批量验证 WebUI 默认配置更安全。
* 告警、SOCKS5、数据库、导入接口等位置做了加固。
* 手册、发布说明和版本描述统一了一轮。

现在专业版里再传高级版参数，会直接按未知参数处理，而不是显示出来但运行时又告诉你不能用。

---

## 专业版和高级版有什么不同

![](https://mmbiz.qpic.cn/sz_mmbiz_png/op0UsH3vuJ0icI4b8SOScpo7eY5P8PwetWUjEIXzniaKMHlztHJ5BrjOLwheQ9MGCphqxH8LliccI5eJxmZIPUXTia7ywc4Wg4nvlSZaSL993z0/640?wx_fmt=png&from=appmsg)

当前版本里，专业版大约 143 个参数，高级版大约 164 个参数。

但重点不是参数数量，而是高级版多出来的是“扫完之后”的分析能力：攻击路径、横向关系、历史变化、告警联动和大规模环境使用。

---

## 专业版适合什么场景

如果你的需求主要是这些，专业版就够用：

* 内网资产梳理
* 端口扫描和服务识别
* Web 指纹识别
* 弱口令验证
* 基础 POC 检测
* 拓扑图、HTML 报告、Excel 报告输出
* 安全服务项目交付

专业版更适合“扫清楚、整理好、交付出去”。

---

## 高级版主要多在哪里

高级版不是简单把参数列表拉长，而是增加了几块更深入的能力。

### 横向移动和攻击路径

普通扫描能告诉你哪些主机开放了哪些端口，哪些服务可能存在弱口令。

高级版会继续往下看：这些凭据有没有可能复用，哪些主机可以作为跳板，哪些路径可能接近关键资产。

也就是说，它更关心“扫到这些东西之后，下一步能怎么走”。

### 高级报告和合规输出

高级版会保留更多适合正式交付和复盘的内容，比如基础合规报告模板、攻击链验证结果、Docker / K8s 初步风险线索识别、凭据情报分析结果、历史扫描趋势等。

这里的 Docker / K8s 分析主要基于扫描结果做初步辅助判断，包括 Docker/K8s 相关端口、API 暴露、TLS 情况、部分 K8s endpoint 和容器逃逸线索，不等同于完整 CSPM / CNAPP 平台。基础合规报告也是基于扫描结果生成检查项和评分，不等同于完整等保、ISO 或 PCI 合规系统。

这些内容更适合护网前排查、攻防演练复盘、企业内部整改、安全服务公司交付等场景。

### 告警联动

高级版支持 Webhook、Slack、钉钉等告警方式。

这不是为了“看起来功能多”，而是因为很多企业环境里，扫描结果不能只躺在本地文件里。高危结果、新增资产、新增风险，最好能进入已有的通知和处置流程。

### 分布式和弱口令批量验证 WebUI

TopoScan 里的 WebUI 不是整套程序的 Web 控制台，也不是通用资产管理平台。

它主要用于弱口令批量验证，方便导入任务、执行验证和查看结果。

分布式扫描则主要面向大网段、多区域环境。目标多、网段多、机器多的时候，只靠单机命令行会比较吃力，这时分布式会更有意义。

---

## 适用场景怎么选

| 场景 | 推荐选择 |
| --- | --- |
| 快速资产普查 | 专业版 + `-preset quick` |
| 常规渗透测试前期信息收集 | 专业版 + `-preset pentest` |
| 客户交付报告 | 专业版 + 拓扑报告 + Excel 报表 |
| 大网段、多区域扫描 | 高级版 + 分布式扫描 |
| 攻击路径和横向分析 | 高级版 |
| 告警联动、基础合规报告、历史趋势 | 高级版 |
| 弱口令批量验证任务管理 | 高级版弱口令验证 WebUI |

---

## 后续规划

后续会优先做两个方向。

### 资产指纹库 + 自动化利用链

把资产指纹、CVE、POC 和利用建议关联起来，帮助用户判断哪些风险更值得优先验证和整改。

### AI 驱动攻击路径推荐

结合拓扑、凭据、漏洞、服务和资产重要性，推荐更值得关注的攻击路径。

拓扑图也会继续增强，重点包括攻击路径高亮、风险热力图、证据面板联动、时间维度拓扑和信任关系图。

目标不是把图画得更复杂，而是让用户更快看懂：风险在哪里，路径怎么走，哪些资产最该优先处理。

---

## 最后

只需要轻量扫描，用 fscan 这类工具就很好。

需要拓扑、报告、路径分析和更正式的交付，再考虑 TopoScan。

专业版把扫描和交付做好。

高级版把分析、联动和长期使用补上。

TopoScan目前已发布到V3.2.4了，专业版是免费的！！后续我们将根据各位师傅的反馈持续更新迭代，欢迎多提宝贵建议，让工具更贴合实战需求。

更多功能详情请参考 TopoScan 使用说明书，公众号后台回复“toposcan”即可获取工具下载地址，也可加入群聊探讨功能。

往期文章Toposcan

[TopoScan网络拓扑扫描利器/扫描 + 可视化一键搞定](https://mp.weixin.qq.com/s?__biz=MzYzMjY5MDM3OA==&mid=2247483883&idx=1&sn=a1e59dcd6d1bef278937772ad1e0d58f&scene=21#wechat_redirect)

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/a0a57o0RVEalyLvktrfycvia9iahgHmHJsOp1d9iaicZ1tRYM5fL5RiclgBEztK88zfvAeVvcWSsLlZiagIGNZXjHgjA/0?wx_fmt=png)

three安全之路

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/a0a57o0RVEalyLvktrfycvia9iahgHmHJsOp1d9iaicZ1tRYM5fL5RiclgBEztK88zfvAeVvcWSsLlZiagIGNZXjHgjA/0?wx_fmt=png)

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