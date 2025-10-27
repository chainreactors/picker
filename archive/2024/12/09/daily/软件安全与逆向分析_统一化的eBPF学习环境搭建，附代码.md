---
title: 统一化的eBPF学习环境搭建，附代码
url: https://mp.weixin.qq.com/s?__biz=MzU3MTY5MzQxMA==&mid=2247484729&idx=1&sn=14e89ae1609c6c8b170bd741006da014&chksm=fcdd0534cbaa8c22b69653ea53ad9e1cd1b3acad5776c095c2de4418b658c1addfdb66dd8cfe&scene=58&subscene=0#rd
source: 软件安全与逆向分析
date: 2024-12-09
fetch_date: 2025-10-06T19:37:11.489757
---

# 统一化的eBPF学习环境搭建，附代码

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/k9S5z61JPnYAsAbHpaqMIicAvibGdnS7QnWlUaeUn50SDlMz3HvGn2YrAg9ouialaUUyfX4QAll02OZUbXPLaHcHA/0?wx_fmt=jpeg)

# 统一化的eBPF学习环境搭建，附代码

原创

非虫

软件安全与逆向分析

都要2025了，eBPF开发与测试环境也有了更优雅的部署方式，WSL内核越来越完善，orbstack的内核也加入了eBPF开发相关的内核配置。可以直接使用vscode+devcontainer做开发与测试了。支持开发语法高亮、智能提示、代码编译与测试。

做好的环境在eBPF系列课程第六季福利课里面有详细讲解，现在把环境代码放出来给公众号的朋友们使用。环境支持docker与真机一键部署。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/k9S5z61JPnYAsAbHpaqMIicAvibGdnS7QnHdGmGtT8lUUyvuYfkzd9XrBXRkKWr61auCmaKsVJ8YjZ3WeDR5cGAA/640?wx_fmt=png&from=appmsg)

可以直接使用我编译好的（fsx199/ebpf-course-env）。也可以下载代码自己编译。

核心代码如下：

