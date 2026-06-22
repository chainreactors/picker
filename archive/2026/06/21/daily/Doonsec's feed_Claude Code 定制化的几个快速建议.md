---
title: Claude Code 定制化的几个快速建议
url: https://mp.weixin.qq.com/s/wPLaPX_QU01aDEXFeDfZ5g
source: Doonsec's feed
date: 2026-06-21
fetch_date: 2026-06-22T07:16:11.334257
---

# Claude Code 定制化的几个快速建议

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/FT3A8r9icDylcNkGfKrK0ayguJiaMFtH68aLQw0EJicySqAw3N4sExepRXrlhiaE38pkSH0X66RWOJUtKxRGnA2oMbgRxS1BW21GW6obyRF3W4g/0?wx_fmt=jpeg)

# Claude Code 定制化的几个快速建议

凉城
凉城

ListSec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## Claude Code 定制化的几个快速建议

如果你发现自己正在做下面这些事，那通常说明这条指令应该放去别的位置：

**在 `CLAUDE.md` 里写“每次发生 X，就一定要做 Y”。** 如果一件事必须可靠发生，比如每次编辑后都跑 `prettier`，或任务完成后自动发 Slack，那么应该把它写进 `settings.json` 中的 hook。让模型“决定去运行 formatter”，和让 formatter “自动执行”，是两回事。

**在 `CLAUDE.md` 里写“绝对不要做这件事”。** 如果有些事是无论如何都不能发生的，那么“写成一条提示指令”就是错的工具。Claude 大多数时候会遵守，但当它处在高压场景、超长会话、模糊情境，或者在任务过程中读到了带提示注入的文件时，它仍可能失手。真正的护栏必须是确定性的，而实现这种护栏的方法，是 hooks 和 permissions。一个 `PreToolUse` hook 可以检查调用并返回码 2 来阻止它。**Managed settings** 还更进一步：它们由管理员下发，用户的本地配置无法覆盖，也是唯一能在组织层面强制执行确定性护栏的手段。

**把一段 30 行的流程塞进 `CLAUDE.md`。** 流程应该属于 skills。`CLAUDE.md` 适合放那些 Claude 需要一直记住的事实：构建命令、monorepo 布局、团队约定。像部署 runbook 或安全审查清单这样的内容，应该放进 `.claude/skills/`，只有调用时才载入正文。

**写了一条只适用于 API 的 rule，却没有加 `paths`。** 如果这条 rule 只作用于 `src/api/**`，那就应该用 `paths:` 限定范围，这样它在做无关任务时就不会占上下文。不加作用域的 rule，在机制上和把同一段内容直接丢进 `CLAUDE.md` 没区别：永远载入，永远消耗 token。

**把个人偏好写进项目级 `CLAUDE.md`。** 所有基于文件的方法，几乎都有一个用户级的对应版本，而且它们会在你每次使用 Claude Code 时载入，无论当前在哪个仓库。个人偏好，例如“永远使用语义化 commit message”，应该放在本地文件里；项目级文件则只应该保留那些“整个团队都认同、且确实属于该代码库”的偏好。

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GPsT7FaPGw5uQIpWOXmtw3tpIcv79XQaeOzFgThibkpMw28zSicDFgOumVJfHnfM533DBb7ibM1KnqkShD3Wtt3BA/0?wx_fmt=png)

ListSec

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GPsT7FaPGw5uQIpWOXmtw3tpIcv79XQaeOzFgThibkpMw28zSicDFgOumVJfHnfM533DBb7ibM1KnqkShD3Wtt3BA/0?wx_fmt=png)

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