---
title: AI正在悄悄改写网安挖洞的游戏规则
url: https://mp.weixin.qq.com/s/zcKZjlWU_69XAxM3puCm-A
source: Doonsec's feed
date: 2026-11-02
fetch_date: 2026-11-03T08:49:44.459007
---

# AI正在悄悄改写网安挖洞的游戏规则

# AI正在悄悄改写网安挖洞的游戏规则

原创

泼猴
泼猴

表哥带我

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/UA4ABKCY6OyVibfrQnuwUOcyTXcSnnFicMR62ZGaLhBAOmZolxeTV36sqNTqwibNVgMR97viaD8KOw1niafutm2cDg3N91SGX7KClibxQdUcYdODg/640?wx_fmt=webp&animated=1&from=appmsg)

**不知道最近挖洞的家人们有没有这种窒息感：好不容易抓了个洞，兴冲冲整理报告提交上去，第二天直接给你浇一盆冷水“重复，感谢提交”**

最近一段时间，陆续有不少厂商 SRC 选择关停或者收缩运营

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/UA4ABKCY6OxFs250Ts3oZVc34zbN3qczQTYdYrcXWRxdibt1FiaTFQZLx0q9AAC6lLZXjXINyddZ2dOUmoBJesaz1Sa3gwo9E05cpGdnHSSmo/640?wx_fmt=webp&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/UA4ABKCY6OyaYduiautn346z5zOLseQibtJ2iastDGAWIB16FjVBuBzlGO2HVf6ItTNMa2tAojALztxricIgib4v6QXl9hVnoPYm3nmfA3tSjqxk/640?wx_fmt=webp&from=appmsg)

很多自媒体复盘这件事，说法各不相同。有人说是厂商预算收紧，不想再持续承担赏金、审核人力成本；也有人觉得，是 SRC 这套 “外部白帽交漏洞、厂商花钱收” 的老模式，已经跟不上现在安全建设的节奏。

| SRC 全称 | 状态简述 |
| --- | --- |
| 平安安全应急响应中心 | 正式关停，2026.7.30 停止运营 |
| 有赞安全应急响应中心 | 暂停接收新漏洞，恢复时间待定 |
| vivo 安全应急响应中心 | 暂停接收新漏洞，平台升级 |
| 同程旅行安全应急响应中心 | 暂停接收新漏洞，流程优化升级 |
| 去哪儿安全应急响应中心 | 公开众测渠道下线 |
| 马蜂窝安全响应中心 | 长期停止对外运营 |
| 斗鱼安全应急响应中心 | 公开提交入口关闭，转为定向 |
| 虎牙安全应急响应中心 | 公开投稿通道关停，仅定向合作 |
| 苏宁安全响应中心 | 早已停止对外众测 |
| 途牛安全响应中心 | 公开提交渠道关闭 |
| 58 同城安全应急响应中心 | 对外 SRC 板块下线 |
| ...... |  |

还有观点指出，AI 大规模进场之后，整个漏洞供给端彻底变天，SRC 只是最先扛不住冲击的一环，审核速度从隔天审完到一个月都审不完。

放在几年前，撞洞当然也有，但频率没这么夸张。那时候挖洞更多靠人的思路：慢慢搜集资产、翻源码、试业务逻辑，每个人的路径不一样，挖到的东西也有区分度，同一个漏洞短时间内好几个人撞上，属于小概率倒霉事件。

现在完全不是一回事。AI 挖洞 Agent、带大模型加持的自动化扫描工具普及之后，挖洞这件事被做成了批量流水线。成千上万的人用差不多的提示词、差不多的开源扫描框架，对着同一批公开资产跑。模型本身偏好识别同类特征明显的漏洞，比如通用组件漏洞、配置错误、简单 XSS 这类门槛低、特征固定的问题。结果就是：同一个接口、同一个组件的同一个弱点，在短短几小时内，被几十上百个 AI 同时扫出来，再由不同人包装成报告提交到 SRC。

