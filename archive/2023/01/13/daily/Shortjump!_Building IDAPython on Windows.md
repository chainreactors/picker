---
title: Building IDAPython on Windows
url: https://0xeb.net/2023/01/building-idapython-on-windows/
source: Shortjump!
date: 2023-01-13
fetch_date: 2025-10-04T03:45:17.729024
---

# Building IDAPython on Windows

[Skip to content](#content)

# [Shortjump!](https://0xeb.net/)

## Reversing engineering, programming and what not…

Menu

* [Home](https://0xeb.net/)
* [About](https://0xeb.net/about/)

[Home](https://0xeb.net/)Building IDAPython on Windows

# Building IDAPython on Windows

[January 12, 2023](https://0xeb.net/2023/01/building-idapython-on-windows/) [elias](https://0xeb.net/author/elias/)
[IDAPython](https://0xeb.net/category/reverse-engineering/idapython/), [Reverse Engineering](https://0xeb.net/category/reverse-engineering/)

# Introduction

If you use IDAPython a lot, I am sure you started reading its source code or felt the need to add missing functionality. In this article, we will show you how to build IDAPython on Windows.

On Linux/macOS, the process is straightforward as per the [BUILDING.txt](https://github.com/idapython/src/blob/master/BUILDING.txt).

In this article:

* [Setting up VS 2019](#vs2019)
* [Setting up Cygwin](#cygwin)
* [Setting up Python 3.x](#python)
* [Setting up SWIG](#swig)
* [Setting up IDA SDK](#idasdk)
* [Building IDAPython](#idapython)

Make sure you already installed the latest IDA for Windows and grabbed yourself a copy of the [SDK](https://hex-rays.com/download-center).

Let’s get started.

# Setting up VS 2019 Community Edition

IDA SDK’s default configuration is targeted towards VS 2019. Just to keep this article simple, let’s stick with that.

Grab VS2019 from here <https://visualstudio.microsoft.com/vs/older-downloads/>

When you install it, make sure you leave all the default installation location (in the `C:\Program Files (x86)`, etc.)

# Setting up Cygwin 64

Download [Cygwin 64](https://www.cygwin.com/setup-x86_64.exe) and install the following components:

* `make` from the `Devel` category.
* `unzip` from the `Archive` category.

# Setting up Python 3.x

Download Python 3.x *AMD64* (say 3.4 to 3.11) and select custom install:

* Install to C:(X = major, Y = minor)
* Make sure you select the following options:
  + for all users
  + pip
  + Precompile standard library
  + Optional: “Download debugging symbols”

After Python is installed, install the `six` module:

```
C:\PythonXY\Scripts\pip install six
```

# Setting up SWIG

In this section, we will build [SWIG](https://www.swig.org) for Windows from scratch. We need a special patched version of SWIG (version 4.0.1, with support for `-py3-limited-api`) and we cannot use the pre-built binaries.

Whether you are using a Linux distro (for example Ubuntu 20) or WSL on Windows 10/11, all the steps below still apply.

Depending on your Linux setup, you may have already installed the needed packages. Just to be on the safe side, you need the following:

```
sudo apt update
sudo apt install wget build-essential mingw-w64 byacc bison automake autotools-dev patchelf -y
```

> If mingw-64 failed to install:
> `sudo apt-add-repository ppa:mingw-w64/ppa && sudo apt-get update && sudo apt-get install mingw-w64`

## Clone IDAPython’s patched SWIG

```
git clone --branch py3-stable-abi https://github.com/idapython/swig.git swig-py3-stable-abi
```

## Download PCRE library and build it

Download PCRE directly into SWIG’s source directory:

`wget https://master.dl.sourceforge.net/project/pcre/pcre/8.10/pcre-8.10.tar.bz2`

Then edit the PCRE build script in SWIG to specify the host compiler:

Open `./Tools/pcre-build.sh` and change this line:

`cd pcre && ./configure --prefix=$pcre_install_dir --disable-shared $* || bail "PCRE configure failed"`

To:

`cd pcre && ./configure --host=x86_64-w64-mingw32 --prefix=$pcre_install_dir --disable-shared $* || bail "PCRE configure failed"`

(we only added the `--host` switch)

Now just run the PCRE build script again:

`./Tools/pcre-build.sh`

You are now ready to build SWIG.

## Building SWIG

First run `./autogen.sh`, then run the configure script with the `--host` switch, while also specifying static linking:

```
LDFLAGS="-static -static-libgcc -static-libstdc++" \
./configure --host=x86_64-w64-mingw32 --prefix=/tmp/swig4-win
```

Now you can run `make` and `make install` as usual.

Alternatively, you can download the pre-build version from [here](http://0xeb.net/wp-content/uploads/2023/01/swig4-win.zip).

Copy the SWIG Windows binaries from `/tmp/swig4-win` to your Windows machine. Let’s put them in `C:\idasdk\swig4`.

# Setting up the IDA SDK

* Download the IDA SDK and unzip to a folder, for example `c:\idasdk`.
* If you have the Decompiler installed, then copy the Decompiler headers from `<ida_install>/plugins/hexrays_sdk/include/hexrays.hpp` to `c:\idasdk\include`.

## Initialize the SDK’s config files

We need to configure various configurations. Open the “Developer Command Prompt for VS 2019”.

If Cygwin was not in the path, then typing ‘make’ will cause an error. If that’s the case, just add it to the PATH:

```
set PATH=c:\cygwin64\bin;%PATH%
```

(Keep that command prompt open for the remainder of this article.)

From `c:\idasdk`, type the following commands:

```
cd c:\idasdk
set __NT__=1
set __X64__=1
```

Now let’s generate the various config files:

* ida64 debug build: `cmd /c "set __EA64__=1 && make env"`
* ida64 optimized build: `cmd /c "set __EA64__=1 && set NDEBUG=1 && make env"`
* ida debug build: `make env`
* ida optimized build: `cmd /c "set NDEBUG=1 && make env`

If you have done everything right, you should have these files in `c:\idasdk`:

* vs19paths.cfg
* x64\_win\_vc\_32.cfg
* x64\_win\_vc\_32\_opt.cfg
* x64\_win\_vc\_64.cfg
* x64\_win\_vc\_64\_opt.cfg

To test if everything is okay, let’s try building the `hello` plugin:

```
cd c:\idasdk\plugins\hello
make
```

Last but not least, let’s put the IDA binaries in the correct place in accordance with the SDK make system. Assuming that IDA was installed in `C:\Tools\IDA82`:

```
xcopy /s c:\Tools\IDA82 c:\idasdk\bin
```

Now, anything we build will go to `c:\idasdk\bin\[plugins|loaders|procs]`:

* `plugins`: for plugin binaries
* `loaders`: for loader modules
* `procs`: for processor modules

# Building IDAPython

Okay, now we are ready to build IDAPython!

## Clone IDAPython

Navigate to `c:\idasdk\plugins` and clone IDAPython there:

```
git clone https://github.com/idapython/src.git idapython
```

## Building IDAPython

Now we have all the prerequisit steps completed, let’s build IDAPython:

```
set PYTHON_VERSION_MAJOR=X
set PYTHON_VERSION_MINOR=Y

C:\PythonXY\python.exe build.py --with-hexrays --swig-home c:\ida\swig4 --ida-install c:\idasdk\bin --debug
```

* Replace `X` and `Y` with the proper values
* If you don’t have the Decompiler then omit the `--with-hexrays` switch
* Similarily, drop the `--debug` for optimized builds.
* Run `build.py --help` for more information

Be patient, this can take between 5 and 30 minutes to complete the first time.

# That’s it!

I know, this has been tedious but I hope it is helpful.

Contributions and suggestions to [IDAPython](https://github.com/idapython/src). We are happy to discuss and merge your changes as applicable.

### Share this:

* [Click to share on Twitter (Opens in new window)](https://0xeb.net/2023/01/building-idapython-on-windows/?share=twitter "Click to share on Twitter")
* [Click to share on Facebook (Opens in new window)](https://0xeb.net/2023/01/building-idapython-on-windows/?share=facebook "Click to share on Facebook")

### *Related*

# Post navigation

[← climacros – IDA productivity tool](https://0xeb.net/2019/04/climacros-ida-productivity-tool/)

### Leave a Reply [Cancel reply](/2023/01/building-idapython-on-windows/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

Website

[ ]  Notify me of follow-up comments by email.

[ ]  Notify me of new posts by email.

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed](https://akismet.com/privacy/).

Search for:

# Recent Posts

* [Building IDAPython on Windows](https://0xeb.net/2023/01/building-idapython-on-windows/)
* [climacros – IDA productivity ...