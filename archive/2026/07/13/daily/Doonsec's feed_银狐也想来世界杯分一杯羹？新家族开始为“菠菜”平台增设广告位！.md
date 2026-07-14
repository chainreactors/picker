---
title: 银狐也想来世界杯分一杯羹？新家族开始为“菠菜”平台增设广告位！
url: https://mp.weixin.qq.com/s/NNJm9glOfDbTemuGJnGEzA
source: Doonsec's feed
date: 2026-07-13
fetch_date: 2026-07-14T04:42:28.677844
---

# 银狐也想来世界杯分一杯羹？新家族开始为“菠菜”平台增设广告位！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/u1Oy5xQ01SoiblPuOpaeJ8LZdfzMRxeKAYqAwUFSNnhOs1CyCuVDrZaVHgNgknYaliaexdL7mOv30Sibhr6aicSDL0YiaDIQicibBMYaX10LwkO8yQ/0?wx_fmt=jpeg)

# 银狐也想来世界杯分一杯羹？新家族开始为“菠菜”平台增设广告位！

原创

火绒安全
火绒安全

火绒安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/u1Oy5xQ01SqxGhgiaLJB5KsxDwrcsec6bROFZMfMNcXOhVStgRum6zYJq3icASyV8I0F7otjrTnXcJ9N76ETmbnWUKGAokicWIgYosLdp5VQes/640?wx_fmt=gif&from=appmsg)

近期，火绒安全实验室在监测网络安全过程中发现异常情况。经过溯源与技术分析，这是银狐黑产使用新的样本针对中国国内用户，通过伪装为压缩包、视频剪辑、Microsoft商店等应用安装软件的投毒行为。与以往不同是，银狐组织在本次攻击中，恶意代码的设计是以插件的形式加载，这就会产生灵活多变的组合让用户防不胜防。本次下载获取的插件是一个关于世界杯广告弹窗投递的插件（涉及赌球“菠菜”等）。该样本可以以插件的形式多次为用户安装其他软件（包括但不限于弹窗广告软件），并在保持后门一直存在的情况下，窃取用户信息、控制用户电脑。

目前，火绒安全产品已经实现对该行为的拦截与查杀。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/u1Oy5xQ01SrNJKyAzDLhlL6h7Pibrt4cez6AjmXibgqfydsLEtDibs8eMGTTJibfqDiblFPuU11Kfnus3r0mRvFT2MDI50BApRlYx9W7RfBymM0I/640?wx_fmt=png&from=appmsg)

**查杀图**

**运行流程**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/u1Oy5xQ01SolvrMicD1xgVesZrvelcG58IGGJB1qGO5ic4zKJxSvZib5eT2GlZFUbPRXX4okYxN3pqoIicjVfyqx8U76EYD9WoLNzrY5bcdm5PM/640?wx_fmt=png&from=appmsg)

**流程图**

**样本分析**

本篇文章提到的4个样本基本相同，后续详细内容只针对1个样本进行描述。不对其他样本进行过多赘述。

**执行初始化**

#### **Rust启动器**

通过多项检测环境来检验该程序是否被调试或者在沙箱、虚拟机等环境。

![](https://mmbiz.qpic.cn/mmbiz_png/u1Oy5xQ01SrdOrzNVP7g0bxnq0Sg0BuNtjdk0rYYBpKKTAbs5eMFojmBw3tdZfRg8q6IEXFHyBED7BrxtiaLzPh4Ou3nzBatjWtJlp0gK0JM/640?wx_fmt=png&from=appmsg)

通过AES算法解密将要释放的3个载荷，首先通过异或算法解密得到文件名称Cache.pmt。后续通过AES解密得到载荷释放到路径C:\Program\CalendarSync\Cache.pmt下。

![](https://mmbiz.qpic.cn/mmbiz_png/u1Oy5xQ01SopBib9iaoWjwdZ51hdbyCOC4NIoAY0y5icGm5BFKx9vlwXf4tPiaT0VM2IEJ9ZfWo7CibaNYeA5KZCgicyhv2BhsxrtycQYyGHibicghE/640?wx_fmt=png&from=appmsg)

最终通过CreateProcessW函数来启动CalendarSync.exe程序。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/u1Oy5xQ01Srm5C2QU9NicALPwKxsSTziaUe0EBl73DZlQj9pTWxicNibqKyc4a37gvGI2pr1ey7wMen7iaG7Lxaxkiakb49TJHroKOia3erLg6NFTk/640?wx_fmt=png&from=appmsg)

#### **加载载荷MasMIX32.dl分析**

恶意MasMIX32.dll首先会通过异或0x37解密得到Cache.pmt的名称，通过hash获取读取文件api函数的地址。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/u1Oy5xQ01Sq57TkI7tKdZOabm40Gkmn0AP89wbTwUDGib4QVXHjHHeFx5ecZXrMGMvTSoyuMthgZWdEHj9mzcfrKgwD5MYUFuicXia807OFZSM/640?wx_fmt=png&from=appmsg)

