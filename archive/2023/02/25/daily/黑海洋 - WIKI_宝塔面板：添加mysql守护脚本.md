---
title: 宝塔面板：添加mysql守护脚本
url: https://blog.upx8.com/3241
source: 黑海洋 - WIKI
date: 2023-02-25
fetch_date: 2025-10-04T08:04:34.257247
---

# 宝塔面板：添加mysql守护脚本

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 宝塔面板：添加mysql守护脚本

发布时间:
2023-02-24

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
18146

云服务器安装的宝塔面板，因为内存经常不足导致宝塔面板mysql经常停止，需要检测mysql进程是否停止，就像php守护程序一样，检测到mysql 进程禁止后，检测到mysql停止会自动启动。

## Mysql进程守护脚本 shell脚本一：

```
pgrep -x mysqld &> /dev/null
if [ $? -ne 0 ];then
        bash /www/server/panel/script/rememory.sh
        /etc/init.d/mysqld start
fi
```

## Mysql进程守护脚本 shell脚本二：

```
#!/bin/bash
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
export PATH
pgrep -x mysqld &> /dev/null
if [ $? -ne 0 ]
then
echo "At time:$(date) :MySQL is stop .">> /var/log/mysql_messages
/etc/init.d/mysqld start
else
exit
fi
```

1、登录宝塔面板 >> 计划任务 >> 添加定时脚本

[![自动草稿](https://www.xpn.cc/wp-content/uploads/2022/11/52420a4b5a13ade.png "自动草稿")](https://www.xpn.cc/wp-content/uploads/2022/11/52420a4b5a13ade.png)

2、手动停止mysql后，执行守护脚本，确认可以正常启动mysql

[![自动草稿](https://www.xpn.cc/wp-content/uploads/2022/11/6e71e1d00a18e95.jpeg "自动草稿")](https://blog.upx8.com/go/aHR0cHM6Ly93d3cueHBuLmNjL3dwLWNvbnRlbnQvdXBsb2Fkcy8yMDIyLzExLzZlNzFlMWQwMGExOGU5NS5qcGVn)

[取消回复](https://blog.upx8.com/3241#respond-post-3241)

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