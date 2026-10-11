---
title: ZipCracker v2.2.1 发布：--batch 无人值守，一条命令跑完 6 层套娃 ZIP
url: https://mp.weixin.qq.com/s/KhQBzxaKwHgEpNurRWlgyA
source: Doonsec's feed
date: 2026-10-10
fetch_date: 2026-10-11T07:59:33.005384
---

# ZipCracker v2.2.1 发布：--batch 无人值守，一条命令跑完 6 层套娃 ZIP

# ZipCracker v2.2.1 发布：--batch 无人值守，一条命令跑完 6 层套娃 ZIP

原创

asaotomo
asaotomo

Hx0极客圈

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

栏目 · 工具发布

ZipCracker v2.2.1 正式发布
无人值守批量恢复 · 套娃 ZIP 逐层解开

Hx0 战队开源的 ZIP 综合破解与恢复工具，在 10 月 7 日、10 月 9 日连续发布 v2.2.0 与 v2.2.1。前者把嵌套压缩包变成一条 -r 命令，后者加上 --batch 无人值守与短明文 CRC32 直接求解。本文用随包样例实跑一遍，终端输出原样贴出。

· 实测环境：macOS / Python 3.14.5 · 样例来自官方发布包 · 2026-10-10

CTF 里的 ZIP 题，卡人的往往不是密码本身，而是你拿到包时并不知道它属于哪一类：伪加密、真加密短明文、套娃、还是只有几个字节的碎片。ZipCracker 把这条判断链收进一个脚本——先验伪加密，再依次走字典、掩码、CRC32、已知明文，命中后自动解压，遇到嵌套包继续往下钻。这两个版本要解决的是两件事：**短明文不必再靠字典碰运气**，以及**整条链能不能不敲一次回车跑完**。

![](https://mmbiz.qpic.cn/mmbiz_png/PUTQGRQ4GO8Q45x6fVyGjZrYz3LTh98ygCicTUgJPbsUM36w9tDVvSxuRgF9vtegA8jcLfyOicC9EWeagxibSaa0Rw4afSQSTNObQQq8hC2rAw/640?wx_fmt=png&from=appmsg)

01它是什么：一个脚本收掉 ZIP 常见题型

ZipCracker 是 Hx0 战队出品的 ZIP 压缩包综合破解与恢复工具，**只用 Python 标准库**即可运行，最低 Python 3.7，官方推荐 3.10+。Linux / macOS / Windows 三平台一致，pyzipper（AES ZIP）与 bkcrack（加速已知明文恢复）都是可选依赖。

|  |  |  |
| --- | --- | --- |
| 能力 | 对应命令 | 版本状态 |
| **伪加密识别与修复** | 直接跑，无需参数 | 一直可用 |
| **字典爆破** | 默认内置 6072 条 + 1~6 位纯数字 | 一直可用 |
| **自定义字典 / 字典目录** | 传入文件或目录路径 | 一直可用 |
| **掩码爆破** | -m '?uali?s?d?d?d' | 一直可用 |
| **已知明文攻击** | -kpa / --kpa-template | 一直可用 |
| **套娃解压（递归嵌套）** | -r / --recursive | v2.2.0 新增 |
| **短明文 CRC32 恢复** | 1~4 字节自动；5~6 字节加 --crc-candidates | v2.2.1 重写 |
| **无人值守批量恢复** | --batch | v2.2.1 新增 |
| **命中后自动解压** | 默认行为，可用 -o 指定目录 | 一直可用 |

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUTQGRQ4GO9jOVb463V1Jx7jJ3H0WB6UPjPv5BIj25ib5EbT9viaicmkCam0ZDnPamoz5dX6kUCrylhcNj0wGKLKhjelZKKvUZQsk05VqGMba8/640?wx_fmt=png&from=appmsg)

图1 | v2.2.1 的启动横幅——**代码注释里的更新日期是 2026.10.09**，与发布包一致。

02两个版本，各解决了什么

v2.2.0 与 v2.2.1 相隔两天，改动方向不同：一个管「套娃怎么往下钻」，一个管「流程怎么不被打断」。两版都保持了旧命令兼容，升级不需要改脚本。

2.1 v2.2.0（2026-10-07）：套娃解压

加上 -r 之后，当前压缩包完整解压成功才会继续扫描本次产生的嵌套 ZIP，逐层复用同一套字典/掩码设置。这一版的取舍集中在「别把东西弄丢」：

