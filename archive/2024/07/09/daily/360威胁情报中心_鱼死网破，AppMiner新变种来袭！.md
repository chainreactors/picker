---
title: 鱼死网破，AppMiner新变种来袭！
url: https://mp.weixin.qq.com/s?__biz=MzUyMjk4NzExMA==&mid=2247499494&idx=1&sn=a8ccdb2ceab9fc02bbe80f47e12bb929&chksm=f9c1cdefceb644f96b46c694516fd44d4e6d530721b22a7772758323770342aec6d6193ab9a3&scene=58&subscene=0#rd
source: 360威胁情报中心
date: 2024-07-09
fetch_date: 2025-10-06T17:46:37.087756
---

# 鱼死网破，AppMiner新变种来袭！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/6CNEHNicic4PqFcpXLEfyCicAtY58Zb5IsVptOG3K7rhrvGWibPN1KKic0uQVq7mhOKefiaCxmybxxpQgtlcAatQehtA/0?wx_fmt=jpeg)

# 鱼死网破，AppMiner新变种来袭！

360威胁情报中心

# **一、背景**

近期，360安全大脑在日常威胁巡检中发现了一种混淆的门罗币挖矿木马，分析发现其为AppMiner新变种，这是该家族继2024年1月的又一次更新。挖矿并不新鲜，但将宿主机弄崩溃的实属少见。攻击者愈发贪婪，以前仅是隐秘挖矿，新变种直接删除主机密码存储和身份认证相关系统文件实现防卸载，致使重启主机无法进入系统界面，堪称鱼死网破之举！截至发稿时其已感染近400台主机，挖矿收益约5 XMR（价值约6000元）；新变种还进一步强化对抗，对C2等敏感信息加密处理以隐藏痕迹。

为此，360安全大脑提醒广大用户，主机感染AppMiner新变种后千万不要关机或重启，应先完成该家族查杀并恢复/etc/passwd等配置文件，以免无法进入系统！鉴于该变种较大的破坏性，360安全大脑特推出AppMiner新变种专杀工具，助力广大用户实时防护及查杀修复，并建议用户从以下5个方面进行加固，以免遭受黑客攻击造成不必要的损失。

|  |
| --- |
| 1）以保留原文件属性方式备份/etc/group 、/etc/passwd等重要系统文件；  2）服务器应配置高强度的登录密码，并定期更换；  3）修改ssh端口为其他端口（非22端口）；  4）若非业务需要，不要在公网开放业务端口（如：redis、GitLab接口），采用本地或内网访问，设置访问白名单等方式进行加固；          5）及时更新主机漏洞补丁，将应用软件升级到安全版本。 |

# **二、主要恶意功能**

分析样本信息如下：

|  |  |  |  |
| --- | --- | --- | --- |
| **MD5** | **文件名** | **文件类型** | **说明** |
| 6392a38d40c8ec0e80b9449ae6358c4b | wtoss | ELF（upx） | 主模块，5个随机字符 |
| 7d7075e6b9a5a5ad36b4627567feadc7 | tepemw | ELF（upx） | 守护程序AppMiner2，  6个随机字符 |
| 8d2f33f064453ed41999c058ac702452 | qiqapm | ELF（upx） | xmrig，6个随机字符 |

为了更直观反应AppMiner的演变进程，此处对其新旧版本作了对比：

|  |  |  |  |
| --- | --- | --- | --- |
| **更新点** | **2024.05****新变种** | **2024.01****版本** | **早期版本** |
| 防卸载：删除主机密码存储和身份认证相关文件 | 是，用户名显示为  I have  no name !，重启主机失败 | 无 | 无 |
| 随机文件名 | 无附加随机字符串+精简文件名  主程序5字符、  子程序及矿工6字符 | 无附加随机字符串  主程序12字符、  矿工14字符 | 附加随机字符串 |
| 函数、变量名 | Gobfuscate混淆+strip函数符号 | 严重混淆  +strip函数符号 | 无混淆  +保留函数符号 |
| 字符串 | 加密C2等敏感字符 | 明文C2 | 明文 |
| 终端运行日志 | 无 | 有 | 有 |

如下是AppMiner新变种的执行流程图：

