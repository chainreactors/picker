---
title: 甲骨文arm重装 Debian 11脚本
url: https://blog.upx8.com/3096
source: 黑海洋 - WIKI
date: 2022-11-19
fetch_date: 2025-10-03T23:13:43.040403
---

# 甲骨文arm重装 Debian 11脚本

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 甲骨文arm重装 Debian 11脚本

发布时间:
2022-11-18

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
20524

甲骨文默认是key登陆，虽然安全，但还是麻烦，他最新的arm机器，其实也能刷系统的最新的Debian11，以下这个脚本也能刷其他的vps，更多操作，详见作者github
[https://github.com/bohanyang/debi](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2JvaGFueWFuZy9kZWJp)

以下以甲骨文arm服务器为例，简单说下如何DD甲骨文的arm

## 暂不支持 Oracle Linux 作为原系统。创建新机器时请选择 Ubuntu 20.04 或 18.04 系统模板（非mini版）。

## 1.下载脚本

```
curl -fLO https://raw.githubusercontent.com/bohanyang/debi/master/debi.sh && chmod a+rx debi.sh
```

## 2.运行脚本

```
sudo ./debi.sh --architecture arm64 --user root --password password
```

## 3.改密码

以上脚本执行后，默认root密码为password，为了安全，一定要改密码。改密码指令为passwd，然后盲输两次密码即可。

## 4.如果以上都没报错，重启

```
sudo shutdown -r now
```

## 5.过5分钟开机

理论上30秒就够了，但如果无法连接，多等一下吧！

[取消回复](https://blog.upx8.com/3096#respond-post-3096)

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