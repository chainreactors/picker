---
title: 美女图片整理工具 V1.0
url: https://h4ck.org.cn/2023/01/%e7%be%8e%e5%a5%b3%e5%9b%be%e7%89%87%e6%95%b4%e7%90%86%e5%b7%a5%e5%85%b7-v1-0/
source: obaby@mars
date: 2023-01-10
fetch_date: 2025-10-04T03:23:13.252685
---

# 美女图片整理工具 V1.0

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

[业余爱好『Favourite』](https://h4ck.org.cn/cats/cxsj/%E4%B8%9A%E4%BD%99%E7%88%B1%E5%A5%BD%E3%80%8Efavourite%E3%80%8F)

# 美女图片整理工具 V1.0

2023年1月9日
[11 条评论](https://h4ck.org.cn/2023/01/10966#comments)

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/01/1d5927bc7c29a7b10d9e395baf1b335a.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/01/1d5927bc7c29a7b10d9e395baf1b335a.jpg)

不知道有没有和姐姐我一样把所有美女的图片都下载下来的，如果没有下载的话可以通过博客的搜索功能搜索爬虫去下载妹子图片了哦。通过爬取的乱七八糟的各种网站，目前粗略的估计所有下载的图片大约有1T左右了。由于各个网站都是分别的下载的，所有下载后的图片会有很多重复的。想找一个图片处理工具，找了半天有个什么推荐的eagle的工具，还是收费的，可以免费试用一个月。结果我把下载的图片目录加进去直接卡死了。啊哈哈。这就离谱，所以如果没有图片处理需求的还是推荐picasa3，我也有发布一个补丁工具，真的是一代神器。

既然没有现成的工具，那就写一个吧，具体的要求：

```
1.能够把所有文件复制到同一个目录下（这不是废话嘛，就是为了干这个的啊）
2.能够过滤10k以下的非图片文件（多数是由于被爬取网站不稳定导致的下载失败，其实不是图片文件）
3.对于不同网站下载的同一个图片不要重复复制（通过计算文件md5的方法进行规避）
4.能够记录整理日志（当然啊，不然那么多文件中间关机了，岂不是得全部再来一遍）
主要就是上面的几个要求啦~~~
```

话不多说，开干吧，为了简化代码，这里没有使用os模块，相对代码也就简单了很多，完整代码如下：

```
# 妹子图整理工具 by obaby
# http://h4ck.org.cn
# http://nai.dog
# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
from pathlib import Path
import hashlib
import shutil
from pyfiglet import Figlet

source_file_paths = [
    Path(r'I:\jpmvb'),
    Path(r'I:\ku138'),
    Path(r'I:\微图坊'),
    Path(r'G:\xgmn'),
    Path(r'G:\xrmnw'),
    Path(r'G:\图片'),
    Path(r'G:\秀人集')
]

dest_file_path = Path('I:\Beauty_Images')

def get_done_paths():
    p = Path('logs.txt')
    if not p.exists():
        return []
    with Path('logs.txt') as f:
        content = open(f, 'r', encoding='utf8')
        return [c.strip() for c in content.readlines()]

def append_done_paths(path_name):
    p = Path('logs.txt')
    content = open(p, 'a+', encoding='utf8')
    content.write(path_name + '\n')

def print_hack():
    print('*' * 100)
    # f = Figlet(font='slant')
    f = Figlet()
    print(f.renderText('obaby@mars'))
    print('美女图片整理工具 V1.0')
    print('Verson: 23.01.09')
    print('Blog: http://www.h4ck.org.cn')
    print('*' * 100)

done_paths = get_done_paths()

def calc_file_md5(img):
    content = open(img, 'rb').read()
    file_md5 = hashlib.md5(content).hexdigest()
    return file_md5

def get_image_md5_in_path(p):
    md5_list = []
    for img in p.glob('*.*'):
        md5_list.append(calc_file_md5(img))
    return md5_list

def copy_image_to_dest(p):
    global done_paths
    print('=' * 200)
    print('[M] 开始复制目录' + p.name + ' ......')
    for dir in p.iterdir():
        if str(dir.resolve()) in done_paths:
            print('[*]' + dir.name + ' 已经完成复制，跳过')
            print('*' * 100)
            continue
        dest_parts = dir.parts[-1]
        dest_path = dest_file_path / dest_parts
        img_md5_list = []
        if dest_path.exists():
            print('[D] 目标文件路径：'+ dest_path.name + '已经存在，正在创建图片md5 列表')
            img_md5_list = get_image_md5_in_path(dest_path)
            print('[D] Md5 list = ' , img_md5_list)
        else:
            dest_path.mkdir(parents=True, exist_ok=False)
        for img in dir.glob('*.*'):
            # print(img)
            # 处理大于100k文件
            if int(img.stat().st_size) > 10000:
                image_name = img.name
                if len(img_md5_list) > 0 :
                    img_md5 = calc_file_md5(img)
                    if img_md5 in img_md5_list:
                        print('[*]' + img.name + ' 检测到存在同值md5文件，跳过')
                        continue
                else:
                    dest_image_file_path = dest_path / image_name
                    shutil.copy(img, dest_image_file_path)
                    print('[*]' + img.name + ' 已经复制')

            else:
                print('[*]' + img.name + ' 文件小于10k，跳过')
        print('[*]' + dir.name + ' 目录复制完成，添加到完成列表')
        print('-' * 200)
        append_done_paths(str(dir.resolve()))
        done_paths.append(str(dir.resolve()))

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hack()
    # append_done_paths('c/dir')
    # done_list = get_done_paths()
    # print(done_list)
    # test_path = Path(r'G:\秀人集')
    # tp = Path(r'G:\秀人集\[XINGYAN星颜社]VOL.154_女神王雨纯脱深色日式和服露性感白色内衣配超薄肉丝诱惑写真82P')
    # print(tp.name)
    # ml = get_image_md5_in_path(Path(r'G:\秀人集\[XINGYAN星颜社]VOL.154_女神王雨纯脱深色日式和服露性感白色内衣配超薄肉丝诱惑写真82P'))
    # print(ml)
    print('*' * 100)
    print('[S] 开始处理图片：')
    for p in source_file_paths:
        copy_image_to_dest(p)

    print('[D] 所有目录复制完成。请欣赏图片吧。')
    print('*' * 100)
```

实际复制效果也挺好的，磁盘基本跑慢了：

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/01/搜狗截图20230109214537.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/01/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20230109214537.jpg)

