---
title: 授权测试里的远程车门解锁与账户接管检测盲区
url: https://mp.weixin.qq.com/s/81r3aszETWJCvsv71B3NZw
source: Doonsec's feed
date: 2026-11-27
fetch_date: 2026-11-28T09:39:26.351127
---

# 授权测试里的远程车门解锁与账户接管检测盲区

# 授权测试里的远程车门解锁与账户接管检测盲区

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaB995ym51yuiaz6UL4C02FAq637ia0w2GiaMZ1NeOTbZsFia0oXMWjkiatyNdibc3tWmRVo9GcFVPnLmf3HcbwDyar3YhWkLDt0DZ4SY/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247582550&idx=1&sn=d7226bc800af241beba7f3da987f9de3&scene=21#wechat_redirect)

11 月 7 日，安全研究员 Shubham Shah 与 Sam Curry 同时公开两份报告，把一条从车牌号到远程解锁的链路完整摊开：起点是澳大利亚各州公开的车牌查 VIN，终点是车联网 App 向测试车辆下发的 door-unlock 指令。

中间没有碰车端 ECU、没有破解防盗芯片、没有利用 CAN 报文，真正被端掉的是车企放在云端的身份认证系统——前端 JavaScript 包里硬编码了 API Key 与 ForgeRock OpenIDM 管理员凭据，边缘 WAF 与后端对同一个 URL 的解析不一致，密码可被改写、MFA 可被跳过，最后换出一枚与车主 App 同款的访问令牌。

对车企、Tier 1 与车联网平台的安全工程师来说，这条链值得逐跳拆开，因为它把「远程控车」这件事的安全边界，重新划到了账号与令牌上。

**一、披露时间线与实测范围**

两份报告于 2026 年 11 月 7 日同时发布，分别覆盖两条调查线：Shah 主笔澳大利亚分支，Curry 主笔美国、加拿大与欧洲方向的身份平台分析。两条线是分批推进的，公开材料对最初发现与上报时间点的表述并不一致，能对齐的硬节点只有披露日与修复动作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaBFLCBjxlKygVIIXFTgqZnjECqiaribSx7X79bwrtC6fo4vUfeQia6wic8bADiayUJLv62Lz35AXNP34iab3sfwbT9c2E3VqHwL5KSWA/640?wx_fmt=png&from=appmsg)

范围上必须收紧：研究者主文称两份报告合起来可对该车企在澳大利亚、美国、加拿大的车辆下发远程指令，但配套报告明确写出，完整的账户到实车控制端到端链条只用美国境内的账户与车辆验证过；澳大利亚分支只在自有或获授权车辆上做了验证，欧洲方向没有做实车控制测试。把标题里的「世界大部分地方」直接读成「全球任意一台联网车」，会越过实测边界。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBKIRuX7b3wzlJZ8wo4GwuG3MAeHUqEMmglqW6caKGdicjdQFiaUGZg83E5PoE5mwu1vW1osnbzYM8iaQwg7Uj1bym8dnIWibSF5A8/640?wx_fmt=png&from=appmsg)

图 1｜手机 App、云平台与 T-BOX 连接架构示意

两家涉事主体均未点名，且公开报道对「是一家车企旗下两个品牌」还是「两家车企共用同一身份平台」的表述并不一致。这类数量差异不影响技术链的成立，正文只按「同一套第三方身份平台支撑的车联网 App」来描述，不替研究者指认品牌。

**二、车牌号到账户信息的映射**

链路的第一步连漏洞都算不上。澳大利亚各州的车辆登记查询支持用牌照号换到 VIN，这是面向二手车查验等场景的公开设计；研究者反编译车企 Android App、重建其与远程信息服务接口的通信后，发现一个公网可访问的内部管理后台，其前端单页应用把完整 JavaScript 包下发给浏览器，包里硬编码了可直接调用的 API Key。

