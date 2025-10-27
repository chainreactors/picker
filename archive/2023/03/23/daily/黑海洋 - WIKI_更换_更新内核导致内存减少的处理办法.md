---
title: 更换/更新内核导致内存减少的处理办法
url: https://blog.upx8.com/3328
source: 黑海洋 - WIKI
date: 2023-03-23
fetch_date: 2025-10-04T10:22:52.372816
---

# 更换/更新内核导致内存减少的处理办法

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 更换/更新内核导致内存减少的处理办法

发布时间:
2023-03-22

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
11827

很多时候，我们DD完Linux后，都会更新或是更换BBR内核来达到网络加速的效果。但是在更换完内核后会经常会出现可用内存减少的情况，一般表现为两种：

• 可用内存数值比实际应有内存数值小得多；
• 已使用内存数值过大。

对于内存大的也就无所谓了，但是对于本身内存就很小的小鸡而言，无疑是一种“灾难”。遇到这种情况该怎么处理呢？下面直接上教程：

1、编辑grub启动文件，位置在 /etc/default/grub。找到“GRUB\_CMDLINE\_LINUX”项，在后面加上参数“iommu=off”

```
GRUB_CMDLINE_LINUX="iommu=off"
```

2、重新生成grub文件

```
sudo update-grub
```

3、此时你就会发现你的内存数值恢复正常了。如果没有恢复的话，执行重启命令即可

```
reboot
```

4、检查是否生效，如果没有任何反馈输出，即代表已经成功。否则检查前面额步骤

```
dmesg | grep SWIOTLB
```

**原理：**iommu用于支持硬件直通，会启用SWIOTLB，直接让你很大一部分内存被吃掉，对于内存不大的小鸡来说这部分内存的占用完全是一种浪费。

[取消回复](https://blog.upx8.com/3328#respond-post-3328)

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