然后通过自定义RC4算法+RtlDecompressBuffer组合解密下一阶段Shellcode。RC4密钥B734BF22E076BDB05AAF549038D4E5F1。

![](https://mmbiz.qpic.cn/mmbiz_png/u1Oy5xQ01Sqzict5iazYou0gic6EPwR9icB1EEA4e77Fpj92cwia21aF7pO4hh9h3nVLC6Agkp0y9WuUmVXpxZSAwIMdKFT9FZnfgdKlDZzZWm4I/640?wx_fmt=png&from=appmsg)

最后通过反射dll在自身申请内存，运行在自身内存中。

![](https://mmbiz.qpic.cn/mmbiz_png/u1Oy5xQ01Squmecj2VoMOuonIypnDJic0yX8k4dc8yib7jQDVzFGoNsSIFw55vePFeDGBhLyAffNpmZmxOvMQS5RejMFgD5MSKLjLFLymY60E/640?wx_fmt=png&from=appmsg)

#### **注入载荷Cache.pmt分析**

由于该文件使用了大量混淆，包括控制流扁平化，不透明谓词，花指令，以及轻量级的VMP混淆。代码阅读效果就由作者构造伪代码来解释。

主要的执行逻辑为，创建互斥体->COM初始化->提权->注入->写入注册表->篡改IP路由表。

![](https://mmbiz.qpic.cn/mmbiz_png/u1Oy5xQ01SpYQ50kIxqQxkWSltnGpqs2Ol0E2xazDjV9JBIEE677CfibVfgOKX083KbTZLX4XHPOeEDjk2ju6u5BmyGzmf47mUYK9BPFTDdA/640?wx_fmt=png&from=appmsg)

互斥体模块，创建互斥体Global\{CFE43A7D-B0E3-40E9-9919-13DEE7900CF8}

![](https://mmbiz.qpic.cn/sz_mmbiz_png/u1Oy5xQ01Sol4N95KbFZzGl8jXbVqmUG6OZDDAU37SHS0Ryq297lIePNVsicNgCnlsyWfcmTO357qgKviaciaG1Uib8npAC610ypicKjicrBAOl8I/640?wx_fmt=png&from=appmsg)

提权模块，通过多个api的连续调用达到提权的目的。

![](https://mmbiz.qpic.cn/mmbiz_png/u1Oy5xQ01SpaRqHQibvAfV9SVR800KqW4BaTOceec6XGOibXVEPwYSLg0p8hXvUXCGhZVOWqwzQDLAR2oLJBxAMqqmqHNnHoGG3owAuX3HGkU/640?wx_fmt=png&from=appmsg)

创建注册表，写入注册表中是加密的。解密后的结构如下：

1、文件路径

2、服务名称1

3、服务名称2

4、加密的下一阶段dll文件

![](https://mmbiz.qpic.cn/mmbiz_png/u1Oy5xQ01SqD97X2Dc5yickl22kcAtXw1LOnND1pANyS2eaMHSUoFENQN8uvSckvfiajSblBQdKjMyK5vVChwg6hgrJWicbicPfia6W2UicTk2nhI/640?wx_fmt=png&from=appmsg)

劫持网关，通过修改ip路由表来达到劫持网关的目的。

![](https://mmbiz.qpic.cn/mmbiz_png/u1Oy5xQ01SpxOMbST6F8H6paWBXwNUzFLxZZ9XaiaYB0ejaP26oPwGKzvRIYkAv1TOqEXXj5ppMA7xVb1GePWS8YO8ibBHf1z7kwyB1hX3q3E/640?wx_fmt=png&from=appmsg)

共享内存注入，通过NtMapViewOfSection等api调用链，为创建的TieringEngineService.exe创建共享内存。挂起线程修改eip恢复线程启动。

![](https://mmbiz.qpic.cn/mmbiz_png/u1Oy5xQ01Sqibqr5Rn1wicHicXbK3L1UQvKfRb6ibSk2FlwVS4NViaWCwwFHEoQLDly7n2FSF7T0pvF37f6zjDq6Yasx7Q1gLxO6LESrn0hI5IWM/640?wx_fmt=png&from=appmsg)

#### **注入载荷2-TieringEngineService.exe分析**

注入载荷2是最终功能调度的前一级。在TieringEngineService.exe中运行。主要功能为循环读取注册表值HKLM\SOFTWARE\Microsoft\Tracing\choco\_RASAPICS注入进程backgroundTaskHost.exe程序。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/u1Oy5xQ01So9amg1JcrmapedJ5n0dkb50owrbJWnlFTeXjFp5UpeHacfiaNibMGgwyVbEdfcryMQ2ePMP5eelvzZL04tZufb1bvSt5DkZHsoY/640?wx_fmt=png&from=appmsg)

通过进程镂空的方式，挂起的方式启动backgroundTaskHost.exe程序，注入，恢复线程。

![](https://mmbiz.qpic.cn/mmbiz_png/u1Oy5xQ01SqVAwsJ88Led2EkpSHf7I8uVZM5sD78prM1l780CcDxOMWlAF9TtD3ry5ICjoAS1lAYHefvQy5JpevMFk3wKWFIcLrZicGQ4ib0g/640?wx_fmt=png&from=appmsg)

**回传数据与插件安装**

#### **最终载荷-backgroundTaskHost.exe分析**

最终载荷通过死循环一直与gawdkl.fit保持连接。

![](https://mmbiz.qpic.cn/mmbiz_png/u1Oy5xQ01SpEPg0pqtoQdibiawAzw9Zwp3TILWJM2tPOCGMaOtLy214JhQG9YPnDeGZYttdu0TI8NhLBptaqGOaGbK08MicrDZsLw6ZzPN1Ff0/640?wx_fmt=png&from=appmsg)

功能调度涉及到的指令非常多，后续插件的安装都是通过指令完成。

![](https://mmbiz.qpic.cn/mmbiz_png/u1Oy5xQ01SrJCepibsBcj34OUK2tiaTHFUTnaqYWhJ3YepzL8WY3Vt587wp5d6zuMpZPu7P2vc8VT0JGL1EiaaCJQkZvW1N4Ozyp1ic1HGUSeGY/640?wx_fmt=png&from=appmsg)

总计80条指令，有效指令为41条。下方按照功能归类指令。归类五大类分别对应：

1、基础控制与信息采集

2、远程控制

3、进程与系统管理

4、多媒体操作

5、插件系统

|  |  |
| --- | --- |
| 指令(16进制/10进制) | 功能 |
| 0x05 (5) | 断开连接（基础控制与侦查） |
| 0x04 (4) | 心跳/时间同步（基础控制与侦查） |
| 0x02 (2) | 系统指纹上报（基础控制与侦查） |
| 0x105 (261) | 定向进程枚举（基础控制与侦查） |
| 0x107 (263) | 安全软件/AV检测（基础控制与侦查） |
| 0x200 (512) | 屏幕捕获启动（远程控制） |
| 0x202 (514) | 屏幕捕获停止（远程控制） |
| 0x203 (515) | 屏幕控制参数（远程控制） |
| 0x204 (516) | 请求屏幕帧数据（远程控制） |
| 0x206 (518) | 鼠标/键盘注入 （远程控制） |
| 0x20C (524) | 输入注入器选择 （远程控制） |
| 0x207 (519) | 读取剪贴板 （远程控制） |
| 0x209 (521) | 设置剪贴板  （远程控制） |
| 0x402 (1026) | 进程列表枚举（进程与系统管理） |
| 0x404 (1028) | 终止进程（进程与系统管理） |
| 0x408 (1032) | 结束进程任务（进程与系统管理） |
| 0x40A (1034) | 挂起/恢复进程（进程与系统管理） |
| 0x40C (1036) | 设置进程优先级（进程与系统管理） |
| 0x40E (1038) | 终止进程树（进程与系统管理） |
| 0x410 (1040) | 服务/驱动枚举（进程与系统管理） |
| 0x412 (1042) | Windows服务控制（进程与系统管理） |
| 0x20B (523) | 唤醒/防休眠（进程与系统管理） |
| 0x406 (1030) | 关机/重启/注销（进程与系统管理） |
| 0x502 (1282) | DirectInput转发（进程与系统管理） |
| 0x504 (1284) | 窗口事件转发（进程与系统管理） |
| 0x505 (1285) | 窗口移除/注销（进程与系统管理） |
| 0x507 (1287) | 窗口注册/心跳（进程与系统管理） |
| 0x700 (1792) | 摄像头捕获启动（多媒体捕获） |
| 0x702 (1794) | 摄像头捕获停止（多媒体捕获） |
| 0x703 (1795) | 摄像头标志设置（多媒体捕获） |
| 0x704 (1796) | 摄像头枚举（多媒体捕获） |
| 0x800 (2048) | 音频捕获启动（多媒体捕获） |
| 0x802 (2050) | 音频捕获停止（多媒体捕获） |
| 0x900 (2304) | 插件注册/加载(插件系统) |
| 0x902 (2306) | 插件写入数据  (插件系统) |
| 0x903 (2307) | 插件提交数据  (插件系统) |
| 0x909 (2313) | 插件启动 (插件系统) |
| 0x90A (2314) | 插件停止 (插件系统) |
| 0x906 (2310) | 插件枚举 (插件系统) |
| 0x905 (2309) | 插件卸载 (插件系统) |
| ≥0x1000 (≥4096) | 插件分发 (插件系统) |

在测试期间得到指令顺序为

|  |  |
| --- | --- |
| 2 | 系统指纹上报 |
| 4 | 心跳协调 |
| 0x101 | ping |
| 0x900 | 插件注册 |
| 0x107 | 安全软件/AV检测 |
| 0x105 | 定向进程枚举 |

插件安装接收回来的数据写入在HKEY\_LOCAL\_MACHINE\SOFTWARE\Microsoft\Tracing\choco\_crm\ID\Bin32。通过解密实际上是下载者，每30分钟下载一次。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/u1Oy5xQ01SpYHE81VygesgVCkjmtN3pHf9IKcicXpZib6H4fQZrQECEdo2myq8VJwLiaicbFiafHNbXIS8vpuzT4omT0yV7OVoMibbezg2yVHSvm4/640?wx_fmt=png&from=appmsg)

最后从https://s3.ap-east-1.amazonaws.com/0xdadb0d80178819f2319190d340ce9a924f783711/PopAD.exe下载回该广告弹窗软件并执行。

![](https://mmbiz.qpic.cn/mmbiz_png/u1Oy5xQ01SribKQMicWUviaW6BZlbVMGaORXyQAmOic7FDUKsJDKxN4hiaAmiaqIAiaiaJrGxXPMIoHibdbptTAmtOOQOoIAicFzAojKk6iaDfEUt7lJqM/640?wx_fmt=png&from=appmsg)

同时还有验证文件PopAD.exe.meta文本，该文本记录更新时间是否正确。这也是判断该软件时效性的依据之一。Wed, 01 Jul 2026 15:08:37 GMT对应北京时间2026年7月1日23:08:37。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/u1Oy5xQ01Sp67l8EI0t6RuibzFIhxiaziceQiaKINkMxLzm90Sibavqn3zsMe5JuysSibMR5ibtV4ZoXzyJsVDSyFVOw5MdrEXjtxeiaK3u89kBMKdE/640?wx_fmt=png&from=appmsg)

### **弹窗广告PopAd.exe**

通知上线的C2以明文的形式存在https://dnyk123.xyz/boot与api token用于服务器验证QHf1GHeq3zV-6pTPsCRwYpJpMyMyspNdaA059i3WpIk。

![](https://mmbiz.qpic.cn/mmbiz_png/u1Oy5xQ01SovLZhDwGpan0F7ROVzTOJmL0TbwicMwHMicn6UkTQibBOiaibthgKic2fiaHMCla8Ms1XfjsWkkybaMWbcA1ZOiapyAgQeyj54Jh5...