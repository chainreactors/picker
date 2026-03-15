---
title: “银狐”盯上“小龙虾” | 针对 OpenClaw 热点流量的工业化钓鱼活动
url: https://mp.weixin.qq.com/s/-w61FK3wEHAzy7CI-1me3g
source: Doonsec's feed
date: 2026-03-14
fetch_date: 2026-03-15T04:31:13.109083
---

# “银狐”盯上“小龙虾” | 针对 OpenClaw 热点流量的工业化钓鱼活动

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/jHUbrwW0VwVaUBufexUZtay3j5CSqNgDnRCJnyDnYuJsVdOgcxfNNduZ9WfC66bQDLcZhw3jhiaDE8GDctImpuZXJJKhQGcLZLIic3pMwf464/0?wx_fmt=jpeg)

# “银狐”盯上“小龙虾” | 针对 OpenClaw 热点流量的工业化钓鱼活动

腾讯安全威胁情报
腾讯安全威胁情报

腾讯安全威胁情报中心

![]()

在小说阅读器中沉浸阅读

2026 年春，OpenClaw （龙虾） 个人 AI 助理的持续火爆，黑灰产团伙银狐迅速嗅到了流量的血腥味，一场针对“养龙虾”用户的 SEO 投毒行动正悄然展开。

近日，腾讯安全威胁情报团队捕获了一批极具欺骗性的投毒域名，它们精准地切中了用户对“官方、稳定、中文版”的心理诱导：

* • **典型诱导站点 A**：https://ai-openclaw.com[.]cn/
  ![https://ai-openclaw.com.cn/](https://mmbiz.qpic.cn/sz_mmbiz_png/jHUbrwW0VwVGyg3EZRZAqX6M3A7maJicjwEushHfAQczsHIPYW2hgTPysmJlKTFVic9bYZultTicVujWJDXK48ib3S0dksGErKt8qzkaFkE1a9I/640?wx_fmt=png&from=appmsg)
* • **典型诱导站点 B**：https://www.web-openclaw.com[.]cn/
  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/jHUbrwW0VwUFpIVtm8T7o0w3QBREKYCbPk8J3mXHwiaxvBZLl5XKICNbkb1LyvU0mBdRpvjKnBkwq92RGlic2xa56Q4KRHAEHaj99DEA5Q0sw/640?wx_fmt=png&from=appmsg)
* • **典型诱导站点 C**：https://openclaw-cn.hl[.]cn/index.html
  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/jHUbrwW0VwVAaYibeJK9j3UFDDNu59Pmje4nx0mBHegcrgyiadUzYbz8fiadq5MOBxouOxbwJth7U5cn0Hic1UHkDXRpiaib1CNtuur18xsEKtKX0/640?wx_fmt=png&from=appmsg)

### 页面层：AI 工厂里的“标准化欺诈”

