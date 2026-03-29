---
title: 【红队工具】VShell v4.9.3 高级版
url: https://mp.weixin.qq.com/s/59bNN2vLx2J8HEFOOCdeWA
source: Doonsec's feed
date: 2026-03-28
fetch_date: 2026-03-29T04:35:26.280989
---

# 【红队工具】VShell v4.9.3 高级版

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ibzm8nWOdauOGAjhcjljGLzMujicvMCgnH0ewKAfrKUbcTEpUrsSVC87sJkbWaKPVZXGDViaPfAFQGXuZHCVqMZOJTyKpYenxUicJzhJ3OaekEU/0?wx_fmt=jpeg)

# 【红队工具】VShell v4.9.3 高级版

原创

小智
小智

智榜样网络安全学习中心

![]()

在小说阅读器中沉浸阅读

> ❝
>
> **💖 温馨提示：**用好这个轻量化的 C2，能让红队在渗透初期打得更快，另外有一点必须预先声明，后续所有关于技术的探讨，皆以获得授权的环境为基础，用于合规的安全测试或系统运维学习，切不可将其挪作他用。

## 一、前言

红队行动，前期突破的速度和隐蔽程度，很大程度上就定了成败的调子， 在那种系统混杂、内网条条框框多、防守方眼睛又多的环境下，一个轻巧、原生就吃 Linux、隧道又好使的 C2 就显得特别关键。

VShell，算是国产 C2 里一个挺有代表性的东西，虽然现在不开源了，但操作体验顺滑，对 Linux 的支持也相当完整，所以在圈内用的人不少，这篇文章将逐步演示 VShell v4.9.3 高级版，从配环境、建监听、搞载荷，一直到让目标上线和搭隧道，顺带也会聊聊我自己实战里的一些心得和踩过的坑。

## 二、工具基础信息与对比

那么，VShell 到底是个啥，为何讲它是「前期突破利器」，

动手部署前，得搞清楚 VShell 是干嘛的，它的设计初衷就是为了「快速突破」，特别适合用在前期拿点、架隧道和捞个初始权限， 至于 Cobalt Strike（CS），那家伙更偏向于后期的横向渗透和权限巩固。

要说这**两者的核心区别**，VShell 的现状是 GitHub 上找不到了，属于圈内流传的闭源状态，而 CS 那边官方还在持续更新，插件生态也成熟得多，

VShell 的核心强项体现在操作的流畅感、对 Linux 的原生支持，还有就是搭隧道特别方便，反观 CS，它的强项在于横向移动的手段花样多，后渗透的功能也更完备，

对于 Linux 系统的支持，VShell 可以说是开箱即用，功能完整，而 CS 则需要依赖第三方插件，功能上存在一些限制，

所以适用阶段就很明确了，VShell 主攻前期打点和建隧道，拿到滩头阵地，CS 则接手后续的横向扩张和长期驻留。

总结一下，他们的主要区别

| 对比维度 | VShell v4.9.3 | Cobalt Strike（CS） |
| --- | --- | --- |
| 工具当前状态 | GitHub 已下架，闭源模式，版本靠行业内私下传播 | 官方持续维护，插件生态成熟，开源社区支持丰富 |
| 核心能力优势 | 操作流畅无卡顿，适配前期打点与隧道搭建，Linux 原生支持 | 横向渗透手段多，可自定义修改特征码，后渗透功能完善 |
| Linux 系统支持 | 无需额外插件，Linux 目标上线与操作功能完整 | 依赖第三方插件实现 Linux 支持，功能局限性较强 |
| 适用渗透阶段 | 前期：目标打点、隧道建立、初始权限获取 | 后期：横向移动、权限维持、域内渗透 |

> ❝
>
> **🌞我的经验：**VShell 在处理 Linux 目标上线和做隧道代理时的那种顺畅体验，是多数开源 C2 比不了的，我自己在一次真实项目里，前后也就花了 3 分钟，就用 VShell 把目标搞上线，顺手建了个 Socks5 隧道，直接为后面的渗透操作打开了局面。

### 1.1 工具下载

VShell 现在主要靠圈内人互相分享，这里有个验证过的网盘链接，

