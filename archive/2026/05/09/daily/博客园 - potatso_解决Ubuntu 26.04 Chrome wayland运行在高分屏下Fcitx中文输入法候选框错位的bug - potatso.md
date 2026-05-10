---
title: 解决Ubuntu 26.04 Chrome wayland运行在高分屏下Fcitx中文输入法候选框错位的bug - potatso
url: https://www.cnblogs.com/potatso/p/20000431
source: 博客园 - potatso
date: 2026-05-09
fetch_date: 2026-05-10T05:36:58.168228
---

# 解决Ubuntu 26.04 Chrome wayland运行在高分屏下Fcitx中文输入法候选框错位的bug - potatso

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [周边](https://cnblogs.vip/store)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19316348)
* [YouClaw](https://youclaw.dev/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://www.cnblogs.com/my "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://www.cnblogs.com/my)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[potatso](https://www.cnblogs.com/potatso)

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/potatso/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/potatso)
* 订阅
* [管理](https://i.cnblogs.com/)

# [解决Ubuntu 26.04 Chrome wayland运行在高分屏下Fcitx中文输入法候选框错位的bug](https://www.cnblogs.com/potatso/p/20000431 "发布于 2026-05-09 10:54")

# 故障描述

chrome使用wayland模式，运行在高分屏下，会出现Fcitx中文输入法候选框错位的bug。在100%缩放比例下没有该问题。该问题只影响高分屏和chrome，其他软件均正常运行。

![截图 2026-05-09 10-33-31](https://img2024.cnblogs.com/blog/1916047/202605/1916047-20260509105042194-220645884.png)

# 分析

我们发现，wechat，飞书等应用输入法候选框是正常运行，查看参数，发现二者运行在X11模式下。所以我们让chrome强制运行在x11即可

```
(base) lzb@lzb-ProArt-PX13-HN7306EA:~/.local/bin$ xlsclients
lzb-ProArt-PX13-HN7306EA  WeChatAppEx
lzb-ProArt-PX13-HN7306EA  bytedance-feishu-stable
lzb-ProArt-PX13-HN7306EA  mutter-x11-frames
```

# 解决

chrome在wayland的高分屏模式下运行本身就会有很多bug，没有办法解决。只能在x11下运行。

修改`sudo vi /usr/share/applications/google-chrome.desktop`
修改启动参数，添加`--ozone-platform=x11`

```
Exec=/usr/bin/google-chrome-stable --ozone-platform=x11  %U
```

因为外接显示器的缩放率可能与内置显示器的缩放率不同，我们还要打开fcitx5的在X11上针对不同屏幕使用单独的dpi，如图

![截图 2026-05-09 11-24-34](https://img2024.cnblogs.com/blog/1916047/202605/1916047-20260509112606445-1441182288.png)

注销重新登录即可

# 成果

![截图 2026-05-09 10-54-56](https://img2024.cnblogs.com/blog/1916047/202605/1916047-20260509105516715-1565562353.png)

posted @
2026-05-09 10:54
[potatso](https://www.cnblogs.com/potatso)
阅读(3)
评论(0)

收藏
[举报](https://report.cnblogs.com?targetLink=https%3A%2F%2Fwww.cnblogs.com%2Fpotatso%2Fp%2F20000431&targetId=20000431&targetType=0)

刷新页面[返回顶部](#top)

[![](https://img2024.cnblogs.com/blog/35695/202512/35695-20251205182619157-1150461542.webp)](https://ais.cn/u/3Qf22e)

### 公告

[博客园](https://www.cnblogs.com/)
  ©  2004-2026