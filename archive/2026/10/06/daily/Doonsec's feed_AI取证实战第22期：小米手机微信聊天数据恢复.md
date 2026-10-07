---
title: AI取证实战第22期：小米手机微信聊天数据恢复
url: https://mp.weixin.qq.com/s/AqTBi-1PB660YYv2EegRMA
source: Doonsec's feed
date: 2026-10-06
fetch_date: 2026-10-07T07:53:04.163400
---

# AI取证实战第22期：小米手机微信聊天数据恢复

# AI取证实战第22期：小米手机微信聊天数据恢复

原创

小谢
小谢

小谢取证

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# AI取证实战第22期：小米手机微信聊天数据恢复

本期用一个真实检材，把**手机微信聊天数据恢复**的完整链路跑一遍：从一个小小的"障眼法"压缩包出发，找到 1.6 GB 的完整手机备份，推导出微信数据库的解密密钥，判断**哪些聊天记录被删除或撤回**，并从中恢复出被删掉的内容。整个过程只给 AI 一句自然语言指令，剩下的全自动完成。

关键词：MIUI 本地备份 · SQLCipher · EnMicroMsg.db

## 一、实验环境

先把环境交代清楚，方便大家对着复现。

| 项目 | 配置 |
| --- | --- |
| 检材机型 | 小米 12S Ultra（内部代号 **zeus**） |
| 系统 / 备份 | MIUI V13.0.10.0.SLBCNXM，MIUI 本地备份 **20241023\_142321**（2024-10-23 14:23） |
| 微信版本 | 8.0.53\_2740 |
| 待检文件 | **backup\_wechat.zip** （2,522,472 字节，用户提供） |
| 真实检材 | **20241023\_142321/微信(com.tencent.mm).bak** （1,623,779,393 字节 ≈ 1.6 GB） |
| 操作主机 | Windows 11 + WorkBuddy 桌面端 |
| 大模型 | Deepseek-V4.1-Flash |
| 运行环境 | Python 3.13（cryptography / sqlite3 / struct / re） |
| 分析工具 | 美亚「超级取证大师」（用于结果交叉验证） |

一句话指令就能开跑：把 **backup\_wechat.zip** 拖进对话框，输入「提取手机微信数据，查看删除的微信聊天记录」。

## 二、第一现场：这个压缩包是"障眼法"

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcHgWItGD09uz90UsvmicQbljiaTWxN3yOiaUicLJU0C09PJw9jEurpTCGCcmbQc1aQj4icCWTibpk2FVN13oc0kyZ4u9eotzDGVaQgRE/640?wx_fmt=png&from=appmsg)

▲ 把检材拖进对话框，一句自然语言指令开始

AI 先做的不是解密，而是**看清楚手里拿的是什么**——这一步非常关键。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcGefMtjXXhgdRRibDjFsOCrJCnibIOlpVQsNvMyeVR47HdrRMCxlMlf0tVcTt97Hqhgms8jf73IVIO1fboJhd39euDTdrMT9rfow/640?wx_fmt=png&from=appmsg)

▲ AI 先解包清点条目：19 个条目里没有 EnMicroMsg.db，只有 2 个 xlog 日志

解包结果：**包内只有 19 个条目，没有 EnMicroMsg.db**。里面是 SD 卡上的微信碎片——两个 xlog 日志（TP\_20241022.xlog / TP\_20241023.xlog）、音乐封面默认视频、openim 图标、语音上传配置、用户头像等。

教学点 ①：微信 xlog 离线解不开，别在这儿耗时间

很多人第一反应是"xlog 是明文日志，能直接读出聊天记录"。实际上微信 xlog 的文件头 magic = **0x07**，是 **ECDH（secp256k1）+ zlib** 加密格式，私钥在运行时生成、不落盘，**离线无法解密**。看到 xlog 就应立刻转向去找完整备份，而不是写脚本硬啃。

结论：换检材

这个 zip 只是从手机里抠出来的一个零碎小包，**根本没有聊天数据库**。要完成"查看删除的聊天记录"，必须去找**完整备份**。

