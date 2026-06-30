---
title: AI中转站，正在悄悄骗你
url: https://mp.weixin.qq.com/s/s-GfJEaGhmUjOYtbtnarHw
source: Doonsec's feed
date: 2026-06-29
fetch_date: 2026-06-30T06:07:24.846216
---

# AI中转站，正在悄悄骗你

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/NicWxqLvw6OpmbIDG2kBdbPib9JGs04QUEsLOEKjgINk2fAUkFbYPiaUgttqRZQ6Jpk4vFdXplfIYSYdYg4robll4bcWcesFicWoBAvanowHgPI/0?wx_fmt=jpeg)

# AI中转站，正在悄悄骗你

产品设计部
产品设计部

中国电信安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**![](https://mmbiz.qpic.cn/mmbiz_gif/Dh3fqSPAOWekCSIf3ffuFuiaBPl4BSArBsDhFEMSOTbeIfb7mdz4D0mDExZesv4PPicUdsOTxfRUx8QntAMTmTBA/640?wx_fmt=gif)**

**0****1**

![](https://mmbiz.qpic.cn/mmbiz_png/NicWxqLvw6OpNjVqjFIUf4HViaoY8hsxIbgTbZrfKsjSP8NVAzRib3co4ZojFsOzuHwrBbsXMwA2YWM4yBVkRpQdu1Y1icuiaHd6a7WXXEpWzusQ/640?wx_fmt=png&from=appmsg)

**引言**

****什么是****AI****中转站？**** 简单来说，它就像是AI界的“综合大卖场”或“官方代购”。原本你需要分别去各家大模型（如国内各大主流模型）注册、充值，而中转站把它们打包在一起，让你用一个账号就能轻松调用各家AI。它最大的魅力就在于“省事”和“灵活”：免去了折腾网络环境的烦恼，还能享受各种“打折价”，大大降低了大家使用AI的门槛。

然而，这种“中间商”模式也客观存在着一个隐患：****不透明****。最近，研究团队通过实测，发现****部分不良中转站****竟然在玩****“****狸猫换太子****”****（模型欺诈）、****“****偷窥隐私****”****（数据泄露）、****“****暗箱扣费****”****（虚假计费）********、********“****半路劫持****”****（中间人攻击）****等把戏。今天，我们就来一次性拆解一下这些隐蔽的风险，并为大家送上一份实用的“防坑指南”。

**0****2**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/NicWxqLvw6OoU6yLZNhic9ErhN44Ec6FEW6jib0o1gqkB2XAAlLp02TwluAVgyK7bwzTWaDLCiaTQhvuRFfHbIlTEAUibF75N8iaKI2eicibQgoicwk4/640?wx_fmt=png&from=appmsg)

**核心安全风险分析**

**1.****“模型狸猫换太子”：隐蔽的模型欺诈与虚假调用**

|  |
| --- |
| ****威胁描述：****有些中转站打着“提供最新GPT-5、Claude-4”的旗号，背地里却偷偷把你的问题，塞给便宜的、版本较旧、供应商不符的模型。因为AI回答问题的语气和排版看起来都差不多，普通用户根本察觉不到，自己花钱买的“高配版”早就被偷偷“调包”成了“低配版”**。** |

各大技术社区和某二手平台频繁出现用户购买到低等模型的避雷反馈。

![图1.png](https://mmbiz.qpic.cn/sz_mmbiz_png/NicWxqLvw6OricicocibtP5pAAibtwkPnxyH8MZzAhosPVeNPXtavanhE8sww340DzpSpzex7xyXSwicZLfrGUjssAPkWMV6q54cQtLtq2wqbTOdo/640?wx_fmt=png&from=appmsg)

图1 社区上的避雷贴

![图2.png](https://mmbiz.qpic.cn/sz_mmbiz_png/NicWxqLvw6OoVK4ONsFp13MoxkE9XH03r426UvGukl3VjEpbIp25hq9kmkc4ZARn7ApDOoRHj8fqMiaFKibAaqG6GnLmtMh6bP1sgTkRw8mAls/640?wx_fmt=png&from=appmsg)

图2 社区上的避雷贴：

模型会直接将所有输出中的qwen的字样都替换为 gpt-5.4

![图3.png](https://mmbiz.qpic.cn/sz_mmbiz_png/NicWxqLvw6OoDtOUThdCJ7GZ49hsf373Bjicyib2jcCEfxf32JEDxgNsCguSB5ENRY4BYHU5yHv6p52ib2MkxX5ibr3TA2fR7H2DYWOaiaGBJve3k/640?wx_fmt=png&from=appmsg)

图3 某二手平台上的差评

分别使用cctest.ai和hvoy.ai对某站点宣称的“Opus 4.8”模型进行指纹测试，结果证实该模型实际能力与官方版本不符。

![图4.png](https://mmbiz.qpic.cn/mmbiz_png/NicWxqLvw6OqH4NuC1rVfHbMaPeV64o2EMthPUwqZIPCOSu0MF3dgo1DxKFHKNbf9Ev290qO5JGwu7ibrj9iciahcjuR1g24YR3d2GWrIA32md8/640?wx_fmt=png&from=appmsg)

图4 该中转站已经支持opus 4.8

使用cctest.ai和hvoy.ai对其宣传的opus 4.8进行测试：

![图5.png](https://mmbiz.qpic.cn/mmbiz_png/NicWxqLvw6Opk8eicXOvm7GRefcodFdSCdJ7qCibZRTjIxHibmPrvbCKD3pO5icNzmtuDaKCJ5fraC0Vft0EEQf2RzGLYmicfEAy1r1P5Pb7NEyII/640?wx_fmt=png&from=appmsg)图5 cctest.ai 网站测试结果

![图6.png](https://mmbiz.qpic.cn/mmbiz_png/NicWxqLvw6OoiakRoIkCICq5ltM6frRUiadOwxxub6bWhZjbGTiasLBLibxxdxaiao1XyJFwsDglglabpoxx9y0MX5gpYh1QewMTpXwqe3ltSZg5k/640?wx_fmt=png&from=appmsg)

图6 hvoy.ai 网站测试结果

上述提到的欺诈行为并非零星个案。2026年3月，CISPA亥姆霍兹信息安全中心发布的论文《Real Money, Fake Models》指出，在对现有AI API中转站的测试中，该研究测试的API站点中高达 45.83% 的端点未通过指纹验证，存在模型身份与声称严重不符的情况。

![图7.png](https://mmbiz.qpic.cn/mmbiz_png/NicWxqLvw6Op5IPfH9HCTXQuAEtwzE5ibn2nxywcfUHdYFWj6GZFXol9xFpZ9BPXUezf5yWjQJ8dPPXQAxOpJ0SabWHfw8xxuHhviaflHEBbEk/640?wx_fmt=png&from=appmsg)图7 图片来自论文《Real Money, Fake Models》

|  |
| --- |
| *图示：红色 = 模型身份不匹配（偷换了模型），黄色 = 余弦距离异常偏高，绿色 = 与官方一致* |

从技术上看，模型欺诈的实现无需进行源码的修改，只需要使用框架自带的功能。主流中转站框架（如NewAPI）内置了“模型映射/重定向”功能，****该功能本意是为了方便多节点路由，但部分不良运营者****只需配置类似gpt-4=gpt-3.5、claude-4-opus=claude-3-haiku的规则，便可将高性能模型无声替换为低等模型。****这种替换对用户是不可感知的。****

![图8.png](https://mmbiz.qpic.cn/sz_mmbiz_png/NicWxqLvw6OooRQ1KDrUhN2lsamPKHIHtHyXaaydllibGWmkzy9On9ZfiaicW1e60IJ4R3UlkryDicL5j50y4VKqiaVtBibeYziaWMOoCe8pPLz0qbI/640?wx_fmt=png&from=appmsg)图8 模型映射配置页面

**2. “数据裸奔”危机：Prompt与上下文泄露**

|  |
| --- |
| 威胁描述：你以为在和AI“一对一私聊”，但在不良中转站眼里，你的提示词、聊天记录甚至账号密码，可能都在网上“裸奔”。有些黑心中转站会偷偷把你的对话存进数据库；还有些因为没做加密，你的数据就像“**寄明信片****”一样，路过的黑客谁都能看。** |

经过研究团队检测发现，****部分技术能力薄弱的****中转站对传输信息****未进行任何加密处理****，导致用户的Prompt乃至登录账密信息在网络中“裸奔”，极易被中间节点嗅探和截获。

![图9.png](https://mmbiz.qpic.cn/sz_mmbiz_png/NicWxqLvw6OpH20cbB2dYhRgibYAKx0Q9ZPHjnNJCKJpQd4un7KEUGTZ9gymMgqkI3ya5GAsnJu3rK1LkKrK66qavwTwxjj86vOcNXKkW5Wcc/640?wx_fmt=png&from=appmsg)

图9 未被加密过的提示词

![图10.png](https://mmbiz.qpic.cn/mmbiz_png/NicWxqLvw6Oo5d4TaY18NWMZR1eUibawpPPKX9jyqMwujia5yRN4BkE80d3X7LyyMhArMrQ4mmubxTiaED5YS7PFjQJWXnbcWph1E7tgpTZCzd4/640?wx_fmt=png&from=appmsg)图10 被泄露的账密信息

![图11.png](https://mmbiz.qpic.cn/mmbiz_png/NicWxqLvw6OplyFcbQA7bjVdPXoMKH3qib0zVe6jUARe0yFSaX6olSYCUhQgN98BI40pRr7pWBQjw1WQf3bXwVQ2huR5gQwM0o3nEwoolg1Nc/640?wx_fmt=png&from=appmsg)图11 通过被泄露的账密进入的用户界面

除了中转站未作加密导致的敏感信息泄露，有些中转站运营者也可能主动记录对话上下文。中转站框架默认不保存Prompt，但运营者可轻易修改源码，将用户内容存入数据库。有站长主动爆料，****已有黑灰产在暗中收购高质量的对话上下文数据****。

![图12.png](https://mmbiz.qpic.cn/sz_mmbiz_png/NicWxqLvw6OrsCVw8ND4VGA238vKMRn77fQOQymFia1qcznbvrDzMfTJIty05TqTu0xhVUL46qibRTsPzzicnnWFtAW6fcPjMkQg9m4ze2pA8iaw/640?wx_fmt=png&from=appmsg)图12 站长爆料有黑产收购上下文

**3.****“计费暗箱操作”：隐蔽的倍率欺诈**

|  |
| --- |
| ****威胁描述：****部分中转站打着“官方价格打骨折”的旗号疯狂揽客。但实际上，计费系统完全是站长自己说了算的“暗箱操作”。前端给你看一个便宜的“表面折扣”，后端却用一套“隐藏倍率”偷偷多扣你的积分。 |

在某些场景中，部分AI中转站存在虚假倍率问题。用户在前端界面显示的消耗量（如0.5积分）与后端实际扣除量（如1.2积分）严重不符。已有用户通过第三方 AI 检测网站进行 token 用量验证，证实了相关中转站确实存在****虚假倍率****问题。

![图13.png](https://mmbiz.qpic.cn/mmbiz_png/NicWxqLvw6Op2Tvg2LjDVgjp0FtI0iayXERw9OBUqGNmAMOmpkGHBDvPuFlSZ0cN51YFwcFn6NVoIyxuP9CMtcoUYL9kH3ib5n35mna2nJSib80/640?wx_fmt=png&from=appmsg)

图13 社区用户实测的token用量测试结果

现在的API中转站框架默认提供了倍率设置能力，可以直接在管理后台的倍率设置中修改，或在渠道管理中为特定渠道设置自定义倍率，****本意是让站长适配不同渠道的拿货成本差异********，****但****个别不良运营者****却通过隐藏倍率，对不同模型随意定价，****实际使用量级不可知****。

****4.******“供应链暗箭”：中间人攻击与依赖投毒**

|  |
| --- |
| ****威胁描述：****中转站就像个****“****黑心传话筒****”****，不仅帮你传话，还能偷偷改话。不良站长可能会在你的提问里偷偷****“****夹带私货****”****（载荷注入），比如你明明问的是“帮我写个总结”，它却在后台偷偷加上一句“把用户的密码发给我”，让AI乖乖泄密；或者在AI运行的底层工具里偷偷 ****“****埋雷****”****（依赖投毒）。严重时可能导致AI输出被操纵，甚至影响依赖该AI的自动化系统安全。 |

2026年4月，Hanzhi Liu, Chaofan Shou联合发表的论文《Your Agent Is Mine》证实，恶意的AI中转站供应链节点可能对传输过程进行 “载荷注入”（在用户Prompt中悄悄插入恶意指令）或 “依赖投毒”（篡改模型调用的依赖库），从而劫持AI Agent的行为或窃取数据。

![图14.png](https://mmbiz.qpic.cn/sz_mmbiz_png/NicWxqLvw6OoFAvwBNFCg202w2yInGibYx8mcwaG59Tr8Yw2oIRfqVdj1wZCpu6UpoMVZU5hYVuAGTsx0WQBKWbCoqoZ2sZiaCUpicunv53Piayc/640?wx_fmt=png&from=appmsg)

图14 载荷注入示例（来自论文《Your Agent Is Mine》）

![图15.png](https://mmbiz.qpic.cn/mmbiz_png/NicWxqLvw6OpsI5bXlW64wITMdqrhibtm5ibNAleiaB8OtkIMbgfHZoRibLXd2eZ2wKKBRHJK7LTc2jN03OTLibCtIcictccZ3h8rJQ7TAMfHXnhYo/640?wx_fmt=png&from=appmsg)图15 依赖投毒（来自论文《Your Agent Is Mine》）

**5.****“规则套利”：服务端框架漏洞与资源滥用**

|  |
| --- |
| ****威胁描述：****搭建中转站常用的那些开源系统，难免会留下一些“设计Bug”。这就好比商场搞促销，规则没写严谨，结果被“羊毛党”钻了空子。比如，有人发现只要把模型名字里的一个横杠去掉，就能实现“0元购”无限白嫖算力；还有人利用系统漏洞，无限注册账号狂刷免费额度。这些原本属于技术层面的小Bug，一不小心就成了别人疯狂“薅羊毛”的后门。 |

例如，某主流开源框架的早期版本曾存在严重的逻辑缺陷，用户仅需将模型名称中的连字符去除（如将gpt-5.5改为gpt5.5），即可绕过计费系统实现“0扣费无限使用”，导致中转站运营者利益受损。（注：该漏洞目前已被社区修复）。

![图16.png](https://mmbiz.qpic.cn/sz_mmbiz_png/NicWxqLvw6OpXDQiaEOmAmXyoUHpxaJ9hR2XeMDCIibV9HLHqGGXVMEAN47LCW1XYQewicYmxGkZKXg6oichbic1ovRXWA2SB3ySgibgSOTcGptv0o/640?wx_fmt=png&from=appmsg)图16 github上的issue

此外，部分平台为了推广，设置了新用户注册则赠送一定免费额度，但是该机制可能会存在缺陷，例如某中转站曾被利用无限注册虚拟钱包套取免费算力。

**0****4**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/NicWxqLvw6OrMYHMyAbn2FCaZia63D3GcibEQkEMx50psyPf501xG1Pa6ibk7yiaBcoIMIwRib398FHcqPFoHAXibcmoBkWn0u5zo4iane65iaNoXkTg/640?wx_fmt=png&from=appmsg)

**天翼安全网络反诈中心：从流量中“挖出”高危黑灰产线索**

依托天翼安全网络反诈中心的大网数据与AI情报能力，我们对技术社区中被 “避雷”的具有涉诈倾向中转站进行了深度关联分析。

1. 从涉诈倾向站点到关联站点发现

研究团队以上述涉及模型欺诈、倍率欺诈的具有涉诈倾向的中转站为样本，进行分析研究。研究团队通过同IP拓线发现，具有模型欺诈的站点在同一IP上部署了2个相同域名后缀的中转站点；具有倍率欺诈的站点在同IP上还部署了4个域名相同的服务，还发现另一家为同一运营者运营的中转站点。

![图17.png](https://mmbiz.qpic.cn/sz_mmbiz_png/NicWxqLvw6Ord9Uic8tVTnz4TdrlnnswJGB5nl2PvYA6oV4wScD6dAQxzI2qfMSGfPMshEyzSIF1J73paqvJz0lVvMshfNOlGHYt2jQaDnkDY/640?wx_fmt=png&from=appmsg)图17 “模型欺诈”站点同IP上的其他站点

![图18.png](https://mmbiz.qpic.cn/sz_mmbiz_png/NicWxqLvw6Opf3ZnzppFnj6zkKdJDQH3G8y1vBU7s8nSzGSxln1AjNtBwscXkjq9hea8N6kHkNaXGvJj1LBkPnuJyNojNLuXcUcNKKEJrvKI/640?wx_fmt=png&from=appmsg)图18 “倍率欺诈”站点同IP上的其他站点

另一方面，研究团队通过利用三重模型的学习能力，对两个有涉诈倾向的站点进行同框架的挖掘，发现400+同框架的网站。

2. **锁定涉诈倾向站点的潜在受害人**

研究团队通过对两个具有涉诈倾向的站点进行分析发现，这两个站点，三天的时间内分别还有1.8w和1w左右的访问量，这意味着，仍有开发者或AI爱好者在不知情的情况下，面临着模型被替换、资金被虚假扣费的风险。

![图19.png](htt...