这批钓鱼网站呈现出高度一致的“AI 生成风格”。通过对 HTML 结构的深度扫描，我们发现了大量大模型辅助思考时留下的“残留注释”：那些人类程序员看起来啰嗦重复的注释，以及大模型特有的标准化冗余代码。
![](https://mmbiz.qpic.cn/mmbiz_png/jHUbrwW0VwWkMlP9IjtOcJ46k5dKoIr49AwgOmqjLSjWibCw2SHyibCEEN5PT7qNa5INScVBBJspkZibXfDsYOhUOypAd1SkUdDiaBCguibJPCiaM/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/jHUbrwW0VwVp7KQ7W3WSwxEq1XEJHxduOgeSNr1iar83HRpHrehaGqlJpHpJrZvrwKjicLcQ0Z0w4SPmAaocqLMX0lDXfhjh4Z4kucy4MfBhc/640?wx_fmt=png&from=appmsg)

这意味着银狐团伙已经完成了其内部工具链的 AI 化升级。他们不再依赖昂贵的人工设计，而是通过大模型批量生成热点话题页面，将钓鱼成本降至低点。配合 `.com.cn` 这种带有天然公信力的后缀，配合站点的seo优化，他们正将广撒网的策略运用在广大ai工具用户。

### 样本层：开源工具的“提线木偶化”

在最新的攻击样本中，该团伙展示了一种极高段位的多重白加黑战术。

他们精心挑选了高信誉的开源二进制工具——如 `hpatchz`（HDiffPatch 项目的补丁工具）——作为其恶意行为的载体。以 EXE 文件 `e58beb4c5dba3c14a6627027ac03e30b` 为例，其原始身份本是由库珀（Kuro）游戏项目编译的合法工具，但在银狐手中，它被 Patch 成了精密的加载器。

**核心手法：改写导入表与函数随机化**
攻击者对合法程序进行了深度改写，通过 Patch 修改其导入表，将原本调用系统模块 `kernel32.dll` 的函数名全部进行了**随机化篡改**。这些虚假的函数调用被重定向至恶意模块 `HLjjBgqULl.8` (MD5: `d01848170c92af6c9ad07b97489f11b3`)。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/jHUbrwW0VwWws3KZZNPRYxXd7vvYSz19CqjcjTAWgT8ehJSGwGrokdw0KPhBH5IicWeLn1I0YvXQrn4IAHjHziaZIZhib8FGo3jTC2MBbD7ZFc/640?wx_fmt=png&from=appmsg)

这种做法对抗成本极高：

1. 1. **规避特征检测**：由于导入函数名被随机化，传统的基于 API 签名匹配的防护系统会彻底失灵。
2. 2. **劫持清白身份**：攻击者利用开源工具的“白名单”身份，在 `DllEntryPoint` 入口点执行恶意代码，构造出一种近似原文件的加载环境。
3. 3. **代码虚拟化对抗**：恶意 DLL 内部使用了严苛的代码虚拟化保护，导致静态反编译工具无法还原出有意义的控制流，令分析者陷入“逻辑黑洞”。

