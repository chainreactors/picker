---
title: 黑天鹅出没！微软突发“蓝屏派对” ，系统崩溃陷入混乱
url: https://www.4hou.com/posts/QX1l
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-07-21
fetch_date: 2025-10-06T17:38:30.400208
---

# 黑天鹅出没！微软突发“蓝屏派对” ，系统崩溃陷入混乱

黑天鹅出没！微软突发“蓝屏派对” ，系统崩溃陷入混乱 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 黑天鹅出没！微软突发“蓝屏派对” ，系统崩溃陷入混乱

山卡拉
[新闻](https://www.4hou.com/category/news)
2024-07-20 08:25:43

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)106975

收藏

导语：7月19日,微软在全球多地出现“蓝屏故障”,大量用户无法正常操作系统,其中不少出现了“csagent.sys”错误。

7月19日,微软在全球多地出现“蓝屏故障”,大量用户无法正常操作系统,其中不少出现了“csagent.sys”错误。其原因是美国网络安全服务提供商CrowdStrike更新错误所致。该事件影响到了世界各地的各种组织和服务，包括机场、电视台和医院等大型企业。

![1111111.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240720/1721434097413302.jpg "1721434097413302.jpg")

事发当天，大量用户反馈在安装 CrowdStrike Falcon Sensor 的最新更新后，Windows 主机陷入启动循环或显示蓝屏死机 (BSOD)。

该安全供应商承认了该问题，并发布了技术警报，解释称其工程师“发现了与此问题相关的内容部署并撤销了这些更改”。

CrowdStrike 的工程团队迅速应对了这一危机。根据该公司论坛上的一个置顶帖，该团队已确定与该问题相关的内容部署并恢复了这些更改。

CrowdStrike透露，罪魁祸首是一个通道文件，其中包含传感器的数据。由于它只是传感器更新的一个组件，因此可以单独解决此类文件，而无需删除 Falcon 传感器更新。

**对于已经受到影响的用户，CrowdStrike 提供了以下解决方法：**

1、将 Windows 启动到安全模式或 Windows 恢复环境

（1）重启你的电脑。

（2）当您的计算机重新启动时，按F8（或Shift + F8）打开高级启动选项菜单。

（3）选择Safe Mode并按 Enter。

2、删除相关文件

（1）导航到 C:\Windows\System32\drivers\CrowdStrike 目录。

（2）找到匹配“C-00000291\*.sys”的文件，并将其删除。

3、重启电脑。

CrowdStrike 的首席执行官表示他们已经发布了修复程序，并建议客户下载最新更新。

![](https://www.bleepstatic.com/images/news/u/1100723/GeorgeKurtz_CrowdStrike_outage.png)

CrowdStrike 首席执行官就故障更新导致 Windows 主机崩溃一事发表评论

在更新的声明中，CrowdStrike 表示“有问题的文件 [ C-00000291\*.sys”，时间戳为 0409 UTC ] 已被恢复”，其正确版本是 C-00000291\*.sys， 时间戳为 0527 UTC 或更新。

该公司还提供了两种解决云和虚拟环境中该问题的选项，一种是回滚到 UTC 04:09 之前的快照。第二种选择是以下七步程序：

1.从受影响的虚拟服务器中分离操作系统磁盘卷

2.在继续操作之前，请创建磁盘卷的快照或备份，以防发生意外更改

3.将卷附加/安装到新的虚拟服务器

4.导航到 %WINDIR%\System32\drivers\CrowdStrike 目录

5.找到匹配“C-00000291\*.sys”的文件，并将其删除。

6.从新的虚拟服务器分离卷

7.将固定卷重新连接到受影响的虚拟服务器

**对于此次微软蓝屏事件，奇安信安全专家汪列军表示：**

> CrowdStrike软件更新导致Windows计算机瘫痪的主要原因是其核心驱动csagent.sys出现了bug，导致操作系统无法正常启动，甚至出现蓝屏。这种情况与一般应用程序不同，因为安全软件的驱动操作涉及操作系统底层，一旦出现问题就会直接影响系统稳定性。
>
> 这一事件影响广泛，特别是在亚太地区（如日本）首先显现，但也在欧美等其他地区引起了不小的波及。影响范围主要集中在使用CrowdStrike的外企及其在中国的分支机构，以及部分国外的云计算环境，尤其是基于Windows的应用实例。
>
> 虽然事件影响了多个Windows版本，但具体影响的范围可能因技术细节而有所不同。此外，虽然有简单的修复方法，例如手动删除或重命名相关驱动文件，但由于涉及大量机器且无法集中管理，修复过程相对耗时复杂，需要逐台操作。
>
> 综上所述，这一事件显示了安全软件更新可能带来的系统性风险，尤其是对大规模部署的影响管理和应急响应能力提出了挑战。

**参考及文献来源：**

**·** https://gbhackers.com/crowdstrike-update-triggers-widespread/

**·** https://www.bleepingcomputer.com/news/security/crowdstrike-update-crashes-windows-systems-causes-outages-worldwide/

**·** 奇安信安全专家汪列军访谈解读。

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?T3dANbfn)

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

![](https://img.4hou.com/FjC8MmzrcnfY_rzJyoXU2_G-O0i9)

# [山卡拉](https://www.4hou.com/member/azxO)

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

[查看更多](https://www.4hou.com/member/azxO)

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

[![](https://www.4hou.com/sihou/images/new4hou/weibo.png)](http://weibo.com/u/6069423878)
![](https://www.4hou.com/sihou/images/new4hou/wechat.png)

本站4hou.com，所使用的字体和图片文字等素材部分来源于原作者或互联网共享平台。如使用任何字体和图片文字有侵犯其版权所有方的，嘶吼将配合联系原作者核实，并做出删除处理。

[©2024 北京嘶吼文化传媒有限公司 京ICP备16063439号-1](https://beian.miit.gov.cn/)
本站由 ![](https://www.4hou.com/sihou/images/new4hou/txcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/bdcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/ucloud.png) 提供云计算服务

微信

[微博](http://weibo.com/u/6069423878)
[RSS](https://www.4hou.com/feed)
[知乎](https://zhuanlan.zhihu.com/roartalk)