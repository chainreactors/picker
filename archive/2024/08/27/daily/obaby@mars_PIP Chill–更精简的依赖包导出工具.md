---
title: PIP Chill–更精简的依赖包导出工具
url: https://h4ck.org.cn/2024/08/17921
source: obaby@mars
date: 2024-08-27
fetch_date: 2025-10-06T18:02:19.657789
---

# PIP Chill–更精简的依赖包导出工具

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

[系统相关『OS』](https://h4ck.org.cn/cats/xtxg)

# PIP Chill–更精简的依赖包导出工具

2024年8月26日
[17 条评论](https://h4ck.org.cn/2024/08/17921#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2024/05/7e3a6041a07f306edbc57d202aa7f34d-1.webp)](https://h4ck.org.cn/wp-content/uploads/2024/05/7e3a6041a07f306edbc57d202aa7f34d-1.webp)

Make requirements with only the packages you need

项目导入的 module 越多，导出的依赖库就越多，尤其是很多系统自带的库一并给导出来来了。

pip freeze 导出效果：

```
asgiref==3.3.4
async-timeout==4.0.3
certifi==2021.5.30
chardet==4.0.0
coreapi==2.3.3
coreschema==0.0.4
Django==3.2.3
django-admin-lightweight-date-hierarchy==1.1.0
django-comment-migrate==0.1.5
django-cors-headers==3.10.1
django-crontab==0.7.1
django-export-xls==0.1.1
django-filter==21.1
django-ranged-response==0.2.0
django-redis==5.2.0
django-restql==0.15.4
django-simple-captcha==0.5.14
django-simpleui==2022.7.29
django-timezone-field==4.2.3
djangorestframework==3.12.4
djangorestframework-simplejwt==5.1.0
drf-yasg==1.20.0
et-xmlfile==1.1.0
idna==2.10
inflection==0.5.1
itypes==1.2.0
Jinja2==3.0.1
MarkupSafe==2.0.1
openpyxl==3.0.9
packaging==20.9
paho-mqtt==1.6.1
Pillow==8.3.1
PyJWT==2.1.0
PyMySQL==1.0.2
pyparsing==2.4.7
pyPEG2==2.15.2
pypinyin==0.46.0
pypng==0.20220715.0
pytz==2021.1
qrcode==7.4.2
redis==5.0.8
requests==2.25.1
ruamel.yaml==0.18.6
ruamel.yaml.clib==0.2.8
simplejson==3.18.4
six==1.16.0
smmap==4.0.0
sqlparse==0.4.1
typing-extensions==3.10.0.0
tzlocal==2.1
ua-parser==0.10.0
uritemplate==3.0.1
urllib3==1.26.6
user-agents==2.2.0
whitenoise==5.3.0
xlwt==1.3.0
```

pip-chill 导出效果：

```
django-admin-lightweight-date-hierarchy==1.1.0
django-comment-migrate==0.1.5
django-cors-headers==3.10.1
django-crontab==0.7.1
django-export-xls==0.1.1
django-filter==21.1
django-redis==5.2.0
django-restql==0.15.4
django-simple-captcha==0.5.14
django-simpleui==2022.7.29
django-timezone-field==4.2.3
djangorestframework-simplejwt==5.1.0
drf-yasg==1.20.0
encryptpy==1.0.5
openpyxl==3.0.9
paho-mqtt==1.6.1
pip-chill==1.0.3
pycryptodome==3.20.0
pymysql==1.0.2
pypinyin==0.46.0
qrcode==7.4.2
simplejson==3.18.4
tzlocal==2.1
user-agents==2.2.0
whitenoise==5.3.0
```

整体减掉了差不多一半多，同样在构建环境的时候也少了很多可能出问题的包，尤其是跨平台 install 的时候。

官方用法：

```
Suppose you have installed in your virtualenv a couple packages. When you run pip freeze, you'll get a list of all packages installed, with all dependencies. If one of the packages you installed ceases to depend on an already installed package, you have to manually remove it from the list. The list also makes no distinction about the packages you actually care about and packages your packages care about, making the requirements file bloated and, ultimately, inaccurate.

On your terminal, run:

$ pip-chill
bandit==1.7.0
bumpversion==0.6.0
click==7.1.2
coverage==5.3.1
flake8==3.8.4
nose==1.3.7
pip-chill==1.0.1
pytest==6.2.1
...
Or, if you want it without version numbers:

$ pip-chill --no-version
bandit
bumpversion
click
coverage
flake8
nose
pip-chill
pytest
...
Or, if you want it without pip-chill:

$ pip-chill --no-chill
bandit==1.7.0
bumpversion==0.6.0
click==7.1.2
coverage==5.3.1
flake8==3.8.4
nose==1.3.7
pytest==6.2.1
...
Or, if you want to list package dependencies too:

$ pip-chill -v
bandit==1.7.0
bumpversion==0.6.0
click==7.1.2
coverage==5.3.1
flake8==3.8.4
nose==1.3.7
pip-chill==1.0.1
pytest==6.2.1
sphinx==3.4.3
tox==3.21.1
twine==3.3.0
watchdog==1.0.2
# alabaster==0.7.12 # Installed as dependency for sphinx
# appdirs==1.4.4 # Installed as dependency for virtualenv
# attrs==20.3.0 # Installed as dependency for pytest
# babel==2.9.0 # Installed as dependency for sphinx
```

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《PIP Chill–更精简的依赖包导出工具》](https://h4ck.org.cn/2024/08/17921)
\* 本文链接：<https://h4ck.org.cn/2024/08/17921>
\* 短链接：<https://oba.by/?p=17921>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[pip](https://h4ck.org.cn/tags/pip)[pip-chill](https://h4ck.org.cn/tags/pip-chill)[Python](https://h4ck.org.cn/tags/python)

[Previous Post](https://h4ck.org.cn/2024/08/17926)
[Next Post](https://h4ck.org.cn/2024/08/17881)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2012年6月27日

#### [PyDbg安装（《Python 灰帽子》）](https://h4ck.org.cn/2012/06/4275)

2021年10月18日

#### [L0phtCrack 7.2.0](https://h4ck.org.cn/2021/10/9178)

2023年9月20日

#### [CPUID HARDWARE MONITOR PRO1.53.0 SN](https://h4ck.org.cn/2023/09/13417)

### 17 comments

1. ![](https://gg.lang.bi/avatar/c8b1c4e066955840427abd9f454b9fb9569d4480ec1b84bb78c8b210d91893d8?s=64&d=identicon&r=r) **爱看**说道：

   [2024年8月26日 17:22](https://h4ck.org.cn/2024/08/17921#comment-118629)

   ![Level 6](https://badgen.net/badge/亲密度/Level 6/red?icon=codebeat)

   ![Microsoft Edge 126](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/edge-2.png "Microsoft Edge 126") Microsoft Edge 126 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![us](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/us.svg "us")

   号外号外，灵妹妹更新啦，虽然看不懂

   [回复](#comment-118629)
2. ![](https://gg.lang.bi/avatar/40c46b2a6ef05464946a7e3f5230bdfa16b5d4e861c7b69977ef77efde66638a?s=64&d=identicon&r=r)

   [2024年8月26日 19:19](https://h4ck.org.cn/2024/08/17921#comment-118631)

   ![Level 4](https://badgen.net/badge/亲密度/Level 4/yellow?icon=codebeat)

   ![Chrome 128](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Chrome 128") Chrome 128 ![iPhone iOS 17.6](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/device/iphone.png "iPhone iOS 17.6") iPhone iOS 17.6 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   配图好评，快把我掰直了

   [回复](#comment-118631)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2024年8月26日 21:44](https://h4ck.org.cn/2024/08/17921#comment-118637)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 126](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 126") Google Chrome 126 ![Android 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/android.png "Android 10") Android 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      别，直了多一伤心人。

      [回复](#comment-118637)

      1. ![](https://gg.lang.bi/avatar/6714902faba36861d49b244a31167852e673fd2b07fd055355346582b0d723b4?s=64&d=identicon&r=r)

         [2024年8月27日 09:31](https://h4ck.org.cn/2024/08/17921#comment-118649)

         ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 6](https://badgen.net/badge/亲密度/Level 6/red?icon=codebeat)

         ![Google Chrome 127](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 127") Google Chrome 127 ![Windows 10](https://h4ck.org.cn/wp-conte...