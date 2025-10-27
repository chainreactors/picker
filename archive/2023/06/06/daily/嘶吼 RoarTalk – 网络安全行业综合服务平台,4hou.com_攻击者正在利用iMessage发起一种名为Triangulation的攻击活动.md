---
title: 攻击者正在利用iMessage发起一种名为Triangulation的攻击活动
url: https://www.4hou.com/posts/xz1E
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-06-06
fetch_date: 2025-10-04T11:44:48.851790
---

# 攻击者正在利用iMessage发起一种名为Triangulation的攻击活动

攻击者正在利用iMessage发起一种名为Triangulation的攻击活动 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# 攻击者正在利用iMessage发起一种名为Triangulation的攻击活动

lucywang
[新闻](https://www.4hou.com/category/news)
2023-06-05 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)178694

收藏

导语：iOS 15.7及其之前的版本存在一个安全漏洞，攻击者正利用iMessage发起一种名为Triangulation的攻击活动。

![微信截图_20230603144314.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230603/1685775257156315.png "1685775257156315.png")

根据卡巴斯基发布的最新报告，有攻击者利用 iMessage 来传播恶意软件，iOS 15.7 以及此前版本均受到影响。研究人员通过 mvt-ios（iOS 移动验证工具包）分析问题设备之后，发现攻击者可以通过 iMessage 发送信息，受害者在接收到信息之后，不需要任何用户交互，就能触发系统内漏洞，从而执行任意恶意代码。

**具体分析**

卡巴斯基实验室研究人员在监控专用于移动设备的Wi-Fi网络的网络流量时，注意到几个基于ios的手机的可疑活动。由于无法从内部检查现代iOS设备，研究人员创建了这些被攻击设备的离线备份，使用移动验证工具包的mvt-ios对其进行了检查，并发现了攻击的一些技术细节。移动验证工具包 (MVT) 是一组实用程序，用于简化和自动化收集取证痕迹的过程，有助于识别 Android 和 iOS 设备的潜在危害。目前，研究人员将这个攻击活动称为“Triangulation活动”。

研究人员创建的移动设备备份包含文件系统的部分副本，包括一些用户数据和服务数据库。文件、文件夹和数据库记录的时间戳允许研究人员重建设备上发生的事件。mvt-ios实用程序将事件的排序时间轴生成一个名为“timeline.csv”的文件，类似于传统数字取证工具使用的超级时间轴。

使用这个时间轴，研究人员能够识别出被攻击的特定固件，并重建了一般的攻击顺序：

1.目标iOS设备通过iMessage服务接收一条消息，其中包含一个包含漏洞的附件。

2.在没有任何用户交互的情况下，该消息会触发导致代码执行的漏洞。

3.利用漏洞攻击中的代码从C&C服务器下载几个后续阶段，其中包括用于权限提升的其他利用漏洞攻击；

4.成功利用后，从C&C服务器下载最终有效负载，这是一个功能齐全的APT平台。

5.附件中的初始消息和漏洞攻击痕迹会被自动删除。

恶意工具集不支持持久性，很可能是由于操作系统的限制。多个设备的时间轴表明，它们可能在重新启动后被重新攻击。研究人员发现的最古老的攻击痕迹发生在2019年。截至发文时，攻击仍在进行中，最新被攻击的版本为iOS 15.7。

对最终有效负载的分析尚未完成，该代码以root权限运行，实现了一组用于收集系统和用户信息的命令，并且可以运行从C&C服务器下载的作为插件模块的任意代码。

需要注意的是，尽管恶意软件包括专门用于清除攻击痕迹的代码部分，但可以可靠地识别设备是否被攻击。此外，如果通过从旧设备迁移用户数据来设置新设备，那么该设备的iTunes备份将包含发生在这两个设备上的攻击痕迹，并带有正确的时间戳。

所有潜在的目标设备都必须使用iTunes或开源实用程序idevicebackup2（来自libimobiledevice包）进行备份。后者作为最流行的Linux发行版的预构建包提供，或者可以从MacOS/Linux的源代码构建。

要使用idevicebackup2创建备份，就要运行以下命令：

```
idevicebackup2 backup --full $backup_directory
```

你可能需要多次输入设备的安全码，根据存储的用户数据量，该过程可能需要几个小时。

**安装MVT**

备份准备就绪后，就必须由移动验证工具包进行处理。如果系统中安装了Python 3，就要运行以下命令：

```
pip install mvt
```

更全面的安装手册可以在MVT主页上找到。

**解密备份**

如果设备所有者以前已为备份设置了加密，则备份副本将被加密。在这种情况下，备份副本必须在运行检查之前解密：

```
mvt-ios decrypt-backup -d $decrypted_backup_directory $backup_directory
```

**使用MVT分析备份**

mvt-ios check-backup -o $mvt\_output\_directory $decrypted\_backup\_directory命令将通过MVT运行所有检查，输出目录将包含几个JSON和CSV文件。使用本文中描述的方法时，你将需要名为timeline.csv的文件。