1**只有完整解压成功的中间包才会被清掉**，最外层输入包始终保留；想全留加 --keep-nested-zips。

2**先落地到临时目录并校验，再交付**；同名旧文件先备份成 目录名\_backup\_随机串，合并失败可回滚。

3**每一层落到独立的 nested\_序号\_包名 目录**，避免同名覆盖，也避免上千层链路在 Windows 上触发超长路径。

4**深度、包数量、累计解压体积都有上限**（默认 2048 层 / 4096 包 / 1GiB），触限就保留未处理包，并通过退出码反馈。

2.2 v2.2.1（2026-10-09）：无人值守 + CRC32 重写

这一版的核心是 --batch：把原本需要人工确认的环节改成有预算的自动执行，同时给嵌套层也放开有限度的自动恢复。

|  |  |
| --- | --- |
| 改动项 | 具体行为 |
| **1~4 字节 CRC32** | 用缓存的 CRC32 逆线性变换**直接求解**，每个条目最多 32 步消元，不再枚举字符组合；支持 00、FF 等二进制字节。 |
| **5~6 字节碰撞** | 默认跳过；显式加 --crc-candidates 才分析，**候选另存到单独目录，不计为恢复成功，也不允许清理来源包**。 |
| **口令校验加速** | 已知明文按 64 字节分块比对，尽早排除错误口令；缓存传统加密头用于快速否决。 |
| **批量模式默认策略** | 默认跳过依赖安装提示；超过 1000 亿组合的掩码直接拒绝执行，不会闷头跑下去。 |
| **预算参数** | --crc-max-candidates （默认 100 万次）、--crc-timeout（默认 5 秒）、--template-timeout（默认 60 秒），均只接受正值。 |
| **正确性修复** | 重名条目（加密与明文同名）改为按归档下标选中条目；口令工作线程异常会向上升级并排空队列，不再静默挂起。 |
| **新增样例** | 随包加入 test07.zip：6 个 ZIP、最大深度 3，覆盖弱口令、伪加密、短明文分片、CRC32 碰撞陷阱与明文分支。 |

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUTQGRQ4GOicHW1XpcVfQyFzxnrjJ1iawzMKSt0dDe9ecvEyQzic55FRfk7wmcmQdmFD5wsksEefeps3lfzWfwadic8uXXhwBD5M3TvXZjhI84Y/640?wx_fmt=png&from=appmsg)

图2 | 产品页把三处改动放在最前——**无人值守 --batch、套娃解压、CRC32 恢复**。（图源：hx0.store 产品页）

03实测一：--batch 把整条链跑完，中途不用敲回车

下面这条命令跑的是官方随包样例 test07.zip。它包含 6 个 ZIP：外层走弱口令字典，第 1 层是伪加密，第 2 层明文直接放行，第 3 层分出三个分支——短明文分片、CRC32 碰撞陷阱、明文检查点。

python3 ZipCracker.py test07.zip -r --batch -o test07\_out

