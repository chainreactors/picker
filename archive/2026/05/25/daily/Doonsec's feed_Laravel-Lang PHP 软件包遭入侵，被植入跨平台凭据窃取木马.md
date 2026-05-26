---
title: Laravel-Lang PHP 软件包遭入侵，被植入跨平台凭据窃取木马
url: https://mp.weixin.qq.com/s/aQIz8GU09riTvUbcVMDISg
source: Doonsec's feed
date: 2026-05-25
fetch_date: 2026-05-26T06:07:42.170692
---

# Laravel-Lang PHP 软件包遭入侵，被植入跨平台凭据窃取木马

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/DYqn7TU9icq0K3414pqSCibAP8cjic8C07iaEE3Yp8FbRS3plM6dqBHJWPL7iciaBSdRV1Lruu8YXdIXw2APWfGT0iciaKCdCAuCvoYtfQCc4XeAw4I/0?wx_fmt=jpeg)

# Laravel-Lang PHP 软件包遭入侵，被植入跨平台凭据窃取木马

鹏鹏同学
鹏鹏同学

黑猫安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

网络安全研究人员发现新一轮软件供应链攻击，黑客入侵多个 Laravel-Lang 旗下 PHP 程序包，植入功能完备的凭据窃取框架。

受影响程序包如下：

* laravel-lang/lang
* laravel-lang/http-statuses
* laravel-lang/attributes
* laravel-lang/actions

安全平台 Socket 表示：新版标签的发布时间与规律表明，此次并非单一恶意版本投毒，而是 Laravel-Lang 组织发布流程整体遭攻陷。恶意版本集中在 2026 年 5 月 22 日至 23 日批量上线，多个版本发布间隔仅数秒。目前已查出七百余个异常版本，疑似攻击者借助程序批量打标签、重发包。推测黑客盗取了组织级账号凭证、仓库自动化权限或发布服务器权限。

本次攻击手法特殊，项目原始源代码并未植入恶意代码，攻击者篡改各仓库所有 Git 标签，将其指向恶意提交节点。

恶意核心代码存放于`src/helpers.php`文件，主要用于采集设备指纹，并外联`flipboxstudio.info`服务器，下载可在 Windows、Linux、macOS 跨平台运行的 PHP 恶意载荷。

安全机构 StepSecurity 说明：攻击者将该恶意文件写入受损包的自动加载配置。Laravel、Symfony、PHPUnit 等主流 PHP 框架启动时均会加载自动加载文件，只要引入该程序包，恶意代码便会自动执行，无需额外调用类或方法触发。

据 Aikido 安全团队监测，恶意程序在 Windows 系统调用 VB 脚本启动程序；在 Linux 与 macOS 系统则通过系统命令运行窃取程序。

Socket 解释，由于该文件被注册至依赖配置的自动加载项，服务器每处理一次 PHP 请求，后门都会自动运行。脚本会依据目录路径、系统架构、索引节点生成唯一设备 MD5 标识，确保单台设备仅触发一次窃取行为，减少暴露概率。

窃取程序可批量窃取系统各类敏感数据，并回传至同一恶意服务器，窃取范围包含：查询云元数据接口获取身份权限与实例凭证、谷歌云默认应用凭据、微软 Azure 访问令牌与服务主体配置、容器集群服务账号令牌及仓库配置；各类云平台、托管平台、容器平台访问密钥；密码管理工具、自动化运维平台、CI/CD 流水线令牌与配置；多类加密钱包、浏览器插件助记词与密钥；绕过浏览器加密防护，窃取主流浏览器浏览记录、Cookie 及登录信息；多款密码管理器本地保险箱数据；远程连接会话、远程桌面配置、系统凭据管理器数据；社交软件会话令牌、邮件客户端、FTP 客户端账号信息；容器授权密钥、SSH 私钥、代码仓库凭证、环境变量、网站配置、集群配置、系统操作日志；各类虚拟专用网络配置与留存账号信息。

安全研究员表示，下载的窃取程序代码约 5900 行，划分十五类专项采集模块。数据采集完毕后，采用 AES-256 算法加密并上传至恶意地址，随后自动删除自身文件，销毁入侵痕迹。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/DYqn7TU9icq0Cqr2KYoUfur4KLeiclhRqlnu9g0qWMQJVEPqRicnicZzBdbaER3Jd1tI4NootkSwZiaruC4ATIbibbuM0riaianEiaRt0dVicRsfUhmI8/0?wx_fmt=png)

黑猫安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/DYqn7TU9icq0Cqr2KYoUfur4KLeiclhRqlnu9g0qWMQJVEPqRicnicZzBdbaER3Jd1tI4NootkSwZiaruC4ATIbibbuM0riaianEiaRt0dVicRsfUhmI8/0?wx_fmt=png)

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