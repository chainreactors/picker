---
title: 人人都能成为代码审计专家（可落地，强的可怕）
url: https://mp.weixin.qq.com/s/B6CGKPMHn82kfB2Tamf5CQ
source: Doonsec's feed
date: 2026-03-13
fetch_date: 2026-03-14T04:06:35.036697
---

# 人人都能成为代码审计专家（可落地，强的可怕）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icX95QI1VmOzbPoIyU2HlYUMrjZFkEobGslZUs1EtOic5KQmgJmh7q8VfeicY7hCzMpgN0qKW0JDx7caD7vcibYqq97LGxM2hCRPCfWmLwgQEt4/0?wx_fmt=jpeg)

# 人人都能成为代码审计专家（可落地，强的可怕）

不秃头的安全

![]()

在小说阅读器中沉浸阅读

编者荐语：

愿景:让每一个人享受到代码审计的快乐!
最好本地搭建测试或有授权测试~

以下文章来源于嗨嗨安全
，作者自然嗨

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM5Kl0iaIajmaBnia5ibYiasQib2GSkW1FKjddVF1etfTWJbrJw/0)

**嗨嗨安全**
.

提供网络安全资料与工具,分享攻防实战经验和思路。

声明

该公众号大部分文章来自作者日常学习笔记，也有部分文章是经过作者授权和其他公众号白名单转载。请勿利用文章内的相关技术从事非法测试，如因此产生的一切不良后果与文章作者和本公众号无关。

滑至文末,获取“searchall”下载链接!

## **一.Trae SOLO模式**

在AI代码审计前，请先了解下Trae SOLO。（AI编程工具）

```
https://www.trae.cn/
```

