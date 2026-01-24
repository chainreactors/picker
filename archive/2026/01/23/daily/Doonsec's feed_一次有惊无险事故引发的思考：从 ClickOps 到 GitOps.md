---
title: 一次有惊无险事故引发的思考：从 ClickOps 到 GitOps
url: https://mp.weixin.qq.com/s/3R6sLyU5gns-1PbDzqUQeQ
source: Doonsec's feed
date: 2026-01-23
fetch_date: 2026-01-24T03:25:12.705666
---

# 一次有惊无险事故引发的思考：从 ClickOps 到 GitOps

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/aiarKdLqgA008vIdRVeanHu5fThJ565KTLgQkZCTZ47KEtdJicvImznibVLFB4gkE8LVUQSzKazsIYDV3gRHluvhg/0?wx_fmt=jpeg)

# 一次有惊无险事故引发的思考：从 ClickOps 到 GitOps

原创

imBobby
imBobby

imBobby的自留地

![]()

在小说阅读器中沉浸阅读

> 2026 年 1 月，因为一条具有歧义的规则备注，导致运维误将核心 WAF 规则关闭，内部系统对公网暴露长达 10 天。
>
> 本文复盘了这次由“文档与代码不一致”引发的事故，并探讨如何通过 IaC 和 GitOps 彻底解决此类人为风险。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/lP0vIEoQ23pCbGMA0jucVLzQLgrBCmDbpzaBdxKes1ZuQJia5iaefSDEL7lXunVrCkcA7mYGBvlCGUQ4IicHkE0icw/640)