目标路径：

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/01/搜狗截图20230109214650.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/01/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20230109214650.jpg)

整理的时候修改这两个路径即可：

```
source_file_paths = [
    Path(r'I:\jpmvb'),
    Path(r'I:\ku138'),
    Path(r'I:\微图坊'),
    Path(r'G:\xgmn'),
    Path(r'G:\xrmnw'),
    Path(r'G:\图片'),
    Path(r'G:\秀人集')
]

dest_file_path = Path('I:\Beauty_Images')
```

运行环境Python 3.8及以上，pip列表：

```
(venv) PS F:\Pycharm_Projects\beauty_image_copyer> pip list
Package    Version
---------- ---------
pyfiglet   0.8.post1
```

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《美女图片整理工具 V1.0》](https://h4ck.org.cn/2023/01/10966)
\* 本文链接：<https://h4ck.org.cn/2023/01/10966>
\* 短链接：<https://oba.by/?p=10966>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[pathlib](https://h4ck.org.cn/tags/pathlib)[Python3](https://h4ck.org.cn/tags/python3)[秀人集](https://h4ck.org.cn/tags/%E7%A7%80%E4%BA%BA%E9%9B%86)[美女图片](https://h4ck.org.cn/tags/%E7%BE%8E%E5%A5%B3%E5%9B%BE%E7%89%87)

[Previous Post](https://h4ck.org.cn/2023/01/10971)
[Next Post](https://h4ck.org.cn/2023/01/10931)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2023年6月29日

#### [Domain Admin–域名 证书到期监控](https://h4ck.org.cn/2023/06/12366)

2023年8月4日

#### [爱图集谷爬虫<预览版>[23.08.04][Windows]](https://h4ck.org.cn/2023/08/12801)

2021年1月4日

#### [Findu 软著证书](https://h4ck.org.cn/2021/01/7957)

### 11 comments

1. ![](https://gg.lang.bi/avatar/d838166f05390e17979f10c8e0fcc3b1d719369e6450e9eb30f218d8579263ee?s=64&d=identicon&r=r) **[dujun](https://dujun.io)**说道：

   [2023年1月10日 01:01](https://h4ck.org.cn/2023/01/10966#comment-90966)

   ![](https://badgen.net/badge/用户/已认证/CCFF33?icon=rss) ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 7](https://badgen.net/badge/亲密度/Level 7/pink?icon=codebeat)

   ![Google Chrome 108](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 108") Google Chrome 108 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   我也写了很多整理的脚本

   [回复](#comment-90966)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc...