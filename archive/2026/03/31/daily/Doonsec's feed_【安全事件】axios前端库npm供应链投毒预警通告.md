---
title: 【安全事件】axios前端库npm供应链投毒预警通告
url: https://mp.weixin.qq.com/s/8XnfHONr9xHj5hmmqApe9A
source: Doonsec's feed
date: 2026-03-31
fetch_date: 2026-04-01T04:45:09.102982
---

# 【安全事件】axios前端库npm供应链投毒预警通告

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/tZgxn6yByvImaohEMK2cSQbaoEgWico0VF6ovCyrwM3ictC8z2FVZ46d1GROl2zexLhdXQLVvbFwM20ibtTWsdibXia2p0Kcsialu0566SPzwqF8Y/0?wx_fmt=jpeg)

# 【安全事件】axios前端库npm供应链投毒预警通告

原创

NS-CERT
NS-CERT

绿盟科技CERT

![]()

在小说阅读器中沉浸阅读

**通告编号:NS-2026-0008**

2026-03-31

|  |  |
| --- | --- |
| **TA****G：** | **axios、npm、供应链攻击** |
| **危害程度：** | **高** |
| **版本：** | **1.0** |

**1**

**事件概述**

3月31日，绿盟科技CERT监测到HTTP客户端库axios的npm仓库遭受供应链投毒，攻击者绕过了项目正常的GitHub Actions CI/CD流水线，将axios维护者的帐户邮箱更改为匿名ProtonMail地址，并通过npm CLI手动发布了带有木马后门的恶意版本，当用户安装后会在主机上建立持久化的远控。影响范围广泛，请相关用户尽快采取措施进行排查与防护。

Axios是一个基于Promise的开源JavaScript HTTP客户端，广泛用于浏览器和Node.js环境。

参考链接：

https://github.com/axios/axios/issues/10604

**SEE MORE →**

**2****影响范围**

**受影响版本**

* axios = 1.14.1
* axios = 0.30.4
  注：Windows、macOS、Linux系统皆受影响，每周下载量超过3亿次。

**不受影响版本**

* axios <= 1.14.0
* axios <= 0.30.3

**3****事件分析**

攻击者窃取并接管了axios项目的主要维护者jasonsaayman的npm和GitHub账户，并将其邮箱修改为匿名的ProtonMail地址：ifstap@proton.me；攻击者先通过单独的一次性账户nrwise@proton.me预先布置了干净的plain-crypto-js@4.2.0建立npm发布历史，规避安全工具对新包的检测告警；等18小时后在npm上更新了恶意包plain-crypto-js@4.2.1，绕过正常的GitHub Actions流程发布恶意版本axios@1.14.和axios@0.30.4，并将plain-crypto-js@4.2.1添加为运行时依赖；plain-crypto-js在安装时会执行setup.js恶意脚本（RAT投放器），其会对当前系统进行检测，并根据macOS、Windows、Linux三个平台分发不同的远程控制载荷。

攻击者在setup.js中植入了自毁逻辑，等木马后门执行完成后，会自动删除自身脚本文件、删除带恶意钩子的package.json，并使用提前备好的干净伪装文件进行替换。

|  |
| --- |
| #脚本自删除 fs.unlink(\_\_filename, (x=>{}));    #用干净的package.md覆盖原始package.json并重命名 fs.rename("package.md", "package.json", (x=>{})); |

事件时间线：

3/30 05:57:32 UTC，攻击者创建plain-crypto-js@4.2.0（干净诱饵铺垫）

3/30 23:59:12 UTC，攻击者发布plain-crypto-js@4.2.1恶意载荷

3/31 00:21:58 UTC，攻击者通过npm CLI发布axios@1.14.1恶意版本

3/31 01:00:57 UTC，攻击者通过npm CLI发布axios@0.30.4恶意版本

3/31 02:30 UTC，攻击者用管理员权限删除告警Issue

3/31 03:40:46 UTC，npm下架恶意版本并吊销所有Token

3/31，绿盟科技CERT发布预警通告

**4****风险排查**

**相关用户可根据下列步骤进行排查：**

1、使用以下命令检查项目中是否存在恶意的axios版本

|  |
| --- |
| #检查项目依赖中的axios版本  npm list axios 2>/dev/null | grep -E "1\.14\.1|0\.30\.4"  #检查lock文件锁定的axios版本 grep -A1 '"axios"' package-lock.json | grep -E "1\.14\.1|0\.30\.4" |

2、检查CI/CD流水线日志，查看是否有任何执行拉取或安装axios新版本的npm install/npm update操作

3、检查node\_modules中是否存在恶意依赖包plain-crypto-js

|  |
| --- |
| ls node\_modules/plain-crypto-js 2>/dev/null && echo "POTENTIALLY AFFECTED" |

注：若package.json为干净存根，则表明后门木马可能已运行。

**用户可使用对应系统的命令检查受影响主机上是否存在后门木马：**

|  |
| --- |
| # macOS ls -la /Library/Caches/com.apple.act.mond 2>/dev/null && echo "COMPROMISED"  # Linux ls -la /tmp/ld.py 2>/dev/null && echo "COMPROMISED"  # Windows dir "%PROGRAMDATA%\wt.exe" 2>nul && echo COMPROMISED |

**5****总结与建议**

本次事件再次为前端生态和开源社区敲醒了供应链安全的警钟，单位务须建立常态化开源组件安全审计机制，构建完善的供应链安全治理体系以预防此类威胁。

建议受影响的用户采取下列措施进行处理：

1、立即将axios降级为安全版本并强制项目所有间接依赖使用：

