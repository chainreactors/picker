---
title: 关于若依Python（Django-Vue-Admin）的一些设置
url: http://h4ck.org.cn/2022/10/%e5%85%b3%e4%ba%8e%e8%8b%a5%e4%be%9dpython%ef%bc%88django-vue-admin%ef%bc%89%e7%9a%84%e4%b8%80%e4%ba%9b%e8%ae%be%e7%bd%ae/
source: obaby@mars
date: 2022-10-23
fetch_date: 2025-10-03T20:40:58.684087
---

# 关于若依Python（Django-Vue-Admin）的一些设置

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

[后台开发『BackEnd』](https://h4ck.org.cn/cats/cxsj/backend)

# 关于若依Python（Django-Vue-Admin）的一些设置

2022年10月22日
[3 条评论](https://h4ck.org.cn/2022/10/10564#comments)

![](https://image.h4ck.org.cn/wp-content/uploads/2022/10/cefc87f63e44d3688b594e4462d59e3b.jpg)

Django-Vue-Admin 是一套全部开源的快速开发平台，毫无保留给个人及企业免费使用。

* 前端采用ruoyi-ui 、Vue、Element UI。
* 后端采用Python语言Django框架。
* 权限认证使用Jwt，支持多终端认证系统。
* 支持加载动态权限菜单，多方式轻松权限控制。

1.恢复原生的admin后台：

系统并没有包含原生的admin后台界面，开发过程中如果要看数据在没有和前端对接的情况下要看数据智能通过数据库管理工具链接数据库查看，这个就很蛋疼了。要开启原生的admin后台也简单：

1）修改installed\_apps，添加admin：

```
INSTALLED_APPS = [
    'simpleui',#效果更直观
    'django.contrib.admin',
]
```

2）创建admin.py注册相关model：

```
from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import *

admin.site.register(Users, UserAdmin)

# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'code', 'sort']
```

![](https://image.h4ck.org.cn/wp-content/uploads/2022/10/Jietu20221022-134730-scaled.jpg)

2.无法通过python manage.py createsuperuser:由于系统修改了用户认证model并且没有实现 用户管理类，直接通过前面的命令创建用户就报错了。要修复这个问题，首先创建用户管理类：

1）在models中添加：

```
class MyUserManager(BaseUserManager):

    def create_user(self, username,email, password=None,is_active=True,is_staff=False,is_admin=False):
        """
        Creates and saves a User with the given email and password.
        """
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            username=username,
        )

        user.set_password(password)
        if email:
            user.email  = self.normalize_email(email)
        user.save(using=self._db)
        return user

    def create_staffuser(self, username,email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            username,
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, username,email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            username,
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

```

2）在user中添加：

```
objects = MyUserManager()
```

现在就可以正常通过命令创建superuser了。

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《关于若依Python（Django-Vue-Admin）的一些设置》](https://h4ck.org.cn/2022/10/10564)
\* 本文链接：<https://h4ck.org.cn/2022/10/10564>
\* 短链接：<https://oba.by/?p=10564>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[Django](https://h4ck.org.cn/tags/django)[Python](https://h4ck.org.cn/tags/python)[若依](https://h4ck.org.cn/tags/%E8%8B%A5%E4%BE%9D)

[Previous Post](https://h4ck.org.cn/2022/10/10567)
[Next Post](https://h4ck.org.cn/2022/10/10557)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2018年8月17日

#### [获取网页中所有的文字](https://h4ck.org.cn/2018/08/6238)

2023年3月2日

#### [爱看美女网爬虫【Windows】【23.03.02】](https://h4ck.org.cn/2023/03/11357)

2013年6月28日

#### [mitmproxy](https://h4ck.org.cn/2013/06/5240)

### 3 comments

1. ![](https://gg.lang.bi/avatar/d838166f05390e17979f10c8e0fcc3b1d719369e6450e9eb30f218d8579263ee?s=64&d=identicon&r=r) **[dujun](https://dujun.io)**说道：

   [2022年10月22日 21:39](https://h4ck.org.cn/2022/10/10564#comment-87975)

   ![](https://badgen.net/badge/用户/已认证/CCFF33?icon=rss) ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 7](https://badgen.net/badge/亲密度/Level 7/pink?icon=codebeat)

   ![Google Chrome 106](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 106") Google Chrome 106 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   我到现在还没用过 vue， 还是 jquery 的水平。

   [回复](#comment-87975)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2022年10月22日 21:47](https://h4ck.org.cn/2022/10/10564#comment-87978)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 104](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 104") Google Chrome 104 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      其实前端我也不专业~~后端还能搞搞

      [回复](#comment-87978)
2. ![](https://gg.lang.bi/avatar/fb86062faf44ff861c064616932e1b3f64926b89c1e3d6aef60a54dcaf7d93dc?s=64&d=identicon&r=r)

   [2022年10月24日 16:46](https://h4ck.org.cn/2022/10/10564#comment-88058)

   ![Level 1](https://badgen.net/badge/亲密度/Level 1/gray?icon=codebeat)

   ![Google Chrome 104](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 104") Google Chrome 104 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   ![smile](https://h4ck.org.cn/wp-content/plugins/kama-wp-smile/packs/qip/smile.gif)

   [回复](#comment-88058)

### 发表回复 [取消回复](/2022/10/10564#respond)

您的邮箱地址不会被公开。 必填项已用 \* 标注

评论 \*

显示名称 \*

邮箱 \*

网站

[ ]  在此浏览器中保存我的显示名称、邮箱地址和网站地址，以便下次评论时使用。

[x] 如果有人回复我的评论，请通过电子邮件通知我。

[x]

Δ

### 标签云[Tag Cloud]

Your browser doesn't support the HTML5 CANVAS tag.

* [C/C++](https://h4ck.org.cn/tags/cc)
* [IDA](https://h4ck.org.cn/tags/ida)
* [无题](https://h4ck.org.cn/tags/nomean)
* [Porn](https://h4ck.org.cn/tags/porn)
* [iOS](https://h4ck.org.cn/tags/ios)
* [Android](https://h4ck.org.cn/tags/android)
* [月经](https://h4ck.org.cn/tags/%E6%9C%88%E7%BB%8F)
* [系统美化](https://h4ck.org.cn/tags/os-diy)
* [Debugger](https://h4ck.org.cn/tags/debugger)
* [大姨妈](https://h4ck.org.cn/tags/%E5%A4%A7%E5%A7%A8%E5%A6%88)
* [美女](https://h4ck.org.cn/tags/beauty)
* [Django](https://h4ck.org.cn/tags/django)
* [妹子图](https://h4ck.org.cn/tags/%E5%A6%B9%E5%AD%90%E5%9B%BE)
* [Mac OS](https://h4ck.org.cn/tags/mac-os)
* [UniApp](https://h4ck.org.cn/tags/uniapp)
* [闺蜜圈](https://h4ck.org.cn/tags/%E9%97%BA%E8%9C%9C%E5%9C%88)
* [Windows](https://h4ck.org.cn/tags/windows)
* [爬虫](https://h4ck.org.cn/tags/%E7%88%AC%E8%99%AB)
* [秀人集](https://h4ck.org.cn/tags/%E7%A7%80%E4%BA%BA%E9%9B%86)
* [心情](https://h4ck.org.cn/tags/myfeeling)
* [驱动开发](https://h4ck.org.cn/tags/driver-develop)
* [ubuntu](https://h4ck.org.cn/tags/ubuntu)
* [游戏](https://h4ck.org.cn/tags/ga...