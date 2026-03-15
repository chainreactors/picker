---
title: 哥斯拉反射自定义 AES 通信插件加密器，基于Data-Flow Break与动态回调伪装的webshell生成器
url: https://mp.weixin.qq.com/s/pRZncXfzx7cknq_mEMOTPA
source: Doonsec's feed
date: 2026-03-14
fetch_date: 2026-03-15T04:30:52.274813
---

# 哥斯拉反射自定义 AES 通信插件加密器，基于Data-Flow Break与动态回调伪装的webshell生成器

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6MNVTibIPy2tGzP71uLnlXGHlGZS8yWsDHVIRbhdynLfZ1nAiclmibRrTUrBvBzhibBJPdwcia2nt80QZusRTTydcQ1owgIBIxZiaJM0/0?wx_fmt=jpeg)

# 哥斯拉反射自定义 AES 通信插件加密器，基于Data-Flow Break与动态回调伪装的webshell生成器

黑白之道

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/3xxicXNlTXLicwgPqvK8QgwnCr09iaSllrsXJLMkThiaHibEntZKkJiaicEd4ibWQxyn3gtAWbyGqtHVb0qqsHFC9jW3oQ/640?wx_fmt=gif)

## 工具介绍

VeilShell，Godzilla\_AES加密器+采用打断数据流（Data-Flow Break）与动态回调伪装的 WebShell|Qwen2-0.5B-Instruc-webshell微调小模型检测方法与对抗。

插件是基于哥斯拉底层反射的自定义AES通信加密器，phpwebshell则基于AES + gzdeflate+Data-Flow Break

![图片](https://mmbiz.qpic.cn/mmbiz_png/WibL3bOeESMJicOpKASakahshSaHwu2j8OhR2ep4PibTl5fSgKTTdp4kuWib4y8uIZibibGEHiatqa5crRLCIXVicOBCLpwfAatIMIPKPe2jP8FQoBM/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=1)
> 本项目生成的荷载在Qwen2-0.5B-Instruct模型中经过30k webshell数据集训练微调后的小模型分析，并未命中。同时在长亭、阿里等webshell检测中也绕过。

## 免杀效果

注：该图展示的样本是二次过滤后的恶意样本，选了40+能过waf的phpwebshell进行测试。并不代表全量训练数据集，全量数据集采用了https://huggingface.co/datasets/nbuser32/PHP-Webshell-Dataset

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/WibL3bOeESMItS5Lx9FekxaCS8VOp47MJbsXuGgMdKpOtbmD9C12KRC7MnYBYzl2J9T5JxCc7TkOIxoibqZjt1e0hdkROLXgJdMB3xoSTkD7Q/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=2)![图片](https://mmbiz.qpic.cn/mmbiz_png/WibL3bOeESMKbh6icWqibNiaWG2GnyPoaib23745g3OcNzk8JFiatt12IibZC2y57kUyBJ3nFI3cHopFb4CEHDCCcq4WuCzNTpq0HN1lguYKgNbiafg/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=3)
> Test metrics: {'test\_loss': 0.08689013123512268, 'test\_accuracy': 0.973571192599934, 'test\_f1': 0.9750623441396509, 'test\_precision': 0.993015873015873, 'test\_recall': 0.9577464788732394, 'test\_runtime': 71.2095, 'test\_samples\_per\_second': 42.508, 'test\_steps\_per\_second': 2.668, 'epoch': 1.0}

### 长亭

![图片](https://mmbiz.qpic.cn/mmbiz_png/WibL3bOeESMJHUHgJsBfJicKmefX61yConFtiaRwO3ejcibg375Jyl5E88KEPaLyNchyaUaTjx2H3BN61OVvfJEJGFfwcl6zJa6VRkTO7BZXwzc/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=4)

### 阿里

![图片](https://mmbiz.qpic.cn/mmbiz_png/WibL3bOeESMIc0geiaN1NuW3Ud8Emw0saSibfpSN10LGw6AzX6fcCEiazjYhQSSdnxM1ULCS7M2CrgSTsx8l8iaDhjqRGCldMz7okaQYD8JVZYf4/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=5)

### virustotal

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/WibL3bOeESMJlq2XtOmJ7vQCGiatLUlZK7zclK4Q9l8ibnZvh6ekCcH5YJLdOibjxdYicfqs00b76CUIeXP8ibnEu70neu00PgibIwQz7MFVsKQh94/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=6)

正常连接及环境：

![图片](https://mmbiz.qpic.cn/mmbiz_png/WibL3bOeESMJdUNOh6US2fvBF0VAIxyVdJYWopSVBKMibQlVJeG0MPLcFrGtaW9JkkraVADuOcAYXhHCANU7kib03554LgNPg32pjKmas7WbWs/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=7)

### post

![图片](https://mmbiz.qpic.cn/mmbiz_png/WibL3bOeESMKMMp5OXibJArogM81HFfw6CjsPh5Pg1XSvDTKicY5NecD7k8c3u7a6FR3akC6ICyRTZ86npQs4qYFnvCTkOaybTOm5vW2UrQctY/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=8)

## 工具获取

https://github.com/e1arth/Godzilla\_bypass\_webshell

> **文章来源：夜组安全**

黑白之道发布、转载的文章中所涉及的技术、思路和工具仅供以安全为目的的学习交流使用，任何人不得将其用于非法用途及盈利等目的，否则后果自行承担！

如侵权请私聊我们删文

**END**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

黑白之道

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

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