|  |
| --- |
| #2个分支对应的安全版本  npm install axios@1.14.0 npm install axios@0.30.3  #在package.json中添加overrides和resolutions  {  "dependencies": { "axios": "1.14.0" },  "overrides":    { "axios": "1.14.0" },  "resolutions":  { "axios": "1.14.0" } } |

2、从node\_modules移除plain-crypto-js，清除npm缓存并重新安装依赖：

|  |
| --- |
| rm -rf node\_modules/plain-crypto-js  npm cache clean --force  npm install --ignore-scripts |

3、撤销并轮换系统所有的npm令牌、SSH密钥、云账号密钥、CI/CD密钥、数据库密码等凭证；

4、封禁并排查恶意IoC；

5、实施最小权限原则，限制CI/CD工具的访问范围、并定期轮换凭据；

6、建立常态化开源组件审计机制，增加发布前的多重审批流程。

**6****IOCs**

**恶意文件**

文件名：axios@1.14.1

SHA1: 2553649f2322049666871cea80a5d0d6adc700ca

文件名：axios@0.30.4

SHA1: d6f3f62fd3b9f5432f5782b62d8cfd5247d5ee71

文件名：plain-crypto-js@4.2.1

SHA1: 07d889e2dadce6f3910dcbc253317d28ca61c766

**恶意域名/IP**

sfrclak.com

callnrwise.com

142.11.206.73

**恶意URL**

http://sfrclak.com:8000/6202033

**恶意邮箱**

nrwise@proton.me

ifstap@proton.me

其他

User-Agent：mozilla/4.0 (compatible; msie 8.0; windows nt 5.1; trident/4.0)

**最后的宣传彩蛋：**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tZgxn6yByvKiasTNplKRoOibKFSibX8zvHvqxNia5NibpqEuRbLVt1eMsmW8z0HKicUftN5ibt1iaG2PUDAqN3rOqwY6aQBiaoMz889LDkCiboAoQhS6s/640?wx_fmt=png&from=appmsg)

**安全情报通告服务：**

绿盟科技CERT日常监控国内外上百家主流软件厂商、数十家安全论坛与漏洞社区，结合每日应急安全事件和私域运营进行情报生产，并根据情报评级、PoC披露情况、产品使用流行度、实际利用价值、网空资产测绘数据等多个维度进行综合评估，及时推送最新重大安全漏洞情况及安全事件给客户，整合公司的研究、产品、服务等能力，针对突发性威胁制定可落地的安全防护方案，在威胁事件爆发之前协助客户及时发现问题，采取相关防护措施，保护用户信息系统安全，提升企业应对威胁的能力。

**凭据泄露监测服务：**

近年来，攻击者经常会通过购买或各种手段获取目标用户的登录凭据，进而突破系统入口开展后续攻击，目前主要被用于加密勒索等高威胁场景。为帮助客户能够快速识别自身敏感凭据的泄露风险，绿盟科技特此推出凭据泄露监测服务。此服务以SaaS方式提供，通过7x24小时持续监测数十万数据泄露渠道，结合AI驱动的数据关联分析，当检测到与客户相关的凭据泄露风险后，及时向客户进行预警。

注：对上述服务感兴趣的客户可通过联系绿盟当地区域同事或发送邮件至cert@nsfocus.com咨询交流。

**绿盟科技应急响应中心（NSFOCUS CERT）致力于为客户提供及时、专业、高效的情报预警与应急服务，针对高危漏洞与安全事件进行快速响应，提供可落地的解决方案。**

**END**

![](https://mmbiz.qpic.cn/mmbiz_png/qR4ORTNELImFwJM2rh6GKbnrurdFA28jJ8chUPyC1U6aW3jhenqEiaXkmeGVmfOnvAJy8j3My901JQ7emHaicYzA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_jpg/qR4ORTNELImFwJM2rh6GKbnrurdFA28jib7icfic0lJJHh3eLRpIXiaia08KqOSEibBsz64vlOH9aqicu3lmjccEeAFWQ/640?wx_fmt=jpeg)

**声明**

本安全公告仅用来描述可能存在的安全问题，绿盟科技不为此安全公告提供任何保证或承诺。由于传播、利用此安全公告所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，绿盟科技以及安全公告作者不为此承担任何责任。

绿盟科技拥有对此安全公告的修改和解释权。如欲转载或传播此安全公告，必须保证此安全公告的完整性，包括版权声明等全部内容。未经绿盟科技允许，不得任意修改或者增减此安全公告内容，不得以任何方式将其用于商业目的。

![](https://mmbiz.qpic.cn/mmbiz_jpg/qR4ORTNELImFwJM2rh6GKbnrurdFA28jib7icfic0lJJHh3eLRpIXiaia08KqOSEibBsz64vlOH9aqicu3lmjccEeAFWQ/640?wx_fmt=jpeg)

**绿盟科技CERT**∣微信公众号

![绿盟科技CERT公众号.jpg](https://mmbiz.qpic.cn/mmbiz_jpg/VvfsuOanecqyy67FzSDQ9AuQhEQkiaKC8E2DOicdrIxRv9N6mjHrw2VohBtFUy6Hu7yrGU5mNp84h9jzdH1DibsFg/640?wx_fmt=jpeg&from=appmsg "绿盟科技CERT公众号.jpg")

![](https://mmbiz.qpic.cn/mmbiz/Hu8hctxHqSW0nSJn8p8OHVEQwHicSwTibFJMBE650AxdzfISoeY8woe2QsgCINIBrccBOOUft2HuU0GsNQWibSG7g/640)

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