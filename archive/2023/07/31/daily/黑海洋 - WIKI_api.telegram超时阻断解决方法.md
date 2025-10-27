---
title: api.telegram超时阻断解决方法
url: https://blog.upx8.com/3727
source: 黑海洋 - WIKI
date: 2023-07-31
fetch_date: 2025-10-04T11:52:15.929668
---

# api.telegram超时阻断解决方法

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# api.telegram超时阻断解决方法

发布时间:
2023-07-30

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
17630

错误：HTTPSConnectionPool(host='api.telegram.org', port=443): Read timed out. (read timeout=25)

解决方法：

安装`sudo apt install tor`

```
sudo apt install privoxy torsocks

nano /etc/privoxy/config
```

`pip install pysocks`

`forward-socks5t / 127.0.0.1:9050 .`

```
sudo systemctl enable privoxy.service
sudo systemctl start privoxy.service
```

`/etc/tor/torsocks.conf`

```
TorAddress 127.0.0.1
TorPort 9050
```

```
from telebot import apihelper

apihelper.proxy = {'https': 'socks5h://127.0.0.1:9050',
#    'http':'http://127.0.0.1:8118',
#    'https':'https://127.0.0.1:8118'
}
bot = telebot.TeleBot(TOKEN) # be sure telebot.TeleBot calls after apihelper.proxy
```

[取消回复](https://blog.upx8.com/3727#respond-post-3727)

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