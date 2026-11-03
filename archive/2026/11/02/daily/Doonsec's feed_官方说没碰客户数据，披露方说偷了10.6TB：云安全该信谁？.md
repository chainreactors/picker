---
title: 官方说没碰客户数据，披露方说偷了10.6TB：云安全该信谁？
url: https://mp.weixin.qq.com/s/6jY796dPV1gLBVbvg131sA
source: Doonsec's feed
date: 2026-11-02
fetch_date: 2026-11-03T08:46:00.920372
---

# 官方说没碰客户数据，披露方说偷了10.6TB：云安全该信谁？

# 官方说没碰客户数据，披露方说偷了10.6TB：云安全该信谁？

走狗是狗哥
走狗是狗哥

安在

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![图片](https://mmbiz.qpic.cn/mmbiz_gif/5eH7xATwT3icpLmjpDSQkXx16oAygiaJncke0vYYJvIkuzECibrQJcUW4oAedTuib1G9m372rleJRDNXNs54fBEVicg/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

近日，开源分布式数据库厂商PingCAP在官网信任中心发布安全事件声明。

同日，勒索兼披露组织FulcrumSec将PingCAP及其云托管平台TiDB Cloud列入受害者名单。

安全情报机构Hackmanac在X上贴出一组数字，事件迅速在开发者圈发酵。

需要先把两件事分开看：哪些是官方确认的，哪些只是攻击者的单方说法。

**官方确认了什么**

PingCAP声明称， 9月9日至10月7日，未授权方使用被盗的服务账号凭据，访问了部分内部系统、复制数据并取得源代码。

公司10月7日知悉此事，当日即开始停用受影响凭据。

外部应急响应公司审查生产系统后，未发现攻击者执行命令或维持持久访问的证据，也没有证据表明TiDB中存储的客户业务数据受到影响。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8C1NLS8ickpdppPy2DDeRdQtvTmXWkaBUvPpe0SxTzC2iapp9Dic10co5sVIMQ9wCkHWmP4Pxl9hwhsp70wYibeibKxcCjvjZ8hxCpw0AmCcyvQs/640?wx_fmt=png&from=appmsg)

已确认被导出的记录包括：用户名与邮箱、组织和项目关联、SQL编辑器文本与错误，以及客户联系人、合同条款、订单、定价和账单配置。

一张导出表中含有加密的TiDB Cloud API密钥值，外部公司测试其中一个值，确认不能直接当作密钥使用。

处置方面，10月12至13日外部公司报出4个漏洞，PingCAP于14日全部修复并复测通过；

截至10月14日，所有已识别的失陷凭据作废、访问路径阻断。

截至19日，公司仍在逐户确定具体影响范围。

**披露方声称了什么，且尚未被核实**

FulcrumSec公开宣称，其从TiDB Cloud持续窃取约10.6TB数据，并放出约200GB首批样本。

Hackmanac转述的清单包括：约18万个租户组织、29万余条用户记录、40余万个独立邮箱、数百万项目与集群，以及11万余对所谓明文控制台密钥。

披露方还称，其使用了PingCAP自己代码仓库中提交过的GCP服务账号密钥和Azure服务主体，搭建复制订阅源，让对方基础设施每6小时自动推送数据，22天内连续导出88次且未触发告警。

必须强调：以上规模、密钥数量与"零告警"说法，均来自披露方自述，尚未获得独立核实，官方声明也未确认。

两类信息的证据等级不同，不能直接等同。

**两种口径为何差距明显**

官方口径保守，聚焦"生产系统有没有被控制、客户业务数据有没有被碰"。

披露方口径激进，强调"我拿走了多少、还能再放多少"，本质是勒索施压。

![](https://mmbiz.qpic.cn/mmbiz_png/8C1NLS8ickpfGPfSx3hD1v5Wb9U8WMbEJ9W8lrLdkicvU3lHOEQJqz6b3jywUBjiauVx2j622tBibyibzajpOIT8YHiaIdLicOWkMTo8kxVMZbIEag/640?wx_fmt=png&from=appmsg)

一个说密钥是加密的、测试值不可直接使用，一个称有11万余对明文密钥、其中4万余对处于激活状态。

在独立取证完成前，这些争议都应存疑，企业不宜仅凭暗网清单下结论。

**真正值得记下的三点**

**第一，入口不是攻破边界，而是代码仓库里的凭据。**

披露方称使用的是厂商自己提交进版本库的云服务账号密钥。

这提醒所有自建云、管流水线的组织：

凭据扫描范围要从应用代码，扩到基础设施代码、流水线变量与镜像构建上下文。

**第二，被拿走的是控制平面，不是业务数据本身。**

租户、项目、集群标识与接口密钥，虽不等于库里的业务数据，却能决定下一批业务数据如何被取走。

这一层的批量导出，常落在以主机和终端为主的监测视野之外。

**第三，密钥轮换是有截止时间的动作，不是一句结论。**

官方至今仍写着"是否还有其他可用凭据暴露待确定"，说明轮换范围应由企业自己主动决定，而不是等对方给清单。

**对使用云服务的企业**

这次事件给客户的直接启示是：

向云服务商问询时，别只问"有没有认证"，要能看到厂商自身那一层的访问日志与导出基线。

同时为关键云服务备好"依赖与可替代性"清单，万一控制平面被完整复制，哪些业务要停、多久能切，应在事前想清。

**结语**

PingCAP事件的价值，不在于10.6TB这个数字真假，而在于它再次暴露了一个共性问题：

云控制平面的凭据管理、批量导出监测与密钥轮换，往往比业务数据本身更脆弱。

在官方调查与独立取证完成前，理性的做法是分清事实与宣称，把教训先落到自己的防线里。

****END**

[![](https://mmbiz.qpic.cn/mmbiz_png/8C1NLS8ickpft3Q38fRygqB6JoiaNnuCd9iciapibWtWwO8ibpib9wPiclHb5UET2E1vSXsmC8vic1h844SFa01Iic2Yq4keCAA4hRibAN8cQc8NqHejBc/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzU5ODgzNTExOQ==&mid=2247657060&idx=1&sn=9fdcb0cd7084523a3ea7fb24ce6e2c31&scene=21#wechat_redirect)

[![图片](https://mmbiz.qpic.cn/mmbiz_png/5eH7xATwT38j3Ndib8YhjyiaBQhdzUe1AApXU9ib7vkMD4KMHhjVfkTqOCUrDibUaBDoH0OGGCMasLLJyv5xppK6rA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp)](https://mp.weixin.qq.com/s?__biz=MzU5ODgzNTExOQ==&mid=2247652102&idx=1&sn=8af8808f9055f99fa71020922d80058c&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5eH7xATwT38HPkvxLkOy5rLCeVBtj8H9SUbVPNZbibc4N2knPCDFjTKduRLhiaAZVQShUa2IZqsBShI2GG2dpqBg/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp)

点击这里阅读原文**

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5eH7xATwT39OIA4MxWIQmVzjc3H2rbMa0sv6no7gMEXOV63OW7hvwk4EDjOaurIkrnPOjBpCmIN00ELKRf16qg/0?wx_fmt=png)

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