管理后台本身能按邮箱查账户、配置车辆功能、添加次要用户、生成远程访问码，功能面相当宽，但研究者明确写到：这些功能都不直接给到远程控车。知道车主是谁，与能以车主身份行动，是两件不同的事。把「查得到账户」写成「车已被控制」，是这条链最容易被夸张的一处。

**三、前端包里的管理员凭据**

真正把两件事接上的，是另一份 vendor JavaScript 包。车企的客户身份体系跑在 ForgeRock OpenAM / OpenIDM 上，OpenIDM 实例管理着车联网平台上注册的每一个身份；而其中一份前端包里，内嵌了 OpenIDM 的管理员凭据。这些凭据本该只用于预发布环境，但在生产环境同样有效。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaDrUDkEllYUe7B4yM6ZPdKkQJG04RdQkRZL4C3eMbWyO5Q1OfuyQjWf4HaS8hXQw9vOs6Yyjv0RGibHLVmoqPiaqKOz0KUfV4wVw/640?wx_fmt=png&from=appmsg)

这不是某个 ForgeRock 产品的 CVE，而是部署与配置问题：凭据怎么进的前端包、为什么跨环境有效、为什么管理面要对外，三个问题都属于车企与其供应商的交付边界。研究者也写到，车企在 WAF 上确实投入了加固，任何直接访问 `/openidm/` 的请求都会被 Nginx 拦下——问题不在有没有防护，而在防护被放在了一个本不该对外暴露的资产前面。

**四、WAF 与后端的解析差异**

绕过发生在同一串字节被两层组件读成两个不同的路径。WAF 按自己的规则判断请求路径是否命中 `/openidm/\*`，后端 servlet 容器则对编码后的斜杠做解码与归一化，再据此选择处理逻辑。形如 `/static%2f..%2fopenidm/` 的路径，在边缘一侧被当成静态资源放行，在后端一侧被还原成管理接口路径。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaARedyP5icwb4UD7IYib1wxgcW3pu6Iia47Y7YKsP7mQOmF84udrxBiaTsnQ7ltic7InicaATFfvsGAIkE2jDqIuUicTHnSFhibVibZDBcg/640?wx_fmt=png&from=appmsg)

图 2｜WAF 绕过与账户接管流程示意

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaDeL3qwbvnicTcrnpTibk1VBFLDY5ys7QxCcn8icnGRZ0yYic42qjgZA2pibAgjbPicCYDkmed7EjiaXK8B7zGErOylz14qEajvjcxyjk/640?wx_fmt=png&from=appmsg)

研究者最初尝试的 `/XUI/..%2fopenidm/` 只拿到管理员 JWT，却因 OpenIDM 的路由机制找不到对应 servlet 而报错；换成自定义端点与静态路径前缀后，才拿到可用的管理接口。这处细节值得记住：解析差异不是某一层的 bug，而是两层对「这个 URL 是什么」没有共同定义。同类问题在车云 API 网关、反向代理与后端微服务之间同样会出现，只是这次的后果落在了控车权限上。

**五、密码改写、MFA 跳过与令牌签发**

拿到 OpenIDM 管理接口后，链路进入身份层：对 `/managed/user/` 发起 PATCH 即可改写任意用户密码；随后用 Resource Owner Password Credentials 授权方式直接请求认证令牌，跳过澳大利亚环境的多因素认证步骤，再把该令牌换成车联网 App 使用的访问令牌。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAAjLNTHfmEAD0NnBU58iacibtfecp40BTTZsVyO82qs31TiaJRlz8xD3tCd1lRJyWic3ERibia6NMsYeEN5MxemmHjhna3Gp2wOkB7Y/640?wx_fmt=png&from=appmsg)

图 3｜IAM 统一身份认证与令牌流程示意

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaDdWWic3gvSbxe7ibz3CrspfjRtpibKhFtbunZ7jOjicKHWVVIHuU6RWwicBa0R1oz1mMiaARSZnS5UKfBaFpAxGwIzcVnZxZFZeDMr8/640?wx_fmt=png&from=appmsg)