![](https://mmbiz.qpic.cn/mmbiz_png/kXzOZWAA4gNaqWFwbOQFDeUWWmMqicHoZtNu9Ex6jbRsPyGtnBib6FetORgr4iak67z1yiaC6jmFJlrbdmbXdedNkw/640)

引言：当注释忽悠了我怎么办

![](https://mmbiz.qpic.cn/mmbiz_png/6Atfia9rqLJiaqM87D7eg3lUK4xmwqJSZLaMAq0MO5rSf5SpClRMZodMq2nXYZdiaRib0Ua5bW0lN7e5kZg9f50d9A/640)

咱们常说“代码是诚实的，但注释可能会撒谎”。我以前以为这只发生在代码里，没想到在 WAF 的配置界面上，一句规则描述竟然导致了防线失守...

上周，我们团队经历了这次静默故障：我们的内部测试系统 test canary alpha QA 等居然允许公网访问了接近十天，虽然说有 WAF 防护吧，但是这些系统肯定是不应该暴露出去的。

当然也要庆幸暴露出去的还好只是测试环境，而不是内部办公域...否则我估计运维团队免不了一番拷打。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/lP0vIEoQ23pCbGMA0jucVLzQLgrBCmDbpzaBdxKes1ZuQJia5iaefSDEL7lXunVrCkcA7mYGBvlCGUQ4IicHkE0icw/640)

![](https://mmbiz.qpic.cn/mmbiz_png/kXzOZWAA4gNaqWFwbOQFDeUWWmMqicHoZtNu9Ex6jbRsPyGtnBib6FetORgr4iak67z1yiaC6jmFJlrbdmbXdedNkw/640)

事故现场：消失的 403

![](https://mmbiz.qpic.cn/mmbiz_png/6Atfia9rqLJiaqM87D7eg3lUK4xmwqJSZLaMAq0MO5rSf5SpClRMZodMq2nXYZdiaRib0Ua5bW0lN7e5kZg9f50d9A/640)

事情的起因很简单。例如说，我们使用 Cloudflare WAF 来保护内部开发域名 `test.xx.dev`，逻辑非常直观：

* **规则逻辑：** 如果（来源 IP 不是办公室）且（来源 IP 不是 VPN），则 **Block（拦截）**。
* **预期效果：** 只有自己人能访问，外网访问直接 403。

然而，有一个研发在今天，也就是 1 月 23 日发现这条规则的状态变成了 `Disabled`。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/lP0vIEoQ23pCbGMA0jucVLzQLgrBCmDbpzaBdxKes1ZuQJia5iaefSDEL7lXunVrCkcA7mYGBvlCGUQ4IicHkE0icw/640)

![](https://mmbiz.qpic.cn/mmbiz_png/kXzOZWAA4gNaqWFwbOQFDeUWWmMqicHoZtNu9Ex6jbRsPyGtnBib6FetORgr4iak67z1yiaC6jmFJlrbdmbXdedNkw/640)

根因分析：好心办坏事

![](https://mmbiz.qpic.cn/mmbiz_png/6Atfia9rqLJiaqM87D7eg3lUK4xmwqJSZLaMAq0MO5rSf5SpClRMZodMq2nXYZdiaRib0Ua5bW0lN7e5kZg9f50d9A/640)

为什么会被关掉？是黑客入侵？还是恶意破坏？ 查看 Cloudflare 的审计日志后，真相让人哭笑不得...

**审计日志还原：**

```
// 2026-01-13 的操作记录"action": "rulesets.update","actor": "user@company.com","modified_rules": [  {    "enabled": false, // 关键动作：关闭规则    "description": "配置期间仅允许指定 IP 访问主站", // 罪魁祸首    "expression": "(not ip.src in $office_ip ...)"   }]
```

**问题出在这个**`description`**上。**

这条规则的规则描述写着：“**配置期间**仅允许指定 IP 访问主站”。 运维同学在看到这条规则时，会认为这条规则的意思是：

**当规则启用时，只允许某些 IP 访问主站；当这条规则禁用时，就允许全部 IP 访问主站**

我们可以认为这属于类似临时维护窗口一样的规则对吧！

刚好赶上了 1 月 13 日我们要切换部分流量到这个站点，也就是说希望 xxx.dev 这个域名能被全部 IP 访问，而不是仅限公司出口和 VPN 出口访问，因此运维同学直接就把这条规则关闭了（并没有看一眼规则内的表达式怎么写）...也还好他是关闭不是删除！

**这就是典型的认知错位：**

* **表达式逻辑：** 是一个永久性的**白名单**防护。
* **描述文字：** 和表达式逻辑不匹配。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/lP0vIEoQ23pCbGMA0jucVLzQLgrBCmDbpzaBdxKes1ZuQJia5iaefSDEL7lXunVrCkcA7mYGBvlCGUQ4IicHkE0icw/640)

![](https://mmbiz.qpic.cn/mmbiz_png/kXzOZWAA4gNaqWFwbOQFDeUWWmMqicHoZtNu9Ex6jbRsPyGtnBib6FetORgr4iak67z1yiaC6jmFJlrbdmbXdedNkw/640)

为什么我们没能立刻发现？

![](https://mmbiz.qpic.cn/mmbiz_png/6Atfia9rqLJiaqM87D7eg3lUK4xmwqJSZLaMAq0MO5rSf5SpClRMZodMq2nXYZdiaRib0Ua5bW0lN7e5kZg9f50d9A/640)

这次事故持续了 10 天，为什么监控没报警？因为没监控（创业公司一团乱李姐一下😅测试环境属于非核心资产，监控级别较低，导致未能第一时间触发 P0 级告警

* **沉默的失败：** 规则被关闭后，业务访问一切正常，没有反馈，运维自然不知道。
* **依赖单点防御：** 我们过分依赖 WAF 这一层，而忽视了对 WAF 本身状态的 Meta-Monitoring。

*（只能说还好我们这些测试系统也做了一层防御，并且入侵检测也一直开着...否则后果不好说啊）*

![](https://mmbiz.qpic.cn/sz_mmbiz_png/lP0vIEoQ23pCbGMA0jucVLzQLgrBCmDbpzaBdxKes1ZuQJia5iaefSDEL7lXunVrCkcA7mYGBvlCGUQ4IicHkE0icw/640)

![](https://mmbiz.qpic.cn/mmbiz_png/kXzOZWAA4gNaqWFwbOQFDeUWWmMqicHoZtNu9Ex6jbRsPyGtnBib6FetORgr4iak67z1yiaC6jmFJlrbdmbXdedNkw/640)

痛定思痛：

![](https://mmbiz.qpic.cn/mmbiz_png/6Atfia9rqLJiaqM87D7eg3lUK4xmwqJSZLaMAq0MO5rSf5SpClRMZodMq2nXYZdiaRib0Ua5bW0lN7e5kZg9f50d9A/640)

#### 事发生了，不应该去要找捅出娄子的同学麻烦，而是要找到问题造成的根因，从根上解决问题。

**整改一：消灭歧义**

我们将所有规则描述标准化，加上了类似 `[CRITICAL]`、`[DO NOT DISABLE]` 的前缀。

* *Before:*`配置期间仅允许指定 IP...`
* *After:*`[核心访问控制] 仅允许办公网 IP 访问 (生产环境常驻)`

**整改二：拥抱 IaC**

我们不能再容忍在 Cloudflare 网页控制台上“点点点”（ClickOps）了。我们编写了自动化脚本，将 WAF 规则纳入 GitLab 版本控制：

1. **代码化：** 所有的规则变成 Terraform 代码或 JSON 配置文件。
2. **版本控制：** 修改规则必须提 Merge Request，看到 diff 才能合并。
3. **自动化审计：** 我临时写了一个脚本 `cloudflare-scripts`，定期拉取线上规则与 Git 仓库里的基线进行比对。如果线上规则被意外关闭，脚本会立刻报警。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/lP0vIEoQ23pCbGMA0jucVLzQLgrBCmDbpzaBdxKes1ZuQJia5iaefSDEL7lXunVrCkcA7mYGBvlCGUQ4IicHkE0icw/640)

![](https://mmbiz.qpic.cn/mmbiz_png/kXzOZWAA4gNaqWFwbOQFDeUWWmMqicHoZtNu9Ex6jbRsPyGtnBib6FetORgr4iak67z1yiaC6jmFJlrbdmbXdedNkw/640)

结语

![](https://mmbiz.qpic.cn/mmbiz_png/6Atfia9rqLJiaqM87D7eg3lUK4xmwqJSZLaMAq0MO5rSf5SpClRMZodMq2nXYZdiaRib0Ua5bW0lN7e5kZg9f50d9A/640)

#### 这次事故怎么说呢，属于给我们这种草台班子创业公司上了一堂生动的人因工程课。

安全不仅是对抗黑客，更是对抗熵增和人为失误。

好的安全系统，不应该让操作者去猜是什么意思，而是应该通过流程和工具，把犯错的成本提高。

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aiarKdLqgA02QQHicBbXAm5hBjbFa2s2Yd38IQr3UDPrm7EfOdmSMLCvSRgVPsVR0YoIMcYwoaBmrqpwvwbhOvag/0?wx_fmt=png)

imBobby的自留地

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aiarKdLqgA02QQHicBbXAm5hBjbFa2s2Yd38IQr3UDPrm7EfOdmSMLCvSRgVPsVR0YoIMcYwoaBmrqpwvwbhOvag/0?wx_fmt=png)

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