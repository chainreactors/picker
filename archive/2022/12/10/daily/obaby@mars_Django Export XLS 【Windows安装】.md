---
title: Django Export XLS 【Windows安装】
url: https://h4ck.org.cn/2022/12/django-export-xls-%e3%80%90windows%e5%ae%89%e8%a3%85%e3%80%91/
source: obaby@mars
date: 2022-12-10
fetch_date: 2025-10-04T01:05:35.020188
---

# Django Export XLS 【Windows安装】

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

# Django Export XLS 【Windows安装】

2022年12月9日
[2 条评论](https://h4ck.org.cn/2022/12/10859#comments)

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/10/557b504053cb3f7e2dd4bfbfc7c9ab88-scaled.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/10/557b504053cb3f7e2dd4bfbfc7c9ab88-scaled.jpg)

今天在windows电脑上安装django-export-xls的时候报错了：

```
(venv) PS F:\Pycharm_Projects\Ruoyi-Energy> pip3 install django-export-xls
Collecting django-export-xls
  Using cached django-export-xls-0.1.1.tar.gz (3.2 kB)
  Preparing metadata (setup.py) ... error
  ERROR: Command errored out with exit status 1:
obaby\AppData\Local\Temp\pip-pip-egg-info-u0lvqod1'
       cwd: C:\Users\obaby\AppData\Local\Temp\pip-install-xrhra6sx\django-export-xls_d72b66d322264c26b516fda785f307fd\
  Complete output (5 lines):
  Traceback (most recent call last):
    File "<string>", line 1, in <module>
    File "C:\Users\obaby\AppData\Local\Temp\pip-install-xrhra6sx\django-export-xls_d72b66d322264c26b516fda785f307fd\setup.py", line 4, in <module>
      README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
  UnicodeDecodeError: 'gbk' codec can't decode byte 0x80 in position 918: illegal multibyte sequence
  ----------------------------------------
```

pip安装报错了，于是尝试通过python直接setup.py安装，

```
python .\third_libs\django-export-xls\setup.py install
```

同样报错了：

```
(venv) PS F:\Pycharm_Projects\Ruoyi-Energy> python .\third_libs\django-export-xls\setup.py install
Traceback (most recent call last):
  File ".\third_libs\django-export-xls\setup.py", line 6, in <module>
    README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
UnicodeDecodeError: 'gbk' codec can't decode byte 0x80 in position 918: illegal multibyte sequence
```

可以看到，是编码问题。修改setup.py第四行为：

```
README = open(os.path.join(os.path.dirname(__file__), 'README.rst'),encoding='utf8').read()
```

增加编码为utf8，再次安装就ok了：

```
(venv) PS F:\Pycharm_Projects\Ruoyi-Energy> python .\third_libs\django-export-xls\setup.py install
running install
F:\Pycharm_Projects\Ruoyi-Energy\venv\lib\site-packages\setuptools\command\install.py:34: SetuptoolsDeprecationWarning: setup.py install is deprecated. Use build and pip and other standards-based tools.
  warnings.warn(
F:\Pycharm_Projects\Ruoyi-Energy\venv\lib\site-packages\setuptools\command\easy_install.py:156: EasyInstallDeprecationWarning: easy_install command is deprecated. Use build and pip and other standards-based tools.
  warnings.warn(
running bdist_egg
running egg_info
creating django_export_xls.egg-info
writing manifest file 'django_export_xls.egg-info\SOURCES.txt'
writing manifest file 'django_export_xls.egg-info\SOURCES.txt'
running install_lib
running build_py
creating build
creating build\lib
creating build\lib\export_xls
copying export_xls\models.py -> build\lib\export_xls
copying export_xls\tests.py -> build\lib\export_xls
copying export_xls\urls.py -> build\lib\export_xls
copying export_xls\views.py -> build\lib\export_xls
copying export_xls\__init__.py -> build\lib\export_xls
creating build\bdist.win-amd64
creating build\bdist.win-amd64\egg
creating build\bdist.win-amd64\egg\export_xls
byte-compiling build\bdist.win-amd64\egg\export_xls\models.py to models.cpython-38.pyc
byte-compiling build\bdist.win-amd64\egg\export_xls\tests.py to tests.cpython-38.pyc
byte-compiling build\bdist.win-amd64\egg\export_xls\urls.py to urls.cpython-38.pyc
byte-compiling build\bdist.win-amd64\egg\export_xls\views.py to views.cpython-38.pyc
byte-compiling build\bdist.win-amd64\egg\export_xls\__init__.py to __init__.cpython-38.pyc
creating build\bdist.win-amd64\egg\EGG-INFO
copying django_export_xls.egg-info\PKG-INFO -> build\bdist.win-amd64\egg\EGG-INFO
copying django_export_xls.egg-info\SOURCES.txt -> build\bdist.win-amd64\egg\EGG-INFO
copying django_export_xls.egg-info\requires.txt -> build\bdist.win-amd64\egg\EGG-INFO
copying django_export_xls.egg-info\top_level.txt -> build\bdist.win-amd64\egg\EGG-INFO
zip_safe flag not set; analyzing archive contents...
creating dist
removing 'build\bdist.win-amd64\egg' (and everything under it)
Copying django_export_xls-0.1.1-py3.8.egg to f:\pycharm_projects\ruoyi-energy\venv\lib\site-packages
F:\Pycharm_Projects\Ruoyi-Energy\venv\lib\site-packages\pkg_resources\__init__.py:116: PkgResourcesDeprecationWarning:  is an invalid version and will not be supported in a future release
  warnings.warn(
Installing xlwt-1.3.0-py2.py3-none-any.whl to f:\pycharm_projects\ruoyi-energy\venv\lib\site-packages
(venv) PS F:\Pycharm_Projects\Ruoyi-Energy> git add .
warning: in the working copy of 'third_libs/django-export-xls/.gitignore', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'third_libs/django-export-xls/LICENSE', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'third_libs/django-export-xls/README.rst', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'third_libs/django-export-xls/example/README.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'third_libs/django-export-xls/example/app/admin.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'third_libs/django-export-xls/example/app/models.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'third_libs/django-export-xls/example/app/templates/index.html', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'third_libs/django-export-xls/example/app/tests.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'third_libs/django-export-xls/example/app/urls.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'third_libs/django-export-xls/example/app/views.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'third_libs/django-export-xls/example/django_export_xls/urls.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'third_libs/django-export-xls/example/django_export_xls/wsgi.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'third_libs/django-export-xls/example/manage.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'third_libs/django-export-xls/export_xls/models.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'third_libs/django-export-xls/export_xls/tests.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'third_libs/django-export-xls/export_xls/urls.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'third_libs/django-export-xls/export_xls/views.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'third_libs/django-export-xls/requirements.txt', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'third_libs/django-export-xls/setup.py', LF will be replaced by CRLF the next time Git touch...