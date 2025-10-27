---
title: 获取windbgx离线安装包
url: https://blog.nsfocus.net/%e8%8e%b7%e5%8f%96windbgx%e7%a6%bb%e7%ba%bf%e5%ae%89%e8%a3%85%e5%8c%85/
source: 绿盟科技技术博客
date: 2025-08-12
fetch_date: 2025-10-07T00:48:25.061845
---

# 获取windbgx离线安装包

* [登录](http://blog.nsfocus.net/wp-login.php)
* [注册](http://blog.nsfocus.net/wp-login.php?action=register)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

# 获取windbgx离线安装包

### 获取windbgx离线安装包

[2025-08-11](https://blog.nsfocus.net/%E8%8E%B7%E5%8F%96windbgx%E7%A6%BB%E7%BA%BF%E5%AE%89%E8%A3%85%E5%8C%85/ "获取windbgx离线安装包")[NSFOCUS](https://blog.nsfocus.net/author/zhengfangying/ "View all posts by NSFOCUS")

阅读： 1,173

创建: 2020-11-16 16:30
更新: 2025-08-07 11:01

windbgx与windbg有差别，下面的内容适用于windbgx。先下载

https://windbg.download.prss.microsoft.com/dbazure/prod/1-0-0/windbg.appinstaller

windbg.appinstaller实际是个XML文件，形如

————————————————————————–
<?xml version=”1.0″ encoding=”utf-8″?>
<AppInstaller Uri=”https://windbg.download.prss.microsoft.com/dbazure/prod/1-0-0/windbg.appinstaller” Version=”1.2506.12002.0″ xmlns=”http://schemas.microsoft.com/appx/appinstaller/2018″>
<MainBundle Name=”Microsoft.WinDbg” Version=”1.2506.12002.0″ Publisher=”CN=Microsoft Corporation, O=Microsoft Corporation, L=Redmond, S=Washington, C=US” Uri=”https://windbg.download.prss.microsoft.com/dbazure/prod/1-2506-12002-0/windbg.msixbundle” />
<UpdateSettings>
<OnLaunch HoursBetweenUpdateChecks=”0″/>
<AutomaticBackgroundTask/>
<ForceUpdateFromAnyVersion>true</ForceUpdateFromAnyVersion>
</UpdateSettings>
</AppInstaller>
————————————————————————–

上例含有windbgx安装包下载链接

https://windbg.download.prss.microsoft.com/dbazure/prod/1-2506-12002-0/windbg.msixbundle

获取安装包后，可安装，可升级。

资源管理器中右键windbg.msixbundle，有个安装，点击安装即可。但这个操作实际
依赖”App Installer”，没有Microsoft Store的Windows此法不通。可用PowerShell
安装、卸载:

Add-AppxPackage -Path “<path>\windbg.msixbundle”
Remove-AppxPackage Microsoft.WinDbg\_1.2506.12002.0\_x64\_\_8wekyb3d8bbwe

更进一步，很多用windbgx的都有Portable的需求，安装后再复制太low了，事实上
7-Zip直接析取即可。windbg.msixbundle中有windbg\_win-x64.msix，7-Zip打开后
者，这是个压缩包，释放到任意位置，就是Portable windbgx，可用于无Store的
Windows。

windbgx若干历史版本

————————————————————————–
总入口
https://windbg.download.prss.microsoft.com/dbazure/prod/1-0-0/windbg.appinstaller

1.2306.12001.0
https://windbg.download.prss.microsoft.com/dbazure/prod/1-2306-12001-0/windbg.msixbundle

1.2402.24001.0
https://windbg.download.prss.microsoft.com/dbazure/prod/1-2402-24001-0/windbg.msixbundle

1.2506.12002.0
https://windbg.download.prss.microsoft.com/dbazure/prod/1-2506-12002-0/windbg.msixbundle
————————————————————————–

Spread the word. Share this post!

[Previous](https://blog.nsfocus.net/windows-5/)

[Next](https://blog.nsfocus.net/quic%E5%8D%8F%E8%AE%AE%E7%A7%91%E6%99%AE/)

### Meet The Author

NSFOCUS

咨询与合作：nsmagazine@nsfocus.com

* [绿盟科技官网](https://www.nsfocus.com.cn)
* [绿盟威胁情报中心（NTI）](https://nti.nsfocus.com)
* [绿盟云](https://cloud.nsfocus.com)