---
title: Linux ELF Shellcode 生成与 Fileless 实战
url: https://guage.cool/linux-shellcode.html
source: 半块西瓜皮
date: 2026-05-21
fetch_date: 2026-05-22T06:07:19.488682
---

# Linux ELF Shellcode 生成与 Fileless 实战

[![](/img/avatar.jpg)](/about/)[氓聧聤氓聺聴猫楼驴莽聯聹莽職庐](/)

忙虏隆忙聹聣忙聣戮氓聢掳氓聠聟氓庐鹿茂录聛

忙聹卢忙聳聡莽聸庐氓陆聲

1. [zigdonut 莽庐聙盲禄聥](#zigdonut-%E7%AE%80%E4%BB%8B)
   1. [莽聣鹿忙聙搂](#%E7%89%B9%E6%80%A7)
2. [盲赂潞盲禄聙盲鹿聢茅聹聙猫娄聛 Static + PIE](#%E4%B8%BA%E4%BB%80%E4%B9%88%E9%9C%80%E8%A6%81-Static-PIE)
   1. [莽录聳猫炉聭 C 盲禄拢莽聽聛茂录職盲禄楼 busybox 盲赂潞盲戮聥](#%E7%BC%96%E8%AF%91-C-%E4%BB%A3%E7%A0%81%EF%BC%9A%E4%BB%A5-busybox-%E4%B8%BA%E4%BE%8B)
   2. [莽录聳猫炉聭 Go 盲禄拢莽聽聛茂录職盲禄楼 fscan 盲赂潞盲戮聥](#%E7%BC%96%E8%AF%91-Go-%E4%BB%A3%E7%A0%81%EF%BC%9A%E4%BB%A5-fscan-%E4%B8%BA%E4%BE%8B)
3. [3. Fileless 盲陆驴莽聰篓氓聹潞忙聶炉](#3-Fileless-%E4%BD%BF%E7%94%A8%E5%9C%BA%E6%99%AF)
   1. [3.1 C2忙聫聮盲禄露氓聹潞忙聶炉茂录職](#3-1-C2%E6%8F%92%E4%BB%B6%E5%9C%BA%E6%99%AF%EF%BC%9A)
   2. [3.2 氓聟聧忙聺聙氓聹潞忙聶炉茂录職python氓聤聽猫陆陆Shellcode](#3-2-%E5%85%8D%E6%9D%80%E5%9C%BA%E6%99%AF%EF%BC%9Apython%E5%8A%A0%E8%BD%BDShellcode)
4. [忙聙禄莽禄聯](#%E6%80%BB%E7%BB%93)

氓聸聻氓聢掳茅隆露茅聝篓氓聫聜盲赂聨猫庐篓猫庐潞

[![](data:image/png;base64...)](https://github.com/howmp)[![](data:image/png;base64...)](https://weibo.com/howmp)[![](data:image/png;base64...)](https://guage.cool/atom.xml)![](data:image/png;base64...)

[盲赂禄茅隆碌](/)
[忙聳聡莽芦聽](/)[莽录聳莽篓聥](/categories/%E7%BC%96%E7%A8%8B/)  [氓聟聧忙聺聙](/categories/%E7%BC%96%E7%A8%8B/%E5%85%8D%E6%9D%80/)

氓聫聭氓赂聝盲潞聨茂录職2026-05-21忙聸麓忙聳掳盲潞聨茂录職2026-05-21

# Linux ELF Shellcode 莽聰聼忙聢聬盲赂聨 Fileless 氓庐聻忙聢聵

## zigdonut 莽庐聙盲禄聥

[zigdonut](https://github.com/howmp/zigdonut)忙聵炉盲赂聙盲赂陋莽聰篓 Zig 氓庐聻莽聨掳莽職聞莽虏戮莽庐聙莽聣聢 donut茫聙聜

忙聹聙猫驴聭忙聳掳氓垄聻盲潞聠linux ELF 莽篓聥氓潞聫猫陆卢忙聧垄忙聢聬shellcode莽職聞氓聤聼猫聝陆茫聙聜

氓聫炉盲禄楼盲禄聨<https://github.com/howmp/zigdonut/releases/tag/v2.0.0>盲赂聥猫陆陆盲陆聯茅陋聦

### 莽聣鹿忙聙搂

1. 盲禄聟忙聰炉忙聦聛茅聺聶忙聙聛茅聯戮忙聨楼莽職聞PIE/ET\_DYN ELF
2. 氓聢露盲陆聹shellcode忙聴露氓聨聥莽录漏茂录聦氓聤聽猫陆陆忙聴露猫聡陋氓聤篓猫搂拢氓聨聥
3. Double fork猫聞卤莽娄禄忙聨搂氓聢露莽禄聢莽芦炉茂录聦氓聬聨氓聫掳忙聣搂猫隆聦茂录聦盲赂聧盲潞搂莽聰聼氓聝碌氓掳赂猫驴聸莽篓聥
4. 氓聫炉氓聤篓忙聙聛忙聦聡氓庐職猫戮聯氓聡潞忙聳聡盲禄露盲禄楼氓聫聤氓聫聜忙聲掳茂录聦stdin/stderr茅聡聧氓庐職氓聬聭氓聢掳猫戮聯氓聡潞忙聳聡盲禄露
5. 氓聢聡忙聧垄氓路楼盲陆聹莽聸庐氓陆聲氓聢掳/tmp

## 盲赂潞盲禄聙盲鹿聢茅聹聙猫娄聛 Static + PIE

zigdonut 莽職聞 ELF shellcode 忙篓隆氓录聫猫娄聛忙卤聜猫戮聯氓聟楼忙聳聡盲禄露氓驴聟茅隆禄忙聵炉**茅聺聶忙聙聛茅聯戮忙聨楼 + PIE茂录聢ET\_DYN茂录聣**忙聽录氓录聫茫聙聜氓聨聼氓聸聽氓娄聜盲赂聥茂录職

* **PIE茂录聢盲陆聧莽陆庐忙聴聽氓聟鲁氓聫炉忙聣搂猫隆聦忙聳聡盲禄露茂录聣**茂录職PIE茅聙職猫驴聡茅聡聧氓庐職盲陆聧猫隆篓盲驴庐氓陇聧氓聬聨茂录聦氓聫炉盲禄楼氓聤聽猫陆陆氓聠聟氓颅聵盲禄禄忙聞聫盲陆聧莽陆庐茫聙聜茅聺聻PIE盲赂聥氓娄聜忙聻聹氓聤聽猫陆陆盲陆聧莽陆庐氓路虏莽禄聫猫垄芦氓聧聽莽聰篓茂录聦盲录職忙聴聽忙鲁聲氓聤聽猫陆陆茫聙聜
* **茅聺聶忙聙聛茅聯戮忙聨楼**茂录職盲赂聧盲戮聺猫碌聳盲禄禄盲陆聲氓聟露盲禄聳so忙聳聡盲禄露

茅陋聦猫炉聛忙聵炉氓聬娄莽卢娄氓聬聢猫娄聛忙卤聜茂录職

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` readelf -h busybox | grep "Type:" #    Type:  DYN (Shared object file)   芒聠聬 PIE  ldd busybox #    statically linked           芒聠聬 茅聺聶忙聙聛茅聯戮忙聨楼 ``` |

### 莽录聳猫炉聭 C 盲禄拢莽聽聛茂录職盲禄楼 busybox 盲赂潞盲戮聥

busybox 茅禄聵猫庐陇莽录聳猫炉聭盲赂潞茅聺聶忙聙聛 ELF茂录聦盲陆聠盲赂聧忙聵炉 PIE茫聙聜茅聹聙猫娄聛氓聹篓 Alpine 氓庐鹿氓聶篓盲赂颅盲陆驴莽聰篓 musl-gcc 茅聡聧忙聳掳茅聯戮忙聨楼盲赂潞 static-pie茂录職

Dockerfile茂录職

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 ``` | ``` FROM alpine:3.20  RUN apk add --no-cache \     build-base \     wget \     tar \     bash \     linux-headers ``` |

忙聻聞氓禄潞猫聞職忙聹卢`build.sh`茂录職

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 ``` | ``` #!/bin/bash set -e  make distclean make defconfig sed -i 's/.*CONFIG_STATIC.*/CONFIG_STATIC=y/' .config sed -i '/CONFIG_EXTRA_CFLAGS/c\CONFIG_EXTRA_CFLAGS="-fPIC"' .config sed -i '/CONFIG_EXTRA_LDFLAGS/c\CONFIG_EXTRA_LDFLAGS=""' .config make CFLAGS="-fPIC" -j$(nproc)  # 氓掳聠 .a 茅聡聧忙聳掳茅聯戮忙聨楼盲赂潞 static-pie gcc -fPIC -static-pie -o busybox_musl_pie \     -Wl,--sort-common -Wl,--sort-section,alignment \     -Wl,--start-group \     applets/built-in.o archival/lib.a archival/libarchive/lib.a \     console-tools/lib.a coreutils/lib.a coreutils/libcoreutils/lib.a \     debianutils/lib.a klibc-utils/lib.a e2fsprogs/lib.a editors/lib.a \     findutils/lib.a init/lib.a libbb/lib.a libpwdgrp/lib.a \     loginutils/lib.a mailutils/lib.a miscutils/lib.a modutils/lib.a \     networking/lib.a networking/libiproute/lib.a networking/udhcp/lib.a \     printutils/lib.a procps/lib.a runit/lib.a selinux/lib.a \     shell/lib.a sysklogd/lib.a util-linux/lib.a util-linux/volume_id/lib.a \     -Wl,--end-group \     -lcrypt -lm -lpthread  strip -s --remove-section=.note --remove-section=.comment busybox_musl_pie readelf -h busybox_musl_pie | grep "Type:" ldd busybox_musl_pie ``` |

莽录聳猫炉聭茂录職

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` docker build --network=host -t build-busybox . docker run -it --rm -v $(pwd):/code --network=host build-busybox sh # 氓庐鹿氓聶篓氓聠聟茂录職 cd code && sh build.sh ``` |

氓聟鲁茅聰庐莽聜鹿茂录職

* `CONFIG_STATIC=y`氓聬炉莽聰篓茅聺聶忙聙聛莽录聳猫炉聭
* `CFLAGS="-fPIC"`莽聰聼忙聢聬盲陆聧莽陆庐忙聴聽氓聟鲁盲禄拢莽聽聛
* `-static-pie`茅聯戮忙聨楼茅聙聣茅隆鹿莽聰聼忙聢聬 PIE 忙聽录氓录聫莽職聞茅聺聶忙聙聛氓聫炉忙聣搂猫隆聦忙聳聡盲禄露
* musl-libc 忙炉聰 glibc 忙聸麓茅聙聜氓聬聢茅聺聶忙聙聛莽录聳猫炉聭茂录聦盲陆聯莽搂炉忙聸麓氓掳聫

### 莽录聳猫炉聭 Go 盲禄拢莽聽聛茂录職盲禄楼 fscan 盲赂潞盲戮聥

|  |  |
| --- | --- |
| ``` 1 ``` | ``` CC="zig cc -target x86_64-linux-musl" go build -buildmode=pie -ldflags "-linkmode external -extldflags '-static -pie' -s -w" -trimpath . ``` |

## 3. Fileless 盲陆驴莽聰篓氓聹潞忙聶炉

### 3.1 C2忙聫聮盲禄露氓聹潞忙聶炉茂录職

氓聫炉氓聫聜猫聙聝[elfscloader.c](https://github.com/howmp/zigdonut/blob/main/src/elfscloader.c)

氓庐聻莽聨掳茅聺聻氓赂赂莽庐聙氓聧聲茂录聢莽潞娄 60 猫隆聦 C 盲禄拢莽聽聛茂录聣茂录聦忙聽赂氓驴聝氓掳卤忙聵炉`mmap`RWX 氓聠聟氓颅聵 芒聠聮 忙聥路猫麓聺 shellcode 芒聠聮 猫路鲁猫陆卢忙聣搂猫隆聦茂录職

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` void *sc_addr = mmap(NULL, map_size, PROT_READ | PROT_WRITE | PROT_EXEC,                      MAP_PRIVATE | MAP_ANONYMOUS, -1, 0); memcpy(sc_addr, data, size); typedef void (*shellcode_fn)(char *output, size_t argc, char **argv, char **envp); shellcode_fn sc_fn = (shellcode_fn)sc_addr; sc_fn(argv[2], (size_t)(argc - 3), argv + 3, envp); ``` |

### 3.2 氓聟聧忙聺聙氓聹潞忙聶炉茂录職python氓聤聽猫陆陆Shellcode

盲录聽莽禄聼忙聳鹿氓录聫莽聸麓忙聨楼盲赂聤盲录聽 ELF 氓聢掳莽聸庐忙聽聡忙聹潞氓聶篓茂录聦氓戮聢氓庐鹿忙聵聯猫垄芦 EDR/AV 忙拢聙忙碌聥茫聙聜氓聫炉盲禄楼茅聙職猫驴聡python氓聤聽猫陆陆shellcode

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 ``` | ``` #!/usr/bin/env python3 """ELF shellcode loader - Python version of elfscloader.c"""  import sys import os import ctypes   def main():     if len(sys.argv) < 3:         print(f"usage: {sys.argv[0]} <shellcode_file> <output> <elfname> [args...]", file=sys.stderr)         sys.exit(1)      filepath = sys.argv[1]     output = sys.argv[2]     elf_args = sys.argv[3:]      # Read shellcode from file     with open(filepath, "rb") as f:         sc_data = f.read()     sc_size = len(sc_data)     print(f"[+] loaded shellcode: {filepath} ({sc_size} bytes)")      # Setup libc with proper types     libc = ctypes.CDLL("libc.so.6", use_errno=True)     libc.mmap.restype = ctypes.c_void_p     libc.mmap.argtypes = [         ctypes.c_void_p, ctypes.c_size_t, ctypes.c_int,         ctypes.c_int, ctypes.c_int, ctypes.c_size_t,     ]      PROT_READ  = 1     PROT_WRITE = 2     PROT_EXEC  = 4     MAP_PRIVATE   = 0x02     MAP_ANONYMOUS = 0x20      page_size = os.sysconf("SC_PAGESIZE")     map_size = (sc_size + page_size - 1) & ~(page_size - 1)      sc_addr = libc.mmap(         None,         map_size,         PROT_READ | PROT_WRITE | PROT_EXEC,         MAP_PRIVATE | MAP_ANONYMOUS,         -1,         0,     )     if sc_addr == ctypes.c_void_p(-1).value:         print("[x] mmap failed", file=sys.stderr)         sys.exit(1)      # Copy shellcode into executable memory     ctypes.memmove(sc_addr, sc_data, sc_size)     print(f"[+] shellcode at: {hex(sc_addr)}")     print(f"[+] output: {output}")     print(f"[+] elfname: {elf_args[0] if elf_args else ''}")      # Build argv: char*[]     argc = len(elf_args)     argv_arr = (ctypes.c_char_p * (argc + 1))()     for i, arg in enumerate(elf_args):         argv_arr[i] = arg.encode()     argv_arr[argc] = None      # Build envp: char*[]     env_list = list(os.environ.items())     envp_arr = (ctypes.c_char_p * (len(env_list) + 1))()     for i, (k, v) in enumerate(env_list):         envp_arr[i] = f"{k}={v}".encode()     envp_arr[len(env_list)] = None      # void (*)(char *output, size_t argc, char **argv, char **envp)     FUNCTYPE = ctypes.CFUNCTYPE(None, ctypes.c_c...