---
title: obsidian quickadd插件使用技巧
url: https://mp.weixin.qq.com/s/vRHnfF0McLLgm8ryuiNIiw
source: Doonsec's feed
date: 2026-04-16
fetch_date: 2026-04-17T04:43:28.027015
---

# obsidian quickadd插件使用技巧

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/FT3A8r9icDyldvbmyuwicf4iaBxChIdO7n17qFqxic1UAubAnaaoJAB6oJIAcayX40FEdCiatksJR3VOWrXfcG56NZLxjQ4zDy1KRgpo8BNV9Tj0/0?wx_fmt=jpeg)

# obsidian quickadd插件使用技巧

原创

凉城
凉城

ListSec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

quickAdd可以快速向存储库添加新的笔记或内容。该插件的功能是快速添加新页面或内容到您的存储库中，解决了用户需要快速添加笔记或内容时的繁琐步骤，提高了工作效率。

插件的官方介绍是：快速地添加笔记（Notes）或内容（Content）到你的库（Vault）。

1、Capture：捕捉。快速输入并保存信息到指定文件或每日笔记。 2、Template：模版。将模板插入到笔记。 3、Macro：宏。通过 JavaScript 与 Obsidian API 执行高级自动化流程。 4、Multi：多个。将以上三类 Choice 分组组织，提升可用性。用于把quickadd命 令做成可选菜单的形式。

