---
title: MAC ParallelsDesktop安装精简系统PE/ESD/ISO/WIM
url: https://www.uedbox.com/post/68600/
source: 体验盒子
date: 2022-10-29
fetch_date: 2025-10-03T21:13:59.302156
---

# MAC ParallelsDesktop安装精简系统PE/ESD/ISO/WIM

[![体验盒子](https://www.uedbox.com/wp-content/themes/UB2019/imgs/logo.png)](https://www.uedbox.com)

* [博文](https://www.uedbox.com/blog/ "博文")
* [设计开发](https://www.uedbox.com/design/ "设计开发")
* [网络安全](https://www.uedbox.com/web-security/ "网络安全")
* [观点](https://www.uedbox.com/entertainment/ "观点")
* [服务](https://www.uedbox.com/service/ "服务")
* [AI导航](https://www.uedbox.com/aihub/ "AI导航")
* 更多
  + [关于](https://www.uedbox.com/about/ "关于")
  + [分享](https://www.uedbox.com/share/ "分享")
  + [老电影](https://www.uedbox.com/movie/ "老电影")
  + [搜索语法/SHDB](https://www.uedbox.com/shdb/ "搜索语法/SHDB")
  + [Exploits](https://www.uedbox.com/exploits/ "Exploits")
  + [SecTools](https://www.uedbox.com/tools/ "SecTools")
  + [UserAgent解析](https://www.uedbox.com/useragentparser/ "UserAgent解析")
  + [地理坐标在线转换](https://www.uedbox.com/geocoordinate/ "地理坐标在线转换")

# MAC ParallelsDesktop安装精简系统PE/ESD/ISO/WIM

* 发表于 2022年10月28日
* [macOS](https://www.uedbox.com/entertainment/macos/) , [周边](https://www.uedbox.com/web-security/safety/)
* 更新于 2022年12月06日 14:28:06 下午

分享一个虚拟机安装精简版 Windows10 系统的方法，只占用 5G 存储空间大小的完整版 win10 系统哦，不要安装那些垃圾阉割过的win7或者xp系统了，win10 也可以占用这么小的空间哦~

用了 Mac 这么久，感觉开发确实用 Mac 更方便更友好一些，但是有时候就会用到 Windows 系统，比如需要用到 XShell 之类 win 上独有的软件。这时候在 Mac 上安一个 Windows 虚拟机就很有用处了。即使是 Windows 电脑，做一些敏感操作容易中毒时候（比如作死玩玩病毒之类的），也最好隔离系统在虚拟机里鼓捣。

在 Mac 上 Parallels Desktop 安装的虚拟机全屏后，和Mac系统无缝切换，就是舒服~

啥？你还问我有什么用？如果你买个 128 GB 存储的 Mac 就知道有没有用了。（我的 256 也不够用，因此鼓捣出这么个方法来）

Windows 系统很占空间，新安装的系统动辄占用 40G - 60G 存储空间，如果安装到虚拟机中，就显得不是那么划算了。（在虚拟机中安过原版镜像的同学，对于虚拟机占用空间的大小，肯定深有体会）

原版镜像的 ISO 文件一般都要 13G 以上，于是我在 远景论坛 找到一个大神精简过的 Win10 ESD 镜像，只精简了无用的一些服务，无捆绑，镜像包仅 1G 大小，安装后也仅占用 4G 空间，真香！

如果你不知道我叨叨的是什么，就不用继续往下看了，以下以 Parallels Desktop 虚拟机举例，其他虚拟机比如 Vmware Fusion 之类的请触类旁通。

目录表

Toggle

* [安装准备](#%E5%AE%89%E8%A3%85%E5%87%86%E5%A4%87)
* [安装引导镜像](#%E5%AE%89%E8%A3%85%E5%BC%95%E5%AF%BC%E9%95%9C%E5%83%8F)
* [安装 win10](#%E5%AE%89%E8%A3%85_win10)
* [收尾工作](#%E6%94%B6%E5%B0%BE%E5%B7%A5%E4%BD%9C)
  + [选择安装 Parallels Tools](#%E9%80%89%E6%8B%A9%E5%AE%89%E8%A3%85_Parallels_Tools)
* [亮点](#%E4%BA%AE%E7%82%B9)

## 安装准备

几乎所有的虚拟机软件安装时，只支持 ISO 文件，但是一般封装的系统都是 ESD WIM 之类的镜像格式，So，需要转换成 ISO 格式。

我这里给出转换好的大神精简的镜像 ISO 文件，用了一年多了，很稳定，和原版镜像没有任何差别，占用空间相对原版镜像少的不是一点半点。若想要自己封装 ISO，见文末参考链接。

[**Win10精简版 ISO 镜像以及引导镜像下载**](https://pan.baidu.com/s/12mMWCCqRuREJC-2RM4gZ8g) 提取码: **vcmq**

网盘内有两个 ISO 文件，**WePE\_64\_V2.0.iso** 为引导镜像，**win10.iso** 为系统镜像。

下载文件到本地。

## 安装引导镜像

新建虚拟机，选择 **WePE\_64\_V2.0.iso** 这个引导镜像，可能会有如下之类的提示，无视跳过即可

![MAC ParallelsDesktop安装精简系统PE/ESD/ISO/WIM](https://www.uedbox.com/wp-content/uploads/2022/10/1.png)

选择系统类型为 win10，这里随便选一个就行

![MAC ParallelsDesktop安装精简系统PE/ESD/ISO/WIM](https://www.uedbox.com/wp-content/uploads/2022/10/2.png)

选择保存位置以及设置虚拟机名称

关闭设定，继续安装虚拟机，直到开机进入 PE 引导系统

## 安装 win10

1. 配置虚拟机连接的镜像为 **win10.iso**

![MAC ParallelsDesktop安装精简系统PE/ESD/ISO/WIM](https://www.uedbox.com/wp-content/uploads/2022/10/3.png)

打开引导系统内左下角的分区工具 DiskGenius，右键硬盘选择建立新分区（这里的大小是不准确的，不用理会），确定之后，选择保存更改，然后格式化选是（放心不会影响你的宿主机环境）

![MAC ParallelsDesktop安装精简系统PE/ESD/ISO/WIM](https://www.uedbox.com/wp-content/uploads/2022/10/4.png)

操作完如图所示（我的是 256G，这里也显示的是 256GB）

![MAC ParallelsDesktop安装精简系统PE/ESD/ISO/WIM](https://www.uedbox.com/wp-content/uploads/2022/10/5.png)

打开 Windows 安装器，选择 win10 镜像（在DVD 驱动器内）

![MAC ParallelsDesktop安装精简系统PE/ESD/ISO/WIM](https://www.uedbox.com/wp-content/uploads/2022/10/6.png)

选择开始安装，然后点确定，等待安装，安装完需要手动在开始菜单中手动重启。

重启后，系统自动进行 win10系统 的加载，稍等一会儿即可

## 收尾工作

选择桌面上的系统激活工具，直接选择激活即可。

这时候全屏虚拟机，会发现分辨率不是最佳的，因为你需要安装一下虚拟机工具，退出全屏

![MAC ParallelsDesktop安装精简系统PE/ESD/ISO/WIM](https://www.uedbox.com/wp-content/uploads/2022/10/8.png)

### 选择安装 Parallels Tools

进入我的电脑，DVD驱动器，运行 Autorun 文件进行安装，安装完选择重启系统

![MAC ParallelsDesktop安装精简系统PE/ESD/ISO/WIM](https://www.uedbox.com/wp-content/uploads/2022/10/9.png)

重启后，选择最大化（而不是融合模式）

![MAC ParallelsDesktop安装精简系统PE/ESD/ISO/WIM](https://www.uedbox.com/wp-content/uploads/2022/10/10.png)

稍等一会，虚拟机会自动调整分辨率到自适应。系统也会成功激活，桌面激活软件会自动消失。

完成！

## 亮点

看一下虚拟机占用吧嘿嘿~

![MAC ParallelsDesktop安装精简系统PE/ESD/ISO/WIM](https://www.uedbox.com/wp-content/uploads/2022/10/11.png)

ref

<https://nullpointer.pw/parallelsdesktop%E5%AE%89%E8%A3%85%E7%B2%BE%E7%AE%80%E7%89%88%E7%B3%BB%E7%BB%9F>

点赞(10)

打赏

分享

标签：[ISO](https://www.uedbox.com/post/tag/iso/) , [Mac](https://www.uedbox.com/post/tag/mac/) , [Parallels](https://www.uedbox.com/post/tag/parallels/) , [PE](https://www.uedbox.com/post/tag/pe/) , [VIM](https://www.uedbox.com/post/tag/vim/) , [虚拟机](https://www.uedbox.com/post/tag/%E8%99%9A%E6%8B%9F%E6%9C%BA/)  原文连接：**[MAC ParallelsDesktop安装精简系统PE/ESD/ISO/WIM](https://www.uedbox.com/post/68600/)**  所有媒体，可在保留署名、
`原文连接`
的情况下转载，若非则不得使用我方内容。

[Xcode垃圾清理、Xcode瘦身精简](https://www.uedbox.com/post/68596/ "Xcode垃圾清理、Xcode瘦身精简") [解决“Windows 安装程序无法配置为在此计算机的硬件上运行”](https://www.uedbox.com/post/68614/ "解决“Windows 安装程序无法配置为在此计算机的硬件上运行”")

* [相关推荐](#pills-xg)
* [最新文章](#pills-last)
* [30天最热](#pills-30)
* [历史最热](#pills-all)

[![2010 年 10 月全球浏览器市场份额统计](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

2010 年 10 月全球浏览器市场份额统计](https://www.uedbox.com/post/2272/ "2010 年 10 月全球浏览器市场份额统计")

[![更新Xcode提示空间不足“Not enough free space”解决](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

更新Xcode提示空间不足“Not enough free space”解决](https://www.uedbox.com/post/66475/ "更新Xcode提示空间不足“Not enough free space”解决")

[![Charles破解与使用](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

Charles破解与使用](https://www.uedbox.com/post/7579/ "Charles破解与使用")

[![好用的Mac清理卸载软件推荐](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

好用的Mac清理卸载软件推荐](https://www.uedbox.com/post/119673/ "好用的Mac清理卸载软件推荐")

[![macOS Mojave屏幕快照，最优的MAC截图工具带录屏](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

macOS Mojave屏幕快照，最优的MAC截图工具带录屏](https://www.uedbox.com/post/58750/ "macOS Mojave屏幕快照，最优的MAC截图工具带录屏")

[![Adobe Mac版本安装失败提示您必须升级错误代码：195解决方法](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

Adobe Mac版本安装失败提示您必须升级错误代码：195解决方法](https://www.uedbox.com/post/66940/ "Adobe Mac版本安装失败提示您必须升级错误代码：195解决方法")

[![CheatSheet，macOS显示当前程序所有快捷键](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

CheatSheet，macOS显示当前程序所有快捷键](https://www.uedbox.com/post/7898/ "CheatSheet，macOS显示当前程序所有快捷键")

[![只有29M的VMware Workstation V7.1.3 汉化绿色破解版](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

只有29M的VMware Workstation V7.1.3 汉化绿色破解版](https://www.uedbox.com/post/3523/ "只有29M的VMware Workstation V7.1.3 汉化绿色破解版")

[![Nginx 利用 fail2ban 自动封禁乱扫的 IP](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

Nginx 利用 fail2ban 自动封禁乱扫的 IP](https://www.uedbox.com/post/119731/ "Nginx 利用 fail2ban 自动封禁乱扫的 IP")

[![最新 绕过Cloudflare最佳实践](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

最新 绕过Cloudflare最佳实践](https://www.uedbox.com/post/119716/ "最新 绕过Cloudflare最佳实践")

[![NinjiaTag，兼容Apple Find My网络的开源防丢神器](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

NinjiaTag，兼容Apple Find My网络的开源防丢神器](https://www.uedbox.com/post/119688/ "NinjiaTag，兼容Apple Find My网络的开源防丢神器")

[![好用的Mac清理卸载软件推荐](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

好用的Mac清理卸载软件推荐](https://www.uedbox.com/post/119673/ "好用的Mac清理卸载软件推荐")

[![AutoGen Studio 容器化部署与维护指南](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

AutoGen Studio 容器化部署与维护指南](https://www.uedbox.com/post/119359/ "AutoGen Studio 容器化部署与维护指南")

[![肌理解剖师：中年人的小确幸](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

肌理解剖师：中年人的小确幸](https://www.uedbox.com/post/119356/ "肌理解剖师：中年人的小确幸")

[![🔥 最新免费域名资源大全 | 永久免费域名获取](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

🔥 最新免费域名资源大全 | 永久免费域名获取](https://www.uedbox.com/post/119352/ "🔥 最新免费域名资源大全 | 永久免费域名获取")

[![Cursor agent ask manual区别](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

Cursor agent ask manual区别](https://www.uedbox.com/post/119346/ "Cursor ...