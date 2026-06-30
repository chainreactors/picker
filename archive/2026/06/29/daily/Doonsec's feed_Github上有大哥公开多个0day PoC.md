---
title: Github上有大哥公开多个0day PoC
url: https://mp.weixin.qq.com/s/s-zmVtTIsXPSsgu973fyrg
source: Doonsec's feed
date: 2026-06-29
fetch_date: 2026-06-30T06:07:45.456845
---

# Github上有大哥公开多个0day PoC

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ft6csZH0gNVkia7s81KofiaISdanWDrc5UcIG7PdBy2GNZdeemeCaDiaDsKaJdzuiaIVwmIWQe972z04TG4H7zkoKPHM0a6t9kPOFxXoHleic47w/0?wx_fmt=jpeg)

# Github上有大哥公开多个0day PoC

助力行业的
助力行业的

李白你好

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

近日，GitHub 用户 **bikini** 维护的仓库https://github.com/bikini/exploitarium迅速引起安全社区的广泛关注。该仓库被描述为“**A single archive of public exploit PoCs and vulnerability research writeups**”（公共漏洞利用 PoC 和漏洞研究报告的单一归档库）。截至目前，已收录多个热门软件和工具的 PoC，包括 7-Zip、AnyDesk、c-ares、Docker、FFmpeg、Firefox、Ghidra、Gitea、ImageMagick、libssh2、Nmap、OpenVPN、PHP、RustDesk 等。

![](https://mmbiz.qpic.cn/mmbiz_png/ft6csZH0gNWPag1Ficffu7owZIMSpygpWEwvxEEHaoJRvd9u3dGmI5TALd6B4tC935icqAicZb1daib8icLM655EQvK1DZCmfMC2om0K7iadf8Lvk/640?wx_fmt=png&from=appmsg)

## 仓库特点与维护者立场

根据仓库 README，该项目的主要目的是**吸引更多人进入安全研究领域**。维护者明确表示：

* 在发布时，这些漏洞**尚未被官方报告**（none have been reported）。
* 鼓励研究者自行报告并申请 CVE，自己不抢功（“Feel free to report them yourself and take credit for the CVE”）。
* **强烈呼吁不要滥用**这些 PoC，仅用于合法研究和学习。

仓库中许多 PoC 采用自包含文件夹形式，保留了原始 README 和文件结构，便于研究者快速复现。同时，维护者还提供了 **cves.md** 文件，记录了基于该仓库研究已分配的部分 CVE（如 CVE-2026-58xxx 系列）。

维护者在 README 中分享了其研究方法：大量使用 AI 辅助 fuzzing（特别是 GPT-5.5-3-Codex-Spark），但 PoC 核心代码多为手动编写，并强调良好的 harness 和人工 oversight 远比模型本身重要。这也反映了当前 AI 在漏洞挖掘中的辅助作用。

## 部分亮点 PoC

![](https://mmbiz.qpic.cn/mmbiz_png/ft6csZH0gNWyLria4bHGf9MrRYdGicJCOWTMa99xdvQzD1eTRFJ5hlRkuPKpgGYClTiac8r9kqOxuH5duA5VpuulK7wqT6g5A82DFx6PWicpVv8/640?wx_fmt=png&from=appmsg)

* **libssh2** 相关：包含 CVE-2026-55200 PoC 以及 publickey list 计算 PoC。
* **FFmpeg**：RASC DLTA 计算 PoC，已关联 CVE。
* **c-ares**：TCP UAF 计算 PoC。
* **Ghidra**、**Nmap**、**ImageMagick**、**RustDesk** 等工具的 RCE、LPE 或信息泄露 PoC。
* **Docker**、**Gitea** 等容器/DevOps 工具的逃逸或配置利用链。

仓库更新活跃，最近几天仍有新 PoC 加入，并承诺“通常每天一个新 PoC”。

## 总结

Exploitarium 体现了开源安全社区的活力——一位研究者通过系统性工作，将多个高质量 PoC 集中分享，推动了漏洞发现与修复的良性循环。它不仅是 PoC 仓库，更是学习高级漏洞利用和研究方法的宝贵资料。

感兴趣的朋友可以直接访问：**https://github.com/bikini/exploitarium**。

## 网络安全情报攻防站

**www.libaisec.com**

综合性的技术交流与资源共享社区

专注于红蓝对抗、攻防渗透、威胁情报、数据泄露

![](https://mmbiz.qpic.cn/mmbiz_jpg/ft6csZH0gNWpEiaFr3wWY8fDBILagqESxOXfedEEz6Nv71pVTribvpoxYrMw6garZ9R9xIquhEbhoJRUvC216w6k00EbaTCxqez9Bzgj2A0Yg/640?wx_fmt=jpeg&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/XoIcX2HtlUAuS65pf9u98YWJSdI6kWZ64ziasaVXOFXiabEV2AuCY8yGygtKHicEFVvHnw3bzhsDXBB3DQIiaNhOiaQ/0?wx_fmt=png)

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