链接: https://pan.baidu.com/s/1LGb4RPgxmJPDEdZlaHQOkA

提取码: ju5z

> ❝
>
> **💖 温馨提示：**网络安全安全方面，毕竟是闭源的东西，用之前最好在隔离环境里跑跑看看有没有后门，免得引狼入室。

## 三、VShell 部署与环境配置

### 2.1 工具上传与权限配置

首先将下载的 VShell 压缩包解压，把所有文件上传到 Kali 虚拟机中（本地测试推荐 Kali，实战中建议部署在 VPS 上）。上传完成后，先进入工具根目录，会发现核心执行文件为`v_linux_arm64`

```
# 进入工具存放的根目录
cd /data/vshell/
# 解压此文件到当前目录
unzip vshell-v4.9.3-linux_arm64.zip
```

![image-20251030141310083](https://mmbiz.qpic.cn/mmbiz_png/ibzm8nWOdauMyDQJwmRicCkicJQfZ3dBSGeIRsMzv1gRpfLvkzAkAm7wLbEAugiavmpf27zuZ2ZUAcfzCNXZnPzMjCzJ3hGemwFHYklX0Owwvow/640?wx_fmt=png&from=appmsg)

image-20251030141310083

### 2.2 解决架构不兼容问题

如果直接执行`./v_linux_arm64`，大概率会出现 “exec format error” 报错 —— 这是因为当前 Kali 多为 x86/x64 架构，而`v_linux_arm64`是为 ARM64 架构编译的程序，二者不兼容。

![image-20251030141831725](https://mmbiz.qpic.cn/sz_mmbiz_png/ibzm8nWOdauPqaR60NItOTTfxbLGRhvpAh5IRAbiaUVO66ahpUQoxOBDpcrfChQicKtSnJiac09anjbdBxOGvr90a48ibaNGxgywvd7K5Sc6UHw4/640?wx_fmt=png&from=appmsg)

image-20251030141831725

解决方法是安装 QEMU 模拟器，通过模拟 ARM 环境实现程序运行：

```
# 安装QEMU模拟器及ARM架构支持包
apt-get install qemu-user-static
```

![image-20251030142029945](https://mmbiz.qpic.cn/mmbiz_png/ibzm8nWOdauO6icDUjzRpOKibd4b5u9qSNbbqBr4MmPiaXntGiamuPAueVH380I1Bk2egNoa3J5HhaiaMuYBfpyvsO8SXSkLokLOEWREA51tvdAQM/640?wx_fmt=png&from=appmsg)

image-20251030142029945

安装完毕再执行`./v_linux_arm64`，即可正常启动（若还报错则重启Kali后重试）。

### 2.3 核心配置修改

VShell的配置全部在`./conf/setting.conf`文件，无需做任何的参数设置，只需注意登录**账号密码**和**启动端口**即可：

```
# 编辑配置文件
vi ./conf/setting.conf
```

![image-20251030141249128](https://mmbiz.qpic.cn/mmbiz_png/ibzm8nWOdauO3ANRyemibAPJYeRCiaiaO0cbymP9eNSqzeejdgibicHkWGBosmXttiaoZe4r4icF7Q94YGH7Y6Cibj5nkBfONLQptH51KflXhh98VAAs/640?wx_fmt=png&from=appmsg)

image-20251030141249128

#### 2.3.1 账号密码配置

找到`web_username`和`web_password`字段，默认值分别为`admin`和`qwe123qwe`。实战中建议修改为复杂密码（如`VShell@2025!`），避免被未授权访问：

```
# JWT密钥（按作者提示留空即可，无需填写）
web_jwt_secret=
# 登录账号（可自定义）
web_username=admin
# 登录密码（建议修改为强密码）
web_password=qwe123qwe
```

![image-20251030172658720](https://mmbiz.qpic.cn/sz_mmbiz_png/ibzm8nWOdauOvYdcpUvO3WhwzTfVf3MHSTGYLNqibvGO3w6KgqDbPZmH1fSMAN1icNM9fiaYyJThdHyADInlSOnMmLfMVr9oMdEdL7wgIiaVBrsM/640?wx_fmt=png&from=appmsg)

image-20251030172658720

#### 2.3.2 启动端口配置

找到`web_port`字段，默认端口为`8082`。若该端口被占用（可通过`netstat -tuln | grep 8082`检查），可修改为其他未占用端口（如`8090`）：

```
# 管理后台界面的标题，可自定义为xxx安全团队渗透系统
web_title=管理平台
# 管理端Web界面端口
web_port=8082
# 让工具监听当前机器上所有可用的网络接口
web_ip=0.0.0.0
```

![image-20251030173253193](https://mmbiz.qpic.cn/mmbiz_png/ibzm8nWOdauPOqiahCpTcuGSgyhybmB2saCS2hguQMEYOVuQQINDJGAMpd0S4cequWz65MZa1HmuuLzY0Eb3BW1mxF7VD9I2yzCjzYWy899Nw/640?wx_fmt=png&from=appmsg)

image-20251030173253193

修改完成后，按`Esc`键，输入`:wq`保存并退出 vi 编辑器。

## 四、VShell 启动与 Web 管理端访问

### 3.1 启动工具

在工具根目录执行核心文件，这里需要注意，该文件默认无执行权限，需先通过命令赋予权限：

```
# 赋予文件执行权限
chmod +x ./v_linux_arm64
```

![image-20251030141850985](https://mmbiz.qpic.cn/sz_mmbiz_png/ibzm8nWOdauMr2nC6reGKnwlQFHRibJBX4XAEPWHAFrzsaibdcKnibqQib6jtOkIcZezjNHYFm3tBz7VT1XWdaA355jhaYyVhKOSNcm9yZmCscWQ/640?wx_fmt=png&from=appmsg)

image-20251030141850985

启动 VShell 服务：

```
# 启动vshell
./v_linux_arm64
```

![image-20251030142333349](https://mmbiz.qpic.cn/mmbiz_png/ibzm8nWOdauNQqgeFPHAN1BW7Zibp4eUMgOyjuwAdOgk7Se38HthSAhniaLNqzr8tM4ub571QthrcbdFf4gTVqoGHRZiba1LMTCV2O13rQLcOyc/640?wx_fmt=png&from=appmsg)

image-20251030142333349

启动成功后，终端会显示服务运行信息，无需保持终端窗口打开（若需后台运行，可加`nohup ./v_linux_arm64 &`）。

### 3.2 获取 Kali 虚拟机 IP

通过以下命令查看 Kali 的 IP 地址（后续访问 Web 管理端需用到）：

```
ip a
```

![image-20251030173205703](https://mmbiz.qpic.cn/mmbiz_png/ibzm8nWOdauP0qFEV69tSTiaqhI3GPvreSYwC1XlGGIveaH1GNX7j65ynHuRdJrlK4tJ5MuQGOXUeCkl3K49dfVT0OGXj31lIaZ8OhYDH2Ticc/640?wx_fmt=png&from=appmsg)

image-20251030173205703

例如，笔者 Kali 的 IP 为`10.10.10.173`，后续访问需结合配置的端口`8082`。

### 3.3 访问 Web 管理端

打开浏览器（推荐 Chrome），在地址栏输入 “KaliIP: 端口”，即：

```
http://10.10.10.173:8082
```

首次访问会跳转到登录页面，输入之前配置的账号（admin）和密码（qwe123qwe），点击 “登录” 即可进入管理端首页。

![image-20251030142412347](https://mmbiz.qpic.cn/mmbiz_png/ibzm8nWOdauMiaVbjhbTKictgwmyopGTtE9eBib8wwWMrJjWTSDT0HlDu3JsH0fSicd8nlCEme1rcfkVgfl5p6M3eCksMFWsO1Wibqofic4KDhI0VI/640?wx_fmt=png&from=appmsg)

image-20251030142412347

来到了管理登录界面，再次输入账号密码

![image-20251030142447621](https://mmbiz.qpic.cn/sz_mmbiz_png/ibzm8nWOdauMF67HibB3z21vkGbMNicibM40L8rRTZ2HicibMfKgIKzc6u6tvgmzKoel9QrIsB6zfdtticYWibXfjnUWZzjJscnRWa37YZ7RZ6N7kibU/640?wx_fmt=png&from=appmsg)

image-20251030142447621

登录成功后，首页会显示 “客户端管理”“主机管理”“监听器” 等核心功能模块，界面简洁直观，无需复杂学习即可上手。

![image-20251030142510991](https://mmbiz.qpic.cn/mmbiz_png/ibzm8nWOdauOOGOc0F1RtIHyibdqtlCbwaGjwGfCcx0cfH88bnPMP5hDmsfQbObt95fialWOIIGVt4ygDcBObhlgTVEyH4icWo8P5pgCudgVZjs/640?wx_fmt=png&from=appmsg)

image-20251030142510991

## 五、监听器创建与恶意载荷生成

### 4.1 创建 TCP 监听器

监听器是 C2 工具与目标主机通信的 “桥梁”，VShell 支持 TCP、UDP、HTTP 等多种监听器类型，这里以实战中常用的 “TCP 正向监听器” 为例：

点击管理端上侧 “监听管理” 模块，选择 “新增监听”；

![image-20251030205016401](https://mmbiz.qpic.cn/sz_mmbiz_png/ibzm8nWOdauOsaM3fHw7f659CbMWiazNfCORT7MN8SkW9jlce56oOzxVaVIHcjM04VlVAxf5CU4wd9SxApzod9dLHZ5YvX9VZzeAHRnsE7rfA/640?wx_fmt=png&from=appmsg)

image-20251030205016401

监听器类型选择 “TCP”，填写监听器名称（如 “TCP\_Forward\_8084”）并填写 Kali 的 IP（`10.10.10.173`）和监听端口（如`8084`，需确保该端口未被占用）；

![image-20251030205148829](https://mmbiz.qpic.cn/sz_mmbiz_png/ibzm8nWOdauOGFpfkNZgleAduHF98UQq9jOAGlcH2tsSfpr1kkibLQHaoomwUnzYZjQcxM8hc89sSwM1eIRoMJE6ZGtgFyicsp1fCBaMN5FJXw/640?wx_fmt=png&from=appmsg)

image-20251030205148829

其他参数保持默认，点击 “新增” 完成监听器创建。

### 4.2 生成 Windows 恶意载荷

恶意载荷（俗称 “马”）是实现目标上线的核心文件，VShell 支持 Staged（分阶段）和 Stageless（无阶段）两种模式，Stageless 模式生成的载荷可独立运行，更适合绕过简单杀毒软件：

1. 点击上侧 “客户端生成” 模块，选择 “stageless” 载荷；

![image-20251030205252371](https://mmbiz.qpic.cn/mmbiz_png/ibzm8nWOdauPpLIucdYyBWtvODnDT6zqXWZBAkZMtzupabapSUPmuYer0bvkVRuTSMnVArkCc5Xe5VRyXP349DNXpiatu3AwiclzRIUicTbCKiak/640?wx_fmt=png&from=appmsg)

image-20251030205252371

监听器选择刚刚创建的 “TCP\_Forward\_80834”；无需额外配置免杀（基础测试用默认即可，实战需加壳或混淆），点击 “生成”；生成完成后，点击 “下载” 将载荷保存到本地（如`vshell_win.exe`）。

![image-20251030143139049](https://mmbiz.qpic.cn/mmbiz_png/ibzm8nWOdauNicAp2KgwTjQib8lyqZIMwXLs8c8ia0tf2WibjG5q8aqZXGvlZkOrCAJlvB2s7gU8yZqjtVSofrvVlOER0XQZz15SgS91lYy3xBaQ/640?wx_fmt=png&from=appmsg)

image-20251030143139049

## 六、目标上线与基础功能测试

### 5.1 载荷执行与杀毒软件检测

将生成的`tcp_windows_amd64.exe`拷贝到 Windows 测试机（建议关闭实时防护，避免被拦截），先通过电脑管家等杀毒软件扫描 —— 测试结果显示，默认载荷可绕过基础杀毒软件（实战中需结合免杀手段，如 UPX 加壳、资源修改）。

![image-20251030143341227](https://mmbiz.qpic.cn/sz_mmbiz_png/ibzm8nWOdauPngKuG7OotCNFvEFicZQYYeqltkN7sjX03XfrGfmL4UnMFq0iaEa5bSzEm6T8TX6...