---
title: Ransom Cartel勒索软件与REvil的可能联系
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247553026&idx=2&sn=06db7e35c104c8e101677df1df77bf5f&chksm=e915c038de62492e75b473222436112b8f26cb3a45210f4808a5fe7fea1711c1461226b301e5&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2022-11-02
fetch_date: 2025-10-03T21:33:31.619753
---

# Ransom Cartel勒索软件与REvil的可能联系

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2icdfC8sTj6RK9fQeawzic2IVf4XovEULNlN8ylzup5Yx80QrbJ7wm1ia6r2U71sF8sDib1UkFdMvRsiag/0?wx_fmt=jpeg)

# Ransom Cartel勒索软件与REvil的可能联系

xiaohui

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

Ransom Cartel是在2021年12月才被发现的勒索软件即服务 (RaaS)。此勒索软件执行双重勒索攻击，并与REvil勒索软件表现出一些相似之处和技术重叠。从时间维度来说，Ransom Cartel是在REvil勒索软件消失后几个月出现的。当Ransom Cartel首次出现时，尚不清楚是REvil的重现还是重用或模仿REvil代码。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icdfC8sTj6RK9fQeawzic2IV9hbsRBwHrwnXpiclmnGwZ8dia38S7CExPZRecFwLnAKG9jRCNyicpJTVg/640?wx_fmt=png)REvil消失的历史

2021年10月，REvil运营商突然中止，其暗网泄露网站也突然无法访问。大约在2022年4月中旬，个别安全研究人员和网络安全媒体报道了REvil的一项新进展，这可能意味着该组织的回归。REvil在dnpscnbaix6nkwvystl3yxglz7nteicqrou3t75tpcc5532cztc46qyd[.]onion和aplebzu47wgazapdqks6vrcv6zcnjppkbxbr6wketf56nf6aq2nmyoyd[.]onion开始将用户重定向到blogxxu75w63ujqarv476otld7cyjkq4yoswzt4ijadkjwvg3vrvd5yd[.]onion/Blog。

同一天晚些时候，重定向被删除。当时，还无法确定是哪个组织发起了重定向，因为这个新的重定向网站并没有显示任何名字或隶属关系。

在重定向开始时，网站上没有列出任何违规组织。随着时间的推移，攻击者开始添加出现在 重定向网站上的记录，大部分是在2021年4月下旬至10月期间。他们还包括以前REvil使用的文件共享链接作为攻击的证据。

新的重定向网站列出了Tox Chat ID，用于与勒索软件运营商进行通信。该网站暗示其运营商与REvil的联系，并声称该新组织提供了 “相同但经过改进的软件”。

unit42最初认为该网站与Ransom Cartel有关，攻击者提到的 “改进软件” 是新的Ransom Cartel变体。然而，在进一步分析和看到更多证据后，研究人员认为这和Ransom Cartel毫无任何关系。

无论新的重定向网站是由Ransom Cartel还是由其他组织运营的，很明显的是，尽管REvil可能已经消失，但其恶意影响力并未消失。新成立的组织似乎可以访问REvil或与其建立联系。同时，我们对Ransom Cartel样本的分析 (在下面的部分中详细介绍) 也提供了与REvil有关的有力证据。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icdfC8sTj6RK9fQeawzic2IV9hbsRBwHrwnXpiclmnGwZ8dia38S7CExPZRecFwLnAKG9jRCNyicpJTVg/640?wx_fmt=png)Ransom Cartel概述

研究人员大约在2022年1月中旬第一次观察到Ransom Cartel。MalwareHunterTeam的安全研究人员认为，该组织至少自2021年12月以来一直活跃。他们观察到第一个已知的Ransom Cartel活动，并注意到与REvil勒索软件的一些相似之处和技术重叠。

关于Ransom Cartel的起源有许多猜测。其中一种猜测是，Ransom Cartel可能是多个组织融合的结果。然而，MalwareHunterTeam的研究人员提出，其中一个被认为已经合并的组织否认与Ransom Cartel有任何联系。此外，unit42发现其中许多组织与REvil有联系外，没有发现这些组织与Ransom Cartel有联系。

目前，研究人员认为Ransom Cartel运营商可以访问REvil ransomware的早期版本的源代码，但不能访问一些最新的开发 (有关更多详细信息，请参阅Ransom Cartel和REvil代码比较)。这表明，在某种程度上，这些组织之间存在着某种关系，尽管这种关系可能不是最近才出现的。

unit42还观察到Ransom Cartel组织的攻击目标，2022年1月左右在美国和法国观察到第一个已知的受害者。Ransom Cartel攻击了以下行业的企业: 教育，制造业，公用事业和能源。unit42事件响应者还协助客户在几起Ransom Cartel案件中做出反应。

像许多其他勒索软件组织一样，Ransom Cartel利用双重勒索技术。unit42观察到该组织采取了更激进的态度，威胁不仅要将窃取的数据发布到他们的泄露网站上，还会将数据发送给受害者的合作伙伴、竞争对手和新闻媒体，以造成名誉损害。

