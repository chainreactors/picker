---
title: 疑似 Mysterious Elephant 组织利用 CHM 文件攻击南亚多国
url: https://mp.weixin.qq.com/s?__biz=MzI2MDc2MDA4OA==&mid=2247512794&idx=1&sn=f41a6a721180828aead94ba761b628bb&chksm=ea6645addd11ccbb0bcc218364f0b2f3e69d66f5df9c96a4b8b9804700b05b6423d89376cb98&scene=58&subscene=0#rd
source: 奇安信威胁情报中心
date: 2024-10-17
fetch_date: 2025-10-06T18:51:58.985086
---

# 疑似 Mysterious Elephant 组织利用 CHM 文件攻击南亚多国

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2AqAgxkehicicWdB3CfpvRcibAcOd2IDE6AxmMJBGaxQNTuvEib9GjgpuhqDMMh1f6tc9NYVYELbo8PTVxawLjCYcw/0?wx_fmt=jpeg)

# 疑似 Mysterious Elephant 组织利用 CHM 文件攻击南亚多国

原创

红雨滴团队

奇安信威胁情报中心

团伙背景

Mysterious Elephant（“神秘象”），是由国外安全厂商卡巴斯基在 2023 年第二季度 APT 趋势报告中命名的一个南亚 APT 组织[1]。国内友商曾披露的归属于蔓灵花（Bitter）组织的新后门 ORPCBackdoor 在神秘象的攻击活动中出现[2, 3]，考虑到归因上可能存在的差异，友商也选择对使用 ORPCBackdoor 后门的团伙赋予不同于 Bitter 组织的新编号进行追踪。根据目前的公开信息，Mysterious Elephant 组织与南亚地区多个 APT 组织存在关联，尤其和 Bitter 组织的攻击手法相像。该团伙的攻击目标包括巴基斯坦等国。

事件概述

奇安信威胁情报中心近期发现一批较为特别的 CHM 文件，其中 html 文件的脚本内容十分简单，只是执行一个外部文件（比如下图中的 “UsoCoreService”）。由于 CHM 脚本自身不包含明显的恶意代码，导致这些样本在 VT 上的报毒数很低。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicWdB3CfpvRcibAcOd2IDE6A34dKTic0GDA2z7utrSicZoYIdia3e5ic2OKeLUYUogOz5Q7zvnC0YuOicLQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicWdB3CfpvRcibAcOd2IDE6AiadxFH33icLJhZHLog6byyHBU7nTta7ydSN6s3VVD0zxQ1LAPddV0Wzw/640?wx_fmt=png&from=appmsg)

CHM 样本带有图片诱饵，结合文件名称中的 “.pdf.chm” 双扩展名伪装为 PDF 文件，诱饵内容与巴基斯坦、孟加拉国、缅甸等南亚多国有关，涉及政府机构、军事、外交、经济等行业。在样本关联过程中，我们还发现攻击者模仿红队手法制作的钓鱼样本，诱饵内容表明攻击对象为巴基斯坦国防军事部门。

CHM 执行的外部文件实际是用 C# 编写的后门，后门代码与一篇披露 Bitter 组织攻击武器库的报告[4]涉及的恶意样本相似。这篇报告提到的用于存放攻击武器的服务器（libraofficeonline[.]com）也与 Mysterious Elephant 有关，上面托管的一些攻击武器正是已披露的 Mysterious Elephant 恶意软件[5]（包括 ORPCBackdoor、WalkerShell、DemoTrySpy 等）。

由于南亚地区 APT 组织之间错综复杂的联系和多方安全研究人员不同的追踪视野，目前业界对于是否将 Mysterious Elephant 和 Bitter 区分开来还没有达成一致意见。为避免引入更多分歧，本文基于恶意样本相似性认为这些特殊的 CHM 攻击样本和 C# 后门很可能来自 Mysterious Elephant 组织。

详细分析

CHM 样本信息如下，其中一些样本此前也被其他安全研究人员披露过[6~8]。

