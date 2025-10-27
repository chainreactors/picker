---
title: 100行代码实现 favicon 小工具
url: https://h4ck.org.cn/2024/09/18075
source: obaby@mars
date: 2024-09-25
fetch_date: 2025-10-06T18:25:16.169604
---

# 100行代码实现 favicon 小工具

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

# 100行代码实现 favicon 小工具

2024年9月24日
[77 条评论](https://h4ck.org.cn/2024/09/18075#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2024/09/WechatIMG1132.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/09/WechatIMG1132.jpg)

这几天查看统计的时候发现统计页面的小图标不显示了。

[![](https://h4ck.org.cn/wp-content/uploads/2024/09/Jietu20240923-190759-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/09/Jietu20240923-190759.jpg)

图标变成了一个白色方框，这个umami 一直无法加载 favicon，之前换成了：https://favicon.cccyun.cc/h4ck.org.cn

现在这个服务貌似证书过期了，也没人维护，看来也没多少人用啊：

[![](https://h4ck.org.cn/wp-content/uploads/2024/09/Jietu20240924-101244.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/09/Jietu20240924-101244.jpg)

本着能动手尽量别 bb 的理念，既然不能用了那就自建服务吧。

个人觉得最简单的代码还是通过 python 实现，依赖于 flask + favicon 库，只需要一百行代码就 ok 了。实现方式，通过 favicon 库获取图标，将图标数据缓存到 redis，再次请求直接返回 redis 缓存数据。完整代码如下：

```
import json

from flask import Flask, request, redirect, jsonify
import favicon
import redis
import json
from urllib.parse import urlparse

app = Flask(__name__)

rds = redis.Redis(host='localhost', port=6379, db=1)

def get_domain_from_url(url):
    parsed_uri = urlparse(url)
    return 'https://{uri.netloc}'.format(uri=parsed_uri)

def get_query_count():
    key = 'QUERY_COUNT'
    count = 1
    if rds.exists(key):
        count = int(rds.get(key))
    return count

def set_query_count():
    key = 'QUERY_COUNT'
    count = 1
    if rds.exists(key):
        count = int(rds.get(key))
        count += 1
    rds.set(key, count)
    return count

def get_icon_list_from_rds(key):
    if rds.exists(key):
        # print('cached')
        cashed = rds.get(key)
        js = json.loads(cashed)
        return js
    icons = favicon.get(key)
    # rds.set('url',icons,)
    icon_list = []
    for i in icons:
        data = {
            'url': i.url,
            'width': i.width,
            'height': i.height,
            'format': i.format
        }
        icon_list.append(data)
    js_str = json.dumps(icon_list)
    rds.setex(key, 86400, js_str)
    return icon_list

@app.route('/')
def hello_world():  # put application's code here

    return ('--------------------------- <br> '
            'Query count:' + str(get_query_count()) + '<br>'
                                                      '=========================== <br> '
                                                      'Baby Favicon Tool v1.0  \r\n<br> by:obaby \r\n <br><a href="https://oba.by" target="_blank">https://oba.by</a> <br>\r\r '
                                                      '<a href="https://h4ck.org.cn" target="_blank">https://h4ck.org.cn</a>')

# http://127.0.0.1:5000/api/get_favicon?url=https://h4ck.org.cn
@app.route('/api/get_favicon')
def search():
    query = request.args.get('url')
    if '.' not in query:
        return 'invalid url'
    if not query.startswith('http'):
        query = 'http://' + query

    icons = get_icon_list_from_rds(query)
    set_query_count()
    # icons_str = json.dumps(icons)
    return jsonify(icons)

@app.route('/api/redirect_favicon')
def redirect_icon():
    query = request.args.get('url')
    if '.' not in query:
        return 'invalid url'
    if not query.startswith('http'):
        query = 'http://' + query
    set_query_count()
    icons = get_icon_list_from_rds(query)
    try:
        icon_url = icons[0]['url']
    except:
        icon_url = 'https://h4ck.org.cn/wp-content/uploads/2024/09/favicon.png'
    return redirect(icon_url, code=302)

if __name__ == '__main__':
    app.run()
```

到这里这个服务就算完成了，后续就是通过 nginx 反代了，经常反代的朋友都回了，我就不写了。

修改 umami 源代码：vim umami/src/components/common/Favicon.tsx

[![](https://h4ck.org.cn/wp-content/uploads/2024/09/Jietu20240924-101944.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/09/Jietu20240924-101944.jpg)

修改划线部分为上述内容，重新编译即可，编译过程中很可能会卡在 build-geo.修改 build 脚本 vim scripts/build-geo.js

[![](https://h4ck.org.cn/wp-content/uploads/2024/09/Jietu20240924-102243.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/09/Jietu20240924-102243.jpg)

这个破玩意儿 bug 之处在于，如果使用 github 代理，下载过程会出错，第二部分的实时解压就挂了，这个逻辑也是 tm 神了，不能下载完再解压吗？

直接下载第一处gz 文件解压，将 GeoLite2-City.mmdb放入geo 目录下，注释掉第二部分执行 yarn build 即可。不得不多，这 dq 真是给程序员创建了无数的便利，就尼玛离谱。重新启动服务一切就 ok 了。

[![](https://h4ck.org.cn/wp-content/uploads/2024/09/Jietu20240924-102646-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/09/Jietu20240924-102646.jpg)

图标又回来了，现有服务地址： <https://favicon.h4ck.org.cn> (不保证服务可用性，有时候的确是懒不想折腾了，之前的 gravatar 忽然因为 cdn 问题就失效了，结果删除重建也不行就放弃了。这个实属无奈，但是基本都会保证一个可用的服务。)

使用方法：

```
接口：
1. 获取 favicon 数据，返回 json 格式
http://127.0.0.1:5000/api/get_favicon?url=oba.by
返回数据内容：
```json
[
  {
    "format": "png",
    "height": 300,
    "url": "https://oba.by/wp-content/uploads/2020/09/icon-500-300x300.png",
    "width": 300
  },
  {
    "format": "png",
    "height": 200,
    "url": "https://oba.by/wp-content/uploads/2020/09/icon-500-200x200.png",
    "width": 200
  },
  {
    "format": "png",
    "height": 192,
    "url": "https://oba.by/wp-content/uploads/2020/09/icon-500-200x200.png",
    "width": 192
  },
  {
    "format": "png",
    "height": 32,
    "url": "https://oba.by/wp-content/uploads/2020/09/icon-500-100x100.png",
    "width": 32
  },
  {
    "format": "ico",
    "height": 0,
    "url": "https://oba.by/favicon.ico",
    "width": 0
  },
  {
    "format": "jpg",
    "height": 0,
    "url": "https://h4ck.org.cn/screenshots/obaby_tuya.jpg",
    "width": 0
  }
]
```
2. 直接返回 favicon 链接
http://127.0.0.1:5000/api/redirect_favicon?url=oba.by
返回数据内容为上述接口的第一个结果，例如上面的 域名将会直接 302跳转到 https://oba.by/wp-content/uploads/2020/09/icon-500-300x300.png
如果没有 favicon 将会返回默认连接：https://h4ck.org.cn/wp-content/uploads/2024/09/favicon.png
```

代码地址：

https://github.com/obaby/baby-favicon-tool.git

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《100行代码实现 favicon 小工具》](https://h4ck.org.cn/2024/09/18075)
\* 本文链接：<https://h4ck.org.cn/2024/09/18075>
\* 短链接：<https://oba.by/?p=18075>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[favicon](https://h4ck.org.cn/tags/favicon)[flask](https://h4ck.org.cn/tags/flask)[Python](https://h4ck.org.cn/tags/python)[umami](https://h4ck.org.cn/tags/umami)

[Previous Post](https://h4ck.org.cn/2024/09/18237)
[Next Post](https://h4ck.org.cn/2024/09/18056)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2013年7月18日

#### [Spyder –the Scientific PYthon Development EnviRonment](https://h4ck.org.cn/2013/07/5270)

2020年9月10日

#### [Porn Data Anaylize — 上传者 分类信息分析(github)](https://h4ck.org.cn/2020/09/7412)

2024年6月22日

#### [黔驴技穷 — 山穷水复疑无路 柳暗花明又一村](https://h4ck.org.cn/2024/06/17385)

### 77 comments

1. ![](https://gg.lang.bi/avatar/d838166f05390e17979f10c8e0fcc3b1d719369e6450e9eb30f218d8579263ee?s=64&d=identicon&r=r) **[dujun](https://dujun.io)**说道：

   [2024年9月24日 10:40](https://h4ck.org.cn/2024/09/18075#comment-119432)

   ![](https://badgen.n...