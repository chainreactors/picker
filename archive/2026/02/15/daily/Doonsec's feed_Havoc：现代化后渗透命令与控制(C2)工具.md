---
title: Havoc：现代化后渗透命令与控制(C2)工具
url: https://mp.weixin.qq.com/s/tI7wYwJurNxz68AmhcSrNg
source: Doonsec's feed
date: 2026-02-15
fetch_date: 2026-02-16T04:17:20.924145
---

# Havoc：现代化后渗透命令与控制(C2)工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/x2ibBTFXYHicJsHcEJ0jfKqNe0CRCG4KZU7AbVQMXNgDoG5U1ov5icG8VvbTKE5RgAoak3KaoUMpNHtaH7h7EEt9zhy0MFVRQvgS9GRHTkct3I/0?wx_fmt=jpeg)

# Havoc：现代化后渗透命令与控制(C2)工具

原创

网安武器库
网安武器库

网安武器库

![]()

在小说阅读器中沉浸阅读

**更多干货  点击蓝字 关注我们**

**注：本文仅供学习，坚决反对一切危害网络安全的行为。造成法律后果自行负责！**

**往期回顾**

·[PCHunter：一款深度检测隐藏恶意代码的扫描工具（兼容win11）](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486351&idx=1&sn=5ad805f6aa58a79e2f21b777849db642&scene=21#wechat_redirect)

·[Web-SurvivalScan：用于快速验证资产存活的轻量化渗透测试扫描工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486350&idx=1&sn=1a4559b375cda713d02d270ae121bc70&scene=21#wechat_redirect)

·[【已复现】最新版微信v4.1出现远程命令执行漏洞：one-click RCE on Linux WeChat](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486318&idx=1&sn=a39e4ceaadd2fcffea08ecdc48319fc9&scene=21#wechat_redirect)

·[xss\_scanner\_mix：一款自动化深度XSS漏洞扫描工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486302&idx=1&sn=08544ff7835ce01fae582f677ad02a98&scene=21#wechat_redirect)

·[StegoScan：CTF自动化隐写识别和解密工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486301&idx=1&sn=704da2217fce796fe07611b66c3448d4&scene=21#wechat_redirect)

·[Coda：实现Windows/Linux入侵痕迹抹除](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486251&idx=1&sn=c2c9dc8f482b43d9c5c0384d37eeb8a6&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

背景分析

传统 C2 工具的局限性

```
单一用户模式 ：许多传统 C2 工具不支持多用户协作，限制了团队作战能力。
功能固化 ：扩展能力有限，难以快速适应新的安全场景和防护技术。
检测规避能力不足 :传统工具的通信模式和行为特征易被现代 EDR（终端检测与响应）系统识别。
跨平台支持差 ：客户端或服务器往往仅支持特定操作系统，部署和使用受限。
```

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicKCx1kkaoicicMoIkN6pQm7rfJU5en20riaQhiaKkt7RiaS6KEts4uu9rsIxGchEHRrDqfzLO382icdsXTqU3Tv7uBhBuf4NK7FVGoRY/640?wx_fmt=png&from=appmsg)

    Havoc是一个现代化、高度可定制的后渗透命令与控制（C2）框架，由安全研究员 @C5pider 创建。它专为红队操作、渗透测试和安全研究设计，提供了一套完整的工具链，用于在目标网络中建立持久访问并执行各种后渗透活动。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicLFcWU3njoJLdgHgor3xmuuFOaqPIWmmzLYYibUbupsecNXrwJbbwDR8FVDoeLFFbmzDF9qRG2wibSuEsahUtoEzb6TppHrDHfZo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicLJVdyED5qjauJx8LjtyDiaT5Lt6mR6k1dKNEr3efUEvicBWE2hMvnYibArRCaIK898PDKXUjoc5EhYqnfjnia4mr2ibm0zLiczLrDcc/640?wx_fmt=png&from=appmsg)

Havoc 的差异化优势

```
1.多用户协作：团队服务器支持多用户同时操作，实现实时协作和任务分配，适合大型红队演练。2.先进的检测规避技术：集成多种睡眠混淆技术（Ekko、Ziliean、FOLIAGE）、返回地址欺骗、间接系统调用等高级技术，提高在高防护环境中的生存能力。3. 高度可定制：通过自定义 C2 配置文件、外部 C2 支持和模块化设计，允许用户根据目标环境调整策略。4.现代化用户界面：基于 Dracula 主题的深色界面，提供直观的操作体验，降低学习成本。
```

项目地址：

```
git clone https://github.com/HavocFramework/Havoc.git
```

或者直接使用kali(这个就不用去编译等操作，更方便):

```
 sudo apt install havoc
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicKr5F7BAQ6nLSTReuM3XHjZicDUeASTDhXrkY4pbibJa5sSMm5uYKbjY5JOjzvmCXbwkeYzRvtJYr7y3lKPeCFFaD7VM3VFdlibQs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

介绍

系统架构

Havoc 采用三层架构设计：

1. 客户端（Client）

```
跨平台用户界面，使用 C++ 和 Qt 开发现代化深色主题，基于 Dracula 设计提供直观的操作界面，用于管理监听器、代理和执行命令
```

2. 团队服务器（Teamserver）

```
使用 Golang 开发支持多用户协作负责有效载荷生成、监听器管理和客户端通信提供 HTTP/HTTPS 监听器和自定义 C2 配置文件
```

3. 代理（Demon）

```
Havoc 的核心代理，使用 C 和汇编开发提供强大的后渗透功能支持多种高级技术，如睡眠混淆、返回地址欺骗和间接系统调用
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicJwlAku4GOEtgMia8qhLtvIKNsKFmUtQZ5Cz32kndKNdQ4Kibjydic4nTCdD89CRpZlta6GwAGDFGjibKjjxtU1iarnXfRNh0hHBfxU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

操作

依赖组件:

```
sudo apt install -y git build-essential apt-utils cmake libfontconfig1 libglu1-mesa-dev libgtest-dev libspdlog-dev libboost-all-dev libncurses5-dev libgdbm-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev libbz2-dev mesa-common-dev qtbase5-dev qtchooser qt5-qmake qtbase5-dev-tools libqt5websockets5 libqt5websockets5-dev qtdeclarative5-dev golang-go qtbase5-dev libqt5websockets5-dev libspdlog-dev python3-dev libboost-all-dev mingw-w64 nasm
```

#### **客户端构建**

```
cd Havoc/Clientmake./Havoc
```

#### **Teamserever构建**

```
cd Havoc/Teamserver     go mod download golang.org/x/sys    go mod download github.com/ugorji/go
```

```
cd Teamserver
# Install MUSL C Compiler./Install.sh
# Build Binarymake./teamserver -h
# Run the teamserversudo ./teamserver server --profile ./profiles/havoc.yaotl -v --debug
```

### **工具使用**

#### **客户端**cd Havoc/Client  ./Havoc

#### **Teamserver连接**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicLBJJUq0BxFMC4vJnh8rFvdkiaDuat4XhAUAibiaFvHEbvibYc4R0apYuAYSqKPv6FQTq4WDDcnmsVe0ZCEVLK8RUkzCQWIwiaq2CCs/640?wx_fmt=png&from=appmsg)

创建 HTTP 监听器

1. 点击 "Listeners" 标签

2. 点击 "Add" 按钮

3. 选择 "HTTP" 类型

4. 配置：

```
  - Name ：HTTP_Listener  - Bind Address ：0.0.0.0  - Port ：80  - Profile ：选择默认配置文件
```

5. 点击 "Save" 保存并启动

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicJqf0KGaIrKj4HhAuqHY0ZmLsKwHTHNfIjicDNYp0bFlD0ibnHr2DFEibuwic4VSfWnjPbnan7GbNpzBIJUcq5ztaqSyKIFXTIO5EY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicKztkvtcy5U7Iu15sxOyUInJsEEByKw7gsTolD2xZ0griasjGLbgInBXYic1vIwT9tYZAib8tzyMVoa3FnPCxI4E3tlhS5xoJQnTA/640?wx_fmt=png&from=appmsg)

生成 EXE 有效载荷

1. 点击 "Payloads" 标签

2. 选择 "Demon" 类型

3. 配置：

```
  - Listener ：HTTP_Listener  - Output ：exe  - Architecture ：x64  - Sleep ：60000  - Obfuscation ：Ekko
```

4. 点击 "Generate" 生成

5. 保存为 payload.exe

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicIsrMvxTEJJ5duZjkIQj9VgZPHqjcnNr5ibibUPdqZ1hkicuX4rvZOWPCoWMaAFKfuVgfMeNciaePrVXXh4NGibJrTyboXnIe7jx7Q0/640?wx_fmt=png&from=appmsg)

部署并执行有效载荷

1. 通过网络共享将 payload.exe 复制到目标主机

2. 在目标主机上执行： C:\share\payload.exe

验证连接

1. 客户端 "Sessions" 标签中出现新会话

2. 双击会话进入控制台

3. 执行 whoami 命令，确认命令执行成功

4. 执行 systeminfo 命令，获取目标主机信息

    攻击者修改了 Havoc 的“Demon”代理以逃避检测并促进秘密行动。

该恶意软件通过利用一种称为“ClickFix”的方法的网络钓鱼活动进行传播。攻击从一封电子邮件开始，该电子邮件包含一个名为“Documents.html”的  HTML 附件。打开后，此文件会显示一条错误消息，指示用户复制并运行 PowerShell  命令。这个看似简单的步骤启动了感染过程，使攻击者能够控制受害者的系统。

    一旦安装在受感染的系统上，Havoc 就会为攻击者提供一套工具来执行命令、操纵用户权限、窃取敏感数据，甚至进行 Kerberos 攻击。其功能包括：

```
收集系统和用户信息执行文件操作，例如上传和下载数据执行任意命令和有效载荷操纵用户令牌来提升权限进行网络侦察和凭证盗窃
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eRUtCzBCFbaMYy1c7utlweibCFXWsicmm9ebyvInBtdsD0QRlUDTdLib1g/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ujZsao69o9To7R2EPMICOxibwVeWgBhbMqg4icbbohwQibUQoRcx6ymIwZylKcXjdYCZWgQcibhibzqTyA/0?wx_fmt=png)

网安武器库

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ujZsao69o9To7R2EPMICOxibwVeWgBhbMqg4icbbohwQibUQoRcx6ymIwZylKcXjdYCZWgQcibhibzqTyA/0?wx_fmt=png)

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