顺着压缩包的路径回溯，果然在手机备份目录里找到了真正的主角：**20241023\_142321/微信(com.tencent.mm).bak**，1.6 GB。

## 三、识别 MIUI 本地备份格式，定位 tar 偏移

![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcEP0Xs2iaEv0brPlFPAe1Xu2Tumxh5wWW8sYJDrt4SeibPZ1Fe4UrobxBZPKyohotaU3Q6zb5aW7c2ictbMWgicWOycWbaFic65WczQ/640?wx_fmt=png&from=appmsg)

▲ 确认是 MIUI 本地备份 v2（底层 Android Backup 格式，加密 = none），机型 zeus

读文件头，格式完全清楚：

MIUI BACKUP\n2\ncom.tencent.mm 微信\n-1\n0\n
ANDROID BACKUP\n5\n0\nnone\n    <- compressed=0，即未压缩
<裸 tar 数据>                <- 从偏移 65 开始

教学点 ②：tar 起始偏移是 65，不是 66

MIUI 备份 = **MIUI BACKUP 头** + **ANDROID BACKUP 头** + **裸 tar**，而且 tar **未压缩**（compressed=0），所以可以随机访问、按需提取，不用把 1.6 GB 全解出来。这个偏移量必须实测确认：写错 1 个字节，tar 解析器就会返回 **0 个成员**。另外一个坑是——**Python 的 tarfile 在自定义 fileobj 上迭代会返回 0 个成员**，必须自写 512 字节 tar 头解析器（并支持 GNU long name "L" 与 PAX "x" 两种扩展头）。

用自写的 tar 解析器按需提取，拿到 **EnMicroMsg.db**（22.19 MB，22723 页）、**-wal**（512 KB）、**-shm**，以及全部 shared\_prefs 配置。

## 四、提取关键身份参数

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcHCe1q0gGrW17b6W34NjQPcqlBXlas6lQVqAiaiaK7oia20K0oXlsx8sxrOkmlGQm8Pib10wSO8GHia8q20vMCUdNbDXBexDGdypAibU/640?wx_fmt=png&from=appmsg)

▲ 从配置里拿到 uin、微信号、绑定手机号、昵称，并确认数据库为 SQLCipher 加密

微信数据库的密钥不是随便猜的，它由 **IMEI 和 UIN** 推导。所以先要拿到这两样东西：

| 参数 | 值 | 来源 |
| --- | --- | --- |
| UIN | **82791xxxx** | sp/system\_config\_prefs.xml（default\_uin） |
| 微信号 | wxid\_3oidxxeyxxxx12 | systemInfo.cfg / 配置 |
| 绑定手机号 | 13764xxxxxx | 配置 |
| 昵称 | Leexxx | 配置 |
| 设备标识（IMEI） | 十六进制 413830…5665 → **A80cc43fe5be45fe** | sp/WLOGIN\_DEVICE\_INFO.xml |
| 数据库头 | 随机字节，**无 "SQLite format 3"** → SQLCipher 加密确认 | EnMicroMsg.db 前 16 字节 |
| 账号目录 | **md5("mm" + uin)** = 2c9a8dfe0dd9a1fc6c3f7b3603caxxxx ✔ | 目录名校验 |

两个校验点务必做：① 账号目录名是否等于 **md5("mm" + uin)**，用于确认 uin 没取错；② 数据库前 16 字节是否**不是** "SQLite format 3"，用于确认确实是加密库（这 16 字节正是 SQLCipher 的 salt）。

## 五、推导解密密钥

![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcHZibc8INJY8NmvYu14JvsNiaJlpZdUQw1ic1X48L8zjgdhLBib0GjRuys7CBGbNRQK27j0AxLu5OQO18wrdwVTFqAxe9FdTIqBlKo/640?wx_fmt=png&from=appmsg)

▲ 分级探测后命中密钥，并确认 page1 明文参数

安卓微信 SQLCipher 1.x 的密钥公式：

key = MD5( IMEI  或  "1234567890ABCDEF" + uin )[0:7]

