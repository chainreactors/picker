---
title: KRIe - Linux Kernel Runtime Integrity With eBPF
url: https://buaq.net/go-145260.html
source: unSafe.sh - 不安全
date: 2023-01-13
fetch_date: 2025-10-04T03:43:23.927719
---

# KRIe - Linux Kernel Runtime Integrity With eBPF

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

![](https://8aqnet.cdn.bcebos.com/60e77d2cdfcc90433ed01612818899cc.jpg)

KRIe - Linux Kernel Runtime Integrity With eBPF

KRIe is a research project that aims to detect Linux Kernel exploits with eBPF. KRIe is far
*2023-1-12 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-145260.htm)
阅读量:36
收藏*

---

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjNmIECC7A08b9iRQsRhl-kYJ3NmF_8jrqbn9GxDP7-5Tp7P620sDoe8BSHhpAcTkIR-QwjZejUeL6rhxzd3CTpx-qH-ck8B76v1XHNbI7qHlcJVwEZv3wdJGo5U9b0FZ2yojt7Fzab5oSMBiRZMUPAnKSvnkosfteeZzLZJjfnjDhMe9tBn8s0XZjOgg/w640-h472/eBPF.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjNmIECC7A08b9iRQsRhl-kYJ3NmF_8jrqbn9GxDP7-5Tp7P620sDoe8BSHhpAcTkIR-QwjZejUeL6rhxzd3CTpx-qH-ck8B76v1XHNbI7qHlcJVwEZv3wdJGo5U9b0FZ2yojt7Fzab5oSMBiRZMUPAnKSvnkosfteeZzLZJjfnjDhMe9tBn8s0XZjOgg/s1324/eBPF.jpg)

