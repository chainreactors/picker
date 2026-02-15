---
title: 二：创建一个高度可利用的windows教育/训练渗透测试环境|终极可持续升级版黑客Lab（Rust）
url: https://mp.weixin.qq.com/s/Ks0GlVYw62eyyot2bhzKUA
source: Doonsec's feed
date: 2026-02-14
fetch_date: 2026-02-15T04:19:45.450883
---

# 二：创建一个高度可利用的windows教育/训练渗透测试环境|终极可持续升级版黑客Lab（Rust）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icfnkibn16VehdJ7VnYLoUUOicEBux96wKA9QZxnNZSX6N1P1pwsLAO7SjBVhribBichWDMTNJnVs5YLpCBGfEWdm5guS8cRP1hF4iaZqvkCq2UCk/0?wx_fmt=jpeg)

# 二：创建一个高度可利用的windows教育/训练渗透测试环境|终极可持续升级版黑客Lab（Rust）

原创

Esn A
Esn A

Esn技术社区

![]()

在小说阅读器中沉浸阅读

> 本次实验室构建物理系统设备硬件：
>
> 1.RAM 16Gb （地摊货）
>
> 2.CPU i510400F （地摊货）
>
> 3.GPU GTX 1650  4G （地摊货）.
>
> 4.内存 500G （地摊货）
>
> 公众号的内容主要在记录我们喜欢的内容,关于学习任何内容是每个人的选择。我们非专业,因为我们知道C++从认识到熟悉到掌握学习 5-10年的时间,必须拥有绝对的专注和绝对的记忆力。
>
> 导读

![[Zero to Mastery]Rust 编程：完整的开发人员指南 | Rust Programming: The Complete ...](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icfnkibn16Veh1EAuqEySpbd5mibqvw9cTXM6icSibSaiaSabr6YqhrRzyG1YcgXIIECr1U9E7JbRcEtDBcJyicXicQQxAOkc3SRm7oZ1EcM02XCEKU/640?wx_fmt=other&from=appmsg)

|  |
| --- |
| LinK：https://rust-lang.org/zh-CN/tools/install/ |

声明：

禁止用于违法行为,同时如果确定对方需要这些东西的目的是进行违法,请勿与这些人分享技术指导和及时代码。避免给你带来不必要的高额罚款！

