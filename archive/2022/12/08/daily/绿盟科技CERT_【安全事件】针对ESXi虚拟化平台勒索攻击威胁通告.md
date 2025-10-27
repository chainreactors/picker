---
title: 【安全事件】针对ESXi虚拟化平台勒索攻击威胁通告
url: https://mp.weixin.qq.com/s?__biz=Mzk0MjE3ODkxNg==&mid=2247487874&idx=1&sn=b4314b968db2be9fa2389c4a2e0af0e2&chksm=c2c64689f5b1cf9f991d112873b3d7b32498a0d875ace9713b25cbd067fd283fa2b83c9baf1b&scene=58&subscene=0#rd
source: 绿盟科技CERT
date: 2022-12-08
fetch_date: 2025-10-04T00:53:54.823547
---

# 【安全事件】针对ESXi虚拟化平台勒索攻击威胁通告

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/VvfsuOanecoNSFGvrFbB5VOmZIzOCiaoicANGKEFt8kAIR2SEsatwYM4tJPwlPGBvkgITzPib5iaA39ZiaoUIvlGibzQ/0?wx_fmt=jpeg)

# 【安全事件】针对ESXi虚拟化平台勒索攻击威胁通告

原创

NS-CERT

绿盟科技CERT

**通告编号:NS-2022-0029**

2022-12-07

|  |  |
| --- | --- |
| **TA****G：** | **RansomHouse、Babuk、横向移动、vCenter、密码重置** |
| **版本：** | **1.0** |

**1**

**事件概述**

绿盟科技CERT团队近期陆续接到多个行业客户反馈遭受勒索病毒攻击，具体表现为企业内网部署的ESXi虚拟化平台遭受攻击，VMware虚拟磁盘等文件后缀被修改为.mario，同时存在勒索信息文件How To Restore Your Files.txt。

