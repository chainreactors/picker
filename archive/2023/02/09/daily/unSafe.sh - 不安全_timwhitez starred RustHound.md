---
title: timwhitez starred RustHound
url: https://buaq.net/go-148516.html
source: unSafe.sh - 不安全
date: 2023-02-09
fetch_date: 2025-10-04T06:05:16.326370
---

# timwhitez starred RustHound

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/e02d32da578d9db59a8e5f0bb748b87d.jpg)

timwhitez starred RustHound

LimitationDescriptionHow to compile it?Using Makefi
*2023-2-8 18:47:56
Author: [github.com(查看原文)](/jump-148516.htm)
阅读量:31
收藏*

---

[![Crates.io](https://camo.githubusercontent.com/903cf2e2a8689d48baaf94621c67de82ce05e5765dbf911a84cba4fa8ef43fed/68747470733a2f2f696d672e736869656c64732e696f2f6372617465732f762f72757374686f756e643f7374796c653d666f722d7468652d6261646765)](https://crates.io/crates/rusthound)
[![GitHub](https://camo.githubusercontent.com/9911f7b7318fd029c412939ec4c1dfd2663aae4de6105ff63ae1f1711b333ab1/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f4f50454e43594245522d46522f52757374486f756e643f7374796c653d666f722d7468652d6261646765)](https://camo.githubusercontent.com/9911f7b7318fd029c412939ec4c1dfd2663aae4de6105ff63ae1f1711b333ab1/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f4f50454e43594245522d46522f52757374486f756e643f7374796c653d666f722d7468652d6261646765)
[![Linux supported](https://camo.githubusercontent.com/280313099bf71550ece6cf6f5d0d934c4e40095f78d2089613990c3e213c99c5/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f537570706f727465642532304f532d4c696e75782d6f72616e67653f7374796c653d666f722d7468652d6261646765)](https://camo.githubusercontent.com/280313099bf71550ece6cf6f5d0d934c4e40095f78d2089613990c3e213c99c5/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f537570706f727465642532304f532d4c696e75782d6f72616e67653f7374796c653d666f722d7468652d6261646765)
[![Windows supported](https://camo.githubusercontent.com/239a582b781850201deec9c3fdaa301977447718e86a6c3f0ae73e0503177344/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f537570706f727465642532304f532d57696e646f77732d677265656e3f7374796c653d666f722d7468652d6261646765)](https://camo.githubusercontent.com/239a582b781850201deec9c3fdaa301977447718e86a6c3f0ae73e0503177344/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f537570706f727465642532304f532d57696e646f77732d677265656e3f7374796c653d666f722d7468652d6261646765)
[![macOS supported](https://camo.githubusercontent.com/820f2dc46e43dbe00089379bf48ccb8ab997c1635004b2f4ced77ae18d436938/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f537570706f727465642532304f532d4d61634f532d626c75653f7374796c653d666f722d7468652d6261646765)](https://camo.githubusercontent.com/820f2dc46e43dbe00089379bf48ccb8ab997c1635004b2f4ced77ae18d436938/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f537570706f727465642532304f532d4d61634f532d626c75653f7374796c653d666f722d7468652d6261646765)
[![Twitter Follow](https://camo.githubusercontent.com/b1ca38a6fc43f5ec1e8f72a98eb813957cdfb67ad94ee982312077fddbc94f37/68747470733a2f2f696d672e736869656c64732e696f2f747769747465722f666f6c6c6f772f4f50454e43594245525f46523f6c6162656c3d4f50454e43594245525f4652267374796c653d666f722d7468652d6261646765)](https://twitter.com/intent/follow?screen_name=OPENCYBER_FR "Follow")
[![](https://camo.githubusercontent.com/15b08ea477123af46bdf27db8ea29602f6b16fb1730d02234b7e68731639e695/68747470733a2f2f696d672e736869656c64732e696f2f747769747465722f666f6c6c6f772f673068346e5f303f6c6162656c3d673068346e267374796c653d666f722d7468652d6261646765)](https://twitter.com/intent/follow?screen_name=g0h4n_0 "Follow")

[![](https://github.com/OPENCYBER-FR/RustHound/raw/main/img/rusthound_logo_v3.png)](https://github.com/OPENCYBER-FR/RustHound/blob/main/img/rusthound_logo_v3.png)

* [Limitation](#limitations)
* [Description](#description)
* [How to compile it?](#how-to-compile-it)
  + [Using Makefile](#using-makefile)
  + [Using Dockerfile](#using-dockerfile)
  + [Using Cargo](#using-cargo)
  + [Linux x86\_64 static version](#manually-for-linux-x86_64-static-version)
  + [Windows static version from Linux](#manually-for-windows-static-version-from-linux)
  + [macOS static version from Linux](#manually-for-macos-static-version-from-linux)
* [How to build documentation?](#how-to-build-documentation)
* [Usage](#usage)
* [Demo](#demo)
  + [Simple usage](#simple-usage)
  + [Module FQDN resolver](#module-fqdn-resolver)
  + [Module ADCS collector](#module-adcs-collector)
* [Statistics](#rocket-statistics)
* [Roadmap](#-roadmap)
* [Links](#link-links)

Not all SharpHound features have been implemented. Some exist in RustHound and not in SharpHound or BloodHound-Python. Please refer to the [roadmap](#-roadmap) for more information.

RustHound is a **cross-platform** BloodHound collector tool written in Rust, making it compatible with Linux, Windows, and macOS.

No AV detection and **cross-compiled**.

RustHound generates users, groups, computers, OUs, GPOs, containers, and domain JSON files that can be analyzed with BloodHound.

> 💡 If you can use SharpHound, use it.
> Use RustHound as a backup solution if SharpHound is detected by AV or if it not compatible with your OS.

## Using Makefile

You can use the **make** command to install RustHound or to compile it for Linux or Windows.

```
make install
rusthound -h
```

More command in the **Makefile**:

```
Default:
usage: make install
usage: make uninstall
usage: make debug
usage: make release

Static:
usage: make windows
usage: make linux_musl
usage: make macos

Dependencies:
usage: make install_windows_deps
usage: make install_linux_musl_deps
usage: make install_macos_deps
```

## Using Dockerfile

Use RustHound with Docker to make sure to have all dependencies.

```
docker build -t rusthound .
docker run rusthound -h
```

## Using Cargo

You will need to install Rust on your system.

<https://www.rust-lang.org/fr/tools/install>

RustHound supports Kerberos and GSSAPI. Therefore, it requires Clang and its development libraries, as well as the Kerberos development libraries. On Debian and Ubuntu, this means **clang-N**, **libclang-N-dev**, and **libkrb5-dev**.

For example:

```
# Debian/Ubuntu
sudo apt-get -y update && sudo apt-get -y install gcc libclang-dev clang libclang-dev libgssapi-krb5-2 libkrb5-dev libsasl2-modules-gssapi-mit musl-tools gcc-mingw-w64-x86-64
```

Here is how to compile the "release" and "debug" versions using the **cargo** command.

```
git clone https://github.com/OPENCYBER-FR/RustHound
cd RustHound
cargo build --release
# or debug version
cargo b
```

The result can be found in the target/release or target/debug folder.

Below you can find the compilation methodology for each of the OS from Linux.
If you need another compilation system, please consult the list in this link: <https://doc.rust-lang.org/nightly/rustc/platform-support.html>

## Manually for Linux x86\_64 static version

```
# Install rustup and Cargo for Linux
curl https://sh.rustup.rs -sSf | sh

# Add Linux deps
rustup install stable-x86_64-unknown-linux-gnu
rustup target add x86_64-unknown-linux-gnu

# Static compilation for Linux
git clone https://github.com/OPENCYBER-FR/RustHound
cd RustHound
CFLAGS="-lrt";LDFLAGS="-lrt";RUSTFLAGS='-C target-feature=+crt-static';cargo build --release --target x86_64-unknown-linux-gnu
```

The result can be found in the target/x86\_64-unknown-linux-gnu/release folder.

## Manually for Windows static version from Linux

```
# Install rustup and Cargo in Linux
curl https://sh.rustup.rs -sSf | sh

# Add Windows deps
rustup install stable-x86_64-pc-windows-gnu
rustup target add x86_64-pc-windows-gnu

# Static compilation for Windows
git clone https://github.com/OPENCYBER-FR/RustHound
cd RustHound
RUSTFLAGS="-C target-feature=+crt-static" cargo build --release --target x86_64-pc-windows-gnu
```

The result can be found in the target/x86\_64-pc-windows-gnu/release folder.

## Manually for macOS ...