---
title: Oracle 补丁日安全通告10月份
url: https://mp.weixin.qq.com/s?__biz=Mzg2NjgzNjA5NQ==&mid=2247523752&idx=1&sn=411e7ac0516323477da3feb160e77078&chksm=ce4616b8f9319fae2aeb231cbbd1041d90a6f6b332011d18b4652478776e9bb31894c561a327&scene=58&subscene=0#rd
source: 深信服千里目安全技术中心
date: 2024-10-17
fetch_date: 2025-10-06T18:53:00.071794
---

# Oracle 补丁日安全通告10月份

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/w8NHw6tcQ5wHxYOJBYUibOrXeW85SeuX71KtfD2GXrWnSiaOv87N9qzVyZJFEeOHzI5YZRaz6lCnicylDegWtcILQ/0?wx_fmt=jpeg)

# Oracle 补丁日安全通告10月份

深瞳漏洞实验室

深信服千里目安全技术中心

![](https://mmbiz.qpic.cn/mmbiz_gif/w8NHw6tcQ5wHxYOJBYUibOrXeW85SeuX7Z8oCuvlq77CrmTGIyiblskC7LCRmZ7aehvzlSjaRPy7BCsNlG9BNsJw/640?wx_fmt=gif)

**漏洞名称：**

Oracle 补丁日5个漏洞

**组件名称：**

Oracle WebLogic Server

**安全公告链接：**

https://www.oracle.com/security-alerts/cpuoct2024.html

**官方解决方案：**

已发布

**漏洞分析**

![](https://mmbiz.qpic.cn/mmbiz_gif/w8NHw6tcQ5wHxYOJBYUibOrXeW85SeuX7uHBViaptYEJ5riaZFkILx16qNTpiagB7tEkrpLXTIKK0jSQFhmjG1j2nw/640?wx_fmt=gif)

**组件介绍**

WebLogic是美国Oracle公司出品的一个Application Server，确切地说是一个基于Jave EE架构的中间件，WebLogic是用于开发、集成、部署和管理大型分布式Web应用、网络应用和数据库应用的Java应用服务器。

WebLogic将Java的动态功能和Java Enterprise标准的安全性引入大型网络应用的开发、集成、部署和管理之中，是商业市场上主要的Java（J2EE）应用服务器软件（Application Server）之一，是世界上第一个成功商业化的J2EE应用服务器，具有可扩展性，快速开发，灵活，可靠性等优势。

![](https://mmbiz.qpic.cn/mmbiz_gif/w8NHw6tcQ5wHxYOJBYUibOrXeW85SeuX7uHBViaptYEJ5riaZFkILx16qNTpiagB7tEkrpLXTIKK0jSQFhmjG1j2nw/640?wx_fmt=gif)

**漏洞描述**

近日，深瞳漏洞实验室监测到一则Oracle WebLogic Server官方发布安全补丁的通告，共修复了5个安全漏洞，其中包含1个严重漏洞，4个高危漏洞的信息。

|  |  |  |  |
| --- | --- | --- | --- |
| **序号** | **漏洞****名称** | **影响版本** | **严重等级** |
| 1 | Oracle WebLogic Server 远程代码执行漏洞(CVE-2024-21216) | 12.2.1.4.0  14.1.1.0.0 | 严重 |
| 2 | Oracle WebLogic Server 未授权信息泄露漏洞(CVE-2024-21234) | 12.2.1.4.0  14.1.1.0.0 | 高危 |
| 3 | Oracle WebLogic Server 未授权拒绝服务漏洞(CVE-2024-21274) | 12.2.1.4.0  14.1.1.0.0 | 高危 |
| 4 | Oracle WebLogic Server 未授权拒绝服务漏洞(CVE-2024-21215) | 12.2.1.4.0  14.1.1.0.0 | 高危 |
| 5 | Oracle WebLogic Server 未授权拒绝服务漏洞(CVE-2024-21260) | 12.2.1.4.0  14.1.1.0.0 | 高危 |

![](https://mmbiz.qpic.cn/mmbiz_gif/w8NHw6tcQ5wHxYOJBYUibOrXeW85SeuX7uHBViaptYEJ5riaZFkILx16qNTpiagB7tEkrpLXTIKK0jSQFhmjG1j2nw/640?wx_fmt=gif)

**高危漏洞描述**

****1.**Oracle WebLogic Server 远程代码执行漏洞(CVE-2024-21216)**

Oracle WebLogic Server 存在远程代码执行漏洞，未经授权的攻击者可以通过T3/IIOP协议在服务器上执行恶意代码，导致服务器失陷。

**2.Oracle WebLogic Server 未授权信息泄露漏洞(CVE-2024-21234)**

Oracle WebLogic Server存在未授权访问漏洞，未经身份验证的攻击者可通过该漏洞获取敏感信息。

**3.Oracle WebLogic Server 未授权拒绝服务漏洞(CVE-2024-21274)**

Oracle WebLogic Server存在未授权拒绝服务漏洞，未经身份验证的攻击者可通过该漏洞让服务器崩溃。

**4.Oracle WebLogic S****erver 未授权拒绝服务漏洞(CVE-2024-21215)**

Oracle WebLogic Server存在未授权访问漏洞，未经身份验证的攻击者可通过该漏洞让服务器崩溃。

**5.Oracle WebLogic Server 未授权拒绝服务漏洞(CVE-2024-21260)**

Oracle WebLogic Server存在未授权访问漏洞，未经身份验证的攻击者可通过该漏洞让服务器崩溃。

**影响范围**

WebLogic 是用于开发、集成、部署和管理大型分布式Web 应用、网络应用和数据库应用的 Java 应用服务器，在全球范围内有广泛的使用。可能受漏洞影响的资产广泛分布于世界各地，广东、北京、上海等省市的受影响资产约占国内受影响资产的 70 %。今年曝出的漏洞涉及用户量多，导致漏洞影响力很大。

**解决方案**

![](https://mmbiz.qpic.cn/mmbiz_gif/w8NHw6tcQ5wHxYOJBYUibOrXeW85SeuX7uHBViaptYEJ5riaZFkILx16qNTpiagB7tEkrpLXTIKK0jSQFhmjG1j2nw/640?wx_fmt=gif)

**修复建议**

**1.如何检测组件系统版本**

（1）检测WebLogic版本

访问WebLogic管理控制台页面，即可获取版本号。

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5zn2Bibo7eh2ibFMyWbWx2Lfz6go7GAARhuGia7HNSUWjqV6Fsn37SiaJ3f3kV7n13jPetXseedwqTdCg/640?wx_fmt=png&from=appmsg)

（2）检测WebLogic补丁版本

用户可以通过进入WebLogic安装主目录下的OPatch目录，在此处打开命令行，输入.\opatch lspatches命令，结果如下：

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5zn2Bibo7eh2ibFMyWbWx2LfzmZicBibVYpFoz6BqqKbhSwvSESqSFl7lnXXKWPREphichAQAjesSGkVSQ/640?wx_fmt=png&from=appmsg)

如上图试验设备补丁号为31656851。

**2.打补丁/升级方法:**

**12.2.1.3版本为例**

**步骤1 更新Opatch补丁升级工具**

进入C:\oracle\Middleware\Oracle\_Home\OPatch目录，执行以下命令：

C:\oracle\Middleware\Oracle\_Home\OPatch > opatch version

如图，如果不是13.9.4.0.0版本则需要先升级Opatch版本，否则直接进入步骤2

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5zn2Bibo7eh2ibFMyWbWx2Lfz5BA9cMwHNQ6Lrc1ib9Do62ONOJdzkKAvCaPibKk1OtDWQa7u4s5kV43Q/640?wx_fmt=png&from=appmsg)

**Opatch升级方法：**

**（1）删除旧版本Opatch**

进入C:\oracle\Middleware\Oracle\_Home目录，

重命名OPatch、oracle\_common、oui、inventory四个目录

****（2）**下载并解压安装包**

下载链接：https://updates.oracle.com/Orion/Services/download/p28186730\_139400\_Generic.zip?aru=22731294&patch\_file=p28186730\_139400\_Generic.zip

由于WebLogic在持续更新，请从官网（https://support.oracle.com）下载最新补丁，具体下载方法可参考如下链接：http://blog.itpub.net/31394774/viewspace-2699573

****（3）**安装Opatch**

执行以下命令：

java -jar opatch\_generic.jar -silent oracle\_home=C:\oracle\Middleware\Oracle\_Home

如果出现如下报错，则切换到jdk安装目录的bin目录下重新安装即可

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5zn2Bibo7eh2ibFMyWbWx2Lfz901yltkRaHkRn33ky7LIWYN2F5NxwA28mUe0fMKn2JwSpzWDMOV91w/640?wx_fmt=png&from=appmsg)

****（4）** 检查安装结果**

OPatch、oracle\_common、oui、inventory四个目录已经重新生成，

重新执行命令：C:\oracle\Middleware\Oracle\_Home\OPatch > opatch version

Opatch版本变为13.9.4

**步骤2 下载并解压补丁包**

本文档下载的补丁链接如下：

https://updates.oracle.com/Orion/Services/download/p29016089\_122130\_Generic.zip?aru=22640288&patch\_file=p29016089\_122130\_Generic.zip

由于WebLogic在持续更新，请从官网（https://support.oracle.com）下载最新补丁，具体下载方法可参考如下链接：http://blog.itpub.net/31394774/viewspace-2699573

下载后解压到任意目录。

**步骤3 打补丁前建议阅读README文档**

**步骤4 停止WebLogic服务**

**步骤5 安装补丁**

进入补丁包解压目录，执行以下命令：

C:\oracle\Middleware\Oracle\_Home\OPatch\opatch  apply

**步骤6 重启WebLogic服务**

重启WebLogic服务，并验证业务是否能够正常使用。

注：若补丁导致业务异常，使用如下命令进行回滚：

C:\oracle\Middleware\Oracle\_Home\OPatch\opatch  rollback -id  <补丁ID>

**其他版本**

其他版本必须先升级到12.2.1.3以上版本，才能打补丁，由于WebLogic属于收费服务，升级方法请联系官方技术支持解决。

**3.临时修复建议**

该临时修复建议存在一定风险，建议用户可根据业务系统特性审慎选择采用临时修复方案：

（1）可通过关闭IIOP协议对此漏洞进行临时防御。操作如下：

在WebLogic控制台中，选择“服务”->”AdminServer”->”协议”，取消“启用IIOP”的勾选。并重启WebLogic项目，使配置生效。

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5zn2Bibo7eh2ibFMyWbWx2LfzQXYibc9bibdHXia3lzH1klUy5ot5Ula2sVTXYx5H17ZDFpSme7nIYkCUg/640?wx_fmt=png&from=appmsg)

