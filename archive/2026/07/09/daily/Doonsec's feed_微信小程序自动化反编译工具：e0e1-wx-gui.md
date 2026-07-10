---
title: 微信小程序自动化反编译工具：e0e1-wx-gui
url: https://mp.weixin.qq.com/s/2ygMDQjc83QZsJZ-47JDOw
source: Doonsec's feed
date: 2026-07-09
fetch_date: 2026-07-10T05:54:19.560656
---

# 微信小程序自动化反编译工具：e0e1-wx-gui

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/x2ibBTFXYHicIscM01ficOv6zJnkYtPyXYnl9gPRPSFCWOvINqMWgbr3xwy8AmxlGVvceRg1zcUxa4raomlIq5MiaYvE31sMXMYKqVvOmVM3OHQ/0?wx_fmt=jpeg)

# 微信小程序自动化反编译工具：e0e1-wx-gui

原创

KivenMitnick
KivenMitnick

网安工具库

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**更多干货  点击蓝字 关注我们**

**注：本文仅供学习，坚决反对一切危害网络安全的行为。造成法律后果自行负责！**

**往期回顾**

·[BugHunter-AI：智能自动化渗透测试助手](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247487792&idx=1&sn=9670c9dc666426642727661c66c1e68c&scene=21#wechat_redirect)

·[Hack Scanner --自动化黑白盒扫描器](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247487782&idx=1&sn=46b4c0dd663f3dc334bd08c72fdc131a&scene=21#wechat_redirect)

·[Firefox‑Reverse：网页版AI自动化逆向算法工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247487775&idx=1&sn=fae88a160aa85ae5e0a4cd6e4bb4c95e&scene=21#wechat_redirect)

·[K8sPenTool：一款面向Kubernetes集群的综合渗透测试评估平台](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247487757&idx=1&sn=34e2084e5d8e8dee47faddcffb2d3c61&scene=21#wechat_redirect)

·[CTF²: 推荐一个比较全面的CTF靶场](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247487722&idx=1&sn=f12056918c209179a318d1f904d05210&scene=21#wechat_redirect)

·[Bug Hunter：一个代码安全审计的skills](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247487714&idx=1&sn=b02dcacd5efb02443bd0a213b80ef99e&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

**背景分析**

![](https://mmbiz.qpic.cn/mmbiz_jpg/x2ibBTFXYHicLnBibExw3BLTcFYm1n8NjbCpQg5zFib4yX3sOEp24oQ2ibPNHKNoO7jyLkoe7JAZeibTSs3DMicPFzR6KffaFW1DhPqpHTDRIUZyf4/640?wx_fmt=jpeg)

      e0e1-wx 是适配 Windows 平台、基于 Python 构建的微信小程序自动化逆向与渗透测试集成脚本框架，面向网络安全研究场景实现静态逆向、动态插桩与敏感资产检测全流程本地化调度。工具依托可配置 yaml 规则引擎自定义正则匹配范式，完成 wxapkg 包批量反编译、工程结构还原与混淆代码语义优化，内置 sessionkey、iv 对称加解密模块以解析小程序客户端会话密文；其动态 Hook 模块依托插件基址适配机制实现 WeChatAppEx 进程调试接口注入，解决高版本客户端偏移缺失引发的插桩失效问题，规避多工具串联调用的流程损耗。工具搭载多线程并发处理机制，自动化遍历本地小程序缓存目录，批量识别硬编码 API 密钥、第三方鉴权凭证等信息泄露风险点，支持解包、动态调试、代码格式化多模式组合执行，依托开源逆向组件完成模块化迭代，为小程序安全审计、逆向工程教学提供标准化自动化分析流水线，仅适用于合规安全研究场景

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

**config.yaml文件解释**

```
tools:  是否开启请求接口  asyncio_http_tf: False  小程序结果保存的文件名  proess_file: "proess.xlsx"  不进行拼接的接口的url,不写入该状态码的接口  not_asyncio_http: ["weixin.qq.com", "www.w3.org", "map.qq.com", "restapi.amap.com"]  not_asyncio_stats: [404]  最大线程数  max_workers: 5  工具运行时间限制，单位秒  wxpcmd_timeout: 30wx-tools:  微信位置(必须配置)，注意这里必须使用的是单引号  wx-file: ''bot:  飞书机器人配置，是否开启飞书提醒  feishu-tf: False  api_id: ""  api_secret: ""  phone: [""]配置正则处，前面是正则名字 后面为正则匹配条件，可自行更改添加rekey:  google_api: 'AIza[0-9A-Za-z-_]{35}'  firebase: 'AAAA[A-Za-z0-9_-]{7}:[A-Za-z0-9_-]{140}'  google_captcha: '6L[0-9A-Za-z-_]{38}|^6[0-9a-zA-Z_-]{39}$'
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

**config配置**

1、配置wx文件夹位置配置

来到设置，查看文件管理对应的文件夹位置

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicLIvKV95IbxicLJ3OzRA7tnibjOmnqIibAncicqIMm99aasNtvnBic8AUeicia2Jia11YTVDibSFnaRhy9yOBtmd1cPqYuiaGluzichaAFalM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicKJb4BNRicQ0bL40nQPgPV5dHxrZ3UiaTmxEkf5z9P52NcYvibYVzP3tXJMH86Vk8ricHMAey1T3Td859h2InZX63h7YGxBbX6VF7s/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicLZaLgf6yUic9GrbwVc3WnRFBb1rs9JFfEoonYsgpZLqqVtZTVaVyq3zxAnoAxoqP4r5AmsCvVGw5yFrVFKo1L3RBkSfUYmlM3A/640?wx_fmt=png&from=appmsg)

2、配置hook，如果想进行hook-f12，我们需要配置对应的基址

```
首先查看 %appdata%\Tencent\WeChat\XPlugin\Plugins\RadiumWMPF\ 文件夹如果这里有两个，就是版本新的，修改日期新的的这个，如果不行就回头试试另一个，这里记住对应的版本
```

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicKFucA2ianf7y2ia8hR4kYtb0JoawrsmppzmSL39IBfKUVd2vTWicfnoxzLzd5HsiaDBmmoHdFQvTWjZvHwVfSGZNjYjI64rHLsWhU/640?wx_fmt=png&from=appmsg)

```
来到https://github.com/x0tools/WeChatOpenDevTools/tree/main/Core/WeChatAppEx.exe ，查看对应版本的addres或者到 https://github.com/eeeeeeeeee-code/wx-hook/tree/master/addres 查看对应的基址
```

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicJ6CJI5LpWjOkC3rPSBZokoM2OAE8aWxmLm29Gwofn0JZ8o3AefXRa10UCmBwW48ITfFlUWRKzf0czlPwTOxkenZvhH8zHWpDc/640?wx_fmt=png&from=appmsg)

来到脚本./tools/WeChatAppEx.exe.js文件中，修改addres参数为对应的版本addres

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicJplUxTZTanJib4twCWnsdhHnAEGuATRjJ9rnXYMia14jPUXVqdF4iaKTJ3ekMYsQ8gxYbE9ojeymh3EnJf0JHe6KC0cAxaWdPQHQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

**使用方法**

1、不进行hook(直接反编译)

```
python3 e0e1-wx.py
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicLjeJL2C8iaKwdbS33TotwrAS4HicvmicibxkIKKM0gnKJRItMsrDeYLJtHne1iaT7QA3ia1WdDHicVAegK5udA1aGHu64C0ibqEic2XPXw/640?wx_fmt=png&from=appmsg)

2、进行hook

```
python3 e0e1-wx.py -hook
```

3、进行hook同时对输出的代码进行优化

```
python3 .\e0e1-wx.py -hook -pretty
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

**github链接**

```
https://github.com/eeeeeeeeee-code/e0e1-wx
```

我们创建了交流群，一起来交流吧！！！

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/x2ibBTFXYHicIlvbicrQjBnHr1W96HkBB6955q27wMhicnydJKCpysVdcDK6kc3SOibicg0Ysq3NRD7MZs4SGicPN3qkIaDiadQHia3jShsP93lN98icE/640?wx_fmt=jpeg&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=11)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eRUtCzBCFbaMYy1c7utlweibCFXWsicmm9ebyvInBtdsD0QRlUDTdLib1g/640?wx_fmt=png&from=appmsg)

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