1）攻击者通过漏洞利用、SSH暴破等方式成功入侵受害者主机后，植入并启动AppMiner新变种主模块（5个随机字符）；

2）主模块请求攻击者制作的Google sites挂马页面，通过正则匹配得到真实的木马下载链接，再经二次正则匹配及base64解码后完成主程序AppMiner1（主模块近似克隆版）、子程序AppMiner2、xmrig矿工的下发及挖矿牟利；

3）主模块删除中招主机/etc目录下的密码存储、身份认证相关文件，阻止中招用户切换到root权限实现防卸载；直接重启主机会导致无法进入系统界面；

4）主程序AppMiner1运行后会重复上述主模块的步骤；

5）子程序AppMiner2作为主程序的守护程序，会再次请求Google sites挂马页面以确保主程序存活且为最新版。

![](https://mmbiz.qpic.cn/mmbiz_jpg/6CNEHNicic4PpcrHriadTI9dIknevhBnkNsKAlpRiaAZT4WDcI9Ekn2Rl33LsFGVecNmecDVIiamrFcAibv9sMaE47Pw/640?wx_fmt=jpeg&from=appmsg)

## **2.1 隐藏敏感信息**

AppMiner新变种（6392a38d40c8ec0e80b9449ae6358c4b）运行时无任何终端日志输出，执行后便删除自身；而早期版本则会输出如下的运行日志：

|  |
| --- |
| 2024/06/25 15:48:59 5050 : 启动子进程成功: -> 5056 |

![](https://mmbiz.qpic.cn/mmbiz_jpg/6CNEHNicic4PpcrHriadTI9dIknevhBnkNs4Gjq028ibibFt7CQnJsw2KsibBTIMIGnhDv9Xzf1GichLveWgQHcxvaqibA/640?wx_fmt=jpeg&from=appmsg)

此外，新变种还对样本中的敏感字符串信息做了加密处理，如下是恢复函数符号前后的对比图：

![](https://mmbiz.qpic.cn/mmbiz_jpg/6CNEHNicic4PpcrHriadTI9dIknevhBnkNsSI2gO8ia2XUt3Kc6Ppe191ibd6nRsibELeHJVByIibubpib9Sb1iaWTmtmpA/640?wx_fmt=jpeg&from=appmsg)

## **2.2 利用Google sites传播木马**

新变种采用了与之前版本相同的恶意模块下发逻辑，但相关C2做了加密处理。

1）新变种访问C2链接：http://www.hellkaluyou.top后返回一个html，通过正则匹配取出其中的url（红框部分）。

![](https://mmbiz.qpic.cn/mmbiz_jpg/6CNEHNicic4PqFcpXLEfyCicAtY58Zb5IsVYicPPUZ1u9iarphAiamv7ElWCI6whrMWh4U46L470c0zvUSPia8rwtsPLQ/640?wx_fmt=jpeg)

2) 访问上述提取出的url，得到下一阶段html

|  |
| --- |
| AppMiner1下载链接：https://www.hellkaluyou.top/1， 通过exe101(.\*)exe101过滤  AppMiner2下载链接：https://www.hellkaluyou.top/2，通过exe102(.\*)exe102过滤  xmrig下载链接1：https://www.hellkaluyou.top/d， 通过UPXD(.\*)UPXD过滤  xmrig下载链接2：https://www.hellkaluyou.top/j， 无响应 |

3）通过正则匹配得到相应base64编码的elf木马，经base64解码后得到对应的elf样本（均为upx样本）。

|  |
| --- |
| exe101：对应AppMiner1的下载链接，大小3504KB，6392a38d40c8ec0e80b9449ae6358c4b  exe102：对应AppMiner2下载链接， 大小3015KB，7d7075e6b9a5a5ad36b4627567feadc7  xmrig矿工：大小2810KB，8d2f33f064453ed41999c058ac702452 |

## **2.3 防卸载，重启无法进入系统界面**

主机感染AppMiner新变种后，用户名处会显示“ I have no name !”，并且无法切换到root用户，重启主机后无法进入系统界面。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PpcrHriadTI9dIknevhBnkNsKV4B0eicnsvLD2DLE597z8sBZib3tiauroRqG7k2Z538icq0xyC3xIAfjQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/6CNEHNicic4PpcrHriadTI9dIknevhBnkNsFibicVubcR9nk9S3TZ5l4KrCMHau0avb0y1E2dxbwO3WuiaH3hlicgzBdA/640?wx_fmt=jpeg&from=appmsg)

分析发现，新变种删除了中招主机中/etc目录下passwd、shadow等与系统密码存储、身份认证相关文件以实现防卸载，致使系统无法查找到此类文件，从而无法认证成功、无法正常重启进入系统界面。/etc目录下被AppMiner新变种删除的的系统文件如下（红框部分）：

![](https://mmbiz.qpic.cn/mmbiz_jpg/6CNEHNicic4PpcrHriadTI9dIknevhBnkNsK9I3tz6FSvUVMHNo8n0ic0alGqpkJXuVyWsnicq4U33qib1d6tqpKIdpA/640?wx_fmt=jpeg&from=appmsg)

除了删除passwd、shadow等系统文件，AppMiner还会在/etc目录保存其下载的木马模块（木马模块使用随机文件名，主程序为5个字符，子程序为6个字符）。因此，主机感染AppMiner新变种后千万不要关机或重启，应先完成该家族查杀并恢复/etc/passwd等配置文件，否则无法进入系统界面！

## **2.4 持久化**

该部分功能与之前版本逻辑相同，即：

1）向/etc/profile文件中写入执行木马主模块（/etc/wtoss）的shell指令，以实现开机启动。

|  |
| --- |
| echo My>/dev/null 2>&1 &/etc/wtoss >/dev/null 2>&1 & |

2）向crontab中写入执行主模块的定时任务（主模块运行后删除自身，并从C2下载恶意模块到 /etc目录），以实现持久化。

|  |
| --- |
| /bin/bash -c "(crontab -l 2>/dev/null; echo \"\*/2 \* \* \* \* /etc/wtoss\") | crontab -" |

## **2.5 门罗币挖矿**

AppMiner下载的xmrig矿工（/etc/qiqapm，6个字符的随机文件名）运行后便删除自身，其采用与早期版本相同的挖矿进程名[card0-crtc0]。如下是其挖矿时的截图信息：

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PpcrHriadTI9dIknevhBnkNs8pdJaKnzX7PJPJ3caRsHMKQib1fGlRBeOyNNgkAxaCBboicOibtnqDicEA/640?wx_fmt=png&from=appmsg)

AppMiner新变种采用c3pool矿池，挖矿收益约5XMR，感染近400台主机。

![](https://mmbiz.qpic.cn/mmbiz_jpg/6CNEHNicic4PpcrHriadTI9dIknevhBnkNsH62rTk3cMSJ4ugPaumicKglaXianp13I5SPjrCmsXJEzNEs0uceUeffw/640?wx_fmt=jpeg&from=appmsg)

#

**附录 IOC**

#

**C2:**

www[.]hellkaluyou.top

**MD5:**

6392a38d40c8ec0e80b9449ae6358c4b

7d7075e6b9a5a5ad36b4627567feadc7

8d2f33f064453ed41999c058ac702452

858494af949b7dad69729ff243c54cb9

813bb1a38d50bcd5bef8d91a3b578017

**矿池：**

auto[.]c3pool.org:443

auto[.]c3pool.org:80

47[.]243.167.150:443

auto[.]c3pool.org:19999

**钱包地址：**

84Q498z9XexF8nnbUmvjiFS94k2DYRadA754zB7Xka551dCcnAQQgW9RUE8NfCbiGEMsJHMXWFJ5zWGeUYRYsVtZBB8VYWb

#

**参考**

#

SupermanMiner挖矿木马新变种持续活跃

（https://cert.360.cn/warning/detail?id=65deee7fc09f255b91b17e0f）

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Pruscv37D0qgOMbfC4jVxUnso6yyhQC9OIyDNX6TYo5k8iafcfZMzT0ia5boCo69WZSicq7krbicKaHsw/0?wx_fmt=png)

360威胁情报中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Pruscv37D0qgOMbfC4jVxUnso6yyhQC9OIyDNX6TYo5k8iafcfZMzT0ia5boCo69WZSicq7krbicKaHsw/0?wx_fmt=png)

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