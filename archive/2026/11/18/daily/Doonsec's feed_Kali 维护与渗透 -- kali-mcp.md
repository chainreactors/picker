---
title: Kali 维护与渗透 -- kali-mcp
url: https://mp.weixin.qq.com/s/H2NdvNiIqNIoytmLmojOCQ
source: Doonsec's feed
date: 2026-11-18
fetch_date: 2026-11-19T09:39:30.649868
---

# Kali 维护与渗透 -- kali-mcp

# Kali 维护与渗透 -- kali-mcp

luziyao504
luziyao504

网络安全者

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

===================================

**免责声明**

请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。工具来自网络，安全性自测，如有侵权请联系删除。个人微信：ivu123ivu

一定要在虚拟机运行，工具下载链接：

公众号后台回复：20261118

链接仅一天有效，每日更新

kali-mcp 这个项目一句话说得清：把 Kali 上的命令行工具全包成 MCP 工具，客户端里填一个地址，就能用自然语言驱动这台机器。仓库 28 个文件、约 2800 行 Python， 运行依赖只有两个包 ：mcp 和 uvicorn。

我把仓库拉下来，在本机装了一遍、起了一遍、把 114 个工具逐个列了一遍。要提前说清一件事： 我这台不是 Kali ，所以扫描本身没验证；能验证的是它的架子——服务、鉴权、范围校验、依赖盘点、审计和报告。这篇只写跑通的，和没跑通的。

01

THE SHAPE

### 一条命令，把一台机器变成地址

安装就三步：clone、 sudo bash install.sh 、把打印出来的令牌贴进客户端配置。脚本会建 venv、装依赖、写 systemd 单元、生成令牌、自检一遍，结束时会直接把可粘贴的 JSON 打印出来。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PQNvx9ufMAjvbMwlZ0icVXjDmbe6Ym8KX3jHLjLv6wlISLaNf6QND6F51u0thWmYhoDguta2Wib3oqXF2x0YwIN21ddTQXeibUjg2O3dxJWlAA/640?wx_fmt=png&from=appmsg)

— 本机实跑：启动日志、/health、不带令牌的 401

上面那段是真的：服务起来后 /health 免鉴权返回 200，而往 /mcp 发一个 initialize 就是 401。令牌首次启动自动生成，写进 data/token.txt ，权限 600；比对用的是 定时安全比较 ，不是 == 。这几处细节做得比预期干净。

最容易填错的是 URL

| 客户端在哪 | URL | 结果 |
| --- | --- | --- |
| Kali 本机 | 127.0.0.1:8765 | 最快 |
| 同内网另一台 | Kali 的内网 IP | 要查 ip addr |
| 外网 / 跨网络 | 内网 IP 不通 | 上 VPN 或隧道 |

0.0.0.0 不能写进客户端。它是「监听所有网卡」的绑定地址，不是一个能访问的地址——README 专门用一整段讲这件事，说明踩的人不少。

02

114 TOOLS

### 114 个工具，全是别人的程序

接上 MCP 之后我数了一遍 tools/list ： 114 个工具、4 个 Prompt、4 个 Resource ，和 README 写的一致。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PQNvx9ufMAh4Rq83n0geE3v6Cqia824gKGEqm4svibIQiblXEaB2blo0wlibCWznH4bz8hUYeSd9KVEB2QV9JDTvibIHbXXicgiaT5KvZagQ3vFrEU/640?wx_fmt=png&from=appmsg)

— 本机实跑：握手、工具总数、几个工具的说明原文

把这 114 个摊开看，会发现它一个自己的扫描引擎都没有。全是 nmap 、 ffuf 、 sqlmap 、 hydra 这些现成 CLI 的封装。分下来大概是这么个形状：

44执行、系统、文件

持久 shell、后台任务、服务日志、cron、用户、打包解包、校验和。这部分和渗透没关系，是运维。

39网络、侦察、Web

nmap、masscan、subfinder、amass、enum4linux、ffuf、nuclei、nikto。真干活的主力都在这一段。

21凭据、利用、无线

hydra、john、hashcat、searchsploit、msf 系列、airodump。到这一段，已经不太适合交给模型自己决定了。

10元工具

武器库盘点、环境体检、装工具、记 finding、设范围、导报告。这 10 个才是这个项目真正自己的东西。

一个值得抄的实现细节

工具内部有两条执行通路： 能参数化的走 argv，不经过 shell ；只有确实要 sudo 的才退回字符串拼接，而拼之前统一 shlex.quote 。端口、脚本名这类参数还有一层白名单正则。对一个要接受模型自由输入的渗透工具来说，这条边界比多写十个工具重要。

它还知道自己缺什么。跑一次武器库盘点，我把 69 个常用工具挨个 which 了一遍，最后给出缺什么、装什么：