![](https://mmbiz.qpic.cn/mmbiz_png/VvfsuOanecoNSFGvrFbB5VOmZIzOCiaoicRmjIreiaQU5VspPY2n4wGfSEZDrc0wQzyduqUiaR20UOovibeDbYTnBGQ/640?wx_fmt=png)

勒索信息文件中包含游戏人物超级马里奥的logo，对应的攻击团伙为RansomHouse，该团伙除了对虚拟机文件进行加密外，还对企业敏感数据进行了窃取。

![](https://mmbiz.qpic.cn/mmbiz_png/VvfsuOanecpmiavg3fbQAu4xTMBUSVRg4lEcIL3nK5icnXKGQLvfm5XxKv04mqrebzwVg12gqicHjRvAqtMR7I73w/640?wx_fmt=png)

该团伙的暗网博客内容与其他勒索病毒家族类似，同样公布了受害企业信息、攻击时间，泄露数据等信息。

![](https://mmbiz.qpic.cn/mmbiz_png/VvfsuOanecoNSFGvrFbB5VOmZIzOCiaoicEcOpebHuohJOWC4VDRer6jgXk4OYruGzoUzwicUCaxn34mQtiaslHRAA/640?wx_fmt=png)

**SEE MORE →**

**2****样本概述**

经分析确认，此次勒索病毒样本为Babuk变种。Babuk又称Babyk，最早出现于2021年初，同时支持对Windows、ESXi及NAS主机进行加密，2021年9月某俄语黑客论坛上泄露了Babuk勒索软件的完整源代码，包括加密程序、解密程序及生成器。

通过对比Babuk源码及mario代码，发现两者代码基本一致，包括生成的勒索信息文件名。

![](https://mmbiz.qpic.cn/mmbiz_png/VvfsuOanecoNSFGvrFbB5VOmZIzOCiaoicl1iagBEEkjqeHoibM73Mwl8dob5FVutVG8C4wPwFLLKXqKRGZQM4IACw/640?wx_fmt=png)

攻击者仅修改了加密后的文件后缀名以及加密的目标文件后缀名列表，增加了对VMware虚拟机打包相关文件后缀（ovf及ova）的支持。

![](https://mmbiz.qpic.cn/mmbiz_png/VvfsuOanecoNSFGvrFbB5VOmZIzOCiaoicJYgysN8YPgSsAjNoRGqqgLeKv8vyyx63MvqLJpag7zbdVmCDhF1OlA/640?wx_fmt=png)

样本加密过程采用非对称密钥算法获得对称密钥，再使用对称密钥算法加密文件，并会对大文件进行分块加密，同时在加密结束后会将密钥内存清零，导致无法在受害主机内存中找到对称密钥痕迹。

![](https://mmbiz.qpic.cn/mmbiz_png/VvfsuOanecoNSFGvrFbB5VOmZIzOCiaoicKLcEmNU33UyNgH7EkAoSqm0ic24xCRVTNoM848nNyicRQiaSTtrCX7NOg/640?wx_fmt=png)

**3****攻击概述**

攻击者首先通过网络钓鱼及水坑攻击获取内部员工PC控制权限，并以此为据点，开始利用AD域相关漏洞获取域控制器权限，并进一步窃取域管理员登录凭证。

随后在域内利用窃取的窃取域管理员凭证，针对目标主机进行横向移动攻击，主要攻击手段为WMI远程命令执行。

![](https://mmbiz.qpic.cn/mmbiz_png/VvfsuOanecoNSFGvrFbB5VOmZIzOCiaoicOZ9mCw5ibH9qL6mnJORvaXibfeQz7icw7c79CPPLl11QHrVRGSV2aC8Pw/640?wx_fmt=png)

同时还会利用微软SysInternals套件中的PsExec工具，以通过本地提权方式获取系统权限。

![](https://mmbiz.qpic.cn/mmbiz_png/VvfsuOanecoNSFGvrFbB5VOmZIzOCiaoicZSuLjplflo6HVSTfuuQXiaYfVGdbhP4pwxMJ1lic3oHibOiantbYicicjKbg/640?wx_fmt=png)

为了躲避相关安全设备监测，攻击者还通过命令行部署了TightVNC软件，以实现后门方式对主机进行远程控制。

![](https://mmbiz.qpic.cn/mmbiz_png/VvfsuOanecoNSFGvrFbB5VOmZIzOCiaoicibIv3aWq58BPNMRz3cvCpHwWVX2tsVkMAKvXu6w4GLg1CgyaSBEIJKA/640?wx_fmt=png)

随后，攻击者通过在IT运维人员主机上窃取的相关凭证，通过内网部署的vCenter重置了ESXi管理员口令。

![](https://mmbiz.qpic.cn/mmbiz_png/VvfsuOanecoNSFGvrFbB5VOmZIzOCiaoicaoCp5wz0G0FocgjFTCp9P61WXW5ic5eiaiaG8Ee2iaU9tE8riafVpEFmD3w/640?wx_fmt=png)

最终，攻击者通过SSH登录ESXi后，上传并执行了其勒索病毒程序。

![](https://mmbiz.qpic.cn/mmbiz_png/VvfsuOanecoNSFGvrFbB5VOmZIzOCiaoicKD5BeknwrOrYjibQ5HuIh3xLj0ZcNnVic7leojkqQsJ5xqerNRZRwITw/640?wx_fmt=png)

除了针对ESXi进行加密破坏外，攻击者还会收集并窃取企业的敏感文件，并通过开源的云存储管理工具Rclone，将数据上传至境外相关网盘。

![](https://mmbiz.qpic.cn/mmbiz_png/VvfsuOanecoNSFGvrFbB5VOmZIzOCiaoicdBYHfrWQvEyDQGzlEoV5giaia2rUKs5SlUppjVzFicHZ0ZC9mxk789Ilg/640?wx_fmt=png)

攻击者在Rclone相关配置文件中，定义了文件上传范围、上传接口、日志信息等参数信息。

![](https://mmbiz.qpic.cn/mmbiz_png/VvfsuOanecoNSFGvrFbB5VOmZIzOCiaoicrrvhcfqAWMndMoue1FdQANyjib53vbMzBsvYvm5Il197D96iabbrQDhA/640?wx_fmt=png)

**4****安全建议**

1、关注VMware虚拟化平台高危漏洞相关情报，评估ESXi、vCenter的安全性及补丁情况；

2、通过配置ACL，在网络层限制对ESXi、vCenter相关管理端口（如：22、443等）的访问；

3、加强对于内部相关安全软件或设备告警的巡检，重点关注横向移动相关攻击；

4、通过网络管理系统或全流量监测系统，对于内部主机的异常流量进行监测告警；

5、对内部员工按岗位进行定向安全意识培训，并定期通过演练方式进行加强与提升；

6、逐步健全数据分级分类规则，加强对于重要业务系统的数据备份与应急演练。

**END**

![](https://mmbiz.qpic.cn/mmbiz_png/qR4ORTNELImFwJM2rh6GKbnrurdFA28jJ8chUPyC1U6aW3jhenqEiaXkmeGVmfOnvAJy8j3My901JQ7emHaicYzA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_jpg/qR4ORTNELImFwJM2rh6GKbnrurdFA28jib7icfic0lJJHh3eLRpIXiaia08KqOSEibBsz64vlOH9aqicu3lmjccEeAFWQ/640?wx_fmt=jpeg)

**声明**

本安全公告仅用来描述可能存在的安全问题，绿盟科技不为此安全公告提供任何保证或承诺。由于传播、利用此安全公告所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，绿盟科技以及安全公告作者不为此承担任何责任。

绿盟科技拥有对此安全公告的修改和解释权。如欲转载或传播此安全公告，必须保证此安全公告的完整性，包括版权声明等全部内容。未经绿盟科技允许，不得任意修改或者增减此安全公告内容，不得以任何方式将其用于商业目的。

![](https://mmbiz.qpic.cn/mmbiz_jpg/qR4ORTNELImFwJM2rh6GKbnrurdFA28jib7icfic0lJJHh3eLRpIXiaia08KqOSEibBsz64vlOH9aqicu3lmjccEeAFWQ/640?wx_fmt=jpeg)

**绿盟科技CERT**∣微信公众号

![](https://mmbiz.qpic.cn/mmbiz_jpg/VvfsuOanecoNSFGvrFbB5VOmZIzOCiaoicpBAOsy4fzcXpR8K5mDZIibo72Z87f68ewFtUia7HdJvlh7oQFqKf22jw/640?wx_fmt=jpeg "绿盟科技CERT公众号.jpg")

![](https://mmbiz.qpic.cn/mmbiz/Hu8hctxHqSW0nSJn8p8OHVEQwHicSwTibFJMBE650AxdzfISoeY8woe2QsgCINIBrccBOOUft2HuU0GsNQWibSG7g/640?wx_fmt=png)

长按识别二维码，关注网络安全威胁信息

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/VvfsuOanecoicvhEy80SjuIeB8aHInNEXXaMDSZpHyeWx4Aer9yLmHDvnjTFT44XkicnIAuF0AiaicLA6ZKFiaXCCicg/0?wx_fmt=png)

绿盟科技CERT

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/VvfsuOanecoicvhEy80SjuIeB8aHInNEXXaMDSZpHyeWx4Aer9yLmHDvnjTFT44XkicnIAuF0AiaicLA6ZKFiaXCCicg/0?wx_fmt=png)

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