---
title: 【安全圈】全新幽灵BTR漏洞曝光：绕过主流防御窃取Linux内核高权哈希
url: https://mp.weixin.qq.com/s/BJ6xcb874rx0okXA8LODEQ
source: Doonsec's feed
date: 2026-09-30
fetch_date: 2026-10-01T07:57:33.916099
---

# 【安全圈】全新幽灵BTR漏洞曝光：绕过主流防御窃取Linux内核高权哈希

# 【安全圈】全新幽灵BTR漏洞曝光：绕过主流防御窃取Linux内核高权哈希

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

漏洞

**事件核心要点：**来自 VUSec 与比萨圣安娜高等学院的研究团队正式公布了新型 Spectre-v2 微架构漏洞，代号 **Branch Target Reuse（BTR，分支目标重用）**。该攻击首次证明：现代处理器的预测机制即便在自修改代码重构后，依然保留过期的间接分支预测条目（BTB）。攻击者可利用 JIT 即时编译器的内存回收周期，构造“瞬态释放后执行”原语，在数分钟内从开启全套防御的 Linux 内核中完整泄露 Root 密码哈希。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyGNiaHgebdRaJpCUPB5777UDZqFoIqU97icicnhBZqQ7WlQsCw4NVlaI4RJd1Bib0F31f9Mp7H5Zem48dROrggTFibZkx5TomVmpAgw/640?wx_fmt=other&from=appmsg)

## ⚡ 颠覆传统假设：从“空间劫持”转向“时间维度重用”

自 2017 年 Spectre（幽灵）漏洞被揭露以来，业界针对 Spectre-v2 的主流防御机制均建立在一个基本前提上：攻击者必须实施“空间维度的目标篡改”，即诱导 CPU 将间接跳转分支重定向至内存中的另一个恶意 Gadget 片段。

然而，BTR 打破了这一固有安全模型。研究团队指出：

```
[传统 Spectre-v2 假定] 分支预测跳转: 从地址 A (合法) 错误诱导至地址 B (恶意代码) [硬件固有盲区] 现代 CPU 处理自修改代码 (SMC) 时，仅保证架构级内存一致性，并不自动清除分支目标缓冲器 (BTB) 的陈旧条目 [BTR 时间维度重用] 1. 攻击者在 JIT 内存块中用同一间接分支进行常规“训练”，BTB 固化跳转目标 2. JIT 引擎释放该代码块 (Free)，该物理内存随即被重新编译分配填入全新指令 3. 原分支预测条目未被清空，在全新代码上下文上触发“瞬态执行 (Transient Execution)” 4. 导致代码在未对齐的非法偏移量处执行，跨边界读取特权缓存
```

在这一过程中，跳转指令自身的位置与目标地址在空间上完全未变，改变的是**目标地址处机器码的实际含义与上下文**。这种“时间维度的分支重用”使得针对跨地址跳转的各类硬件级过滤手段（包括针对 Training Solo 漏洞的 CVE-2024-28956 与 CVE-2025-24495 防护方案）全部失效。

## 🔍 攻陷三大 JIT 引擎：全补丁系统数分钟失守

任何具备即时编译与动态代码生成特性的运行环境均受该硬件缺陷波及。研究人员针对三款工业级基础设施进行了实测验证：

* **Linux 内核 cBPF JIT**

  ：通过向内核注入受限的低权限 BPF 过滤指令，诱发内核级 JIT 生成与重构，成功实施跨特权级侧信道窥探；
* **Mozilla Firefox SpiderMonkey 引擎**

  ：普通网页 JavaScript 脚本即可驱动浏览器 JIT 缓存抖动，突破沙箱读取宿主进程内存；
* **GraalVM 高性能多语言虚拟机**

  ：在多租户运行环境下同样展现出可利用的瞬态释放执行通道。

在部署了全部官方补丁并开启默认硬件防御的真实 Intel 生产服务器上，研究团队构建的端到端 PoC 攻击链仅耗时数分钟，便无视内核隔离机制，完整重构出了 Linux 系统的 Root 密码哈希值。

## 🛡️ 厂商响应与工程级缓解难点

与一般应用层漏洞不同，微架构侧信道漏洞的根除通常需要芯片级微码更新或极高代价的性能损耗：

📦 缓解建议与架构防护权衡：

• **JIT 代码缓存强行失效**：在运行时环境释放旧代码块或复用物理内存页时，必须显式触发微码层级的 BTB 刷新指令，但该操作会对 Java/V8 等高并发 JIT 性能造成明显回退；

• **内核 BPF 严格审计**：生产环境严格关闭非特权用户调用 eBPF/cBPF 的权限（`sysctl -w kernel.unprivileged_bpf_disabled=1`），彻底切断低权限本地提权通道；

• **浏览器跨站进程物理隔离**：启用最高等级的 Site Isolation，防范恶意 Web 页面通过瞬态侧信道窃取同源进程中的 Cookie 与身份凭据。

***END***

阅读推荐

[【安全圈】看张图片就中招？苹果的这个漏洞你一定要看](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079161&idx=1&sn=d33e558e6c0b63eff92e7b87e35da4f9&scene=21#wechat_redirect)

[【安全圈】OpenAI叫停大模型训练：Agent突破沙箱偷连外部服务](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079161&idx=2&sn=afb4262b4d676f9ed2b6da390755c347&scene=21#wechat_redirect)

[【安全圈】MCP官方SDK高危漏洞：恶意服务可盗取OAuth凭证](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079161&idx=3&sn=704f24afc846aa0d28375d6b5f4d600a&scene=21#wechat_redirect)

[【安全圈】苹果崩了](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079150&idx=1&sn=f25dd80dbe08777b632a88ab45425b84&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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