Ransom Cartel通常通过被破坏的凭证获得对环境的初始访问权，这是勒索软件运营商初始访问的最常见途径之一。这包括外部远程服务、远程桌面协议 (RDP) 、安全shell协议 (SSH) 和虚拟专用网络 (vpn) 的访问凭证。这些凭证在网络黑市中被广泛可用，并为攻击者提供了一种可靠的手段来访问受害者的公司网络。

这些凭据也可以通过勒索软件运营商本身的活动或通过从初始访问代理购买来获得。

初始访问代理是提供出售受损网络访问的攻击者。他们的动机不是自己进行网络攻击，而是向其他攻击者出售访问权限。由于勒索软件的盈利能力，这些代理可能会根据他们愿意支付的金额与RaaS组织建立合作关系。

unit42已经发现Ransom Cartel依靠这种类型的服务来获得对勒索软件部署的初始访问权限的证据。Unit 42还观察到Ransom Cartel在攻击企业网络时对Windows和Linux VMWare ESXi服务器进行加密。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icdfC8sTj6RK9fQeawzic2IV9hbsRBwHrwnXpiclmnGwZ8dia38S7CExPZRecFwLnAKG9jRCNyicpJTVg/640?wx_fmt=png)在Ransom Cartel攻击中观察到的战术、技术和程序

unit42使用一种名为DonPAPI的工具观察到一名Ransom Cartel攻击者，这种工具在过去的事件中从未被发现过。该工具可以定位和检索Windows数据保护API (DPAPI)受保护的凭证，这被称为DPAPI转储。

DonPAPI用于搜索设备上已知为DPAPI blob的某些文件，包括Wi-Fi密钥、RDP密码、保存在web浏览器中的凭证等。为了避免被反病毒(av)或终端检测和响应(EDR)检测到的风险，该工具下载文件并在本地解密。为了破坏Linux ESXi设备，Ransom Cartel使用DonPAPI获取存储在web浏览器中的凭据，用于对vCenter web界面进行认证。

研究人员还观察到攻击者使用了其他工具，包括恢复本地存储的凭据的LaZagne和从主机内存窃取凭据的Mimikatz。

为了建立对Linux ESXi设备的持久访问，攻击者在对vCenter进行身份验证后启用SSH。攻击者将创建新的帐户，并将帐户的用户标识符(UID)设置为零。对于Unix/Linux用户，UID=0表示root。这意味着任何安全检查都被绕过了。

据观察，该攻击者正在下载并使用一种名为PDQ Inventory的合法工具的破解版本。PDQ Inventory是一种合法的系统管理解决方案，IT管理员可以使用它扫描他们的网络，收集硬件、软件和Windows配置数据。Ransom Cartel利用它作为远程访问工具，建立交互式命令和控制通道，并扫描受感染的网络。

一旦VMware ESXi服务器被破坏，攻击者将启动加密器，它将自动枚举正在运行的虚拟机(vm)，并使用esxcli命令关闭它们。通过终止虚拟机进程，可以确保勒索软件能够成功加密vmware相关文件。

在加密过程中，Ransom Cartel专门寻找具有以下文件扩展名的文件：.log， .vmdk， .vmem， .vswp和.vmsn。这些扩展与ESXi快照、日志文件、交换文件、分页文件和虚拟磁盘相关联。加密后，观察到以下文件扩展名：.zmi5z， .nwixz， .ext， .zje2m， .5vm8t和.m4tzt。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icdfC8sTj6RK9fQeawzic2IV9hbsRBwHrwnXpiclmnGwZ8dia38S7CExPZRecFwLnAKG9jRCNyicpJTVg/640?wx_fmt=png)勒索通知

unit42观察到Ransom Cartel发送的两种不同版本的勒索通知。第一个勒索通知最早是在2022年1月周围观察到的，另一个勒索通知是在2022年8月首次出现的。第二个版本似乎被完全重写了，如图1所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icdfC8sTj6RK9fQeawzic2IVQzapc7oMWf8Q5cibe85eLicMupFXm7qTicDMHgKU0LtFPpjkVkZhaK8cA/640?wx_fmt=png)

Ransom Cartel勒索通知，左边的是在2022年1月中首次观察到的，右边的是在2022年8月中首次观察到的

有趣的是，Ransom Cartel使用的第一个勒索通知的结构与REvil发送的勒索通知具有相似之处，如下图所示。除了使用类似的措辞外，两个注释都对UID采用了相同格式的16字节十六进制字符串。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icdfC8sTj6RK9fQeawzic2IVStibncbdcYcV6ezibbuX4sVxC390L9qiayicw7ia26KMlsmLbttV1xeyhqA/640?wx_fmt=png)

左侧显示的Ransom Cartel勒索通知，而右边显示的是REvil发送的勒索通知

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icdfC8sTj6RK9fQeawzic2IV9hbsRBwHrwnXpiclmnGwZ8dia38S7CExPZRecFwLnAKG9jRCNyicpJTVg/640?wx_fmt=png)Ransom Cartel TOR网站

Ransom Cartel与受害者沟通的网站可通过赎金说明中提供的TOR链接获得。我们已经观察到属于Ransom Cartel的多个TOR url，这可能表明他们一直在改变基础设施并积极开发其网站。访问网站需要一个TOR私钥。

