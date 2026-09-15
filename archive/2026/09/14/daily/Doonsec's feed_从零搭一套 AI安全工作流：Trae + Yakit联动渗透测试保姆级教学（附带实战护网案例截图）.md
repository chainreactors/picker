---
title: 从零搭一套 AI安全工作流：Trae + Yakit联动渗透测试保姆级教学（附带实战护网案例截图）
url: https://mp.weixin.qq.com/s/2J5zfnQ65YWI6JDdnwYJYw
source: Doonsec's feed
date: 2026-09-14
fetch_date: 2026-09-15T07:00:34.992468
---

# 从零搭一套 AI安全工作流：Trae + Yakit联动渗透测试保姆级教学（附带实战护网案例截图）

# 从零搭一套 AI安全工作流：Trae + Yakit联动渗透测试保姆级教学（附带实战护网案例截图）

原创

zkaq-zbs
zkaq-zbs

掌控安全EDU

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

扫码领资料

获网安教程

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrpvQG1VKMy1AQ1oVvUSeZYhLRYCeiaa3KSFkibg5xRjLlkwfIe7loMVfGuINInDQTVa4BibicW0iaTsKw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=0)

![图片](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaaJcib7FH02wTKvoHALAMw4fchVnBLMw4kTQ7B9oUy0RGfiacu34QEZgDpfia0sVmWrHcDZCV1Na5wDQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=1)

# 本文由掌控安全学院 - **zbs 投稿**

**来****Track安全社区投稿~**

**千元稿费！还有保底奖励~（  https://bbs.zkaq.cn   **）****

## **0x00  前言**

用Trae + Yakit 联动搞自动化渗透，这事儿我跑通了。从零搭一套轻量级 AI 漏洞检测流水线，靠智能体调度 MCP 驱动 Yakit 干活，实战验证整条链路可用。下面手把手教你复刻。

## **0x01  环境搭建与工具联动配置**

整套方案主打轻量——不需要虚拟机，Windows / Mac 都能跑，跟着做就行。四个步骤搞定环境：装工具、开 MCP、建智能体、绑配置，半小时内全通。

### **1.1  基础环境准备**

先把 Trae 和 Yakit 的最新版装上。Yakit 装完别关，让它挂着跑，端口别被占，防火墙记得放行。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoJvy5Tl36alBau5tFkLvjNPtN27uYfmEHvX4YUicKNgGpb24tPb7ptGzujVh0HCk1d5DUuMng2QEtibpoAwEj1EowibewvIq2orpM/640?wx_fmt=png&from=appmsg)

装完 Yakit 打开就是这界面——MITM 交互式劫持页，左边是 17 个被动检测插件（SQL 注入、XSS、命令注入啥都有），右边是代理参数配置，默认监听 127.0.0.1:8083。别急着点"劫持启动"，先把 MCP 开了再说。

### **1.2  开启 Yakit 的 MCP 服务**

打开 Yakit，点右上角齿轮 → 试验性功能 → Yak MCP，进入 MCP 配置页。这是让 AI 能"遥控" Yakit 的关键一步。

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoLvD1CuqO0FhnFRk4f7TibIjAKibLNkJQ1kPLoxiaAAmw4865UzfVZA5VFDtRvPyS9mibd1D3rWoTHyazNXVZwypwMbDmwJ4l4Xvf4/640?wx_fmt=png&from=appmsg)

配置页面能开三类能力开关：MCP 内置工具（port\_scan、httpflow 这些老牌 Yak 工具集）、AI Tool Framework（代码审计、脚本执行等 AI 能力）、桥接外部 MCP（把其他 AI Agent 的工具也拉进来）。底下还有一大排可开关的工具清单，按需启用就行。

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoL8XqkziclfpPOkI3yQFOBqUvID5ia6URBW0xnhSm8NjcsfB4uwI6gnSgJn0ADsswXCJCq8gZwlLt4NE8ADDFZTtwUVdMl19nicPw/640?wx_fmt=png&from=appmsg)

配置完点启用，MCP 服务就跑起来了。选 SSE 模式，地址 http://127.0.0.1:11432/sse，页面底部会绿字提示"MCP 服务已启动"。旁边还贴心给了 JSON 配置，复制出来后面要用。

### **1.3  创建渗透测试智能体**

环境通了我们回到 Trae，新建一个自定义智能体。你可以手动填表，也可以直接点右上角的「智能生成」——对，就是那个带绿色加号的按钮。

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoKcSp6iamSgp3NB1ozIibEzs3wcCySOe5fC6sea3f0h2duw8icIfSgdqicMeem4uOKhSrL0Q0FZ6GTOjzoukqndcQgqkia8LJKkNGpY/640?wx_fmt=png&from=appmsg)

点完「智能生成」会弹出个窗口，你只要用大白话描述想要啥智能体就行——比如"帮我做个护网渗透测试的智能体，用 Yakit 扫漏洞"，它就自动帮你把名称、提示词、调用规则全填好。懒人福音，填表地狱直接解脱。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoKCcOWiaxdfXNAkaKEQ6RdqsG8hpNWC7BDF272QZicyQb5PNJ5l0vSTs2BjKzktnA2iaXaqMc7y04GIuZUmsKKDTAN890KKibSPzLE/640?wx_fmt=png&from=appmsg)

