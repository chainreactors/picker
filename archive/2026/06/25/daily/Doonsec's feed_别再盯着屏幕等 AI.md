---
title: 别再盯着屏幕等 AI
url: https://mp.weixin.qq.com/s/yUd9dTXyIoPoZc6HISgVBw
source: Doonsec's feed
date: 2026-06-25
fetch_date: 2026-06-26T06:05:08.743396
---

# 别再盯着屏幕等 AI

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/I4ibOKsL0MdB1GiciaOhNNsCeOevDw4982siakI168nKScO7LM8HCDI7jSm5b6NEvvkPM9OS4WIYiccJRtV3TCCcjYXY3f7En6rCMiciaXq0zx8TGY/0?wx_fmt=jpeg)

# 别再盯着屏幕等 AI

AI和效率工具
AI和效率工具

SOC安全分析之旅

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 别再盯着屏幕等 AI：给 Claude Code 配个"完工语音提醒"

离开座位倒杯水，回来不知道 Claude Code 干完没有；切到别的窗口干活，又忍不住反复切回去瞄一眼。一行配置，让它干完活主动开口喊你。

用 Claude Code 这类 AI 编程助手干活，最大的隐性损耗不是 token，是**注意力**。

你让它跑个重构、写个脚本、批量改一堆文件。这活儿可能两分钟，也可能二十分钟。于是你陷入一种尴尬的等待：

•盯着屏幕看，浪费时间。

•切去干别的，每隔几分钟又忍不住切回来瞄一眼，思路反复被打断。

•干脆离开座位，回来还得重新进入状态。

缺的不是能力，是一个**"完工信号"**。

## macOS 里藏着一个免费方案

其实 Mac 自带一个被严重低估的命令：`say`。配合 Claude Code 的 **Stop Hook**，一行配置，就能让它每次干完活，用语音喊你一句。

零依赖，零成本，全局生效。

## 为什么必须用"钩子"，不是"技能"

Claude Code 里"自动触发某件事"有两种方式：技能（Skill）和钩子（Hook）。这俩长得像，脾气完全不同。

技能是你喊它才动；钩子是事件一发生就自己动。

"每次任务完成后自动提醒"——这种需求**只能用钩子**。因为技能要 Claude 每次都"记得"主动调用它，一忙就漏；钩子挂在事件上，由系统强制执行，**绝不漏**。

## 一行配置，立刻生效

编辑全局配置文件 `~/.claude/settings.json`，加入这段 `hooks.Stop`：

```
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "say -v Tingting \"任务执行完毕\"",
            "async": true
          }
        ]
      }
    ]
  }
}
```

三个关键字段：

•**Stop** —— Claude 每次停止响应时触发。

•**async: true** —— 后台播放语音，不拖慢响应。

•**say -v Tingting** —— macOS 自带语音引擎，Tingting 是中文普通话女声"婷婷"。

如果文件里已有其他配置（比如 env），把上面的 `hooks` 字段并列追加进去就行，别整个替换。

保存后，新会话自动生效；当前会话需要在交互终端打开一次 `/hooks`，或重启会话。

## 挑个顺耳的声音

终端跑 `say -v '?'` 能列出系统所有语音。常用的中文选项：

| 语音名 | 风格 |
| --- | --- |
| Tingting | 普通话女声，默认推荐 |
| Shelley / Sandy | 新版神经语音，更自然 |
| Sinji | 粤语 |

换声音只改 `-v` 后的名字。比如 `say -v Shelley "任务执行完毕"`。

## 再进一步

**换个俏皮的文案**——改命令里的文字即可：

```
"command": "say -v Tingting \"老板，活干完了\""
```

**手动试听一句**——终端直接跑：

```
say -v Tingting "任务执行完毕"
```

**哪天嫌吵想关掉**——删掉那段配置，或加一行全局禁用：

```
"disableAllHooks": true
```

## 一个小提醒

Stop 事件在清屏（/clear）、恢复会话（resume）、压缩上下文时也会触发，不只是真正跑完任务。每次响应结束都会响，包括简短问答。介意频繁响的话，可以加条件过滤——比如只在有文件改动时才响。

## 这套思路能玩出更多花样

同样的套路，换个事件和命令就行：

•写完代码自动跑格式化（PostToolUse + Write）

•记录所有执行过的命令到日志（PreToolUse + Bash）

•每次开会话播一句问候语（SessionStart）

核心思路就一句：**找到事件，挂条命令，让系统替你执行。**

---

把"等待—检查—再等待"的循环交给一行配置，把注意力还给真正重要的事。

AI 替你干活，也该替你盯着活。

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/I4ibOKsL0MdDIqvp6vDcv2HqdekyL3JDHW2vQpW4iaSegBwCiasoHhXGbxhK7sicWhKszfYzXOdj2bjPaadHTzUBYTZzOuzbzntH5tMKAOY8DKM/0?wx_fmt=png)

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