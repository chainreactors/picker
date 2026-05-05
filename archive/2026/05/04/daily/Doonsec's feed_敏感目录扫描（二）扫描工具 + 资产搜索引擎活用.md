---
title: 敏感目录扫描（二）扫描工具 + 资产搜索引擎活用
url: https://mp.weixin.qq.com/s/LROf573tUeBXt1pG3Fyx_g
source: Doonsec's feed
date: 2026-05-04
fetch_date: 2026-05-05T05:00:17.876844
---

# 敏感目录扫描（二）扫描工具 + 资产搜索引擎活用

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/3PxWhY8513bDoztRtckbscbzaP2PO3biaicrcGhJ31K8ECh8mkzYAicTUg5At0v0PlagYmaXkwe4BbLnvQS4icuRy5mSwPMsK2aiboSwd8zicEcwo/0?wx_fmt=jpeg)

# 敏感目录扫描（二）扫描工具 + 资产搜索引擎活用

原创

皮皮宋
皮皮宋

皮皮宋渗透笔记

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

一篇我们掌握了手动寻找敏感目录的各类思路，适合精细化、低流量探测。但面对大型站点、多级目录、批量资产检测时，纯手动效率极低，这时候就需要依靠专业目录扫描工具，借助高量级字典、多线程请求，快速批量探测开放目录与遗留文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3PxWhY8513aDhNl96z1SyyAvBqZD2tTibYyOIklYOBBicRonXqGFxDogwT3WdbYUdr4qa8DV8Lmje9LkRDz0mHjAAYfM0kvhTWObUJ9ibc4BKg/640?wx_fmt=png&from=appmsg)

# 一、目录扫描工具核心要求

一款合格的目录扫描工具，必须满足三个条件：

* 支持多线程并发，扫描速度可控
* 内置 / 支持自定义大字典，覆盖常见路径
* 容错性强，降低 404 伪装、页面跳转带来的漏报

# 1. 经典工具：Dirsearch 实操

Dirsearch 是目前渗透圈使用最广的开源目录扫描工具，轻量化、易上手、功能全面。核心常用参数：

* -u：指定目标 URL 地址
* -e：限定扫描文件后缀，精准过滤
* -r：开启递归扫描，自动遍历子目录

简单理解：设定好目标与规则后，工具会自动拼接字典路径批量请求，快速筛选存在的敏感目录、备份文件、后台地址。

# 2. 全网主流目录扫描工具合集

整理日常实战高频用到的工具，按需选择即可：

* Dirsearch：通用型 Web 目录扫描，新手首选
* Gospider：高级爬虫 + 目录探测，适合复杂站点
* Dirmap：智能分析站点架构，低漏报深度扫描
* Cansina：轻量敏感文件探测工具
* 御剑后台扫描：国产工具，专门针对后台地址批量扫描
* DirBuster：经典老牌目录爆破工具

---

# 二、搜索引擎语法信息搜集

搜索引擎不只是用来查资料，更是免费、无痕迹的信息搜集利器。通过定制语法，可以精准过滤全网收录的敏感页面、泄露文件、后台路径。

| 搜索语法 | 实战用途 |
| --- | --- |
| site | 限定指定域名，聚焦目标资产 |
| inurl | 匹配 URL 包含指定关键词（admin、login 等） |
| intext | 匹配页面正文关键字，搜集泄露内容 |
| filetype | 筛选指定格式文件：bak/zip/sql/conf |
| intitle | 匹配网页标题，快速锁定后台登录页 |
| info | 查询站点基础备案、服务器信息 |
| cache | 读取搜索引擎历史缓存，挖掘已删除文件 |

普通通用引擎：百度、Bing、Google

资产测绘引擎：FOFA、ZoomEye、Shodan、Censys

这类专业引擎远强于普通搜索，会持续全网抓取端口、服务、组件、标题、证书等指纹，是横向资产搜集的核心利器。

以 FOFA 为例，通过组合语法，可以批量筛选同架构、同服务器、同城市的所有资产，快速拓展测试范围。

---

# 三、Burp Suite Repeater 信息挖掘

Burp 不只是抓包改包的工具，在信息收集中也作用巨大。通过抓取网站原生请求与响应包，可以直接获取：

* Web 容器版本（Nginx/Apache/Tomcat）
* 运行语言及版本（PHP、Java）
* 服务器系统指纹、中间件信息
* 隐藏接口、未公开路由、内网代理地址

根据服务版本，我们可以快速匹配对应历史漏洞、弱口令风险、组件缺陷，做到针对性测试，不再盲目扫描。

---

# 四、GitHub 源码泄露搜集

开发人员不当上传代码，是企业最常见的泄露源头之一，源码、账号密码、数据库配置、内网地址极易直接暴露在代码仓库。

# 1. 手动搜索语法

掌握关键词规则，即可精准检索敏感仓库：

* in:name 匹配仓库名称关键字
* in:description 匹配项目介绍
* in:readme 匹配项目说明文档
* repo:xxx/xxx 指定目标仓库精准检索

搭配password、db、config、database等关键词，很容易挖到核心配置文件。

# 2. 自动化搜集工具

批量爬取代码平台敏感信息，适合批量资产检测：

* GitPrey
* GSIL
* Gshark
* theHarvester

---

💡皮皮宋小结

工具可以提升效率，但不能完全依赖。字典质量、请求频率、网站 WAF 防护、404 页面伪装，都会直接影响扫描结果。

下一篇，我们重点讲解旁站、C 段横向渗透思路，主站打不穿时，靠横向资产突破，完整打通目录搜集全流程。

感谢您抽出 ![图片](https://mmbiz.qpic.cn/mmbiz_gif/jzC1MZl7uvpkwDV3NcrFRpT6QRJSY1j2fmBhd9q58lS5Y7AD6wFEcDwATcl4EE4opylqeM9SfvgqfPhuyibX68w/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp) ![图片](https://mmbiz.qpic.cn/mmbiz_gif/jzC1MZl7uvpkwDV3NcrFRpT6QRJSY1j2ibfVug8UCLkFuUujUoSyOXh5CqOQCEKIcfKnW1GQ44x9Ne70wEdZfag/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)·![图片](https://mmbiz.qpic.cn/mmbiz_gif/jzC1MZl7uvpkwDV3NcrFRpT6QRJSY1j2uXNXnTIfFfy57Se7rsutTQf1dl4F9IWEs68rhI1h92t0dMmVCFfu2Q/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp) ![图片](https://mmbiz.qpic.cn/mmbiz_gif/jzC1MZl7uvpkwDV3NcrFRpT6QRJSY1j2BoAnxnn1vrz1ZNoqcUckl4UCVfhTOsCy3meVib6Bc8juibR7LEZqWO1g/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)来阅读此文，觉得不错的话记得点个赞和在看

![](https://mmbiz.qpic.cn/mmbiz_gif/3PxWhY8513bsCAJic7zCKv1WWR9cxMiaHJ86FnEBgvJHR3FzbusGJpCqiaYRzqhv6qeHUyJ2aNfcn4VgbvSOdTIaR6YlSAVMYvLa9TTXRhiaNiaY/640?wx_fmt=gif&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/CrpWk11pwIicrkmF1ZAbZl48vjGQFt5MKRmdXeAcNxicBjVnQqx3DYUqGd2UhqveP86KHpS0CYUoSia6QAF01kVhw/0?wx_fmt=png)

皮皮宋渗透笔记

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/CrpWk11pwIicrkmF1ZAbZl48vjGQFt5MKRmdXeAcNxicBjVnQqx3DYUqGd2UhqveP86KHpS0CYUoSia6QAF01kVhw/0?wx_fmt=png)

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