输入密钥时，将加载以下页面：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icdfC8sTj6RK9fQeawzic2IVF1ic3KWISuQLXtf2CHJwEwYGkFZFFhfJJ6qLC87c8szf0NUibqq3VozQ/640?wx_fmt=png)

Ransom CartelTOR网站登陆页面

通过授权按钮进入TOR网站后，会出现一个屏幕，要求输入赎金通知中包含的详细信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icdfC8sTj6RK9fQeawzic2IVXOXoegsgsvibnyMvhxrqngMQpqnvOzoO81TrYgHs4q9KXmnv73Pm3vQ/640?wx_fmt=png)

Ransom Cartel网站，要求在赎金通知中提供的ID和密钥

在TOR网站上完成授权后，将出现下图所示的页面。该网站包括美元和比特币的赎金需求以及比特币钱包地址等详细信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icdfC8sTj6RK9fQeawzic2IVGg5TpuUxgYOu4TRIYWcAANPurUamlk8MBslJrVHDj034Hv9lJE92nA/640?wx_fmt=png)

Ransom CartelTOR网站

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icdfC8sTj6RK9fQeawzic2IV9hbsRBwHrwnXpiclmnGwZ8dia38S7CExPZRecFwLnAKG9jRCNyicpJTVg/640?wx_fmt=png)技术细节

在此分析中使用了两个Ransom Cartel样本:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icdfC8sTj6RK9fQeawzic2IVkRkNUoaEmqs9IBa3qY5IezvUmkBLG7IWMQA9VEZA6rzbFgNmN7lgQQ/640?wx_fmt=png)

两个样本都包含三种输出：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icdfC8sTj6RK9fQeawzic2IVuYFAH2mHoa3SIssPbdtt8IiaqauyFjxVhv7tZFwkHTYsGc1gD0WsMIg/640?wx_fmt=png)

如果不指定导出而执行DLL，则示例还包含一个DllEntryPoint。DllEntryPoint指向一个函数，该函数在对Curve25519 Donna算法的调用上迭代24次。迭代结束后，示例将查询系统指标，特别是SM\_CLEANBOOT值。如果这个值不是0，勒索软件将继续通过rundll32.exe生成自己的另一个实例，并指定Rathbuige导出。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icdfC8sTj6RK9fQeawzic2IVsDRYeSDN2bCKUQ3OAVvpZ9ibZ0iaVeIPRQuRIVxv7yBb8RT03CnWkyMQ/640?wx_fmt=png)

SM\_CLEANBOOT值

Rathbuige导出从创建以下互斥锁开始:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icdfC8sTj6RK9fQeawzic2IVpYbwgG67ItXs0tkIa3MaggYXFC0MicyGKPzvjaU1xeFVUUvicH9HwzGg/640?wx_fmt=png)

创建互斥锁后，示例开始解密并解析其嵌入式配置。该配置存储为一个base64编码的blob，其中base64编码的blob的前16个字节是RC4密钥，用于在解码后解密blob的其余部分。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icdfC8sTj6RK9fQeawzic2IV7KDcDdLFPr4SL98sBzbiaFdEDSjDILoH6agicblYia7nDELiaqYIiacfKvw/640?wx_fmt=png)

Ransom Cartel加密配置

一旦解密，该配置将以JSON格式存储，并包含诸如加密文件扩展名、攻击者的公共Curve25519-donna密钥、base64编码的赎金通知以及加密前要终止的进程和服务列表等信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icdfC8sTj6RK9fQeawzic2IVs9fZ4WHaZCkDSlicPRcN6ZXXBy5IKRVCaEzaLaxqcsGEgWicXSEia948g/640?wx_fmt=png)

解密Ransom Cartel配置示例

配置中的对应值如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icdfC8sTj6RK9fQeawzic2IVCykBqleQBeuLo0ht3dicZ2vic6AkCciac63MCumTvCojYXuMM6xr7t2Nw/640?wx_fmt=png)

配置结构

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icdfC8sTj6RK9fQeawzic2IVwn5NrSmF4hk9ichxvdib6ibql2nQhvJVoRGRRWE07KfaIrVmEZPQE8J9g/640?wx_fmt=png)

有针对性的进程列表

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icdfC8sTj6RK9fQeawzic2IVYteicTibI6G1xtaH1DYec1AfZHZKUTpR24XSzGmE5qx4mW8WdY3Kiaic0Q/640?wx_fmt=png)

有针对性的服务列表

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icdfC8sTj6RK9fQeawzic2IVDYxLPBTZ2thucLudVlQRNyJHeQCiaSHbUvbekcY67tAhUa5Sc7aFWng/640?wx_fmt=png)

避免扩展

解密配置后，将收集某些系统信息，包括用户名，计算机名称，域名，区域设置和产品名称。然后将此信息格式化为以下JSON结构:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icdfC8sTj6RK9fQeawzic2IVkRkNUoaEmqs9IBa3qY5IezvUmkBLG7IWMQA9VEZA6rzbFgNmN7lgQQ/640?wx_fmt=png)

结构内每个项的作用

![](https://...