---
title: 【TrustZone相关漏洞导读】Glitched on Earth by Humans
url: https://mp.weixin.qq.com/s?__biz=MzkyMzAwMDEyNg==&mid=2247534924&idx=4&sn=f5a83697da74ed3e41697c47cc94c8e3&chksm=c1e9c51df69e4c0b83839e8f5a755f8ccd6680911ad11479e7cad9c43172e1383b54edf2a378&scene=58&subscene=0#rd
source: 关键基础设施安全应急响应中心
date: 2023-02-26
fetch_date: 2025-10-04T08:09:08.675682
---

# 【TrustZone相关漏洞导读】Glitched on Earth by Humans

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogvjjHVKUr4osSBL988X0cnBQCdzZGyTe5TAIVVpOMkicqqAx5c4w9iaz4TTw5JTuLolbPZbA4Bj4u7w/0?wx_fmt=jpeg)

# 【TrustZone相关漏洞导读】Glitched on Earth by Humans

关键基础设施安全应急响应中心

* ![](https://mmbiz.qpic.cn/mmbiz_png/eEicdLAdfSLIia4BNIIEia7V58fqeEufa10v8Vv9Pqnp3Awp03hibNByQem0PfX8XGAfYljagUP3Csbj7rhBkLwODA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

议题名称：Glitched on Earth by Humans: A Black-Box Security Evaluation of the SpaceX Starlink User Terminal (2022.08)[1]

议题视频：https://www.youtube.com/watch?v=NXqLMmGwJm0 (2022.11)[2]

议题作者：Lennert Wouters（伦纳特·沃特斯）

破解目标：Starlink 天线锅盖（Version Before 2021.04.16） 本地获取 rootshell

目标固件：未公开

主要漏洞：未在安全启动过程中添加针对故障注入的防护代码

利用方法：烧写flash替换固件，并进行电压故障注入攻击BL1的启动校验

利用代码：修改的固件未公开，但自研的modchip(故障注入设备)公开了设计：KULeuven-COSIC/Starlink-FI[3]

## **作者**

根据Linkedin资料显示，Lennert Wouters[4]（伦纳特·沃特斯 @LennertWo[5]），来自比利时，90年左右生人，目前30岁左右。本硕博均就读于比利时鲁汶大学（KU Leuven），目前为鲁汶大学 COSIC（Computer Security and Industrial Cryptography group）小组 [6]的安全研究员。虽然他目前工作于高校中，并且也有不少的论文成果[7]，但他并不局限于象牙塔派的抽象工作，同时也是一个真正的实战破解高手。除了本次让他登上BlackHat和DEF CON的星链破解工作以外，他还曾完成近场蓝牙解锁任意特斯拉汽车的破解，并以此登上 DEF CON 29 Car Hacking Village，议题为 My other car is your car[8]：

> Youtube: COSIC researchers hack Tesla Model X key fob[9]

![](https://mmbiz.qpic.cn/mmbiz_png/eEicdLAdfSLIia4BNIIEia7V58fqeEufa10yxpwDEQrBeicNqcO2OQIK8ImFQUltyTUXu7RDr1kM32bkFsWmC9o2bA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

这个议题也来过中国：[GoGoHack 2022: 我的另一辆车是你的车——黑掉特斯拉ModelX无钥匙进入系统](https://mp.weixin.qq.com/s?__biz=Mzg4Mzc2MTY1Mg==&mid=2247483769&idx=1&sn=390e640918e778e2fe05afd1185dd20c&scene=21#wechat_redirect "GoGoHack 2022: 我的另一辆车是你的车——黑掉特斯拉ModelX无钥匙进入系统")，听下来就可以发现，他这次破解特斯拉的手法真是太朋克了！破解本身复用了特斯拉中控主板和车钥匙自身的软件逻辑，所以Lennert给他们都焊到一起，彻底复用硬件完成攻击。相当于拆一个自己的特斯拉，然后打别人的特斯拉，也可以说是用特斯拉打特斯拉：

![](https://mmbiz.qpic.cn/mmbiz_png/eEicdLAdfSLIia4BNIIEia7V58fqeEufa103EUrOzPjnApnGcrhS01Ycg4jJsn2lVibbpjVdSeFvZK667I1Fz2Yeng/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

其他中文报道：

* • 比利时鲁汶大学科技大牛25€破解星链！曾90秒成功解锁特斯拉车锁密钥[10]
* • 马斯克的Space X卫星被破解，25美元的工具就能入侵终端[11]
* • 花170元黑掉马斯克星链终端，黑客公开自制工具[12]
* • 特斯拉车钥匙又被黑，10秒钟就能开走Model Y[13]
* • Tesla Model X无钥匙进入系统及固件升级漏洞[14]

# **背景**

我们对星链可能有些陌生，星链主要有两个设备，一个锅盖天线，一个路由器，二者网线相连。锅放房顶，路由器放屋里，因此可把锅类比为光猫，锅接出来的网线连到路由器的wan口上即可。锅盖和路由器主系统都是Linux，其中星链二代路由器的固件全部开源：starlink-wifi-gen2[15]，并且开启了SSH，但其只支持私钥登录，私钥未公开，因此我们也无法登录路由器的shell（博客：Starlink: First Impressions[16]）。然而，开源的路由器并不是我们关注的目标，路由器也没什么特别的，破解的目标是锅盖天线。因为锅盖负责与星链的卫星进行通信，因此在本地拿到锅盖的root shell，是继续深入分析锅盖与卫星间通信链路的前提：

* • 星链Starlink中文开箱测评 华语开箱星链第一人 安装配置测速[17]
* • 太空Wifi有多快？STARLINK RV二代星链房车版野外速度测试/开箱/安装[18]

![](https://mmbiz.qpic.cn/mmbiz_png/eEicdLAdfSLIia4BNIIEia7V58fqeEufa10WOprC82KSIj7H834gF9W79FibjJRVCCBbtG9ibiasTcRkb2NKrBzkmwag/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

Lennert Wouters通过替换固件并进行故障注入，最终在本地拿到了锅盖的root shell：

![](https://mmbiz.qpic.cn/mmbiz_png/eEicdLAdfSLIia4BNIIEia7V58fqeEufa10JAXTiasGcvb603TNWBMR2EHIq2Z921XxQaibChReAgf6dRoZ7gWhFfnQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

有了root shell，我们即可调试分析锅盖上的业务与驱动程序，对锅盖与卫星的通信协议进行逆向，最终达到破解协议、扩展攻击路径等更深入的破解工作：

![](https://mmbiz.qpic.cn/mmbiz_png/eEicdLAdfSLIia4BNIIEia7V58fqeEufa10WcaSib7GUlwu6icvDA4vteGr5sll3gGNJ160vY27HMxMVkq9eDXlCnKA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

# **破解**

在早期版本的锅盖中，串口连上就是Linux shell，有输出，但是关闭了输入：

![](https://mmbiz.qpic.cn/mmbiz_png/eEicdLAdfSLIia4BNIIEia7V58fqeEufa10oqJHCuBibF6vr8h4XGScPvCXYcIcZd0wqopA3QY4f5Zb3FZplqDBFdw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_png/eEicdLAdfSLIia4BNIIEia7V58fqeEufa10svOFuIYkbj0cuSkU9KiadQCd1pT0qjD13FiaTckPwJC4LtmSPl2IHib0A/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

Lennert Wouters的破解方法就是通过飞线烧写设备上的FLASH，将原始固件替换为打开串口输入的恶意固件。但由于安全启动的存在，恶意固件无法通过启动校验。因此还需要在启动过程进行电压故障注入，跳过固件校验的代码逻辑，才能获得设备的root shell。整个破解过程中最有特色的是他设计并开源了一个针对锅的故障注入设备，游戏机破解行当多称其为modchip：

> 此modchip的PCB和软件操控代码均开源：KULeuven-COSIC/Starlink-FI[19]

![](https://mmbiz.qpic.cn/mmbiz_jpg/eEicdLAdfSLIia4BNIIEia7V58fqeEufa10lbxtVSYBMctTj5ICqpSPdkfEiaYqoa1E9tErKMVx0dOTqUMpzFu4Cgw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

此modchip的使用方式大概如下：

![](https://mmbiz.qpic.cn/mmbiz_png/eEicdLAdfSLIia4BNIIEia7V58fqeEufa10S8rqe0nPwYPdfnhOGMn2tP1D4kGAEjwr1wGeXIiaKicWnmngFxxu3aLA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

既然作者给出了故障注入设备的PCB和软件操控代码，那这个破解好复现么？整个破解过程简单来说，就是利用故障注入攻击安全启动，进而启动可以拿到root shell恶意固件。然而这个的恶意固件是怎么修改出来的，Lennert Wouters基本没提，也没有公开出patch好的固件，因此这个破解不能无脑复现：

![](https://mmbiz.qpic.cn/mmbiz_png/eEicdLAdfSLIia4BNIIEia7V58fqeEufa10iavZ5h1yrgL9Nqic8TNcAl8nf5IiaK19T9fyaqqiahs9iadpDIoENQFj8Ig/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

并且星链锅盖的固件甚至无法在网络上找到，只能从设备的FLASH上读出：

> 只找到固件版本跟踪网站Starlink Firmware[20]，只有版本号，没有固件本体

![](https://mmbiz.qpic.cn/mmbiz_png/eEicdLAdfSLIia4BNIIEia7V58fqeEufa10pAwEAxMibY76rSbqkfoJcbHEcbRuc84p9ZAROfVHEpwBlcbzRqvRQPw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

因此在没有设备的情况下，想要看清整个破解的全貌都是不可能的，所以我们就更难完整的理解并复现这个破解。

# **复现准备**

> 要复现这个破解还有一些麻烦事，首先是要找到串口有输出的老版本锅盖。然后还有就是星链的业务遍布全球，不同国家版本的星链锅盖可能还会有细节上的不同，因此设备情况可能与破解示例有所差异，这或许也会给复现带来一些困惑。由于我还没缘分碰到设备，因此目前我只能以公开的TF-A和StarLink开源的u-boot为起点，做一些复现的准备工作。

从原理上，整个破解的过程主要有两步，首先是先patch固件并烧写回FLASH，然后进行再故障注入。FLASH中固件的组织方式可以参考：SpaceX StarLink 星链卫星固件提取研究[21]，可见其安全启动的实现就是开源的TF-A（也即ATF），经过分析我们确认了他的具体打法：

> 和checkm8、checkm30这种打手机root的方法一样，就是逐级patch

* • Patch：从BL2内容证书开始patch，直至BL33
* • Glitch：打BL1校验BL2内容证书

![](https://mmbiz.qpic.cn/mmbiz_png/eEicdLAdfSLIia4BNIIEia7V58fqeEufa10Eia2ILv0fpHPiaYWcCu1cicNhEdlyNicRxzMkdsc7P9wdthyLibOPjlWO8g/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

具体来说patch的主要有三部分：

1. 1. BL2内容证书：SHA512的hash数据
2. 2. BL2：校验BL33的代码位点
3. 3. BL33：开启串口输入、默认启动shell

### patch BL2

> 目前无固件

首先来说BL2固件的patch，因为BL2内容证书的patch依赖于BL2固件的SHA512。经过分析只要把auth\_mod\_verify\_img[22]这个函数patch成返回0即可跳过所有校验：

![](https://mmbiz.qpic.cn/mmbiz_png/eEicdLAdfSLIia4BNIIEia7V58fqeEufa10gJw3EI5UHzuNKPv7ialw1iasM3R959Yu4icr7bOjphTPlH588WM8ibQiaRw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

所以BL2往后的一切证书相关的校验数据都作废了：

![](https://mmbiz.qpic.cn/mmbiz_png/eEicdLAdfSLIia4BNIIEia7V58fqeEufa10Eia2ILv0fpHPiaYWcCu1cicNhEdlyNicRxzMkdsc7P9wdthyLibOPjlWO8g/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

### **patch BL2 内容证书**

> 目前无固件

BL1校验BL2的过程主要有两步：

1. 1. 首先校验BL2内容证书的签名
2. 2. 然后校验BL2内容证书中的hash与BL2固件的hash是否一致

当我们修改完BL2时，内容证书中的hash与BL2固件不一致，校验不通过，因此故障注入的位置有两种选择：

1. 1. 修改BL2内容证书中的hash，故障注入BL1对BL2内容证书的签名校验
2. 2. 不修改BL2内容证书，故障注入BL1对BL2固件的hash校验

![](https://mmbiz.qpic.cn/mmbiz_png/eEicdLAdfSLIia4BNIIEia7V58fqeEufa10T3ZmpVtibIOFic1icFWLZqQxt2zTlR6UytuJGIib8d9Gicn1ucgPhiawzG5g/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

最终他根据测试结果发现，第一种选择，即修改BL2内容证书中的hash并通过故障注入跳过BL2内容证书的签名校验的成功率较高。因此按照第一种选择，我们需要在固件中找到这144字节的证书，并修改其中的hash数据为patch后BL2的SHA512，因此这个patch是在patch完BL2之后才能进行：

![](https://mmbiz.qpic.cn/mmbiz_png/eEicdLAdfSLIia4BNIIEia7V58fqeEufa10lEWR6OAsyaKDxqRsPaE5FSlB8ZFibeJASia3jDqVXjfCWrU8C222ulEw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

### **patch BL33（u-boot)**

> 锅的u-boot开源了，但是太奇怪了，spacex把修改过的u-boot放在仓库的release[23]中了，所以你直在目标仓库里搜相关头文件如spacex\_catson\_boot.h是搜不到的...

用版本号为7左右的gcc：gcc-linaro-7.1.1-2017.05-x86\_64\_aarch64-linux-gnu.tar.xz[24]

```
➜  wget https://github.com/SpaceExplorationTechnologies/u-boot/archive/refs/tags/sx_2020_11_25.tar.gz ➜  tar -xvzf ./u-boot-sx_2020_11_25.tar.gz➜  cd u-boot-sx_2020_11_25
➜  git init➜  git add .➜  git commit -m "1"
➜  make SPACEX_CATSON_UTERM_EMMC_defconfig ➜  make ARCH=arm CROSS_COMPILE=/mnt/disk2/starlink/gcc-linaro-7.1.1-2017.05-x86_64_aarch64-linux-gnu/bin/aarch64-linux-gnu- -j `nproc`
➜  lsapi        drivers   Licenses     test                u-boot.maparch       dts       MAINTAINERS  tools               u-boot-nodtb.binboard      env       Makefile     u-boot              uboot.patchcmd        examples  net          u-boot.bin          u-boot.sreccommon     fs        post         u-boot.cfg          u-boot.symconfig.mk  include   README       u-boot.cfg.configsconfigs    Kbuild    scripts      u-boot.dtbdisk       Kconfig   spacex       u-boot-dtb.bindoc        lib       System.map   u-boot.lds➜  file u-boot      u-boot: ELF 64-bit LSB executable...