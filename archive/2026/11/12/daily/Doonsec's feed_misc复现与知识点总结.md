---
title: misc复现与知识点总结
url: https://mp.weixin.qq.com/s/kI0DZZsZho7ZIIezO0C66Q
source: Doonsec's feed
date: 2026-11-12
fetch_date: 2026-11-13T09:01:46.430298
---

# misc复现与知识点总结

# misc复现与知识点总结

弥生
弥生

三社院信息Sec

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

| 题目 | 考点 |
| --- | --- |
| **bear** | 中文特殊文本编码的识别 |
| **表情包** | 图片元数据隐写（XMP） |
| **whale** | Windows 平台的中文程序，字符串几乎都是 GBK（代码页 936）编码 |
| **神奇的压缩包** | ZIP 伪加密：文件的通用标志位被标记为"已加密"，但数据本身是明文 |
| **是我的Hanser!** | 零宽字符隐写 + base-5 解码／ZIP AES-256 真加密（识别 + 密码使用）／PSD 图层结构，文字图层内容 |
| **上号** | pcap 流量分析 · JPEG 文件尾附加串 · steghide 口令隐写 |

# bear

#### 考点：中文特殊文本编码的**识别**。该类编码属于可逆编码，不是加密，无法暴力破解，只能依靠识别。

## 题目

记事本打开，发现是很怪的文本不认识

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IjQoEYG92cxrnZylbFvWQiaPtMJmNSoV79uqHichIHSpGSXqSK9fgVpMoSdCm7FNaIzz3q8oqhI6tCx4lRUkPGrmaF7pGI3z4FfsTuFUE1sZo/640?wx_fmt=webp&from=appmsg)

### 搜索发现 “熊曰”是**与熊论道**加密

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IjQoEYG92cwm5PicJ68Ktibobn8eIX2ib1Cw88JUF2VFzF7l2amv3SWMc4s2fwtian1O2pNqFWCkwlGDJj3coiciam4Pq6p0HEyU28p5Kaq85ZCNI/640?wx_fmt=webp&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_jpg/IjQoEYG92cxSsJlp48ibHxzAzJzo8uIMKe03K0picCsCDzwoJNg9zBoQZqu2c0bFt2h1ftTQgYovjl0GJ8aUv7U0P3zCgz7ydPOVibvoCqWV1E/640?wx_fmt=webp&from=appmsg)

**核心算法**

```
解密：去"呋" → 整体倒序 → 按 91 字表映射成 0-90 的数字
      → Base91 解码 → raw Deflate 解压 → UTF-8 明文
加密：UTF-8 → Deflate(level 1) → Base91 → 91 字表替换 → 倒序 → 加"呋"
```

#### Misc 里“中文怪文本”这一类的解法固定：**先看前缀和字符集，再查对应工具**。因此，建立一张特征表比理解算法更划算。可以用脚本 decode.py

