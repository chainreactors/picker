---
title: OpenViking 3D理解模型上线轴测八视图及PMI解析
url: https://mp.weixin.qq.com/s/c_1XnUC4_3VvBBAM-md4lA
source: Doonsec's feed
date: 2026-11-12
fetch_date: 2026-11-13T08:58:07.753209
---

# OpenViking 3D理解模型上线轴测八视图及PMI解析

# OpenViking 3D理解模型上线轴测八视图及PMI解析

原创

OpenViking
OpenViking

字节跳动技术团队

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**OpenViking如何理解一个3D模型**

OpenViking发布原生3D内容理解模型，支持三维.STEP文件的导入与解析，**信息还原率做到 100%**。

![](https://mmbiz.qpic.cn/mmbiz_png/FGB4hYw9FedRZVQ5icibEeQZ1xiacLR7xpiaiaBmrPwGQ2fibrIVApI2qL5iagcGCRe7BfLwME4bVM4myRAVG6jC1IuKiaiarzhCFSYErDVoicQTXRyNk/640?wx_fmt=png&from=appmsg)

导入一个3D文件，不仅会提取常规的正交视图、几何信息，**还会使用八轴侧视图来补充被遮挡的内部结构和几何特征，同时保留全部的尺寸、公差、装配、工艺（PMI）细节。看得见内部结构，也能读懂规格参数。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9Fef8ck1d66Bo1RrqLQmNs3hq1iaZdWyzJRKbCicnsQIn77E59bpUQYzk4LHvOLyU8GGjb1oCfW2HpVszXahiaWrWHWRnUI0wtt0ZZ0/640?wx_fmt=png&from=appmsg)

解析目录

![](https://mmbiz.qpic.cn/mmbiz_png/FGB4hYw9FeeE8hEqM0lx8ju1I6iargjbLq1dfM4fVbOy0VfibGohv2UoAnM3sWTMs2a7lXN5tibkapbtFyU57ibSPhF4IVsJ26dKibzJhQAv2FR8/640?wx_fmt=png&from=appmsg)

正交六视图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FedBybB5BN3SYJYGUfsGPkZ3DUTqxwiaJh8vpuJYhhZDwlGE2I0HEP7gV9VvWyp0RfhsNadKcQhiagmCvNE8RrG6HKbp69uZNMic5g/640?wx_fmt=png&from=appmsg)

轴侧八视图

![](https://mmbiz.qpic.cn/mmbiz_png/FGB4hYw9FeevrcBOiaNzlmFmQO3stYleZPr8NficU5ESappDmAHicsIic8DN9w5YTGmcaeziaDXEjpDF2z8j3Fic01yVsLzWkiajwRtT6mhUHicBnbg/640?wx_fmt=png&from=appmsg)

信息摘要（含PMI）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FefIMbwyFkDeQkTP0iasU1QbT4KTjpgms59egAhYwHpB5LSsdK0MWmT0JhEVE98TZ2J9MyB5HQtWmf3L41Uic8iaIS25tGGhpA3yOo/640?wx_fmt=png&from=appmsg)

模型明细

左右滑动查看更多精彩内容

**二、****轴侧视图如何用｜同一类零件，识别细节差异**

以两款四方嵌件底座为例：外形完全相同，唯一的区别在内壁盲窝——**型号 1 是圆形，型号 2 是六角形。**

![](https://mmbiz.qpic.cn/mmbiz_png/FGB4hYw9FefHpG1sgiaUGhiacQoCicz3pTUqqxDOpQpzbr1ovk9To67csQib3T42lhTib0EUPicKEKHOpiabVMbRJibmibSIoYSv4aW48ibjmUU9cEUm4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/FGB4hYw9FefngKkLKhMELYPNZ8icj3Obu84Xget7Cv4j5Jiat2mk5U15EibmqJHr2OdNK131SwIKVy6Foe983nzoQTfcRdBFRy0UzpicnwwSWbg/640?wx_fmt=png&from=appmsg)

型号1 嵌件底座

型号2 嵌件底座

这个差异藏在壳体内部，正交六视图里看不到，两款零件的六视图完全一致。同样问 Agent：“帮我找一个内壁有六边形盲孔的四方嵌件底座，之前有设计过”，结果截然不同：

|  |  |  |
| --- | --- | --- |
| \_ | **只有正交六视图** | **正交六视图 + 轴测八视图** |
| **检索结果** | 无法确认，只能给出型号 1、型号 2 两个候选 | 直接定位到型号 2 |
| **判断依据** | 六视图看不到内壁孔口和孔底 | 轴测图中能看到内壁的六边形凹孔和孔底 |
| **后续动作** | 需要你逐个打开模型确认 | 无需人工确认 |

**只有正交六视图时，**Agent 找到两款外形相符的候选，但无法判断哪一款带六边形盲孔：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FefJMPwzJtAIUEWF3RctF7WUMrh1JelRq9vCd4GibKIg1Vtu0xzzP2VBc2RDBtRcz8FnRITxL6to2wlKfOrWRMDwqnXlQW3LfwjY/640?wx_fmt=png&from=appmsg)

