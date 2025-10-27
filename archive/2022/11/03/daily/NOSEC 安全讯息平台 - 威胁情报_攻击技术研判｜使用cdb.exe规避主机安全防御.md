---
title: 攻击技术研判｜使用cdb.exe规避主机安全防御
url: https://nosec.org/home/detail/5043.html
source: NOSEC 安全讯息平台 - 威胁情报
date: 2022-11-03
fetch_date: 2025-10-03T21:39:42.916162
---

# 攻击技术研判｜使用cdb.exe规避主机安全防御

[![](https://nosec.org/home/image/logo.png)](/)

[登录/注册](https://nosec.org/home/caslogin)

[投稿](https://nosec.org/home/caslogin)

[首页](/home/index)
[威胁情报](/home/index/threaten.html)
[安全动态](/home/index/security.html)
[漏洞预警](/home/index/hole.html)

数据泄露

* [新闻浏览](/home/index/leakage.html)
* [图表统计](/home/index/graphshtml)

[专题报告](/home/index/speech.html)
[技术分析](/home/index/skill.html)
[安全工具](/home/index/tool.html)

# 攻击技术研判｜使用cdb.exe规避主机安全防御

![](https://nosec.org/home/image/headImg.png)xiannv  1066天前

**情报背景**

具备丰富EDR开发经验的安全团队SentinelLabs近期公布了名为metador的新黑客组织攻击活动，其攻击目标主要针对电信、互联网服务商和大学。攻击者熟悉攻击操作安全，其中使用了Windows控制台调试程序来运行其复杂的恶意控制框架。

| **组织名称** | 未知 |
| --- | --- |
| **关联组织** | 未知 |
| **战术标签** | 防御规避 |
| **技术标签** | lolbins、process inject、wmi |
| **情报来源** | <https://assets.sentinelone.com/sentinellabs22/metador> |

**01 攻击技术分析**

为了部署其完全基于内存windows恶意攻击框架，攻击者选择一些实用的加载机制来规避检测，利用wmi事件订阅和windows控制台调试程序(cdb.exe)来执行其恶意行为，能相对容易的避开本地安全产品。

其攻击流程如下：

1. 创建一个名为hard\_disk\_start的wmi订阅事件（系统启动事件）

2. 订阅事件会运行windows控制台调试程序(cdb.exe)的命令行调试运行合法程序（c:\windows\system32\cdb.exe -cf c:\windows\system32\cdb.ini c:\windows\system32\defrag.exe -module fcache13.db）

其中-cf cdb.ini是调试脚本路径，c:\windows\system32\defrag.exe是被调试的程序，-module fcache13.db是加密的metador载荷文件路径

3. cdb.exe 注入恶意shellcode到合法程序defrag.exe的入口处运行

4. shellcode会加载后续的metamain反射DLL加载模块Speech02.db

5. Speech02.db会加载后续恶意模块

![1.png](/avatar/uploads/attach/image/e77a90f5617e6b33106004a6cec5466a/1.png)

SentinelLabs文章中描述的metador攻击利用过程

**cdb.exe的攻击利用方式**

cdb.exe是Windows调试工具（Debugging Tools）附带的一个具有Microsoft签名的二进制文件，可以调试指定进程，且在指定进程里分配RWX属性内存并写入shellcode，最后执行该内存中的shellcode。

由于默认windows系统并不包含cdb.exe，所以攻击者还需要将cdb.exe的副本带入到目标系统之中，执行完后攻击者会将其删除以擦除攻击痕迹。

cdb.ini 中包含的恶意脚本内容

![2.png](/avatar/uploads/attach/image/64935efac14b1968e0221a2b2b3dfcd0/2.png)

这段脚本的内容很简单，-eq $exentry代表将后续的数值作为代码写入可执行文件的入口。dq代表退出分离调试程序。

四字节值反汇编后的shellcode代码片段

![3.png](/avatar/uploads/attach/image/2fba973a8b87647209841131c8b9bb01/3.png)

shellcode将读取、解密运行metamain的反射DLL加载器Speech02.db，Speech02.db之后就会继续解密加载metamain的主要运行体Speech03.db。

在mrdx的文章The Power of Cdb.exe | mr.d0x (<https://mrd0x.com/the-power-of-cdb-debugging-tool/>)中总结了关于cdb.exe的多种利用方式：

1. 运行shellcode

```
cdb.exe -pd -cf c:\path\to\payload\test.wds -o notepad.exe
```

2. 执行可执行程序

```
cdb.exe -pd -pn notepad.exe -a "c:\users\mr.d0x\desktop\out.exe"
```

3. 加载运行DLL文件

```
cdb.exe -pd -pn notepad.exe

.load c:\path\to\dll\evil.dll
```

4. 执行SHELL命令

```
cdb.exe -pd -pn notepad.exe

.shell ping 127.0.0.1
```

5. 强制结束安全程序

**02 总结**

基于内存的复杂恶意框架越来越常见，攻击者为了保护其重要的攻击武器资产，选择使用cdb.exe来作为初始的执行方式来对现有的安全策略进行绕过，一旦初始执行成功便可以转入合法进程的内存空间，掩盖其后续的恶意行为。

**参考**

[1] cdb | LOLBAS (<https://lolbas-project.github.io/lolbas/OtherMSBinaries/Cdb/>)

[2] The Power of Cdb.exe | mr.d0x (<https://mrd0x.com/the-power-of-cdb-debugging-tool/>)

来源：[天元实验室 M01N Team](https://mp.weixin.qq.com/s/JbQBWvFkMTwtHWCkNcmiZg)

[上一篇：
regulator ：一种独特的子域枚举......](/home/detail/5042.html)
[下一篇：
GoEXP WANTED 3](/home/detail/5044.html)

浏览: 6095
评论: 1

![](https://nosec.org/home/image/weibo.png)

#### 最新评论

![](/home/image/headImg.png)

求知
 :
有没有样本？

1058天前
回复

![](/home/image/loading.gif)
评论正在提交，请稍等...

昵称

邮箱

已有账号，[登录](/home/caslogin)评论

提交评论

[x]  有人回复邮件通知我

![](https://nosec.org/home/image/code.png)

## 相关推荐

[Karken勒索软件2.0版本开始传播](/home/detail/1936.html "Karken勒索软件2.0版本开始传播")

[【译】4200 万用户密码文件被上...](/home/detail/1822.html "【译】4200 万用户密码文件被上传至 kayo.moe 托管服务")

[【安全通报】Nagios XI 多个安全...](/home/detail/4432.html "【安全通报】Nagios XI 多个安全漏洞")

[Goby 内测版1.9.314｜代理全局状...](/home/detail/4918.html "Goby 内测版1.9.314｜代理全局状态切换、报告支持插件数据显示、新增47种 UDP 协议支持")

[mjrfw.gov.cn官网被黑，主站已打...](/home/detail/1483.html "mjrfw.gov.cn官网被黑，主站已打不开")

## 热门文章

×

#### 分享到微信朋友圈

![](https://nosec.org/home/image/logo.png)

友情链接：[FOFA](https://fofa.info) [FOEYE](http://www.baimaohui.net/foeye) [BAIMAOHUI](http://baimaohui.net) [安全客](https://www.anquanke.com) [i春秋](https://www.ichunqiu.com)
[指尖安全](https://www.secfree.com)
[2021上海网络安全博览会](http://www.sins-expo.com)

nosec.org All Rights Reserved [京ICP备15042518号-2](http://beian.miit.gov.cn)