KRIe is a [research project](https://www.kitploit.com/search/label/Research%20Project "research project") that aims to detect [Linux Kernel](https://www.kitploit.com/search/label/Linux%20Kernel "Linux Kernel") exploits with eBPF. KRIe is far from being a bulletproof strategy: from eBPF related limitations to [post exploitation](https://www.kitploit.com/search/label/Post%20Exploitation "post exploitation") detections that might rely on a compromised kernel to emit security events, it is clear that a motivated attacker will eventually be able to bypass it. That being said, the goal of the project is to make attackers' lives harder and ultimately prevent out-of-the-box exploits from working on a [vulnerable](https://www.kitploit.com/search/label/Vulnerable "vulnerable") kernel.

KRIe has been developed using [CO-RE (Compile Once - Run Everywhere)](https://facebookmicrosites.github.io/bpf/blog/2020/02/19/bpf-portability-and-co-re.html "CO-RE (Compile Once - Run Everywhere)") so that it is compatible with a large range of kernel versions. If your kernel doesn't export its BTF debug information, KRIe will try to download it automatically from [BTFHub](https://github.com/aquasecurity/btfhub "BTFHub"). If your kernel isn't available on BTFHub, but you have been able to manually generate your kernel's BTF data, you can provide it in the configuration file (see below).

### System requirements

This project was developed on Ubuntu Focal 20.04 (Linux Kernel 5.15) and has been tested on older releases down to Ubuntu Bionic 18.04 (Linux Kernel 4.15).

* golang 1.18+
* (optional) Kernel headers are expected to be installed in `lib/modules/$(uname -r)`, update the `Makefile` with their location otherwise.
* (optional) clang & llvm 14.0.6+

Optional fields are required to recompile the eBPF programs.

### Build

1. Since KRIe was built using CORE, you shouldn't need to rebuild the eBPF programs. That said, if you want still want to rebuild the eBPF programs, you can use the following command:

2. To build KRIE, run:

3. To install KRIE (copy to /usr/bin/krie) run:

### Getting started

KRIe needs to run as root. Run `sudo krie -h` to get help.

```
# ~ krie -h
```

### Configuration

```
## Log level, options are: panic, fatal, error, warn, info, debug or trace
log_level: debug

## JSON output file, leave empty to disable JSON output.
output: "/tmp/krie.json"

## BTF information for the current kernel in .tar.xz format (required only if KRIE isn't able to locate it by itself)
vmlinux: ""

## events configuration
events:
  ## action taken when an init_module event is detected
  init_module: log

## action taken when an delete_module event is detected
  delete_module: log

## action taken when a bpf event is detected
  bpf: log

## action taken when a bpf_filter event is detected
  bpf_filter: log

## action taken when a ptrace event is detected
  ptrace: log

## action taken when a kprobe event is detected
  kprobe: log

## action taken when a sysctl event is detected
  sysctl:
    action:    log

## Default settings for sysctl programs (kernel 5.2+ only)
    sysctl_default:
      block_read_access: false
      block_write_access: false

## Custom settings for sysctl programs (kernel 5.2+ only)
    sysctl_parameters:
      kernel/yama/ptrace_scope:
        block_write_access: true
      kernel/ftrace_enabled:
        override_input_value_with: "1\n"

## action taken when a hooked_syscall_table event is detected
  hooked_syscall_table: log

## action taken when a hooked_syscall event is detected
  hooked_syscall: log

## kernel_parameter event configuration
  kernel_parameter:
    action: log
    periodic_action: log
    ticker: 1 # sends at most one event every [ticker] second(s)
    list:
      - symbol: system/kprobes_all_disarmed
        expected_value: 0
        size: 4
      #      - symbol: system/selinux_state
      #        expecte   d_value: 256
      #        size: 2

# sysctl
      - symbol: system/ftrace_dump_on_oops
        expected_value: 0
        size: 4
      - symbol: system/kptr_restrict
        expected_value: 0
        size: 4
      - symbol: system/randomize_va_space
        expected_value: 2
        size: 4
      - symbol: system/stack_tracer_enabled
        expected_value: 0
        size: 4
      - symbol: system/unprivileged_userns_clone
        expected_value: 0
        size: 4
      - symbol: system/unprivileged_userns_apparmor_policy
        expected_value: 1
        size: 4
      - symbol: system/sysctl_unprivileged_bpf_disabled
        expected_value: 1
        size: 4
      - symbol: system/ptrace_scope
        expected_value: 2
        size: 4
      - symbol: system/sysctl_perf_event_paranoid
        expected_value: 2
        size: 4
      - symbol: system/kexe   c_load_disabled
        expected_value: 1
        size: 4
      - symbol: system/dmesg_restrict
        expected_value: 1
        size: 4
      - symbol: system/modules_disabled
        expected_value: 0
        size: 4
      - symbol: system/ftrace_enabled
        expected_value: 1
        size: 4
      - symbol: system/ftrace_disabled
        expected_value: 0
        size: 4
      - symbol: system/sysctl_protected_fifos
        expected_value: 1
        size: 4
      - symbol: system/sysctl_protected_hardlinks
        expected_value: 1
        size: 4
      - symbol: system/sysctl_protected_regular
        expected_value: 2
        size: 4
      - symbol: system/sysctl_protected_symlinks
        expected_value: 1
        size: 4
      - symbol: system/sysctl_unprivileged_userfaultfd
        expected_value: 0
        size: 4

## action to check when a regis   ter_check fails on a sensitive kernel space hook point
  register_check: log
```

## Documentation

* The first version of KRIe was announced at BlackHat 2022, during the briefing: [Return to Sender - Detecting Kernel Exploits with eBPF](https://www.blackhat.com/us-22/briefings/schedule/index.html#return-to-sender---detecting-kernel-exploits-with-ebpf-27127 "Return to Sender - Detecting Kernel Exploits with eBPF")

## License

* The golang code is under Apache 2.0 License.
* The eBPF programs are under the GPL v2 License.

KRIe - Linux Kernel Runtime Integrity With eBPF
![KRIe - Linux Kernel Runtime Integrity With eBPF](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjNmIECC7A08b9iRQsRhl-kYJ3NmF_8jrqbn9GxDP7-5Tp7P620sDoe8BSHhpAcTkIR-QwjZejUeL6rhxzd3CTpx-qH-ck8B76v1XHNbI7qHlcJVwEZv3wdJGo5U9b0FZ2yojt7Fzab5oSMBiRZMUPAnKSvnkosfteeZzLZJjfnjDhMe9tBn8s0XZjOgg/s72-w640-c-h472/eBPF.jpg)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2023/01/krie-linux-kernel-runtime-integrity.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe...