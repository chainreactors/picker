---
title: Brute Ratel C4 Badger分析实战与检测
url: https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247487622&idx=1&sn=3fad2e28a552eb5fe43798ea8f1f0aec&chksm=902fbfaea75836b80990fa4c22183143f603a484128a0a52364a0f50573e27932e193af22851&scene=58&subscene=0#rd
source: 安全分析与研究
date: 2022-11-19
fetch_date: 2025-10-03T23:13:44.678162
---

# Brute Ratel C4 Badger分析实战与检测

![cover_image]()

# Brute Ratel C4 Badger分析实战与检测

原创

pandazhengzheng

安全分析与研究

**安全分析与研究**

专注于全球恶意软件的分析与研究

前言

一转眼，2022年已经接近尾声了，还有一个半月的时间就要到2023年了，快到年底了，又要开始做明年的技术规划以及目标制定了，安全要做的事还挺多的，黑客的攻击手法和攻击武器在不断的变化，安全研究人员也要时刻保持学习，不断进步，跟踪分析研究最新的安全攻击技术和攻击武器，最近一年己经有越来越多的新型恶意软件家族被全球各大黑客组织进行APT攻击和勒索攻击等黑客攻击活动当中，同时黑客组织也在不断更新和维护全球流行的恶意软件家族，比如像Emotet这种复杂的顶级恶意软件家族也在消失大约半年之后又开始流行起来，而且攻击态势非常猛烈。

前段时间Brute Ratel C4攻击武器平台被泄露了，对于一些新的攻击技术和攻击样本，笔者一直本着“不放过”的研究态度，只要一有时间就会去深入的分析和研究一下，就拿之前朋友发给笔者泄露的Brute Ratel C4 1.2.2版本以及两个真实的攻击案例样本进行分析与研究，供大家参考学习。

Brute Ratel C4是一款类似于Cobalt Strike的商业红队武器框架，每年License收费为2500美元，客户需要提供企业电子邮件地址并在颁发许可证之前进行验证，首个版本Brute Ratel C4 v0.2于2021年2月9日发布，它是由Mandiant和CrowdStrike的前红队队员Chetan Nayak创建的，**该工具独特之处在于它专门设计防止端点检测和响应(EDR)和防病毒(AV)软件的检测**，是一款新型的红队商业对抗性攻击模拟武器。

与Cobalt Strike的Beacon后门类似，Brute Ratel C4允许红队在远程终端主机上部署Badger后门程序，Badger连接回攻击者的命令和控制服务器，接收服务器端的命令执行相关的恶意行为。

分析

Brute Ratel C4的Badger有多种形式，包含exe、dll和shellcode等，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWUSE7rTT08xGazfe5ZNtdxDoellWKux9Bn20FwGia2jIGjesxLHmRr08B2AySdHt31VrnujJt71aQ/640?wx_fmt=png)

笔者生成HTTP通信协议类型各种不同形式的Badger后门样本，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWUSE7rTT08xGazfe5ZNtdx55ReXcIWp9wYjicPKF4Jc992k3PWp31GXSia44jgiaicjDBjG6tyl7ukoA/640?wx_fmt=png)

Brute Ratel C4的Badger还有其他三种通信协议类型：SMB、TCP、DOH，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWUSE7rTT08xGazfe5ZNtdxCJwlzkFIYmHicdflJYESDFmFGkgtrh9bVEMEQk8xXgDAWdx7IB9r8hQ/640?wx_fmt=png)

使用工具生成的Badger的ShellCode代码badger\_x64\_ret，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWUSE7rTT08xGazfe5ZNtdxbHxzT5PFbwZNxdgsjPxokE3j8DcBiaJhqZuic3Ok3iciaA7eHqLp9h28WA/640?wx_fmt=png)

前面是一大堆mov和push操作之后，跳转执行到核心函数，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWUSE7rTT08xGazfe5ZNtdxVvedNopcsZ04mwmpJXADia02DSlNZ23lickVd9KpRq8HcdQ1L6eAgokA/640?wx_fmt=png)

通过PEB标志位进行反调试，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWUSE7rTT08xGazfe5ZNtdxibgjUnuiakzB3OsNnUzkdXZ2QW901DyKLJH6vOzKVvnrUVLDkVEGwdCQ/640?wx_fmt=png)

通过对函数进行ror13 hash计算，然后对比目标函数hash找到需要的函数，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWUSE7rTT08xGazfe5ZNtdxb54r8E9prTA5E2CJfp3JUXwfx0oHgopDfRSeIUNk9JWhcv7MMVhU6w/640?wx_fmt=png)

检测函数头，是否存在int3断点(0xCC)或者是否被EDR等安全产品HOOK了(0xE9)，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWUSE7rTT08xGazfe5ZNtdxq8c52VBRDWYxqEQ48tcUqL06z3nEtw74ib5jH2XdVgFnZc0dp5LazBg/640?wx_fmt=png)

然后在内存中解密出Badger的核心代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWUSE7rTT08xGazfe5ZNtdx3m6YU4TIQiaDjXaPVmQTCHc9Zspial0N9ESgMGTj6BQMbsm5ibdSQLuRQ/640?wx_fmt=png)

解密的核心代码抺掉了文件头信息，解密之后，就可以看Brute Ratel的几个核心特征字符串信息了，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWUSE7rTT08xGazfe5ZNtdxKcYcFtLQbGliaicMcp0ibgDO0j7DUyp0ycBdAiaNeLLe30W9lic4PyIvgzA/640?wx_fmt=png)

Badger的ShellCode代码解密过程就分析完了，里面就是Badger的核心代码了，Badger的DLL和SVC服务程序，其实就是把Badger的ShellCode代码封装了一下，核心仍然是Badger的ShellCode加载代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWUSE7rTT08xGazfe5ZNtdxNJtMB58fFr1gMIyMIVKKWXHh6rLm6fzibKTibz8kQYpKYRySQcEoic6Pw/640?wx_fmt=png)

动态调试先获取指定的函数，再检测这些函数是否被EDR等安全产品HOOK了，然后再传入获取到指定函数的syscall id，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWUSE7rTT08xGazfe5ZNtdx3enRibWaU1yqIMaHkeGcy35zUYYia9SxuictG9JJRDrzNsaEbhAKlrsWA/640?wx_fmt=png)

执行相关的函数，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWUSE7rTT08xGazfe5ZNtdxDzH6p21KlNXfHI44W1pD91hIEYBjaJVHLtvyu6S1ic9k7dDOElopKvw/640?wx_fmt=png)

调用NtAllocateVirtualMemory分配指定的内存空间，然后再把Badger的ShellCode代码拷贝到该内存空间当中，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWUSE7rTT08xGazfe5ZNtdxuf3fuEvDnJ6cG8QeP41X3sR9cxSP3tu0Hh1icSYkiafYxibo7VhWx4P7Q/640?wx_fmt=png)

调用NtProtectVirtualMemory修改该内存的属性，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWUSE7rTT08xGazfe5ZNtdxyHic52caNj35LNI0nUeabRhnaSQaol72oOAYWibNXNUpkMjfKU01C5Aw/640?wx_fmt=png)

修改之后的属性为可执行，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWUSE7rTT08xGazfe5ZNtdx1PTPkHjjPqHcLVgpu1N6FVtzYyZwibSJbk72RO5TO6wOIC2nq9BIBicw/640?wx_fmt=png)

调用NtCreateThreadEx启动线程代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWUSE7rTT08xGazfe5ZNtdxqU8ztyo9tKMoibib5WQ9UANmAZu9OznSnvZd48mic3D0ciciaYibU9XlWD9g/640?wx_fmt=png)

最后调用NtWaitForSingleObject等待线程执行，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWUSE7rTT08xGazfe5ZNtdxb8wZCv593PumyMygOfwaMnic15O42icvBSx74ucOIwicTexwS7gwebIqg/640?wx_fmt=png)

后面的代码就是此前Badger的ShellCode代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWUSE7rTT08xGazfe5ZNtdxnhumtiaJpk36rKGvDSUHFsb2kbfSRG1KCEvUfN8CvqgVhyATVIPZ2Wg/640?wx_fmt=png)

到此Brute Ratel C4 Badger的Demo样本ShellCode加载器部分的代码基本就分析完成了，Badger的核心代码在后面的实战分析再进行详细分析。

事件

上面笔者利用泄露的工具生成了Brute Ratel C4 Badger的各种Demo样本，并对这些Demo样本ShellCode加载器部分代码进行了逆向分析，现在还需要去分析一些实际的攻击样本，安全研究重在实战应用，作为安全研究人员平时就要多去研究一些真实的安全攻击事件中使用的攻击样本、利用的漏洞以及最新的攻击技术，这些攻击事件中使用的各种攻击武器和攻击技术背后都是真实的黑客组织，也是最有研究价值的，因为有可能你的客户就是这些黑客组织攻击的下一个目标，也有可能在不久的将来你的客户就有可能感染这些最新的攻击武器，Brute Ratel C4虽然才出来一年多的时间，但是已经有主流的勒索病毒黑客组织和APT黑客组织开始使用Brute Ratel C4进行真实的网络攻击，下面笔者就对前段时间真实攻击案例中使用的Brute Ratel C4  Badger进行详细分析，一个是之前APT29组织攻击事件中使用的Brute Ratel真实样本，一个是Black Basta勒索病毒黑客组织攻击事件中使用的Brute Ratel真实样本。

Unit42团队捕获到一例APT29黑客组织利用Brute Ratel C4的安全事件，APT29黑客组织将代码注入到进程中加载执行解密的Brute Ratel C4 Badger的ShellCode代码，整个事件的攻击流程，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWUSE7rTT08xGazfe5ZNtdx44icNj8Jguocica4q47IIIDK2j5qCtiaal2l0Poic5BWzoyeia6v3bWrpeg/640?wx_fmt=png)

上图选自Unit42分析团队分析报告，具体的报告链接：

https://unit42.paloaltonetworks.com/brute-ratel-c4-tool/

详细分析恶意DLL样本version.dll，利用WTSEnumerateProcessesA函数枚举进程,如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWUSE7rTT08xGazfe5ZNtdxBvu8Xpy0fOeSxm0VqpPssKrEWOYiah1Ljn0sL3r4LDMb9FtTM1y42Kg/640?wx_fmt=png)

调用NtOpenProcess打开进程，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWUSE7rTT08xGazfe5ZNtdxCNpk6BIj291UOtSxeEmqicejbQSicJIZoSvYvoiaqDNbZrHZvKJwwQzIw/640?wx_fmt=png)

在内存中解密之前读取出来的加密的Brute Ratel C4 Badger的ShellCode代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWUSE7rTT08xGazfe5ZNtdxQafXqZJWO8R4hmx2yFllynFs5xGxz1UJSYN4xBYfLMyq6tBEoFiatrA/640?wx_fmt=png)

解密之后，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWUSE7rTT08xGazfe5ZNtdx1ZrAiam4gU8YLYbNPlFatOFbdFO96hbfQXv8ULMDicy3jtJZH6rot0sg/640?wx_fmt=png)

然后再调用NtCreateSection创建Section，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWUSE7rTT08xGazfe5ZNtdxgBeWfv2fdLw7HghkYo3rpXgkqVAW7N9W728QqulibRpGTQjpKfuGVag/640?wx_fmt=png)

调用NtMapViewOfSection函数将section映射到RuntimeBroker.exe进程虚拟内存，并将相关的代码拷贝到RuntimeBroker.exe进程，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWUSE7rTT08xGazfe5ZNtdxquC7fuPWByUcNfUvggmpEEvGGH42vIzREH3DIxbiaN0xNxIlU7ibD1mQ/640?wx_fmt=png)

最后调用NtCreateThreadEx函数执行线程代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWUSE7rTT08xGazfe5ZNtdx9OnRORTy6MHAvia3hzhibVpZfT5wQaut7wmcUn7b3KmdgsZxiaT2ujBuw/640?wx_fmt=png)

线程代码，就是Brute Ratel C4 Badger的ShellCode加载器代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWUSE7rTT08xGazfe5ZNtdxoMk3oEicbnB7ufoOibhV0XjcmfDBibw3YPcj4chawmjm0MyeyKA9KEwkQ/640?wx_fmt=png)

Black Basta勒索病毒也是笔者之前重点关注的几十个主流勒索病毒家族之一，该勒索病毒是一款2022年新型的勒索病毒，最早于2022年4月被首次曝光，主要针对Windows系统进行攻击，随后该勒索病毒黑客组织又积极开发更新了Linux版本的攻击样本，详细的报告可以参考笔者此前的文章《Linux版Black Basta勒索病毒针对VMware ESXi服务器》

前不久国外某安全厂商捕获到一例Black Basta勒索病毒黑客组织利用Brute Ratel C4进行勒索攻击活动事件，笔者针对事件中的Brute Ratel C4的攻击样本进行跟踪分析，该样本直接将Brute Ratel C4 Badger的ShellCode代码封装成DLL，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWUSE7rTT08xGazfe5ZNtdx3GkCro8bnwSKLu8mCCP778MI6jLtPZPBsV8PhQ0j8lAIZN9lLg6M5A/640?wx_fmt=png)

对比笔者此前生成的Demo文件，可以发现真实攻击样本与Demo样本的代码高达90%左右的相似度，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWUSE7rTT08xGazfe5ZNtdxfJMaoZiaz0E1kpwH8TVoRHavuNS9pIlR3xFuVs9U9RMUCxgHicmvPgEw/640?wx_fmt=png)

动态调试过程与此前Demo样本执行过程基本一致，在内存中加载执行Brute Ratel C4的Badger的ShellCode加载器代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWUSE7rTT08xGazfe5ZNtdx9LD5lWAHq8xic5QhkiaG3ZsRMB4Z2AKdD4nmpzvCBMc7psctGC5zeG3A/640?wx_fmt=png)

ShellCode加载器代码会在内存中解密出Brute Ratel C4 Badger的核心代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWUSE7rTT08xGazfe5ZNtdxicxegwOyroOh6ZTowgCKQQlDqEdbDFXgmhdfTrYfg68LhXKI7dz52Dw/640?wx_f...