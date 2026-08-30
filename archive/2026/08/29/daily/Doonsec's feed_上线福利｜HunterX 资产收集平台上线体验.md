---
title: 上线福利｜HunterX 资产收集平台上线体验
url: https://mp.weixin.qq.com/s/r_YqkBueaGRPbsqvCuSbOw
source: Doonsec's feed
date: 2026-08-29
fetch_date: 2026-08-30T07:40:54.230534
---

# 上线福利｜HunterX 资产收集平台上线体验

# 上线福利｜HunterX 资产收集平台上线体验

菜狗安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

以下文章来源于Daylight庆尘
，作者庆尘

![](https://wx.qlogo.cn/mmhead/OM4v0FU2h0s97hBneksdKoudzI5qAtzW7vQkBZYfJUTGnoBob4kroP77siaBiapntIBYJ6PKDaXbQ/0)

**Daylight庆尘**
.

专注于代码审计与企业SRC漏洞挖掘思路与案例分享，想了解SRC漏洞挖掘培训的可以联系我，本人亲带

依旧先看图

![](https://mmbiz.qpic.cn/mmbiz_png/9chXicZO71s57Cf0ibELYeRf0pSNW4LFrqTiaDOlegVILJzTTib0tINQYwicwLWFlgZHSltMeY3a8Znkq0iceM2NeWuja6lKnKm5QchpzhGOM71GE/640?wx_fmt=png&from=appmsg)

盒子目前赛季第一

![](https://mmbiz.qpic.cn/mmbiz_png/9chXicZO71s4ekT2BEXSlKW4TOjUgbtuvpMu9AjDLjm3V0aKnF9WbIvNSVUgO4cuzicexHTicYORSWxbrgf7icMVu3xGFdFlXOzZ37wicxWzGAtU/640?wx_fmt=png&from=appmsg)

所有漏洞都是这周（盒子赛季8月25开始）用AI挖的，不需要多说，AI 渗透的能力大家都看到了，当然，我发这些不是为了卖课，其实我觉得AI自动化渗透的学习周期很低，只要是个之前挖过漏洞的人，只要知道怎么用，其实很快就能上手，从opencode，zcode等各家自己的cli，以及各个厉害的开源渗透项目，比如黑客松前几名的项目二开出来的各种产品都可以作为渗透能力的载体，可以快速体验到AI挖漏洞的能力

但这里有个问题，说到AI测试能力，师傅们最主要的第一反应是什么，是SKILL，是项目架构，是工作任务流，这些就决定了你的AI自动化挖洞能力。对于大多数人来说AI挖洞的能力区别对独立站点来说大差不大（各种大牛的除外）。 你会调教 AI，别人也会；你用最强的模型，别人换个模型一样打。当大部分人的“测试能力”被 AI 拉平之后，拼什么？拼的就是资产。所以我尝试收集到更多，更全的资产，但各种渠道的资产，总有普及不到的地方，比如hunter有的资产quake没有，quake有的资产fofa没有，fofa没有的资产在bing上有，如何能最大限度的获取到资产呢，我的答案就是写一个自己的资产搜索平台，尽最大能力进行资产收集，所以我花了一个月完成了我的新资产收集平台，HunterX

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9chXicZO71s5VcHNYVSLn0nP92wChcal8QZ7IGrecicLDkmDthPADBnx3jAnUra2CuBXD2KvOAICZIMv4wzJH7GkgLncZPqJC62mxlLOniaWC4/640?wx_fmt=png&from=appmsg)

项目参考如下文章（感谢kk师傅的思路分享）

[怎么做好资产信息收集](https://mp.weixin.qq.com/s?__biz=Mzg3Mzg0NDcxMA==&mid=2247483794&idx=1&sn=f4c087078afee5aa09e33e5e1711e130&scene=21#wechat_redirect)

融入了项目中多个思路，例如扫描探针，403分类识别，影子资产，B端主动探测等

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9chXicZO71s5rvxs4N8kMApvZf3Olm4vSM08ia9CITRcbT3o00TFVjsZI8prdq635ia469E4kQpAetbEvjEpQics7k2gqCVHwicRP7d8wQFQet5E/640?wx_fmt=png&from=appmsg)

融入了多个hunter,quake,bing等多个资产搜索引擎和我认为最重要点：目录服务，还融入了AI进行决策判断

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9chXicZO71s7kics0ykrk0O9UEWnASlXt4mLP75WPNTD3rgFkg9pQ9nPNxGum4QoNMSNQmFVKTvUbq3mmqKMGfSz2WLHptALJlcAicSfL9I65E/640?wx_fmt=png&from=appmsg)

为什么说AI渗透能力相同，资产收集就更为重要，以某个网站举例

假设你通过信息收集，quake，hunter等，找到如下子域

sp.xxxovomm.com。尝试直接访问网站，首页如下

![](https://mmbiz.qpic.cn/mmbiz_png/9chXicZO71s6jl6cLLStzUJHkWy0TmbZ12QlzC6Qs5VmumbuujwUZeTdug5zdgqib82oanl74FibXJ9DqI6DcYx0dxMibIibGlmhDSicYzqicbRu1k/640?wx_fmt=png&from=appmsg)

这个站给ai，ai会怎么测，探框架，fuzz目录，找找B端站点，看看IP（我菜，能想到的就这么多），还能做什么吗，如果都没有结果是不是就结束了，何况还有一个点，这种站你们真的会费劲去给ai测吗？

你直接访问这个首页——一片空白。丢给 AI？AI 盯着一个空白页，也只能摇头

那我为什么说资产重要呢，看这个站我平台收集到的结果

![](https://mmbiz.qpic.cn/mmbiz_png/9chXicZO71s662v0QvfvoKiaBMRgL8NgDhz5nfMSopqghqqficng320PucLjencWZT7ZqqwceTR385LhC12Yxbrsba2rQCWrgsa0bg1bibFAKZk/640?wx_fmt=png&from=appmsg)

可以看到依靠bing和js分析成功拿到了三个目录服务

| 路径 | 状态 | 标题 | 长度 | 风险 | 来源 |
| --- | --- | --- | --- | --- | --- |
| /dataservice/register | 200 | 数据服务 | 4985 | low | bing+3条相同响应 |
| /fui/dgcf/pcstore/log | 502 | — | 0 | info | regex\_backfill |
| /report/api/v1/users/captcha | 200 | — | 0 | info | regex\_backfill |

第三个路径路径回显图像验证码无用，第二个路径返回502没用。但第一个接口返回正常注册服务页面

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9chXicZO71s7KAM1AF6vC5ib6FsUvIQMHrveJ3iaMye7L8JcnPF42ZyOKSDfwueHyFSnia98kGueTBw7WicR5LEXaEib5vtBS3tHOpiazbOO6JJfIA/640?wx_fmt=png&from=appmsg)

所以你认为是让ai将sp.xxxovomm.com作为测试目标，让它自己测，还是把sp.xxxovomm.com和这三个目录一起给AI让它测试呢？能完全指望靠AI发现/dataservice/register页面吗

首页不能访问但目录挂载服务这样的案例在HunterX数不胜数

![](https://mmbiz.qpic.cn/mmbiz_png/9chXicZO71s5J0gkhKdwuCgTAuSdUgV5ibia7EdqQLqdUkSicUOuWttJmTxhLXGHjYEG6zUkibfKVicOGwOUg5vu7nc7kHAsu05vE4ibOHkuNYRrOg/640?wx_fmt=png&from=appmsg)

上线前经过一周学员测试，贴几个反馈

![](https://mmbiz.qpic.cn/mmbiz_png/9chXicZO71s6RkKV54XBvuWXOAQDdvNfRTkicIrDD0NuUZkCsXC176ZAC1DZeuUaPD1r6NibaQbrO4jG0ibRk8FWSFrGhvjwzfBwTefgYP2eYD8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9chXicZO71s4vjpHf0XkicNzIaxHxwwnUlVeibTbduKLWebsziaQkLftUjWAMZBakuaibJvJd1bjcTQPmoesrjJpbk0GNVofbKfAibaWwE7UFxXLs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9chXicZO71s6PEscPR0hfWQysHa8E6D2FOND0YHvicibFkWwAibWHhXTDK4DX9pP565VwIp1sVib5dtTCDo9ttibH7jsyZXRibmhWFvXvk8w8MflFg/640?wx_fmt=png&from=appmsg)

当时，我自己那些洞有的也是靠hunterx挖到的，有时候挖到洞了我复现都找不到源头，如下

![](https://mmbiz.qpic.cn/mmbiz_png/9chXicZO71s6lfIjyC2crT1QKwUhBxan8BQ9lKWo45WQ5cztwyDm4bXmREnP2g3Ik1yZibmGiccWX1txichqAbodSDawicD5K5ZJVKl19icNd3LyU/640?wx_fmt=png&from=appmsg)

这个洞是8月上旬挖的，算上活动单洞给了9k赏金，没有hunterX我也完全挖不到这个漏洞，所以这也是我为啥越发重视资产收集的原因

目前HunterX都已经上线且投入使用了，但接入了大量外部付费秘钥，还有项目中引入的AI模型，每个月服务器的费用，这些都是成本，所以决定开放出来供各位感兴趣的师傅使用

说明：平台只对公开渠道的资产信息做聚合展示，不提供扫描任务下发功能，注册需同意《用户协议》；数据请用于授权范围内的安全研究。

但由于目前hunterx地址还是IP，没有接域名，所以访问地址暂不在此公开（预计下周上域名），文末放50个7天体验期会员抽奖，中奖的师傅可以获得体验会员和平台地址。

感兴趣的师傅也可以闲鱼搜索HunterX自行购买，感谢各位师傅支持。最后，欢迎扫下方二维码加交流群，群内不定时抽注册码和会员码

![](https://mmbiz.qpic.cn/mmbiz_png/9chXicZO71s6dEnic9VJLNum52OnO23U2vg1icL4nmpaaotsPZlsR8ibtb4K345rZVhdmtJaibVajvp7PgF2lmZyqOulSVPQ54icPwzZP5RQt67Ks/640?wx_fmt=png&from=appmsg)

文末抽50个注册码（注册后可体验7天平台会员），欢迎各位师傅体验

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/QtaE6uFmibPn7WSR6T3iciardwvmOl3QYQC1gf0hyicbYOicUbH88x1tRibG53XWGmyORYQMm1STFcgx5oPFM23EkpYw/0?wx_fmt=png)

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