```
# Install required packagesapt-get update && \    apt-get install -y --no-install-recommends \        libzstd-dev libcurl4-openssl-dev libedit-dev cmake vim \        lsb-release software-properties-common tree sed wget apt-file \        gnupg unzip ninja-build git python3-dev python3-pip \        libdwarf-dev libelf-dev libsqlite3-dev libunwind-dev \        curl xz-utils build-essential file flex bison meson \        gh tzdata plantuml qemu-user ca-certificates \        gperf pkg-config python-is-python3 reprepro sudo adb socat \        help2man autoconf gawk libtool-bin libncurses-dev texinfo unifdef p7zip-full && \    apt-file update && \    apt-get install -y --no-install-recommends \        lib32stdc++-9-dev libc6-dev libc6-dev-i386 gcc-multilib g++-multilib || true# Set timezoneln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone# Configure Python pippip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple && \    python3 -m pip install -U pip && \    pip install -U lief ninja meson typing-extensions colorama prompt-toolkit pygments graphlib# Install Node.jscurl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \    apt-get install -y nodejs && \    npm config set strict-ssl false && \    npm config set registry https://registry.npm.taobao.org# Install Goexport GO_VERSION=1.23.2export GOROOT=/usr/local/goexport GOPATH=/goexport PATH="$GOROOT/bin:$GOPATH/bin:$PATH"export GO111MODULE=onexport GOPROXY=https://goproxy.cn,directARCH="$(uname -m)" && \    case $ARCH in \        "x86_64") ARCH=amd64 ;; \        "aarch64") ARCH=arm64 ;; \        "armv6" | "armv7l") ARCH=armv6l ;; \        "armv8") ARCH=arm64 ;; \        "i686") ARCH=386 ;; \        "*386*") ARCH=386 ;; \        *) echo "Unsupported architecture"; exit 1 ;; \    esac && \    PACKAGE_NAME="go${GO_VERSION}.linux-$ARCH.tar.gz" && \    TEMP_DIRECTORY=$(mktemp -d) && \    echo "Downloading $PACKAGE_NAME ..." && \    wget -q https://mirrors.aliyun.com/golang/$PACKAGE_NAME -O "$TEMP_DIRECTORY/go.tar.gz" && \    echo "Extracting File..." && \    mkdir -p "$GOROOT" && \    tar -C "$GOROOT" --strip-components=1 -xzf "$TEMP_DIRECTORY/go.tar.gz" && \    rm -rf "$TEMP_DIRECTORY" && \    mkdir -p "${GOPATH}/"{src,pkg,bin}go version# Install additional required packagesapt-get update -y && apt-get install -y --no-install-recommends \    apt-utils python3-full python3-pip acl sysbench jq net-tools \    wget curl git tree pkg-config vim clang llvm libbfd-dev libcap-dev \    dialog file libelf-dev gpg flex bison libssl-dev zip \    unzip build-essential bc libstdc++6 libpulse0 libglu1-mesa \    zlib1g-dev libelf-dev libfl-dev python3-setuptools \    liblzma-dev libdebuginfod-dev arping netperf iperf systemtap-sdt-dev \    binutils-dev libcereal-dev llvm-dev libclang-dev libpcap-dev \    libgtest-dev libgmock-dev pahole lld libelf1 rsync kmod cpio xz-utils \    git-lfs s-tui stress htop locales lcov libncurses6 libncurses-dev devscripts# Clone and build eBPF toolsmkdir -p eBPFpushd eBPFgit_clone_or_pull() {    local repo_url=$1    local dir_name=$2    if [ ! -d "$dir_name" ]; then        git clone --progress --recursive "$repo_url" "$dir_name"    else        git -C "$dir_name" pull    fi}git_clone_or_pull https://github.com/iovisor/bcc.git bccgit_clone_or_pull https://github.com/bpftrace/bpftrace.git bpftracegit_clone_or_pull https://github.com/libbpf/libbpf.git libbpfgit_clone_or_pull https://github.com/libbpf/libbpf-bootstrap.git libbpf-bootstrapgit_clone_or_pull https://github.com/libbpf/bpftool.git bpftool# Static link binariesEXTRA_CFLAGS=--staticpushd libbpf/srcmake -j$(nproc)sudo make installpopdpushd libbpf-bootstrap/examples/cmake -j$(nproc)popdpushd bpftool/srcmake -j$(nproc)sudo make installpopdmkdir -p bcc/buildpushd bcc/buildLLVM_ROOT=/usr/lib/llvm-14 cmake ..make -j$(nproc)sudo make installcmake -DPYTHON_CMD=python3 ..pushd src/python/make -j$(nproc)sudo make installpopdpopdpushd bcc/libbpf-tools/make -j$(nproc) BPFCFLAGS="-g -O2 -Wall -I/usr/include/$(uname -m)-linux-gnu"sudo make installpopdmkdir -p bpftrace/buildpushd bpftrace/buildLLVM_ROOT=/usr/lib/llvm-14 cmake -DCMAKE_BUILD_TYPE=Release -DBUILD_TESTING=OFF ..make -j$(nproc)sudo make installpopdpopd
```

代码下载地址：

https://github.com/feicong/ebpf-course/tree/main/.devcontainer

注意看build.sh，虽然跑在容器中，也支持在ubuntu22.04上一键运行部署。

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/k9S5z61JPnagibFHbJibmtyCM7IOiajRiaM0NuA7VKhACWn9uohpR26icDoZHQ4zxQH0vURtcmFkh5vzR5icYmY6cmibg/0?wx_fmt=png)

软件安全与逆向分析

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/k9S5z61JPnagibFHbJibmtyCM7IOiajRiaM0NuA7VKhACWn9uohpR26icDoZHQ4zxQH0vURtcmFkh5vzR5icYmY6cmibg/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过