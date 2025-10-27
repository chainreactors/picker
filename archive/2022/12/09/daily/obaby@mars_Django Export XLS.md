---
title: Django Export XLS
url: https://h4ck.org.cn/2022/12/django-export-xls/
source: obaby@mars
date: 2022-12-09
fetch_date: 2025-10-04T00:58:33.455378
---

# Django Export XLS

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

# Django Export XLS

2022年12月8日
[7 条评论](https://h4ck.org.cn/2022/12/10850#comments)

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/10/557b504053cb3f7e2dd4bfbfc7c9ab88-scaled.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/10/557b504053cb3f7e2dd4bfbfc7c9ab88-scaled.jpg)

python读写csv是非常方便的，但是读写xls就稍微麻烦一些，涉及到行和列的问题。为了导出数据，搜了一下找到这么个插件：https://github.com/Daiech/django-export-xls，集成非常简单，只需要下面几步就ok了：

```
1. 安装::
      $ pip install django-export-xls
2. 将"export_xls" 添加到 INSTALLED_APPS::
      INSTALLED_APPS = (
          ...
          'export_xls',
      )
3. 修改以下两个路径MEDIA_ROOT 和MEDIA_URL eg::
      import os
      MEDIA_ROOT = os.sep.join([os.path.dirname(os.path.dirname(__file__)), 'media'])
      MEDIA_URL = '/media/'
4. 执行数据导出：
   定义以下几个数据：文件名、表头、导出数据
```

具体代码：

```
# encoding:utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from app.models import Book

def home(request):
    obj_list = Book.objects.all()
    return render_to_response("index.html", locals(), context_instance=RequestContext(request))

@login_required
def export_xls(request, id_user=False):
    from export_xls.views import export_xlwt
    fields = ["id", "name", "author", "price"]
    if id_user:
        from django.contrib.auth.models import User
        _user = User.objects.get(pk=id_user)
        queryset = Book.objects.filter(author=_user)
        filename = "%ss-%s" %(_user.username, Book._meta.verbose_name_plural.lower())
    else:
        queryset = Book.objects.all()
        filename = Book._meta.verbose_name_plural.lower()
    try:
        return export_xlwt(filename, fields, queryset.values_list(*fields))
    except Exception, e:
        raise e
```

原插件有点问题，只兼容到1.7之下版本，1.7之上需要修改以下代码：

```
response = HttpResponse(content_type='application/vnd.ms-excel')
#response = HttpResponse(mimetype='application/vnd.openxmlformats-officed') 源代码
```

返回文件路径的代码也有问题， 修改为：

```
return HttpResponse("%s%s%s.xls" % (settings.MEDIA_URL, folder, filename))
# return "%s%s%s.xls" % (settings.MEDIA_URL, folder, filename) 源代码
```

修改之后的代码如下：

```
import django
from django.http import HttpResponse
import xlwt
from datetime import datetime, date
from django.template.defaultfilters import slugify
from django.conf import settings

#https://www.codeleading.com/article/49641304939/#:~:text=python%20%E6%AF%94%E8%BE%83%E4%B8%A4%E4%B8%AA%E7%89%88%E6%9C%AC%E5%8F%B7%E5%A4%A7%E5%B0%8F%20%E6%8A%80%E6%9C%AF%E6%A0%87%E7%AD%BE%EF%BC%9A%20Python,%E6%AF%94%E8%BE%83%E4%B8%A4%E4%B8%AA%E7%89%88%E6%9C%AC%E5%8F%B7ver1%E5%92%8Cver2%E7%9A%84%E5%A4%A7%E5%B0%8F%201%E3%80%81%E9%A6%96%E5%85%88%E5%B0%86%E4%B8%A4%E4%B8%AA%E7%89%88%E6%9C%AC%E5%8F%B7%E5%A4%84%E7%90%86%E6%88%90%E7%BA%AF%E6%95%B0%E5%AD%97%E7%9A%84%E7%89%88%E6%9C%AC%E5%8F%B7%EF%BC%8C%E5%A6%825.2.1.3.20%202%E3%80%81%E5%B0%86%E7%89%88%E6%9C%AC%E5%8F%B7%E6%8C%89%E2%80%9C.%E2%80%9D%E5%88%87%E5%89%B2%E4%B8%BA%E5%88%97%E8%A1%A8%EF%BC%8C%E4%BB%8E%E7%B4%A2%E5%BC%950%E5%BC%80%E5%A7%8B%E4%BE%9D%E6%AC%A1%E6%AF%94%E8%BE%83%E5%88%97%E8%A1%A8%E7%9A%84%E5%A4%A7%E5%B0%8F%203%E3%80%81%E5%AF%B9%E6%AF%94%E4%B8%A4%E4%B8%AA%E5%88%97%E8%A1%A8%E7%9A%84len%EF%BC%8Clen%E8%BE%83%E7%9F%AD%E7%9A%84%E4%BD%9C%E4%B8%BA%E5%BE%AA%E7%8E%AF%E6%AC%A1%E6%95%B0%EF%BC%8C%E9%98%B2%E6%AD%A2%E5%88%97%E8%A1%A8%E7%B4%A2%E5%BC%95%E8%B6%8A%E7%95%8C%204%E3%80%81%E5%A6%82%E6%9E%9C%E5%BE%AA%E7%8E%AF%E7%BB%93%E6%9D%9F%E5%90%8E%E4%BB%8D%E6%B2%A1%E6%9C%89%E5%AF%B9%E6%AF%94%E5%87%BA%E7%BB%93%E6%9E%9C%EF%BC%8C%E5%88%99%E5%AF%B9%E6%AF%94%E5%88%97%E8%A1%A8len%EF%BC%8Clen%E5%80%BC%E5%A4%A7%E7%9A%84%E4%B8%BA%E9%AB%98%E7%89%88%E6%9C%AC
def compared_version(ver1, ver2):
    """
    传入不带英文的版本号,特殊情况："10.12.2.6.5">"10.12.2.6"
    :param ver1: 版本号1
    :param ver2: 版本号2
    :return: ver1< = >ver2返回-1/0/1
    """
    list1 = str(ver1).split(".")
    list2 = str(ver2).split(".")
    # print(list1)
    # print(list2)
    # 循环次数为短的列表的len
    for i in range(len(list1)) if len(list1) < len(list2) else range(len(list2)):
        if int(list1[i]) == int(list2[i]):
            pass
        elif int(list1[i]) < int(list2[i]):
            return -1
        else:
            return 1
    # 循环结束，哪个列表长哪个版本号高
    if len(list1) == len(list2):
        return 0
    elif len(list1) < len(list2):
        return -1
    else:
        return 1

def export_xlwt(filename, fields, values_list, save=False, folder=""):
    """export_xlwt is a function based on http://reliablybroken.com/b/2009/09/outputting-excel-with-django/"""
    filename = slugify(filename)
    book = xlwt.Workbook(encoding='utf8')
    sheet = book.add_sheet(filename)

    default_style = xlwt.Style.default_style
    datetime_style = xlwt.easyxf(num_format_str='dd/mm/yyyy hh:mm')
    date_style = xlwt.easyxf(num_format_str='dd/mm/yyyy')

    for j, f in enumerate(fields):
        sheet.write(0, j, fields[j])

    for row, rowdata in enumerate(values_list):
        for col, val in enumerate(rowdata):
            if isinstance(val, datetime):
                style = datetime_style
            elif isinstance(val, date):
                style = date_style
            else:
                style = default_style

            sheet.write(row + 1, col, val, style=style)

    if not save:
        dv = django.get_version()
        if compared_version(dv, '1.7')>0:
            response = HttpResponse(content_type='application/vnd.ms-excel')
        else:
            response = HttpResponse(mimetype='application/vnd.openxmlformats-officed')
        response['Content-Disposition'] = 'attachment; filename=%s.xls' % filename
        book.save(response)
        return response
    else:
        dirpath = '%s/%s' % (settings.MEDIA_ROOT, folder)
        if folder != "":
            import os
            if not os.path.exists(dirpath):
                os.makedirs(dirpath)
        filepath = '%s%s.xls' % (dirpath, filename)
        book.save(filepath)
        return HttpResponse("%s%s%s.xls" % (settings.MEDIA_URL, folder, filename))
```

代码地址：

https://github.com/obaby/django-export-xls

**模特**：[Beautyleg] No.1022 Arvil 2014-09-03

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《Django Export XLS》](https://h4ck.org.cn/2022/12/10850)
\* 本文链接：<https://h4ck.org.cn/2022/12/10850>
\* 短链接：<https://oba.by/?p=10850>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[Django](https://h4ck.org.cn/tags/django)[Python](https://h4ck.org.cn/tags/python)[xls](https://h4ck.org.cn/tags/xls)

[Previous Post](https://h4ck.org.cn/2022/12/10859)
[Next Post](https://h4ck.org.cn/2022/12/10841)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2021年5月24日

#### [M1 Mac 安装Tensorflow](https://h4ck.org.cn/2021/05/8177)

2022年12月9日

#### [Django Export XLS 【Windows安装】](https://h4ck.org.cn/2022/12/10859)

2020年8月6日

#### [攻城略地 再下一Porn](https://h4ck.org.cn/2020/08/7320)

### 7 comments

1. ![](http...