---
title: 黑客利用OrBit Rootkit窃取Linux系统SSH与Sudo凭证
url: https://mp.weixin.qq.com/s/90KTh-M2nElYmocKULWtoA
source: Doonsec's feed
date: 2026-05-16
fetch_date: 2026-05-17T05:44:01.720095
---

# 黑客利用OrBit Rootkit窃取Linux系统SSH与Sudo凭证

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WibvcdjxgJnvicN8sMcGCBbgjqxCzQ17tbu1ECVOl71xcW18LqrrFjicrial8kITn8QNjBE422opw6uHPj7rK5FcdIAgUUsq0GWAibWX9GrhfTP8/0?wx_fmt=jpeg)

# 黑客利用OrBit Rootkit窃取Linux系统SSH与Sudo凭证

网安百色

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/WibvcdjxgJnvAgruzKfAy6pxKIsCZKDic5Liady7eY9nC3Ie5VDibWaE77ghJ3FN72Du9TlGUCswlHFW3aF0UCARcbiaUGw4Lny8fBsgKavqAEvo/640?wx_fmt=png&from=appmsg)

一种名为OrBit的危险rootkit多年来一直在悄无声息地针对Linux系统，窃取登录凭证并深度隐藏在受感染机器内部，几乎不会触发主流安全工具的警报。

最新研究显示，此前被认为定制开发的威胁，实则是公开可用rootkit的修改版本，正通过多个黑客组织在全球范围内传播。

OrBit通过将自身嵌入Linux系统核心实现运作，挂钩超过四十个基础系统函数，使其几乎完全隐形。一旦入侵机器，它会监听通过SSH和sudo发起的登录尝试，捕获用户名与密码并保存至标准系统扫描无法检测的隐藏目录中。攻击者随后通过秘密SSH后门连接回受控系统，全程无需经互联网发送指令。

Intezer研究人员在提交给《网络安全新闻》(CSN)的报告中指出，OrBit并非原创代码，而是基于2022年12月发布在GitHub上的公开rootkit Medusa构建而成。黑客的工作并非编写新代码，而是配置现有源文件、轮换密码及修改安装路径以维持隐蔽性。

黑客组织利用OrBit rootkit
Intezer分析追踪了2022年至2026年初的十余个样本，通过静态与差异分析发现两条独立构建路径：功能完整的"谱系A"（Lineage A）携带全套攻击工具，而精简版"谱系B"（Lineage B）则移除部分功能以降低痕迹。谱系B在2024年后不再出现，表明攻击者可能已回归主版本。

OrBit以共享库文件形式部署在目标Linux机器上，通过修改动态链接器配置实现持久化，使恶意库自动加载至系统所有进程。在此位置，它拦截文件读取、目录列表及网络连接数据，对管理员和安全工具完全隐形。恶意软件将窃取的凭证和配置数据存储在标准工具无法查看的隐藏目录`/lib/libseconf/`中——该目录因rootkit自身的挂钩机制而不可见。

2025年出现重大能力跃升：新版构建增加了`pam_sm_authenticate`挂钩（一种服务器端认证函数）。早期版本仅能被动收集用户输入的凭证，而此版本可伪造认证结果，使攻击者能随意批准或拒绝受控系统的登录请求。同年还出现了新型双阶段投递链：感染器嵌入投放器，后者解压安装rootkit，并创建cron任务从外部域名获取更新载荷。

多个黑客组织利用此后门
研究最令人警觉的发现是至少三个独立黑客组织正在使用OrBit：

* Mandiant追踪的国家级间谍组织UNC3886，使用特定0xAA加密密钥、专属凭证及与Intezer 2024年谱系A样本完全匹配的安装路径；
* CrowdStrike在2026年全球威胁报告中指出，以"禁运"勒索软件闻名的网络犯罪组织BLOCKADE SPIDER，利用OrBit在VMware虚拟化环境中维持隐蔽访问；
* 2025年观测到的第三起攻击使用与RHOMBUS（2020年首次报告的Linux僵尸网络）关联的相同投放器架构，两者共享解析至俄罗斯基础设施的同一C2域名。

防御建议监控`sshpass.txt`、`.logpam`和`.ports`等固定文件名在异常目录中的共现情况——这些是Medusa构建管道的固定产物，与编译者无关。通过变量密钥解码XOR字符串表并匹配已知明文条目的YARA规则，可捕获该家族任何版本，即使使用新凭证或重命名安装路径。

威胁指标(IoCs)：

表格

