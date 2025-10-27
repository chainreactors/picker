---
title: 通过分析JavaScript文件寻找漏洞
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496037&idx=1&sn=8baa21296ec3927599c0f53deaeb66b6&chksm=e8a5fb06dfd27210d3f13ee64d487ac203c0fc67ce1f41a413715ac6188ab68ceab18c0013a4&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2024-10-09
fetch_date: 2025-10-06T18:54:43.856065
---

# 通过分析JavaScript文件寻找漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj6A6ibRNLnSZRt4dlKQugQ6juWkB27Yb61d15Zd2lKalAphYRUr6bfwV1iaHNlo9uLLAPuBlichhicxzw/0?wx_fmt=jpeg)

# 通过分析JavaScript文件寻找漏洞

Anastasis

迪哥讲事

JavaScript在web中起着至关重要的作用，JavaScript文件是web应用程序的重要组成部分。以下是为什么JavaScript文件在web中很重要的一些重要原因。

交互性:JavaScript使开发人员能够为网页添加交互性和响应性，使其更具吸引力和用户友好性。

动态内容:JavaScript允许动态加载和更新网页上的内容，而不需要重新加载整个页面，增强用户体验。

表单验证:JavaScript支持客户端表单验证，确保用户输入在提交前符合特定标准，从而提高数据准确性和用户体验。

JavaScript文件可以在漏洞赏金计划中发挥重要作用，安全研究人员可以在该计划中识别并报告web应用程序中的漏洞。JavaScript文件可以包括以下内容:

```
aws access key
aws secret key
api key
passwords
admin credential
secret token
oauth_token
oauth token secret
```

如果您发现了敏感信息，则可以将其报告为信息泄露，如果该信息包含凭据，则还可以从中受益，在这种情况下，可以将其报告为访问控制失败等等。

## 重要问题:如何分析JavaScript文件?

这很简单，只是查看页面。

好吧，我开玩笑的。

我在JavaScript文件中发现了有效的登录凭据。

具体步骤:

你要有一个域名列表，我们称之为domains.txt。利用任何抓取url的工具来获取这样一个列表。

Katana or Waybackurl or gau

```
cat domains.txt | katana | grep js | httpx -mc 200 | tee js.txt
```

命令解释:

1. `cat domains.txt | katana`:该命令使用cat实用程序显示文件domains.txt的内容。它假设domains.txt包含一个域名或url列表，并通过|传递到katana以从域中抓取url
2. `grep js`: grep命令用于文本文件中的模式匹配。在本例中，它正在搜索包含”.js”模式的行，该模式表示JavaScript文件。这会过滤输出，只包含提到JavaScript文件的行。
3. `httpx -mc 200`:该命令利用httpx工具发送HTTP请求并从过滤后的url中检索响应。mc 200选项指定只显示返回成功HTTP状态码200(OK)的url。这将过滤掉不存在或返回错误的url。
4. `tee js.txt`: tee命令用于显示命令的输出，同时保存到文件中。在本例中，它将匹配前面条件的过滤url保存到一个名为js.txt的文件中。

现在我们有了所有的javascript链接。

通过nuclei进行扫描：

```
nuclei -l js.txt -t ~/nuclei-templates/exposures/ -o js_bugs.txt
```

另一种方式:

下载js.txt中的所有链接。

一定要搜索一下。

代码:

```
file="js.txt"
```

```
# Loop through each line in the file
while IFS= read -r link
do
    # Download the JavaScript file using wget
    wget "$link"
done < "$file"
```

```
grep -r -E "aws_access_key|aws_secret_key|api key|passwd|pwd|heroku|slack|firebase|swagger|aws_secret_key|aws key|password|ftp password|jdbc|db|sql|secret jet|config|admin|pwd|json|gcp|htaccess|.env|ssh key|.git|access key|secret token|oauth_token|oauth_token_secret|smtp" *.js
```

如果你是一个长期主义者，欢迎加入我的知识星球，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5jYW8icFkojHqg2WTWTjAnvcuF7qGrj3JLz1VgSFDDMOx0DbKjsia5ibMpeISsibYJ0ib1d2glMk2hySA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

##

## 往期回顾

[一款bp神器](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495880&idx=1&sn=65d42fbff5e198509e55072674ac5283&chksm=e8a5faabdfd273bd55df8f7db3d644d3102d7382020234741e37ca29e963eace13dd17fcabdd&scene=21#wechat_redirect)

[ssrf绕过新思路](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495841&idx=1&sn=bbf477afa30391b8072d23469645d026&chksm=e8a5fac2dfd273d42344f18c7c6f0f7a158cca94041c4c4db330c3adf2d1f77f062dcaf6c5e0&scene=21#wechat_redirect)

[dom-xss精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247488819&idx=1&sn=5141f88f3e70b9c97e63a4b68689bf6e&chksm=e8a61f50dfd1964692f93412f122087ac160b743b4532ee0c1e42a83039de62825ebbd066a1e&scene=21#wechat_redirect)

[年度精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487187&idx=1&sn=622438ee6492e4c639ebd8500384ab2f&chksm=e8a604b0dfd18da6c459b4705abd520cc2259a607dd9306915d845c1965224cc117207fc6236&scene=21#wechat_redirect)

[Nuclei权威指南-如何躺赚](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487122&idx=1&sn=32459310408d126aa43240673b8b0846&chksm=e8a604f1dfd18de737769dd512ad4063a3da328117b8a98c4ca9bc5b48af4dcfa397c667f4e3&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试设置功能IV](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486973&idx=1&sn=6ec419db11ff93d30aa2fbc04d8dbab6&chksm=e8a6079edfd18e88f6236e237837ee0d1101489d52f2abb28532162e2937ec4612f1be52a88f&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试注册功能以及相关Tips](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486764&idx=1&sn=9f78d4c937675d76fb94de20effdeb78&chksm=e8a6074fdfd18e59126990bc3fcae300cdac492b374ad3962926092aa0074c3ee0945a31aa8a&scene=21#wechat_redirect)

##

## 福利视频

笔者自己录制的一套php视频教程(适合0基础的),感兴趣的童鞋可以看看,基础视频总共约200多集,目前已经录制完毕,后续还有更多视频出品

https://space.bilibili.com/177546377/channel/seriesdetail?sid=2949374

## 技术交流

技术交流请加笔者微信:richardo1o1 (暗号:growing)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

迪哥讲事

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

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