这一步之后，攻击者与车主在认证系统眼里没有区别。防火墙规则、验签、车端鉴权都只会看到「一个持有合法令牌的 App」，这正是整条链最硬的一句结论：控车权限的安全等级，被账号系统的安全等级拉平了。

**六、远程指令与账户状态盲区**

研究者在授权测试车辆上验证了车门解锁、上锁、鸣笛、远程启动与熄火，以及车辆位置、里程、油量或续航、车门车窗状态、车况报告等读取能力。功能范围随车型与订阅方案变化，不是所有车都具备同一组远程指令。

更值得工程侧留下的是两处状态盲区。研究者把测试账户的邮箱改回原值后，此前签发的令牌仍然可用；改邮箱与改密码也没有把真实车主从 App 里登出，账号告警还能被导向另一个号码。这意味着只检查「账户当前状态」的监控会漏掉整段序列：邮箱与口令变更 → 新设备登录 → 通知渠道变更 → 异常时段的远程解锁，单个事件都像普通操作，串起来才是攻击。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBOkppbVlw7qLJ4Dm6D0LxpBGXDoBc4CUV3M7GgUwzwlaanJyASYiazjyzElVv533Jszs4FlYlhWwov7jrkWleAbo8ODVUuYgNk/640?wx_fmt=png&from=appmsg)

一个「恢复原状」的账户，并不等于一次没有发生过的接管。敏感命令的授权判断，应该把「恢复联系方式、设备绑定关系最近是否被改过」「批准是否来自此前可信通道」一起纳入，而不是只看当下这枚令牌能不能通过校验。

**七、美加分支的代码执行路径**

Curry 主笔的配套报告给出了另一条更重的入口：同一套 ForgeRock 部署的生产身份认证服务器上，研究者通过管理控制台与默认凭据、再借 OpenIDM 的调度能力执行脚本，实现了服务器端远程代码执行。由此可为该部署管理的任意车主账户创建合法会话，进而取得与手机 App 相同的车辆定位、遥测、锁闭解锁与远程启停能力。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCctPpyQrXVoicZRyCQ33F1RLnLHhweicjJNTDI4ic5Upvg6D1c7r0Zs1WJHYyibvEeopxjsFu6Jz93NUEffgqQjKOJGFV1eibF94Vc/640?wx_fmt=png&from=appmsg)

两条分支的收敛点相同：都不是车端被攻破，而是身份平台一旦失守，控车能力就随合法会话一起交出去。厂商在收到报告后约两小时内完成修复并轮换凭据，响应本身很快；但因为根因是部署配置而非产品缺陷，没有 CVE、没有厂商公告，也没有公开的受影响车型与软件版本清单——这给车队侧自查留下的唯一可靠抓手，是自己的身份平台配置与会话台账。

**八、适用边界与未确认项**

这不是车端漏洞，也不是车辆被远程入侵。代码执行发生在生产身份认证服务器上，车端只是按设计接受了由合法令牌发起的指令；公开材料没有显示转向、制动、驾驶辅助或动力控制被触及，也没有把它认定为某款车的安全缺陷。

这也不是对某家车企的指认。研究者主动隐去了名称、域名与凭据，社区里据演示视频车型作出的品牌猜测没有获得任何确认，不能写进结论；公开报道对涉事主体是一家车企两个品牌、还是两家车企共用平台也不一致。同样，没有证据显示这些弱点在修复前曾被恶意利用，测试全程在自有或授权车辆上进行。

至于受影响的车型、年款、市场、固件与订阅方案清单，厂商与研究者均未公布；「数十万辆车受影响」一类的估算缺乏按 VIN 与版本可核对的台账，不宜当作事实。两份报告对最初发现与上报时间的表述也存在差异，能对齐的只有 11 月 7 日披露与两小时内的修复动作。

**九、给车企与 Tier 1 的验收项**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaDexgamQzLsibTgq5E8BfmSE3KaDckesC3QIM8CwEMoicF1ict6ica32yzHJibnsiaqXeL3jXicG50qAZeD0qxhXvbkOR08v9sib3qo1zo/640?wx_fmt=png&from=appmsg)

