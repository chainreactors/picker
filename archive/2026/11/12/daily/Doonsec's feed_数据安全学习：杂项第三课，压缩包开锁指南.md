---
title: 数据安全学习：杂项第三课，压缩包开锁指南
url: https://mp.weixin.qq.com/s/opH2Keye0E6PxTcDEfGHlg
source: Doonsec's feed
date: 2026-11-12
fetch_date: 2026-11-13T08:59:18.157622
---

# 数据安全学习：杂项第三课，压缩包开锁指南

# CTF数据安全学习：杂项第三课，压缩包开锁指南

原创

森林之家zbs
森林之家zbs

allby森林之家

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

上一课[CTF数据安全学习：杂项第二课，LSB图片隐写](https://mp.weixin.qq.com/s?__biz=Mzg3NjY2NTYzOQ==&mid=2247486683&idx=1&sn=caabe09b3a0de55fabc41b37a6e7d902&scene=21#wechat_redirect)文末留了个彩蛋：一个 ZIP 设了 6 位纯数字密码，暴力破解最多要试多少次？

现在揭晓答案：那就是100 万次。

从 000000 试到 999999，满打满算有100 万种组合。

听上去是不是还挺安全挺能扛的？

Nonono，其实只要一份纯 Python 手写的解密预检（每秒 4.2 万次）， 24 秒就能够扫完破解了。

如果是专业工具挂上 GPU，这个数还要再快几个数量级。

而我们今天学习的压缩包开锁题，更是 CTF 杂项里的常客～废话不多说，我找了三道题目真实运行输出，一起原汁原味地从头开始学习它。

**【渗透测试与技术学习仅限授权环境与靶场，这是红线】**

![AI意境图：包裹与三把钥匙](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2wf8V0A7uBd9ycrt2ibjjvgNKz0DfEMIOCA2PI5cIhibWymxTYLIWRbFUoYicSbV8fkl2afDLBYdj7RI0ufAiaDFiaPsEAKv9yyphwjoRUDcFByw/640?wx_fmt=jpeg)

## 识锁：ZIP 账本里那个"锁芯"

ZIP 文件开头是每个文件的 Local File Header（本地文件头），末尾有一张 Central Directory（中央目录）当总账，外加一个 EOCD 收尾。

所有"这文件加密没"的秘密，都写在账本的一个字段里——**General Purpose Bit Flag，通用标志位**。

这个标志位有 16 个比特，第 0 位就是加密位：置 1，工具就按"加密包"处理，老老实实问你要密码；置 0，直接开箱。

妙就妙在这：标志位只是个"声明"。它说了加密并不代表真的加密了——密码学上压根没有校验它说真话的机制。伪加密的一切，都从这个"声明没人查"开始。

## 伪加密，一个 bit 撑场子

还是老规矩，先上题目！

![题目A：伪加密挑战](https://mmbiz.qpic.cn/mmbiz_jpg/2wf8V0A7uBcofJt5gWGE0ib7nxIiblPAl5hf604nC2uwUVqEYqg9knYQCTzH2q31ibfyBZ6VkW29j1uZzXWKB3I1XECiaXTY749vFib2RlxoNvg8/640?wx_fmt=jpeg&from=appmsg)

很多人一看到要密码，本能反应就是掏工具开始爆破。但请先慢着，你有没有检查过，这锁是真的吗？

这题是一个完全正常的压缩包，flag.txt，无密码，142 字节。

然后我把 Local File Header（offset 06）和中央目录（offset 08）两处标志位的最低位，改成 1。总共动了两个字节的最后一位，文件大小一个字节都没变。

看真实字节：

![伪加密前后十六进制对比](https://mmbiz.qpic.cn/mmbiz_jpg/2wf8V0A7uBc13QCPrO9sfVThMfB88VWF4zY2bM9uWrjEst0rcflaOy8SicuyIbwPs1rVxHVkAOIFyzrowwSXfYug3icmC0BIumQKbwJLyicicUE/640?wx_fmt=jpeg&from=appmsg)

再用 Python 标准库去读，报错来得理直气壮：

```
RuntimeError: File 'flag.txt' is encrypted, password required for extraction
```

它以为锁上了，其实锁根本不存在——纸糊的。修复也土得掉渣，把那两处 bit0 改回 0，文件原样打开。验收看答案卡：

![答案A：伪加密修复结果](https://mmbiz.qpic.cn/mmbiz_jpg/2wf8V0A7uBduKYOJPgMIhDyxCBNEtgWlL7E8n55OOoP2z3uxzH0NBhFBYQ9m6l4ToB17YUdZGRMicib5U6FxYrHuObYTCOFsTJPxWIjhSNnxM/640?wx_fmt=jpeg&from=appmsg)

142 字节的压缩包，它的全部安全性，就系在一个 bit 的诚实度上。

是不是有点眼熟？**上一课[CTF数据安全学习：杂项第二课，LSB图片隐写](https://mp.weixin.qq.com/s?__biz=Mzg3NjY2NTYzOQ==&mid=2247486683&idx=1&sn=caabe09b3a0de55fabc41b37a6e7d902&scene=21#wechat_redirect)我们把最低位当地板，往里藏东西；这一课出题人把最低位当门面，虚掩一扇门；**

同一个思路，同一个 bit，同一块地基！

## 不解锁掏货：CRC32 爆破

往下看第二题：

![题目B：CRC32挑战](https://mmbiz.qpic.cn/mmbiz_jpg/2wf8V0A7uBdQ9n5GemfeBH2HmOFOYPhD3y11t0cTJib3dOeU2HFOPGpekSYBgzd5uLEaObaJq16DGibGOwrla81gmKk25GIbNtGQxswW3gjxM/640?wx_fmt=jpeg&from=appmsg)

ZIP 账本里每个文件都记着一个 CRC32 校验值——拿它验数据完整性用的。关键是：**这个值不解压就能看到。**

出题人往往这么埋题：压缩包不加密，可里面的文件只有 10 个字节。文件小、内容空间小（比如 flag{4 位数字}），根本不用碰压缩算法——把候选内容逐个算 CRC32，跟账本上的对，对上了就是答案。

真实跑完长这样：

![答案B：CRC32命中结果](https://mmbiz.qpic.cn/mmbiz_jpg/2wf8V0A7uBfzIqH2vmf1EzSlLmcKt17Bs7SxWLKlcsNUnf4eib8j1BIZvMENeCz2kQSgFKTWoTsW54IibUBjr8dT9kYH5fWq3vEU2quJZJlUM/640?wx_fmt=jpeg&from=appmsg)

12.5 毫秒，换成 6 位数字，按本机每秒 228 万次的 CRC32 速率，全程 0.4 秒——**这招压根不吃密码强度，吃的是内容空间大小。**只要答案的"可能取值"少到能穷举，锁再结实都白搭，因为压根没锁。

严谨归严谨，但CRC32 是 32 位校验，理论上不同内容可以同值（碰撞）。

命中之后最好真正解开验证一下，不过短数字空间里，几乎就是一击即中。

## 真加密，以及暴破的门道

ZIP 的传统加密叫 ZipCrypto（PKWARE 传统加密），1990 年代的算法：密码先初始化一串内部密钥（key0、key1、key2，每个 32 位），加密的过程就是密钥流跟明文逐字节异或。

我把这套算法手写了一遍，亲手造了个带密码的压缩包，再让 Python 官方库来解——两头对上证明我造的锁是真锁：

```
[+] 手写 ZipCrypto 加密包: 153 字节, 密码: 8741 [+] 官方库解密结果: flag{R34l_Z1pCr1pt0_L0ck} | 与原文一致: True
```

有了真锁，就能聊真暴破了。工具暴破的头道工序其实很省：只解加密头 12 个字节，看第 12 个字节等不等于内容 CRC 的最高 8 位——不等直接换下一个密码，根本不碰正文。真实跑分：

![本机暴破测速卡](https://mmbiz.qpic.cn/mmbiz_jpg/2wf8V0A7uBdWkjgTbDXHh6icbREiapfzHKlv3KGRTbvMGPFXGuS04rH7Zpryq2W0aI0aQna4ZzwEkcP0ETymUialMJfpDgBibR7NgxKO7bXgXtc/640?wx_fmt=jpeg&from=appmsg)

先说说误报：单字节校验天然有 1/256 的命中率，我扫一万个 4 位数字密码，出来了 40 个候选——所以真实工具都是两步走，预检筛一遍，再对候选做完整解密验证，最后才报真密码。

再说说速率差：预检每秒 4 万次是纯 Python 单进程的成绩，专业工具（John the Ripper、hashcat 这类）上了 GPU，速率再加几个数量级。所以网上那些"8 位纯数字密码撑了 3 天"的传说，在挂 GPU 的字典攻击面前，先掂量掂量密码的成色。

## 不用钥匙的锁：明文攻击

最后一个场景：加密压缩包里有十几个文件，其中一个是 readme.txt、一张图片、或者开源软件的 LICENSE——这些内容你拿得到原件的明文，加上压缩包里的密文，两头一拼：

```
[+] 明文前 5 字节: b'flag{'   密文前 5 字节: 52 00 9d 8b a4 [+] 密钥流前 8 字节（密文 XOR 明文）: 34 6c fc ec df 68 4b 3b
```

密文异或明文，直接吐出密钥流片段——这是我在本机真实算出来的。ZipCrypto 的密钥流由 key0、key1、key2 这串内部密钥滚动生成，Biham 和 Kocher 两位密码学家证明了：**只要凑齐至少 12 字节的连续已知明文，就能反推内部密钥，再一路外推整个密钥流——密码本身？从头到尾没人碰它。**

开源工具 bkcrack 就是这套攻击的实现，使用条件清楚得很：传统 ZipCrypto 加密、攻击目标最好用 Store 方式存（压缩后明文和原文逐字节对齐）、凑够 12 字节以上连续明文。命中之后不只这一个文件，同密码加密的所有文件全部解开。

明文攻击这一招告诉我们一件事：加密系统的强度，从来不只取决于算法和密码，还取决于攻击者手里有多少已知信息。

## 考场工具箱：fcrackzip、John、bkcrack

手写脚本是练习，比赛还得靠工具。按场景给大家分个工：

**看锁识锁**：010 Editor 或 Python 脚本直接翻标志位，伪加密一秒识破——记住口诀：声明加密不算数，看字节才作数。

**暴力破解**：Linux 下 fcrackzip 轻量顺手；通用玩家用 John the Ripper（zip2john 先提取哈希）或 hashcat 挂 GPU；Windows 图形界面党用 ARCHPR，掩码、字典、明文攻击都有按钮。

**明文攻击**：bkcrack 一家独大，能凑出 12 字节已知明文时，优先用它——比暴破优雅太多。

## 手写实现，核心就两行

今天的伪加密修复的机关：

```
buf[lfh_offset + 6] &= 0xFE    # Local File Header 的加密位清零 buf[cdh_offset + 8] &= 0xFE    # 中央目录的加密位清零
```

配上昨天那两行 LSB 的藏与取，你应该已经摸到规律了：所谓骚操作，底层常常就是一两个 bit 的事而已。

**【本文实验均为本地构造的教学靶题，仅用于学习，这是红线】**

**【小彩蛋】**

今日小问题——评论区可以猜猜看：

下面这串东西，你能解开几层？解出来是什么？

```
Wm14aFozdERNR1F6WDBOb05ERnVYekZ6WDBNd2JURnVaMzA9
```

【最后今日封面图给各位送上】

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2wf8V0A7uBdeiaU9HRVDHVKSF9ezu1aDvWicjGxUDZI69ibicROuoamYLwXEL1GGickHx6mUbWmftOWzftvPGGxFJcI4EtqYfZOFQlUEcNibta4MU/640?wx_fmt=jpeg)

预览时标签不可点

修改于

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ZEY5a7YmV0vemdjA6fvqqblGxKWCcN4CTJCB2ujDEQP5r90enPicrtUGtNvOQIl2a61SGXtT8OcClCWGfhwv5DQ/0?wx_fmt=png)

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