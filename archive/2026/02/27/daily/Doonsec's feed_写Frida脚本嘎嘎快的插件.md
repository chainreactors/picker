---
title: 写Frida脚本嘎嘎快的插件
url: https://mp.weixin.qq.com/s/Y6Z5qwIEJpj1Zg0h3A6uqw
source: Doonsec's feed
date: 2026-02-27
fetch_date: 2026-02-28T03:50:30.931011
---

# 写Frida脚本嘎嘎快的插件

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oQ0sWhcqsVn2qtCQvIeBGzibx8c0FZVmClqkvXZvVsJKqbnibjuib4hIXqhr6TIYpia5Zqe5DIZZ90GLCC001bd1kEm3R9wLKd2hiaFcziaPw3yjE/0?wx_fmt=jpeg)

# 写Frida脚本嘎嘎快的插件

进击的HACK

![]()

在小说阅读器中沉浸阅读

> 字数 279，阅读大约需 2 分钟

## 前言

过年回来开宫，Frida 启动命令都忘光了。更不要说 Frida 脚本怎么写了。

打开 Pycharm，手放键盘上不知道敲什么，还要去文档里找，或者直接大模型启动了。

午饭和我同事聊到这个，他好心的给我推了 Pycharm 的插件。我试了一下，写 Frida 脚本，确实爽歪歪。

## zafrida-ui

项目地址：https://github.com/yilongmd/zafrida-ui

该插件可以在 github 下载然后导入 Pycharm，或者直接在 Pycharm 插件商店下载。

**环境要求**

* • IntelliJ IDEA 或 PyCharm (建议 2024.3+)
* • 本地已安装 Python3 及 `frida-tools` (`pip install frida-tools`)
* • 确保 `frida`, `frida-ps`, `frida-ls-devices` 在系统 PATH 中或在插件设置中指定路径。

**ZAFrida**
![2fe49e15d510d4ad9e9f06837121d598.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVlicNKmVicN1IEZKicxmEcwsouJzzgdPGpCHq0SGSAupTJUm5OeibpK8QZSiaJzHbZr6c9BZh0PIAdsKMPvwkBxGDxLvvA5o0l5Xw4E/640?from=appmsg "null")

2fe49e15d510d4ad9e9f06837121d598.png

安装完成，
![b6aebed013f43cacb494e6e7b7777b95.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVmBvFQpyB5VMfL2RP9fATib6INn8w57wgdCJnCxAI5C80jsjIxhB3YAySJsh14PSPbm73tGzdYktiaBaeKIojwUoUP88Nm3okDFc/640?from=appmsg "null")

b6aebed013f43cacb494e6e7b7777b95.png

手机运行 frida-server，USB 或远程连接手机，可以直接点击启动
![9408a3dcd37299cb64456c508a00bdb7.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVnTxaCU2FibboI8pcSWres5wu52VvZhjlPs5Ayr4siasQiaSbzpicY7jF0AIAzm7KYYT9qaIP2vHZKPs4yOQkvWBub747ibVTE9F7jI/640?from=appmsg "null")

9408a3dcd37299cb64456c508a00bdb7.png

## 自带脚本

插件不仅如此，还有自带 Frida 脚本，常用的都包含了，没在里面的可以自己添加
![74d255fc5de8f97f6edcae2e64189df9.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVk9XK8n60Jka28XTQ3TwIrYSN8dfnEhLqHvTId0k3fY6NmzOiboAd4efUictBSKiaVruzib7ic33nHtrBPMAhm4OHxU4ulKYgMy726Y/640?from=appmsg "null")

74d255fc5de8f97f6edcae2e64189df9.png

* • Android
* • iOS

鼠标右键，也可以选择常用模块
![06a153c820db4042eeca24186d5c8ad0.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVnkO5z2icQYRCuhnnD1cp37T0vLsF65KAhichIwxsBMFarEicAHnAQB2m6PQEKPOuVxlpkzFibJ1WRqvlfEBvpCLy5ibStN9GneyJicQ/640?from=appmsg "null")

06a153c820db4042eeca24186d5c8ad0.png

## 总结

用这个插件写 Frida，比自己哼哧哼哧写要快很多。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

进击的HACK

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

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