![](https://mmbiz.qpic.cn/mmbiz_jpg/UA4ABKCY6Ozc99F14NDIBlQyWrwWfOtprggPdKNB8ia64xck0LS2T7PmTlkUdrYVmnVuPZdMic4JreDwnG57iaiciavSBxOk6qt2s2EZGsxBkEzw/640?wx_fmt=webp&from=appmsg)

从各家已经更新的公告能看出来趋势：收紧 AI 报告规则、明确要求 AI 产出的内容必须人工完整复现、提供扎实验证证据，纯 AI 生成没有人工核验的报告直接拒收，甚至多次提交会限制账号；提高漏洞准入门槛，优先收逻辑类、复杂链式漏洞，弱化低危信息泄露、简单反射 XSS 这类容易批量产出的漏洞评级；还有一部分厂商，把 SRC 改成定向邀请制，不再对全部白帽开放，只邀请有持续高质量产出的研究员合作，从 “广撒网众测” 转向小范围深度合作。

客观来讲，SRC 的集体收缩，不是网安赏金模式的死刑，而是一次洗牌。AI 不是单纯的敌人，它会淘汰掉只依赖工具、缺少独立思考的挖洞方式，倒逼所有还想在这个赛道走下去的人，往更深的业务理解、更复杂的攻击链路、更独特的资产发现方向走。

---

对此`你怎么看`在评论区发表你的意见吧

其他阅读

[Claude官方扩展被投毒植入持久化SSH后门](https://mp.weixin.qq.com/s?__biz=Mzg4NDg2NTM3NQ==&mid=2247488217&idx=1&sn=389ce49437cd6b5a414c18bc051119ba&scene=21#wechat_redirect)

[【吃瓜】黑客公布美国国土安全局4.1万条信息](https://mp.weixin.qq.com/s?__biz=Mzg4NDg2NTM3NQ==&mid=2247488217&idx=2&sn=8f572d619978ad4d73843f1e2c2915db&scene=21#wechat_redirect)

[【吃瓜】无印良品泄露2726万条信息](https://mp.weixin.qq.com/s?__biz=Mzg4NDg2NTM3NQ==&mid=2247488203&idx=1&sn=cdf85e55414edcec4dcd182168aba91c&scene=21#wechat_redirect)

[【吃瓜】冰箱也能被黑](https://mp.weixin.qq.com/s?__biz=Mzg4NDg2NTM3NQ==&mid=2247488197&idx=1&sn=4049fbf054b477a035f58eb50cd7803e&scene=21#wechat_redirect)

[【吃瓜】朝鲜黑客盗走交易所60亿美元](https://mp.weixin.qq.com/s?__biz=Mzg4NDg2NTM3NQ==&mid=2247488197&idx=2&sn=7213e22ab5b2ccd819fbb725858fdb64&scene=21#wechat_redirect)

[【吃瓜】补天刷怪笼刷出开盒怪](https://mp.weixin.qq.com/s?__biz=Mzg4NDg2NTM3NQ==&mid=2247488081&idx=1&sn=e9c0a4cd721d1aae8a8ff435889fea76&scene=21#wechat_redirect)

[PingCAP泄露10.6T数据](https://mp.weixin.qq.com/s?__biz=Mzg4NDg2NTM3NQ==&mid=2247488070&idx=2&sn=a20a3f36e61bd6f903e35773c30cdf0c&scene=21#wechat_redirect)

[【吃瓜】耐克盒马等账号发淫秽事件梳理](https://mp.weixin.qq.com/s?__biz=Mzg4NDg2NTM3NQ==&mid=2247488016&idx=1&sn=c1af2be1807753b41b47919cb6ae56ae&scene=21#wechat_redirect)

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/pxKqYxJWy7PW1JR7KU1wRqvaNyp3ESh9m1FzIau0Uqvh7DDnryFJCzq3u7sc2J8wAtOffybvhBgkQW1CfJs9sg/0?wx_fmt=png)

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