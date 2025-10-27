---
title: eCapture支持borgingssl TLS 1.3明文数据包捕获
url: https://www.cnxct.com/ecapture-boringssl-tls-1_3/
source: CFC4N的博客
date: 2023-01-09
fetch_date: 2025-10-04T03:21:36.348207
---

# eCapture支持borgingssl TLS 1.3明文数据包捕获

Toggle navigation

[CFC4N的博客](https://www.cnxct.com/ "CFC4N的博客")
希望与理想是最令人珍惜的部分!

* 作品
  + [eCapture旁观者–HTTPS/TLS抓包](https://ecapture.cc "eCapture旁观者--HTTPS/TLS抓包")
  + [Golang eBPF Manager](https://github.com/gojue/ebpfmanager "Golang eBPF Manager")
  + [eBPF技术精选资料](https://github.com/gojue/ehids-slide "eBPF技术精选资料")
  + [League Of legends启动器](https://github.com/cfc4n/lol_launcher "League Of legends启动器")
  + [eBPF HIDS主机入侵检测](https://github.com/gojue/ehids-agent "eBPF HIDS主机入侵检测")
* [归档](https://www.cnxct.com/archives/ "归档")
* [关于我](https://www.cnxct.com/about/ "关于我")
* [工作机会](https://www.cnxct.com/jobs/ "工作机会")

# eCapture支持boringssl TLS 1.3明文数据包捕获

[2023/01/082023/01/09](https://www.cnxct.com/ecapture-boringssl-tls-1_3/)  [CFC4N](https://www.cnxct.com/author/admin/)

### 文章目录

1. [前言](#ftoc-heading-1)
2. [boringssl与openssl的差异](#ftoc-heading-2)
3. [android boringssl与普通boringssl的差异](#ftoc-heading-3)
   1. [Android boringssl偏移地址](#ftoc-heading-4)
   2. [普通boringssl类库偏移地址](#ftoc-heading-5)
   3. [偏移地址差异diff](#ftoc-heading-6)
4. [Linux上普通boringssl类库的eCapture使用](#ftoc-heading-7)
5. [功能演示](#ftoc-heading-8)
   1. [演示环境](#ftoc-heading-9)
   2. [演示命令](#ftoc-heading-10)
   3. [演示截图：](#ftoc-heading-11)
6. [eCapture链接地址](#ftoc-heading-12)
7. [未来展望：](#ftoc-heading-13)

### 前言

一个多月前，有网友反馈Android上，TLS 1.2明文网络包正常捕获，而1.3的密钥无法捕获。笔者得知这个问题后，花了几个周末时间修复、添加了这个功能。在这期间，笔者工作繁忙以及感染新冠，整个功能拖了1个月 才完成。精力与体力，支撑起来越来越吃力。搞开源，全是靠爱发电，实属不易。

值得庆幸的是，收获了5400星的关注，这也是对笔者最大的认可。

![](https://image.cnxct.com/2023/01/ecapture-github-5k-stars-scaled.jpg)

这个周末，发布了eCapture 0.4.11版本，支持boringssl的TLS 1.3的密钥捕获，支持明文解密pcapng数据包存储。 有需要的朋友可以下载使用。

![eCapture卡通人物](https://image.cnxct.com/2023/01/ecapture-logo-new-10002.jpg)

其次，这次支持boringssl的TLS 1.3明文数据包捕获，还遇到了一些技术性问题，在这里也一并分享给大家。

### boringssl与openssl的差异

Google开源了[boringssl](https://github.com/google/boringssl)这个SSL加密类库，是基于openssl的增强版。使用C++封装C的类库，在结构体内存布局上，与openssl有一些差异。而且TLS通信密钥捕获的Hook函数上，与openssl有差异。在openssl中，只需要HOOK `SSL_write`、`SSL_read` 两个函数，读取参数中`SSL`结构体的内存布局，定位相关SSL密钥存储地址，即可读取密钥。

而在boringssl中，在调用`SSL_write`函数时，这个TLS链接可能还没建立好。需要寻找更合适的HOOK函数，笔者在实现时，做了大量的测试、调试工作，最终在`SSL_do_handshake` 跟`SSL_in_init`两个函数中，选择了`SSL_in_init`，进行密钥的读取。

实际使用时，仍会有`s3_st`为空、`s3->hs`地址为空的情况，以及TLS未建立、正在握手中，密钥不完整等情况，笔者最后选择将所有eBPF捕获内存数据，通过bpf map发送给用户空间程序，再在用户空间判断密钥，进行过滤，曲折实现。

### android boringssl与普通boringssl的差异

说到boringssl，刚接触的人可能搞不清楚版本，认为google在github上开源的https://github.com/google/boringssl.git 项目就是，直接用这个测试。实际上，Android系统使用的boringssl并不是这个仓库，而是 <https://android.googlesource.com/platform/external/boringssl> ，二者的差异，对ecapture来说，其结构体的内存布局不一样，属性的偏移地址不一样。

笔者就被这个问题困扰很久，为什么在PC上，使用boringssl测试成功，而在android手机上却无法工作。手机、模拟器、重刷ROM，都是不行。。一直到笔者把Android上类库源码重新检出，仔细测试boringssl的代码，才发现这个问题。 Google在这块文档上，并没有说明，实在是让人无奈。

#### Android boringssl偏移地址

你可以按照自己Android使用的boringssl版本，自己重新生成boringssl的偏移量，使用命令如下：

```
rm -f kern/boringssl_1_1_1_kern.c
bash utils/boringssl_offset_1.1.1.sh
```

#### 普通boringssl类库偏移地址

在Linux上，很多类库都是支持改用openssl为boringssl的，eCapture也提供了自助生成新偏移量的脚本，它比`Android boringssl`命令后面多个参数`1`，生成命令如下：

```
rm -f kern/boringssl_1_1_1_kern.c
bash utils/boringssl_offset_1.1.1.sh 1
```

#### 偏移地址差异diff

![](https://image.cnxct.com/2023/01/boringssl-offset.jpg)

### Linux上普通boringssl类库的eCapture使用

以curl类库为例，启用boringssl的编译命令如下：

```
git clone https://github.com/curl/curl.git
autoreconf -fi
LIBS=-lpthread ./configure --with-ssl=/home/cfc4n/project/boringssl --enable-versioned-symbols
make
sudo make install
sudo ldconfig
```

如果你在编译启用boringssl的curl遇到错误时，可以参考笔者的经历：[alt-svc build error on ubuntu 18.04: missing struct tm #9989](https://github.com/curl/curl/issues/9989)

**eCapture捕获命令：**

```
bin/ecapture tls --libssl=/usr/local/lib/libcurl.so.4 --ssl_version="boringssl 1.1.1" -w a.pcapng -i ens33
```

### 功能演示

#### 演示环境

系统：macOS

模拟器：Android Studio Dolphin | 2021.3.1 Patch 1

镜像ROM：Pixel 3a API 33 x86\_64

内核：Linux localhost 5.10.66-android12-9-00041-gfa9c9074531e-ab7914766 #1 SMP PREEMPT Fri Nov 12 11:36:25 UTC 2021 x86\_64

测试APP：百度手机助手9.5.8.1

#### 演示命令

**启动eCapture**

```
emulator64_x86_64_arm64:/data/local/tmp # ./ecapture tls -w aa.pcapng -i wlan0
tls_2023/01/08 14:02:54 ECAPTURE :: ecapture Version : androidgki_x86_64:0.4.11-20230107-59a76e0:5.4.0-131-generic
tls_2023/01/08 14:02:54 ECAPTURE :: Pid Info : 26496
tls_2023/01/08 14:02:54 ECAPTURE :: Kernel Info : 5.10.66
tls_2023/01/08 14:02:54 EBPFProbeOPENSSL    module initialization
tls_2023/01/08 14:02:54 EBPFProbeOPENSSL    Module.Run()
tls_2023/01/08 14:02:54 EBPFProbeOPENSSL    TC MODEL
tls_2023/01/08 14:02:54 EBPFProbeOPENSSL    OpenSSL/BoringSSL version not found, used default version :android_default
tls_2023/01/08 14:02:54 EBPFProbeOPENSSL    HOOK type:2, binrayPath:/apex/com.android.conscrypt/lib64/libssl.so
tls_2023/01/08 14:02:54 EBPFProbeOPENSSL    Ifname:wlan0, Ifindex:16,  Port:443, Pcapng filepath:/data/local/tmp/aa.pcapng
tls_2023/01/08 14:02:54 EBPFProbeOPENSSL    Hook masterKey function:SSL_in_init
tls_2023/01/08 14:02:54 EBPFProbeOPENSSL    target all process.
tls_2023/01/08 14:02:54 EBPFProbeOPENSSL    target all users.
tls_2023/01/08 14:02:54 EBPFProbeOPENSSL    BPF bytecode filename:user/bytecode/boringssl_1_1_1_kern.o
tls_2023/01/08 14:02:54 EBPFProbeOPENSSL    module started successfully.
tls_2023/01/08 14:02:54 ECAPTURE ::     start 1 modules
794b86e16f4f17d1c90fee21e72d56aa92c1f4deb5f7494c0eab9598895d48ff to file success, 176 bytes
tls_2023/01/08 14:05:06 TLS1_3_VERSION: save CLIENT_RANDOM 7fbea9bdcc818fb80cc04c1d0ad0c0c870cf97267678d42fa6026dd92cfa6b20 to file success, 778 bytes
tls_2023/01/08 14:05:43 TLS1_2_VERSION: save CLIENT_RANDOM 50a103ecbdd2a84c707eeda3262381ab8a427993c2407ecd537ae2414978f821 to file success, 176 bytes
```

**捕获的TLS 1.3密钥**

```
130|emulator64_x86_64_arm64:/data/local/tmp # cat ecapture_masterkey.log
CLIENT_HANDSHAKE_TRAFFIC_SECRET 7fbea9bdcc818fb80cc04c1d0ad0c0c870cf97267678d42fa6026dd92cfa6b20 e34deeab543a3cd63e8009737a4cf4188e9f5c2b6588e5b72874055818004c6c
CLIENT_TRAFFIC_SECRET_0 7fbea9bdcc818fb80cc04c1d0ad0c0c870cf97267678d42fa6026dd92cfa6b20 82857c8eb07c88b6c56c9d38759c23cc6d14d9dd23a37bb17fa41e5913cf211e
SERVER_HANDSHAKE_TRAFFIC_SECRET 7fbea9bdcc818fb80cc04c1d0ad0c0c870cf97267678d42fa6026dd92cfa6b20 bef4cde1643c47d5971f226e9d637155d55087184f0f75963db792d71afc56c0
SERVER_TRAFFIC_SECRET_0 7fbea9bdcc818fb80cc04c1d0ad0c0c870cf97267678d42fa6026dd92cfa6b20 c949827f3150a3c4c4589478caa1b2987493dd17dfe008aa26ce9b881d9af21b
EXPORTER_SECRET 7fbea9bdcc818fb80cc04c1d0ad0c0c870cf97267678d42fa6026dd92cfa6b20 0b0017b44c8ac50126a7aeb03494d1454f7f4ec560fbaba144198eb74ddab280
CLIENT_RANDOM 50a103ecbdd2a84c707eeda3262381ab8a427993c2407ecd537ae2414978f821 e1a6d3edd5f4e817aea86b2d15d3d21a23c8d2d60770c36819303e25873f30089d555d447ab29b8208b8c0ecd230405a
```

#### 演示截图：

![](https://image.cnxct.com/2023/01/android-x86-boringssl-scaled.jpg)

### eCapture链接地址

[eCapture v0.4.11 下载地址](https://github.com/gojue/ecapture/releases/tag/v0.4.11)

[eCapture 官网](https://ecapture.cc/)

[eCapture 代码仓库](https://github.com/gojue/ecapture)

### 未来展望：

eCapture功能趋于稳定，以及笔者经历有限，未来更新频率可能会降低，欢迎广大网友参与其中，一起为开源做贡献，一起为你点赞。

![](https://image.cnxct.com/2023/01/xiaoyaoguai-scaled.jpg)

[![知识共享许可协议](//www.cnxct.com/attachments/88x31.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh-hans)CFC4N的博客 由 [CFC4N](http://www.cnxct.com) 创作，采用 [署名—非商业性使用—相同方式共享 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh-hans) 进行许可。基于[https://www.cnxct.com](http://www.cnxct.com)上的作品创作。转载请注明转自：[eCapture支持boringssl TLS 1.3明文数据包捕获](https://www.cnxct.com/ecapture-boringssl-tls-1_3/)

相关文章:

1. [eCapture旁观者：Android HTTPS明文抓包，无需CA证书](https://www.cnxct.com/ecapture-for-android/ "eCapture旁观者：Android HTTPS明文抓包，无需CA证书")
2. [eCapture的几个好消息，支持Android…](https://www.cnxct.com/ecapture-news-android/ "eCapture的几个好消息，支持Android…")
3. [eCapture：无需CA证书抓https网络明文通讯](https://www.cnxct.com/what-is-ecapture/ "eCapture：无需CA证书抓https网络明文通讯")
4. [分享一些eBPF技术相关的PDF](https://www.cnxct.com/ebpf-slide-pdf-share/ "分享一些eBPF技术相关的PDF")
5. [datadog的eBPF安全检测机制分析](ht...