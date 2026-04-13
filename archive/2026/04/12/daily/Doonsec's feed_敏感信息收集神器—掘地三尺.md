---
title: 敏感信息收集神器—掘地三尺
url: https://mp.weixin.qq.com/s/BDy_sTneH8nJ9rUr27GJow
source: Doonsec's feed
date: 2026-04-12
fetch_date: 2026-04-13T04:55:48.145893
---

# 敏感信息收集神器—掘地三尺

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Nuuibh3bDOw6sUptRUSYDFPFL1eprNM1u5sOcib2e0UgJUqAFZiap2NeklDY01NXdu0ZxNEwC3xiaCPLHZjpiarhFTzpH6hiauiaMTKsgiaicOoFrfko/0?wx_fmt=jpeg)

# 敏感信息收集神器—掘地三尺

原创

shine
shine

无影安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

免责声明：本篇文章仅用于技术交流，请勿利用文章内的相关技术从事非法测试，由于传播、利用本公众号无影安全实验室所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号无影安全实验室及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉。谢谢！所有工具安全性自测！！！**VX：smile62157**

朋友们现在只对常读和星标的公众号才展示大图推送，建议大家把"**无影安全实验室**"设为星标，这样更新文章也能第一时间推送！

![](https://mmbiz.qpic.cn/mmbiz_gif/3GHDOauYyUGbiaHXGx1ib5UxkKzSNtpMzY5tbbGdibG7icBSxlH783x1YTF0icAv8MWrmanB4u5qjyKfmYo1dDf7YbA/640?&wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1)

安全工具

## 0x01 工具介绍

在日常渗透测试、代码审计或源码泄漏排查中，最令人头疼的就是**硬编码密钥、云服务器AK/SK、手机号、身份证号、数据库连接串**等敏感信息散落在文件角落里，人工翻找效率低下，还容易遗漏，错过关键信息。

于是开发了“掘地三尺”这个信息收集工具，该工具支持渗透测试时候常遇到的场景，例如获取了网站源码、web前端js、html等文件、或者反编译APP和小程序获取到源码后，要去查找源码里面的敏感信息，例如身份证号、密码、AK/SK、地图调用Key、加密密钥、小程序密钥等信息，那么就可以用掘地三尺来帮你高效完成。

## 0x02 工具功能

工具内置的敏感信息提取规则近百条，是结合网上公开正则以及多年实战渗透测试经验，提炼出来的正则规则，覆盖云安全、小程序、APP、web等常见敏感信息泄露类型，使用的时候只需要选择需要扫描的文件即可，支持递归多层文件夹扫描，即使是藏在最深层文件夹中的文件敏感信息，也能精准获取，不仅可以获取敏感信息，还可以精准定位泄露的位置，以及通过工具对泄露位置的上下文进行预览。

部分敏感信息类型如下：

🔑 **高危**：密码、各种云平台 AccessKey（阿里/腾讯/京东/百度/字节/金山/谷歌）、微信 sessionkey、webhook、JWT 令牌、AWS Key、Google OAuth Token 等。

📱 **中危**：手机号、身份证、邮箱、内网/公网 IP、MAC 地址、URL、微信公众号/小程序 APPID、企业微信/钉钉 corpid 、加密密钥等。

☁️ **低危**：各类云存储桶（阿里/腾讯/华为/亚马逊/百度/谷歌/微软/京东）、地图调用密钥等。

🧩 **额外检测**：Swagger、Druid 路径、SQL 错误信息、目录遍历特征、SSRF 参数、JSONP 回调参数、Source Map 文件等。

**其它功能**：
✅ 支持按风险等级（高/中/低）和数据类型快速筛选
✅ 结果表格一键导出（TXT / JSON / CSV 三种格式）
✅ 双击任意记录，**高亮显示命中行 + 上下文 5 行**（HTML 渲染，敏感信息标红）
✅ 右键单条复制、单条导出、单条删除（仅从结果移除）
✅ 智能去重（URL、微信公众号 APPID 等重复项只保留一次）
✅ 自动跳过二进制文件（.dex/.apk/.png/.jar 等），扫描效率极高
✅ 实时进度条 + 当前文件提示，大文件扫描不焦虑

## 0x03 工具演示

1、对一个小程序进行反编译，得到了源码文件

![](https://mmbiz.qpic.cn/mmbiz_png/Nuuibh3bDOw43hyZv33dWPllGibxXV24dG4oWMSSuw3hiaPicCCPI9mvRDO3no6MNfpzE5d0rRumvYz1tP6qiaLCkMMqtyXxJ6kKia9gLoHnb0ibBg/640?wx_fmt=png&from=appmsg)

2、打开掘地三尺

```
java -jar DigDeep.jar
```

3、选中小程序反编译后的源码文件夹，点击开始扫描，可看到扫描出大量敏感信息，包括身份证、手机号、IP地址、邮箱📮、密码等。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Nuuibh3bDOw6a1w6ibvWicfzkrnqG8VwUus5rB4jhnBoS2icaGSJ5EtkldmUtuUrJaT7uCxsvNT50TEbGDuGI4vR0Rj7DuiaPNycypfrGbVzFicGE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Nuuibh3bDOw6QM7J9KMPWNRzCGx6F3Cb9icAmhzk1IDts65LXHS0cDwsM5Q2Cicnia9yqjrd7XlVfH7JK5ZCZfgpNhSOicpNcKUlFMJVA96OZFLY/640?wx_fmt=png&from=appmsg)

4、双击其中的任意一条敏感信息，可以预览泄露位置的上下文（敏感信息，会以红色高亮显示），且会显示泄露信息具体的文件位置。

![](https://mmbiz.qpic.cn/mmbiz_png/Nuuibh3bDOw64BbtKFqrVzMfgR9N0ygFB4XAicsiatghtEtOhibOK9ibRVSmlqvB6pm2ZCch44j12a6lU5aS7s2d5vBBlYAzicfMS0AjWLnhEPLyA/640?wx_fmt=png&from=appmsg)

## 0x04 工具下载

```
https://github.com/shine798/DigDeep
```

最后推荐一下内部小密圈，干货满满，物超所值，**内部圈子每增加100人，价格将上涨20元，越早进越优惠！！！**

**![图片](https://mmbiz.qpic.cn/mmbiz_jpg/awCdqJkJFET8apEknf7bc6ZR8CyWIBqmV3L88k03ibsUgLfyzvyvuOjkZUfWm9YsK0phQ3owbjBgbhibnWBicgsXw/640?wx_fmt=other&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&randomid=ebo9tcn3&tp=webp)**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/awCdqJkJFESkGMPLLYOibsOdiaYUbUGH2ibd832G0h4stN7iacicE62hCJGle1IuVQbgGDx5v5GXjwUuE23xJNJjgTg/0?wx_fmt=png)

无影安全实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/awCdqJkJFESkGMPLLYOibsOdiaYUbUGH2ibd832G0h4stN7iacicE62hCJGle1IuVQbgGDx5v5GXjwUuE23xJNJjgTg/0?wx_fmt=png)

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