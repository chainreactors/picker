---
title: Hugging Face vs ModelScope：两大开源模型平台深度对比与高效下载指南
url: https://mp.weixin.qq.com/s/mY60NHN1OI2hQWpdvs1Muw
source: Doonsec's feed
date: 2026-06-21
fetch_date: 2026-06-22T07:14:55.786454
---

# Hugging Face vs ModelScope：两大开源模型平台深度对比与高效下载指南

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/RJrNBTwulvcWm35bD11sZ3WicvngibLyJUSQCpuOXOAI0my1sDWO689S5RbJtOWQj6aib8dfQz6GjBcB1OC5rCghib2C8KAuzkmRjnPBXWmECDQ/0?wx_fmt=jpeg)

# Hugging Face vs ModelScope：两大开源模型平台深度对比与高效下载指南

原创

一只岸上的鱼
一只岸上的鱼

一只岸上的鱼

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 缘起

最近连续看到好几篇博文，关于在8g显存的电脑上运行本地大模型的帖子，好想试试。

本来想着，等等价格降一点，买个二线的5080，有个16g，或者至少5070ti，有个12g，但是现在看来，短时间内没希望了，九年本子涨的太疯狂了。

索性就5060吧，尝试一下，等俩年，大模型再发展一下，电脑再降价，再换一个大显存的。

这是我乘着618换的本子：

![](https://mmbiz.qpic.cn/mmbiz_png/RJrNBTwulvdg2N0gcX7xibFZD5Xaicy2xZAwAFqDfVOoPdFOrD5ZERr5PjBLOwPd40p9r5OKTPOcsOIOsoqdkicGeSzURJBKFMYiaSCxQGAib2Gw/640?wx_fmt=png&from=appmsg)

今天先研究一下如何下载模型文件。

## Hugging Face vs ModelScope

### Hugging Face

Hugging Face通俗翻译抱脸（字面翻译），始于2016年，在开源大模型绝对有着全球影响力，他不仅提供了大量的预训练的模型，还有大量的公开数据集，甚至还提供了很多免费的算力和空间，关于他的免费资源，我还曾写过：

[抱脸的免费资源值得找私网去访问么](https://mp.weixin.qq.com/s?__biz=MzA3MDg4MjA4Mw==&mid=2649650641&idx=1&sn=67669a4fa91a2cb33985eca101848a4f&scene=21#wechat_redirect)

### ModelScope

中文名魔搭，是猫厂（阿里巴巴）于2022年推出，定位更聚焦于**中文场景下的模型工业化落地，**也有大量的模型文件，数据集。

## 安装和使用

### Hugging Face

在powershell下安装：

```
irm https://hf.co/cli/install.ps1 | iex
```

抱脸毕竟是国外的网站，正常下载几乎无解，好像下载工具有镜像可以用：

```
$env:HF_ENDPOINT="https://hf-mirror.com"
$env:HF_XET_HIGH_PERFORMANCE="1"
```

试试下载效果：

```
hf download "yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF:Q4_K_M" --local-dir D:/model
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RJrNBTwulveriaby9pbsWNVl9bUGP1NHOKg1GRibbW5F10zDjHbL8ewlFUEqhWGNpUh8mW1iaWMzz4DXVrDiavmLPPBFb7NgmcfDIUvTQQ2P9iaY/640?wx_fmt=png&from=appmsg)

总的来说，速度还可以

### ModelScope

魔搭直接用pip安装

```
pip install modelscope
```

试试下载效果：

```
modelscope download --model unsloth/Qwen3.6-35B-A3B-GGUF Qwen3.6-35B-A3B-UD-Q4_K_M.gguf --local_dir D:/model
```

![](https://mmbiz.qpic.cn/mmbiz_png/RJrNBTwulvcmmnpWQdfn1BkFjFKibLvcI0YnbqA6hSJXqfEKkCWMTgSXibwIkeJPEqT2GazSibQLplibRAX5fguQ8aALKkSZrFaezbDsfEqbNso/640?wx_fmt=png&from=appmsg)

速度还是特别好的！

## 小结

推荐下载的顺序：

1. 魔搭
2. 抱脸（镜像存在的情况下）
3. 抱脸（国内镜像可能没有，直下，速度以k计，建议使用特殊方式，或者放弃等魔搭）

模型终于下完了，下载了2个，一个是Qwen3.6-35B-A3B，一个是gemma4-12b,等我测试的消息😄

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/ZG8Fru1tL1whh58JUwn0GLYzvqhGcECfmoW1O5J0JY0h7tksUWibmqwhwmEkL7kf1TTb37avJialEYsc7GfDhBCw/0?wx_fmt=png)

一只岸上的鱼

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/ZG8Fru1tL1whh58JUwn0GLYzvqhGcECfmoW1O5J0JY0h7tksUWibmqwhwmEkL7kf1TTb37avJialEYsc7GfDhBCw/0?wx_fmt=png)

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