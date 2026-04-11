---
title: 国家网络安全通报中心：近期集中爆发多起供应链投毒攻击事件，涉及开源软件仓库和商用工具两大场景
url: https://mp.weixin.qq.com/s/H_TOMqn4hcdcwaZ6UnUU9w
source: Doonsec's feed
date: 2026-04-10
fetch_date: 2026-04-11T04:20:22.842704
---

# 国家网络安全通报中心：近期集中爆发多起供应链投毒攻击事件，涉及开源软件仓库和商用工具两大场景

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/2ZmL5d0ic88XygLYQMPS0HvCsibKQODZGVlE5zbukOGIqibOxu6hz12levgjicjfHcKcpicSezlJZQiabvTf6icr5xzA46h73QY0tzicHsjpXODRVYw/0?wx_fmt=jpeg)

# 国家网络安全通报中心：近期集中爆发多起供应链投毒攻击事件，涉及开源软件仓库和商用工具两大场景

内生安全联盟

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/2ZmL5d0ic88XTHK7yaEiagKmpvFoLU9m4bs7Qf6uldH0ymATI9QxpPPyEokmoOhtI7sMu5kcQTWcBneTFemVblDY4EZHQqeTuAicRZbdXeicgug/640?wx_fmt=gif&from=appmsg)

据国家网络安全通报中心微信公众号消息，国家通报中心监测发现，近期集中爆发多起供应链投毒攻击事件，攻击目标包括API研发工具Apifox、Python开发库LiteLLM以及JavaScript HTTP库Axios，涉及开源软件仓库和商用工具两大核心供应链场景。

其中，Axios投毒事件因OpenClaw等大量AI应用及插件生态直接依赖该库，导致风险通过依赖链向终端用户进一步蔓延。三起供应链投毒事件呈现攻击隐蔽性强、影响范围广、危害程度高和传播速度快的共性特征，可造成凭据遭窃取、远程代码执行和敏感数据泄露等严重危害。

01

供应链投毒风险分析

一是攻击对象聚焦重点用户。开发运营人员往往拥有较高系统权限与密钥访问能力，使供应链投毒攻击具备较高潜在收益。

二是攻击路径隐蔽易于扩散。投毒攻击通过账号劫持、上游依赖污染或发布渠道篡改等方式实施，无需用户主动交互即可触发风险，并可向下游环境快速传播。

三是攻击危害呈现放大效应。单次投毒事件可进一步引发横向移动与二次投毒，使影响范围由开发者终端扩展至单位生产环境及核心业务系统。

四是攻击检测阻断难度较大。相关恶意代码普遍采用混淆、自清除及反调试等技术手段，部分攻击还结合隐蔽通信机制运行，显著增加安全检测与拦截阻断难度。

02

供应链安全防护建议

当前，供应链安全事件已从偶发性风险演变为常态化、精准化的安全威胁，建议广大开发运维用户加强安全防范。

一是甄别安装来源渠道。仅从官方仓库、官方渠道下载安装包和工具，谨慎下载安装第三方镜像、网盘、论坛等不明来源资源。重要组件建议使用稳定版本，初次安装或者更新前应核对官方发布的校验信息，确保未被篡改。

二是加强开发环境管理。为不同项目搭建独立运行环境，避免将开发运维环境直接暴露在互联网，减少恶意代码获取系统权限、窃取信息或破坏文件的可能，不随意执行未知命令。

三是强化风险防范处置。关注供应链官方安全公告和权威部门发布的安全预警信息，及时采取安装补丁、升级版本、更新配置等方式消除危害影响。官方未发布漏洞补丁前，可按规范操作回退至历史稳定版本，并清理本地缓存文件，防止恶意程序驻留。

来源：“国家网络安全通报中心”微信公众号

