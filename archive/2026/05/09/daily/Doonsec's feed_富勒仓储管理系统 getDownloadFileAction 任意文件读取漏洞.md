---
title: 富勒仓储管理系统 getDownloadFileAction 任意文件读取漏洞
url: https://mp.weixin.qq.com/s/fQe8__x_maBLpSZoeu4dsQ
source: Doonsec's feed
date: 2026-05-09
fetch_date: 2026-05-10T05:32:19.376626
---

# 富勒仓储管理系统 getDownloadFileAction 任意文件读取漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/h29PqzMrB7vaMz86MWxesqetjWSH0nR5Efl4YHjoZvITU16dwX7T6YKoxJUu3hIiammwAQvMWlicfxzjIKOYhJ8xqyV9TfubpDeicQBcrksZEs/0?wx_fmt=jpeg)

# 富勒仓储管理系统 getDownloadFileAction 任意文件读取漏洞

原创

安羽安全
安羽安全

安羽安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**01****免责声明：**

文章内容仅供日常学习使用，请勿非法测试，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，由使用者承担全部法律及连带责任，作者及发布者不承担任何法律及连带责任。如有内容争议或侵权，我们会及时删除。

---

**02    漏洞描述**

富勒仓储管理系统 getDownloadFileAction 任意文件读取漏洞复现。

**fofa：body="/logincenterapp/ValidateImageService" || title="FLUX WMS生产环境"**

![](https://mmbiz.qpic.cn/mmbiz_png/h29PqzMrB7vmKymFePoatKKWiaaNjibJofgLoMy88yOOCMPfyj7aIrDVadMc3Yx3HwYEq6hGzmHiaHeblC1VmoTScX361guBRzrgSmuXtzhG00/640?wx_fmt=png&from=appmsg)

## **03    漏洞复现**

1、访问系统

![](https://mmbiz.qpic.cn/sz_mmbiz_png/h29PqzMrB7vyXKhxDskFNyJxCDYJCEaAWeeUzLe1iclRWRJq04Hs8GShSeyS1ngbGUEEw6BFThe5zfs8W14DWeFoAvSw0LeuriakiaDQXJWqvI/640?wx_fmt=png&from=appmsg)

2、漏洞验证

![](https://mmbiz.qpic.cn/mmbiz_png/h29PqzMrB7tLYPoDrH5gia6EbpS5zWXz7p0NkKGO7Cbc27o9icB5o44hQAS4gu12dVD418KNMlP5mS3DbKHbzyXSBWhENH6Om9RBapwuxIRug/640?wx_fmt=png&from=appmsg)

****关注公众号回复：**260509**获取漏洞POC详情****

**04    漏洞详情**

**Nuclei 批量自查验证脚本，加入下方内部圈子获取**

![](https://mmbiz.qpic.cn/mmbiz_png/h29PqzMrB7trqF8bAGxLrlPzfcJWBvMXSDIEXucxjkibylmWOutM6J47tT7yJf1Xz2O4xvbhSUVEGl1C0YjmT3qZoq0o1mfpQhcJms1aPxnA/640?wx_fmt=png&from=appmsg)

**圈子目前福利：**

整合全网公开1day/Nday漏洞POC、漏洞复现

每周持续更新，已更新漏洞500+

md5帮忙解密

凌风云网盘搜索 帮忙下载资源

后续福利还在增加中......

**漏洞持续更新中，限时立减19**

![](https://mmbiz.qpic.cn/mmbiz_png/h29PqzMrB7t9VLrmZ1uJxGkZibCQ8afPSbecPdkfsCzWXXGI8rmGrhGiasKRMOEJick3cPIVW87YuRBHJTb3IR5QUtmIjqmNHJgwicNcFPr7bOM/640?wx_fmt=png&from=appmsg)

扫描上方图片 二维码即可加入纷传内部圈子

![](https://mmbiz.qpic.cn/mmbiz_png/h29PqzMrB7sqYESPmZ4QkPSEFFuwzhh4pRaDcZWMkfwY937026ic096Xyk6gAtMKJdvl9F70EicR41PutQXUHspaSVnMuJ00Vh1xzXX2vr7Ts/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/LTgFltBqB7PO8sBn6daxxSpcm1cYAeQdVa2wicl6lh50EYCkw0yiaBrlc6Vh5HMKKaOzNLib9R2ricMCN6HTibR9IicQ/0?wx_fmt=png)

安羽安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/LTgFltBqB7PO8sBn6daxxSpcm1cYAeQdVa2wicl6lh50EYCkw0yiaBrlc6Vh5HMKKaOzNLib9R2ricMCN6HTibR9IicQ/0?wx_fmt=png)

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