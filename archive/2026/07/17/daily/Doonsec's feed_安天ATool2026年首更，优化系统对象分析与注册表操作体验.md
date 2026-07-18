---
title: 安天ATool2026年首更，优化系统对象分析与注册表操作体验
url: https://mp.weixin.qq.com/s/LY-P730i3QzweJACuh4Lsg
source: Doonsec's feed
date: 2026-07-17
fetch_date: 2026-07-18T04:41:39.289425
---

# 安天ATool2026年首更，优化系统对象分析与注册表操作体验

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/XBFaicYdOHk8WTe1IE1Gib2GHvjKL7IFZ3DVshmSPxo61bibQa5dnwOv9hVQRZ5gqnrwZ6UjsdnajkdqkibBAg7KPEYAdknQAbHsJsEeKQkUAak/0?wx_fmt=jpeg)

# 安天ATool2026年首更，优化系统对象分析与注册表操作体验

安天集团

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

点击上方"蓝字"

关注我们吧！

[安天ATool](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650202392&idx=1&sn=2df9432c1732feea0b8fbf1ce3328ee0&scene=21#wechat_redirect)（全称：安天系统安全内核分析工具）进行了2026年的首次版本更新，改善了 ATool 在主机安全排查和应急响应中的基础操作能力。

ATool 是安天研发的系统安全内核分析和 RootKit 检测工具（ARK工具），Windows 版本一直免费开放下载。可分析系统内核模块、驱动、服务、进程端口等关键信息，对目标对象进行安全检查和可信验证。帮助使用者检查主机上是否存在异常进程、可疑驱动、异常网络连接或恶意自启动项，处置顽固木马感染。

ATool的一项重要特色是：针对内存中的运行对象清单，均可调用安天AVL SDK反病毒引擎的云查接口，对运行对象（执行体）进行检测分析和信誉评估，输出发布者、内容、行为、位置四种信誉查询结果，发现恶意代码则标记告警。借此帮助使用者甄别有害与可信对象，后续可关联在线沙箱分析、逆向分析，也可交由AVL Code安全智能体进行判断（当前需手动触发，联动功能尚未开发）。

自Win10系统起，微软对安全机制进行了更为严格的调整，多数传统ARK工具已无法在Win10及以上系统加载运行。ATool成为全球少数仍能兼容 Win10 及以上系统的 ARK 工具之一。

7 月 15 日，Atool 推出今年首个更新版本 3.5.1.6，主要更新点如下：

1.优化进程、服务/驱动、端口、自启动项、SSDT/Shadow SSDT、IFEO、SPI、MBR 等模块的列表数据整理与展示逻辑。

2.修复文件详情采集、任务文件元数据回退、环境路径规范化、网格边界处理及部分枚举流程的稳定性问题。

3.完善 AToolFunc、MockAToolsClt、MFC 行为及多模块表格契约测试，提升回归验证覆盖度。

4.调整ATool 程序图标，正式启用红色T型镐Logo（与企业版保持一致）。

根据热心网友的反馈，今日更新至ATool 3.5.1.7，主要更新点如下：

1.重新设计注册表的新建、修改和查看功能。对话框改用Windows 原生控件，完整支持字符串、DWORD、QWORD、多字符串和二进制值。

2.补充二进制注册表数据操作能力。用户可以新建空值、调整数据长度、编辑内容或以只读方式查看数据，便于检查非文本类注册表配置。

3.增加注册表地址和URI 导航。工具兼容“计算机”等路径前缀，也支持 HKLM、HKCU 等常用根键缩写，可直接跳转到指定注册表位置。

4.修复注册表刷新较慢的问题，在键值数量较多或目录层级较深时，浏览体验有所改善。

欢迎访问[安天垂直响应平台](https://mp.weixin.qq.com/s?__biz=Mzg5MTU3NTM0Nw==&mid=2247486142&idx=1&sn=debdedb4cc44328ad4f73799144b65d3&scene=21#wechat_redirect)[（https://vs.antiy.cn/）](https://mp.weixin.qq.com/s?__biz=Mzg5MTU3NTM0Nw==&mid=2247486142&idx=1&sn=debdedb4cc44328ad4f73799144b65d3&scene=21#wechat_redirect)免费获取新版ATool 。

**往期推荐:**

# [安天文件快速搜索工具ASearch新版上线](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650215096&idx=1&sn=1c35b7f6ddf1941e4ec6e044ed0bfebb&scene=21#wechat_redirect)

[安天垂直响应平台改版上线](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650215084&idx=2&sn=78f234b359ecbe7df8a3dfc439eb4588&scene=21#wechat_redirect)

#

# [以执行体信誉查询辅助威胁“半自动”猎杀处置——安天小胖谈系统工具ATool的特色](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650202392&idx=1&sn=2df9432c1732feea0b8fbf1ce3328ee0&scene=21#wechat_redirect)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/krU5D4C1q6Su8m4epwZC39J9XTv5TOxXtKXld0O7YvcKGpIweyd5y6LHX1FW1QU1RLuE08hwNZmLTdcd4fOUGg/0?wx_fmt=png)

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