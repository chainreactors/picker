---
title: 免费贡献给粉丝们：我调整claudecode源码后配置使用本地大模型后，现在完全只交电费了
url: https://mp.weixin.qq.com/s/v3FyEbpdsDAweXNllIENrw
source: Doonsec's feed
date: 2026-04-12
fetch_date: 2026-04-13T04:53:43.194396
---

# 免费贡献给粉丝们：我调整claudecode源码后配置使用本地大模型后，现在完全只交电费了

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/WkIYDhtln6YRQPN83ibrzgfiaYG6jZaB6st7jibxy8SnQEpOGHgFMHOkJib5Scmg2QmgvA1B2WqcticGk6ebxeR5eDflDgBCaJML3Z1FgAm9bYic8/0?wx_fmt=jpeg)

# 免费贡献给粉丝们：我调整claudecode源码后配置使用本地大模型后，现在完全只交电费了

原创

谢谢您哦
谢谢您哦

OA大助手

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmecoa.qpic.cn/mmecoa_png/FibgVmkS0fhZR4viaK2rnGJBOWiaKugWtDbLwcBFV9x9Sa1Tm4LehGUs2A0DQ6CXoGibYGtCSKHkGIHDBZqqDEPfGg/640?wx_fmt=png)

近期AI圈最受关注的事，就是Anthropic旗下的Claude Code（简称CC）源码泄露——因官方发布时的配置疏忽，51.2万行核心源码意外曝光，无需复杂破解就能获取。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/L1TSZiaYzvDtbvx1TQQGLLShiamzMaBQIwfhTh7tj2uUY9GYGd6XvCoAb6Y6V58rrjg95KANIAn38L8anAUoRRAw/640?wx_fmt=png)

**福利来啦！**

估计不少关注AI工具的朋友，都刷到这场泄露事件了吧！今天给大家带来个实打实的福利：我已经拿到了完整泄露源码，并且做了去认证拦截调整，现在只要简单配置个APIKey和BaseUrl，就能直接用这款超强AI编程工具啦！

**重点：**

**1、后台回复 claudecode 获取！内容不易，请多多支持！**

**2、后台回复 flynatgui 获取内网穿透工具！**

找到 run-claude.bat 批处理脚本，设置API\_KEY和BASE\_URL就可以运行使用了。

```
@echo off
setlocal
cd /d "%~dp0"
REM 这儿设置你的 APIKEY 和 BASEURL 即可
set ANTHROPIC_API_KEY=not-used
set ANTHROPIC_BASE_URL=http://jzixpm71.beesnat.com/v1
set ANTHROPIC_MODEL=Qwen3-Coder-XH-Next-Q4_K_M.gguf
set ANTHROPIC_DEFAULT_SONNET_MODEL=Qwen3-Coder-XH-Next-Q4_K_M.gguf
set CLAUDE_CODE_MAX_TOKENS=55000
set ANTHROPIC_MAX_TOKENS=4096

where bun >nul 2>&1
if errorlevel 1 (
    echo ERROR: bun not found. Install from https://bun.sh
    pause
    exit /b 1
)

set CLAUDE_CODE_AUTO_TRUST_CWD=1

if defined ANTHROPIC_BASE_URL if defined ANTHROPIC_API_KEY (
  if not defined ANTHROPIC_MODEL set ANTHROPIC_MODEL=gemini-pro
  set ANTHROPIC_AUTH_TOKEN=
)

echo [1/2] bun install...
call bun install
if errorlevel 1 (
    echo ERROR: bun install failed.
    pause
    exit /b 1
)

echo.
echo [2/2] Starting Claude Code - bun run .\run.ts
echo.
echo This is NOT the whole app. The next thing you should see is either:
echo   - a full-screen Claude Code interface, OR
echo   - one line "[claude-code] Loading interactive UI" then the interface.
echo If the window stays empty/black after ~15s, run start.bat so Windows Terminal opens.
echo Exit anytime: Ctrl+C
echo.

call bun run .\run.ts

set ERR=%ERRORLEVEL%
if not "%ERR%"=="0" (
    echo.
    echo Exit code: %ERR%
    pause
)
exit /b %ERR%
```

    mac 版本的小伙伴请自行使用大模型转写这个脚本配置即可！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/L1TSZiaYzvDtbvx1TQQGLLShiamzMaBQIwfhTh7tj2uUY9GYGd6XvCoAb6Y6V58rrjg95KANIAn38L8anAUoRRAw/640?wx_fmt=png)

**本地大模型内网穿透**

如果你的本地大模型需要在其他外网使用，可以配置内网穿透，本人使用的 蜻蜓映射 ！需要 2 块钱的实名认真费用，免费穿透稳定，网速也不错！

然后 BASE\_URL 配置映射的域名即可！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/L1TSZiaYzvDtbvx1TQQGLLShiamzMaBQIwfhTh7tj2uUY9GYGd6XvCoAb6Y6V58rrjg95KANIAn38L8anAUoRRAw/640?wx_fmt=png)

**AI 电脑推荐**

很高兴给大家推荐一款 AI 电脑，技术支持是真的非常出色和良心！

![](https://mmbiz.qpic.cn/mmbiz_jpg/WkIYDhtln6ZXBfoST6Dib5BCzWRqcIxaVd8gBgBLc7U4n09sQia4ibIdIl2G5ztzTWnD99qibFbuoCmnpmDMdTzFsgWwQp6DM5Dq1QL2VlK3PsQ/640?wx_fmt=jpeg)

**口袋玲珑：锐龙 AI Max+395 128G 内存 96 显存 2TSSD**

![](https://mmbiz.qpic.cn/mmbiz_png/WkIYDhtln6YhtABx6Bh8mMjdD3IohvnnOh7xtkxDQHeHH8SrMBOS3CsuAx8Th7vIaD6rqUf5wTtmbbkUC6SP3PNB0N4hM6UGhFia5asa766g/640?wx_fmt=png)

内置大模型及应用，技术团队也一直在持续更新维护，全部开箱即用！很给力！

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/TEnldia9cPNib3PtzEdOVlJ9mZGSCYRtib5gFFYDmzzPIGibFIqib2ZQIQptzpiaAH17gBe74aeBX600YwXvWgp9ns5Q/0?wx_fmt=png)

OA大助手

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/TEnldia9cPNib3PtzEdOVlJ9mZGSCYRtib5gFFYDmzzPIGibFIqib2ZQIQptzpiaAH17gBe74aeBX600YwXvWgp9ns5Q/0?wx_fmt=png)

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