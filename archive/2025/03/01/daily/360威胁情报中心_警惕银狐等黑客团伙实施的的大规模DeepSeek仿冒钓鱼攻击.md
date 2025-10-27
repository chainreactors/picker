---
title: 警惕银狐等黑客团伙实施的的大规模DeepSeek仿冒钓鱼攻击
url: https://mp.weixin.qq.com/s?__biz=MzUyMjk4NzExMA==&mid=2247505670&idx=1&sn=9a0b8bdbc1102d73a87ca021bf26ede6&chksm=f9c1e40fceb66d193492d1fa86b3314ffd5d2867198e7d452a8add1cd7b2ff9cda87a163a890&scene=58&subscene=0#rd
source: 360威胁情报中心
date: 2025-03-01
fetch_date: 2025-10-06T22:01:23.472642
---

# 警惕银狐等黑客团伙实施的的大规模DeepSeek仿冒钓鱼攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/6CNEHNicic4PozPNbcDapVk0hzW7AcaRP1zsNgemO807Bh9ntGO93ujm5D0b8n1g0Y1HBJwNtc9fU68NejyhwxVw/0?wx_fmt=jpeg)

# 警惕银狐等黑客团伙实施的的大规模DeepSeek仿冒钓鱼攻击

360威胁情报中心

随着人工智能技术的飞速发展，大型语言模型如DeepSeek的本地化部署已成为行业趋势。这不仅为企业和开发者提供了定制化AI解决方案的便利，也为网络安全领域带来了新的挑战。

近期，我们观察到银狐等黑客团伙的大规模攻击活动，这些团伙正在利用DeepSeek本地化部署的普及，发起一系列精准的钓鱼攻击。这些攻击并非简单的恶意软件传播，而是结合了社会工程学和高超的技术手段，针对DeepSeek用户精心设计。

一、攻击方式

1. 钓鱼网站诱导下载

伪造DeepSeek官方网站，从界面上看足以以假乱真，域名多与deepseek.com相近，诱骗用户输入敏感信息，下载安装病毒木马。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PozPNbcDapVk0hzW7AcaRP1b5esU5GSNSw7130kO8FuHahwX8H6XicDIqaZaWHykQFGcicAMcQzSdIQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PozPNbcDapVk0hzW7AcaRP1RnicrZNL30x1Mqic7ibojbGYtuEvbm8tmXqtRBj096k8C4x8ianGlVEZSw/640?wx_fmt=png&from=appmsg)

2. 文件名伪装

采用“ds大模型安装助手”、” DeelpSeek\_windowsAI助手”等文件名，用户点击运行之后，会被植入远控或窃密木马。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PozPNbcDapVk0hzW7AcaRP1LBjEvwCTHvXfuAd0icVunj0qDB8uuLuSt0AyIJoS1vf45icwiaVEiafWOQ/640?wx_fmt=png&from=appmsg)

二、攻击分析还原

下面选择3个典型攻击样本对攻击过程进行还原。

0x1  样本一

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PozPNbcDapVk0hzW7AcaRP1mVVwGs1VIs6eNgIia3xcvsWK5IKZ77ZnbnTXnPOTIDmHrdVmrSrwcYg/640?wx_fmt=png&from=appmsg)

攻击流程如下：

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PozPNbcDapVk0hzW7AcaRP1icLNQstgADvZSqIQ8z9LFBNEWfExWEDc3zcQ1e7EgiavEqM0nNLullMA/640?wx_fmt=png&from=appmsg)

从钓鱼网站下载压缩包解压后包含DeepSeek Installation.lnk文件，该快捷方式可以执行powershell命令，访问https://raw.githubusercontent.com/lee2313456/f/refs/heads/main/f 获取命令并执行。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PozPNbcDapVk0hzW7AcaRP1ibPO3rWZK2DozGEGTqLVOkZzFEwBAFbfvibwjibn3HGafPUHAXnqH9jwQ/640?wx_fmt=png&from=appmsg)

获取的命令如下所示，下载f.zip 解压后执行1.bat。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PozPNbcDapVk0hzW7AcaRP1NzDkRXfFiaFEySiaPPTFU9lRrQf2MfhNEsV66htyfXNcDz23mMIbvELA/640?wx_fmt=png&from=appmsg)

