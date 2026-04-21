---
title: ICP-CAT—工某部备案资产提取插件
url: https://mp.weixin.qq.com/s/DbwOIw2iuzi4TasR4M9b5Q
source: Doonsec's feed
date: 2026-04-20
fetch_date: 2026-04-21T04:47:34.974053
---

# ICP-CAT—工某部备案资产提取插件

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/pgh9MpJCA6jmEbbpFpB40oHCw6j3DiaQzpoC0y1OTiaJSu46xia1V8uiaB5t68CeR2j9wS7ctEOhlNGUdMYBL1QUSF8IXF2JKQliak1ZTk8ZzJOo/0?wx_fmt=jpeg)

# ICP-CAT—工某部备案资产提取插件

原创

kuki
kuki

Heri76安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

背景：

今天给大家分享一款自己写的谷歌浏览器小插件，在平时的攻防、挖掘SRC的过程中，需要收集目标公司的备案资产，有的攻防就很认工信部官网备案的资产，随着互联网资产的快速更替一些非官方的icp备案网站上备案的资产已经不在官方备案列表里了，这时候就需要自己手动去工信部官网https://beian.miit.gov.cn/去查询，面对防守严密的滑块验证码一个一个点手都要得腱鞘炎了！！

之前和 地图大师 学了一招是通过抓包然后将响应包放到icp备案资产提取器.html里正则匹配出域名和IP，再一键复制。对于我这种经常打攻防的懒蛋来说还是过于麻烦。于是写了一个浏览器插件来提取备案资产。

# ICP-cat

```
https://github.com/yingfff123/icp-cat
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pgh9MpJCA6iamHibXP8eK7acnY8IyBKLhlZTHj9D7Nha2fFo6xxnbLXXlRakY1icCj7OyAZZZict4iblBticesSE00sbqKq1ribUsNYC1XjiagklUf0/640?wx_fmt=png&from=appmsg)

使用方法：

1. `打开https://beian.miit.gov.cn/`
2. 点击扩展图标打开弹窗
3. 打开“监听”开关
4. 在备案页面执行查询
5. 查看窗口中的提取结果
6. 如果多次查询或分页结果，扩展会自动累加并去重
7. 可以使用“复制”按钮导出当前标签页内容，或使用“清空”按钮重置结果

> 注意1：受工信部备案网站分页规则，单次通常最多只能返回10条备案资产。对于备案资产分区的目标，可以在查询结果页面中继续点击不同页面码，插件会自动累计后续限制页面中的域名与IP导出结果。
>
> 注意2：当前版本暂不支持小程序/APP相关资产的提取，仅支持域名与IP地址提取。

![](https://mmbiz.qpic.cn/mmbiz_png/pgh9MpJCA6hzM2F6CMgImQuHzzotrxIFjtAp9EpCbJ30jseibZX6wxAZ1KusQll9rqPsUay69VCmvL2uEJiaWetaxBibKFybrLcUXJDhy6j6MI/640?wx_fmt=png&from=appmsg)你不清除的情况下可以对多家公司的查询资产进行叠加。

## 工作原理

扩展由 4 个主要部分组成：

* `manifest.json`

+ 定义扩展权限、注入规则和弹窗入口

* `content.js`

+ 注入页面脚本`injected.js`
+ 通过`window.postMessage`发布的数据接收页面
+ 将响应数据转发到后台

* `injected.js`

+ 运行在页面上下文中
+ 重写`window.fetch`与`XMLHttpRequest`，拦截目标接口响应

* `background.js`

+ 接收响应数据
+ 提取域名/IP
+ 去重后写入 `chrome.storage.local`

如果对这这个插件感兴趣的师傅可以试用一下。

本项目仅用于技术研究、学习交流、接口调试与合规安全测试目的。

本项目不会主动绕过身份认证、访问控制、频率或其他。用户不得将本项目用于任何未经安全授权的数据采集、批量抓取、商业化机制抓取、干扰目标服务正常运行、侵犯他人合法权益或其他违法限制用途。

另外，需要参加护网师傅可以查看下方文章投递简历

[【通知】各位白帽子注意，2026国家HVV招聘开始！](https://mp.weixin.qq.com/s?__biz=Mzk2NDUzMjgxOA==&mid=2247484891&idx=1&sn=d8fbe23bad3f15621890320700ebd819&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/AqssE4sA0pxLFhcrEGPTHJEnribLEOoAdRM12swib4SQn8m8hqCafod9K6VAye42u4vuke0nqJWG8BFVTYZxT3mQ/0?wx_fmt=png)

Heri76安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/AqssE4sA0pxLFhcrEGPTHJEnribLEOoAdRM12swib4SQn8m8hqCafod9K6VAye42u4vuke0nqJWG8BFVTYZxT3mQ/0?wx_fmt=png)

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