---
title: 关于“Atlasx”使用手册
url: https://mp.weixin.qq.com/s/t4-EDPuF7YdDG82uj2D04g
source: Doonsec's feed
date: 2026-09-12
fetch_date: 2026-09-13T06:59:04.917031
---

# 关于“Atlasx”使用手册

# 关于“Atlasx”使用手册

原创

kuki
kuki

Heri76安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

「阿特拉斯X」社区版，该项目现已上线开源社区GitHub。Atlasx 旨在快速侦察企业关联的互联网暴露面资产，构建暴露面资产信息库。协助企业安全团队或者企业SRC白帽子有效侦察和检索隐藏资产，发现企业存在的薄弱点和攻击面。

[“SRC神器”互联网暴露面（AtlasX）正式发布](https://mp.weixin.qq.com/s?__biz=Mzk2NDUzMjgxOA==&mid=2247484969&idx=1&sn=3e1798d279db3a3de104da0df2d81990&scene=21#wechat_redirect)

项目地址：

```
https://github.com/yingfff123/AtlasX
```

Atlasx发布过去两天也得到了不少好的反馈和一些修改建议，不少在测试中没发现的问题也在最新版中修复；今天聊一聊很多朋友私信我的 关于“Pro版如何获取？”和“Atlasx的正确打开方式”

1.Pro版的获取

社区版和 Pro 版在资产采集上是一样的，区别在于：Pro 版在资产的测绘深度上比社区版更加深入，且 LLM 回溯、网关、技术栈分析匹配更透彻，从而使证据更准确，资产危险等级也更高（如图所示）；解决了1.资产不够深、2.这么多资产从哪里下手的问题；后续还会加入路径辅助猜解拼接等其他功能。其次，Pro 版的 API 接口可以更好地适配团队作战，方便接入 Agent 分析指定网站有点像MCP功能，Agent 通过 API 接口可以获取到目标资产的所有已收集线索。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pgh9MpJCA6j5dPTZZkkW62L1pC3Pz0PGiaEP5vRfzYiaeDibvicDAL5VnYeEd9peThIfsTw3am8RPXXTpTTAaA3fHiaiaFFhEtNYOJPH6Uk1mC6zo/640?wx_fmt=png&from=appmsg)

关于具体如何获取，考虑到大家还需要自配第三方key等，本着做开源产品的想法所以希望大家都能用上好的资产暴露面收集产品定价不会很高。这几天也有不少小伙伴试用，想了下还是暂不对外开售。。

2.Atlasx正确打开方式

2-1 首先说下各种打法：

最低配置打法（啥都不加，纯靠免费源）：能打，但是可能采集源有限，性能不包

哥布林打法（FOFA第三方key+chaos+主动扫描策略开启+js深度爬取+LLM用Deepseek或minimax）：基本功能都能实现，信息收集95%

富哥打法（全key配齐+Pro扫描策略全开+LLM用Claude/GPT）：信息收集99%，高风险资产优先程度极高，每个资产的细节全、业务分析准。

2-2 先说基本常见功能：

创建扫描任务，必须先创建企业再登记域名

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pgh9MpJCA6hP1sCanicns1uqT58vWW9jU4tQum6pTtFt9dH02wq0QcqVKUk8RKXibEad0qDKSu97Orn5TfKws31WuiaFjWAOk6cVwe4VTyGsOI/640?wx_fmt=png&from=appmsg)

创建项目，选择好企业后可以选择扫描目标和定期扫描

![](https://mmbiz.qpic.cn/mmbiz_png/pgh9MpJCA6hp7G6MSib9Ddov3yakcFhYpu6JTZSibibvR7WZzTNAwMO9OUlIViaasdSknWCkhAlYswO8OMkv4qSdBnH1axEUIrLj3EmFYwXGcG4/640?wx_fmt=png&from=appmsg)

添加凭据，下方可以跳转获取key

![](https://mmbiz.qpic.cn/mmbiz_png/pgh9MpJCA6j6IiaAgQMzInC3Ht2CvsJN7EjjESph7FXwIiaiaVYHYCv2pdibBT8bQOU9yic1yMomgsLjEO2UlzJTWmic2hnHVnsib8ZDHgf7c5zHVg/640?wx_fmt=png&from=appmsg)

扫描策略里->js情报爬取默认都关闭，推荐开启，不过时间会很慢

![](https://mmbiz.qpic.cn/mmbiz_png/pgh9MpJCA6h5RQLmKc2j4w1LmEfrgfPqbz1uicyArIWuTZw082ic8dD7yEAbOm2N1LQF0UTa7diaYeNvylla93Ggcx3Py3O2f5P1ymw4iamWFicw/640?wx_fmt=png&from=appmsg)

点击资产的+/-可以查看变更

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pgh9MpJCA6jW3zRzyxtjEuX715zVfBK4vjKxArR5QgXTYuMBXQU56KYL0jIXCqLYeMzFcRXsfD1VOb6CHbuRufibSbu9e04DMXXLLIqiba4dA/640?wx_fmt=png&from=appmsg)

2-3 Pro版功能的使用

API接口使用，点击用法可以直接获取api接口和token的命令可以直接使用

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pgh9MpJCA6hAnDExkgUSJux4mqJJz9sG7qZznnJa7a0MfhAyzWtVdEw3DjXgR9gHia9ibo9FeW5QcteDuA1qCtX77eK23IUc5qJe1gjenZySg/640?wx_fmt=png&from=appmsg)

直接发给Agent使用，以下为举例

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pgh9MpJCA6hhQemVSiafjGlmKibwzw85X5dWECWxwTocenicbQ90SgHAkiajqHWKl69GLFtBHBEyfPp3824hSBBKgeuMUiaMia7CmzfwVe2XIGcK8/640?wx_fmt=png&from=appmsg)

扫描策略，Pro版需要对这个功能进行开启，如果有企业报告需求开启开启威胁报告在报告里生成导出报告，模版是默认模版

深爬 JS → 短探针 → 未授权接口确认 → 宿主补种/兄弟浅爬 → 产出 why/narrative

![](https://mmbiz.qpic.cn/mmbiz_png/pgh9MpJCA6h1axdtfU5z4OsRrLruOic8Xj25jVjibcN6IzYTtwDv2aNgCXZylaBeVFguicicf2vXI09fpoGWbJdefVicgHAlCXuHM66Xx9duUDWw/640?wx_fmt=png&from=appmsg)

另外有一个问题：升级失败可能需要docker重启下进行升级

大家可以加下交流群，后续有更新会在群里通知

有什么bug问题和改进建议可以群里提出

![](https://mmbiz.qpic.cn/mmbiz_jpg/pgh9MpJCA6jzYh6bHS8MBpxHnicfPKpQFUFQ8aORtk04AmhkWBfEFjODfmAUnTFt8LnHPlicjzDoWPtVwtAib5iaw614Xo7l4rQgyqj3AsHUK2E/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

修改于

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/pgh9MpJCA6gbFh9W0gdWoYiabq065yTdtaggL9Sbt63JXUKCUILD7qMkaxobe0hMr9O6pJn7CdOH6fSk3rbwPZBzUm40zepYfiaNT5I2aerJU/0?wx_fmt=png)

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