f.zip解压后如下图所示。解压出的svchost.exe是python主程序，1.bat调用python主程序执行窃密脚本python.py

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PozPNbcDapVk0hzW7AcaRP1HIl3URLC5vQWUe8IywV6rGsfKyo0ibDOulPJlkDKRMla7BJutJhxCcg/640?wx_fmt=png&from=appmsg)

python.py可以窃取浏览器cookie、应用程序凭据、文件等多种信息，通过telegram发送给攻击者。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PozPNbcDapVk0hzW7AcaRP1YJ1eh85eYbLkAVqe1TcIDbWxQx17pYu8gHIuftfibLwDg4CC3CA3JaA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PozPNbcDapVk0hzW7AcaRP14VQItaib30yGuib6ChqfxniaxJ9iaP64N175MOjwpicYcbNYv1IVxO6wrEg/640?wx_fmt=png&from=appmsg)

0x2  样本二

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PozPNbcDapVk0hzW7AcaRP1YgcLVrbUwWakTg2dKFgUvusc0ljic1q4jUmia5GRUpSCZRF5iaYVBvEZA/640?wx_fmt=png&from=appmsg)

攻击流程如下：

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PozPNbcDapVk0hzW7AcaRP1oeDoD5sAeCjBrCjicrXHXgK0bUBWNQuCUIq3zZNkogmM6CIHrBDOT1g/640?wx_fmt=png&from=appmsg)

从钓鱼页面下载伪装成"DS大模型安装助手"的恶意样本（ds大模型安装助手\_1.0.0.6\_1740119628.exe）。

恶意样本采用WinRAR自解压技术封装，执行后除了运行正常的安装助手程序外，会静默释放并执行恶意程序“ds大模型安装助手响应.exe”，以此规避用户感知并建立持久控制。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PozPNbcDapVk0hzW7AcaRP1KWamttW7v9oviaCQMa3thBKSRuh7micGke9qvl7wgVpDSlHia4bQIG7icg/640?wx_fmt=png&from=appmsg)

恶意程序由Golang编写，运行后首先检测当前进程权限，若未获取管理员权限则通过GitHub开源模块提权并重新启动自身。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PozPNbcDapVk0hzW7AcaRP1rwSjl6wwvk0ribhOUCyRURCJAWN5Tvlu7m8uZJCdyiaA6aLG2fwsKdBA/640?wx_fmt=png)

成功提权后，释放无影云桌面客户端程序及恶意组件vcruntime140.dll到C:\ProgramData\{UUID}\目录下，通过DLL侧加载的方式加载恶意模块vcruntime140.dll。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PozPNbcDapVk0hzW7AcaRP1f4lic5Z5azZ9iaVOnhta6tsqbxCIib6n2nuLiafMOXLiamWqBHwUJrZuEBw/640?wx_fmt=png)

恶意模块vcruntime140.dll由C语言和Golang语言交叉编译而成，功能是从wuying\_focusmode.exe.db中读取解密密钥，然后解压，解密，反射加载最终的NewC2木马模块。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PozPNbcDapVk0hzW7AcaRP1J3cKcqOqfh6Jv1VHA9XofFDBsYtiayqRiaERfttyAvxevVvicgWM7pzicQ/640?wx_fmt=png)

NewC2木马模块由Golang编译，主要由键盘窃听，Tg加密传输，反射Shell，浏览器数据窃取等功能组成。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PozPNbcDapVk0hzW7AcaRP1XI7lCpArfTib6ZthruQ0ueMNtqxV53scBCQZGxtPHCEGUrgxGklawkA/640?wx_fmt=png)

0x3  样本三

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PozPNbcDapVk0hzW7AcaRP16XnXcrnsKEVXia9NmCpo4Bojtxdvcww8n9TOwh3arMiagLf0swFsE3dQ/640?wx_fmt=png)

攻击流程如下：

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PozPNbcDapVk0hzW7AcaRP1WeS0pict7bbrXWgslLMNaE6AeiaqtKeYgZ6BRcvkTqcAG9DGDUPDvNkQ/640?wx_fmt=png)

