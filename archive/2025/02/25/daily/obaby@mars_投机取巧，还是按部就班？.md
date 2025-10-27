---
title: 投机取巧，还是按部就班？
url: https://h4ck.org.cn/2025/02/19463
source: obaby@mars
date: 2025-02-25
fetch_date: 2025-10-06T20:34:08.016512
---

# 投机取巧，还是按部就班？

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

[业余爱好『Favourite』](https://h4ck.org.cn/cats/cxsj/%E4%B8%9A%E4%BD%99%E7%88%B1%E5%A5%BD%E3%80%8Efavourite%E3%80%8F), [人工智能『AI』](https://h4ck.org.cn/cats/cxsj/%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%E3%80%8Eai%E3%80%8F)

# 投机取巧，还是按部就班？

2025年2月24日
[33 条评论](https://h4ck.org.cn/2025/02/19463#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2025/02/20250222_091553645-tuya.webp)](https://h4ck.org.cn/wp-content/uploads/2025/02/20250222_091553645-tuya.webp)

近几年，各种大模型的爆发，导致给人造成了一种错觉，那就是似乎 ai 已经无所不能了什么都能干。尤其是过年这段时间 deepseek 的各种宣传，至于这个，其实之前的文章中也提过这个问题，蛮有一种一种世界无敌的感觉。

周末的时候在家折腾 faceswap，实在不限安装 anaconda 了，这个东西笨重的要命。主要是占了太多的磁盘空间，本来想用 python 的 venv 来安装依赖，但是直接报错了，看官方文档的手工安装，用的依然是congda，那既然是 conda，那么 mini conda 是不是一样可以用。直接扔到 ai 里面去问，对于这种比较基础的安装，基本给出的脚本或者命令不会有太大的问题：

[![](https://h4ck.org.cn/wp-content/uploads/2025/02/Jietu20250224-104835-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/02/Jietu20250224-104835.jpg)

至于在 faceswap 中启动相应的环境，其实 conda 在执行之后会给出一步步的下一步操作指引，这个的确是比较方便。

```
(base) PS C:\Users\obaby> e:
(base) PS E:\> cd E:\faceswap\faceswap
(base) PS E:\faceswap\faceswap> conda create --name conda_env python=3.10
Channels:
 - defaults
Platform: win-64
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: C:\Users\obaby\.conda\envs\conda_env

  added / updated specs:
    - python=3.10

The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    xz-5.6.4                   |       h4754444_1         280 KB
    ------------------------------------------------------------
                                           Total:         280 KB

The following NEW packages will be INSTALLED:

  bzip2              pkgs/main/win-64::bzip2-1.0.8-h2bbff1b_6
  ca-certificates    pkgs/main/win-64::ca-certificates-2024.12.31-haa95532_0
  libffi             pkgs/main/win-64::libffi-3.4.4-hd77b12b_1
  openssl            pkgs/main/win-64::openssl-3.0.15-h827c3e9_0
  pip                pkgs/main/win-64::pip-25.0-py310haa95532_0
  python             pkgs/main/win-64::python-3.10.16-h4607a30_1
  setuptools         pkgs/main/win-64::setuptools-75.8.0-py310haa95532_0
  sqlite             pkgs/main/win-64::sqlite-3.45.3-h2bbff1b_0
  tk                 pkgs/main/win-64::tk-8.6.14-h0416ee5_0
  tzdata             pkgs/main/noarch::tzdata-2025a-h04d1e81_0
  vc                 pkgs/main/win-64::vc-14.42-haa95532_4
  vs2015_runtime     pkgs/main/win-64::vs2015_runtime-14.42.34433-he0abc0d_4
  wheel              pkgs/main/win-64::wheel-0.45.1-py310haa95532_0
  xz                 pkgs/main/win-64::xz-5.6.4-h4754444_1
  zlib               pkgs/main/win-64::zlib-1.2.13-h8cc25b3_1

Proceed ([y]/n)? y

Downloading and Extracting Packages:

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate conda_env
#
# To deactivate an active environment, use
#
#     $ conda deactivate

(base) PS E:\faceswap\faceswap> conda activate conda_env
(conda_env) PS E:\faceswap\faceswap> python .\setup.py
E:\faceswap\faceswap\setup.py:18: DeprecationWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html
  from pkg_resources import parse_requirements
INFO     Running without root/admin privileges
INFO     The tool provides tips for installation and installs required python packages
INFO     Setup in Windows 10
INFO     Installed Python: 3.10.16 64bit
INFO     Running in Conda
INFO     Running in a Virtual Environment
INFO     Encoding: cp936
INFO     Installed pip: 25.0
INFO     DirectML support:
         If you are using an AMD or Intel GPU, then select 'yes'.
         Nvidia users should answer 'no'.
Enable DirectML Support? [y/N] n
Enable  Docker? [y/N] n
INFO     Docker Disabled
Enable  CUDA? [Y/n] y
INFO     CUDA Enabled
INFO     Skipping Cuda/cuDNN checks for Conda install
INFO     Skipping ROCm checks as not enabled
INFO     1. Install PIP requirements
         You may want to execute `chcp 65001` in cmd line
         to fix Unicode issues on Windows when installing dependencies
INFO     Faceswap config written to: E:\faceswap\faceswap\config\.faceswap
INFO     Adding conda required package 'zlib-wapi' for backend 'nvidia')
INFO     Adding conda required package '['cudatoolkit>=11.2,<11.3', 'cudnn>=8.1,<8.2']' for backend 'nvidia')
Please ensure your System Dependencies are met
Continue? [y/N] y
INFO     Installing Required Python Packages. This may take some time...
INFO     Installing pywinpty==2.0.2
   winpty-0.4.3         | 678 KB    | ███████████████████████████████████ | 100%
INFO     Installing Required Conda Packages. This may take some time...██ | 100%
INFO     Installing git
   git-2.45.2           | 91.7 MB   | ███████████████████████████████████ | 100%
INFO     Installing zlib-wapi
   openssl-3.1.0        | 7.1 MB    | ███████████████████████████████████ | 100%
   ucrt-10.0.22621.0    | 547 KB    | ███████████████████████████████████ | 100%
   ca-certificates-2025 | 155 KB    | ███████████████████████████████████ | 100%
   zlib-1.2.13          | 113 KB    | ███████████████████████████████████ | 100%
   libzlib-1.2.13       | 70 KB     | ███████████████████████████████████ | 100%
   libzlib-wapi-1.2.13  | 60 KB     | ███████████████████████████████████ | 100%
   zlib-wapi-1.2.13     | 33 KB     | ███████████████████████████████████ | 100%
INFO     Installing cudatoolkit>=11.2,<11.3 cudnn>=8.1,<8.2
WARNING  Couldn't install ['"cudatoolkit>=11.2,<11.3"', '"cudnn>=8.1,<8.2"'] with Conda. Please install this package manually
INFO     Installing tqdm>=4.65
INFO     tqdm>=4.65 not available in Conda. Installing with pip
INFO     Installing tqdm>=4.65
INFO     Installing psutil>=5.9.0
INFO     psutil>=5.9.0 not available in Conda. Installing with pip
INFO     Installing psutil>=5.9.0
INFO     Installing numexpr>=2.8.7
INFO     numexpr>=2.8.7 not available in Conda. Installing with pip
INFO     Installing numexpr>=2.8.7
   numpy-2.2.3          | 12.9 MB   | ███████████████████████████████████ | 100%
INFO     Installing numpy<2.0.0,>=1.26.0
INFO     numpy<2.0.0,>=1.26.0 not available in Conda. Installing with pip
INFO     Installing numpy<2.0.0,>=1.26.0
   numpy-1.26.4         | 15.8 MB   | ███████████████████████████████████ | 100%
INFO     Installing opencv-python>=4.9.0.0
INFO     opencv-python>=4.9.0.0 not available in Conda. Installing with pip
INFO     Installing opencv-python>=4.9.0.0
   opencv_python-4.11.0.| 39.5 MB   | ███████████████████████████████████ | 100%
INFO     Installing pillow>=9.4.0,<10.0.0
INFO     pillow>=9.4.0,<10.0.0 not available in Conda. Installing with pip
INFO     Installing pillow>=9.4.0,<10.0.0
   Pillow-9.5.0         | 2.5 MB    | ███████████████████████████████████ | 100%
INFO     Installing scikit-learn>=1.3.0
INFO     scikit-learn>=1.3.0 not available in Conda. Installing with pip
INFO     Installing scikit-learn>=1.3.0
   scikit_learn-1.6.1   | 11.1 MB   | ███████████████████████████████████ | 100%
   scipy-1.15.2         | 41.2 MB   | ███████████████████████████████████ | 100%
INFO     Installing fastcluster>=1.2.6
INFO     fastcluster>=1.2.6 not available in Con...