|  |  |  |
| --- | --- | --- |
| **MD5** | **文件名** | **诱饵主题** |
| 3df2d899d6d8d827adf2d92c91b3b32b | Upcoming high level visit  from China.pdf.chm | 中国访问巴基斯坦期间可能达成的成果 |
| b38aca4f2d80484d5523f1eada9afe76 | STRATEGIC RESTRAINT REGIME IN SOUTH ASIA.pdf.chm | 巴基斯坦与印度关系 |
| 75ee4f79a3ed4137a918888482ded6a1 | defoffsetpolicy.pdf.chm | 巴基斯坦国防政策 |
| 8e2377022b80cdc51d2c98bbf0c9d313 | Myanmar Ship Clearance OM-2209.pdf.chm | 缅甸海军船只请求驶入孟加拉国水域 |
| 2f7ee7c1c75fbfdc1d079fcc6e325d19 | PM Thanks Letter FAO Xi  an Pak.pdf.chm | 巴基斯坦访问后的感谢信 |
| 19b767974205b66a12a28ccdb69943ed | Talking Points IAEA GC 2024.pdf.chm | 中国-巴基斯坦双边会议要点 |
| aeb0b7e40f12ba093ff523fc124383ae | Bilateral Cooperation  Pakistan China.pdf.chm | 巴基斯坦-中国双边合作 |
| 1645f406ab4e0d54e477330473c76664 | SR ICT 030924.pdf.chm | 巴基斯坦军事 |
| d0030f5411698bb65f1cd281c5d302bc | 26082024\_DSR\_No.pdf.chm | 巴基斯坦伊斯兰堡警察局报告 |
| 232bb5b436c0836370fde34ca7b7138a | A Letter of China Development Bank.pdf.chm | 中国发展银行来信 |
| f26435785dd856ddb1fbcc682547aab0 | CAPSTONE Course  2024.pdf.chm | 孟加拉国政府文件 |
| 68d458d1df36eaf885116a1b6801ab42 | Notice EC10 Power.pdf.chm | 巴基斯坦特别投资促进委员会（SIFC）关于电力部门的会议 |

部分诱饵图片如下所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicWdB3CfpvRcibAcOd2IDE6AlOXSG1fym8wBMxUia9w4I5saJr8xmqFRu9T2N3CwU69dPH1U2Ibk7qA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicWdB3CfpvRcibAcOd2IDE6A5hxBCnCasAsiazBV5IjzDwUqgfQroxQ0JkxftHk6zsDiabOicWKhiaHicxg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicWdB3CfpvRcibAcOd2IDE6A5ELqZKQh5jjl3wTLYEzd5nNiaMXOyFKia4ku1Qxt8G0xRBWGoaMENrFA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicWdB3CfpvRcibAcOd2IDE6A5xcCtowVUDibalJ0g1YGj1TXNibbDAW57OMy3WVd0iaIhUuibZOC1SWeMw/640?wx_fmt=png&from=appmsg)

相关的 C# 后门信息如下：

|  |  |
| --- | --- |
| **MD5** | **文件名** |
| 27ac8eb519679530999e786281e9a578 | FileViewer.exe |
| 115fb536e981c87873b0f35cb0059d93 | STRATEGIC\_RESTRAINT\_REGIME\_DETAILS.exe |
| 4e8e1339f9754d8d2c5f74cb03f44fbb | Guidelines\_on\_Offset\_Program.exe |
| 00f2df1829893caa85f3968961b6e736 | UsoCoreService.exe |
| a59fe2c89b0000a360a8468f2b990c73 | IAEA\_GC\_2024.exe；Bilateral\_Cooperation.exe |
| a3a06d50438681fc9917e22c41bd2cab | SR\_ICT.exe |
| 316e8d798f7db625c207532e2f7a5d38 | Annexure.exe |
| 616b29bd9e20fc032bc54acd5ed8aff0 | RuntimeIndexer.exe |
| ee64e70388e422dd9a620c3d18613268 | RuntimeIndexer.exe |

**钓鱼样本构造**

根据已披露的样本[8, 9]，攻击者通过加密压缩包的方式投递钓鱼样本。CHM 文件和 C# 后门均存在于压缩包中，但 C# 后门设置了文件隐藏属性，导致解压后受害者只能看到 CHM 文件。即使有些具备安全意识的受害者会用杀毒软件扫描 CHM 文件，但由于 CHM 文件本身不携带太多的恶意脚本，很可能被判定为安全，进而使受害者直接打开诱饵 CHM 文件，启动隐藏的 C# 后门。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicWdB3CfpvRcibAcOd2IDE6A2PlhVJfoZewkEsvEU4iaMsCaPrY6iaTf6oTIZqpBrNr6RUpOjY836nMg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicWdB3CfpvRcibAcOd2IDE6Anvk0sICBWbzFSdTLFic2o61xWUFmkibeTIFyYFiayMgs7pnz6lEWVXnFA/640?wx_fmt=png&from=appmsg)

**C# 后门**

C# 后门采用 Task 异步编程，其中一部分经过 ConfuserEx 加壳处理。功能较为简单，主要执行 C2 服务器下发的 cmd 命令，个别后门还支持其他攻击指令。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicWdB3CfpvRcibAcOd2IDE6A1ibjTtJ9MI1oZGRunv1bvUGA9icybVJ2XxIG1ghBVEr92opjjTkhdtBQ/640?wx_fmt=png&from=appmsg)

**获取C2**

C# 后门获取 C2 服务器信息的方式各有不同，包括如下几种。