[![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2ZmL5d0ic88UR6icztiaMDcvGBs077WN4FIDNT7bJkZ4NKH5o7uRIGIzibFZa2mq1qXCzmtBEz8ICcicPia9n64FMynVib4bjvbnZCppHQ1Z5TpIkQ/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=9)](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247537006&idx=1&sn=47b4fd64c51fd886882eba9f2755bd0a&scene=21#wechat_redirect)

[安测促发展，积聚创未来——2026网络通信安全融合生态创新发展大会在宁举行](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247537006&idx=1&sn=47b4fd64c51fd886882eba9f2755bd0a&scene=21#wechat_redirect)

[![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2ZmL5d0ic88WjwEF932bqbsMPq0DTA9D2YkakBfmTLKazcj1TV2FCpaSMerCv4bCfffibN5lN92u3woYmLXauY5iazscibMiaXvuVD6xxNSGszGM/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=10)](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247537051&idx=1&sn=cd6f6b480f3b1cafb714df95f3132ae1&scene=21#wechat_redirect)

[征集标准参编单位！关于征集《消费级无人机检验检测通用要求》认证认可行业标准参编单位的通知](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247537051&idx=1&sn=cd6f6b480f3b1cafb714df95f3132ae1&scene=21#wechat_redirect)

****热点聚焦****

****HOT！！****

**[邬江兴院士：AI内生安全问题及可信应用系统研究](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247524079&idx=1&sn=f4e4c0da54b241108c7940047ee1be77&scene=21#wechat_redirect)**

**[征稿启事 | 16个热点问题，欢迎来稿！](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247521812&idx=1&sn=df8ac4f4f7071445227e454703cf3eac&scene=21&token=891324421&lang=zh_CN#wechat_redirect)**

**[新书出版 | 邬江兴院士发布最新英文著作](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247525711&idx=1&sn=7c47de2a92853e19af33b0c0ff76063e&scene=21#wechat_redirect)**

**[可信内生安全、变结构拟态计算技术等入选“新一代信息工程科技新质生产力技术备选清单（2024）”](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247524134&idx=1&sn=e8f83445d7ea448a8ea38a06e228f77c&scene=21#wechat_redirect)**

**[持续赋能内生安全！第五届网络空间内生安全学术大会暨第八届“强网”拟态防御国际精英挑战赛完美收官](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247534994&idx=1&sn=a35dc208810295861b94d6af88c2c7e8&scene=21#wechat_redirect)**

[蓝皮书下载 | 第五届网络空间内生安全学术大会，四本蓝皮书重磅发布](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247535240&idx=2&sn=da33dc8d3ad64e3c161538e0d3a14494&scene=21#wechat_redirect)

**[正式发布！网络空间内生安全理论和标准体系入选信息通信领域十大科技进展（附手册）](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247527344&idx=1&sn=b9f70ff5f052f6866645a8bc506f43bd&scene=21#wechat_redirect)**

**[递交2025网信生态高质量发展“开年答卷”  网络通信安全融合生态创新发展大会在宁举行](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247528656&idx=1&sn=28c73aa522cb86038989efae1f2c8ee2&scene=21#wechat_redirect)**

**[邬江兴院士为五色石先导班学生授课](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247530005&idx=1&sn=ae066476dfc29be0b0d528a64e6b6679&scene=21&token=891324421&lang=zh_CN#wechat_redirect)**

**[邬江兴院士——AI时代内生安全自主知识体系建设的思考](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247534787&idx=1&sn=3e2e3df01300637de00f028894fd6493&scene=21#wechat_redirect)**

**[出版啦！南京市网络空间内生安全协会5项团体标准在中国标准出版社正式出版](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247534684&idx=1&sn=1814c0aed65128d0e345064e5b7b83d1&scene=21#wechat_redirect)**

**[邬江兴院士 | 破击美欧网络弹性铁幕——基于自主知识技术体系的数字生态系统底层驱动范式变革](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247533711&idx=1&sn=7a843b5f85bfce11554c51cb97c5e1f0&scene=21#wechat_redirect)**

**[喜报！南京市网络空间内生安全协会获评为AAAA等级社会组织！](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247535467&idx=1&sn=343185d42eca10a491337f0111035b24&scene=21#wechat_redirect)**

**[邬江兴院士提出“时空协同复杂度”理论——揭秘介观尺度智能涌现机理引领AI架构革新](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247535842&idx=1&sn=bf905ee97eb951d993e28c518e8adf67&scene=21#wechat_redirect)**

**[南京市网络空间内生安全协会第二届会员大会暨换届选举大会圆满举行](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247536554&idx=1&sn=e7d5d716f55a62c9f64360c2a527d45d&scene=21&token=891324421&lang=zh_CN#wechat_redirect)**

****| 往期回顾****

**[AI4E如何重构数字生态系统网络发展范式？](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247532455&idx=1&sn=ee5102d94087e9440ede67b18386c621&scene=21#wechat_redirect)**

**[资料下载 | 十五五规划建议全文及说明](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247534593&idx=2&sn=7f9516f40cbafbcb1012d5999612157a&scene=21#wechat_redirect)**

**[邬江兴院士：人工智能内生安全质量检测中试平台](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247536446&idx=1&sn=0ede0c81fb0d67df45be75a62e84b87b&scene=21#wechat_redirect)**

[仅凭一份漏洞公告，Claude 4小时攻破全球最安全系统](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247537168&idx=1&sn=099a6c0daa36a45a470b116272949219&scene=21#wechat_redirect)

[李强签署国务院令 公布《国务院关于产业链供应链安全的规定》](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247537182&idx=1&sn=15516a135f123bff06b49e4237e4e902&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/jRRfTC292pXGqHBACsK1cVtpyTB5F8VFsEY3paWnfS3dichupP4OknoSrNN3c6YviaDsLwKnfHwj1OibB7lWFvbibQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=1)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/jRRfTC292pX7QK5QfSb6k3uQJ3EsDmeCnsG6veyEXTXsbCcuuTJ7LWzo0tPv2ezibrAF07JXGxYs8zSXgXibLX2Q/0?wx_fmt=png)

内生安全联盟

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/jRRfTC292pX7QK5QfSb6k3uQJ3EsDmeCnsG6veyEXTXsbCcuuTJ7LWzo0tPv2ezibrAF07JXGxYs8zSXgXibLX2Q/0?wx_fmt=png)

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