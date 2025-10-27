---
title: 针对ESXi虚拟化平台勒索攻击威胁通告
url: http://blog.nsfocus.net/esxi/
source: 绿盟科技技术博客
date: 2022-12-22
fetch_date: 2025-10-04T02:13:42.061336
---

# 针对ESXi虚拟化平台勒索攻击威胁通告

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

# 针对ESXi虚拟化平台勒索攻击威胁通告

### 针对ESXi虚拟化平台勒索攻击威胁通告

[2022-12-21](https://blog.nsfocus.net/esxi/ "针对ESXi虚拟化平台勒索攻击威胁通告")[绿盟科技](https://blog.nsfocus.net/author/nsfocus/ "View all posts by 绿盟科技")[安全漏洞](https://blog.nsfocus.net/tag/%E5%AE%89%E5%85%A8%E6%BC%8F%E6%B4%9E/), [漏洞防护](https://blog.nsfocus.net/tag/%E6%BC%8F%E6%B4%9E%E9%98%B2%E6%8A%A4/)

阅读： 993

****一、事件概述****

绿盟科技CERT团队近期陆续接到多个行业客户反馈遭受勒索病毒攻击，具体表现为企业内网部署的ESXi虚拟化平台遭受攻击，VMware虚拟磁盘等文件后缀被修改为.mario，同时存在勒索信息文件How To Restore Your Files.txt。

![](https://blog.nsfocus.net/wp-content/uploads/2022/12/wps_doc_2-3-300x165.png)

勒索信息文件中包含游戏人物超级马里奥的logo，对应的攻击团伙为RansomHouse，该团伙除了对虚拟机文件进行加密外，还对企业敏感数据进行了窃取。

![](https://blog.nsfocus.net/wp-content/uploads/2022/12/wps_doc_3-2-300x292.png)

该团伙的暗网博客内容与其他勒索病毒家族类似，同样公布了受害企业信息、攻击时间，泄露数据等信息。

![](https://blog.nsfocus.net/wp-content/uploads/2022/12/wps_doc_4-1-300x219.png)

## ****二、样本概述****

经分析确认，此次勒索病毒样本为Babuk变种。Babuk又称Babyk，最早出现于2021年初，同时支持对Windows、ESXi及NAS主机进行加密，2021年9月某俄语黑客论坛上泄露了Babuk勒索软件的完整源代码，包括加密程序、解密程序及生成器。

通过对比Babuk源码及mario代码，发现两者代码基本一致，包括生成的勒索信息文件名。

![](https://blog.nsfocus.net/wp-content/uploads/2022/12/wps_doc_5-1-300x72.png)

攻击者仅修改了加密后的文件后缀名以及加密的目标文件后缀名列表，增加了对VMware虚拟机打包相关文件后缀（ovf及ova）的支持。

![](https://blog.nsfocus.net/wp-content/uploads/2022/12/wps_doc_6-1-300x135.png)

样本加密过程采用非对称密钥算法获得对称密钥，再使用对称密钥算法加密文件，并会对大文件进行分块加密，同时在加密结束后会将密钥内存清零，导致无法在受害主机内存中找到对称密钥痕迹。

![](https://blog.nsfocus.net/wp-content/uploads/2022/12/wps_doc_7-1-300x178.png)

## ****三、攻击概述****

攻击者首先通过网络钓鱼及水坑攻击获取内部员工PC控制权限，并以此为据点，开始利用AD域相关漏洞获取域控制器权限，并进一步窃取域管理员登录凭证。

随后在域内利用窃取的窃取域管理员凭证，针对目标主机进行横向移动攻击，主要攻击手段为WMI远程命令执行。

![](https://blog.nsfocus.net/wp-content/uploads/2022/12/wps_doc_8-1-300x87.png)

同时还会利用微软SysInternals套件中的PsExec工具，以通过本地提权方式获取系统权限。

![](https://blog.nsfocus.net/wp-content/uploads/2022/12/wps_doc_9-1-300x124.png)

为了躲避相关安全设备监测，攻击者还通过命令行部署了TightVNC软件，以实现后门方式对主机进行远程控制。

![](https://blog.nsfocus.net/wp-content/uploads/2022/12/wps_doc_10-1-300x127.png)

随后，攻击者通过在IT运维人员主机上窃取的相关凭证，通过内网部署的vCenter重置了ESXi管理员口令。

![](https://blog.nsfocus.net/wp-content/uploads/2022/12/wps_doc_11-1-300x45.png)

最终，攻击者通过SSH登录ESXi后，上传并执行了其勒索病毒程序。

![](https://blog.nsfocus.net/wp-content/uploads/2022/12/wps_doc_12-1-300x57.png)

除了针对ESXi进行加密破坏外，攻击者还会收集并窃取企业的敏感文件，并通过开源的云存储管理工具Rclone，将数据上传至境外相关网盘。

![](https://blog.nsfocus.net/wp-content/uploads/2022/12/wps_doc_13-1-300x225.png)

攻击者在Rclone相关配置文件中，定义了文件上传范围、上传接口、日志信息等参数信息。

![](https://blog.nsfocus.net/wp-content/uploads/2022/12/wps_doc_14-1-300x198.png)

## ****四、安全建议****

* 关注VMware虚拟化平台高危漏洞相关情报，评估ESXi、vCenter的安全性及补丁情况；
* 通过配置ACL，在网络层限制对ESXi、vCenter相关管理端口（如：22、443等）的访问；
* 加强对于内部相关安全软件或设备告警的巡检，重点关注横向移动相关攻击；
* 通过网络管理系统或全流量监测系统，对于内部主机的异常流量进行监测告警；
* 对内部员工按岗位进行定向安全意识培训，并定期通过演练方式进行加强与提升；
* 逐步健全数据分级分类规则，加强对于重要业务系统的数据备份与应急演练。

****声明****

本安全公告仅用来描述可能存在的安全问题，绿盟科技不为此安全公告提供任何保证或承诺。由于传播、利用此安全公告所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，绿盟科技以及安全公告作者不为此承担任何责任。

绿盟科技拥有对此安全公告的修改和解释权。如欲转载或传播此安全公告，必须保证此安全公告的完整性，包括版权声明等全部内容。未经绿盟科技允许，不得任意修改或者增减此安全公告内容，不得以任何方式将其用于商业目的。

Spread the word. Share this post!

[Previous](https://blog.nsfocus.net/cacti%EF%BC%88cve-2022-46169%EF%BC%89/)

[Next](https://blog.nsfocus.net/google-chrome-v8cve-2022-4262/)

### Meet The Author

绿盟科技

咨询与合作：nsmagazine@nsfocus.com

* [绿盟科技官网](https://www.nsfocus.com.cn)
* [绿盟威胁情报中心（NTI）](https://nti.nsfocus.com)
* [绿盟云](https://cloud.nsfocus.com)