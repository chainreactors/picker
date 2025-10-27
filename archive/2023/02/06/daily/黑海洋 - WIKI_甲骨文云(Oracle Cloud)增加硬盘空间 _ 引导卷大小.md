---
title: 甲骨文云(Oracle Cloud)增加硬盘空间 | 引导卷大小
url: https://blog.upx8.com/3209
source: 黑海洋 - WIKI
date: 2023-02-06
fetch_date: 2025-10-04T05:47:55.631812
---

# 甲骨文云(Oracle Cloud)增加硬盘空间 | 引导卷大小

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 甲骨文云(Oracle Cloud)增加硬盘空间 | 引导卷大小

发布时间:
2023-02-05

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
16542

教程：[https://www.youtube.com/watch?v=7FBYKdW5gos](https://blog.upx8.com/go/aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g_dj03RkJZS2RXNWdvcw)

这个视频将展示，如何在Oracle Cloud(甲骨文云）的免费实例VPS上增加驱动器空间。默认大小约为 50GB，您可以在首次设置实例时增加此大小。 您也可以稍后增加它，这有点复杂，但是通过以下操作可以实现。

命令：

sudo su -

在甲骨文云修改Boot Volume以后，得到类似于以下的命令行：
sudo dd iflag=direct if=/dev/oracleoci/oraclevda of=/dev/null count=1
echo "1" | sudo tee /sys/class/block/`readlink /dev/oracleoci/oraclevda | cut -d'/' -f 2`/device/rescan

growpart /dev/sda 1

resize2fs /dev/sda1

df -h

[取消回复](https://blog.upx8.com/3209#respond-post-3209)

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