---
title: 没木马、没0day，仅靠一个配置错误，企业SharePoint被洗劫一空
url: https://mp.weixin.qq.com/s/EDXVcMd8ruiCL51Gm7mbbw
source: Doonsec's feed
date: 2026-04-11
fetch_date: 2026-04-12T04:45:57.441386
---

# 没木马、没0day，仅靠一个配置错误，企业SharePoint被洗劫一空

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/E3ZvvAXyiaibnFF1Hu03vyccpGL5AOwicMAdjYwmp57SrfHDkPYTYJu7rK59a79e16g22jGic0Cp7ibtmMQlY1PkZpwBsvLjQ3rKy7xaQEoqRd7E/0?wx_fmt=jpeg)

# 没木马、没0day，仅靠一个配置错误，企业SharePoint被洗劫一空

原创

AI紫队安全研究
AI紫队安全研究

AI紫队安全研究

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**大家好，我是AI紫队安全研究。建议大家把公众号“AI紫队安全研究”设为星标，否则可能就无法及时看到啦！因为公众号只对常读和星标的公众号才能大图推送。操作方法：先点击上面的“AI**紫队安全研究**”，然后点击右上角的【...】,然后点击【设为星标】即可。**

**关注视频号 “**AI紫队安全研究**” 不定期周五晚上10点直播。**

![](https://mmbiz.qpic.cn/mmbiz_png/E3ZvvAXyiaibn8E7ha4XdnQn9hicXhMVvqwY7cu4wRASaBDXibb26aaTUMSOE8WunuTV3oJS0x46afE6BEfxKaA0taMzpR2BArgVkfoia1E4zq0A/640?wx_fmt=png&from=appmsg)

你以为MFA开了就高枕无忧？

现实是：一个暴露的接口 + 一份明文密码表 + 一个被遗忘的认证流程，就能轻松绕开多因素认证，把核心文档全部偷走。

这不是电影桥段，是2026年最新真实攻防案例。

01 入侵起点：一个“随手暴露”的监控接口

攻击者最开始什么都没干，只是扫到了一个公开可访问的 Spring Boot Actuator。

这个接口本来是给运维看监控、健康检查、配置信息的。

结果这家公司：

没加登录验证

没做IP白名单

`/env` `/configprops` 直接裸奔

攻击者几行curl一跑，当场拿到：

SharePoint服务账号用户名

站点地址、应用配置

关键密码虽然打码，但知道密码存在配置文件里

第一步：入口拿到，路线摸清。

02 致命助攻：明文密码躺在Excel里

更离谱的是：

内部应用的 client-id、client-secret、密钥，居然明文存在一张表格里。

谁能想到：

攻击者从Actuator摸到线索，再找到这份“密码清单”，

直接拿到了Azure AD应用的全套登录凭证。

这一步之后，他已经拥有：

应用身份

服务账号信息

云端入口

只差最后一步：登录。

03 绝杀技：绕开MFA的“后门认证”

你开了MFA，有用吗？

在 OAuth2 ROPC 面前，形同虚设。

ROPC（资源所有者密码凭证）允许：

直接传账号+密码+应用密钥

不跳转、不弹窗、不验证二次校验

直接返回访问令牌

攻击者拿着偷来的信息，组装请求：

1. 填入client-id / client-secret

2. 填入SharePoint服务账号密码

3. 发往Azure AD

登录成功，令牌到手，MFA完全没触发。

04 最后30分钟：SharePoint被批量拖走

拿到令牌后，攻击者通过Microsoft Graph API：

遍历站点

枚举文档库

批量下载文件

日志里清清楚楚：

Credential.txt

VPN\_Exception.xlsx

DB账号密码、备份清单、SQL脚本

内部计划、架构信息

全程无木马、无漏洞利用，只用“合法权限”完成盗窃。

05 复盘：整个入侵只靠3个低级错误

这起事件最扎心的地方：

没有高级技术，全是管理漏洞。

1. Spring Boot Actuator 公网暴露

   `/env` 泄露配置，等于给攻击者递地图。

2. 密钥明文存文档/表格

   开发图方便，最终变成灾难入口。

3. 保留ROPC老旧认证流程

   这是MFA的天然漏洞，密码一漏，全线失守。

06 立刻照做：4条止血建议（企业必查）

1）马上锁死 Actuator

禁止公网访问 `/actuator/env` `/heapdump`

加登录、加IP白名单、用反向代理保护

生产环境绝对不暴露敏感端点

2）全面清剿“明文密码”

搜一遍：Excel、文档、共享盘、配置文件

凡是明文存的账号/密钥，全部轮换

改用密钥保管库（Azure KeyVault等）

3）禁用 ROPC

这是本次绕开MFA的核心通道

能关就关，改用现代OAuth流程

开启条件访问、强制MFA、最小权限

4）监控异常登录

盯紧：非交互式登录、API批量下载

境外IP、curl/脚本UA高频访问

SharePoint/Graph接口异常调用

结语

云端安全的真相：

你以为的坚固防线，往往毁在最不起眼的配置里。

MFA不是免死金牌，权限最小化、密钥安全、接口收敛，才是真正的底线。

**加入知识星球，可获取权益**

一、"全球高级持续威胁：网络世界的隐形战争"，总共26章，为你带来体系化认识APT，欢迎感兴趣的朋友入圈交流。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/E3ZvvAXyiaiblj6Qa1c5j4iaSxNtaWyMmOrsJ7WJafnTfxff3PA2nhkdQL7AyqtkzhPaoCicbu2FWhIAe1y02o5icTMZiaiaD1T4WXgf5TRsAVyEFU/640?wx_fmt=png&from=appmsg)

二、为什么加入？

职场瓶颈期找不到突破方向？安全项目落地缺成熟方案？面对APT攻击、勒索病毒不知如何构建防御体系？

三、在这里，你能获得的不只是资料包，而是直接对接行业专家的「私人顾问服务」

✅ 职业发展「精准导航」

 1v1简历优化：针对安全岗（渗透测试/安全运营/合规等）拆解JD，突出核心竞争力；

 晋升避坑指南：从工程师到安全负责人，分享晋升路径，避开「技术强但管理弱」的晋升陷阱；

 技能栈规划：根据你的基础（应届生/3年经验/资深专家）定制学习路线，比如从0到1学SOC安全建设、APT威胁狩猎。

✅ 安全方案「对症开方」

 实战方案库：含医疗/制造业/等行业的勒索防御、数据安全合规、供应链安全加固方案（附落地工具清单+成本测算）；

 架构设计咨询：小到EDR选型，大到零信任体系搭建，提供「预算效果」平衡的最优解（已帮10+企业节省40%防护成本）。

✅ 圈子资源「直接对接」

 大厂安全负责人拆解真实案例（如某支付公司攻防对抗的实战复盘）；

四、适合谁？

 想突破职业天花板的安全工程师/架构师；

 需快速落地安全项目的企业负责人；

 关注行业动态的安全爱好者或IT从业人员。

**喜欢文章的朋友动动发财手点赞、转发、赞赏，你的每一次认可，都是我继续前进的动力。**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/sUKKZDdVP8SDmJE3icia7GnaJnVTPhzvKxNj1UhibY8xmZLVfpF4v54OD9Jia6UhwdOcd8YMMw0ZbHnN3UodTaib7tw/0?wx_fmt=png)

AI紫队安全研究

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/sUKKZDdVP8SDmJE3icia7GnaJnVTPhzvKxNj1UhibY8xmZLVfpF4v54OD9Jia6UhwdOcd8YMMw0ZbHnN3UodTaib7tw/0?wx_fmt=png)

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