**查看timeline.csv中的指标**

研究人员发现的唯一最可靠的指标是提到名为“BackupAgent”的进程的数据使用行。这是一个废弃的二进制文件，在正常使用设备期间该文件不应出现在时间轴中。然而，需要注意的是，还有一个名为“BackupAgent2”的二进制文件，这并不是一个攻击指标。

在许多情况下，BackupAgent前面有一个进程“IMTransferAgent”，它下载的附件恰好是一个漏洞，这导致修改“Library/SMS/Attachments”中多个目录的时间戳。然后删除附件，只留下修改过的目录，其中没有实际的文件：

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230603/1685775217273962.png "1685775082113950.png")

还有一些不太可靠的指标，如果其中几个指标在几分钟内发生，则可能被视为IOC：

1.修改一个或多个文件：com.apple.ImageIO.plist, com.apple.locationd.StatusBarIconManager.plist, com.apple.imservice.ids.FaceTime.plist；

2.服务的数据使用信息com.apple.WebKit.WebContent, powerd/com.apple.datausage.diagnostics, lockdownd/com.apple.datausage.security。

示例：

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230603/1685775218754318.png "1685775096794247.png")

另一个示例：修改短信附件目录（但没有附件文件名），然后使用com.apple.WebKit.WebContent的数据，最后修改com.apple.locationd.StatusBarIconManager.plist。所有事件都发生在1-3分钟内，这表明通过iMessage附件成功实现了攻击。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230603/1685775218646597.png "1685775113211634.png")

另外一个攻击指标是用户无法安装iOS更新。研究人员发现了发现恶意代码修改了一个名为com.apple.softwareupdateservicesd.plist的系统设置文件，他们观察到更新尝试以错误消息“软件更新失败，下载iOS时出错”结束。

**漏洞利用期间的网络活动**

在网络活动中，成功的利用尝试可以通过几个HTTPS连接事件的顺序来识别。这些可以在包含DNS/TLS主机信息的网络流数据或PCAP转储中被发现：

1.与iMessage服务进行合法的网络交互，通常使用域名\*.ess.apple.com；

2.使用域名icloud-content.com、content.icloud.com下载iMessage附件；

3.到C&C域的多个连接，通常是2个不同的域（下面是已知域的列表）。C&C会话的典型网络流数据将显示具有大量传出流量的网络会话。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230603/1685775219223893.png "1685775137567790.png")

网络漏洞利用顺序，Wireshark转储

iMessage附件是通过HTTPS加密和下载的，唯一可以使用的隐含指标是下载的数据量，约为242 Kb。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230603/1685775220207312.png "1685775154184146.png")

加密iMessage附件，Wireshark转储

**C&C域**

使用取证固件，可以识别漏洞利用和之后恶意阶段使用的域名集。它们可用于检查DNS日志中的历史信息，并识别当前运行恶意软件的设备：

```
addatamarket[.]netbackuprabbit[.]combusinessvideonews[.]comcloudsponcer[.]comdatamarketplace[.]netmobilegamerstats[.]comsnoweeanalytics[.]comtagclick-cdn[.]comtopographyupdates[.]comunlimitedteacup[.]comvirtuallaughing[.]comweb-trackers[.]comgrowthtransport[.]comanstv[.]netans7tv[.]net
```

尽管卡巴斯基已经发现了这一漏洞，但关于该漏洞的最新修复和更新信息暂未得知。为了确保设备安全，建议用户及时升级到最新的iOS系统版本，并遵循相关的安全建议和最佳实践。同时，避免点击来自不明来源的链接或点击可疑信息。

本文翻译自：https://securelist.com/operation-triangulation/109842/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?UGUKfxwa)

#### 你可能感兴趣的

* [![]()

  ​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
* [![]()

  新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
* [![]()

  新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
* [![]()

  Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
* [![]()

  npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/posts/mk5p)
* [![]()

  大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/posts/l01l)

![](https://img.4hou.com/uploads/20171229/1514527090244385.gif)

# [lucywang](https://www.4hou.com/member/eXPv)

这个家伙很懒,什么也没说!

#### 最新文章

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
  2025-09-30 12:01:00
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
  2025-09-29 12:00:00
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
  2025-09-28 12:00:00
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
  2025-09-26 12:01:00

[查看更多](https://www.4hou.com/member/eXPv)

# 相关热文

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)

  胡金鱼
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)

  胡金鱼
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)

  胡金鱼
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)

  胡金鱼
* [npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/posts/mk5p)

  胡金鱼
* [大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/posts/l01l)

  胡金鱼

![]()

[公司简介](https://www.4hou.com/about?title=公司简介)
|
[我要投稿](https://www.4hou.com/about?title=我要投稿)
|
[更新日志](https://www.4hou.com/about?title=更新日志)
|
[友情链接](https://www.4hou.com/about?title=友情链接)
|
[隐私政策](https://www.4hou.com/about?title=隐私政策)
|

[![](https://www.4hou.com/...