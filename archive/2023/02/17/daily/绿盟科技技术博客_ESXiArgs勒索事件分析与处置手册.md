---
title: ESXiArgs勒索事件分析与处置手册
url: http://blog.nsfocus.net/esxiargs/
source: 绿盟科技技术博客
date: 2023-02-17
fetch_date: 2025-10-04T06:52:36.687284
---

# ESXiArgs勒索事件分析与处置手册

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

# ESXiArgs勒索事件分析与处置手册

### ESXiArgs勒索事件分析与处置手册

[2023-02-16](https://blog.nsfocus.net/esxiargs/ "ESXiArgs勒索事件分析与处置手册")[绿盟科技](https://blog.nsfocus.net/author/nsfocus/ "View all posts by 绿盟科技")

阅读： 1,858

## ****一、事件********概述****

绿盟科技CERT近期监测到，欧洲多个安全机构发布了ESXiArgs勒索病毒的攻击预警，该病毒利用2021年披露的ESXi远程溢出漏洞（CVE-2021-21974）进行传播，根据网络空间测绘平台的数据统计，目前全球已有1800余台主机被感染，且绝大部分均分布于欧美等国家。

勒索病毒执行后，将对指定后缀的虚拟机相关文件进行加密，同时生成args后缀的文件，用来保存加密相应文件时使用的参数。

![](https://blog.nsfocus.net/wp-content/uploads/2023/02/wps_doc_2-4-300x166.png)

通过对感染主机勒索信的统计分析，确认此次攻击事件系同一黑产团伙所为；通过对ESXi版本的统计分析，以及漏洞代码对比分析，确认此次事件涉及漏洞影响的版本，除VMware官方公布的以外，还包括ESXi 5.5及6.0；通过对病毒样本分析，发现在加密大文件时存在缺陷，可通过对磁盘描述文件进行重建，并结合数据恢复软件，即可恢复被加密磁盘中的文件。

## ****二、事件时间线****

2021年2月23日 ，VMware发布CVE-2021-21974漏洞相关产品补丁，涉及的ESXi 版本包括6.5、6.7及7.0。

![](https://blog.nsfocus.net/wp-content/uploads/2023/02/wps_doc_3-3-300x83.png)

2021年5月25日，国外安全研究人员在其个人博客公布了该漏洞细节及详细分析过程，并提供了针对ESXi 6.7指定版本的漏洞利用代码。

2023年2月4日法国互联网应急中心（CERT-FR）发布了此次勒索病毒攻击事件的相关预警，包括攻击涉及的漏洞信息。

![](https://blog.nsfocus.net/wp-content/uploads/2023/02/wps_doc_4-2-300x120.png)

2月5日意大利国家网络安全局（ACN）发布预警，警告有黑客利用ESXi漏洞对全球数千台服务器进行攻击。

2月7日绿盟科技CERT监测到此次攻击事件，并开始跟踪分析。

2月8日美国网络安全和基础设施安全局（CISA）发布了ESXiArgs勒索病毒恢复脚本，以协助受害用户恢复被加密的虚拟机。

![](https://blog.nsfocus.net/wp-content/uploads/2023/02/wps_doc_5-3-300x109.png)

## ****三、漏洞********分析****

CVE-2021-21974是由ESXi的SLP（Service Location Protocol）服务中的堆溢出问题引起。SLP是一个网络服务，默认监听TCP/UDP 427端口，且无需认证即可远程访问。

漏洞源自SLPParseSrvUrl函数，在[1]处SLPParseSrvUrl函数内部调用了calloc函数申请URL的长度加上0x1d大小的内存，在[2]处调用了strstr函数来查找子字符串“:/”在 URL中的位置，并在第[3]处将子字符串“:/”之前的URL内容复制到[1]处calloc函数申请的内存中。由于param\_2实际为来自网络输入，就可能导致在[3]处复制时，复制数据的大小大于[1]处申请内存的大小，引发堆溢出，最终导致漏洞产生。

![](https://blog.nsfocus.net/wp-content/uploads/2023/02/wps_doc_6-2-300x218.png)

通过对感染主机ESXi版本的统计分析，发现此次事件涉及的ESXi版本还包括5.5及6.0；通过对比5.5及6.7版本代码，确认5.5版本同样存在该漏洞。

![](https://blog.nsfocus.net/wp-content/uploads/2023/02/wps_doc_7-2-300x200.png)

通过修改公开的漏洞利用代码，成功在ESXi 5.5上复现了该漏洞。

![](https://blog.nsfocus.net/wp-content/uploads/2023/02/wps_doc_8-2-300x181.png)

VMware公布的产品生命周期中，ESXi 5.5及6.0的技术支持截止时间分别为2018年9月及2020年3月。

![](https://blog.nsfocus.net/wp-content/uploads/2023/02/wps_doc_9-2-300x133.png)

通过对ESXi补丁信息检索，证实在上述时间点后，官方并未再发布上述产品的任何安全补丁。

![](https://blog.nsfocus.net/wp-content/uploads/2023/02/wps_doc_10-2-300x126.png)

## ****四、样本分析****

ESXiArgs勒索程序使用RSA+sosemanuk的组合加密算法进行加密，但本身功能简单，只具备加密单个文件的能力，因此攻击者将勒索程序与shell脚本结合使用，通过shell脚本实现批量文件加密、修改系统文件、清理日志及自身文件等功能。

* **勒索程序分析**

样本为Linux 64位可执行程序，在相关威胁情报平台上，该样本的最早上传时间为2023年2月4日。

![](https://blog.nsfocus.net/wp-content/uploads/2023/02/wps_doc_11-2-300x119.png)

样本运行时，需要提供指定参数，其中公钥文件<publibc\_key>和加密文件路径<file\_to\_encrypt>是必选参数，可选参数包括：

* enc\_step：加密文件时，每个加密数据块的间隔；
* enc\_size：指定每个加密数据块的大小；
* file\_size：指定文件大小，当文件大小小于file\_size时，则加密整个文件；文件大小大于file\_size时，最多加密file\_size的大小，该参数默认值为0，因此如果不指定大于0的值，则不进行加密。

![](https://blog.nsfocus.net/wp-content/uploads/2023/02/wps_doc_12-1-300x43.png)

该勒索程序使用非对称加密RSA+对称加密sosemanuk算法，完成整个文件加密流程。

![](https://blog.nsfocus.net/wp-content/uploads/2023/02/wps_doc_13-1-300x127.png)

勒索程序本身不具备目录遍历功能，每次只能加密一个文件，每次运行生成新的sosemanuk流密钥。将生成的sosemanuk流密钥使用RSA公钥加密，在完成文件加密后写入到原文件末尾。

![](https://blog.nsfocus.net/wp-content/uploads/2023/02/wps_doc_14-1-300x95.png)

加密代码的本意是在加密大文件时，只加密指定的大小，不加密全部文件，但此处代码存在bug，导致当file\_size参数为缺省状态时，则不进行加密。

![](https://blog.nsfocus.net/wp-content/uploads/2023/02/wps_doc_15-1-300x255.png)

此外，勒索程序在获取file\_size参数时使用了atoi函数，导致获取到的最大值为0xffff ffff，因此只能正确加密4GB以内的文件。

如果文件等于4GB（0x1 0000 0000）那么高位丢失，加密0个字节，在文件尾写入密钥数据（由于勒索脚本使用du -k命令获取文件大小，因此file\_size比实际文件更大）；如果文件大于4G，则加密size=文件大小&0xffff ffff，在文件尾写入密钥数据。

![](https://blog.nsfocus.net/wp-content/uploads/2023/02/wps_doc_16-1-300x165.png)

如原本5G（0x140002000）大小的文件，由于高位丢失导致文件大小变成1G（0x40002000）。

![](https://blog.nsfocus.net/wp-content/uploads/2023/02/wps_doc_17-1-300x198.png)

每次加密块的大小由enc\_size指定（样本中为1MB），如果文件刚好是4GB多一个字节，那么处理一个加密块，即加密文件头部1MB数据。当加密size大于enc\_size时，由enc\_step指定间隔，实现文件数据间断加密。

![](https://blog.nsfocus.net/wp-content/uploads/2023/02/wps_doc_18-1-300x273.png)

加密完成后ESXi中相关原文件被加密，同时生成对应的\*.args文件用来保存加密时使用的参数。

![](https://blog.nsfocus.net/wp-content/uploads/2023/02/wps_doc_19-1-300x54.png)

该勒索程序不存在文件释放或其他驻留行为，仅使用传统的文件加密，要完成整个勒索攻击还需要配合脚本执行，属于完成度很低的勒索程序。

* **勒索脚本分析**

勒索脚本包含修改ESXi配置、结束虚拟机进程、启动加密程序、替换index.html文件、替换/etc/motd文件、清理自身痕迹、修改文件时间等功能。

首先通过遍历/vmfs/volumes，寻找指定后缀名的文件进行加密，包括：\*.vmdk、\*.vmx、 \*.vmxf、\*.vmsd、\*.vmsn、\*.vswp、\*.vmss、\*.nvram、\*.vmem。

![](https://blog.nsfocus.net/wp-content/uploads/2023/02/wps_doc_20-1-300x80.png)

在替换index.html和/etc/motd文件时，会先进行备份。

![](https://blog.nsfocus.net/wp-content/uploads/2023/02/wps_doc_21-300x88.png)

修改虚拟机配置文件，并结束虚拟机进程。

![](https://blog.nsfocus.net/wp-content/uploads/2023/02/wps_doc_22-300x62.png)

查找以\*.log结尾的日志文件并删除，之后等待加密程序结束，再执行后续功能。

![](https://blog.nsfocus.net/wp-content/uploads/2023/02/wps_doc_23-300x80.png)

恢复/sbin/hostd-probe文件，并将其修改和访问时间更新为busybox文件时间。

![](https://blog.nsfocus.net/wp-content/uploads/2023/02/wps_doc_24-300x41.png)

恢复计划任务文件/var/spool/cron/crontabs/root，删除原文件的最后一行和1-8行。

![](https://blog.nsfocus.net/wp-content/uploads/2023/02/wps_doc_27-300x25.png)

再次删除/bin/hostd-probe.sh文件的第一行。

![](https://blog.nsfocus.net/wp-content/uploads/2023/02/wps_doc_26-300x18.png)

删除/store/packages/vmtools.py并恢复/etc/vmware/rhttpproxy/endpoints.conf，同时清空/etc/rc.local.d/local.sh。

![](https://blog.nsfocus.net/wp-content/uploads/2023/02/wps_doc_28-300x25.png)

更新/etc/vmware/rhttpproxy/endpoints.conf、/bin/hostd-probe.sh、/etc/rc.local.d/local.sh文件的修改和访问时间。

![](https://blog.nsfocus.net/wp-content/uploads/2023/02/wps_doc_28-300x25.png)

最后删除自身文件，并启动SSH服务。

![](https://blog.nsfocus.net/wp-content/uploads/2023/02/wps_doc_29-300x22.png)

## ****五、加密文件恢复****

虚拟机的每个磁盘驱动器都包含了一对\*.vmdk文件，其中一个为文本文件（如：test.vmdk），包含虚拟硬盘的描述数据，另一个则是磁盘的实际数据文件（如：test-flat.vmdk）。这些数据是以二进制形式存放在物理磁盘上的，描述文件（如：test.vmdk）就是用于描述这种映射关系的。

而描述文件（如：test.vmdk），可通过实际数据文件（如：test-flat.vmdk）进行重建恢复。VMWare对此提供了详细方法：<https://kb.vmware.com/s/article/1002511?lang=zh_CN>。美国网络安全和基础设施安全局（CISA）提供了恢复脚本：https://github.com/cisagov/ESXiArgs-Recover。ESXiArgs-Recover脚本的核心功能就是将描述文件的重建过程自动化。

由于ESXiArgs勒索程序本身缺陷，导致只能对大文件的前4GB数据进行间断加密，因此文件越大被加密的数据量就越少，被恢复的可能性也就越大，而ESXi中的磁盘文件实际大小往往为几十G、几百G。

* **ESXiArgs-Recover**

恢复脚本（ESXiArgs-Recover）主要功能为恢复vmx配置文件和重建磁盘描述文件。

1. 恢复配置文件

运行状态的虚拟机会自动生成一个\*.vmx~文件作为原始配置文件的备份，由于\*.vmx~后缀并不在加密范围内，因此通过重命名\*.vmx~文件即可恢复虚拟机配置；但如果虚拟机为关机或暂停状态，则不存在\*.vmx~文件，也就无法恢复配置文件，这种情况可根据虚拟机原始配置，重新创建配置文件即可。

![](https://blog.nsfocus.net/wp-content/uploads/2023/02/wps_doc_30-300x143.png)

2. 重建磁盘描述文件

恢复脚本（ESXiArgs-Recover）可自动化完成磁盘描述文件的重建，但由于磁盘文件大小及加密情况不同，部分虚拟机在执行恢复脚本后，可能无法正常引导开机。

![](https://blog.nsfocus.net/wp-content/uploads/2023/02/wps_doc_31-300x88.png)

* **数据恢复软件**

对于使用恢复脚本（ESXiArgs-Recover）后无法正常引导开机的虚拟机，可将恢复后的磁盘文件挂载到其他Windows虚拟机中，并通过数据恢复软件（如：R-Studio）恢复磁盘中文件。

首先在挂载的磁盘上执行分区搜索操作，恢复损坏的分区表信息。

![](https://blog.nsfocus.net/wp-c...