注意这里有两个候选串。本检材实测**真实 IMEI 未被采用**，走的是兜底串 —— 这是 8.0.x 的常见情形，排查时两个候选都要试。

教学点 ③：用"分级探测"代替暴力轮询

一开始按 256000 轮 × 各种参数组合全量试，跑了 4 分钟没输出（还被管道缓冲住了）。改成**分级探测**：第一轮只用"高优先级参数"（PBKDF2-HMAC-**SHA1** / **4000** 轮 / **1024** page\_size / **16** reserve）秒扫候选口令，命中即停，立刻出结果。

命中结果：

**key = MD5("1234567890ABCDEF" + "827914076")[0:7] = 16db1a3**
page1 明文前 5 字节 = **04 00 02 02 10** → page\_size=1024 ✔ / 读写版本 2·2 ✔ / reserved=16 ✔

参数全部对上，说明密钥与加密参数都正确，可以进入全量解密。

## 六、全量解密：注意 WAL 这个坑

SQLCipher 1.x 的完整参数：

* page\_size = **1024**，reserve = **16**（IV 就藏在这 16 字节里）
* KDF = **PBKDF2-HMAC-SHA1 / 4000 轮 / 32 字节**
* 加密算法 = **AES-256-CBC**，**每页独立 IV**，IV 取该页**页尾 16 字节**
* page1 特殊：前 16 字节是明文 salt，密文从偏移 16 开始；其余页密文从偏移 0 开始
* 重建后的 page1 = `"SQLite format 3\0"` + 解密数据 + 16 字节补零

只解主库，**PRAGMA integrity\_check = ok**，message 表 **6829 条**、会话 23 个。

⚠️ 关键坑：WAL 与主库不是同一时刻的快照

截图里 AI 一开始把 WAL 也回放了，得到 message 表 **6786 条**——这个数是**错的**。深挖发现：这个 **-wal** 文件里 500 帧竟然分属 **15 个不同的盐值世代**（f55b6df1 → f55b6df0 → f55b6ded → … → f55b6d3e），只有**前 50 帧**与 WAL 头的 salt 一致。把旧世代的残留帧一起回放，必然导致结构错乱（**2nd reference to page** / **never used**）。

正确做法：**按帧头 salt 筛出"当前代"再决定是否回放**；本次以主库为可信状态（6829 条），WAL 只当"旧页镜像"用于雕刻比对。

## 七、怎么判断"哪些聊天记录被删除了"

这是本题的核心。有四个层次，必须一层层排：

1. 行级删除 → 看 msgId 是否连续

msgId 是 **全局自增**主键。查询 `min/max/count`：本次为 **2 ~ 6830，共 6829 条，连续无缺口** → 说明 **message 表没有任何数据行被 DELETE**。注意：**同一会话内部**的 msgId 跳跃只是其他会话的消息交错，**不是**删除证据，别误判。

2. 会话级删除 → 看 DeletedConversationInfo

该表记录用户"删除过的会话"。本次 2 条：**2186076XXXX@chatroom**、**2342174XXXX@chatroom**（lastSeq 均为 0）。再对照 **BackupMoveTime** 表，发现同样只有这两个群 → 删除动作是**「聊天记录迁移/备份」**触发的。而微信「删除该聊天」**不会删 message 表的数据行**，所以这两个群的 6608 / 143 条记录仍然完整可读。

3. 撤回消息 → 看 type 低 16 位是否为 10002

这是本次真正的"记录级删除痕迹"。微信「撤回」**不是删行，而是 UPDATE 原行**：把 `type` 改写为 **10002**，`content` 字段**保留被撤回消息的原文**，`lvbuffer` 里写入完整撤回报文。所以 msgId 依然连续，但内容可以完整恢复。

4. 雕刻兜底 → 主库全页 + WAL 全帧 + 未分配区 + 同步载荷

把主库 22723 页、WAL 500 帧、各页未分配区、以及 **msgsynchronize.zip** 同步载荷（38 条）全部与活表做差集 → **表外消息 0 条**。这从反面印证了：本检材不存在"删除聊天记录"式的行级删除。

