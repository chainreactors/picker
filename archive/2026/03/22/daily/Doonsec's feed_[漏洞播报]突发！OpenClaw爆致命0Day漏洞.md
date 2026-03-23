---
title: [漏洞播报]突发！OpenClaw爆致命0Day漏洞
url: https://mp.weixin.qq.com/s/pxx9oBQ_R_iqROjNz0FlEQ
source: Doonsec's feed
date: 2026-03-22
fetch_date: 2026-03-23T04:18:50.181827
---

# [漏洞播报]突发！OpenClaw爆致命0Day漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icCLY10D8tvJ41J350cqObTwgB9cQXCpYU5OHticibufpXQSZn8DfDh7Nd35fepnibFS8pyyTlLn5RQ61smKacCmFXIdtE6ueLkiclzTfWV2GE18/0?wx_fmt=jpeg)

# [漏洞播报]突发！OpenClaw爆致命0Day漏洞

原创

Elon
Elon

好靶场

![]()

在小说阅读器中沉浸阅读

> 💡 好靶场
>
> 团队宗旨：我们立志于为所有的网络安全同伴制作出好的靶场，让所有初学者都可以用最低的成本入门网络安全。所以我们团队名称就叫“好靶场”。

---

我们承诺每天至少更新1-2个新靶场，好靶场追求的是稳定日常更新而不仅仅是数量。

---

## 1.好靶场介绍

**官网链接http://www.loveli.com.cn/**

> 零基础入门不迷茫！ 专属网络安全从零到一体系化训练——配套完整靶场+精选学习资料，帮你快速搭建网安知识框架，迈出入门关键一步！ 全场景实战全覆盖！ 聚焦Web渗透工程师核心能力，深度拆解TOP10逻辑漏洞，精通PHP代码审计、Java代码审计等核心技能，从基础原理到实战攻防，覆盖行业高频应用场景！ 真实漏洞场景沉浸式体验！src训练专题重磅上线——1:1还原真实漏洞报告，让你亲身感受实战挖洞流程，积累符合企业需求的实战经验！

🚀哈喽～各位宝子们晚上好~~👋！今日为大家带来的是关于小龙虾的内容，这一次小龙虾OpenClaw又被揪出漏洞这次是0Day漏洞，宝子们在部署的时刻一定要注意不要暴露在公网，接下来进行详细的报道；以下的详细内容👇

## 2. 报道内容

AI安全圈昨夜突发重磅消息，彻底打破了行业的平静。3月22日，OpenClaw创始人Peter Steinberger通过官方邮件正式回信，确认了360安全云团队独家发现的WebSocket无认证升级漏洞真实存在——这是一枚CVSS 10.0满分的零日（0Day）漏洞，被业内称为“数字定时炸弹”，直接威胁全球超13万台OpenClaw智能体网关的安全。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icCLY10D8tvIzPpd0dECHHOKgWbcIpoPqqF1cMXhxdmSGicG8Z3WVYqoz9xZsWxzeicWVMKvuhWZ8sDt5FWEHtKznXQvCOo6PGsJAzBibSOlXKE/640?wx_fmt=png&from=appmsg)

### 先搞懂：OpenClaw是什么？这枚0Day漏洞有多致命？