OpenViking + Codex 检索结果：无法确认

![](https://mmbiz.qpic.cn/mmbiz_png/FGB4hYw9FeeTiby1k8QGeMRQClUb1mJ49VDxQJ4YukmN9kQLqricZstcEfICK2yDHsfjtQTehN28GiaIGcjj6HAYsNI59neO9cvXprqoBZwwkc/640?wx_fmt=png&from=appmsg)

仅保留正交六视图

![](https://mmbiz.qpic.cn/mmbiz_png/FGB4hYw9Fefe7Uz56h61tIFQxSJrFjyfAEVhv06NBRIZ0ZP6qtpwIuO8YibENYF8tZI4q85tygWm6D4cDC0H53Vx6KqsFJ5vxMwOXnECvCE8/640?wx_fmt=png&from=appmsg)

型号 1 / 2 的正交六视图一致

左右滑动查看更多精彩内容

**加上轴测八视图后，Agent 从轴测图中识别出内壁的六边形凹孔，直接给出答案：**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9Fecxaib2zsSJ7UbjkQyToNwGaecpsiaUHksVx3vOCMxSyn4KkEljhWjNj5qEI61C4VxyDth6lduRIjsUdRF9GaIGpJyCClpvIdK4c/640?wx_fmt=png&from=appmsg)

OpenViking + Codex 检索结果：直接定位型号 2

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FefHGrKRVLfq3ZdgL3Ooj3MJa4oS3g6KzfABlXicdiaXou1WckLwIhPFBrZLKJrcxL4iaT9L2yvWAYjI51YVae8AqOuQ6xzv2oOHuE/640?wx_fmt=png&from=appmsg)

正交六视图 + 轴测八视图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FedY6y8GoOyDanSZnudMWmhLyTYPx1vo9CXavuzm0icEnibj0RibLdfvUHSHQx09oicyarrzk3VVAkOaiblAf9OHd6euBxmbKbwDibXDo/640?wx_fmt=png&from=appmsg)

型号 1

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FeexCTUW7ttur1hLNA0CcDghibicvq9vkGhn4IY7gHvKImx7ubggXHOlS5lkn0Yo1yQPtPzDV633Glas5spjiaUjAaiayRicYqOBKiaNU/640?wx_fmt=png&from=appmsg)

型号 2

左右滑动查看更多精彩内容

再细节的差异也能被3D内容理解模型捕捉，Agent都能检索到。

**三、****PMI信息如何用｜提供零件规格，实现精准定位**

PMI（Product and Manufacturing Information，产品制造信息）是 3D 模型中附带的尺寸、公差、材料、工艺等制造信息。以一个基础安装座为例：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FefcxDaRYofg7I93zicYcnnbQ6yOFt26M9AfwiaAYJvn7QKib6KyuFSMEAzWcWXtvIfW6ZkmHhiaRibUviczRjONkQIlko6a0q8icWKLhE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/FGB4hYw9Fed10U1urx5albb3LFOiacwdBsFgjyAWqpyooXcZrVq9qXB9MAEJ8Vy3vDZdPvxqMS1JpD41c0tD7HhDSvuCJzWzNgYekLtAbEfA/640?wx_fmt=png&from=appmsg)

安装底座模型

PMI&模型对应关系图

