---
title: 【转载】【BurpSuite插件推荐】微信小程序一键提取API、敏感信息--jaysenwxapkg
url: https://mp.weixin.qq.com/s/n2qtK7Mn5erNUL24vOT8fQ
source: Doonsec's feed
date: 2026-01-24
fetch_date: 2026-01-25T03:54:40.709366
---

# 【转载】【BurpSuite插件推荐】微信小程序一键提取API、敏感信息--jaysenwxapkg

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/NCLsGXruwoSDR5Z5eiaClTibhRszVYKwtLue5O2NQ16Z3icJeJ2VoMpAxoJxj2z7QcXr2lAGcZMOxET6jgT5UD2pg/0?wx_fmt=jpeg)

# 【转载】【BurpSuite插件推荐】微信小程序一键提取API、敏感信息--jaysenwxapkg

secureyang

![]()

在小说阅读器中沉浸阅读

以下文章转载于大佬 jaysen 凌霜雁安全志。

该burp插件可以解密新版本微信并且提取api和敏感信息。很方便，欢迎推广和使用。

0x00 插件介绍

以前老版本的微信很多师傅都登不上了，目前市面上也好像没有针对微信新版本的小程序反编译解包并提取敏感信息的插件，**jaysenwxapkg** 就是一款基于burp api 2025.8开发的插件

**项目地址：**

```
https://github.com/Jaysen13/jaysenwxapkg
```

（点击直达 GitHub，star 收藏不迷路～）

*简洁直观的操作面板，功能一目了然*