![](https://mmbiz.qpic.cn/mmbiz_png/PQNvx9ufMAjhIZPEqCa4ia9DiaKibibUIzXBqZA6N9cKKiaEfvGD35zJ9oD0PdSMNtEKGy1JcM5VFbLQcJ6nG4olgiaibJ10VyvJU2W9mcm0IDR9wU/640?wx_fmt=png&from=appmsg)

— 本机实跑：69 项里 15 项就绪（节选，省略 6 个分类）

NOTE

我这台不是 Kali，15/69 这个数字只能说明「没装」，说明不了「不能用」。装到真机上这一屏应该接近满绿——它的价值在于：缺哪个、怎么补，都直接写在返回里，模型下一步不会瞎猜。

顺带说两个数字对不上的地方。README 的模块表分项加起来是 105，代码里实际注册 114；自带测试只断言 工具数 >= 80 ，不是 114。不影响用，但说明这张表是手工维护的。

03

THE GATE

### 范围校验，挡在「装没装」之前

这类工具最该先回答的问题是：模型要是打了不该打的目标，谁拦？kali-mcp 的答案是 scope ：设一组 IP、CIDR、域名，之后所有带目标的工具都先过一遍判定，越界直接返回、不执行。

关键在于顺序。看代码，每个工具都是先 guard() 再 need() —— 先判该不该打，再看打不打得动 。所以哪怕机器上没装 nmap，越界目标也会先被范围拦掉，而不是先报「缺少命令」。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PQNvx9ufMAjSQiaIpJBS7rzdGDGB39Vo1CXYfQKzicg41Ribc9YryooJFXFwDQ24fdD0gic5pxC41YsWsujicR1VPDbbbDQnRMmkMPnPUnoyJAvU/640?wx_fmt=png&from=appmsg)

— 本机实跑：同一组范围，两个不同工具被同一处判定拦下

覆盖面上，侦察 12 处、Web 11 处、网络 7 处、凭据 2 处、利用 1 处，合计 33 处校验。文件类、系统类工具不做范围校验——它们动的是自己这台机器，不是别人的资产，这个取舍说得通。

然后我试了它的边界

判定的实现是「通配 + IP 网段 + 后缀」三重匹配。我直接调这个函数，拿八种目标各试了一遍：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PQNvx9ufMAhEaLGMz6YBl6d3aQQvmFpmmnByjuzhIxjrPxFtqSjA6diaB0G6XDwBRwSPedIJpeib4uXLGAaK6ucCstsGtIM7qNibdafbBvdsHQ/640?wx_fmt=png&from=appmsg)

— 本机实测：同一函数在「未设置」与「已设置」两种状态下的判定

三行值得单独拎出来看。第一， 不设范围等于不校验 ，返回的是 None 不是 True——装完不设范围，所有目标都是放行的。第二，写 \*.example.com 并不覆盖 example.com 本身，根域要单独写一行。第三， a.b.example.com 是放行的——通配符跨点匹配，比 DNS 语义更松。

所以装完第一件事不是扫，是 kali\_scope\_set。它的围栏默认是开着的，但门是虚掩的。

04

THE GAP

### 三处该补，但不影响它值得看

项目自称有「全量审计」：每次工具调用写一行到 audit.log 。我跑完上面那一串之后去看，只有两行。

![](https://mmbiz.qpic.cn/mmbiz_png/PQNvx9ufMAhYcqpK2rCicW0Hp3VUHuLlf6CjkrLv403hK1zg4KWRIWTFg2G2EJd5KumBeGcYibQ51bBJsQLlQribZHQy4iayZuXZnNKBN0NYQGg/640?wx_fmt=png&from=appmsg)

— 本机实跑：两次被拦下的调用，审计里没有留痕

原因不难找：审计写在执行函数里，而 guard() 在更前面就 return 掉了，压根走不到执行。于是 「被拦下」这件事本身没有记录 。而上一条我恰恰认为最该留证：一个渗透 Agent 去碰范围外的目标，不管拦没拦住，都该是事后要复核的动作。

NOTE

另外两处：服务默认绑 0.0.0.0、默认以 root 运行、令牌以明文存在数据目录里——README 都写了提醒，但默认值仍是那个最宽的。还有握手时自报版本 1.30.0，而包版本是 1.0.0，原因是 FastMCP 没传 version，取了底层库的号。

说这些不是挑刺。反过来看，它已经做到了很多同类项目不做的： 删除默认进回收站 （只有显式关掉备份才真删）、每次执行留原始产物并按 400 份滚动、finding 能直接导成 Markdown 报告、装成 systemd 服务带 CI 和冒烟测试。我这边 5 个测试 1.67 秒全过。

∞

THE END

### 围栏不是保险

把 Kali 交给模型，风险从来不在于它不会用工具，而在于它太会用。这类项目的价值，也不在于多接了 114 个命令，而在于 把「不许做什么」写成了代码 ：范围先判、参数走 argv、删除留后路、产物留档。

但它是围栏，不是保险。默认不设范围、默认 root、默认 0.0.0.0——这三条任意一条没改，围栏就是敞着的。真正决定边界的仍然是那个设范围的人。

「工具只负责把门装上，钥匙在谁手里，是另一回事。」

我这边只在本机回环地址上验证了服务与判定逻辑，没有对任何外部目标发起请求，也没有跑成一次真实扫描。想看扫描效果，得自己在 Kali 上装一遍——那种场景下， 先设范围再动手 ，这句话不是客套。

END

一定要在虚拟机运行，工具下载链接：

公众号后台回复：20261118

链接仅一天有效，每日更新

**·****今 日 推 荐****·**

![](https://mmbiz.qpic.cn/mmbiz_png/PQNvx9ufMAia0hC6ib15Xxa0A5wHwCnuEI51wVHJl2uVBrwCZFZmEqjClS8NedricR45wnesyXP6VZAmPeQibXKzXUm0J5v81qkqKMhrSc4sC9I/640?wx_fmt=png&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/0JJXjA8siccyMF9RkfYpDn6879qdDPwuSUicNgL09meX6BzicL78PBTD7ue9VFAia6Ye1o1uvXSyXLW7hvhkLmhj9g/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过