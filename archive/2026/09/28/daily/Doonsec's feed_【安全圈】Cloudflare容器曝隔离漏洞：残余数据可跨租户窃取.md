---
title: 【安全圈】Cloudflare容器曝隔离漏洞：残余数据可跨租户窃取
url: https://mp.weixin.qq.com/s/WWEGmOhvdJFK54IXpsgErg
source: Doonsec's feed
date: 2026-09-28
fetch_date: 2026-09-29T07:39:42.443088
---

# 【安全圈】Cloudflare容器曝隔离漏洞：残余数据可跨租户窃取

# 【安全圈】Cloudflare容器曝隔离漏洞：残余数据可跨租户窃取

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

漏洞

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyGef5eLj7Vm6haWpwiaLvtnhuwEcSSHvdrkb3BT6UV5CgLMX5j2ksoEGJicBcnJMtMhOib34ibibq6O77FqaDDI72EH2ia4MXGPFhZts/640?wx_fmt=jpeg&from=appmsg)

**核心要点：**安全机构披露了 Cloudflare Containers（容器）与 Sandboxes（沙箱）运行环境中存在的一处跨租户数据隔离漏洞。拥有 Workers 付费账户的攻击者可在底层共享宿主机上，恢复其他租户容器销毁后残留的敏感存储数据。该问题根源在于共享存储池分配时跳过了“物理块清零（Zeroing）”操作，导致 SQLite 数据库、环境凭据与浏览器配置处于未擦除状态。Cloudflare 目前已在云端完成全网热修，客户无需手动介入。

## 🚨 共享宿主机下的隐形穿透：4KB 写入引出 60KB 历史数据

Cloudflare Containers 允许开发者在 Cloudflare 边缘基础设施上直接运行微服务、异步数据处理任务以及 AI Agent 代码沙箱环境。为了提高物理资源的周转效率，不同租户的容器会被动态调度到同一台物理宿主机上运行。

来自安全科技企业 Accomplish 的研究员 Oren Yomtov 在通过 HackerOne 提交的漏洞报告中揭示了其存储层的致命漏洞：**底层共享存储池在回收并重新分配物理存储块时，配置为了“跳过块清零”**。

```
[流程1: 租户A业务结束] 租户A的容器销毁 -> 根磁盘精简卷 (Thin Volume) 被释放 [流程2: 物理块未清零] 包含A数据的 64 KiB 物理块被直接退回共享可用块池 (Pool) [流程3: 租户B申请写入] 恶意租户B启动新容器，向未使用的磁盘扇区写入 4 KiB 填充数据 [流程4: 触发底层分配] 存储引擎按 64 KiB 粒度将此前属于租户A的物理块映射给租户B [流程5: 泄露历史残余] 4 KiB 被覆盖，其余 60 KiB 仍保留租户A原始明文，租户B直接读取
```

在标准的虚拟化隔离模型中，未清零的存储块会被直接复用。由于攻击者仅写入了 4 KiB，剩余的 60 KiB 空间并未被空字节或随机数据覆写，攻击者借此绕过了租户边界，直接读取到了历史分配给上一位客户的原始磁盘扇区。

## 🔍 实测捕获成果：结构完整的 SQLite 库与环境变量

安全团队在受控验证环境下进行了多次调度测试，统计结果表明该漏洞在生产环境中具备极高的复现确定性：

* **高达 75% 的捕获率：**

  在发起的 24 次容器调度部署中，有 18 次成功在未写入区域读取到了其他租户留下的数据残余；
* **跨节点普遍存在：**

  测试覆盖的 22 台底层物理计算节点中，有 20 台均能稳定复现这一泄露现象；
* **失窃资产极度敏感：**

  提取出的碎片中包含了清晰的文件系统目录树、Chromium 浏览器会话配置、存放 API 密钥的 `.env` 配置文件，甚至包括结构完好、可直接挂载解析的 SQLite 数据库页。

**影响范围边界评估：**
Cloudflare 官方强调，该攻击属于被动恢复历史残余，攻击者**无法主动指定窃取某一特定目标企业的数据**，也无法读取当前正在挂载运行中的活跃容器磁盘，更不具备篡改其他用户数据或破坏业务负载的能力。

## 🛡️ 官方处置动作：存储池重构与全网快照清退

9月4日收到安全报告后，Cloudflare 工程团队在两周内完成了云端整改，并于 9月19日 全面完成治理闭环：

1. **强制清零逻辑回滚：**

   彻底移除了存储池中允许跳过块清零的配置参数，所有释放块入池前必须完成物理擦除；
2. **轮换现有容器磁盘：**

   退役并重建了所有历史创建的精简卷容器磁盘资产；
3. **清理快照残留：**

   清空了可能包含旧映射关系的磁盘快照缓存；
4. **历史日志审计：**

   追溯历史遥测与访问日志，未发现该漏洞被恶意黑客滥用的迹象。

## 💡 对云原生与 AI 沙箱架构的安全启示

此次漏洞直接波及了 Cloudflare Sandboxes——一个专门被宣传用于“安全执行不受信代码与 AI Agent 自主生成脚本”的隔离环境。这一事件为当前火热的 Agent 基础设施架构敲响了警钟：

* **性能优化与安全底线的冲突：**

  存储层为了降低 I/O 延迟而跳过清零，往往是多租户云环境发生“幽灵泄露”的源头；
* **数据销毁的彻底性审计：**

  对于部署在公共云上的自动化 AI 任务，务必在应用层做好敏感临时文件（如数据库、Token 缓存）的主动加盐加密，避免单纯依赖云服务商的基础设施隔离。

***END***

阅读推荐

[【安全圈】OpenAI 研究代理曾将用户图片传到第三方图床，已发现 53 次](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079129&idx=1&sn=7df0283a6c5d51694b17203ac0b35c59&scene=21#wechat_redirect)

[【安全圈】两个恶意 GitHub Actions 曾重新上线，旧工作流需排查](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079129&idx=2&sn=df0e0e05d2843681315bf1ebf88e985d&scene=21#wechat_redirect)

[【安全圈】SharePoint 代码注入漏洞出现实际攻击，已发布补丁仍需核对](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079129&idx=3&sn=8eab1210d63abf0b373ad59028f7c1ad&scene=21#wechat_redirect)

[【安全圈】暴露的 Docker 接口成攻击入口，Carbonato 借 AI 代理控制主机](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079118&idx=1&sn=c15dc9fe4166f047f1ddffafc639e2e0&scene=21#wechat_redirect)

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