填完之后能看到完整的智能体配置页：名字、提示词（写清楚这是什么场景的安全评估智能体）、调用时机——"在 xx 场景对目标做渗透测试时调用"

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoJyCnRgJicEhD2zf1dPgN4Bt2qwg7aFlOSrtUpoIoUe5VpCaohib3n9ianTXgvxP16ha5LVrdxFVicY4wwHib66iaYzCOia38wMMhgByY/640?wx_fmt=png&from=appmsg)

配置好智能体后，Trae 会把这个智能体加到可调用列表里。在「Agent」菜单里能看到你的「福州护网渗透测试」智能体，红色框标注的是「编辑工具」入口，方便后续调整。

### **1.4  配置 MCP 协议并绑定工具**

到 Trae 的智能体配置页，点「工具 → 添加 MCP Server → 手动配置」，把 Yakit MCP 的 JSON 配置粘进去。保存后勾选「Yakit MCP」绑定到你的渗透智能体，通道就算打通了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoLvHWbmV0gWfm8wUCFXVdCdicPibXjNgZ0Er9HBGiaSOLLlRDOgzUuics2J6mEZZrJdcUGzFiaSv6IHe9OsQpyRT9JO9OBIs85gwtxI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoIfE8bekuRUEjGm3Agy7WZt6GtfOnS62DgJExXpp4tEX7Mdfk17q1S27wQMr5ndZiafnlPdhl0LtRicWsAA18svEAytgm7hPAFbU/640?wx_fmt=png&from=appmsg)

在 MCP 管理页能看到刚加的「yakit」服务器，绿勾代表连接正常，开关是开着的，就说明 MCP 通道已经通了。

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoKicfLlicoSpBosgtk4PDGCbLFHmvtAx1wyN7pp47iaDyGalicLJ8BQU4icP0xu9pKSSPRcao3iaMUyeZKcQ1XMguCiaaRfdVXvXT5A4o/640?wx_fmt=png&from=appmsg)

点击「手动配置」后弹出一个 JSON 输入框，把 Yakit MCP 的地址粘进去就行。配置不长，就几行：类型 SSE，地址 http://127.0.0.1:11432/sse。弹窗底下还有个黄色警告"配置前请确认来源，甄别风险"——官方提醒你别乱粘别人的配置，安全第一。

到这里，环境搭建全部完成。Yakit MCP 通了，Trae 智能体绑好了，接下来就是实战环节。

## **0x02  测试实操与结果展示**

纸上谈兵没意思，拿 HW 实战说话。下面用真实业务目标跑一遍 AI 渗透测试全流程，看看这套组合拳到底能打多重。

### **2.1  下发测试任务**

在 Trae 智能体里直接输入检测指令就行。比如"测试这个链接有没有 SQL 注入"或者"换一个目标，这个 IP 被提交过了"——Trae 自动调度 MCP 去调 Yakit 干活

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoIPgXvqpTrlLYYicLyA9U0bBfB6dWMggMNv0uscDGsFWTrUFUSC2R0NPtkUtjNfiaTF9wUFXgpJRYWia0HpibOWQArSL3HKiaYYuE2c/640?wx_fmt=png&from=appmsg)

AI 收到任务后，自动查看之前的快速扫描结果，从里面筛选出还没测过的新目标。中间还顺手帮你破解了 MD5 密码、生成了 PoC 成果报告，整个流程一条龙——你只管说"换目标"，它就自己去翻结果找新靶子。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoKjh7hUBlibdLCedjuGT6UN1QhkwyuPGLNYqglh896hAiaDknskjzKbf2OcRX79BeRibhjY3B7rRamc6Bo2PqGjgyctudG5cB3wK8/640?wx_fmt=png&from=appmsg)

AI 接到指令后，先验证目标链接能不能通，通了就开始疯狂发 payload——连续调用了多次 Yakit 的 HTTP 请求工具，把各种 SQL 注入的测试 payload 挨个砸过去。你只管提需求，剩下的它自己编排。

### **2.2  自动化执行过程**

Trae 自己拆解任务、编排步骤，调度 Yakit 对目标跑渗透测试——你全程看戏。AI 会自动写脚本、跑端口探测、发现漏洞后自主决定下一步打哪里，比你在那手动一个个测快了不知道多少倍。

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoKlBPvj9AmTgwefKLn1HDdTnMnSgKIibenZnL5iagClQt0oyQAYHuJCIRYW0AZg2AThl6Iffh0PCcUq7Csa5OfS5Kw3Cx5Uic2wWc/640?wx_fmt=png&from=appmsg)

