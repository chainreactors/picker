---
title: \"龙笛行动\" - 常州大学2026年《国家学生体质健康标准》测试通知最终版.zip
url: https://mp.weixin.qq.com/s/WDY6CVD_QMCtPDQJBg3K4A
source: Doonsec's feed
date: 2026-08-19
fetch_date: 2026-08-20T02:51:56.272303
---

# \"龙笛行动\" - 常州大学2026年《国家学生体质健康标准》测试通知最终版.zip

# "龙笛行动" - 常州大学2026年《国家学生体质健康标准》测试通知最终版.zip

Ots安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**威胁简报**

**恶意软件**

**漏洞攻击**

![](https://mmbiz.qpic.cn/mmbiz_png/zNsFJyIuL0HoCWUR1WMW9fwZVRXXqzGP2dS6eS1oGsGOe6ZkTeqsD3rHFhZEKWWJiaicEzbpYpWhoUUDZU3p3YI42gu5Diazl9rqJG0jjTsicys/640?wx_fmt=png&from=appmsg)

在我国的高校校园里，每年的《国家学生体质健康标准》测试（简称“体测”）是每一位学子都无法绕过的“大考”。这不仅关乎学分，更直接挂钩毕业资格。正是利用这种高度的合规压力与紧迫感，一支隐秘的境外威胁力量悄然吹响了名为“龙笛”的攻击号角。

近期，安全研究机构披露了一场代号为“龙笛行动”（Operation Dragon Whistle）的定向攻击活动。该行动由被追踪为 UNG0002 的威胁组织发起，其目标直指我国学术界，特别是针对常州大学等高校的师生群体。这不仅仅是一次简单的钓鱼攻击，更是一场融合了心理博弈、供应链滥用与深度隐蔽技术的协同作战。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zNsFJyIuL0EtvjnHSK7y5pRqJJwaiaRgkicaibFicKc8N2JZxofFbzMTYMsvKX4hzbsnhW4q9nZ9Jk4WclczfsSu9REowRDfGpDVNu04vRhoM5I/640?wx_fmt=png&from=appmsg)

## 一、 心理战术的极致：为什么“体测通知”防不胜防？

黑客深谙“攻心为上”的道理。在“龙笛行动”中，攻击者并没有使用常见的“工资补贴”或“账号异常”等泛化诱饵，而是精准锁定了一份《常州大学2026年〈国家学生体质健康标准〉测试通知最终版》。

![](https://mmbiz.qpic.cn/mmbiz_png/zNsFJyIuL0HzZBT2nkCibLicL8lB7DCSTq0GDStDwYrxMexXiavZg0bqYaqqUzqv94a0x8u3aricgJbQwxMP5ZNRhBLYMNypEj8sFIuYIUMDuOc/640?wx_fmt=png&from=appmsg)

这份诱饵的逼真程度令人惊叹。它不仅完全复刻了我国高校行政通知的行文风格，还包含了真实的教职工姓名、直接联系电话、活跃的 QQ 协调群号，甚至盖有极其真实的院校公章。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zNsFJyIuL0HA5VjNHO09agMgapfPyr701OOZpdUQmPgo7uAsVgPxBbTm01odaIibWNpwBudeegdHusXibuZxFqUjgCbtdN1Vypia0NgJe7Our4/640?wx_fmt=png&from=appmsg)

文中详细列出了体测的时间节点、三甲医院证明要求等细节，营造出一种“官方、权威、紧迫”的氛围。对于正处于体测周期内的师生来说，顺手点开这个压缩包几乎是一种本能的行政配合行为。

这种高度定制化的社会工程学攻击，反映出攻击者对我国高校行政文化有着极深的研究，甚至可能具备长期的情报积累或内部知识背景。

## 二、 隐秘的杀招：拆解“套路满满”的感染链条

当我们剥开伪装的画皮，会发现这支“龙笛”的内部构造极其复杂且阴险。攻击者并没有直接投递木马程序，而是设计了一套环环相扣的“降维打击”流程。

攻击的第一步是投递一个看似普通的 ZIP 压缩包。解压后，受害者会看到一个图标为 PDF、但实际后缀为 .lnk 的快捷方式文件1。这是攻击者利用 Windows 默认隐藏已知后缀名功能的经典手段。一旦点击，便触发了后方的连环陷阱。

点击 LNK 文件后，系统会调用一个隐藏在深层文件夹中的 VBS 脚本（chromedo.vbs）。这个脚本执行了高超的“双轨并行”策略：它会迅速弹出一个真实的、合法的体测通知 PDF 文件供受害者阅读，以此打消其疑虑；而与此同时，脚本已经在后台悄悄启动了一个合法的压缩软件——Bandizip.exe1。

这里正是攻击的核心所在：白加黑（DLL 侧加载）技术。黑客利用了合法软件 Bandizip 在启动时会自动加载同目录下 DLL 文件的特性，将恶意的 ark.x64.dll 放置其中1。这种方式能够完美绕过绝大多数基于签名和白名单的杀毒软件，让恶意代码在合法程序的“皮囊”下大摇大摆地运行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zNsFJyIuL0F7eKpuVu55ZAyGzew9mxHs28kTP5EFum99ermWqBPdtXOvicLE0nh79J2lV522e6sLniaNCiaibXbJHQtkRyru0zLwg6db5EN7haU/640?wx_fmt=png&from=appmsg)