这种“寄生”于开源生态的手法，标志着该团伙在规避沙箱监测和反查杀层面已日臻成熟。欲了解该类样本演进的完整脉络，推荐往期的系列文章：[银狐情报共享第3期｜银狐软硬兼施，硬刚百款安全软件外，悄悄藏身杀软信任区](https://mp.weixin.qq.com/s?__biz=MzI5ODk3OTM1Ng==&mid=2247510749&idx=1&sn=380a24de9de0c991e7cf7feb321dee18&scene=21#wechat_redirect)。

### 拓线分析：九百个虚假锚点的工业化扩张

通过对基础设施的深度溯源，我们发现了一个规模惊人的资产池：

* • **关键资产统计**：

+ • **关联域名总数**：963 个
+ • **核心控制枢纽**：`hudada265@gmail.com`（关联 129 个域名）、`yaarluq55342@outlook.com`（关联 834 个域名）
+ • **程式化命名逻辑**：
     攻击者采用了高度标准化的 `{前缀}-{品牌}-{后缀}` 模式。

1. 1. **伪造地理可信度**：使用 `cc-*`、`cn-*`、`cnzh-*`、`zhcn-*`（合计 69 个）。这些前缀旨在通过“中国/中文”的暗示，让用户误以为是品牌在华的官方镜像站。
2. 2. **伪装分发入口**：使用 `apps-*`、`pc-*`、`wap-*`。模拟官方的移动应用中心或桌面端下载专区。
3. 3. **视觉与拼写错觉**：刻意利用 `sogou`/`sougou`、`chrome`/`chrom`/`goog` 等拼写变体。这种“视线残留”欺诈在快节奏的搜索引擎点击中极难被肉眼识别。

| 模式类型 | 示例域名 | 典型特征 |
| --- | --- | --- |
| **地域标识型** | `cc-google.com.cn` , `cn-wps.com.cn` | 增强“本土官方”假象 |
| **平台标识型** | `apps-wps.com.cn` , `pc-google.com.cn` | 诱导软件下载行为 |
| **拼写变体型** | `sougou-shu.com.cn` , `goog-chrome.com.cn` | 规避关键词检测 |
| **混淆字符型** | `aoe-google.com.cn` , `safew-go.com.cn` | 模糊攻击意图 |

银狐的仿冒网站目标选择主要聚焦于高流量、高办公依赖度的互联网基础设施。其仿冒目标分布如下：

| 目标品牌 | 占比 | 攻击战术特征 |
| --- | --- | --- |
| **某国外办公套件** (315+126) | **45.8%** | 针对跨境办公、开发者群体 |
| **某国内办公套件** (143) | **14.8%** | 渗透国产办公生态，利用用户对常用生产力工具的低警惕性 |
| **xx输入法** (73) | **7.6%** | 典型的“静默渗透”，输入法作为底层权限极高的软件，是绝佳的窃密跳板 |
| **其他** (291) | 30.3% | 涵盖 热门通讯软件、浏览器 等，以及本次行动的核心——OpenClaw |

### 结语

中国互联网正在经历一场“龙虾狂热”。从大厂抢滩到地方政府加码，所有人都在试图驯服这只代表着通用智能的“龙虾”，将其转化为生产力的增量。然而，在这场被媒体戏称为“龙虾盛宴”的狂欢背后，关于信任的博弈正在暗处角力。银狐团伙对热点的捕捉从不迟到。他们利用 AI 批量生产出的伪装站，不再是拙劣的模仿，而是对用户信任心理的精准解剖。

**针对OpenClaw安全风险，腾讯推出多场景安全防护矩阵：**

**本地个人：**

> 腾讯电脑管家18.0版本为C端用户提供「龙虾管家-AI安全沙箱」，可实现“隔离运行、全程防护、行为可溯”，将“龙虾”放到“安全隔离房”里。

**本地企业：**

> 腾讯iOA为B端企业推出办公网安全方案，管控安装非法插件（Skills）、阻断非法访问、拦截数据窃取、限制违规外发，为企业构建全生命周期的安全防御。

**云端部署**：

> Lighthouse 与腾讯云 ClawPro 自带云端物理防爆箱：环境隔离、最小化端口放行、一键快照回滚
> AI Agent安全中心对 AI Agent 部署情况、Agent 行为、异常指令以及 skills 风险进行全面管理与防护
> Agent Runtime 提供 VM 级强隔离、网络隔离、文件隔离、零凭证访问等能力，支持数十万实例并发

**Skills安全**：

> EdgeOne ClawScan 一句话即可让龙虾自己安装，自动 “体检” 并输出报告
> HaS Anonymizer 隐私保护，支持文本 / 图片信息扫描、脱敏和还原
>
> 威胁情报中心 Skills安全检测，构建覆盖互联网威胁发现与未知样本检测的全方面防护能力

![](https://mmbiz.qpic.cn/mmbiz_jpg/jHUbrwW0VwXcdoyCTDLiaY8n4lL85KWGofq03Mac60k4F9J3MReqqmfmdDp7XaoIdoNhdO7iayUiaExD687cxFxZA3uafRv8lVOcVNcV9KKUws/640?wx_fmt=jpeg&from=appmsg)

腾讯将持续跟进AI时代面临的新型威胁态势，为拥抱AI的每位用户保驾护航。

腾讯云安全威胁情报 Skill 安全守护计划正式发布，更多内容可查阅往期推送：👉 [腾讯云安全威胁情报SKill安全守护计划发布](https://mp.weixin.qq.com/s?__biz=MzI5ODk3OTM1Ng==&mid=2247511088&idx=1&sn=652370ddb00c4d2a2e075c3b3635f564&scene=21#wechat_redirect)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/6AoQM3RKCWUu1j1TYiaYRU8wWVGpaHhqaEDCiah9eDwNn00ncbMsWBQwBbd41N9WNYEvp7neMHMksDS9dScCZ2aQ/0?wx_fmt=png)

腾讯安全威胁情报中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6AoQM3RKCWUu1j1TYiaYRU8wWVGpaHhqaEDCiah9eDwNn00ncbMsWBQwBbd41N9WNYEvp7neMHMksDS9dScCZ2aQ/0?wx_fmt=png)

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