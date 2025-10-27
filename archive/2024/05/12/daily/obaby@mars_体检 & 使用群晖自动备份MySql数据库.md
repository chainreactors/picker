---
title: 体检 & 使用群晖自动备份MySql数据库
url: https://h4ck.org.cn/2024/05/16947
source: obaby@mars
date: 2024-05-12
fetch_date: 2025-10-06T17:16:12.852728
---

# 体检 & 使用群晖自动备份MySql数据库

[![obaby@mars](/wp-content/uploads/2023/08/logo-pink-small.png)](https://h4ck.org.cn)

Artificial Intelligence / Reverse Engineering / Internet of Things / Full Stack Developer

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

 [Menu](#mobilemenu)

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

[个人日记『Diary』](https://h4ck.org.cn/cats/dddd/grrj)

# 体检 & 使用群晖自动备份MySql数据库

2024年5月11日
[45 条评论](https://h4ck.org.cn/2024/05/16947#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2024/05/IMG_20220429_081813-tuya-scaled.webp)](https://h4ck.org.cn/wp-content/uploads/2024/05/IMG_20220429_081813-tuya.webp)

预约了今天早上七点半的体检，结果才六点半就被尿给憋醒了。开始轮流做各种乱七八糟的梦，实在憋不住了从床上爬起来看了下时间六点五十，虽然仅仅二十分钟，在梦里感觉似乎过了半个世纪那么长。

简单洗刷收拾之后，看了下时间尚早，开车过去也就十几分钟。于是打开电脑，看了下昨天写的备份脚本是不是执行成功了。嗯，如果不出意外的话就出意外了。备份文件大小是0。也就是失败了。

通过ssh登陆到群晖上跑了一下脚本，发现root账号登陆失败了。🤔这才想起来，root是禁止远程登录的，使用数据库的连接账号也失败了，权限太小。只好重新创建了一个备份专用账号，权限给的高一些，正好可以把几个数据库都倒出来，就不用管理不同的备份密码了，倒是也省力气了。

备份方法：

1.编写备份脚本，替换ip地址，用户名密码等信息

```
#!/bin/bash
# MySQL数据库的用户名
USER="backup_user"
# MySQL数据库的密码
PASSWORD="PASSWORD"
# 需要备份的数据库名
DATABASE="blog"
# 备份文件的保存路径
BACKUP_DIR="/volume1/backup/website_db_backup/blog"
# 备份文件名
BACKUP_NAME="backup-$(date +%Y%m%d%H%M%S).sql"
# 数据库IP地址
HOST_IP = "192.168.1.10"

# 备份MySQL数据库
mysqldump -h $HOST_IP -u $USER -p$PASSWORD $DATABASE > $BACKUP_DIR/$BACKUP_NAME

# 检查备份是否成功
if [ $? -eq 0 ]; then
    echo "MySQL backup completed successfully."
else
    echo "MySQL backup failed."
    exit 1
fi

# 删除10天以前的备份文件
find $BACKUP_DIR -name "backup-*.sql" -type f -mtime +10 -delete

# 删除操作完成后，输出提示信息
echo "Old backups deleted."
```

需要注意备份路径要填对哦

2.登陆群晖后台，点击控制面板打开任务计划：

[![](https://h4ck.org.cn/wp-content/uploads/2024/05/Jietu20240511-102059.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/05/Jietu20240511-102059.jpg)

3.新增任务输入任务名称，修改计划时间，任务设置输入运行命令：

```
bash /volume1/backup/backup_scripts/obaby.sh
```

[![](https://h4ck.org.cn/wp-content/uploads/2024/05/Jietu20240511-102706.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/05/Jietu20240511-102706.jpg)

4.添加任务之后，可以在任务列表邮件执行，如果要调试的话可以开启群晖的 ssh 功能，通过 ssh 进行脚本调试。

[![](https://h4ck.org.cn/wp-content/uploads/2024/05/Jietu20240511-102833-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/05/Jietu20240511-102833.jpg)

执行效果：

[![](https://h4ck.org.cn/wp-content/uploads/2024/05/Jietu20240511-102931-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/05/Jietu20240511-102931.jpg)

最下面的两个文件是备份脚本有问题，导致文件出错了。暂时先不管啦。

出门之后，发现路上开始淅淅沥沥的下小雨了。停好车，到医院的时间尚早，尚且开始叫号。领了个 17 号的号牌，虽然前面人不少，但是整体速度还是可以的。体检比上次来的时候感觉好了很多，几个费时的项目 B 超和心电图开启了智能排队功能，扫码可以看到是先做哪项检查。

做 B 超的小姐姐说，整体问题不大，除了脂肪肝，双肾有两个囊肿。甲状腺以及颈部的血管都挺好的。这两个囊肿已经存在了大约三四年的时间了，每年都能看到他们。除此之外，剩下的就得等体检报告了，现在是看不到什么东西了。

去公司的路上，雨下的更大了。绿灯起步之后超了几辆车，这时候看到头顶的闪光灯闪了一下，不知道是不是测速的，下意识的瞄了一眼速度表，指针刚好到中间，落到了 120 的位置上，心里不禁一凛，咯噔一下，这，千万别被拍啊。

等红绿灯的时候，在路口中间出现了三个大聪明，从执行车道强行跑到了左转上。嗯，貌似还是清一色的梅赛德斯，最近的是 C260，中间是 amg 45，最前面的没看到型号，这是组团左转的吗？

[![](https://h4ck.org.cn/wp-content/uploads/2024/05/WechatIMG806.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/05/WechatIMG806.jpg)

嗯，这个做法不错呢，可以少等两轮红绿灯，至少我已经等了两轮了。

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《体检 & 使用群晖自动备份MySql数据库》](https://h4ck.org.cn/2024/05/16947)
\* 本文链接：<https://h4ck.org.cn/2024/05/16947>
\* 短链接：<https://oba.by/?p=16947>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[Mysql](https://h4ck.org.cn/tags/mysql)[体检](https://h4ck.org.cn/tags/%E4%BD%93%E6%A3%80)[备份](https://h4ck.org.cn/tags/%E5%A4%87%E4%BB%BD)[群晖](https://h4ck.org.cn/tags/%E7%BE%A4%E6%99%96)

[Previous Post](https://h4ck.org.cn/2024/05/16956)
[Next Post](https://h4ck.org.cn/2024/05/16942)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2024年4月1日

#### [寻表记](https://h4ck.org.cn/2024/04/16129)

2025年9月8日

#### [改变](https://h4ck.org.cn/2025/09/21500)

2024年7月23日

#### [夏日游记 — episode 1 inner mongolia](https://h4ck.org.cn/2024/07/17587)

### 45 comments

1. ![](https://gg.lang.bi/avatar/44c40589887c2a6c75aab996bc0a381fa3e3f60b168761754818a9ea10a9d728?s=64&d=identicon&r=r) **[刘郎](https://yjvc.cn/)**说道：

   [2024年5月11日 11:28](https://h4ck.org.cn/2024/05/16947#comment-115094)

   ![Level 4](https://badgen.net/badge/亲密度/Level 4/yellow?icon=codebeat)

   ![Safari 17](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/safari.png "Safari 17") Safari 17 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   再憋会儿就把地图画上了~
   群晖还是超方便的

   [回复](#comment-115094)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2024年5月11日 11:39](https://h4ck.org.cn/2024/05/16947#comment-115098)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 124](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 124") Google Chrome 124 ![Android 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/android.png "Android 10") Android 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      🤣😂😅

      [回复](#comment-115098)
2. ![](https://gg.lang.bi/avatar/d838166f05390e17979f10c8e0fcc3b1d719369e6450e9eb30f218d8579263ee?s=64&d=identicon&r=r)

   [2024年5月11日 13:53](https://h4ck.org.cn/2024/05/16947#comment-115100)

   ![](https://badgen.net/badge/用户/已认证/CCFF33?icon=rss) ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 7](https://badgen.net/badge/亲密度/Level 7/pink?icon=codebeat)

   ![Google Chrome 124](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 124") Google Chrome 124 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   我刚做的体检时血糖高，所以不能喝饮料了。

   [回复](#comment-115100)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2024年5月11日 13:54](https://h4ck.org.cn/2024/05/16947#comment-115101)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 124](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 124") Google Chrome 124 ![Android 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/android.png "Android 10") Android 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      无糖的？喝点人工添加剂 😁

      [回复](#comment-115101)

      1. ![](https://gg.lang.bi/avatar/d838166f05390e17979f10c8e0fcc3b1d719369e6450e9eb30f218d8579263ee?s=64&d=identicon&r=r)

         [2024年5月11日 13:54](https://h4ck.org.cn/2024/05/16947#comment-115102)

         ![](https://badgen.net/badge/用户/已认证/CCFF33?icon=rss) ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 7](https://badgen.net/badge/亲密度/Level 7/pink?icon=codebeat)

         ![Google Chrome 124](https://h4ck.org.cn/wp-content/plugins/wp-useragent/i...