车牌号本身不是秘密，VIN 也有正当的公开用途。真正把一辆车交出去的，是「谁能改一个账号、谁能签一枚令牌、这枚令牌能做什么」这条链上每一跳的默认信任。车端的防盗可以做到很硬，但只要云端身份平台还把管理员凭据写进前端包、还让两层组件对同一个 URL 各读各的，车门的最终权限就不在车里。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCfv8Rp38N5sYLv34P5K2FpbKBdOqic0AaRmDVCFhEyTzRU6zQT3tmaxMial0KrepPFt3Ew0Q9icVLRq6etEGGZUpF3eBwKBiaBqSU/640?wx_fmt=png&from=appmsg)

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=appmsg)

**精品活动推荐**

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBvgQxffuoSxCK5zHBjMe1zHgWJ84eiapLGn9OJxaSDIkr7ZxqlZePY6F37BhEGKickoLHqodK770FzBXHPlIuxyHCSicGTiaF5FP4/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247580896&idx=1&sn=36a65f68d014c79310fdeb0e1e55b6b0&scene=21#wechat_redirect)

**专业社群**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJnASqAJY7fLYIeMGl8fHu4aPXusCVuX2qAYkrb9bQMRGEBvSghHETaQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247535223&idx=1&sn=e30e07a44accd5b0e9ada3d8b537f977&scene=21#wechat_redirect)

**部分入群专家来自：**

**新势力车企：**

特斯拉、理想、极氪、小米、零跑汽车、阿维塔汽车、智己汽车、小鹏、岚图汽车、蔚来汽车、吉祥汽车、赛力斯......

**外资传统主流车企代表:**

大众中国、大众酷翼、奥迪汽车、宝马、福特、戴姆勒-奔驰、通用、保时捷、沃尔沃、现代汽车、日产汽车、捷豹路虎、斯堪尼亚......

**内资传统主流车企：**

吉利汽车、上汽乘用车、长城汽车、上汽大众、长安汽车、北京汽车、东风汽车、广汽、比亚迪、一汽集团、一汽解放、东风商用、上汽商用......

**全球领先一级供应商：**

博世、大陆集团、联合汽车电子、安波福、采埃孚、科世达、舍弗勒、霍尼韦尔、大疆、日立、哈曼、华为、百度、联想、联发科、普瑞均胜、德赛西威、蜂巢转向、均联智行、武汉光庭、星纪魅族、中车集团、潍柴集团、地平线、紫光同芯、字节跳动、......

**二级供应商(500+以上)：**

中科数测、ETAS、BlackDuck、NXP、上海软件中心、Deloitte、奇安信、为辰信安、云驰未来、信长城、泽鹿安全、纽创信安、复旦微电子、天融信、奇虎360、中汽中心、中国汽研、上海汽检、加特兰微电子、浙江大学......

**人员占比**

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJVW2JR9ib5icMR4wIs58nO6ia3OicH5l6vONnmuhfLqMKqj8T2AnD7W1vqQ/640?wx_fmt=png&from=appmsg)

**公司类型占比**

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJU6yKtYSJu4oPaJABYuCSyTpLXjRNbVv7OUTUUCxmB1OuPhtcM4j1kw/640?wx_fmt=png&from=appmsg)

**文章**

# [不要错过哦，这可能是汽车网络安全产业最大的专属社区！](http://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247535223&idx=1&sn=e30e07a44accd5b0e9ada3d8b537f977&chksm=e9270eacde5087bacb4d9c888f3a21ceae227156c89aba0be7d9ebc8b02a68b4f11e7595255a&scene=21#wechat_redirect)

[关于涉嫌仿冒AutoSec会议品牌的律师声明](http://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247531034&idx=2&sn=e466ca3e7c2927a91dd9a81be705afe1&chksm=e9273ec1de50b7d7f540ae2e4c255bfb42f842228a87f7dbc...