![](https://mmbiz.qpic.cn/mmbiz_png/PUTQGRQ4GO9H2vQI8xbbYKia2eU5T3AZ6xXdJdUlncNXcicgPdcsgEicXj4zhMfahNSlkLOLo4expxzVxEwB6UISLDh3rKT8YlAjoquYIqd8CI/640?wx_fmt=png&from=appmsg)

图3 | 一次运行的实际输出——**共处理 5 个嵌套包，最大深度 3**，耗时 0.279 秒，退出码 0，最外层 test07.zip 保留。

整段流程里没有人机交互：伪加密修复失败自动转真加密流程，字典没命中自动转 1~6 位纯数字，短明文分片交给 CRC32 求解，碰撞分支跳过候选枚举改用字典拿到口令。日志把每一层的深度、包名和走向都单独列了一行，排查时能直接对着看。

这条命令的完整输出与退出码见上图。**在交互式环境里，不带 --batch 时脚本会就 CRC32 询问你一句**；重定向输入或加 --batch 后按预算自动决策，适合放进流水线或批量处理。

04实测二：短明文不靠字典，碰撞候选不算答案

4.1 八个 3~4 字节的分片，直接解出完整 flag

传统 ZIP 加密对 1~4 字节的条目，其内容在长度与 CRC32 元数据正确的前提下原像是唯一的。v2.2.1 不再枚举字符组合，而是用缓存的 CRC32 逆线性变换直接求解，每个条目最多 32 步消元。样例里 8 个碎片被逐个还原：

![](https://mmbiz.qpic.cn/mmbiz_png/PUTQGRQ4GO9eGHxMT857WAJVLrwlbTtAdny5O6hfQ1oaUAPCl23ghTjZQsibia0s3RIJAMdcoJBDNZ75S8Qlb310s9EflRXJhnjWBRvGrPzYw/640?wx_fmt=png&from=appmsg)

图4 | 8 个分片分别解出 flag、{bat、ch\_c ……——**全部无歧义恢复后，脚本直接跳过字典攻击**。

4.2 五字节陷阱：找到候选不等于找到答案

5~6 字节存在 CRC32 碰撞：同样的长度、同样的 CRC32，内容可以有多个。样例的 02\_crc\_collision.zip 就是为这一条设计的。默认行为是跳过候选枚举，转回字典，用口令 123456 真正解出内容。

![](https://mmbiz.qpic.cn/mmbiz_png/PUTQGRQ4GO8AVFm3rSUhV143edsUt33W1zMMWWykNvlA3gByasBnhcZQDONicGjeueHZicq4JHkoyribJ5T2UcVnVOIFVODdMib3yYZnv6EPRls/640?wx_fmt=png&from=appmsg)

图5 | 加 --crc-candidates 后仍会分析候选，但**明确标注「可能碰撞，不计为验证成功」**，并把来源包留下继续验证。

把两次运行的结果摆在一起就清楚了：真值是 aRQ\,，候选是 00000。两者同为 5 字节、CRC32 同为 0x4adc54f5，但内容完全不同。这也正是这一版把候选单独落盘、并且**不允许它触发来源包清理**的原因。

![](https://mmbiz.qpic.cn/mmbiz_png/PUTQGRQ4GOibe2icqmmbuIjoHuMCRsoDZy02n6Vqa1BM8tXbzadeXznOSQSADzJmAic0JzKPumTaiafxsdvdick7G9uY2Cyuwc7CXqdVd3RSqSck/640?wx_fmt=png&from=appmsg)

图6 | 运行结束后逐项核对产物：分片拼成 flag，真值与候选分列两行——**命令与输出逐字取自实际终端**。

本文另行独立复算了一遍：zlib.crc32(b'aRQ\\,') 与 zlib.crc32(b'00000') 都等于 0x4adc54f5，长度都是 5。**碰撞确实成立，工具没有把候选当成答案。**

05实测三：套娃、掩码、已知明文、伪加密复验

除 test07 之外，官方样例包里的其余题目也一并跑了一遍。它们分别压在不同能力上，这里只留结论性的输出。

5.1 test06.zip：五层套娃，四种不同路径

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUTQGRQ4GOiccCsEX8LsrgnNCibIxosJZ4xdIr7O0pqtbJh3gGQA5jZQCy4micjjw2974SRajaRicDzZPbYPyeyhXarKUOrlkQ7R1xIO0bg6Zgo/640?wx_fmt=png&from=appmsg)

图7 | 第 3 层是 602B 的数字口令包，字典失败后转 1~6 位纯数字命中 0713——**共处理 4 个嵌套包，最大深度 4，全部完成**。

5.2 test04.zip：掩码爆破 832,000 组合

![](https://mmbiz.qpic.cn/mmbiz_png/PUTQGRQ4GO8nZU1FYhMSn5TLllUzicGr91tYYiauC2PE0ObdnYpNhoPWLyglJQe0W2HibwPd6ichO2icIw8icVwdNaabE7ppRB7zGGczkxaGeJlNk/640?wx_fmt=png&from=appmsg)

图8 | 掩码 ?uali?s?d?d?d 共 83.2 万组合，本机 40 线程、8 秒左右命中 Kali@123。

5.3 test05.zip：已知明文恢复内部密钥后反推口令

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUTQGRQ4GOib44bEic1mH9NibHdlnOrADt6F7LWuicVyEo0Lcg9EbicXCNTVeuVZXxBpO0DkdW14se20c0picTd1mGIFmAMs1H8mgu0RhcCVlx7Dw/640?wx_fmt=png&from=appmsg)

图9 | bkcrack 从 32 字节已知明文恢复出内部密钥，随后用已知明文快速验证出原始口令 123123。

5.4 test01.zip：伪加密只需验一个标志位

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUTQGRQ4GO96x0mPZDa5QTZwibbHDIcSvMyDYebVSr9lxZIOiaC7MY1WonvWSO9pWgNdNvd1LCXtwzQ4yyeiaBI4zBDt80ia4PsPeMGKZleWzxE/640?wx_fmt=png&from=appmsg)

图10 | 加密标志位开着但数据本身没加密——**修复后无需任何字典，直接取出内容**。

06快速上手：五条命令覆盖大部分场景

下载完整 ZIP 包后解压，进入 ZipCracker-v2.2.1 目录即可运行。以下命令与官方 README 一致：

|  |  |
| --- | --- |
| 场景 | 命令 |
| **第一次上手** | python3 ZipCracker.py test01.zip |
| **已知明文攻击** | python3 ZipCracker.py test05.zip -kpa test05\_plain.txt |
| **套娃解压** | python3 ZipCracker.py outer.zip -r |
| **无人值守批量恢复** | python3 ZipCracker.py test07.zip -r --batch -o test07\_out |
| **超大字典（跳过预统计）** | ZIPCRACKER\_SKIP\_DICT\_COUNT=1 python3 ZipCracker.py target.zip huge\_dict.txt |

几个常用环境变量也一并列出：ZIPCRACKER\_SKIP\_DICT\_COUNT=1 跳过超大字典预统计；ZIPCRACKER\_SKIP\_ORIG\_PW\_RECOVERY=1 在已知明文攻击解压后不再反推原始口令；BKCRACK\_JOBS=1 降低 bkcrack 线程数，便于在 Windows 上排障。

07已知边界与适用场景

把限制写清楚，比藏着更省事。以下几处属于设计上的取舍，遇到时不必当成故障：

1**AES ZIP 慢是正常的**，密码校验与解压本身就比传统 ZipCrypto 重。未装 pyzipper 时，真正的 AES 包会保留原包并停止无效遍历，装上再跑即可。

2**已知明文攻击里的「明文」是加密前的数据流**，不一定是解压后的原文件。目标是 ZIP\_DEFLATED 时直接传未压缩原文件可能报 ciphertext is smaller than plaintext，这类情况见随包 docs/KPA\_KNOWN\_PLAINTEXT\_NOTE.md。

3**套娃模式的资源上限只作用于套娃**，原有单包用法不受影响；累计解压量包含失败尝试已写入的字节，删掉中间包不会返还预算。

4**退出码是有意义的**：0 表示请求的处理全部完成，1 表示仍有未恢复、损坏或受资源限制跳过的包，130 是用户中断。批量任务靠它判断成败，不要只看有没有输出。

本工具面向 **CTF / 靶场、自有数据恢复、经授权的安全测试**。请勿用于任何未授权的攻击或非法用途——这句话写进了 README，也是每次使用的前提。

08项目信息与获取

项目在 GitHub 上完全开源，仓库同时提供中英文 README 与完整更新日志。这一版的嵌套 ZIP 能力吸收了 **@halfcity789** 在 PR #19 的贡献，批量模式则来自其 PR #23 的建议，作者署名保留在 Git 历史中。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUTQGRQ4GO9l3HdEaO5FIB7dW75sCibic2W4fs4AjW1dtwoTKsD73ausjkicsvvjH0cnuGYe09QicrTNOic8d5ibyKTrJRmT7OibgQiaibYlq0Dkd9oY/640?wx_fmt=png&from=appmsg)

图11 | 仓库页面——**951 Star / 120 Fork**，最新一次提交是 10 月 9 日的 README 更新，与 v2.2.1 发版同日。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUTQGRQ4GOic5DDp4zKrDs2AUHjj4z2G4anenMyH1TGibADvEaQW5AsbrFiagiaJfpVAZO0VYB7ibtzE1QHMyIa2VmNJrYo0URQmogLaMAQ2wAaE/640?wx_fmt=png&from=appmsg)

图12 | 产品页已同步到 v2.2.1，**发布日期 2026-10-09**，提供 GitHub 与 Gitee 两条下载路径。

🎯 一句话总结

如果只看一件事：**这次新增的 --batch 让 ZipCracker 从「交互式解题脚本」变成了「可以放进流水线的恢复工具」**——短明文由求解替代枚举，5~6 字节碰撞被隔离开，嵌套层也能在预算...