![](https://mmbiz.qpic.cn/mmbiz_jpg/icCLY10D8tvKA4hngLrME8c5BC6uJ5FNJD4B4b25ibrlVXbicrSttxd2MSM52kEde58KWGHYdc4GgAjwawekTVZdc38MfSDEiaBeOyic9J1QfeHQ/640?wx_fmt=jpeg&from=appmsg)

在聊漏洞之前，先跟大家科普一个关键信息：OpenClaw，圈内俗称“小龙虾”，是海外现象级开源AI智能体网关，被广泛应用于企业AI服务、智能家居、工业控制等多个核心场景，简单说，它就是AI智能体的“中枢大门”，所有AI智能体的数据传输、指令执行，都要经过这个“大门”调度。 而这次360发现的，是最危险的0Day漏洞——所谓0Day漏洞，就是指在被发现前，除了产品开发者，没有任何第三方（包括黑客、安全机构）知晓其存在，没有任何补丁和预警，攻击者可以直接利用，目标系统毫无防备。 更可怕的是，这枚漏洞的CVSS评分高达10.0（满分），属于最高危级别。技术细节显示，攻击者只需获取共享令牌，在WebSocket连接时声明高权限作用域，就能静默绕过所有权限认证，直接夺取网关控制权，全程无弹窗、无提示、无日志记录，受害者根本无法通过常规方式察觉。 一旦被黑产利用，后果不堪设想：攻击者可以读取API密钥、篡改网关配置、接管设备节点，甚至远程执行代码；对企业而言，核心数据、业务逻辑、接口密钥会被轻易窃取篡改；对个人开发者来说，本地文件、源代码、私密信息可能被静默外传，设备也可能被完全掌控。 更值得警惕的是，据360漏洞研究院监测，公网中超过13万台OpenClaw实例默认暴露在公网，且大量设备未启用强认证，几乎处于“裸奔”状态，90%以上可直接被攻击，相当于全球有13万台“定时炸弹”随时可能引爆。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icCLY10D8tvLIicrGc85wlYEesibrN9eLaRFZKibbBqiaKjJZhHgiaibRPp1DsgfBZzzZmQmEAuywAicjXkuAXx5Z94oE0MLyTlgseGt7MdibgvvJLwk/640?wx_fmt=png&from=appmsg)

### 时间线梳理：360如何揪出这枚“隐形炸弹”？

这起漏洞事件的发酵，始于360安全云团队的一次常规扫描，整个过程严谨规范，完全遵循国际通用漏洞披露流程，每一步都尽显专业：

1. 3月17日，360安全云团队通过“龙虾安全体检智能体”主动扫描，率先发现OpenClaw的WebSocket共享认证越权漏洞，这也是“以模治模”AI安全思路的一次典型落地；
2. 发现漏洞后，360并未急于公开造势，而是第一时间向OpenClaw创始人Peter提交完整漏洞报告，同步报送国家信息安全漏洞共享平台（CNVD），全力推动官方修复，做到“先防护、后披露”，最大限度避免黑产提前利用；

   ![](https://mmbiz.qpic.cn/mmbiz_png/icCLY10D8tvItUB670CSuOlicDrGr1eATxB9pSicl9WHsJIlNEOzWGXIxN0VpHD8LUO5niadWjTTicVctJZBphse0xsebuN0tX4jVKxAMAvib5dqk/640?wx_fmt=png&from=appmsg)
3. 短短几天内，OpenClaw创始人Peter通过官方邮件正式回应，明确承认漏洞存在、影响范围清晰，并已启动紧急修复方案；

## 3. 如何使用好靶场

首先关注“好靶场微信公众号”然后发送bug，可以点击链接直接登录

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icCLY10D8tvJn80Sicpic7OmticxNKsrrgJFTNUhAftHBnCibiaicLFUCB8ehvyT0PrXEG4lDcsnvDLAqJSBQlHz0V4F8SIF5gpO9iaNiaH97PBFjQRw/640?wx_fmt=png&from=appmsg)

## 4. 福利

福利1： 找到个人中心，邀请码输入0482d6d28539424c，白嫖14天高级会员。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icCLY10D8tvLCicFgYymsZVpugibO1C8AVsib8XicsA53jA7a050c434b35AhxXQHcdCOzjtRl9N3GpUzIsFdNXY0rh56Mll8dmpKNJIib98uZvibQ/640?wx_fmt=png&from=appmsg)

福利2： 关注好靶场bilibili。拿着关注截图找到客服，领取5积分或者7天高级会员。