![](https://mmbiz.qpic.cn/mmbiz_jpg/IjQoEYG92cySgUjnHClQCuqicsU86PE8xVU0dFAS3KKI1TS8WG5wgtpVnE8Zw2ibtIAEY9ohc9zBGt7tMVwPx2ETGqmiaBIdEvW8icpUCjloQaw/640?wx_fmt=webp&from=appmsg)

**Abracadabra 魔曰**用这个工具 粘贴密文、**不带 `熊曰：` 前缀**、无需密码，直接解开得到flag

![](https://mmbiz.qpic.cn/mmbiz_jpg/IjQoEYG92cxAlq0tdSiaeiaGeqlgah5MTtcsJzgdho27HDibp7SRkaL9aiaMlhpibdYjQib6ZYwqsohfegwarI5XGTzgTnBW1SpuBnAcz95WHibft0/640?wx_fmt=webp&from=appmsg)

##### FLAG

```
qsnctf{80038e81-5f67-4085-a70e-77a3fd74cf96}
```

# 表情包

图包题做题命令用exiftool查元数据

```
.\exiftool.exe -a -G1 -r "目标目录" | Select-String "ctf|flag"
```

题目

![](https://mmbiz.qpic.cn/mmbiz_jpg/IjQoEYG92cwdLOEKHrYKwr25NOlRcNZcMgia9W0wyWxpJaoascibia2vNeWusjl7RstAE8BKjtciaia9xjrBEHaCeicokWOkUgAsEOVt9b8K1yIB4/640?wx_fmt=webp&from=appmsg)

#### 先看文件名

25 个文件名形如 `$Y07P$~E{%G%~9MVW2OQ5MK.jpg`，长度均为 23，字符落在 Base91 字母表内，第一反应是“文件名被编码了”。

用 Base91 解码，得到 18 字节：

c8 a8 a5 3e db e2 10 77 43 2e 82 1d 3c 48 d3 b7 f4 11

不是合法 UTF-8，也不是文本，判定为随机数据，**排除文件名这条线**。

#### 图包题的下一步固定是查元数据

```
.\exiftool.exe -a -G1 -r "表情包" | Select-String "qsnctf"
-a 显示所有同名标签，-G1 标注来源组，-r 递归。
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/IjQoEYG92cwO820PUqFnI9e6OZrXXLqfda4WcEqtB0a1yDxfw48BJAF7xdEibD98K0x3q4LGTHJS7ibXcbWZ1VmYu7B0SMZAwEib2HhBjDticmY/640?wx_fmt=webp&from=appmsg)

验证

```
.\exiftool.exe -a -G1 '表情包\R_4NOO%7L{(H@3U22YNUWN3.jpg'
```

```
<dc:creator>
  <rdf:li>qsnctf</rdf:li>
  <rdf:li>qsnctf{5cab6ff8-0684-4adc-95c3-89283607073e}</rdf:li>
</dc:creator>
```

##### FLAG

```
qsnctf{5cab6ff8-0684-4adc-95c3-89283607073e}
```

# whale

直接用记事本打开 ctrl+f 搜索flag直接得到flag，或者直接双击运行，比较快，需要认真看

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IjQoEYG92cwt60g8XSf8ufT80PtCz1LJpMic7C5VCGsmP5exSsy1EhFibzRqKGduGCokQ92Igrxax7mYN1aLbtdk4q0nqL8LtYBpI7EERfia1w/640?wx_fmt=webp&from=appmsg)

##### FLAG

```
flag{鲸鱼带你进入鲸奇世界}
```

# 神奇的压缩包

### 解题过程

**第一种方法.可以用随波逐流，会出现一个伪加密修复的压缩包，里面就是flag**

![](https://mmbiz.qpic.cn/mmbiz_jpg/IjQoEYG92cyTwJOfVRWJSrdfhJTnlkwL45ia3JqSEqkMEYokj5WoLric41TeF1rFQ92tgoMNj612ic1NGBiaYgA5j2kCrzyibahHY5or3I8bib8BI/640?wx_fmt=webp&from=appmsg)

**第二种方法.双击 / 右键解压 `神奇的压缩包.zip`，弹出「输入密码」对话框。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/IjQoEYG92czXAWD0Qx0xZ08ia6CNAU4K8QFZE7lWHKzic6JnicAN8RCHdibh3GiarwxHYA3PDdvvo9oQEibkTXIP4Hib7rpaicNko3sjdSWUULKbXGM/640?wx_fmt=webp&from=appmsg)

先用 010 Editor 打开，看标志位：

```
00000h  50 4B 03 04 14 00 [01 00] 08 00 ...   ← 本地头，标志位 = 0x0001
00796h  50 4B 01 02 3F 00 14 00 [01 00] 08 00 ... ← 中央目录，标志位 = 0x0001
```

两处 bit0 都是 1，软件据此认为文件加密。

![](https://mmbiz.qpic.cn/mmbiz_jpg/IjQoEYG92czGwDeW8bxkycsdic17fv6hxJqhY3SL5sMyB0eFyDahicPk8eahRnT9FfqfhWOYWphoksicNAOiaYZ5VyrDEic6QvUe6xFA9LBd4Zkk/640?wx_fmt=webp&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IjQoEYG92cwJHrgDbyl6riammgicpBr5OByiakicRoQvwUuIkxAR5icC1PG6dxY5D1SSTXN0O5ahBwrNlp4Eicffnz1S18sibPKcYlz9MibvPWQ8iaRk/640?wx_fmt=webp&from=appmsg)

**完整的 PNG 文件头**。

**如果这是真加密（ZipCrypto / AES），解压结果必然是随机字节，绝不可能规整地出现 89 50 4E 47。**

#### **标志位说"我加密了"，数据说"我没加密"——矛盾即结论：伪加密。**

#### 1.要改的地方

**搜 `50 4B 01 02`，往后数 8 个字节。**

```
0x796  50 4B 01 02   ← 签名（4 个字节，固定写法）
0x79A  3F 00         ← 版本号（2 个字节）
0x79C  14 00         ← 版本号（2 个字节）
0x79E  01 00         ← 加密标志（2 个字节）← 就是它
```

4 + 2 + 2 = 8，所以第 8 个字节就是标志位

#### 2.怎么改

1.`Ctrl + G`，输入 `0x79E`，回车，光标就跳过去了

2.光标停在 `01` 上，敲 `0``0`，那格就变成 `00` 了

3.`Ctrl + S` 保存

![](https://mmbiz.qpic.cn/mmbiz_jpg/IjQoEYG92cyCZpeqOsCvb19Yad922P6LW8UkxqyicIyqoAgRGL6eYHWeItIqXPHibhNyaEmCMaa1fYziaNvxGUibZAUnAj2K4E1cjVGqniamLpPI/640?wx_fmt=webp&from=appmsg)

#### 3.验证

关掉 010，重新解压，**不再弹密码框**，得到 `flag.png`。

打开图片，内容即 flag。![](https://mmbiz.qpic.cn/mmbiz_jpg/IjQoEYG92cwq7JR8dia6OzYafmVeEIJEFng0WI6ODRxoibFTQ5O2gYJQFIoa5DicMG6USVwuJG54H6A5IaN7ribFRalpeacDOCvOrqTgHMs13zk/640?wx_fmt=webp&from=appmsg)

##### FLAG

```
qsnctf{b6627d79-1500-47b2-81c1-b9f158968fc5}
```

#### ZIP知识点

一个 ZIP 文件对每个成员保存了两份元数据：

| 名称 | 位置 | 作用 |
| --- | --- | --- |
| **本地文件头** | 数据前面，`PK\x03\x04` 开头 | 流式解压时用 |
| **中央目录** | 文件末尾，`PK\x01\x02` 开头 | 整个包的"目录表"，解压软件**先读它** |

两份头里都有一格 2 字节的 **通用标志位（General Purpose Bit Flag）**

```
bit0 = 1  →  该文件已加密
bit0 = 0  →  未加密
```

#### **伪加密的套路就是把 bit0 置 1，但不真正加密。**

解压软件只读标志位、不验证数据，看到"加密"就弹密码框；而这里根本没有密码可以爆破——因为根本没加密。

#### **一、补充知识点：到底该改哪一处**

伪加密有时会同时置位本地头和中央目录。实测三种改法：

| 改动位置 | Python `zipfile` | Windows `Expand-Archive` |
| --- | --- | --- |
| 只改本地头 `0x06` | ❌ 仍报需要密码 | — |
| **只改中央目录 `0x79E`** | ✅ 成功 | ✅ 成功 |
| 两处都改 | ✅ 成功 | ✅ 成功 |

**原因**：常规解压流程先读中央目录，标志位不对就直接拦下，本地头根本没机会被检查。

**结论**：最小改动是中央目录一处；两处都改更保险，兼容个别会校验本地头的工具。

### 二、常见变体与区分

标志位不一定是 `01 00`

| 值 | 含义 |
| --- | --- |
| `01 00` | 只置 bit0（加密） |
| `09 00` | bit0 + bit3（加密 + 数据描述符），同样按"加密"处理 |

**改法一致**：整格改成 `00 00`。

![](https://mmbiz.qpic.cn/mmbiz_jpg/IjQoEYG92cwG25XF6zEkciayaWRh0n5EZDkL7tjGG4omxCAsY6zKJfQYhef5mZUc9ibRCGzxfTMTD608SQ0COibq2yArE2YJAF1KcZCIstsIFM/640?wx_fmt=webp&from=appmsg)

# 是我的Hanser!

#### 一、解题过程

拿到附件解压后拿到一个zip文件和一个txt文本，txt 看起来是一段普通外文，zip 解压要密码

![](https://mmbiz.qpic.cn/mmbiz_jpg/IjQoEYG92cwQgTzhZiaSiaIPrM8QvfrbRA1nPlJDjVcic56RsStutrUYuTEF7P1jiceXerNILguBds3vCQDibtA4lXfYAZa0ibLQjsou1w6AWk9t8/640?wx_fmt=webp&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_jpg/IjQoEYG92cw87LMRTfcxjWnH3CpweS7ph2rHShk66LzY1bqWVu7NvBG13CQYwlXzapC5plbmB8fHUmQH5q6HWpkibh8P125o6Wv5mMTHzIl8/640?wx_fmt=webp&from=appmsg)

### 第一层: 文本体检 发现零宽字符

```
python textcheck.py 是我的Hanser!.txt
```

输出：

![](https://mmbiz.qpic.cn/mmbiz_jpg/IjQoEYG92cxMW48SicOBecXia3X9X1WNsicgqpdUl3tic6aoEibcl6SxicOR2ZZ3uAV5iao06pIJXN4L51BicicVUJhE4DnVNVdds2NWktJnlW5bjMBg/640?wx_fmt=webp&from=appmsg)

**95 个零宽字符，6 种**——这就是编码用的"字母表"。

##### 手工检测的办法：Word 里打开 → 开始 → 显示/隐藏编辑标记；或在线搜 "zero width character detector" 粘贴全文。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IjQoEYG92cz5FGyg3ry47B2ZECAZYTf1nvRNXhSYRYkviazuibjNHrzeOu9KstpWVBo34WcGuLGfV40dbQAdb0ovetx1eVOfbPI8ITwm9VYAw/640?wx_fmt=webp&from=appmsg)

```
Password is : Hanser2024
```

##### 或者用零宽字符的隐写脚本

```
python zwdecode.py 是我的Hanser!.txt
```

直接输出密码：

![](https://mmbiz.qpic.cn/mmbiz_jpg/IjQoEYG92cwU6bSygyGdyHoMuUG7b2PpMBhG591UHibWsAHHw0XmCXye4fD2bqIWIl2QAcDL2a6d9w4m7UmkkZCHiaNSXd59kVDnv8l1Yzwg4/640?wx_fmt=webp&from=appmsg)

### 2.第二层：判断 ZIP 的加密类型

先看结构，确认是不是伪加密：

```
python misc_scan.py Hanser.zip
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/IjQoEYG92czlkB79GqmibMYolVE6TMN4dRCuGpsibyelws06uuLknztVvDAk9r8ScSpbu8JLBkw1Exicp4FjBmdIl1B2grXdNBBg0BD7CyMNws/640?wx_fmt=webp&from=appmsg)

| 检查项 | 值 | 含义 |
| --- | --- | --- |
| 压缩方法 | **99** | AES 加密（不是普通的 8 = deflate） |
| extra 字段 | `0x9901` = `0200 4145 03` | AE-2 格式，强度 3 = **AES-256** |
| 数据熵 | **7.999** | 密文（伪加密会低很多） |
| CRC | 0 | AES 包不写 CRC |
| 内含文件 | `Hanser.psd` | 16,477,602 字节 |

四个特征齐了 → **真加密**，不是伪加密，只能用密码解。

#### 2.1.解密 ZIP

**7-Zip**

右键 `Hanser.zip` → 7-Zip → 提取到当前位置 → 输入密码 `Hanser2024`。

![](https://m...