![图片](https://mmbiz.qpic.cn/mmbiz_png/n5sIVjOfpLpKvQVeNy1icsvrQu9RBzXicj9Qbq5c2MIRnho2hnsQyibQEqjH8emQFOacKicTvrsjVVMBflCz2BiaLcQ/640?wx_fmt=png&from=appmsg&watermark=1&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=0)

0x01 插件使用

1、下载安装

* 访问项目仓库，下载最新版 jar 包
* 打开 BurpSuite → 「Extender」→ 「Add」→ 选中 jar 包

![图片](https://mmbiz.qpic.cn/mmbiz_png/n5sIVjOfpLpKvQVeNy1icsvrQu9RBzXicjtUws0LJYWH8VluxqiaOCLiaPt3nmJamV49dAGadwdvoFGBkUXFNmzGRw/640?wx_fmt=png&from=appmsg&watermark=1&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=1)

加载成功后，插件栏会出现专属图标，像这样👇

![图片](https://mmbiz.qpic.cn/mmbiz_png/n5sIVjOfpLpKvQVeNy1icsvrQu9RBzXicjz7Dw4RWaONqtUg3eiad1XLquLsQ6BvbXZ4SUWibqbXTY7PL0jJotYp6w/640?wx_fmt=png&from=appmsg&watermark=1&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=2)

2、找到小程序包，定位关键路径

可以查看我目前是微信最新版本：4.1.6.14

![图片](https://mmbiz.qpic.cn/mmbiz_png/n5sIVjOfpLpKvQVeNy1icsvrQu9RBzXicjcMr8E2zlR5I8cZNBia9SyE5Cxv2YhLhd19NLZHxRyPQO8JNuIBOSC0g/640?wx_fmt=png&from=appmsg&watermark=1&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=3)

微信最新版（测试版本 所有4版本亲测可用）的小程序包默认藏在这里：

```

```

```
C:\Users\你的用户名\AppData\Roaming\Tencent\xwechat\radium\Applet\packages\
```

找不到的可以全局findsomething搜索一下packages

![图片](https://mmbiz.qpic.cn/mmbiz_png/n5sIVjOfpLpKvQVeNy1icsvrQu9RBzXicjdIqAmTs8DJjlZ1gDeWPUEuIdHGmrBHKRNeSTv0kd3hPFXB1ibia2Aebg/640?wx_fmt=png&from=appmsg&watermark=1&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=4)

*每个子文件夹对应一个小程序，主包、子包全在这，像这样👇*

![图片](https://mmbiz.qpic.cn/mmbiz_png/n5sIVjOfpLpKvQVeNy1icsvrQu9RBzXicj1SzeO8AhoLk2UrxTOvEzjNenVFBgy5LXj1STJrR12eiaKlic9VNibRh4g/640?wx_fmt=png&from=appmsg&watermark=1&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=5)

这里会有很多包，每一个包代表一个小程序，部分包还存在多个wxapkg文件，由于不知道哪个包是哪个小程序，先全部删除

![图片](https://mmbiz.qpic.cn/mmbiz_png/n5sIVjOfpLpKvQVeNy1icsvrQu9RBzXicjNibOzAWG4vxGGUe39QcDCMvLNuz2tzGGB4vRxX74DibFFnzYfBhfxicrA/640?wx_fmt=png&from=appmsg&watermark=1&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=6)

3、一键解析，信息自动提取

打开需要提取信息的小程序后，在插件选择小程序的文件默认首先打开以下路径：

```

```

```
C:\Users\你的用户名\AppData\Roaming\Tencent\xwechat\radium\Applet\packages\
```

![图片](https://mmbiz.qpic.cn/mmbiz_png/n5sIVjOfpLpKvQVeNy1icsvrQu9RBzXicjfib5xGo5ogvWvu2gGsGPu4xKGibFY5apmwicxlqibETaxnqO8gQdNPH0wA/640?wx_fmt=png&from=appmsg&watermark=1&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=7)

点击【批量解析所有wxapkg包】即可解密该小程序的所有主包和子包，并提取信息，*像这样👇*

![图片](https://mmbiz.qpic.cn/mmbiz_png/n5sIVjOfpLpKvQVeNy1icsvrQu9RBzXicjLuxKzF4ZWj1Po6Tm32vzO4TAfaIrXZHTc8icbxY9pu0QbUNicOnO7nLA/640?wx_fmt=png&from=appmsg&watermark=1&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=8)

![图片](https://mmbiz.qpic.cn/mmbiz_png/n5sIVjOfpLpKvQVeNy1icsvrQu9RBzXicjRgclAk5uhNphy1B3rIP2rGstUyxtHvL9a4vKAJJkONWUVor9gvAw1A/640?wx_fmt=png&from=appmsg&watermark=1&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=9)

![图片](https://mmbiz.qpic.cn/mmbiz_png/n5sIVjOfpLpKvQVeNy1icsvrQu9RBzXicjvA17d9I8Xq85iaX9FghbaBxpQygnYoiaT8TwQNhz0BydmXSRLnTicE1Gw/640?wx_fmt=png&from=appmsg&watermark=1&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=10)

解包缓存在

```
C:\Users\你的用户名\.burp\JaySenWxapkgOutput
```

![图片](https://mmbiz.qpic.cn/mmbiz_png/n5sIVjOfpLpKvQVeNy1icsvrQu9RBzXicjkOXBicQkb8MNgicFetUQEbTQ9wDtpwnqlXCHZyAQydj77arzeicTy6flA/640?wx_fmt=png&from=appmsg&watermark=1&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=11)

可以用编译器打开该目录搜索刚刚提取的铭感信息解包后的文件内容

![图片](https://mmbiz.qpic.cn/mmbiz_png/n5sIVjOfpLpKvQVeNy1icsvrQu9RBzXicjBO1oTGU7d09lVFR1GsARNAmLzcPibN4rn72PEicJtzFFejVxiaYRPP7hw/640?wx_fmt=png&from=appmsg&watermark=1&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=12)

## 0x02 插件配置示例

**敏感信息正则示例**

```

```

```
手机号:1[3-9]\d{9}车牌:^[京津沪渝冀豫云辽黑湘皖鲁新苏浙赣鄂桂甘晋蒙陕吉闽贵粤青藏川宁琼使领A-Z]{1}[A-Z]{1}[A-Z0-9]{4}[A-Z0-9挂学警港澳]{1}$AppSecret 泄露:(?i)\b\w*secret\bIP地址:^(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$微信小程序 session_key 泄露:(?i)\bsession_key\b身份证号:\b\d{17}([0-9]|X|x)\b邮箱地址:[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4
```

**API接口提取正则示例**

```
```
(?:"|')(((?:[a-zA-Z]{1,10}://|//)[^"'/]{1,}\.([a-zA-Z]{2,})[^"']{0,})|((?:/|\.\./|\./)[^"'><,;| *()(%%$^/\\\[\]][^"'><,;|()]{1,})|([a-zA-Z0-9_\-/]{1,}/[a-zA-Z0-9_\-/]{1,}\.(?:[a-zA-Z]{1,4}|action)(?:[\?|/][^"|']{0,}|))|([a-zA-Z0-9_\-]{1,}\.(?:php|asp|aspx|jsp|json|action|html|js|txt|xml)(?:\?[^"|']{0,}|)))(?:"|')
```
```

**前缀/后缀黑名单示例**

* 前缀黑名单：

```
/pages/,/components/,/static/,/uni_modules/,uview-ui/
```

* 后缀黑名单：

```
jpg,gif,svg,wxss,wxml,png,js,jpeg
```

**【免责与授权声明】**

本文旨在进行**安全技术研究、提升安全防御意识**，所有内容仅限于**授权环境下的测试与学习**。

**请务必遵守《网络安全法》及相关法律法规。** 文中涉及的漏洞信息及利用方法，严禁用于任何未授权的非法测试与攻击。任何个人或组织因不当使用本文内容而触犯法律，均需自行承担全部责任。

安全之路，始于责任，忠于技术。愿与各位同仁共筑更安全的数字世界。

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoQW0gRe2T7PcibUQdxRXlZ9gUmhnDnCnZH1QV9ickJOicpYfupCNqRefT4xquSPPTcAIhDibeicp4aL8ZQ/0?wx_fmt=png)

secureyang

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoQW0gRe2T7PcibUQdxRXlZ9gUmhnDnCnZH1QV9ickJOicpYfupCNqRefT4xquSPPTcAIhDibeicp4aL8ZQ/0?wx_fmt=png)

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