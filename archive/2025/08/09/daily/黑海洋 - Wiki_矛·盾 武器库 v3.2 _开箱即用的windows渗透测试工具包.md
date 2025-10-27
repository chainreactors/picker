---
title: 矛·盾 武器库 v3.2 |开箱即用的windows渗透测试工具包
url: https://wiki.upx8.com/4828
source: 黑海洋 - Wiki
date: 2025-08-09
fetch_date: 2025-10-07T00:47:57.906371
---

# 矛·盾 武器库 v3.2 |开箱即用的windows渗透测试工具包

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 矛·盾 武器库 v3.2 |开箱即用的windows渗透测试工具包

发布时间:
2025-08-08

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
72811

## **系统简介**

* 本环境旨在提供一个开箱即用的windows渗透测试环境；
* 本项目欢迎转载，转载时请注明原作者和原文链接:[https://github.com/arch3rPro/Pentest-Windows](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2FyY2gzclByby9QZW50ZXN0LVdpbmRvd3M)
* 建议运行环境：【vmware：17.0 】 /【运行内存：8G】 /【固态硬盘：100G】
* 由于Windows11的TPM策略(v3.1PD版已去除TPM，Fusion版本还有)，虚拟机已加密，密码：`123456789` 系统账号：`admin`，密码：`123456` 登录后请及时修改密码!!!
* Pentest-Windows中文名：**矛·盾 武器库**,寓意网络安全是攻防一体的，锋利无比的矛和坚固无比盾，相互依存，合理竞争才能持续发展

⚔️Windows11 Penetration Suite Toolkit 🔰 The First Windows Penetration Testing Environment on Mac M Chips

[![矛·盾 武器库 v3.2 |开箱即用的windows渗透测试工具包](https://www.ddosi.org/wp-content/uploads/2025/06/1818-1.webp)](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuZGRvc2kub3JnL3dwLWNvbnRlbnQvdXBsb2Fkcy8yMDI1LzA2LzE4MTgtMS53ZWJw)

## **虚拟机下载**

版本发布情况如下，其他版本正在制作中，敬请期待！：

* Mac M芯片 Arm64 Fusion版本 v3.0
* Mac M芯片 Arm64 Parallels Desktop版本 v3.1
* Windows/Mac Intel x64 Vmware 版本 v3.2
* KVM/PromoxVE Qcow2版本 v3.2
* VirtualBox OVF版本
* Hype-V 和 Ventoy引导启动版本

用VitePress搭了一个静态站，方便后续发布和文档更新。

[![矛·盾 武器库 v3.2 |开箱即用的windows渗透测试工具包](https://www.ddosi.org/wp-content/uploads/2025/06/1818-2.webp)](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuZGRvc2kub3JnL3dwLWNvbnRlbnQvdXBsb2Fkcy8yMDI1LzA2LzE4MTgtMi53ZWJw)

## 下载地址:

[https://arch3rpro.github.io/download](https://blog.upx8.com/go/aHR0cHM6Ly9hcmNoM3Jwcm8uZ2l0aHViLmlvL2Rvd25sb2Fk)

备用地址(Netlify):[https://arch3rpro.netlify.app/download](https://blog.upx8.com/go/aHR0cHM6Ly9hcmNoM3Jwcm8ubmV0bGlmeS5hcHAvZG93bmxvYWQ)

> * 当前使用百度云网盘，已开通置顶issue存放其他网盘下载地址，欢迎大家一起参与！

## **工具需求收集**

已经在腾讯文档上，创建了Pentest-Windows 工具需求收集表，用于征集一些比较好用的工具，加入到后续版本更新中！

可通过访问下方链接进行填写，填写时请遵守下述需求收集规则，谢谢！

* 【腾讯文档】工具需求收集表 [https://docs.qq.com/form/page/DTEJva2Z3cnNjUFdL](https://blog.upx8.com/go/aHR0cHM6Ly9kb2NzLnFxLmNvbS9mb3JtL3BhZ2UvRFRFSnZhMlozY25OalVGZEw)

可通过访问以下链接，查看工具需求收集结果和版本更新状态

* 【腾讯文档】工具需求收集结果 [https://docs.qq.com/sheet/DTHpudHlMQVVQeEFk?tab=ss\_wqwwpb](https://blog.upx8.com/go/aHR0cHM6Ly9kb2NzLnFxLmNvbS9zaGVldC9EVEhwdWRIbE1RVlZRZUVGaz90YWI9c3Nfd3F3d3Bi)

### 需求收集规则

* 提交需求前，请确认该工具是否可用；
* 提交需求前，请确认该工具在[工具需求收集结果](https://blog.upx8.com/go/aHR0cHM6Ly9kb2NzLnFxLmNvbS9zaGVldC9EVEhwdWRIbE1RVlZRZUVGaz90YWI9c3Nfd3F3d3Bi)上是否已经有人提交过了，避免需求重复提交；
* 工具是否收录，取决于工具的易用性和实用性；
* Maye工具箱内的工具需要logo，如果有比较好的设计，请上传logo；
* 为了确保虚拟机的体积大小，尽量不要提交特别大的工具，非常牛逼的除外；
* 工作较忙，版本发布时间不固定，请谅解！

## **版本介绍**

```
1. 最新版本：v3.2 x64架构的【VMware|PVE-KVM】，Mac M芯片的Arm架构【Fusion|Parallel Desktop】已发布VirualBox版本制作中 ：)
2. v3.1版本基于Windows11官方ARM版ISO，博主自己精简制作的镜像；
3. 精简系统自带软件，美化终端字体及部分图标，适度优化；纯精简优化不带工具的系统镜像后续也会放出来；
4. 镜像系统硬盘100GB，使用单磁盘文件存储，提升性能；（更新中，尽量精简镜像大小）
5. 工具图标已重新构建，每个工具都有对应图标；
6. 2.1加入scoop包管理器对大部分软件和工具进行管理，支持scoop update + 工具名称进行更新；
7. 2.2已解决scoop对脚本类工具进行管理，支持脚本类的工具使用scoop安装和更新；
8. Windows Terminal进行优化，采用统一的主题风格和oh-my-posh进行增强；
9. v3.0版本增加内网渗透、凭据获取、VPN网络多个分类工具，其他分类工具也做了更新版本和补充，当前工具数量已增加至 360+，需要新增的工具可在issue中进行提交；
10. v3.0版本工具箱使用新版本Maya Lite，支持子分类，工具归类更加清晰；
11. v3.0版本工具箱内，所有工具都添加了注释，鼠标移上去会显示工具介绍；
12. 已更新Scoop环境变量，命令行工具直接在CMD或Powershell命令行下输入工具名称+参数即可；
13. 删除了部分已不再维护或基本不用的工具；
14. WSL由于使用频率不高，占用空间太大，且Arm版本暂不支持WSL安装，暂时移除，后续看需求量考虑是否加入；
15. v3.1版本Chrome添加标签页管理，已经导入了此项目的工具链接，可直接访问；
16. v3.1版本 Maye工具包分类和子分类添加了emoji进行美化展示
17. v3.2版本 优化图形化bat工具的启动方式，添加vbs无CMD弹窗启动
18. v3.2版本 KVM虚拟机已安装QGA和VirtualIO驱动，已在ProxmoxVE中适配，导入即可使用（建议用RDP远程）
19. v3.2版本 添加了UniGetUI管理，支持图形化对scoop安装工具和软件进行更新
```

## **v3.x 版本变化**

```
新增工具清单和移除工具清单待补充（没时间整理，吐血）
```

## **版本遗留问题**

```
暂未发现，待补充，有问题提issue
```

## **补充介绍**

* 具体支持的工具列表和工具是否有更新版本，请查看[https://github.com/arch3rPro/scoop-bucket](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2FyY2gzclByby9zY29vcC1idWNrZXQ) ；
* 部分机器不支持虚拟化嵌套或者本机安装hype-v会冲突，请使用不装kali-WSL的NoWSL精简版；
* 工具默认处于初始安装状态，部分工具需要进行初始化，少量工具因为要安装插件所以手动配置了。

## **制作声明：**

```
1. 所有的安装类软件均下载自软件对应的官方网站；
2. 所有的绿色类软件均下载自果核剥壳。（https://www.ghxi.com/）；
3. 所有的脚本类工具均下载自github。
4. 部分授权类工具（破解版）及优秀的渗透工具来自微信公众号分享；
5. 本项目制作的初衷是帮助渗透新手快速搭建工作环境，工欲善其事，必先利其器；
6. 本项目由于后期调试原因可能会遗留部分本人的信息，请直接忽视；
7. 本项目坚决不接受也从未曾接受任何形式的赞助。
```

## **免责声明：**

```
1. 本镜像仅面向合法授权的企业安全建设行为，如您需要测试本镜像的可用性，请自行搭建靶机环境；
2. 在使用本镜像进行检测时，您应确保该行为符合当地的法律法规，并且已经取得了足够的授权；
3. 如您在使用本镜像的过程中存在任何非法行为，您需自行承担相应后果，作者将不承担任何法律及连带责任。
```

## 软件及工具介绍：

### 0. 基础介绍

* 🪟：由scoop进行管理和安装，支持一键安装和更新；
* 🐧：由Kali WSL 安装和启动 ，端口监听请开启wslpp；
* 💾：脚本类工具，在Windows中启动，运行时需要的依赖包，由手工完成安装；
* 🌐：在线类安全工具，访问时需要网络，部分需要科学上网；
* 📖：离线知识库，包含密码字典、工具使用、漏洞利用、免杀教程等PDF和Markdown文件。

### 1. 编程环境及集成开发环境：

* Python v3.10.11 (D:/Base/apps/Python310) 🪟
  + 启动命令：`python3 test.py`
  + 已集成本镜像所有python3工具的依赖库
  + 使用`pip3`命令调用python3 pip

* Python v2.7.18 (D:/Base/apps/Python27) 🪟
  + 启动命令：`python2 test.py`
  + 已集成本镜像所有python2工具的依赖库
  + 使用`pip2`命令调用python2 pip

* JRE v1.8.0\_381 (D:\Base\apps\liberica17-jre\current\bin)🪟

* Perl v5.36.1 (D:\Base\apps\git\current\usr\bin\perl.exe) 🪟

* Ruby v3.2.2 🪟

* TDM-gcc v10.3.0 (D:\Base\apps\tdm-gcc) 🪟

* Laragon v5.0.0 (D:\Base\apps\laragon) 🪟
  + Nginx v1.14.0
  + Apache v2.4.43
  + PHP v5.4.9
  + MySQL v5.1.72

* Git v2.41.0 (D:/Base/apps/git) 🪟

* Curl v8.1.1 (D:/Base/apps/Curl/bin) 🪟

* Wget v1.21.4 (D:/Base/apps/Wget) 🪟

* Scoop：windows包管理器 v0.3.1 (D:/Base/apps/scoop) 🪟

### 2. 常用软件：

**系统增强:**

* 7zip：一款拥有极高压缩比的开源压缩软件 🪟
* utools：多功能文件搜索启动器 🪟
  + 搜素快捷键：双击Ctrl启动

* Windows Terminal：（已替换默认cmd）

* VMware：VMware Tools 虚拟机客户机操作系统性能并改善虚拟机管理的实用工具

* Oh-My-Posh：全平台终端提示符个性化工具 🪟

* Clink：Windows Cmd.exe Bash样式命令行编辑工具 (D:/Base/apps/Clink) 🪟

* Doskey (D:/Program Files/Tools/Scripts/alias\_key.bat) 💾
  + alias\_key.bat 文件定义了所有宏
  + 已设置注册表，开机自动设置命令alias

**系统优化:**

* AAct：Windows激活工具 v4.2.8 Portable
* Dism++：Windows 系统管理优化工具 🪟
* WiseCare365：系统优化工具绿色修改版 v6.5.1\_Pro（果核剥壳）
* Tools：自定义小工具
  + 右键管理：一键设置WIN10/WIN11右键模式 💾
  + Autologin：Windows自动登录注册表 💾
  + ClearHistory.ps1: 一清除PowerShell历史记录 💾
  + Scripts：cmd 和 powershell 别名脚本 💾

**文本编辑:**

* SublimeText：高效文本编辑器-汉化特别版 v4.4150 （果核剥壳）

**服务连接:**

* mRemoteNG: 标签式、多协议的远程连接管理器 🪟
* WinSCP: 支持SSH的SCP文件传输软件🪟
* MobaXterm: 工作在Windows桌面环境的多合一远程管理工具，包括几乎所有常用的远程网络工具（SSH、X11、RDP、VNC等）和Unix命令（bash、ls、cat，sed、grep、awk、rsync等 🪟
* Telnet: 实用的远程连接命令，采用的是TCP/IP协议 🪟
* OpenSSH: 包含一系列组件和工具，提供安全且简单的远程系统管理方法【启动命令：ssh】 🪟
* Redis-cli: Redis命令行界面，允许向Redis发送命令、并直接从终端读取服务器发送的回复的简单的程序 【客户端：redis-cli】【服务端：redis-server】🪟
* DBeaver: 一个通用的数据库管理工具和SQL 客户端，几乎支持所有主流的数据库 🪟
* HeidiSQL: 免费开源的轻量级数据库客户端软件，拥有图形化界面支持访问MySQL、MariaDB 和SQL Server 🪟
* OpenVPN: 一款基于SSL的开源VPN软件 🪟
* WindTerm：专业的跨平台SSH/Sftp/Shell/Telnet/Serial终端 🪟

**浏览器及插件：**

* Chrome：已设置为默认浏览器 v116.0.5845.180 **主要集成插件:**
  + Bishop Vulnerability Scanner:Search websites for git repos, exposed config files, and more as you browse.
  + Country Flags & IP Whois：显示网站服务器位置的国旗、Whois 和地理信息
  + FOFA Pro View: FOFA Pro view
  + Funnel Search：Advance search operators for google search
  + Hack-Tools: The all in one Red team extension for web pentester
  + HackBar: A browser extension for Penetration Testing
  + IP, DNS & Security Tools: Quick access to IP, DNS & Network Tools.
  + Proxy SwitchyOmega:轻松快捷地管理和切换多个代理设置。
  + Shodan: The Shodan plugin tells you where the website is hosted (country, city), who owns the IP and what other services/ ports are open.
  + Vulners Web Scanner：Tiny vulnerability scanner based on vulners.com vulnerability database.
  + Wappalyzer: 网页技术分析工具
  + WhatRuns: 网页技术分析工具
  + ZoomEye Tools: ZoomEye Tools provides a variety of functions to assist the use of Zoomeye
  + Octotree: 增强 GitHub 代码审查和探索的浏览器扩展
  + PostWoman：Http接口调试插件

* Firefox：v117.0 便携版​ **主要集成插件:**
  + Country Flags & IP Whois：显示网站服务器位置的国旗、Whois 和地理信息
  + FOFA Pro View: FOFA Pro view
  + Hack-Tools:The all in one Red team extension for web pentester
  + HackBar：A HackBar for google chrome/firefox browser. Small tool for pentesting websercurity.
  + Octotree: 增强 GitHub 代码审查和探索的浏览器扩展
  + Proxy SwitchyOmega:轻松快捷地管理和切换多个代理设置。
  + Shodan: The Shodan plugin tells you where the website is hosted (country, city), who owns the IP and what other services/ ports are open.
  + Supercopy：超级复制
  + Vulners Web Scanner：Tiny vulnerab...