![](https://mmbiz.qpic.cn/mmbiz_png/icfnkibn16VeiaPOcicH6s7dEYNhJkaLW2qjbqjrl0Dqxw36xrhFeNLIgeEOvnMxeBicbXkcjnd5hIAJf5rMleiaCOB9JnAPUXGumRJEcUibnSicY2g/640?wx_fmt=png&from=appmsg)

开阅趣闻

{— 实验室的目的是打造一套详细完整的可提供与Ai记忆学习和个人记忆学习和针对性练习的内容|包含windows Ubuntu  安卓和ios的没什么必要。 }

{— 配合最新网络犯罪防治法,让我们在本地训练可尝试各种漏洞和各种方法,}因为网络问题毕竟严重.所以我个人放弃了其他的网络的维护,Ar9re 在昨天进行了删除一些不必要的通讯！目前就单独保留了微软邮箱。

阅读顺序

#黑客实验室

[零：重构黑客实验室windows+Linux的叙述](https://mp.weixin.qq.com/s?__biz=MzU5Njg5NzUzMw==&mid=2247492206&idx=1&sn=24837ec1b1be29ea9b81c27d40a2fc20&scene=21#wechat_redirect)

[一：创建了一个高度可利用的Ubuntu教育/道德黑客渗透测试环境](https://mp.weixin.qq.com/s?__biz=MzU5Njg5NzUzMw==&mid=2247492197&idx=1&sn=dc55225030769818837bb1ca21225c3b&scene=21#wechat_redirect)

|  |
| --- |
| 审视篇\_Ubuntu服务器微调代码和步骤：https://share.weiyun.com/PWFWUSX3  调整到图内参数即可  ![](https://mmbiz.qpic.cn/mmbiz_png/icfnkibn16VegABkWiag2PvTFXSbNyvFU1Uqtz9AAwGhBcmujcmtytR4ssic1HkR8yKUNo2bvibFXWJSmmWxFxeKxiaiaVsoUHN4nWoQbIWia8SRKdw/640?wx_fmt=png&from=appmsg) |

![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/Expression/Expression_61@2x.png) 二：创建一个高度可利用的windows教育/道德黑客渗透测试环境

0x

Windows 变更：

![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/Expression/Expression_84@2x.png)修改格式TxT替换成Md格式或在微云进行分享,完整的配置档案！

[Windows 10-11 虚拟机安装和Pyhton3的安装](https://mp.weixin.qq.com/s?__biz=MzU5Njg5NzUzMw==&mid=2247490954&idx=1&sn=99d3df5b6d2e6aa14d4e026ae92aabdd&scene=21#wechat_redirect)（非服务器版）

[Windows10-11启动内置：SSh](https://mp.weixin.qq.com/s?__biz=MzU5Njg5NzUzMw==&mid=2247489281&idx=3&sn=56f430978e1148bf3bdac7de9b6087c4&scene=21#wechat_redirect)

* 安装系统
* 配置Pyhotn
* 启动SSH

这两篇文记录了如何下载和安装操作系统和Pyhton+开启ssh和远程启动。如你在过程中遇问题可以通过Ai或者是豆包进行解决,提供报错部分复制粘贴根据Ai回复的步骤即可完成。

Windows 服务器Lab从零开始安装的步骤可以选择[Windows 10-11](https://mp.weixin.qq.com/s?__biz=MzU5Njg5NzUzMw==&mid=2247490954&idx=1&sn=99d3df5b6d2e6aa14d4e026ae92aabdd&scene=21#wechat_redirect) 正常安装步骤可以参考本文内容。仅参考VM安装部分即可。如果你在这个地方遇到了问题可以在公众号留言描述你遇到的问题我看到后会进行回复！

警告：

本次创建只允许在虚拟机中进行创建,因为是百分之百的高危险漏洞主机,仅限用于个人实验室或者是Ai助手成长实验室或本地夺旗。主要目的用于安全研究,让人人都可以用得上免费的实验室。

工具：

* VMWare
* windows 10 pro  （win11 对硬件要求过高）

下载windows 10

|  |
| --- |
| 推荐10年匠心地址：https://msdn.itellyou.cn/ |

---

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icfnkibn16Vej7gHTap85IDnnUoNhqJslbt4RC5L326tfyx8lNxdE2ibwRNJgXeEibkyE1kYefRDT7mxDBPzibKCAHKMoJiaMicSicRL52zGiayKj0A4/640?wx_fmt=png&from=appmsg)

安装步骤可以参考本文：0x 部分提供的window10安装设置过程。就一个要求：X64位的 ,ESN社区将会舍去x32的研究,因为没有太大的价值存在浪费时间。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icfnkibn16VeguftOiaxIAIHkxIiccP2BLkoaJWdULuvSzYxrgctvd0YjyUloic5WNkVicMExMiaANcEF0GwBJ5ia9lmWSJheESZicrRZhIJWPSlAnnA/640?wx_fmt=png&from=appmsg)

重点部分：

![](https://mmbiz.qpic.cn/mmbiz_png/icfnkibn16VejUhYqJhActtdl8sqpqeujdmhWmv5Wcc5omNOnQCPM129PmUuFItjicD6uTeQuAxhiaMOiaKGqFNGYlsdocbW6uerL2JgOuKQZkTY/640?wx_fmt=png&from=appmsg)

网络选择：

![](https://mmbiz.qpic.cn/mmbiz_png/icfnkibn16VeiaNUNGxTUGVJcTfpev9RRtDLbwvIV6cib8BoeuajLQjYSo8Makg9Hia7CIvkO9vS9QRGnng4oTWSKZ3mzKq06I4JKLnRZC5HuDjM/640?wx_fmt=png&from=appmsg)

记得选择个人 Pro\_暂时不用选择企业。请保留你的ios镜像文件,用于Ai一键部署实验室备用。

账号：admin

密码：admin123

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icfnkibn16VehzOLmhxDXAVJqicCFgxdJFKIzOWRraoASqBkzeOic85cvOh7uwibEood1sjo08vKFAwaS5ydia9icPp3iaYIZfwrXRHnJkIwNNKBYZE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/icfnkibn16VeiaTl53S4Sibm4IJiciaiaRqIwJXe9cprzdkCH9lrZ7QMkKlcIB35LDgDOhMszEa8yjqw805DhQ2QmB2iaKTmyS0Gt3HECdRS24sAyWk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/icfnkibn16VegOMgtoor0MvSKibyoF1PtaxgtUTPoaLMCL0O4BIv5XBrd2Y8g6cYyZibwRRe0LqlIsgmwsRrPbIGfAVnJklXfUQzj9zENxicooPc/640?wx_fmt=png&from=appmsg)

到这里框架基本上就构建完成了！我们现在需要打开一切可能被利用的端口和内核！同时防火墙进行关闭！ps：需要知道防火墙关闭和防火墙限制于输出。

![](https://mmbiz.qpic.cn/mmbiz_png/icfnkibn16VehrL68PeotED2ekrr36OflW69x4ssvVIbT1w3OfxF8yfJphBtNc8OJu3wa1aXgJfcfkLtTB7u82n6QTSQZIDcyja73OCOPYvuY/640?wx_fmt=png&from=appmsg)

——

如你有多个实验室环境自己配置静态网络,否则会出现远程IP重叠！

——

![](https://mmbiz.qpic.cn/mmbiz_png/icfnkibn16VegzY2ymFcz2kXXG8XVRP9eLLIr9udFwknab3XOMgtvFqGJsOFbqeZbtGSA0WiaAvIgGBeHHaHE8MEXCG34oA9K3DOBBLxsdXMSI/640?wx_fmt=png&from=appmsg)

打开windows PowerShell  （必须管理员身份运行）

```
# ==============================================================================# esn漏洞实验室环境搭建脚本 # 注意：必须使用“管理员权限”运行，否则部分功能可能无法执行# 警告：仅能用于虚拟机安装windows进行使用,并且必须保证自己的实验室属于内网阶段,禁止在任何开放性电脑上使用这个脚本。# ================代码的问题.....................
```

然后列入脚本：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icfnkibn16Veg7VlenIUian9R4aBQPOYPdV6kD8g9SOPqQ66RxVZWz366Sf1lMdVPSOjHEnXFFlcMaLH5ntwqhWJnHqyCd3ibtta0xp9gPYAfWI/640?wx_fmt=png&from=appmsg)

这段PowerShell 脚本的核心行为是在实验室配置真实可入侵环境的部署,并且主动消弱系统安全并制造可被利用条件。

* 关闭Defendre ,关闭防火墙
* 关闭UAC，VBS , nx , Hyper-V
* 启动SMBv1
* 创建弱口令用户
* 打开高危端口
* 设置AlwaysInstallElevated
* 构造可利用服务器路径
* 共享整个C盘

现在我们进行虚拟机快照拍摄, 需要注意：我在配置的时候整个windows 实验室虚拟机均属于内网并且关闭了数据传输。

![](https://mmbiz.qpic.cn/mmbiz_png/icfnkibn16VeiaxicrWicOFX1eDG8KAsBRoAjmE7GzL4v5quBmqWxxU4jl5icvod5NQLibfD0TDpzPRmffbicU4f1TVPGq0cz5PF48ibwZPEHFkoGCPc/640?wx_fmt=png&from=appmsg)

因为属于高危险！所以必须强制在本地安装部署以后再进行考虑 是否允许实验室链接公网。

#黑客实验室

现在我们重启电脑,因为我们设置的内容有部分是需要重启后才能运行。

弱口令账号已生成

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icfnkibn16VegG8a2WsiayJQc0l25XOLhxAtC4jo8PVhVJEB8BKAxpEykicshAnalttpTTfdNY6U1yXicuwPu2P2B2q1iczgH4YZhH4uIlkCnYsOA/640?wx_fmt=png&from=appmsg)

现在我们需要运行脚本：

```
# 启动 SSH 服务（如果存在则启动，忽略错误）Start-Service sshd -ErrorAction SilentlyContinue
```

```
# 验证环境# 查看关键端口是否开启（FTP 21、SSH 22、HTTP 80、SMB 445、RDP 3389）netstat -ano | findstr ":21 :22 :80 :445 :3389"
# 检查是否启用了 SMBv1 协议（EternalBlue 利用依赖此协议）Get-SmbServerConfiguration | Select EnableSMB1Protocol
# 输出实验环境就绪提示信息Write-Host "实验环境已就绪：EternalBlue + 存在漏洞的 FTP + SSH + RDP + 开放共享！" -ForegroundColor Cyan
```

#CVE-2017-0144=2017 年 WannaCry 勒索软件传播的核心漏洞之一

---

到这里我们基本上就已经设置了百分之60,但是因为家庭版和专业版不支持完全通过脚本创建FTP站点。也就是说现在并不能完成自动化创建FTP服务。

|  |
| --- |
| Windows 10 家庭版/专业版虽然能安装 FTP 功能，但无法像 Windows Server 那样完全通过脚本自动创建和管理 FTP 站点，需要借助 IIS 管理界面手动操作。 |

你的动手能力实践：

|  |
| --- |
| 请自己动手打开Ai助手和配合你的脑子进行开启 家庭版和专业版支持完全通过脚本创建和管理FTP站点。我会在下一篇文中嵌入整体的方法。 |

如何打开自己直接丢给Ai 红色文章部分,Ai可以很好的给你说出你当前可以修改的内容。

友情警告：

设置的每一个漏洞都可以通过ai提示处自己完成训练学习,每一个漏洞都可以找到对应的方法,实验室的目的就是配置所有出现过的漏洞和可被利用的内容进行“实践”,红色警告：不要为该漏洞中的任何一个问题而付费！如出现配置问题直接丢给Ai！

现在拍摄一下快照,因为我们要求构建自己的长矛,用于攻略我们自己的本地实验室。

|  |
| --- |
| 后续会出现微调整个实验室的细节,我会在内容中更新出来！  我们的目的是：现代化Ai+红队实验室  我们首推的编码是：Rust+Pyhton  我们持续专注的是C++编码的某个领域而并非是完整的C++    微云：实验室配置代码地址：https://share.weiyun.com/MwDAXAjJ （长久更新） |

配置完成后我根据本文的点赞和完整阅读次数作基数参考,来决定是否推送下一篇实验室文章,因为一篇文章需要3-7天才能构建完成,我杜绝使用Ai的原因是：正在培训自己的Esn AiBot助手！接口都被调用了～～

![](https://mmbiz.qpic.cn/mmbiz_jpg/PwaXL3w2IRaDgaRQG5ujsPrXostCchunyCR5Y0VpBpPTkXATnVMxBwPRnYBKdqgPx7AB433icw5FXez1xp6Nibqg/640?wx_fmt=jpeg&from=appmsg)

我们删除了一些关于赞赏的要求,重新描述一下：

包含：公众号文章赞赏+Discoed助推6个月 金额大于等于200Cny,将会邀请添加最新的私密群组。 请在赞赏后留下你的联系方式！

我们设定助推才能添加私密群的原因很简单：我只希望在这个快节奏的时代有着让自己可以静心交流并增长自己的地方。设定基础的门槛是为了让我们更加舒适地在一起。

关于2026 E.s.n C++是一直以来的专注编码语言学习,C++任何地方都恶心,唯一不恶心的就是C++“绝对的自由”。如果你也想选择C++千万不要盲目的进入C++！你必须拥有<足够坚定>的目的以后才能进行C++编码,否者你就是在浪费你自己的时间。我们都浪费了2-5年的时间去求证一些“自以为是”的概念。#游戏黑客  #黑客逆向  #恶意软件分析 #嵌入式安全 #崩溃编码

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/PwaXL3w2IRbdW3dY1XLuF3qWXIEQCvzWGBaFGLibfRGHs2JDuomUTlU6FRYuHxWDaluyrOwDg...