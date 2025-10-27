---
title: 华为云电脑 DD windows（保姆级教程）
url: https://blog.upx8.com/4783
source: 黑海洋 - Wiki
date: 2025-05-03
fetch_date: 2025-10-06T22:27:44.541537
---

# 华为云电脑 DD windows（保姆级教程）

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 华为云电脑 DD windows（保姆级教程）

发布时间:
2025-05-02

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
70985

把华云云电脑DD成Win系统，禁止计时功能，无限使用。

开通地址：[https://devstation.connect.huaweicloud.com](https://blog.upx8.com/go/aHR0cHM6Ly9kZXZzdGF0aW9uLmNvbm5lY3QuaHVhd2VpY2xvdWQuY29t)

### CPU 架构从 ARM 改为 x86

打开云[电脑控制台](https://blog.upx8.com/go/aHR0cHM6Ly9kZXZlbG9wZXIuaHVhd2VpY2xvdWQuY29tL3NwYWNlL2RldnBvcnRhbC9kZXNrdG9w)，点击重置，配置云电脑主机，CPU 架构 修改`ARM`改为`x86`

### ![](https://cdn.skyimg.net/up/2025/5/2/ef36f81a.webp)

### 完整操作流程（Linux环境下DD安装Windows系统）

![](https://cdn.skyimg.net/up/2025/5/2/ab288c74.webp)

1. **修改root密码**

```
sudo passwd root
# 输入当前密码（若需要）→ 设置新密码 → 确认新密码

su root
# 输入刚设置的密码切换至root权限
```

2. **下载安装脚本**

```
curl -O https://cnb.cool/bin456789/reinstall/-/git/raw/main/reinstall.sh || wget -O reinstall.sh $_
```

3. **执行DD安装Win10（华为云电脑适用版）**

```
bash reinstall.sh windows --image-name "Windows 10 Enterprise LTSC 2021" --password "ABCabc123" --iso "http://jdc.cool/d/Yd/WIN10_LSTC_TVNC(1).iso?sign=6vi1vIzVA8TQoIvCm6Y8ghpzAF3hifJXSeymk8recX0=:0"
```

### ![](https://cdn.skyimg.net/up/2025/5/2/bc1da0ca.webp)

### 关键注意事项

1. **部署阶段**

* 等待2-3分钟脚本执行 → 自动`reboot`
* 等待20-30分钟（期间不要操作控制台）

2. **成功验证**

* 控制台出现Windows登录界面即成功
* 控制台点击开机或者返回开发者工作台页面重启进入

`![](https://cdn.skyimg.net/up/2025/5/2/7c860130.webp)`

* 使用远程桌面连接（默认凭证）：

  ```
  用户名: administrator
  密码: ABCabc123
  ```

3. **资源管理技巧**

* 完成操作后务必通过[华为云工作台](https://blog.upx8.com/go/aHR0cHM6Ly9kZXZlbG9wZXIuaHVhd2VpY2xvdWQuY29tL3NwYWNlL2RldnBvcnRhbC9kZXNrdG9w)点击"关机"，这样就不会计时了.
* 推荐安装向日葵、UU远程控制等工具实现持久化管理

1. ![abclhx](//q2.qlogo.cn/headimg_dl?dst_uin=17807274&spec=100)

   **abclhx**

   2025-06-20 06:47:24

   [回复](https://blog.upx8.com/4783/comment-page-1?replyTo=30620#respond-post-4783)

   https://devstation.connect.huaweicloud.com这个链接打不开
2. ![关之琳](//q2.qlogo.cn/headimg_dl?dst_uin=136699799&spec=100)

   **关之琳**

   2025-05-02 18:09:05

   [回复](https://blog.upx8.com/4783/comment-page-1?replyTo=30585#respond-post-4783)

   成功了，谢谢

[取消回复](https://blog.upx8.com/4783#respond-post-4783)

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