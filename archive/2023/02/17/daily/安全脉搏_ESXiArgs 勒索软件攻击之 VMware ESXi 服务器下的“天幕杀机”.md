---
title: ESXiArgs 勒索软件攻击之 VMware ESXi 服务器下的“天幕杀机”
url: https://www.secpulse.com/archives/196003.html
source: 安全脉搏
date: 2023-02-17
fetch_date: 2025-10-04T06:50:37.352747
---

# ESXiArgs 勒索软件攻击之 VMware ESXi 服务器下的“天幕杀机”

[![](https://www.secpulse.com/wp-content/themes/secpulse2017/img/logo-header.png)](https://www.secpulse.com "安全脉搏")

* [首页](https://www.secpulse.com/)
* [分类阅读](https://www.secpulse.com/archives/category/category)

  #### 脉搏文库

  - [内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)
  - |
  - [代码审计](https://www.secpulse.com/archives/category/articles/code-audit)
  - |
  - [安全文献](https://www.secpulse.com/archives/category/articles/sec-doc)
  - |
  - [Web安全](https://www.secpulse.com/archives/category/articles/web)
  - |
  - [移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)
  - |
  - [系统安全](https://www.secpulse.com/archives/category/articles/system)
  - |
  - [工控安全](https://www.secpulse.com/archives/category/articles/industrial-safety)
  - |
  - [CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)
  - |
  - [IOT安全](https://www.secpulse.com/archives/category/iot-security)
  - |

#### 安全建设

+ [业务安全](https://www.secpulse.com/archives/category/construction/businesssecurity)
+ |
+ [安全管理](https://www.secpulse.com/archives/category/construction/securityissue)
+ |
+ [数据分析](https://www.secpulse.com/archives/category/construction/bigdata)
+ |

#### 其他

+ [资讯](https://www.secpulse.com/archives/category/news)
+ |
+ [漏洞](https://www.secpulse.com/archives/category/vul)
+ |
+ [工具](https://www.secpulse.com/archives/category/tools)
+ |
+ [人物志](https://www.secpulse.com/archives/category/people)
+ |
+ [区块链安全](https://www.secpulse.com/archives/category/exclusive/block_chain_security)
+ |
+ [安全招聘](https://www.secpulse.com/archives/category/hiring)
+ |

- [安全问答](https://www.secpulse.com/newpage/question_list)
- [金币商城](https://www.secpulse.com/shop?donotcachepage=c010349fd98847cb9d6e07d3cbc19288)
- [安全招聘](https://www.secpulse.com/archives/category/hiring)
- [活动日程](https://www.secpulse.com/newpage/activity)
- [live课程](https://www.secpulse.com/live)
- [企业服务](https://duoyinsu.com/service.html)
- [插件社区](https://x.secpulse.com/)

小程序

![脉搏小程序](https://www.secpulse.com/wp-content/themes/secpulse2017/img/wxchat.jpg)
[登录](https://www.secpulse.com/user_login)
|
[注册](https://www.secpulse.com/user-register)

# ESXiArgs 勒索软件攻击之 VMware ESXi 服务器下的“天幕杀机”

[漏洞](https://www.secpulse.com/archives/category/vul)

[Further\_eye](https://www.secpulse.com/newpage/author?author_id=9241)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2023-02-16

9,861

**恶意家族名称：**

ESXiArgs

**威胁类型：**

勒索事件

**简单描述：**

近期一款新的针对 VMware ESXi 服务器勒索软件正在全球范围内大规模传播，攻击者采用 2021 年的远程代码执行漏洞 CVE-2021-21974 获得交互式访问，借以部署新的 ESXiArgs 勒索软件。

**恶意文件分析**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196003-16765307311.gif)

**恶意文件描述**

近期，深信服深盾终端实验室在运营工作中发现了一种新的勒索软件 ESXiArgs ，该勒索软件于今年2月开始大规模出现。攻击者利用两年前未经修补的 RCE 漏洞 CVE-2021-21974 将恶意文件传输至 ESXi 导致 OpenSLP 服务中的堆溢出。

**漏洞利用**

该漏洞与 OpenSLP 相关，通过 427/UDP 进行攻击，未经身份验证的威胁参与者可以利用该漏洞在低复杂性攻击中获得远程代码执行。截止本文发布，基于censys统计数据全球已受影响服务器有 2453 台，国内已受影响服务器大概数十台左右。

**CVE-2021-21974 漏洞影响以下版本：**

```
ESXi70U1c-17325551之前的ESXi 7.x版本
ESXi670-202102401-SG之前的ESXi 6.7.x版本
ESXi650-202102101-SG之前的ESXi 6.5.x版本
```

受 ESXiArgs 影响 ESXi 服务器涉及版本集中在 6.7.0、6.5.0、6.0.0、5.5.0。**此外 VMware 关于 CVE-2021-21974 的官方公告并没有具体说明 6.0.0 和 5.5.0 版本是受影响的版本，但是，根据网络空间测绘数据统计该版本明确被攻击。**

**国内存在该漏洞影响的服务器数量如下所示（基于censys统计数据）：**

|  |  |
| --- | --- |
| **版本** | **数量统计** |
| ESXi 6.5 | 715 |
| ESXi 6.7 | 3184 |
| ESXi 7.0 | 1271 |
| ESXi 6.0.0 | 665 |
| ESXi 5.0.0 | 342 |

**该漏洞在2021年已及时进行响应，相关链接如下所示：**

**[【漏洞更新】VMware ESXi OpenSLP堆溢出漏洞 CVE-2021-21974](http://mp.weixin.qq.com/s?__biz=Mzg2NjgzNjA5NQ==&mid=2247514754&idx=2&sn=facb153d29e5eb21e1b93b43e1cf0a6c&chksm=ce463192f931b884743fc9654c4c6df7a73f4c5a6ad7afe848fb1af108dce7e5d4f8790de57b&scene=21#wechat_redirect)**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196003-1676530732.gif)

**恶意文件分析**

**通过分析发现与该勒索行为相关的文件共有5个，位于受害服务器中的/tmp/文件夹下，相关恶意文件及描述如下所示：**

```
encrypt– 加密器（ELF可执行文件）
encrypted.sh – 执行加密器之前的功能文件
public.pem – 用于加密文件的RSA加密算法中的公钥
motd——文本格式的勒索信文件
index.html – html格式的勒索信文件
```

该样本使用参数进行启动，在程序启动初始阶段便会对参数进行强校验，样本通过正确参数启动后便会进行后续操作，勒索信文件名为 “How to Restore Your Files.html”， 指示受害者通过  TOX\_ID  与攻击者取得联系，以恢复加密文件或防止数据被泄露。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196003-1676530732.png)

**encrypt.sh**

shell脚本整体逻辑如下所示：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196003-1676530736.png)

**修改配置文件**

修改虚拟机的磁盘文件 vmdk 及虚拟内存文件 vswp 的文件名，增加受害者在文件加密后找到和恢复初始数据的困难性。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196003-1676530737.png)

**加密文件**

首先枚举 ESXi 主机上所有的存储卷，因此未连接到 VM 的虚拟磁盘可能也会受到影响。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196003-1676530738.png)

加密存储卷中包含如下扩展名的文件：

```
*.vmdk
*.vmx
*.vmxf
*.vmsd
*.vmsn
*.vswp
*.vmss
*.nvram
*.vmem
```

**持久化**

将 encrypt\_file() 勒索信文件复制到 /usr/lib/vmware 目录下

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196003-1676530747.png)

**防御规避**

该勒索软件为了避免被发现及数据恢复，尝试了如下操作：包括删除系统中所有的 `log` 文件、清除计划任务、删除备份文件、删除 `http` 端口配置文件中所有存在的 `ip`、删除`store/packages/vmtools.py`后门文件及最初始上传的 `tmp/` 目录下的恶意文件。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196003-1676530750.png)

**启动ssh服务**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196003-1676530752.png)

**加密器encrypt**

启动命令，启动参数包括公共 RSA 密钥文件、要加密的文件路径、避免加密的数据块、加密块的大小和文件大小。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196003-16765307521.png)

勒索软件启动会执行多个步骤来加密系统文件

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196003-1676530753.png)

`encrypt_file()`函数进一步调用`encrypt_simple()`函数来执行加密过程。下图显示了 `encrypt_file()`函数的代码片段

`encrypt_simple`函数如下所示：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196003-1676530760.png)

`sosemanuk_encrypt` 加密过程如下所示：

检查存储在 `result` 中的值是否小于 `0x4F`，当小于 `0x4F`时，它将明文的前 `80LL - (a1 + 128)`字节与 `Sosemanuk` 密码的内部状态进行异或。然后该函数进入一个循环，每次以 `80LL` 字节的块加密剩余的明文，在每个块加密后更新 `Sosemanuk`密码的内部状态。然后将加密块与明文进行异或运算以生成密文。

文件小于 `128MB` 时，完全加密

文件大于 `128MB (1M=1024K)`时未完全加密

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196003-1676530761.png)

**生成流密钥**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196003-1676530762.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196003-1676530763.gif)

**ATT&CK**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196003-1676530763.png)

**IOCs**

**ESXi勒索软件支付地址列表**

https://gist.github.com/cablej/c79102960c4615396e8ffc712136744a

**MD5**

```
d0d36f169f1458806053aae482af5010    encrypt.sh
87b010bc90cd7dd776fb42ea5b3f85d3    encrypt
```

**解决方案**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196003-1676530767.gif)

**处置建议**

1. 在 `ESXi` 中禁用 `OpenSLP` 服务，或者升级至 `ESXi 7.0 U2c` 或 `ESXi 8.0 GA`，`ESXi 7.0 U2c`或 `ESXi 8.0 GA` 版本默认情况下禁用该服务。

2. 检查文件 `“vmtools.py”` 是否存在于`“/store/packages/”`位置。如果找到，建议立即删除该文件。

3. 安装信誉良好的防病毒/反间谍软件，定期进行系统全盘扫描，并删除检测到的威胁，按时升级打补丁。

4. 重要的数据最好双机备份或云备份。

**本文作者：[Further\_eye](newpage/author?author_id=9241)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/196003.html**](https://www.secpulse.com/archives/196003.html)

Tags: [ATT&CK™](https://www.secpulse.com/archives/tag/attck)、[CVE-2021-21974](https://www.secpulse.com/archives/tag/cve-2021-21974)、[encrypt\_file()函数](https://www.secpulse.com/archives/tag/encrypt_file%E5%87%BD%E6%95%B0)、[encrypt()](https://www.secpulse.com/archives/tag/encrypt)、[ESXiArgs](https://www.secpulse.com/archives/...