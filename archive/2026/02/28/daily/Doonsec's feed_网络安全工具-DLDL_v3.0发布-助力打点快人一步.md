---
title: 网络安全工具-DLDL_v3.0发布-助力打点快人一步
url: https://mp.weixin.qq.com/s/0GtNPn_Q3BMg13PXjmpngg
source: Doonsec's feed
date: 2026-02-28
fetch_date: 2026-03-01T04:20:43.031490
---

# 网络安全工具-DLDL_v3.0发布-助力打点快人一步

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Oiag47y540yic1m2aXWj0nwtAHiaeyWac2LJvObCNNUMQ5jBedT29XknJSuFZDicf5pibmXxyhD7xBp2YFic7n4XkMbQ521KS4RwSvqmJOmWrLmJ4/0?wx_fmt=jpeg)

# 网络安全工具-DLDL\_v3.0发布-助力打点快人一步

原创

Yn8rt
Yn8rt

迷人安全

![]()

在小说阅读器中沉浸阅读

DLDL详情可以看公众号上上篇文章：

[DDDD之自动生成+批量编写Workflow—DLDL](https://mp.weixin.qq.com/s?__biz=MzkwOTUwMTc1OA==&mid=2247484124&idx=1&sn=62d999bf1fd0f6c5ecfcc243860b6d29&scene=21#wechat_redirect)

# 3.0新增功能

1.添加dddd漏扫模块需要配合，部分功能需要配合专版dddd
2.修复保存到文件功能
3.新增api管理
4.优化自动生成workflow逻辑
![公众号/DLDL/assets/f6128c798a807e0666b3ff162b24a2d2_MD5.jpg](https://mmbiz.qpic.cn/mmbiz_png/Oiag47y540yibmtn3QX9BX3oaGZgJlmSfuSvwckw5nwLCP5ZL7CH92KuF2eKUvoj3O5TWBWNCVFoaicLRlmSp3kF22r3T0xic1kVttXwdagatqA/640?wx_fmt=png&from=appmsg)

# 2.0新增功能

1.半自动化生成workflow需要人工审核
2.人工打标功能
3.更新更改黑名单关键字
4.增加poc上限阈值(防误报)
5.poc增加文件夹选择功能
6.poc增加workflow状态检测功能
7.运行模式新增可选项：跳过已存在workflow中的POC
8.修复若干bug

# 成功展示

目前生成workflow：1301条，**耗时10s**
![公众号/DLDL/assets/290712ce9ce474a8f36cdb4f7337d34c_MD5.jpg](https://mmbiz.qpic.cn/mmbiz_png/Oiag47y540yibS8yZSDPODLCgibNqbcUjncIPz7d5RknIx7eB4SolBUOMtjFx0Z8hgIuBZQEpIicwQ2ZIwUEcmZAnSEcOGpgQGvQbibsacJkKTTs/640?wx_fmt=png&from=appmsg)

我用的POC数量是4512条，都是我用DLDL处理完中文编码格式错误，还有不符合nuclei的yaml格式的(xray格式)

# 使用教程

## 案例一

a：exe放在哪个目录下？
b：让exe与workflow.yaml、finger.yaml、dir.yaml、pocs文件夹同目录即可
![公众号/DLDL/assets/769969cadaf6481c0189101adc6dbc0f_MD5.jpg](https://mmbiz.qpic.cn/sz_mmbiz_png/Oiag47y540yib0qmGZt2j2zg3GX9DicAiaf0d9c6z2zvWb3dypJOEUQo6KdN0ZPwxzdsDWzwkSmrqsFQnD42aiaooPfMtjkDdwgzHUdZzpQFpoho/640?wx_fmt=png&from=appmsg)

## 案例二

a：如何一键生成workflow？
b：想全自动就按照如下勾选，如果想自己审核那就半自动化即可
![公众号/DLDL/assets/195c48433043a097a0ebe76475311119_MD5.jpg](https://mmbiz.qpic.cn/mmbiz_png/Oiag47y540y9XHYa6fnMkw2T5xR7GwdEyicPm1CZaQCN2jlOCj41z6GsuhfsGRiazn45QboKHRGfrA1o6sAHbcibyVpEv4sMnfKWibpSR8UNYtlY/640?wx_fmt=png&from=appmsg)

**可以感受一下准确度：**
![公众号/DLDL/assets/028a7aa228e2255872856aba02d72f00_MD5.jpg](https://mmbiz.qpic.cn/mmbiz_png/Oiag47y540y9VRXT79bfmp2OIa8oBIjpywtC3AuHvz4oA3uiaF61F9VHCnbTY9AJbbm3MmEeoAj6v28PTKIpFXIHXdgw6zEGibEJibDSdVhWfLw/640?wx_fmt=png&from=appmsg)

**半自动化**：会出现如下打标页面
![公众号/DLDL/assets/8f0e7f0ac6195cd6db749262c3ec4776_MD5.jpg](https://mmbiz.qpic.cn/sz_mmbiz_png/Oiag47y540y8cUiczQxaKleV8FNtDwtYfR8RLSYxnqz888KgI29ZrJMRW69MpvPOgqXlNumhpkVY0mpLUk94zHHfoZ4QXn6LtXDiaMYMHUHWgA/640?wx_fmt=png&from=appmsg)

## 案例三

a：生产完workflow怎么用？
b：编译一下自己的dddd，或者用别的dddd指定一下参数也可以
![公众号/DLDL/assets/59f91dc55d6cbd8136516ef96f065c03_MD5.jpg](https://mmbiz.qpic.cn/sz_mmbiz_png/Oiag47y540yicNIUl4PS6llo9foFs9GbsFQNjbeGQPtElJjVYwBUD5cgiaMDNIJN8icLsR5gCfQfJsLmhvRicBibyicq0TRzBuBq31wNLgCC9AYo3o/640?wx_fmt=png&from=appmsg)

# 项目地址

项目闭源免费
https://github.com/Yn8rt/DLDL/releases

# 交流/反馈群

**转发本文到圈内群(200人以上)，或者朋友圈可在群里找我要已经处理好dddd**
特此声明：POC都是大家能搞的我只是稍加处理
![公众号/DLDL/assets/1f9a8fe851e0586fdb9f6eb393643a7f_MD5.jpg](https://mmbiz.qpic.cn/mmbiz_png/Oiag47y540y8QB1icphPia3IYCvicDF2t0YaLsNLnoDse5X3JDWGYy1DgbVBOu4DcQSxKT18PiadGxc1606Ox1jQDgaFdFsQzx7ibiczWVP3cs3VOU/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/IOUVFMosoqPvCzibggORicOgMhjBp7HVEtlMoDQGga60sr3AsTe5aHRs7bA7yNic8sibicSpXUIzHkWuDoIH3ibESHCQ/0?wx_fmt=png)

迷人安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/IOUVFMosoqPvCzibggORicOgMhjBp7HVEtlMoDQGga60sr3AsTe5aHRs7bA7yNic8sibicSpXUIzHkWuDoIH3ibESHCQ/0?wx_fmt=png)

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