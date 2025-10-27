---
title: 近期APT组织SideCopy针对印度政府的钓鱼攻击活动分析
url: http://blog.nsfocus.net/sidecopyphishinganalysis/
source: 绿盟科技技术博客
date: 2023-02-25
fetch_date: 2025-10-04T08:04:32.174364
---

# 近期APT组织SideCopy针对印度政府的钓鱼攻击活动分析

* [登录](http://blog.nsfocus.net/wp-login.php)
* [注册](http://blog.nsfocus.net/wp-login.php?action=register)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

# 近期APT组织SideCopy针对印度政府的钓鱼攻击活动分析

### 近期APT组织SideCopy针对印度政府的钓鱼攻击活动分析

[2023-02-24](https://blog.nsfocus.net/sidecopyphishinganalysis/ "近期APT组织SideCopy针对印度政府的钓鱼攻击活动分析")[伏影实验室](https://blog.nsfocus.net/author/fuying-lab/ "View all posts by 伏影实验室")[Advisory](https://blog.nsfocus.net/tag/advisory/), [India](https://blog.nsfocus.net/tag/india/), [Pakistan](https://blog.nsfocus.net/tag/pakistan/), [ReverseRAT](https://blog.nsfocus.net/tag/reverserat/), [SideCopy](https://blog.nsfocus.net/tag/sidecopy/)

阅读： 2,152

## ****一、事件概要****

**1.1 事件简介**

2月1日，绿盟科技监测到一份恶意宏文档，名为”Cyber Advisory 2023.docm”（网络安全通告2023）。经分析，确认该文档由巴基斯坦APT组织SideCopy投递，目的是引诱目标打开阅览的同时下载ReverseRAT木马，以接收C&C指令进行窃密活动。

关于SideCopy的历史攻击事件，参见绿盟博客伏影实验室文章《近期巴基斯坦APT组织SIDECOPY针对印度军事训练营的鱼叉攻击活动》（https://blog.nsfocus.net/apt-sidecopy/）。

**1.2 组织****背景**

SideCopy由安全公司Quick Heal于2020年披露，近年来因受印巴紧张关系影响而频繁活跃。该组织的主要攻击目标以印度的军事设施为主，尤其是与克什米尔边防相关的机构，与巴基斯坦的国家利益关联。据研究人员分析，SideCopy与巴基斯坦主要APT组织TransparentTribe在TTP方面存在相似性，可能存在从属或合作关系。

**1.3 诱饵文档**

本次事件中，SideCopy作者冒充印度政府信息部门官员投递诱饵文档，类型为通告（Advisory），主题为“安卓威胁与预防措施”，并在正文部分列出了几种针对安卓手机的攻击方式和应对手段。从正文落款来看，通告的“作者”为印度安全保障部的安全审计总监Vinai Kumar Kanaujia。通告是印度政府发布的应用文格式之一，有些会保存在官方网站上，因此可被攻击者轻易获得来学习其话术，从而构建诱饵文档。

![](https://blog.nsfocus.net/wp-content/uploads/2023/02/wps_doc_7-5-300x193.png)

诱饵文档内容

考虑到巴方攻击组织曾使用安卓间谍工具来针对印度（安卓手机在印度市场占有率较高），再结合本次事件诱饵文档中对安卓安全的强调以及SideCopy的既往偏好，推测其本次攻击的目标应为印度政府、军队或重点科研单位人员，尤其是安卓手机用户。

而根据文档属性中的首次出现时间，本次攻击活动可能发生在1月28日~1月30日。

![](https://blog.nsfocus.net/wp-content/uploads/2023/02/wps_doc_8-5.png)

文档属性

诱饵文档开头最上方一行醒目的一号字体内容并不是标题，而是提醒目标启用宏，显示这是一次利用恶意宏进行的钓鱼攻击，是APT组织的惯用手法。

通告的结构形式完全按照印度政府通告的标准，在写完主题（Subject）和一段摘要后，对正式内容直接从2开始标号。

不过，该通告在制作时存在纰漏：通告第3条建议提到附录1，但实际并不存在；同时，通告末尾处还提到一个“链接”，但并未指向任何实际网址。

通告落款处为发出者Vinai Kumar Kanaujia信息，并包含其个人签名，但该签名与印度政府官网公开文档中的真人签名有显著差异。相比之下，历史签名更能看出对应的人名字母，而此次文档中的签名则非常潦草，存在伪造签名的情况。

![](https://blog.nsfocus.net/wp-content/uploads/2023/02/wps_doc_9-5-300x169.png)

诱饵文档签名与Vinai Kumar Kanaujia真人历史签名对比

**1.4 活动简述**

本次SideCopy活动流程较为直接，通过诱饵文档内嵌的恶意宏来下载木马并执行。

![](https://blog.nsfocus.net/wp-content/uploads/2023/02/wps_doc_10-5-300x122.png)

攻击流程

## ****二、详细分析****

**2.1 第一阶段** **–** **诱饵文档**

**2.1.1 Cyber Advisory 2023.docm**

诱饵文档通过首行醒目的一号字体内容，诱使目标启用宏。当目标关闭文档时，内置的VBA宏则通过HTTP GET请求访问luckyoilpk.com/vlan.html。该网站曾被标注为巴基斯坦某能源公司（Lucky Oil Company）的官网，但如今打开后显示出错，表明其已被用作水坑站点。

![](https://blog.nsfocus.net/wp-content/uploads/2023/02/wps_doc_11-5-300x117.png)

luckyoilpk.com网站

之后VBA宏从下载的内容中抽取出木马数据，并通过FreeFile方式来创建本地文件。其中，木马被命名为vlan.exe，保存在Startup目录下，尽管没有被直接执行，但已实现了开机自启动。

![](https://blog.nsfocus.net/wp-content/uploads/2023/02/wps_doc_12-4-300x85.png)

VBA宏

![](https://blog.nsfocus.net/wp-content/uploads/2023/02/wps_doc_13-4-300x40.png)

VBA宏下载得到的Payload

**2.2 第二阶段** **–** **执行木马**

**2.2.1 vlan.exe**

下载的vlan.exe是经过混淆的ReverseRAT木马。该家族为SideCopy组织已知攻击载荷（亦被思科称为CetaRAT），用于执行各类远程控制功能。

![](https://blog.nsfocus.net/wp-content/uploads/2023/02/wps_doc_14-4-300x145.png)

ReverseRAT会在启动后收集宿主机的基本信息，经过Gzip压缩和RC4加密（初始密钥为”12121”），并通过HTTP POST发送至CnC。

![](https://blog.nsfocus.net/wp-content/uploads/2023/02/wps_doc_15-4-300x77.png)

实验环境下的HTTPPOST流量

表1 收集的基本信息

|  |  |
| --- | --- |
| **k****ey****name** | **v****alue** |
| **mode** | 发送模式，上传基础信息时为”info” |
| **id** | 网卡地址 |
| **compname** | 主机名称 |
| **os** | 操作系统名称与版本 |
| **ip** | 公网地址IP |
| **memory** | 内存总大小 |
| **p****rocessor** | CPU型号 |
| **w****ebcam** | 检测到摄像头则为1，否则为0 |
| **i****nterval** | 默认等待时间 |

之后，木马对C&C返回的内容进行对等处理，通过RC4解密和Gzip解压，提取其中的C&C指令。指令分为名称与参数，每项之间由“|”隔开，格式为：

<指令名称> | <参数1> | <参数2> | ….

表2 指令与功能

|  |  |
| --- | --- |
| **指令** | **功能** |
| **“list”** | 获取指定目录的文件列表 |
| **“downloadexe”** | 下载可执行文件并执行 |
| **“run”** | 执行指定文件 |
| **“close”** | 退出 |
| **“upload”** | 压缩上传指定文件 |
| **“download”** | 解压并保存文件 |
| **“regdelkey”** | 删除注册表指定键或值 |
| **“delete”** | 删除文件或目录 |
| **“screen”** | 屏幕截图 |
| **“reglist”** | 获取指定注册表键值列表 |
| **“clipboardset”** | 写剪贴板 |
| **“process”** | 获取进程与对对应文件信息 |
| **“programs”** | 获取安装程序信息 |
| **“rename”** | 移动指定文件 |
| **“pkill”** | 杀指定进程 |
| **“clipboard”** | 读剪贴板 |
| **“shellexec”** | 执行命令行 |
| **“creatdir”** | 创建目录 |
| **“regnewkey”** | 创建新键值 |

执行指令后，返回的内容结构与上传基础信息时类似，同样经过压缩和加密，指定发送方式为“返回指令结果”，具体传输方式不变。

表3 返回的信息

|  |  |
| --- | --- |
| **k****ey****name** | **v****alue** |
| **mode** | 发送模式，返回指令结果时为”result” |
| **id** | 网卡地址 |
| **result** | 指令执行结果 |

## ****三、总结****

SideCopy组织此次活动流程较为简洁，一次性通过钓鱼文档下载远控木马，没有其他中间环节。SideCopy对远控木马做了混淆处理，但由于其整体逻辑并不复杂，因此很容易被识别出是ReverseRAT。此外，诱饵文档的VBA宏是在文档关闭时触发，而且下载远控木马后并未执行，而是需要重启，这两点表明攻击者有意推迟恶意代码的运行，在一定程度上增强了行为的隐匿性。

## ****四、I********o********c****

ffa2e6f6a7a8001f56c352df43af3fe5

luckyoilpk.com

0baa1d0cc20d80fa47eeb764292b9e98

http[:]//185.174.102.54:443/

**版权声明**
本站“技术博客”所有内容的版权持有者为绿盟科技集团股份有限公司（“绿盟科技”）。作为分享技术资讯的平台，绿盟科技期待与广大用户互动交流，并欢迎在标明出处（绿盟科技-技术博客）及网址的情形下，全文转发。
上述情形之外的任何使用形式，均需提前向绿盟科技（010-68438880-5462）申请版权授权。如擅自使用，绿盟科技保留追责权利。同时，如因擅自使用博客内容引发法律纠纷，由使用者自行承担全部法律责任，与绿盟科技无关。

Spread the word. Share this post!

[Previous](https://blog.nsfocus.net/securityloophole/)

[Next](https://blog.nsfocus.net/socks5dns/)

### Meet The Author

伏影实验室

伏影实验室专注于安全威胁监测与对抗技术研究。
研究目标包括Botnet、APT高级威胁，DDoS对抗，WEB对抗，流行服务系统脆弱利用威胁、身份认证威胁，数字资产威胁，黑色产业威胁及新兴威胁。通过掌控现网威胁来识别风险，缓解威胁伤害，为威胁对抗提供决策支撑。

咨询与合作：nsmagazine@nsfocus.com

* [绿盟科技官网](https://www.nsfocus.com.cn)
* [绿盟威胁情报中心（NTI）](https://nti.nsfocus.com)
* [绿盟云](https://cloud.nsfocus.com)