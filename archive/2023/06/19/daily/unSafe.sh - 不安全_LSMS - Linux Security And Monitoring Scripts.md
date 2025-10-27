---
title: LSMS - Linux Security And Monitoring Scripts
url: https://buaq.net/go-169251.html
source: unSafe.sh - 不安全
date: 2023-06-19
fetch_date: 2025-10-04T11:44:47.232512
---

# LSMS - Linux Security And Monitoring Scripts

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

![](https://8aqnet.cdn.bcebos.com/54a3f14e1573b3496cccf5faff2ca3bf.jpg)

LSMS - Linux Security And Monitoring Scripts

These are a collection of security and monitoring scripts you can use to monitor your Linux
*2023-6-18 20:30:0
Author: [www.kitploit.com(查看原文)](/jump-169251.htm)
阅读量:35
收藏*

---

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhhOUAv4hUykZ7J9MXslUWbxCDdlHdtbIiIMFSGK9cWC7UGCIY9e3NHe6DdxYtRR50ZdqSyROXW3zOdvWk0KOv1UEeXNA3OqCuSVUK1CNkgr3H9OYCM3UIFSukK_k-zf4nsXK43n30h3uePBiAHWqvanxuri0bxEHY9AWSzfakNd4mYQTxUVL4bwWJBxg/w640-h420/h39.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhhOUAv4hUykZ7J9MXslUWbxCDdlHdtbIiIMFSGK9cWC7UGCIY9e3NHe6DdxYtRR50ZdqSyROXW3zOdvWk0KOv1UEeXNA3OqCuSVUK1CNkgr3H9OYCM3UIFSukK_k-zf4nsXK43n30h3uePBiAHWqvanxuri0bxEHY9AWSzfakNd4mYQTxUVL4bwWJBxg/s537/h39.png)

