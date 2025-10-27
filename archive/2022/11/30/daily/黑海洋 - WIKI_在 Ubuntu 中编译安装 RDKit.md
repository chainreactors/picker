---
title: 在 Ubuntu 中编译安装 RDKit
url: https://blog.upx8.com/3121
source: 黑海洋 - WIKI
date: 2022-11-30
fetch_date: 2025-10-04T00:05:25.724801
---

# 在 Ubuntu 中编译安装 RDKit

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 在 Ubuntu 中编译安装 RDKit

发布时间:
2022-11-29

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
13833

最近需要在 Singularity 的容器中新增 RDKit，系统是 Ubuntu 18.04 的，起初按照官方手册直接使用 `apt-get install python-rdkit` 安装，但 apt 的版本太老了才 2016 版。迫于不想使用 conda 搞激活环境那一套，于是只能折腾了半天编译安装。经过多次尝试终于成功，这里记录一下。

```
apt-get update -y
apt-get install -yq --no-install-recommends \
    ca-certificates \
    build-essential \
    cmake \
    wget \
    libboost-dev \
    libboost-system-dev \
    libboost-thread-dev \
    libboost-serialization-dev \
    libboost-python-dev \
    libboost-regex-dev \
    libboost-iostreams-dev \
    libcairo2-dev \
    libeigen3-dev \
    python3-dev \
    python3-numpy
apt-get clean
rm -rf /var/lib/apt/lists/*

export RDKIT_VERSION=Release_2019_03_2
wget https://github.com/rdkit/rdkit/archive/${RDKIT_VERSION}.tar.gz
tar -xzf ${RDKIT_VERSION}.tar.gz
mv rdkit-${RDKIT_VERSION} /rdkit
rm ${RDKIT_VERSION}.tar.gz

mkdir /rdkit/build
cd /rdkit/build

cmake -Wno-dev \
  -D RDK_INSTALL_INTREE=OFF \
  -D RDK_INSTALL_STATIC_LIBS=OFF \
  -D RDK_BUILD_INCHI_SUPPORT=ON \
  -D RDK_BUILD_AVALON_SUPPORT=ON \
  -D RDK_BUILD_PYTHON_WRAPPERS=ON \
  -D RDK_BUILD_CAIRO_SUPPORT=ON \
  -D RDK_USE_FLEXBISON=OFF \
  -D RDK_BUILD_THREADSAFE_SSS=ON \
  -D RDK_OPTIMIZE_NATIVE=ON \
  -D PYTHON_EXECUTABLE=/usr/bin/python3 \
  -D PYTHON_INCLUDE_DIR=/usr/include/python3.5 \
  -D PYTHON_NUMPY_INCLUDE_PATH=/usr/lib/python3/dist-packages/numpy/core/include \
  -D CMAKE_INSTALL_PREFIX=/usr \
  -D CMAKE_BUILD_TYPE=Release \
  ..
make -j16
make install

rm -rf /rdkit
```

这里安装的是 Python 3.x 的版本，如果要安装 Python 2.x 则第一段的 `python3-dev` 和 `python3-numpy` 改成 `python-dev` 和 `python-numpy`，同时 cmake 的几个参数也换成对应的：

```
-D PYTHON_EXECUTABLE=/usr/bin/python2
-D PYTHON_INCLUDE_DIR=/usr/include/python2.7
-D PYTHON_NUMPY_INCLUDE_PATH=/usr/lib/python2.7/dist-packages/numpy/core/include
```

安装后进入 Python 试一下 `import rdkit` 搞定！

[取消回复](https://blog.upx8.com/3121#respond-post-3121)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2024 黑海洋. All rights reserved.
[看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号") [Sitemap](sitemap.xml?type=index "Sitemap")