跑起来之后，AI 先自动探测 Web 端口，发现目标有 Druid 监控和 Swagger UI 两个大宝贝。Druid 默认弱口令 admin/admin 居然能登录？Swagger 接口文档也暴露在外面？AI 立刻调转枪头，先打这两个方向。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoJib3ftxsJ8ogN8NTezRx3JgraDEyaoRwfiawjiax6MYNosB2ZH4etUR5YMpmPdiacSZMStw7ibIjKd7iaibyFZZcSVmv4V00SroYiaIps/640?wx_fmt=png&from=appmsg)

自动探测到 8082 端口跑的是后端 API 服务，一口气发现了 4 个可利用点：Druid 登录页可访问、Swagger v2/v3 接口文档都在、登录接口不校验验证码、验证码图片接口不用认证就能拿。AI 直接规划了 3 步后续行动：验证 Druid 弱口令、解析 Swagger 测未授权接口、暴力破解登录密码。

**2.3  测试结果与报告输出**

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoIGM7yZCGw2T1E1fE3DgZvEGmPJHy8XdyddxxOQWxOvSUMThmTZZxUUanBdxIiaUqKHVUtKvib5Htic8BCrdOEDHHWvEBltWE0dn4/640?wx_fmt=png&from=appmsg)

最终确认了 6 个漏洞：2 个高危、2 个中危、2 个低危。高危的已经实际拿到数据和下载到文件了。

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoLT1sUMv6SvD18iaxrT1tqw7u3d8bSicp1AOSygATrT9PaDoUvFMIppdK6ezNTJHo61ZhCBY9fFyd35YrjUGnwxpphmL71ApNsNQ/640?wx_fmt=png&from=appmsg)

以上是漏洞确认结果。但最炸裂的还在后面——AI 在深挖数据的时候，发现数据泄露规模远超预估：一张表就泄露了 24 万条记录，另一张 11 万条，最少的也有一万。数据表名和敏感内容都脱敏了，但光看记录数就够让人倒吸一口凉气。

## **写在最后**

整条链路跑下来，从环境搭建到出报告，核心就是三件事：Trae 当大脑，MCP 当神经，Yakit 当拳头。AI 帮你拆任务、编步骤、写脚本、跑检测、出结果，你只管发号施令和拍板决策。

当然话说回来，这套方案本质是辅助工具，不是全自动骇客套件——合规边界、目标授权、结果研判还是得人把关。工具再强，也替代不了安全人的判断力。

感兴趣的同学可以按上面的步骤自己搭一套试试，有问题评论区见。

申明：本公众号所分享内容仅用于网络安全技术讨论，切勿用于违法途径，

所有渗透都需获取授权，违者后果自行承担，与本号及作者无关，请谨记守法.

![图片](https://mmbiz.qpic.cn/mmbiz_gif/BwqHlJ29vcqJvF3Qicdr3GR5xnNYic4wHWaCD3pqD9SSJ3YMhuahjm3anU6mlEJaepA8qOwm3C4GVIETQZT6uHGQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=34)

**没看够~？欢迎关注！**

**分享本文到朋友圈，可以凭截图找老师领取**

上千**教程+工具+交流群+靶场账号**哦

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrpvQG1VKMy1AQ1oVvUSeZYhLRYCeiaa3KSFkibg5xRjLlkwfIe7loMVfGuINInDQTVa4BibicW0iaTsKw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=35)

**分享后扫码加我！**

**回顾往期内容**

[网络安全人员必考的几本证书！](http://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247520349&idx=1&sn=41b1bcd357e4178ba478e164ae531626&chksm=fa6be92ccd1c603af2d9100348600db5ed5a2284e82fd2b370e00b1138731b3cac5f83a3a542&scene=21#wechat_redirect)

[文库｜内网神器cs4.0使用说明书](http://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247519540&idx=1&sn=e8246a12895a32b4fc2909a0874faac2&chksm=fa6bf445cd1c7d53a207200289fe15a8518cd1eb0cc18535222ea01ac51c3e22706f63f20251&scene=21#wechat_redirect)

[重生HW之感谢客服小姐姐带我进入内网遨游](https://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247549901&idx=1&sn=f7c9c17858ce86edf5679149cce9ae9a&scene=21#wechat_redirect)

[手把手教你CNVD漏洞挖掘 + 资产收集](https://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247542576&idx=1&sn=d9f419d7a632390d52591ec0a5f4ba01&token=74838194&lang=zh_CN&scene=21#wechat_redirect)

[【精选】SRC快速入门+上分小秘籍+实战指南](http://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247512593&idx=1&sn=24c8e51745added4f81aa1e337fc8a1a&chksm=fa6bcb60cd1c4276d9d21ebaa7cb4c0c8c562e54fe8742c87e62343c00a1283c9eb3ea1c67dc&scene=21#wechat_redirect)

## [代理池工具撰写 | 只有无尽的跳转，没有封禁的IP！](http://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247503462&idx=1&sn=0b696f0cabab0a046385599a1683dfb2&chksm=fa6bb717cd1c3e01afc0d6126ea141bb9a39bf3b4123462528d37fb00f74ea525b83e948bc80&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/BwqHlJ29vcqJvF3Qicdr3GR5xnNYic4wHWaCD3pqD9SSJ3YMhuahjm3anU6ml...