![](https://mmbiz.qpic.cn/mmbiz_png/icCLY10D8tvIicU6vDElyplQWIXkDdgNCmMkL9xCMOx9EsUKtNN4OhyBrAGbMo3QkpzFS5OP8ETAdLenHsJAjz3XCVrfnBSu186zyaqERbsLk/640?wx_fmt=png&from=appmsg)

## 5. 每日限免

每日限免 为了能让更多的宝子可以免费的开启会员靶场，我们会在工作日随机开放一些靶场的限免，还请加群关注。

![](https://mmbiz.qpic.cn/mmbiz_png/icCLY10D8tvJguqkEichc2zwjCTwfQsl8FW56dZAlNmdDAbLVarx22icu0Y6sJibk94vBBoibkNU3htXEknvAVQQCObYtlB51hatQab1ibRp13a98/640?wx_fmt=png&from=appmsg)

我们会在微信群、QQ群每天更新限免靶场，以及免费学习资料；任选一个群添加即可，所有的通知都会到位在交流群通知，请添加好友，我将邀请你加入“好靶场内部交流群”

![](https://mmbiz.qpic.cn/mmbiz_png/icCLY10D8tvKvSCywPlC90S8mWg9fr8xxhWShHvJ3z1njibcmLCFHchA6Xl70fByLuek75ZgF8uUR5r8wqQJT730tcQvzD7ATHIdIibj1Yq3Io/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icCLY10D8tvL62Jib8LO4pnzu27PofUnice4tk9fv57UjsK6dySBood4KOYYIyqcyzG8xdksv5hWMltXV27rSiaQBoXbQd4scwms3D2oXp5PX3A/640?wx_fmt=png&from=appmsg)

## 6. 好靶场AI客服机器人

为方便学习还有提问，我们设计了好靶场Ai客服机器人，可以完成简单的客服能力，以及好靶场日常靶场提醒更新、根据你的询问推荐靶场

![](https://mmbiz.qpic.cn/mmbiz_png/icCLY10D8tvJWgicVJZCqicFqHryHf2oekbyLAic3fkgiaibJeZF3sofXCBPJj1EokyFA6CWGqoah7K5wGP9fGgRbXrof4QwkGm8sFV8PLUZlBdicA/640?wx_fmt=png&from=appmsg)

> “噜噜大王”正式上线

大家点击左边的快捷工具，有一个AI助教功能，然后点开就可以和噜噜大王对话啦，由于是内测期间，仅限于年会员才可以进行使用。还需要进行微调，会随着大家的使用而进行优化。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icCLY10D8tvLibGj2clL9G5HcdQzicDhvj0aFX2T40aN0HpavNpECT4gwFKiamia5bkhRN8cL8IYvGh1B64GLsEwoeZw9rSTKjQftZXZichrU3MVQ/640?wx_fmt=png&from=appmsg)

你可以尝试问一下关于打靶场的问题

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icCLY10D8tvIaxlSRORYukR4uXiceXJGvPjMAic5UUeRQvm2UujPNHRS83OuickUK1RRGPibAVMSRyvsIWnr4BsoCwdojr7APJNNIH2Q0wqOGHS4/640?wx_fmt=png&from=appmsg)

## 🚀好靶场会员订阅

好靶场会员订阅 首先点击会员订阅 ，然后选择对应的套餐 ，选择对应的会员去支付 ，支付完成后即可会员到账

![](https://mmbiz.qpic.cn/mmbiz_png/icCLY10D8tvLicRSPx4NXENbaPVxeF2rLIuyHArtS8HOoIM8TfID3wFxo8icSQDQasMxnqU9QbjfXskbHibKgHbeVBw3nBZ21L65YekWYnt4xUA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/icCLY10D8tvJcatqLTdbqI1MI6wP5uKCiagTMKqQOvHlrRI5nIGzOg4nzIKIwfOBruOVe7cSNK7T29SwAyUY7f0tMTuqicl4aKUBAGJKPKa3A0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/icCLY10D8tvJkQZQagkapGxPmA54TpyG9ic1NiaMQlhCdpKSVPMGuDZiaiaAZBHrD35MqBAb3DaOxiaDe4FZgUhFwOrDpUxrcKH6AzzS1KK3xnibVc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icCLY10D8tvLqz0Ib7Km2ibLlJRMh5P4mxCyIticKBGMYVQdzCESabI8o64l24pyhHgOdoupK1EuykUMJdgNJAwJFYsnQjmNibuXVvQPp182M6o/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/h1AzajLJTBvK2C7klp7wKKhoR7iamhAw3AVsjpcIvpHzC5YZWjhMSQ6s5sWRLqawfkh3SXcMGw99vGgwRBMkGeA/0?wx_fmt=png)

好靶场

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/h1AzajLJTBvK2C7klp7wKKhoR7iamhAw3AVsjpcIvpHzC5YZWjhMSQ6s5sWRLqawfkh3SXcMGw99vGgwRBMkGeA/0?wx_fmt=png)

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