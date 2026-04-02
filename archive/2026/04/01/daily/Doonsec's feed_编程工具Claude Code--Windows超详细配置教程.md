---
title: 编程工具Claude Code--Windows超详细配置教程
url: https://mp.weixin.qq.com/s/UeUf30y3rFps_X7JbT2k_A
source: Doonsec's feed
date: 2026-04-01
fetch_date: 2026-04-02T04:21:54.908066
---

# 编程工具Claude Code--Windows超详细配置教程

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/x2ibBTFXYHicJ7HNUa572An7Q2nMOLeNtpLA6IbhdiahX9BKLdicgRPwl0815icFImVMFyEQTKUSBJWlzia2xkFFGcy49Nr3zQAGbPD9VTBDGjGJQ/0?wx_fmt=jpeg)

# 编程工具Claude Code--Windows超详细配置教程

原创

KivenMitnick
KivenMitnick

网安工具库

![]()

在小说阅读器中沉浸阅读

**更多干货  点击蓝字 关注我们**

**注：本文仅供学习，坚决反对一切危害网络安全的行为。造成法律后果自行负责！**

**往期回顾**

·[TideFinger：一款开源的网络扫描工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486907&idx=1&sn=80168f54f2bd7d1b8b55a4fd9ff8d409&scene=21#wechat_redirect)

·[LnkMeMaybe：在蜜罐里创建快捷方式身份认证反向钓鱼](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486886&idx=1&sn=e95a4d8e43d973acfe0edec7db4e9807&scene=21#wechat_redirect)

·[FireKylin：一款开源安全应急响应系统痕迹采集工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486874&idx=1&sn=8aa0a2f192fd02765e6d602093333038&scene=21#wechat_redirect)

·[WatchVuln-web：一款开源漏洞情报监测工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486855&idx=1&sn=191e6b51306d5da6dc65388dc623ac0e&scene=21#wechat_redirect)

·[CTF-Web神器：让ai去帮你打CTF好了](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486849&idx=1&sn=19904be3904d7492f131658fca2fed3f&scene=21#wechat_redirect)

·[MDUT-Extend：数据库安全综合测试工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486840&idx=1&sn=ebc0e80ec4e9b9bd6670090fce379561&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

介绍

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicIiaWLtOvMaoNCe2iaCtn6w4w3hLOwt8oibshssBJibSuibNnJeiabvxv1sw5QqUbJRP8LK3iaYC58V2IEtpialg2wHxmYZzps2ibsT2ULA/640?wx_fmt=png&from=appmsg)

      Claude Code 是 Anthropic 推出的面向开发者的终端原生交互式编程助手，依托 Claude 大语言模型的深度语义理解与代码生成能力，为本地开发环境提供代码编辑、项目重构、调试排错与文档生成等全链路辅助，通过工具调用与上下文感知实现开发流程的智能化协同，其轻量化终端交互形态可无缝嵌入现有工作流，助力开发者提升编码效率与代码质量。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

安装教程

1.Node安装

进入网址

```
https://nodejs.org/zh-cn
```

获取Node->选择版本->windows下载程序

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicLgSO5HyGRVnEO33fTwsCF9AbiaruKVAVdZzww2zYoRm91wzkib2hiaFyjeqHaYb2qAsxwVRc5EqX36MU7hTeWVg0ckPKpqDGaDyM/640?wx_fmt=png&from=appmsg)

下载后一路next即可

安装完成后，打开powershell输入

```
node -vnpm -v
```

检查安装

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicK7XiaefWTtCXPeUTtDR9QOqHpbqd2VZmS7Wl5Vw0lIyicRAGibIialdPianTub3ML94afJZgL8lOQApks8zGibFUiaicGqucmbcV0MHv8/640?wx_fmt=png&from=appmsg)

2.安装git

进入官网

```
https://git-scm.com/install/windows
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicJJaUUZyZZs7DZFdyq5iaVmZkLg1xkde1u0oicOiaRBicTG0XehQsOGwYBXYnplibLTgpXN7DlLDCkqQorbzc4KAXNvt4FAeMib7ahcU/640?wx_fmt=png&from=appmsg)

下载安装（一路点击next即可）好后，powershell内输入：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicKmTtSRZtgHMsQ6NfCc1TFKgdF0fqJyJNwWEq7QmgIdksy08dSxFuMiaibaCM1Rg9vP2RVK5IicsfmwiahONmLHXfQHHP7bGgOGI5s/640?wx_fmt=png&from=appmsg)

检查安装

3.安装 Claude Code

1)直接全局安装（可能很慢）

```
npm install -g @anthropic-ai/claude-code
```

2）先修改成国内镜像全局安装，再改回原本的官方镜像

```
npm config set registry https://registry.npmmirror.com #改成国内镜像源npm install -g @anthropic-ai/claude-code #全局安装npm config set registry https://registry.npmjs.org  #改回官方镜像（可选）
```

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicLcAh1efiaTvxzgY8daM8B9easUHibaTXJqDaOxOzsKUWULd74mFMhjRCcmuEuVCicFtmjz2BMqzVtY5cd5jWAqyFSqqSdnWJNdHI/640?wx_fmt=png&from=appmsg)

安装完成后直接输入claude -v可能会报错，原因并不一定是安装失败，而是因为输入的 claude -v本质是调用 claude.ps1 脚本，被系统安全策略拦截了，可以选用以下步骤解决：

1）以管理员身份打开 PowerShell

2） 修改 PowerShell 执行策略

在管理员终端中输入以下命令，按回车执行：

```
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

执行时会弹出确认提示，输入 Y 回车确认。

这个策略的含义：本地脚本可以运行，从网络下载的脚本需要数字签名，是最安全常用的配置，不会影响系统安全。

3） 验证策略生效

执行以下命令，确认策略已修改：

```
Get-ExecutionPolicy -List
```

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicLWAQdrd7mfuEJUgfJHqB9GoBEwEX2aZJUgXZhPH8VhEla1rRshaFy5wYQJ9eSRA1ORZ1UNdaEEnbxiask9AJl5iaKibdwLd8MI0k/640?wx_fmt=png&from=appmsg)

如果 CurrentUser 行显示 RemoteSigned，说明配置成功。

4） 重新验证 Claude Code

关闭管理员终端，打开普通 PowerShell，输入命令验证：

```
claude --version
```

如果正常输出版本号，说明问题彻底解决。

4.配置API key

使用Claude Code 需要使用 Anthropic 账号或者配置你自己的API Key ，这里我用的是乘丰做演示，大家可以根据自身情况选用不同的第三方代理

这是乘丰的网址

```
https://api.cphone.vip/
```

这是我的邀请链接（好像可以给大家免费领余额（？））

```
https://api.cphone.vip/register?aff=Z5VC
```

按照图示新建API key（其他代理流程也差不多）

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicKfsv2FBe0SMl5SscUt7mHJVFcmXl0stwHtsibAzPfyTX6Qucnmib72rAMfFC9ynO3aRwia5xwc04O7VhMQsveZPH6TwANwLs6g6g/640?wx_fmt=png&from=appmsg)

确定需要填写的API地址，如乘丰的是

```
https://api.cphone.vip/
```

其他代理商的地址问一下AI即可

5.配置windows环境变量

打开设置，搜索环境变量->编辑系统环境变量

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicLEDwjrF2a78Qjy4sMCViag8gpGgERuSrsDTfXmtnYjkK5zu98XWebovUOLxjydYFB8pwMHrMdicibsty1U5F904QzibCwLISFKGcw/640?wx_fmt=png&from=appmsg)