（2）对T3服务进行控制

控制T3服务的方法:

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5zn2Bibo7eh2ibFMyWbWx2LfzHHmE9tUwI4iavGMhibzmITX2ibOubDUqGrdTraupQyXz3bgYTlcIMvCZQ/640?wx_fmt=png&from=appmsg)

在上图这个WebLogic界面中选择安全-筛选器，在下方出现的界面中找到“连接筛选器”，在里面输入

security.net.ConnectionFilterImpl

然后在连接筛选器规则中输入

127.0.0.1 \* \* allow t3 t3s，0.0.0.0/0 \* \* deny t3 t3s

最后保存并重启服务器即可生效。

![](https://mmbiz.qpic.cn/mmbiz_gif/w8NHw6tcQ5wHxYOJBYUibOrXeW85SeuX7uHBViaptYEJ5riaZFkILx16qNTpiagB7tEkrpLXTIKK0jSQFhmjG1j2nw/640?wx_fmt=gif)

**官方修复建议**

当前官方已发布受影响版本的对应补丁，建议受影响的用户及时更新官方的安全补丁。链接如下：

https://www.oracle.com/security-alerts/cpuoct2024.html

![](https://mmbiz.qpic.cn/mmbiz_gif/w8NHw6tcQ5wHxYOJBYUibOrXeW85SeuX7uHBViaptYEJ5riaZFkILx16qNTpiagB7tEkrpLXTIKK0jSQFhmjG1j2nw/640?wx_fmt=gif)

**深信服解决方案**

**1.风险资产发现**

支持对Oracle WebLogic Server的主动检测，可**批量检出**业务场景中该事件的**受影响资产**情况，相关产品如下：

**【深信服主机安全检测响应平台CWPP】**已发布资产检测方案。

**【深信服云镜YJ】**已发布资产检测方案。

**2.漏洞主动检测**

支持对CVE-2024-21274，CVE-2024-21215，CVE-2024-21234，CVE-2024-21260，CVE-2024-21216漏洞的主动检测，可**批量****快速检出**业务场景中是否存在**漏洞风险**，相关产品如下：

**【深信服云镜YJ】**预计2024年10月20日发布检测方案。编号：SF-0005-21021 到 SF-0005-21025。

**【深信服漏洞评估工具TSS】**预计2024年10月17日发布检测方案。编号：SF-0005-21021 到 SF-0005-21025。

**【深信服安全托管服务MSS】**预计2024年10月17日发布检测方案（需要具备TSS组件能力）。编号：SF-0005-21021 到 SF-0005-21025。

**【深信服安全检测与响应平台XDR】**预计2024年10月20日发布检测方案（需要具备云镜组件能力）。编号：SF-0005-21021 到 SF-0005-21025。

**参考链接**

https://www.oracle.com/security-alerts/cpuoct2024.html

**时间轴**

**2024/10/16**

深瞳漏洞实验室监测到Oracle官方发布安全补丁。

**2024/10/16**

深瞳漏洞实验室中心发布漏洞通告。

点击**阅读原文**，及时关注并登录深信服**智安全平台**，可轻松查询漏洞相关解决方案

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5zn2Bibo7eh2ibFMyWbWx2Lfzz4EmT64k9WBZjpVprsdL5ERtibQO2gelMYNnSvgatetBf4f1GeUkTsg/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_jpg/w8NHw6tcQ5zvcIHbwGGYKbqDVYsVKzNNia1jYtHf49C7133AlDXAgex2W4lFvpia56tjQQDkiauNBrl08YbxqG01A/640?wx_fmt=jpeg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5xUEmJGibg2JE8nVwwxzibBrJTEzuyfhPTuTZeyvTviay6rzGOGrHkAO45vyyibnV1FZThckmmfFfM6BA/0?wx_fmt=png)

深信服千里目安全技术中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5xUEmJGibg2JE8nVwwxzibBrJTEzuyfhPTuTZeyvTviay6rzGOGrHkAO45vyyibnV1FZThckmmfFfM6BA/0?wx_fmt=png)

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