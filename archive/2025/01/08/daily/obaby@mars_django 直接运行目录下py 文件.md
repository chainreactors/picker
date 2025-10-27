---
title: django 直接运行目录下py 文件
url: https://h4ck.org.cn/2025/01/18968
source: obaby@mars
date: 2025-01-08
fetch_date: 2025-10-06T20:08:55.577556
---

# django 直接运行目录下py 文件

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

# django 直接运行目录下py 文件

2025年1月7日
[17 条评论](https://h4ck.org.cn/2025/01/18968#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2025/01/WechatIMG880.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/01/WechatIMG880.jpg)

为了处理数据，直接写了一个文件用来处理解析数据。然而比较诡异的一点是，使用 pycharm 可以直接运行这个文件，不会报错。但是，如果用命令运行就直接报错了。

[![](https://h4ck.org.cn/wp-content/uploads/2025/01/Screenshot-2025-01-05-123315.png)](https://h4ck.org.cn/wp-content/uploads/2025/01/Screenshot-2025-01-05-123315.png)

上面是 pycharm 的运行效果，下面是直接命令运行的效果。

[![](https://h4ck.org.cn/wp-content/uploads/2025/01/Screenshot-2025-01-05-123327.png)](https://h4ck.org.cn/wp-content/uploads/2025/01/Screenshot-2025-01-05-123327.png)

```
(venv) PS E:\Pycharm_Projects\powersystem> E:\Pycharm_Projects\powersystem\venv\Scripts\python.exe E:\Pycharm_Projects\powersystem\application\data_process_test.py
Traceback (most recent call last):
  File "E:\Pycharm_Projects\powersystem\application\data_process_test.py", line 17, in <module>
    django.setup()
  File "E:\Pycharm_Projects\powersystem\venv\lib\site-packages\django\__init__.py", line 19, in setup
    configure_logging(settings.LOGGING_CONFIG, settings.LOGGING)
  File "E:\Pycharm_Projects\powersystem\venv\lib\site-packages\django\conf\__init__.py", line 82, in __getattr__
    self._setup(name)
  File "E:\Pycharm_Projects\powersystem\venv\lib\site-packages\django\conf\__init__.py", line 69, in _setup
    self._wrapped = Settings(settings_module)
  File "E:\Pycharm_Projects\powersystem\venv\lib\site-packages\django\conf\__init__.py", line 170, in __init__
    mod = importlib.import_module(self.SETTINGS_MODULE)
  File "G:\Python3.10.6\lib\importlib\__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 992, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1004, in _find_and_load_unlocked
ModuleNotFoundError: No module named 'application'
```

提示的错误信息是找不到 application，但是这个文件是作为 django 的一部分存在的，按理也不需要去设置什么东西。之前的时候不能运行也就算了，但是现在有台服务器在内网，无法链接内网的的数据库进行数据处理，这就比较麻烦。

不过既然 pycharm 能运行，那肯定是有些东西不一样，猜测是 pycharm 将当前的目录加入 lib 目录了。添加下面的代码重新运行。

```
import os,sys

if __name__ == '__main__':
    # 获取当前脚本所在目录的绝对路径
    current_directory = os.path.abspath(os.path.dirname(__file__))

    # 将当前目录添加到sys.path
    sys.path.append("E:/Pycharm_Projects/powersystem/")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "application.settings")
    import django

    django.setup()
    label =get_device_label(msg['devvar'])
    new_msg = rebuild_msg(msg, label)
    print(new_msg)
```

现在一切就 ok 了。

[![](https://h4ck.org.cn/wp-content/uploads/2025/01/Screenshot-2025-01-05-123943.png)](https://h4ck.org.cn/wp-content/uploads/2025/01/Screenshot-2025-01-05-123943.png)

其他的运行脚本方式：

https://django-extensions-zh.readthedocs.io/zh-cn/latest/runscript.html

https://www.jb51.net/article/236739.htm

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《django 直接运行目录下py 文件》](https://h4ck.org.cn/2025/01/18968)
\* 本文链接：<https://h4ck.org.cn/2025/01/18968>
\* 短链接：<https://oba.by/?p=18968>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[Django](https://h4ck.org.cn/tags/django)[Pycharm](https://h4ck.org.cn/tags/pycharm)[Python](https://h4ck.org.cn/tags/python)

[Previous Post](https://h4ck.org.cn/2025/01/18978)
[Next Post](https://h4ck.org.cn/2025/01/18956)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2013年7月18日

#### [Spyder –the Scientific PYthon Development EnviRonment](https://h4ck.org.cn/2013/07/5270)

2024年3月4日

#### [未雨绸缪](https://h4ck.org.cn/2024/03/15722)

2022年8月12日

#### [Django 代码保护](https://h4ck.org.cn/2022/08/10306)

### 17 comments

1. ![](https://gg.lang.bi/avatar/19a53855a6616e2ead18670b736d1917a8b5dbe3f22d629e637d9e3f384e451f?s=64&d=identicon&r=r) **[小彦](https://note-star.cn/)**说道：

   [2025年1月7日 11:36](https://h4ck.org.cn/2025/01/18968#comment-122824)

   ![](https://badgen.net/badge/用户/已认证/CCFF33?icon=rss) ![Level 6](https://badgen.net/badge/亲密度/Level 6/red?icon=codebeat)

   ![Microsoft Edge 131](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/edge-2.png "Microsoft Edge 131") Microsoft Edge 131 ![Windows 11](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 11") Windows 11 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   怀孕了，自拍孕照~

   [回复](#comment-122824)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2025年1月7日 12:58](https://h4ck.org.cn/2025/01/18968#comment-122826)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 130](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 130") Google Chrome 130 ![Android 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/android.png "Android 10") Android 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      只是大而已 ![laugh1](https://h4ck.org.cn/wp-content/plugins/kama-wp-smile/packs/qip/laugh1.gif)

      [回复](#comment-122826)
2. ![](https://gg.lang.bi/avatar/f40b0e33d5ff14853f68e06d9583b6672c844267507ed0603c02f7bdf5714ba6?s=64&d=identicon&r=r)

   [2025年1月7日 11:53](https://h4ck.org.cn/2025/01/18968#comment-122825)

   ![Level 6](https://badgen.net/badge/亲密度/Level 6/red?icon=codebeat)

   ![Google Chrome 131](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 131") Google Chrome 131 ![Windows 11](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 11") Windows 11 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   技术不懂，但图片让人能多逗留几分！

   [回复](#comment-122825)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2025年1月7日 13:19](https://h4ck.org.cn/2025/01/18968#comment-122827)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 126](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 126") Google Chrome 126 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-u...