These are a collection of security and monitoring [scripts](https://www.kitploit.com/search/label/Scripts "scripts") you can use to monitor your Linux installation for security-related events or for an investigation. Each script works on its own and is independent of other scripts. The scripts can be set up to either print out their results, send them to you via mail, or using [AlertR](https://github.com/sqall01/alertR "AlertR") as notification channel.

## Repository Structure

The scripts are located in the [directory](https://www.kitploit.com/search/label/Directory "directory") `scripts/`. Each script contains a short summary in the header of the file with a description of what it is supposed to do, (if needed) dependencies that have to be installed and (if available) references to where the idea for this script stems from.

Each script has a configuration file in the `scripts/config/` directory to configure it. If the configuration file was not found during the execution of the script, the script will fall back to default settings and print out the results. Hence, it is not necessary to provide a configuration file.

The `scripts/lib/` directory contains code that is shared between different scripts.

Scripts using a `monitor_` prefix hold a state and are only useful for monitoring purposes. A single usage of them for an investigation will only result in showing the current state the Linux system and not changes that might be relevant for the system's security. If you want to establish the current state of your system as benign for these scripts, you can provide the `--init` argument.

## Usage

Take a look at the header of the script you want to execute. It contains a short description what this script is supposed to do and what [requirements](https://www.kitploit.com/search/label/Requirements "requirements") are needed (if any needed at all). If requirements are needed, install them before running the script.

The shared configuration file `scripts/config/config.py` contains settings that are used by all scripts. Furthermore, each script can be configured by using the corresponding configuration file in the `scripts/config/` directory. If no configuration file was found, a default setting is used and the results are printed out.

Finally, you can run all configured scripts by executing `start_search.py` (which is located in the main directory) or by executing each script manually. A Python3 interpreter is needed to run the scripts.

### Monitoring

If you want to use the scripts to monitor your Linux system constantly, you have to perform the following steps:

1. Set up a notification channel that is supported by the scripts (currently printing out, mail, or [AlertR](https://github.com/sqall01/alertR "AlertR")).
2. Configure the scripts that you want to run using the configuration files in the `scripts/config/` directory.
3. Execute `start_search.py` with the `--init` argument to initialize the scripts with the `monitor_` prefix and let them establish a state of your system. However, this assumes that your system is currently uncompromised. If you are unsure of this, you should verify its current state.
4. Set up a cron job as `root` user that executes `start_search.py` (e.g., `0 * * * * root /opt/LSMS/start_search.py` to start the search hourly).

## List of Scripts

| Name | Script |
| --- | --- |
| Monitoring cron files | [monitor\_cron.py](https://github.com/sqall01/LSMS/blob/main/scripts/monitor_cron.py "monitor_cron.py") |
| Monitoring /etc/hosts file | [monitor\_hosts\_file.py](https://github.com/sqall01/LSMS/blob/main/scripts/monitor_hosts_file.py "monitor_hosts_file.py") |
| Monitoring /etc/ld.so.preload file | [monitor\_ld\_preload.py](https://github.com/sqall01/LSMS/blob/main/scripts/monitor_ld_preload.py "monitor_ld_preload.py") |
| Monitoring /etc/passwd file | [monitor\_passwd.py](https://github.com/sqall01/LSMS/blob/main/scripts/monitor_passwd.py "monitor_passwd.py") |
| Monitoring modules | [monitor\_modules.py](https://github.com/sqall01/LSMS/blob/main/scripts/monitor_modules.py "monitor_modules.py") |
| Monitoring SSH authorized\_keys files | [monitor\_ssh\_authorized\_keys.py](https://github.com/sqall01/LSMS/blob/main/scripts/monitor_ssh_authorized_keys.py "monitor_ssh_authorized_keys.py") |
| Monitoring systemd unit files | [monitor\_systemd\_units.py](https://github.com/sqall01/LSMS/blob/main/scripts/monitor_systemd_units.py "monitor_systemd_units.py") |
| Search executables in /dev/shm | [search\_dev\_shm.py](https://github.com/sqall01/LSMS/blob/main/scripts/search_dev_shm.py "search_dev_shm.py") |
| Search [fileless](https://www.kitploit.com/search/label/Fileless "fileless") programs (memfd\_create) | [search\_memfd\_create.py](https://github.com/sqall01/LSMS/blob/main/scripts/search_memfd_create.py "search_memfd_create.py") |
| Search hidden ELF files | [search\_hidden\_exe.py](https://github.com/sqall01/LSMS/blob/main/scripts/search_hidden_exe.py "search_hidden_exe.py") |
| Search immutable files | [search\_immutable\_files.py](https://github.com/sqall01/LSMS/blob/main/scripts/search_immutable_files.py "search_immutable_files.py") |
| Search kernel thread impersonations | [search\_non\_kthreads.py](https://github.com/sqall01/LSMS/blob/main/scripts/search_non_kthreads.py "search_non_kthreads.py") |
| Search processes that were started by a now disconnected SSH session | [search\_ssh\_leftover\_processes.py](https://github.com/sqall01/LSMS/blob/main/scripts/search_ssh_leftover_processes.py "search_ssh_leftover_processes.py") |
| Search running deleted programs | [search\_deleted\_exe.py](https://github.com/sqall01/LSMS/blob/main/scripts/search_deleted_exe.py "search_deleted_exe.py") |
| Test script to check if [alerting](https://www.kitploit.com/search/label/Alerting "alerting") works | [test\_alert.py](https://github.com/sqall01/LSMS/blob/main/scripts/test_alert.py "test_alert.py") |
| Verify integrity of installed .deb packages | [verify\_deb\_packages.py](https://github.com/sqall01/LSMS/blob/main/scripts/verify_deb_packages.py "verify_deb_packages.py") |

LSMS - Linux Security And Monitoring Scripts
![LSMS - Linux Security And Monitoring Scripts](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhhOUAv4hUykZ7J9MXslUWbxCDdlHdtbIiIMFSGK9cWC7UGCIY9e3NHe6DdxYtRR50ZdqSyROXW3zOdvWk0KOv1UEeXNA3OqCuSVUK1CNkgr3H9OYCM3UIFSukK_k-zf4nsXK43n30h3uePBiAHWqvanxuri0bxEHY9AWSzfakNd4mYQTxUVL4bwWJBxg/s72-w640-c-h420/h39.png)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2023/06/lsms-linux-security-and-monitoring.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)