![](https://mmbiz.qpic.cn/mmbiz_png/icX95QI1VmOzOCkK5yrRV9ahcIeYCicma4ick3ZicP2Cq26mgicpNaia6qy6VGx9jD1vzau13nbeLBnr8oUb1wGEgjTovBGGkq9qXjQu3icMch5vPI/640?wx_fmt=png&from=appmsg)

为什么要选择它作为代码审计工具的主体，主要是因为它可以免费使用glm5.0模型。

## **二.如何做代码审计**

这里需要三个基本要素。

1.测试环境（需授权的测试环境或者本地搭建环境）

一般采用docker环境搭建、或者phpstudy之类的的等等。

2.skills

这里我们选用code-audit技能

```
https://github.com/3stoneBrother/code-audit.git
```

```
# 在Trae中导入技能库 进入Skills模块 -> Import Local Folder -> 选择code-audit目录
```

![](https://mmbiz.qpic.cn/mmbiz_png/icX95QI1VmOwpyzbar1QcqEgBbGlqEDE1jSEe1qpslMFWAscpgIyTLT5jd2Dw5fLFvmLnMzR4SJKib8hCJMkZX6A21aic6b6qrBStcLpkMTkEs/640?wx_fmt=png&from=appmsg)

3. mcp

需要yakit的mcp，其中http\_fuzzer工具作为请求包/响应包。

![](https://mmbiz.qpic.cn/mmbiz_png/icX95QI1VmOxjOribA1U3WHsXuGBhVcWw4uNXA9iaUQo62d18h9C1MxwQ7RnK4j80WTKnzV217DiamvicueW5oibpJEH715YvAMJfRibyWibSzjqcY4/640?wx_fmt=png&from=appmsg)

trae上配置json

```
{   "mcpServers": {     "yakit": {       "url": "http://127.0.0.1:11432/sse"     }   } }
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icX95QI1VmOzVLiaG8PBc5Q1ibxYawzs7dc7tiaYWuLB8ibHHQwy3PpdkpTwbQR65FvfjzozBdJwnouWgOmHDolicDoCbkv68cYbcgQpDueiaZRrxE/640?wx_fmt=png&from=appmsg)

## **三.工作流实现**

有了以上基本三个要素，那么我们如何真正用起来呢。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icX95QI1VmOyRXhPGiayF9qGB2cDibfHSicDSbw2ibjZibjXwYgibtWP12zolUYTCYIw9d5bQIiaFKaqmtQOUE3CiaAYZicbNnniaLNRTwuzcH4gOJ63r8/640?wx_fmt=png&from=appmsg)

基本就是这个思想，在测试环境中，提供下url和认证信息，先让它生成一版审计报告，再让AI通过报告中的漏洞去生成请求包，在测试环境中不断让AI自行测试，直至让它判断漏洞是否真实存在，同步输出到报告中。

当然我们还需要提示词，去驱动该工作流的流程。以下是我常用的提示词，仅供参考，如有写的不对的地方或者可以优化的地方，可以后台私信我，进行沟通交流。

```
角色设定： 你是一位资深的网络安全行业的代码审计专家，擅长代码审计与漏洞验证。请针对当前项目执行一次“审计-验 证-迭代”的深度安全分析任务。 核心目标： 生成一份零误报的最终审计报告。所有列出的漏洞必须经过 Yakit MCP 的实际验证，并附带可用的 PoC（概 念验证）。 执行工作流：第一阶段：深度扫描与初稿生成 使用code-audit能力的 deep 模式（启动R1，R2，R3）对当前项目代码进行全量审计,并输出项目名称-日期- 审计报告.md。 第二阶段：自动化验证与 PoC 构建（核心循环） 请利用 Yakit 的 MCP 模块 加载项目名称-日期-审计报告.md报告中存在的所有请求包，对每个请求包进行 实战验证： 发送请求： 配置目标 URL 为 http://xx.xx.xx.xx/，并在请求中自动附加以下 Cookie: PHPSESSID=xxxxxx响应分析： 验证成功： 如果响应包符合预期，则判定为真实漏洞并把请求包和真实的响应包更新在审计报告中。 验证失败/存疑： 如果响应不明确或未命中，不要直接丢弃。 第三阶段：迭代修正与最终交付 针对第二阶段中“验证失败”或“存疑”的漏洞请求包，执行以下逻辑： 重新审计： 针对该特定漏洞点，重新分析该漏洞点，，结合 Yakit 返回的实际响应包数据，分析该漏洞是否 存在。 循环验证： 修正请求包后再次通过 Yakit 验证。 最终判定： 若确认为误报（经过多次迭代仍无法复现），则在报告中剔除该项。 若确认为真实高危漏洞，则更新报告。
```

感谢文章提到的项目及作者，如有侵权，请在后台私信！

📚 往期推荐

### [ChiXiao (赤霄)现代化红蓝攻防综合平台](https://mp.weixin.qq.com/s?__biz=Mzg3NzkwMTYyOQ==&mid=2247491100&idx=1&sn=8545c1289ba3fd70a315cdafef2ce507&scene=21#wechat_redirect) [FLUX-Web安全扫描工具](https://mp.weixin.qq.com/s?__biz=Mzg3NzkwMTYyOQ==&mid=2247490999&idx=1&sn=24f8e1f744d6e441db79cfd59c3c9888&scene=21#wechat_redirect) [白盒审计获得CNVD证书的案例](https://mp.weixin.qq.com/s?__biz=Mzg3NzkwMTYyOQ==&mid=2247490959&idx=1&sn=35282bf39f8b9b549fef5335e8f317e0&scene=21#wechat_redirect) [飞牛私有云fnOS远程命令执行漏洞与文件读取漏洞【批量验证脚本】](https://mp.weixin.qq.com/s?__biz=Mzg3NzkwMTYyOQ==&mid=2247490952&idx=1&sn=d22d3d66b990615483705493017833de&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_png/I2dhkmhKrSaQwuNHex2H6WnDNX0AzbNPHGdRfUwMicE3D3iborFiakjyqbDibhPZtx523RusapPyr3j91AwJE1UuhKTtQ7hJJ9PkbFudybbiavX8/640?wx_fmt=other&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=18)

**关于我们:**

感谢各位大佬们关注-不秃头的安全，后续会坚持更新渗透漏洞思路分享、安全测试、好用工具分享以及挖掘SRC思路等文章，同时会组织不定期抽奖，希望能得到各位的关注与支持，考证请加联系vx咨询。

## 1. 需要以下各类安全证书的可以联系~

①Cn\*d，NCC，NVDB🀄️高漏洞证书

②CNNVD中高\漏洞情报\ 一二三级支撑单位均可协助获得

③CISP、PTE/PTS、CISP-DSG、IRE/IRS、NISP一二级、PMP、CCSK、CISSP/CCSP、CISAW各种类、CCRC\CCSC、itil、软考中高级、CDSP各种类、CISA，oscp等等巨优惠。ISO27001、ITss服务项目经理报名等下证即可，证书组团报更便宜，可对公，可开专普票。以下是其他全部证书

【腾讯文档】【信息安全 数据安全 IT认证证书】～不秃头的安全Vx:Meditation0723

https://docs.qq.com/doc/DZmtOckpOakJrcFVv?#

想加群下方二维码，群过期或群满加下方vx拉：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/I2dhkmhKrSanVXQOGRzh9u4AnvjfIvtiaFz66lexmBZ0rQTQrw1kfianzPO71e1nfcMjYQrKYJNiaHWW5k64tO11OrylbKw12UTvKKJq7ibFlzE/640?wx_fmt=jpeg&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=21)

2. 需要入星球的可以私聊优惠？

```
1、维护更新src、cnxd、cnnxd专项漏洞知识库，包含原理、挖掘技巧、实战案例
2、fafo/零零信安 高级会员key
3、最新POC通用报告详情分享思路
4、知识星球专属微信“内部圈子交流群”
5、攻防演练资源分享（免杀、溯源、钓鱼等）
6、新鲜工具分享
7、不定期有工作招聘内推（工作/护网内推）
8、19个专栏会持续更新~提前续费有优惠，好用不贵很实惠
```

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/I2dhkmhKrSYFcTcyGTR08iaCVUxfocNWhswp0LfhYktviagD05xbMuYMkEMtBhrB5peygL0vQjG4rCOwEAC7Lbkg81UgX3lf4mj3GVmDHcGVQ/640?wx_fmt=other&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=25)

## 3、其他合作（合法合规）

1、承接红蓝攻防、渗透、安全意识培训、基线核查及加固、应急响应、重保防守、代码审计等安全项目（须授权），需要攻防团队或岗位招聘都可代发、代招（灰黑勿扰）；

2、各位安全老板需要文章推广的请私聊，承接合法合规推广文章发布，可直发、可按产品编辑推广；合作、推广代发、安全项目、岗位代招均可发布；

3、接受脱敏投稿,送一年知识星球及礼包。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/I2dhkmhKrSZA72dh8EJKRPhpMaA51dW6OOoItCzv9lSl4icGMaT7RI5Mibib48ZyYGYbyYNFa06MCJLlSicvpfzL4ibdTkM4aZ3FbUyVTjLxVzAk/640?wx_fmt=other&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=23)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/DicRqXXQJ6fVZYQ3CLswQeCkia9axLIjSV5hFqM9ouzExlwAsUtDeqEyXE2pLUIRCeDJ0m89GHyibMCFAHXBHmiacg/0?wx_fmt=png)

不秃头的安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/DicRqXXQJ6fVZYQ3CLswQeCkia9axLIjSV5hFqM9ouzExlwAsUtDeqEyXE2pLUIRCeDJ0m89GHyibMCFAHXBHmiacg/0?wx_fmt=png)

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