## 三、 深度对抗：恶意 DLL 中的反分析黑科技

为了确保攻击的成功率，攻击者在恶意的 ark.x64.dll 中集成了大量针对安全专家的对抗技术。

首先是严苛的环境检测。该 DLL 在执行核心逻辑前，会调用 GetTickCount 等 API 进行时间差检测，以此识别是否运行在沙箱或调试器中。同时，它还会疯狂遍历系统进程，一旦发现 wireshark.exe（抓包工具）、procmon.exe（进程监控）或各种反汇编分析工具，木马会立即选择“自毁”终止运行，不给安全研究员留下一丝痕迹。

![](https://mmbiz.qpic.cn/mmbiz_png/zNsFJyIuL0EyrFFnMex4Z4WEm1wUMCFtCqatRBtF01GCnCLvzPDxqibag7ib759Vcv6RWiaV0H5cGWl7iaEKyCNhGWDhibWC05rWYiaIxgevGQPJ8/640?wx_fmt=png&from=appmsg)

说明：反调试-沙箱规避-1

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zNsFJyIuL0EibakSqGedSBx519eogqwiaJvmia2ictr0afQnicPrXXOb84bEMQquQG5neJBx5MoUwuvdFMYkw5fk9v2iaFKibkvTmcF5t0DJG6j5Do/640?wx_fmt=png&from=appmsg)

说明：反调试-沙箱规避-2

其次是内存级的隐蔽执行。在确认环境安全后，木马会解密并释放一个 SFX 模块，直接在内存中展开并注入 Cobalt Strike Beacon（远控木马）。它还会尝试干扰 Windows 的 AMSI（反恶意软件扫描接口）和 ETW（事件追踪遥测），让操作系统的防御机制彻底变成“睁眼瞎”。这种不落地的执行方式，让传统的硬盘文件扫描完全失效。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zNsFJyIuL0FYdPpfw3yIxIF1ezzc5pP0J5GjbZTUQq5icGUFqfQdbMNK22AicHQiblzHrtMFsC3xE62ogScYKWtX6a9mgKeJbGNicGA2nWBr7rQ/640?wx_fmt=png&from=appmsg)

## 四、 溯源与演进：UNG0002 组织的黑产版图

“龙笛行动”并非孤立事件。通过对威胁情报的深度关联，我们发现发起攻击的 UNG0002 组织（也被部分机构称为 DragonForce）是一个活跃于南亚地区的定向攻击簇。

在 2024 年，该组织曾发起“钴色低语行动”（Operation Cobalt Whisper），主要针对航空、国防等敏感领域。到了 2025 年，他们又发起了“琥珀雾行动”（Operation AmberMist），攻击范围进一步扩大，开始显露出对我国及东南亚地区学术研究机构的浓厚兴趣。

从早期的简单木马投递，到如今在“龙笛行动”中展现出的深度定制化社工与复杂的规避技术，我们可以清晰地看到该组织攻击手段的快速演进。他们正变得越来越专业，对我国特定行业的背景研究也越来越深入。

## 五、 威胁指标（IOCs）与防御建议

为了守护我国学术界的数字安全，各单位网信部门及广大师生应重点排查以下威胁指标。

在文件特征方面，应警惕文件名为“常州大学2026年《国家学生体质健康标准》测试通知最终版.zip”的压缩包，其对应的钓鱼邮件 SHA256 哈希值为 ff892c71475c71eccf3ab3f650d7aea30b61c9dc0c39a89b7f3f434469aa8d8b。

同时，在内网流量监控中，应重点关注指向 adobe-pdfreader[.]b-cdn[.]net 等伪装域名的异常连接。

## 六、 结语

网络安全是一场没有硝烟的持久战。当攻击者开始利用我们最亲近的校园文化作为武器时，唯有保持高度的警惕与专业的技术防护，才能让这支“龙笛”彻底失声。

各位老师和同学，你在日常学习中是否遇到过这种“官方味”十足的诱饵？欢迎在评论区留言讨论。如果你觉得这篇文章有用，请点赞、在看并转发，让更多人看清黑客的真面目！

文章参考：

* https://www.seqrite.com/blog/operation-dragon-whistle-ung002-targets-chinese-academia-via-weaponized-institutional-lure/
* https://advisory.eventussecurity.com/advisory/ung002-group-breaches-academic-sector-by-applying-steganographic-techniques/
* https://thehackernews.com/2025/07/ung0002-group-hits-china-hong-kong.html

**END**

![](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0FRCNZrJoX7zM6wibWxibbfKpyy65d5GFrX5UOiaiavpQ1ZNoibPcs5mg21A95wyGibmSnjfd4puUSNWlU20EaTpDEsZ8w5zbZ9uMJ3g/640?wx_fmt=jpeg&from=appmsg)

公众号内容都来自国外平台-所有文章可通过点击阅读原文到达原文地址或参考地址

排版 编辑 | Ots 小安

采集 翻译 | Ots Ai牛马

公众号 | AnQuan7 (Ots安全)

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/rWGOWg48tadhkzMbpPpSw6NfJHUgsHudwQFGS0EobaB49HVwda7L2eJiaDMvwpakagffpPgepM6gBZzpCncMMHg/0?wx_fmt=png)

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