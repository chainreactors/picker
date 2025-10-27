---
title: 甲骨文(ARM/x86均可) oracle cloud使用netboot任意重装系统
url: https://blog.upx8.com/3197
source: 黑海洋 - WIKI
date: 2023-01-22
fetch_date: 2025-10-04T04:33:37.193137
---

# 甲骨文(ARM/x86均可) oracle cloud使用netboot任意重装系统

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 甲骨文(ARM/x86均可) oracle cloud使用netboot任意重装系统

发布时间:
2023-01-21

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
31407

甲骨文 ARM 热门地区现在是很难开出来了,一旦把自己好不容易抢到的机玩坏了,想再开一个是相当的难,这里就带来 netboot 重装系统的教程,教程使用 x86 小鸡进行演示,PS:我开不出 ARM:(

## 一.创建控制台连接

注意:创建 vps 时候记得开默认的系统,oracle linux,其他系统的 bios 和它不一定相同(试过 ubuntu 是不一样的,其他没尝试过)

这里我选择用本地的 wsl 生成了 ssh key 命令如下

`ssh-keygen -t rsa`

`cat .ssh/id_rsa.pub`

即可获得你的 ssh 公钥

[![](https://note.lazzman.com:18084/media/202203/2022-03-16_1639560.10563553444351015.png)](https://note.lazzman.com:18084/media/202203/2022-03-16_1639560.10563553444351015.png)

然后去创建控制台连接粘贴密钥

[![](https://note.lazzman.com:18084/media/202203/2022-03-16_1639560.17571451817673833.png)](https://note.lazzman.com:18084/media/202203/2022-03-16_1639560.17571451817673833.png)

创建完成后,复制 linux 的串口连接命令

[![](https://note.lazzman.com:18084/media/202203/2022-03-16_1639560.45843786892759675.png)](https://note.lazzman.com:18084/media/202203/2022-03-16_1639560.45843786892759675.png)

再将命令复制到刚才的 linux 系统里就可以连接了,连接时候会有警告,输入 yes 即可

## 二.下载 netboot.efi

这是重装系统前的最后一步,去 netboot.xyz 下载 EFI 引导文件

x86\_64:[https://boot.netboot.xyz/ipxe/netboot.xyz.efi](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuem1jenguY29tL2dvL2FIUjBjSE02THk5aWIyOTBMbTVsZEdKdmIzUXVlSGw2TDJsd2VHVXZibVYwWW05dmRDNTRlWG91WldacA)

arm64:[https://boot.netboot.xyz/ipxe/netboot.xyz-arm64.efi](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuem1jenguY29tL2dvL2FIUjBjSE02THk5aWIyOTBMbTVsZEdKdmIzUXVlSGw2TDJsd2VHVXZibVYwWW05dmRDNTRlWG90WVhKdE5qUXVaV1pw)

将 efi 文件 wget 到 vps 的/boot/efi/EFI 文件夹下即可

## 三.开始重装

连接上串口连接后,去网站控制台重启 vps,然后回到连接中,狂按 ESC,即可进入 bios

这里选择第三项 Boot Maintenance Manager 按回车进入

[![](https://note.lazzman.com:18084/media/202203/2022-03-16_1639560.3765375552223269.png)](https://note.lazzman.com:18084/media/202203/2022-03-16_1639560.3765375552223269.png)

选择 Boot From File

[![](https://note.lazzman.com:18084/media/202203/2022-03-16_1639560.8323116620969606.png)](https://note.lazzman.com:18084/media/202203/2022-03-16_1639560.8323116620969606.png)

然后再按一次回车进入默认的硬盘,选择 EFI 文件夹下的 netboot.efi 进入 netboot

[![](https://note.lazzman.com:18084/media/202203/2022-03-16_1639560.08197678019857824.png)](https://note.lazzman.com:18084/media/202203/2022-03-16_1639560.08197678019857824.png)

[![](https://note.lazzman.com:18084/media/202203/2022-03-16_1639560.595764785597723.png)](https://www.zmczx.com/usr/uploads/2021/09/1784959824.png)

这是启动 netboot 后的界面,选择 Linux Network Installs 开始安装

[![](https://note.lazzman.com:18084/media/202203/2022-03-16_1639560.24710170006036902.png)](https://note.lazzman.com:18084/media/202203/2022-03-16_1639560.24710170006036902.png)

可以看到能安装的系统相当多,我这里选择安装 debian11

[![](https://note.lazzman.com:18084/media/202203/2022-03-16_1639560.9570991403413591.png)](https://note.lazzman.com:18084/media/202203/2022-03-16_1639560.9570991403413591.png)

安装时候记得选择 Text Based Install

后面的安装过程大家应该都会,就不多做介绍了,不懂的可以在网上搜索 xxx 系统安装教程,这里安装过程全部一致,只是没有图形化安装过程了。

[取消回复](https://blog.upx8.com/3197#respond-post-3197)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2024 黑海洋. All rights reserved.
[看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号") [Sitemap](sitemap.xml?type=index "Sitemap")