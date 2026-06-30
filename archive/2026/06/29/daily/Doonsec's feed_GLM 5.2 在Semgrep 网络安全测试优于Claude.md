---
title: GLM 5.2 在Semgrep 网络安全测试优于Claude
url: https://mp.weixin.qq.com/s/o1x7x34R7xva6D3rmrXx4w
source: Doonsec's feed
date: 2026-06-29
fetch_date: 2026-06-30T06:06:35.483684
---

# GLM 5.2 在Semgrep 网络安全测试优于Claude

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/mqibEhCEN2ljvZz7hWFrjiaZvCFjAB0Btl2dqelV85NjnMA1nfahuW7ht6lyJ44qqB4xktdqcTcVNcQiclLMPOGKA78toIuB4oqxUH5YrENMDw/0?wx_fmt=jpeg)

# GLM 5.2 在Semgrep 网络安全测试优于Claude

酷酷信安

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/LicngnvC2AYJLaFkGPyjibguibsTp9PQfSeiaLqiap9nA5f6RQMprBDAbqhfnV9x6DA7JYljfSvW3lXY3CT9ysxia9gg/640?wx_fmt=gif)

**“** Semgrep 在 2026 年的一篇测试多个模型IDOR效果中报告，其最新基准测试结果显示 GLM 5.2 在网络安全代码分析任务中优于 Claude，成本大约是Claude的6分之一**”**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mqibEhCEN2lhojFACQfXGNfRcv75uxebEbkgCxwuKVVkQ7jbWapC4eUF0p6Svst3kYeyhPVUyYQdzpjibBlvMFDVrq1RZSuA0OyKV47gbtgU0/640?wx_fmt=png&from=appmsg)

01

—

实验:

```
@app.route('/user/<int:user_id>')def get_user(user_id):    user = User.query.get_or_404(user_id)    return jsonify(user.to_dict())
```

这个 Flask 路由直接从 URL 中的 ID 获取并返回用户记录，而没有检查请求者是否拥有该记录。任何已登录的用户都可以修改 user\_id 并读取其他用户的记录。IDOR 介于业务逻辑缺陷和配置错误之间，它并非污点流漏洞，这使得静态分析和 LLM 都难以检测：没有危险的函数需要标记，只有*缺少*检查。它也是实际应用中最常见的漏洞之一（目前在 HackerOne 的常见漏洞类型列表中排名第四），因此我们一直将其作为基准进行研究。

回到我们的实验：我们保持三个条件不变，改变一个条件，即标准实验条件。不变的条件包括：IDOR 数据集（与我们之前研究中使用的相同的真实开源应用程序）、评估方法（针对已知真阳性数据集的 F1 分数）以及 IDOR 系统提示本身。改变的条件包括：模型及其框架。具体来说：

* **Semgrep Multimodal**运行在我们自定义的框架中：该框架会枚举端点并将模型定向到这些端点。我们使用两个 Frontier 模型对其进行了测试。
* 但是，我们也通过 Claude Code SDK 运行了**Claude Code**，并通过其原生 SDK 运行了其他提供商模型，但提示信息相同。
* 包括 GLM 5.2、MiniMax M3 和 Kimi K2.7 代码在内的**开放权重模型**，在简单的 Pydantic AI 框架中运行，仅使用 IDOR 提示符，没有其他任何功能。

这是一个重要的细节，所以我们再强调一遍：开放权重模型并没有像多模态流程那样获得端点发现方面的支持。它们只看到了提示信息和代码库。这就是它们在没有任何帮助的情况下所能做到的

02

—

结论：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mqibEhCEN2lgxybAibqHHUCBk4Ws3YtpVZy3gZ7MCYASBEdibAsbw8rNuko75RVs2lClzPpWUeR6icwaLVsK5tQMicCa4q8BnDeZEpKUguK5vRYo/640?wx_fmt=png&from=appmsg)

    这不是对模型原始能力的直接比较，不希望任何人误解。我们认为应该得出这样的结论：在给定相同最低提示和资源的情况下，GLM 5.2（一种开放权重模型）的成本仅为前沿LLM的六分之一，却在一项真正高难度的安全研究任务中击败了Claude Code模型

1. 框架仍然比模型更重要。表格中最大的性能差距并非存在于不同模型之间，而是存在于启用端点发现的配置和禁用端点发现的配置之间。但对于目前关注安全研究的人来说，这绝对不足为奇，完全在意料之中。
2. 但是，当这种意想不到的结果突然出现，并且计算成本如此之低时，它就鲜明地提醒我们，不能把所有鸡蛋都放在一个LLM篮子里。如果你固守于昂贵的前沿模型，即使拥有最好的厂商锁定框架，你也可能错过更换模型带来的优势，无论是成本还是性能方面。
3. 开源模型已经跨越了一个值得关注的门槛。一年前，将开源模型列入漏洞检测排行榜简直是天方夜谭。而如今，GLM 5.2 仅凭一个简单的提示符就能击败 Frontier Agent，成本却只有后者的六分之一，而且还可以选择完全在用户自己的环境中运行。对于许多安全团队来说，这无疑是一个极具吸引力的选择。

需要说明的是：这只是一个任务、一个数据集、一次运行的结果。IDOR 检测是非确定性的，数据集是有限的，而且我们只彻底修改了一个配置。对于 IDOR 检测，GLM-5.2 可能确实比 Claude 更好，但对于 SSRF 检测，情况则可能相反——我们目前还无法确定，但可以肯定的是，我们会找到答案。

文章来源：

https://semgrep.dev/blog/2026/we-have-mythos-at-home-glm-52-beats-claude-in-our-cyber-benchmarks/

![](https://mmbiz.qpic.cn/mmbiz_gif/LicngnvC2AYJLaFkGPyjibguibsTp9PQfSeD1clNISC4IJc5jrc4hCwFGUyU8wkLlmia8badUdyMBIY2AIBDjUhbRg/640?wx_fmt=gif)

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/LicngnvC2AYLLP1XTZO2VmESctbhgz9PGJTo6uJ4yRqaSalTRLaTlc0RfKjpRLS9GLpVkL5lx7klx8LC30Z2gDA/0?wx_fmt=png)

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