## 八、恢复结果：被删除的 3 条记录

用美亚「超级取证大师」对该检材做交叉验证，结果与本地分析完全一致 —— 与「淼淼 maryxielee」的会话里，**最后 3 条被标记为「恢复」**：

![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcH9xfBO4qWUp0yp4ziav0pd1z19Bu0FDcwbibwYmKJHz719fwmxmMjQoic1epm7uMKD4HRgPLvb0g93tnS8089nrLR145kOicmGFhU/640?wx_fmt=png&from=appmsg)

▲ 被删除的 3 条记录（msgId 6829、6830）

在完整聊天记录里，它们是这样呈现的 —— 红色边框 + 🗑「已删除 · 已恢复」缎带：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcFicCibkMczWem945FLRNPzfNicFfQKkCML0riaeibhOFfzFQLkLicN2B3UUvpicryePwCZfU71zYIXTe8ibZrUiaT4TWcia49ToqMxLC9O0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcEgtjDHaxcWNvzfI5Hjdh16a0Sty8XF6g4nGvcicUyFGs8n47ZwEdLjiaJ7g4ia5MyMZOj2qnMtQia3A1Px5N3Y1ghibibT6SiblO3Mb0/640?wx_fmt=png&from=appmsg)

▲ 红色边框 + 缎带 = 被删除、经恢复取得的记录；其余为正常在库记录

![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcHWkkhwtTloLnUuhJfeDReR6ribg4ePBQve6HIGQck2OdISfENcjXcUhvGfbBkJHWxdicfwFQpQ0f8N3BHGWjMnqSg4gEMmw1mp8/640?wx_fmt=png&from=appmsg)

▲ 美亚超级取证大师的恢复结果（与本地分析互相印证）

本地库里的硬证据

为什么能确定这 3 条是"被删除/撤回"的？逐项核验如下：

* **msgId 6830 的 type = 268445458**

  ，低 16 位 = **10002** —— 微信「撤回消息」系统提示类型；
* 该行 `content` 仍保留**被撤回消息的原文「哦，好的」**；
* 该行 `lvbuffer` 里是完整撤回报文：
  `<sysmsg type="invokeMessage"><invokeMessage><text><![CDATA[你撤回了一条消息]]></text><timestamp><![CDATA[1729664517465]]></timestamp>…`
  其中 timestamp = **2024-10-23 14:21:57**，与取证软件显示时间**分秒一致**；
* 该行 `msgSeq = NULL`、`status = 2`，是全库**唯一**一条没有会话序号的消息（本地生成、未上云），符合撤回后重建的特征；
* msgId 6829 的 `msgSeq = 869986331`，是**全库最大**的会话序号，即该被删除会话中最后一条到达的文本消息。

一句话记住

「撤回」不是删行，是把 type 改成 **10002**（UPDATE）。所以"msgId 连续无缺口"和"存在被删除的记录"这两件事可以同时成立——这正是本题最容易判错的地方。

## 九、顺手的收获：内部文件.zip → AeroX-900

会话里有一条文件消息「内部文件.zip」。顺着它往下挖，还能再拿一层证据：

| 项目 | 内容 |
| --- | --- |
| 文件路径 | r/MicroMsg/2c9a8dfe…/attachment/内部文件.zip |
| 文件大小 | 12 479 字节（与消息 **<totallen>12479</totallen>** 完全一致） |
| MD5 | 5a9f7b2bed389f0333113d10e8997afd（与消息 **<md5>** 完全一致 ✔） |
| 加密方式 | WinZip AES-256（method=99） |
| 包内文件 | 这是一个重要文件.docx（12 253 字节） |
| 口令 | **20001027** （爆破 177 721 个生日候选后命中，HMAC 校验通过） |
| 文件正文 | 恭喜你，找到这个重要文件 / 公司即将发布的新产品型号：**AeroX-900** |

教学点 ④：WinZip AES 爆破要先验校验值、再验 HMAC

WinZip AES 的结构是 **salt(16) + 口令校验(2) + AES-CTR 密文 + HMAC-SHA1 前 10 字节**，密钥派...