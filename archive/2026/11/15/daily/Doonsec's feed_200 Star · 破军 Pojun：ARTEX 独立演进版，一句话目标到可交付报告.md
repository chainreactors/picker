---
title: 200 Star · 破军 Pojun：ARTEX 独立演进版，一句话目标到可交付报告
url: https://mp.weixin.qq.com/s/MkmVjKBCzGGBDLc2pGumBg
source: Doonsec's feed
date: 2026-11-15
fetch_date: 2026-11-16T08:43:27.123514
---

# 200 Star · 破军 Pojun：ARTEX 独立演进版，一句话目标到可交付报告

# 200 Star · 破军 Pojun：ARTEX 独立演进版，一句话目标到可交付报告

原创

效能跃迁实验室
效能跃迁实验室

效能跃迁实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 破军（Pojun）以原 ARTEX 最终定版为起点，于 2026-11-02 完成标识与路径切换，并在其后独立维护。

**系统接收自然语言任务目标后，由 planner 生成意图、worker 调用真实工具执行；HTTP 流量经 MITM 留痕，人工可纠偏与审批，输出绑定证据的 Word 报告。**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/w4WPiaObtlpy60jhtlTXrWKiawRuibWyjQ22icLQPNK6PRYJboTQsnMd3duUMuWfMaJybSeJoicvN4Ydqge2BJFZCDSr6jNbjUqE1nuRubCKMgXQ/640?wx_fmt=webp&from=appmsg)

---

## 开源地址

* **仓库**：https://github.com/chu0119/Pojun
* **Docker**：`ghcr.io/chu0119/pojun` · `xingchuan1314/pojun`
* **Release**：https://github.com/chu0119/Pojun/releases
* **许可**：AGPL-3.0

---

## 实测效果

控制台总览：任务、确认发现、资产节点与 Token 用量一屏可见（官方运行实例脱敏截图）：

![](https://mmbiz.qpic.cn/mmbiz_jpg/w4WPiaObtlpwj3AoccFxHvaGhqgjTHNVE3SMmXLTduEI3sJDQadWldsibAriaybejQLLsicEdS19hLXcJyJV6RGHmwAEAB5lKUMia24xo1QaPOeA/640?wx_fmt=webp&from=appmsg)

任务列表：目标进度与漏洞分布：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/w4WPiaObtlpxrwXryia9mB7iaAYhSiaTk7DmP5ibpDjLNBKw5IN54z7ywHTqiajibhvlTukSDcqNODgnloxoSxRJcjL0kRiawicVBMDia8vFY5viaOrg0o/640?wx_fmt=webp&from=appmsg)

任务详情：planner 态势研判与多 worker 会话内联可见：

![](https://mmbiz.qpic.cn/mmbiz_jpg/w4WPiaObtlpxvtlDJMxvib0gYvGFVjcdI4rl5Xe4icpkpUf1hV7ibWMrFobmkMCFwZulWyza1ypNvEwBRAQmnVTwjfRwBicfmBJP70G1t58cqHhs/640?wx_fmt=webp&from=appmsg)

漏洞详情：摘要、现场截图、PoC 与复测入口绑在同一条发现上：

![](https://mmbiz.qpic.cn/mmbiz_jpg/w4WPiaObtlpyMDLfTiaVUmseP1JoU1rNCQuCwvHFXH0fHjc8ougUVSxCAzNqOYal9SX1CwubHD9ZUglGjhW78N3rSdKRBft0UnQLDUIDROyo8/640?wx_fmt=webp&from=appmsg)

资产覆盖图：力导向布局，已测节点高亮：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/w4WPiaObtlpzZm6thPz0VscALES2VAcxafgM7pcq8nQLRLichbk93GwLPtTGAPrpCib1W6Mp55Dm3ticvJZicDwJQROiau8ljZK2Cs1ktDfnSJickY/640?wx_fmt=webp&from=appmsg)

README 给出的单机实测基线（真实授权项目数据，Kali 部署）：**12** 个任务、**56,000+** 次工具调用、**295** 个确认漏洞（严重 28 / 高危 140）、**2,752** 个资产节点。

---

## 它适合谁

* **授权靶场 / 本地隔离环境**：把「一句话目标 → 证据链 → Word 报告」整条链路跑通，观察 planner/worker 闭环
* **红队与 SRC 交付演练**：需要 MITM 流量证据、附件归档、19 类漏洞枚举折叠进专业级报告
* **平台能力对照**：关注漏洞情报（NVD / CISA KEV / GHSA）、宿主工具一键装齐、C2 出口三形态与人工审批闸门

仓库 README 写明：允许阅读源码与**本地隔离环境验证**；对线上系统发起扫描、探测或利用，超出其声明的使用范围。

---

## 使用方式（三选一）

依赖 **PostgreSQL**；探索需在 UI 配置 **LLM**（Anthropic / OpenAI / 任意兼容网关，支持三通道轮询）。默认控制台：`http://localhost:8787`。

**1️⃣ 一键安装脚本（README 推荐）**

```
git clone https://github.com/chu0119/Pojun.git && cd Pojun
sudo ./install.sh                    # 交互选择（默认二进制）
sudo ./install.sh --mode=binary      # 二进制 + systemd
sudo ./install.sh --mode=docker      # Docker Compose
sudo ./install.sh --mode=binary --with-tools   # 顺装常用渗透工具
```

**2️⃣ 预编译二进制**

到 Releases 下载对应平台 zip，解压后：

```
cp config.example.json config.json   # 填好 database 连接
./start.sh                           # → http://localhost:8787
```

**3️⃣ 首次启动四步**

1. 打开控制台 → 初始化管理员密码（≥8 位）
2. 「LLM 配置」配模型通道（实战建议 ≥2 通道并开启轮询）
3. 「宿主环境」一键装齐缺失工具（或安装时加 `--with-tools`）
4. 新建任务，给一句话目标

---

## 延伸阅读

* 破军 Pojun 仓库：https://github.com/chu0119/Pojun
* 安装与部署说明（README · 安装）：https://github.com/chu0119/Pojun#安装
* Release 与预编译包：https://github.com/chu0119/Pojun/releases
* norma（多 Agent harness 参考）：https://github.com/norma-dev/norma
* nuclei-templates：https://github.com/projectdiscovery/nuclei-templates

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/7OncKt4Qr9zqhxVYGj9l6Y3F1k75h3f7IBYroJUJnfhfxJGCYnYkkOEXsicDG171scGlicL58pmwTsFyR7pOCb0Q/0?wx_fmt=png)

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