按图示设置两个环境变量，分别是：

```
变量名：ANTHROPIC_BASE_URL变量值：你的代理商API地址，如https://api.cphone.vip/变量名：ANTHROPIC_AUTH_KEY变量值：你的API key
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicJILxY17XLfdlWAIwS2d1VMvtklJWDEf79J52qd3VmfG9KeuEyic0RicHhVDCN7957ia8Sd24L1TDRS60n6rmicMFRw2b0icEXIBFHA/640?wx_fmt=png&from=appmsg)

之后新建powershell窗口，输入

```
echo $env:ANTHROPIC_BASE_URLecho $env:ANTHROPIC_AUTH_KEY
```

分别输出你的代理商API地址和API key即可

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicJRUOqNS0lrhq0Q5qWbyY2zc83RuxpVb5ra1REtPLOR6s265r0iaWicDhUNBm8XX7Dphn1pbAv7rNiahg8uv9MSictDoIjZrEjJw1s/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

**使用及常见问题**

打开项目目录，之后输入

```
claude
```

即可使用

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicLZf8ur3yme7NXqayOxYJkWJxRhF8A9dyucrAaxUFUXtH6OaNSKCR9X0PqiafDqAPQhTuqbthelCjsoCjCY4rbEbzlGKCw8iaomY/640?wx_fmt=png&from=appmsg)

若报错，原因和前面claude -v的报错原因相同，只需要按照前文步骤配置一下即可解决

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicIxToopMwtQHOPwgczVGI7mtpEykK63PqsAQTmcrmrgVPXYyiaWNBfSae5683woEQQWBQLuJ005eycdQuhem0OiblSGnzPrgQT1A/640?wx_fmt=png&from=appmsg)

若出现如下报错

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicJrM2FcEaYu5suo81Ub8csgw3Qv0krTaWhonUng9BFlFiaBiaUOKkdq7I5KBrXXibqm4LtFM4jTB07DWB3UPIlt5S8icafUYkicIBdc/640?wx_fmt=png&from=appmsg)

有如下解决方法：

1.可能是你选择的claude版本对于key等的变量名与我用的版本不同，可以在终端输入：

```
claude --help env
```

将结果喂给AI即可找到正确变量名

2.可能你选择的代理商不支持claude支持的AI,可以换个代理商或者干脆用我用的乘丰

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eRUtCzBCFbaMYy1c7utlweibCFXWsicmm9ebyvInBtdsD0QRlUDTdLib1g/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicJVRBMdib7K3ZtqZv8Yl8uRmgwoJjcDRPibW9TfdiaaibJnTboUxTXo5C0iacxMHS0JnjVbGextpYnIfUquG9E3icJmibOWcPSVNJOOIk/0?wx_fmt=png)

网安工具库

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicJVRBMdib7K3ZtqZv8Yl8uRmgwoJjcDRPibW9TfdiaaibJnTboUxTXo5C0iacxMHS0JnjVbGextpYnIfUquG9E3icJmibOWcPSVNJOOIk/0?wx_fmt=png)

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