OpenViking的3D内容理解模型可以对3D结构的全部PMI信息进行理解，同时区分几何、尺寸、公差、装配、工艺五个部分，自动加工到Summary.md文件中，供Agent按需读取。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FefanfPmuysVibMqObPFIQwXVZFghdX4ksryMDrjJOqp0AWCTicaZFcEewVj8tUaqhU9ic2dvgF1toQyOg7mEBlkmrUiaFt68vqKsx0/640?wx_fmt=png&from=appmsg)

几何

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9Fee1YzM8ojHqd0QFiaJX0qw8xQUAeibib8I0heaVDRibia60w0XQnBeuPYA0ADfKk1Jibiahnnvs0JIWaUdw7fvupQAW5lVf3sunYzFMKw/640?wx_fmt=png&from=appmsg)

尺寸

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FecjqpG99AJ4A7NyLRaZiarMIUWSn0Nia2q7j5mguxB43nN2vjqzX29SL7XYjVFm9BibLyl916EO4LBBEDv3AeakYLXo8haOIQ7CDY/640?wx_fmt=png&from=appmsg)

公差

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9Fee6ibNic4MKrGtfOBokb5oQEc7kkDByT87MPNTVxdkh6yn7coKmTyAUGVfsvDMFXTq7PxHoMHe2egXMUwUWI2SgLP8uLCmiaCJkB4/640?wx_fmt=png&from=appmsg)

装配

![](https://mmbiz.qpic.cn/mmbiz_png/FGB4hYw9FefMbCjWKE9oCCMLQ1vP5y2ZoTN3pATavW70vriaUGBibBWJtfuibuNczpeuWI1jo02gNOwzMjZygM7vOH4TFYmWzD023sstUm1jnY/640?wx_fmt=png&from=appmsg)

工艺

左右滑动查看更多精彩内容

当你需要找到一个精确尺寸的零件，可以问Agent：“找一个底板厚2cm，带4个直径6.6 mm安装孔的底座”，Agent 会定位到「基础安装座标品.step」，逐项对照你的要求列出零件参数——板厚 20 mm（±0.05 mm）、4 个贯通底板的安装孔、孔径 Ø6.6 mm（±0.1 mm），并标明信息来源。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FedKMe5aBSkK8wXlw2ib8ia75KSByJxoF7hthSYGTQDfA0Tu1JRkSPqgJkt3xER8uAAlmxCiaUoVH6oIFm8eicjXJogJfTL3nroia4z8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/FGB4hYw9FedZTp99R35C58a0saeU303g6JtIf8FEbTCOCl8mFMMGL64DjAIaR38zCov9OVBrK7WqP3ibLvvJLSJqFUld3Vnl6GuCqTMJsm5k/640?wx_fmt=png&from=appmsg)

OpenViking导入

OpenViking + Codex检索

**最后**

OpenViking 作为业内首个理解三维世界的 Agent 上下文数据库产品，能够完整准确理解3D模型的所有细节特征和规格参数，实现精准检索。看得见内部结构，也能读懂规格参数。现在接入，点击【阅读原文】即刻使用。

🚀 **上手试用，前 50 文档免费：**

https://s.c1ns.cn/TwLos

🌟开源 OpenViking：

访问 GitHub 仓库（https://github.com/volcengine/OpenViking），为我们点亮一颗 Star！

❓三分钟测出你是哪种 Agent 饲养员选择属于你的 OpenViking

https://blog.openviking.ai/post/should-you-use-openviking/

💬 加入飞书交流群&微信群！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FefLUsWMKoBian7GnEQhxuWWC8hia4Qv7ELM0Qkdor2os4G4B3U849BqFQZdvFwF2hV4JGiawex5hlH8r8kk6c1szSuicxibopJEAuVc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/FGB4hYw9FefSz7OhrW8n0cUjNpm7hv9ydaSZ3WY1hAt7f3l2EKkH2zuPvm3hzmz50FiaY1j362burjYQPnrNoC0CN6CVcPSCic7V6mNv3OmUA/640?wx_fmt=jpeg&from=appmsg)

点击**「阅读原文」**立即体验

预览时标签不可点

阅读原文

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhkoWTP1gVm0Lqs480XOARyoSYjPEsRVCSF35cbWIp6cliaYic8KUfNfiaSjVnruzTQUTCA0lmv9vUmw/0?wx_fmt=png)

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