| 类型 | 指标 | 说明 |
| --- | --- | --- |
| SHA256 | 40b5127c8cf9d6bec4dbeb61ba766a95c7b2d0cafafcb82ede5a3a679a3e3020 | 2022年OrBit载荷，谱系A |
| SHA256 | ec7462c3f4a87430eb19d16cfd775c173f4ba60d2f43697743db991c3d1c3067 | 2022年OrBit载荷，谱系A |
| SHA256 | f1612924814ac73339f777b48b0de28b716d606e142d4d3f4308ec648e3f56c8 | 2022年投放器 |
| SHA256 | d419a9b17f7b4c23fd4e80a9bce130d2a13c307fccc4bfbc4d49f6b770d06d3b | 2023年载荷，谱系A |
| SHA256 | 296d28eb7b66aa2cbea7d9c2e7dc1ad6ce6f97d44d34139760c38817aec083e7 | 2023年载荷，谱系A |
| SHA256 | 3ba6c174a72e4bf5a10c8aaadab2c4b98702ee2308438e94a5512b69df998d5a | 2023年载荷，谱系B |
| SHA256 | 4203271c1a0c24443b7e85cbf066c9928fcc69934772a431d779017fb85c9d73 | 2023年载荷，谱系B |
| SHA256 | eea274eddd712fe0b4434dbef6a2a92810cb13b8be3deca0571410ee78d37c9f | 2024年载荷，谱系A |
| SHA256 | a61386384173b352e3bd90dcef4c7268a73cd29f6ae343c15b92070b1354a349 | 2024年载荷，谱系A |
| SHA256 | a34299a16cf30dac1096c1d24188c72eed1f9d320b1585fe0de4692472e3d4dc | 2024年载荷，谱系B |
| SHA256 | b1dd18a6a4b0c6e2589312bbec55b392a20a95824ffe630a73c94d24504c553d | 2024年载荷，谱系B |
| SHA256 | 989f7eb4f805591839bcbc321dd44418eb5694d1342e37b7f24126817f10e37e | 2024年载荷（已提取），谱系B |
| SHA256 | 8ea420d9aa341ba23cdea0ac03951bce866c933ba297268bc7db8a01ce8e9b8e | 2024年载荷（静态ELF），谱系A |
| SHA256 | 26082cd36fdaf76ec0d74b7fbf455418c49fbab64b20892a873c415c3bb60675 | 2024年加载器/安装器 |
| SHA256 | 48a68d0555f850c36f7d338b1a42ed1a661043cacf2ba2a4b0a347fac3cb3ee6 | 2024年投放器 |
| SHA256 | fc2e0cb627a00d0e4509bd319271721ea74fb11150847213abe9e8fea060cc8a | 2024年投放器 |
| SHA256 | 8e83cbb2ed12faba9b452ea41291bcebdce08162f64ac9a5f82592df62f47613 | 2025年载荷，谱系A |
| SHA256 | 2b2eeb2271c19e2097a0ef0d90b2b615c20f726590bbfee139403db1dced5b0a | 2025年载荷，谱系A |
| SHA256 | 84828f31d741f92ce4bca98cfc2148ff8cff6663e2908a025b1386dd4953ffef | 2025年载荷（截断版），谱系A |
| SHA256 | 090b15fd8912cab340b22e715d44db079ec641db5e2f92916aa1f2bc9236e03e | 2025年投放器 |
| SHA256 | 64a3ebd3ad3927fc783f6ac020d5a6192e9778fb16b51cceba06e4ee5416adff | 2025年投放器 |
| SHA256 | b85ed15756568b85148c1d432a8920f81e4b21f2bc38f0cf51d06ced619e0e77 | 2025年投放器 |
| SHA256 | d3d204c19d93e5e37697c7f80dd0de9f76a2fb4517ced9cafd7d7d46a6e285ba | 2025年投放器 |
| SHA256 | 73b95b7d1006caf8d3477e4a9a0994eaa469e98b70b8c198a82c4a12c91ad49a | 2025年双阶段感染器 |
| SHA256 | 04c06be0f65d3ead95f3d3dd26fe150270ac8b58890e35515f9317fc7c7723c9 | 2026年载荷，谱系A |
| SHA256 | d7b487d2e840c4546661f497af0195614fc0906c03d187dc39815c811ea5ec3f | 2026年载荷，谱系A |
| SHA256 | b982276458a85cd3dd7c8aa6cb4bbb2d4885b385053f92395a99abbfb0e43784 | 2020年RHOMBUS投放器（共享架构） |
| URL | http://cf0 [.]pw/0 | 2025年cron持久化机制使用的C2域名 |
| IP地址 | 109.95.212[.]253 | C2域名cf0[.]pw当前解析结果，俄罗斯基础设施 |
| IP地址 | 109.95.211[.]141 | 共享相同BANNER\_0\_HASH-IP值的相关基础设施，俄罗斯 |
| 文件路径 | /lib/libseconf/ | 多数OrBit变种使用的主隐藏工作目录 |
| 文件路径 | /lib/libntpVnQE6mk/ | 原始2022年OrBit隐藏工作目录 |
| 文件路径 | /lib/locate/ | UNC3886/MEDUSA 2024集群使用的备用安装路径 |
| 文件名 | sshpass.txt | Medusa构建管道固定凭证存储文件 |
| 文件名 | .logpam | Medusa构建管道固定PAM凭证日志文件 |
| 文件名 | /etc/cron.hourly/0 | 2025年感染器投放的远程载荷下载持久化脚本 |

注：IP地址和域名已刻意脱敏（例如[.]），防止意外解析或超链接。仅可在MISP、VirusTotal或SIEM等受控威胁情报平台内重新启用解析功能。

本公众号所载文章为本公众号原创或根据网络搜索下载编辑整理，文章版权归原作者所有，仅供读者学习、参考，禁止用于商业用途。因转载众多，无法找到真正来源，如标错来源，或对于文中所使用的图片、文字、链接中所包含的软件/资料等，如有侵权，请跟我们联系删除，谢谢！

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/1QIbxKfhZo5lNbibXUkeIxDGJmD2Md5vKicbNtIkdNvibicL87FjAOqGicuxcgBuRjjolLcGDOnfhMdykXibWuH6DV1g/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&randomid=p6hk1x4r&tp=webp#imgIndex=1)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1QIbxKfhZo6T5IuE1hib7qvAtbaaUZ8tt2fviaDoictibySdn9ibPOF34VZoLwMDYQWCnQGouyMttnhZib6G8fddDqNw/0?wx_fmt=png)

网安百色

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1QIbxKfhZo6T5IuE1hib7qvAtbaaUZ8tt2fviaDoictibySdn9ibPOF34VZoLwMDYQWCnQGouyMttnhZib6G8fddDqNw/0?wx_fmt=png)

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