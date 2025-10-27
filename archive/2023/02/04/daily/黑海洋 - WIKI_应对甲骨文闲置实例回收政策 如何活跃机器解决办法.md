---
title: 应对甲骨文闲置实例回收政策 如何活跃机器解决办法
url: https://blog.upx8.com/3207
source: 黑海洋 - WIKI
date: 2023-02-04
fetch_date: 2025-10-04T05:41:07.617850
---

# 应对甲骨文闲置实例回收政策 如何活跃机器解决办法

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 应对甲骨文闲置实例回收政策 如何活跃机器解决办法

发布时间:
2023-02-03

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
11810

最近的消息甲骨文对用户闲置机器开始要求活跃了，不活跃就要停机。给更有需要的人用了。也试图缓解资源紧缺的情况。

**回收条件**以七天为单位

1.在七天里的95%的时间里。CPU都低于10%

2.内存低于10%

3.网络占用量10%

这三个条件满足任意一个还是全部满足停机。官方没说清楚。

原文地址:[https://docs.oracle.com/en-us/iaas/Content/FreeTier/freetier\_topic-Always\_Free\_Resources.htm](https://blog.upx8.com/go/aHR0cHM6Ly9kb2NzLm9yYWNsZS5jb20vZW4tdXMvaWFhcy9Db250ZW50L0ZyZWVUaWVyL2ZyZWV0aWVyX3RvcGljLUFsd2F5c19GcmVlX1Jlc291cmNlcy5odG0)

**为了应对甲骨文最新回收机制而作的垃圾脚本**

说在前面： 由于甲骨文目前对不活跃机器实行回收，本脚本的作用就是 通过下载文件，上传，cpu跑分让甲骨文以为你是"活跃用户" 脚本仅做辅助，无法保证不被删机

**1.cpu占用脚本**，自定义占用率。

cd /root && wget -qO OneKeyFuck\_OCPU.sh https://raw.githubusercontent.com/Mrmineduce21/Oracle\_OneKey\_Active/main/OneKeyFuck\_OCPU.sh && chmod +x OneKeyFuck\_OCPU.sh && bash OneKeyFuck\_OCPU.sh

**2.内存占用脚本**。固定吃2G内存，可叠加使用

cd /root && wget -qO memory\_usage.sh https://raw.githubusercontent.com/Mrmineduce21/Oracle\_OneKey\_Active/main/memory\_usage.sh && chmod +x memory\_usage.sh && bash memory\_usage.sh consume 2G

**3.网络占用脚本**。每半个小时下载一次资源，随后自动删除。全自动

cd /root && wget -qO FuckNetWork.sh https://raw.githubusercontent.com/Mrmineduce21/Oracle\_OneKey\_Active/main/FuckNetWork.sh && chmod +x FuckNetWork.sh && nohup ./FuckNetWork.sh &

不想占用资源了直接重启服务器即可：reboot

大神GitHub源地址，讲的更为详细。多多支持这样的大神

[https://github.com/Mrmineduce21/Oracle\_OneKey\_Active](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL01ybWluZWR1Y2UyMS9PcmFjbGVfT25lS2V5X0FjdGl2ZQ)

目前还未出现回收情况，会时刻关注此事进展。有新情况会更新补充！

推荐新脚本：[https://github.com/spiritLHLS/Oracle-server-keep-alive-script](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3NwaXJpdExITFMvT3JhY2xlLXNlcnZlci1rZWVwLWFsaXZlLXNjcmlwdA)

[取消回复](https://blog.upx8.com/3207#respond-post-3207)

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