攻击者诱导用户从钓鱼网站下载恶意安装包DeepSeek.msi，运行后释放正常Deepseek安装包以及恶意组件Autoshell.dll、 AuthShellXor.bpl、 mods.dat。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PozPNbcDapVk0hzW7AcaRP1zWtZrm5CIqIpNNjlIAtxvlnGzqstlnh1YK7UPxUDAsteviatNhAu97w/640?wx_fmt=png&from=appmsg)

然后通过白文件update.exe加载恶意模块Autoshell.dll 。恶意模块解密AuthShellXor.bpl执行shellcode,  shellcode读入mods.dat并解密执行。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PozPNbcDapVk0hzW7AcaRP1ovqDFaWYwzx4PLS4FS7FyM67U6gDyAXnCVqfVNK9VAd6PeYR28TZPw/640?wx_fmt=png)

解密后的mods.dat 是PE文件，导出名为“上线模块.dll”。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PozPNbcDapVk0hzW7AcaRP1Oic4myQ1JRG96mhk7krzb8sqfRLrVnSApwk0vstfdb6yEMiaG71O241g/640?wx_fmt=png&from=appmsg)

“上线模块.dll”具有银狐远控的明显特征， C&C 为45.192.168.12:8080。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PozPNbcDapVk0hzW7AcaRP1PPD9Ha9cicbyW3fSCrUcV7UFRlR9Prlso8cxgia1ffSFHVvyJqce6Xcg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PozPNbcDapVk0hzW7AcaRP1jlzQ7MViaQwKdSMxI4paorpVpkWn36jGibjMIiaJOeq9vR7cO0jqb69eA/640?wx_fmt=png&from=appmsg)

##

**结语**

随着DeepSeek在人工智能领域的持续走红，不法分子开始构建大量钓鱼网站，利用其市场热度大肆传播。对近期各种钓鱼攻击的分析中我们发现，恶名昭著的银狐木马团伙也加入了这一攻击浪潮。360建议需要部署或测试DeepSeek的IT从业人员注意外部应用的来源可信度，广大政企机构应尽快构建更加体系化、实战化、智能化的数字安全防御体系。

**附录 IOC**

样本Hash

e62ce0f1a63c2bf13e2d7a8a42e4190d

3e0f160a626452fa1cb29b8ee3149e4f

4039d84a8bdccbd0ff83be0a2af168af

27349604af6bc596f5de89ee23c0fd97

e1ea1b600f218c265d09e7240b7ea819

3fe225c0e5d2659b673692a1d26c5b1b

675bee62ae421f6a3ab46a151bccbcc0

2925768d3ca1faf2b2886218f86b7ca0

4ef18b2748a8f499ed99e986b4087518

d0463c58aa587a19a0f6d8b5589646a4

b6c0ac181f008887afa7c525584df63f

2b62aba98292f7d7098cf8fd580bffb4

f033ef2b4f2b6462e20526bf6a5d6b5f

0ea1db82cf64e59b8774e0eff16282a6

155bdb53d0bf520e3ae9b47f35212f16

8ead807e9635044223ed8f38067daa9e

31ee1603e608bf34cf3c8ae6f3bdbcf4

48e5c06644ff515bda87d9df38644589

4e30b154756e702ee08ffd42856d4ca5

0ccc397f9cdcf5d6a427d0bbc4737075

钓鱼页面：

deepseek.tt1gg4[.]icu

app.deepelseek[.]top

depseek[.]shop

zzxzas[.]top

web.depseek[.]top

app.dealpseek[.]top

app.dieepseeka[.]top

app.deapseek[.]top

deeopal[.]top

dpsk.dghjwd[.]cn

app.ucnj3iu[.]icu

wvw.deepseekc.top

ww.djm43j[.]icu

ww.sfplfwk3[.]icu

ww.oegwli3[.]icu

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Pruscv37D0qgOMbfC4jVxUnso6yyhQC9OIyDNX6TYo5k8iafcfZMzT0ia5boCo69WZSicq7krbicKaHsw/0?wx_fmt=png)

360威胁情报中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Pruscv37D0qgOMbfC4jVxUnso6yyhQC9OIyDNX6TYo5k8iafcfZMzT0ia5boCo69WZSicq7krbicKaHsw/0?wx_fmt=png)

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