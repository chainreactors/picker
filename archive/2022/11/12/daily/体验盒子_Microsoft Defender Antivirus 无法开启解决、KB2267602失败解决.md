---
title: Microsoft Defender Antivirus 无法开启解决、KB2267602失败解决
url: https://www.uedbox.com/post/68619/
source: 体验盒子
date: 2022-11-12
fetch_date: 2025-10-03T22:32:23.239970
---

# Microsoft Defender Antivirus 无法开启解决、KB2267602失败解决

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

# Microsoft Defender Antivirus 无法开启解决、KB2267602失败解决

* 发表于 2022年11月11日
* [windows](https://www.uedbox.com/entertainment/windows/) , [周边](https://www.uedbox.com/web-security/safety/)

问题描述：

目录表

Toggle

* [Defender无法开启、KB2267602更新失败](#Defender%E6%97%A0%E6%B3%95%E5%BC%80%E5%90%AF%E3%80%81KB2267602%E6%9B%B4%E6%96%B0%E5%A4%B1%E8%B4%A5)
* [最终的解决方案](#%E6%9C%80%E7%BB%88%E7%9A%84%E8%A7%A3%E5%86%B3%E6%96%B9%E6%A1%88)
  + [意外的解决了](#%E6%84%8F%E5%A4%96%E7%9A%84%E8%A7%A3%E5%86%B3%E4%BA%86)

## Defender无法开启、KB2267602更新失败

突然间**Microsoft Defender Antivirus自动关闭了，开关全灰无法手动开启**。

检查发现有Windows更新未完成，发现有个更新一直卡着无法更新完成：

**Microsoft Defender Antivirus 的安全智能更新 - KB2267602 （版本 1.379.86.0）
状态：正在安装 - 66%**

![Microsoft Defender Antivirus 无法开启解决、KB2267602失败解决](https://www.uedbox.com/wp-content/uploads/2022/11/20221109105043.png)

![Microsoft Defender Antivirus 无法开启解决、KB2267602失败解决](https://www.uedbox.com/wp-content/uploads/2022/11/20221109230314.png)

Windows 无法更新

直觉可能跟这个有关，于是网上找了几小时未能解决，最终调整思路，在翻设置时无意间发现：
`Windows安全中心->应用和浏览器控制->隔离浏览下`
，竟然有个，安装Microsoft Defender应用程序防护？？？，难道Defender突然间被卸载了？？？于是点进去看，点击后打开了“Windows功能”菜单，里边显示
`Microsoft Defender 应用程序防护竟然是灰色的，也没勾，说明确实不在了`
。

把鼠标放在菜单灰色处，它会提示“
`该固件中的虚拟化支持被禁用`
”无法安装？唉，难道是主板不支持？于是马上进BIOS查看，发现主板确实关闭了虚拟化支持，华硕主板BIOS开户虚拟化设置参照：<https://www.asus.com.cn/support/FAQ/1038245>

然后再进系统，按照网络的路径去安装“Microsoft Defender应用程序防护”，这回不是灰色了，勾选上它，点确实，它会进行安装，安装完成后会要求重启，重启后Defender应用就可正常开启了。

![此图片的alt属性为空；文件名为20221109235959.png](https://www.uedbox.com/wp-content/uploads/2022/11/20221109235959.png)

Microsoft Defender 应用程序防护灰色修复，上图为已经修复后的，没修复前的忘记截图了

然而，问题并没解决，虽然Windows功能那显示已经安装，但其实**Microsoft Defender Antivirus**还是被关闭无法开户使用的，而且**KB2267602**也依然无法更新，一直卡在66%。

## 最终的解决方案

网络中所有能搜到的方案都无法解决我遇到的问题，在尝试所有方法无果后，准备使用系统的重置功能。

但在重置操作中又再次失败，说发生错误中止，什么错误没说，这……。于是直接关机准备改天重装系统。在准备躺平的闲间思考，既然所有找到的方法（含Microsoft官方给出的）都无法解决，那是否可以曲线方案？找个微软自家的管理工具来试下？抱着经验和直觉的思想就去搜关键词“电脑管家”，因为官方出的一般会以这种命名，不负所望，微软真的出了个“微软电脑管家”，但是还处于测试开发阶段，于是安装。

![Microsoft Defender Antivirus 无法开启解决、KB2267602失败解决](https://www.uedbox.com/wp-content/uploads/2022/11/20221111102448.png)

微软电脑管家界面

### 意外的解决了

在安装完微软电脑管家，并进行了优化体验优化后，奇迹出现，**`Microsoft Defender Antivirus`**竟然正常了！！！并且
`Microsoft Defender Antivirus 的安全智能更新 - KB2267602 （版本 1.379.86.0）也更新成功了`
，吐血！！！

![Microsoft Defender Antivirus 无法开启解决、KB2267602失败解决](https://www.uedbox.com/wp-content/uploads/2022/11/20221111100634.png)

`Defender`
`KB2267602`
更新成功

这操作属实SAO，微软社区工作人员给了一众方案都无法解决，最后装个他们的软件解决了！

点赞(4)

打赏

分享

标签：[Defender](https://www.uedbox.com/post/tag/defender/) , [KB2267602](https://www.uedbox.com/post/tag/kb2267602/) , [Windows 10](https://www.uedbox.com/post/tag/windows-10/)  原文连接：**[Microsoft Defender Antivirus 无法开启解决、KB2267602失败解决](https://www.uedbox.com/post/68619/)**  所有媒体，可在保留署名、
`原文连接`
的情况下转载，若非则不得使用我方内容。

[Windows原版系统下载地址](https://www.uedbox.com/post/68616/ "Windows原版系统下载地址") [AdSense收款招商银行电汇教程](https://www.uedbox.com/post/68634/ "AdSense收款招商银行电汇教程")

* [相关推荐](#pills-xg)
* [最新文章](#pills-last)
* [30天最热](#pills-30)
* [历史最热](#pills-all)

[![Windows原版系统下载地址](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

Windows原版系统下载地址](https://www.uedbox.com/post/68616/ "Windows原版系统下载地址")

[![Hwidgen 62.01原版 – Windows 10数字许可证永久激活工具](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

Hwidgen 62.01原版 – Windows 10数字许可证永久激活工具](https://www.uedbox.com/post/56997/ "Hwidgen 62.01原版 – Windows 10数字许可证永久激活工具")

[![解决“Windows 安装程序无法配置为在此计算机的硬件上运行”](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

解决“Windows 安装程序无法配置为在此计算机的硬件上运行”](https://www.uedbox.com/post/68614/ "解决“Windows 安装程序无法配置为在此计算机的硬件上运行”")

[![家庭摄像头会遭遇攻击吗?](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

家庭摄像头会遭遇攻击吗?](https://www.uedbox.com/post/6440/ "家庭摄像头会遭遇攻击吗?")

[![Mysql综合利用工具](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

Mysql综合利用工具](https://www.uedbox.com/post/5823/ "Mysql综合利用工具")

[![那些强悍的PHP一句话后门](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

那些强悍的PHP一句话后门](https://www.uedbox.com/post/6051/ "那些强悍的PHP一句话后门")

[![用JS给XP的右键加上“打开文件位置”](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

用JS给XP的右键加上“打开文件位置”](https://www.uedbox.com/post/6125/ "用JS给XP的右键加上“打开文件位置”")

[![burpsuite pro v1.4.07破解版](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

burpsuite pro v1.4.07破解版](https://www.uedbox.com/post/4650/ "burpsuite pro v1.4.07破解版")

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

Cursor agent ask manual区别](https://www.uedbox.com/post/119346/ "Cursor agent ask manual区别")

* [最新 绕过Cloudflare最佳实践](https://www.uedbox.com/post/119716/ "最新 绕过Cloudflare最佳实践")
* [NinjiaTag，兼容Apple Find My网络的开源防丢神器](https://www.uedbox.com/post/119688/ "NinjiaTag，兼容Apple Find My网络的开源防丢神器")
* [Nginx 利用 fail2ban 自动封禁乱扫的 IP](https://www.uedbox.com/post/119731/ "Nginx 利用 fail2ban 自动封禁乱扫的 IP")

* [2025 BT磁力搜索引擎大全【最新优质】](https://www.uedbox.com/post/54994/ "2025 BT磁力搜索引擎大全【最新优质】")
* [怎么用图片搜索番号？以图搜图AI搜图](https://www.uedbox.com/post/55287/ "怎么用图片搜索番号？以图搜图AI搜图")
* [this channel is blocked because it was used：Telegram群组/频道屏蔽解决方法](https://www.uedbox.com/post/56387/ "this channel is blocked because it was used：Telegram群组/频道屏蔽解决方法")
* [2025免费在线影视/动漫番剧优质网站，合集汇总更新](https://www.uedbox.com/post/69704/ "2025免费在线影视/动漫番剧优质网站，合集汇总更新")
* [最新ESET NOD32 License Key/激活码/许可证密钥/用户名密码](https://www.uedbox.com/post/58618/ "最新ESET NOD32 License Key/激活码/许可证密钥/用户名密码")
* [谷歌识图，以图搜图](https://www.uedbox.com/post/3902/ "谷歌识图，以图搜图")
* [No Access-Control-Allow-Origin 跨域错误解决](https://www.uedbox.com/post/50992/ "No Access-Control-Allow-Origin 跨域错误解决")
* [7款常用《网络抓包工具》更新](https://www.uedbox.com/post/59475/ "7款常用《网络抓包工具》更新")
* [手机BT/种子下载，手机磁力链下载软件整理](https://www.uedbox.com/post/56509/ "手机BT/种子下载，手机磁力链下载软件整理")
* [404.php webs...