![Pasted image 20260416203751](https://mmbiz.qpic.cn/sz_mmbiz_png/FT3A8r9icDyn4vYJltXhMGLdqw83XeZsFWzA1Efv1aq0NjiaZLDibu3jJyvndoiaGiaKvdZjCibtb98Wo0iasVPicCTf39JjahJXx0vLVxhj8MggNDo/640?wx_fmt=png&from=appmsg)

Pasted image 20260416203751

## **Capture**

![cda942c42201e09dce62132981749c2f_MD5](https://mmbiz.qpic.cn/mmbiz_png/FT3A8r9icDykylcRH6phKibCCVnx8S3LRk4sQ6gcic09VPHqIC5OAOvoOByua9zN0ewjQblQbbPIR3mLGyxz7Qtm5cxqPvFzdRUXrO7Blyg2QU/640?wx_fmt=png&from=appmsg)

cda942c42201e09dce62132981749c2f\_MD5

**Location部分**:指定内容存放的目标文件

> Capture，输入的内容作用于当前的文件，就是ob当前打开的文件

![02c1ba831eaec47bc322b7a31542ef31_MD5](https://mmbiz.qpic.cn/mmbiz_png/FT3A8r9icDyn2GAHCjQDwCibm5ET5A3zf3BKIYmc7jrTBSmpJ8g0qwEMzzyOryHiaSb8FLdBSsY2CTyibDpSicPcVBEU9I6UZOFJDpCYWaDJkRA8/640?wx_fmt=png&from=appmsg)

02c1ba831eaec47bc322b7a31542ef31\_MD5

> File Path / Format 捕获的文本输入到这里指定的文件中，支持语法格式。如：{{DATE}}代表时间，preview中可以预览当前路径中变量的设定

![871dd9fc6c7c93898a350ac5a9d28b6c_MD5](https://mmbiz.qpic.cn/mmbiz_png/FT3A8r9icDykVS9WoywAct7oyE7TYbZt239PK58Al6y2RH3UGe1EGxGzG3EAzwptjAJmr7D7rMpjUG9iayfHnmjrcNGbLQZYb37fBuqiaricxIQ/640?wx_fmt=png&from=appmsg)

871dd9fc6c7c93898a350ac5a9d28b6c\_MD5

> 如果目标文件不存在，则创建，创建文件时可以指定模版

![c54bbe4c8c067dafe39c4bf3d06822b2_MD5](https://mmbiz.qpic.cn/sz_mmbiz_png/FT3A8r9icDylUunpkou3kXYhOIIz5cVv1AURxPQb5o1L0ZfPXtoLFIFEGJibVc2nmk3G3kIibZYojicsKClw3HLxPU0WThU3FL76lo5kHibUGIYs/640?wx_fmt=png&from=appmsg)

c54bbe4c8c067dafe39c4bf3d06822b2\_MD5

**Position：内容插入到文件的哪个位置？**

> 插入的内容可以写入指定的位置，如文件开头、指定行后面、文件结尾处。我这里选择插入指定行后面，那么在Insert after处，可以指定插入到哪后面，下图是插入到## 今日思考后面，一般可以指定在标题后面。

![00cd669d1390818319366f5092d66c78_MD5](https://mmbiz.qpic.cn/mmbiz_png/FT3A8r9icDyn9fJCmF8bKedicpafCfDaCibXMam7nSmIE1B8RwqV8BvTXwfckRtktcTy7owaBxLJRpyuKG0BSxS6dJ9mfpevnAricQjIWMlhsgI/640?wx_fmt=png&from=appmsg)

00cd669d1390818319366f5092d66c78\_MD5

> Insert at end of section:在本节末尾插入，如 ## 今日思考 后面插入内容，叠加至文本后面。 Consider subsections:包括该节的子节点。 Create line if not found:如果没有找到则创建行

![d3d258f72490401d5e3aa8c3e2b139fa_MD5](https://mmbiz.qpic.cn/sz_mmbiz_png/FT3A8r9icDynz0scRvhYCBb96ALiaBtIibc7LLjHlyI33eVIBGbkxLyONhocyOwlf4uyDLWuMHQXHLNKsqkLW66BhHbho3ZnsHsicXy9pDsbiaPA/640?wx_fmt=png&from=appmsg)

d3d258f72490401d5e3aa8c3e2b139fa\_MD5

Content：设置插入的内容的格式

> Task:任务格式，以- 开头 Capture format：设置内容格式，如下图，时间，内容

![e84b3335ae36be20db2f69fe1c0c3ffb_MD5](https://mmbiz.qpic.cn/sz_mmbiz_png/FT3A8r9icDyl9sgrDu8kuCLmQaoa43PHRoySLXvlyAyzoI7adJMGzWqjp7RtKuteicLvJ3zYHGmXXRnjBVo2oR3aJMxeq0aD2ysGe7qoVWq1o/640?wx_fmt=png&from=appmsg)

e84b3335ae36be20db2f69fe1c0c3ffb\_MD5

Behavior：行为

> 创建Capture之后的行为 如打开文件，运行指定的Templater，

![f87e774650e6716df26ee8d5b31b973a_MD5](https://mmbiz.qpic.cn/sz_mmbiz_png/FT3A8r9icDynGEKMNxicI2vmcTIic0YibewpOpRItyNO6oWjCylcEqIXrbib4JibxKHB0PHiafPKuwsa3L6V4icd0UJ8MJA0Xb4gPlxXux2xbY4MnjE/640?wx_fmt=png&from=appmsg)

f87e774650e6716df26ee8d5b31b973a\_MD5

## template

新建笔记时指定相应的模版，并将笔记存放至指定的目录。这个比较简单。

![0f02f0828e3d583afe0146ec282b6d23_MD5](https://mmbiz.qpic.cn/sz_mmbiz_png/FT3A8r9icDyn6mjUq2xxfx99mlGgnibDXWicWHiaWrv8sNPTFfq5piaAwZLicgMblgxthuezJ0XH88TicVVniaFeHILaqLOLQ0d1q6rdJG4sr6wkHgg/640?wx_fmt=png&from=appmsg)

0f02f0828e3d583afe0146ec282b6d23\_MD5

## quickadd结合admonition

ad-后面可以使用{{VALUE:值1,值2,…}}接多个变量

```
```ad-{{VALUE:faq,info,tip,success,warning,danger,fail,example,bug}}
{{Value}}
```
```

最终结果如下，选中内容，按quickadd的快捷键（可到快捷键中设置）

![e7753e07a297c87ea9fba6965ff70300_MD5](https://mmbiz.qpic.cn/mmbiz_png/FT3A8r9icDylJyd3r0RCScCmkT01QH2LcwBBiaKoicOibicvCfRlyvp9VOHYTPbbH1vTsokiadZibTSwerChyHCzu6vqlYCIQbZEN0Kh3oSqCaffSU/640?wx_fmt=png&from=appmsg)

e7753e07a297c87ea9fba6965ff70300\_MD5

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GPsT7FaPGw5uQIpWOXmtw3tpIcv79XQaeOzFgThibkpMw28zSicDFgOumVJfHnfM533DBb7ibM1KnqkShD3Wtt3BA/0?wx_fmt=png)

ListSec

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GPsT7FaPGw5uQIpWOXmtw3tpIcv79XQaeOzFgThibkpMw28zSicDFgOumVJfHnfM533DBb7ibM1KnqkShD3Wtt3BA/0?wx_fmt=png)

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