（1）C2 服务器信息直接硬编码在代码中。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicWdB3CfpvRcibAcOd2IDE6AibC8duiaBFO1NUpEFnydiac57R5HT9NKJj820Hvgcep3mCeuPHYUuTIBQ/640?wx_fmt=png&from=appmsg)

（2）从配置文件中解密。

比如 00f2df1829893caa85f3968961b6e736 和 316e8d798f7db625c207532e2f7a5d38 均是读取同目录下的 SysConfig.enc 文件，再用 AES 解密得到 C2 服务器的信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicWdB3CfpvRcibAcOd2IDE6AGpHF4fR5IQdomvTJOKnUocrNmj1Sbghf3OQ6YffibfkuSUZjAxDLRoQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicWdB3CfpvRcibAcOd2IDE6APjO8GxGVicFocGHicMfJg0hLRTkRn5rpUNKA2IJ6zQzLV3iaGzK4xtCeA/640?wx_fmt=png&from=appmsg)

（3）伪装为看似合法的网络服务访问请求，从远程服务器响应内容中解析。

以 a3a06d50438681fc9917e22c41bd2cab 为例，GetIpInfo 函数请求 “hxxp://easyiplookup.com:5080/main/get\_ip\_data?userId=zqlCYqgp4f&ip=8.8.8.8”

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicWdB3CfpvRcibAcOd2IDE6AqsPPeyRicUh5q5fMqJ8JR4kjm9fk4jR97ticLJZjTKDk97lDTROS7LRA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicWdB3CfpvRcibAcOd2IDE6AY2Bsr3jTbiaTWzJIQHicPUypQ1v99IvYicdGJfjwCic47JJTxZnehhPfrA/640?wx_fmt=png&from=appmsg)

从响应内容的 RequestId 字段提取内容，base64 解码得到 C2 信息 “91.132.92.231:5959”。除了 5959 端口，同一 IP（91.132.92.231）的 6060 端口也被发现作为 C2 信息传递给 C# 后门。通过这种方式，攻击者可以灵活地更改后门实际连接的 C2 服务器 IP 地址和端口。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicWdB3CfpvRcibAcOd2IDE6A8hvxowTBXfLM6zWQT44WskfIJCeqLk8iaQXpykcL3xbNuQYjKR0dqPA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicWdB3CfpvRcibAcOd2IDE6A5sWgtQEOTYT9bsfnq6icCQjJibrnloVJYQ0DzIQCaQcavAzGsu6yTjsQ/640?wx_fmt=png&from=appmsg)

easyiplookup.com 域名的 80 端口看起来运行着 IP 查询服务，网站脚本 custom.js 调用 fetchIpInfo 函数从 ip-api.com 获取访问者的 IP 信息，并显示在页面上。点击网页的 IP 查询按钮 “Lookup” 提交表单后，会访问与后门请求 C2 信息一样的 URL（“hxxp://easyiplookup.com:5080/main/get\_ip\_data”），表明该网站在攻击者的控制之下。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicWdB3CfpvRcibAcOd2IDE6AY7ibT2e140XyVWsBtWRc1tibeKzuEsQTs2sausJicWXnDxLGFJsVWgYQQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicWdB3CfpvRcibAcOd2IDE6AjGce3Hpe1tMRhzwZR4rYKa4icMibfC5mytBJAjFofDLtvoZKWNLfVsibA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicWdB3CfpvRcibAcOd2IDE6ATIJ33G5jQZZbmu0z5vK11GEicmht4EbiaeibibtGGX09KZibk60jp0xtH5Q/640?wx_fmt=png&from=appmsg)

其他用相同方式获取 C2 信息的 C# 后门有：

|  |  |
| --- | --- |
| **MD5** | 4e8e1339f9754d8d2c5f74cb03f44fbb |
| **请求URL** | hxxp://winfreecloud.net:6396/athena/identification?name=f0inqMaHra&addr=6.5.6.2 |
| **获取的C2信息** | 162.252.175.131:8246 |

|  |  |
| --- | --- |
| **MD5** | 115fb536e981c87873b0f35cb0059d93 |
| **请求URL** | hxxp://winfreecloud.net:6396/athena/identification?name=9az1g3qdYp&addr=9.9.9.9 |
| **获取的C2信息** | 46.183.186.208:6060 |

winfreecloud.net 和 easyiplookup.com 均解析到相同的 IP（151.236.9.75 和 84.32.84.32）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicWdB3CfpvRcibAcOd2IDE6AvM5P3fI6hmI4TUKibk1Dh906s2WSYXBPJNVFklAxbib3yficktTItT1nA/640?wx_fmt=png&from=appmsg)

**后门功能**

后门连接 C2 服务器后用感染设备的主机名和用户名作为受害者标识信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicWdB3CfpvRcibAcOd2IDE6A5k2APR6Cz5DZic3Qg5k0ADPycp6icw9Cz8YWOiasQ9wcBHbMrNJg...