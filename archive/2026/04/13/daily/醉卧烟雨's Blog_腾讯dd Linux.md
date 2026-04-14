---
title: 腾讯dd Linux
url: https://blog.cctv.com.im/4276
source: 醉卧烟雨's Blog
date: 2026-04-13
fetch_date: 2026-04-14T04:38:53.718320
---

# 腾讯dd Linux

# 腾讯dd Linux

* [首页](https://blog.cctv.com.im/)
* [留言](/2002)
* [归档](https://blog.cctv.com.im/archives)

##

2026-04-13 /
 0评 /
0赞

赏

码

*移动设备上继续阅读*

清除腾讯监控，逐条拷贝执行即可：

```
systemctl stop tat_agent
systemctl disable tat_agent
rm -rf /etc/systemd/system/tat_agent.service
rm -fr /usr/local/qcloud

ps -A | grep agent
# 检查看是否还有腾讯云组件
# kill 这个进程
```

剩下的看这里：<https://github.com/leitbogioro/Tools>

* [linux](https://blog.cctv.com.im/tag/linux)

[RealtekAudioControl\_1.51.328](https://blog.cctv.com.im/4273)

### 发表回复 [取消回复](/4276#respond)

您的邮箱地址不会被公开。 必填项已用 \* 标注

显示名称 \*

邮箱 \*

网站

[ ]  在此浏览器中保存我的显示名称、邮箱地址和网站地址，以便下次评论时使用。

评论 \*

![](https://blog.cctv.com.im/wp-content/plugins/wp-alu-master/static/img/icon_mrgreen.gif)![](https://blog.cctv.com.im/wp-content/plugins/wp-alu-master/static/img/icon_neutral.gif)![](https://blog.cctv.com.im/wp-content/plugins/wp-alu-master/static/img/icon_twisted.gif)![](https://blog.cctv.com.im/wp-content/plugins/wp-alu-master/static/img/icon_arrow.gif)![](https://blog.cctv.com.im/wp-content/plugins/wp-alu-master/static/img/icon_eek.gif)![](https://blog.cctv.com.im/wp-content/plugins/wp-alu-master/static/img/icon_smile.gif)![](https://blog.cctv.com.im/wp-content/plugins/wp-alu-master/static/img/icon_confused.gif)![](https://blog.cctv.com.im/wp-content/plugins/wp-alu-master/static/img/icon_cool.gif)![](https://blog.cctv.com.im/wp-content/plugins/wp-alu-master/static/img/icon_evil.gif)![](https://blog.cctv.com.im/wp-content/plugins/wp-alu-master/static/img/icon_biggrin.gif)![](https://blog.cctv.com.im/wp-content/plugins/wp-alu-master/static/img/icon_idea.gif)![](https://blog.cctv.com.im/wp-content/plugins/wp-alu-master/static/img/icon_redface.gif)![](https://blog.cctv.com.im/wp-content/plugins/wp-alu-master/static/img/icon_razz.gif)![](https://blog.cctv.com.im/wp-content/plugins/wp-alu-master/static/img/icon_rolleyes.gif)![](https://blog.cctv.com.im/wp-content/plugins/wp-alu-master/static/img/icon_wink.gif)![](https://blog.cctv.com.im/wp-content/plugins/wp-alu-master/static/img/icon_cry.gif)![](https://blog.cctv.com.im/wp-content/plugins/wp-alu-master/static/img/icon_surprised.gif)![](https://blog.cctv.com.im/wp-content/plugins/wp-alu-master/static/img/icon_lol.gif)![](https://blog.cctv.com.im/wp-content/plugins/wp-alu-master/static/img/icon_mad.gif)![](https://blog.cctv.com.im/wp-content/plugins/wp-alu-master/static/img/icon_sad.gif)![](https://blog.cctv.com.im/wp-content/plugins/wp-alu-master/static/img/icon_exclaim.gif)![](https://blog.cctv.com.im/wp-content/plugins/wp-alu-master/static/img/icon_question.gif)

Δ

* [关于](https://blog.cctv.com.im/about)
* [订阅](/feed)

© 2026 [醉卧烟雨's Blog](https://blog.cctv.com.im)

Theme by [Adams](https://biji.io)

* 默认
* 护眼
* 夜晚
* Serif
* Sans