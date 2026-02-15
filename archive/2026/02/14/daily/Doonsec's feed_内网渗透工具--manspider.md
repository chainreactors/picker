---
title: 内网渗透工具--manspider
url: https://mp.weixin.qq.com/s/fgF7994DRF33qLy0pXt93A
source: Doonsec's feed
date: 2026-02-14
fetch_date: 2026-02-15T04:23:18.846918
---

# 内网渗透工具--manspider

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/EYGYnyEdzQU5tX3d0Wiag05ia7EKpO8uJ6AO0o7RaSAhDyXcatsBSkeJqYxR4jL5lOAc1BhkiawxXgiczQJTFQEVuCGFp1DlNDoARoBW12CHuo8/0?wx_fmt=jpeg)

# 内网渗透工具--manspider

原创

Hello888
Hello888

安全天书

![]()

在小说阅读器中沉浸阅读

0x01 工具介绍

扫描网络SMB共享中敏感文件，支持文件内容搜索 + 正则表达式！

### 支持的文件类型：

* `PDF`
* `DOCX`
* `XLSX`
* `PPTX`
* 任何基于文本的格式
* 还有更多！！

## 使用命令：

```
usage: manspider [-h] [-u USERNAME] [-p PASSWORD] [-d DOMAIN] [-l LOOT_DIR] [-m MAXDEPTH] [-H HASH] [-k] [-aesKey HEX] [-dc-ip IP] [-t THREADS] [-f REGEX [REGEX ...]] [-e EXT [EXT ...]]                 [--exclude-extensions EXT [EXT ...]] [-c REGEX [REGEX ...]] [--sharenames SHARE [SHARE ...]] [--exclude-sharenames [SHARE ...]] [--dirnames DIR [DIR ...]]                 [--exclude-dirnames DIR [DIR ...]] [-q] [-n] [-mfail INT] [-o] [-s SIZE] [-v]                 targets [targets ...]
Scan for juicy data on SMB shares. Matching files and logs are stored in $HOME/.manspider. All filters are case-insensitive.
positional arguments:  targets               IPs, Hostnames, CIDR ranges, or files containing targets to spider (NOTE: local searching also supported, specify directory name or keyword "loot" to search                        downloaded files)
options:  -h, --help            show this help message and exit  -u, --username USERNAME                        username for authentication  -p, --password PASSWORD                        password for authentication  -d, --domain DOMAIN   domain for authentication  -l, --loot-dir LOOT_DIR                        loot directory (default ~/.manspider/)  -m, --maxdepth MAXDEPTH                        maximum depth to spider (default: 10)  -H, --hash HASH       NTLM hash for authentication  -k, --kerberos        Use Kerberos authentication. Grabs credentials from ccache file (KRB5CCNAME) based on target parameters  -aesKey, --aes-key HEX                        AES key to use for Kerberos Authentication (128 or 256 bits)  -dc-ip, --dc-ip IP    IP Address of the domain controller. If omitted it will use the domain part (FQDN) specified in the target parameter  -t, --threads THREADS                        concurrent threads (default: 5)  -f, --filenames REGEX [REGEX ...]                        filter filenames using regex (space-separated)  -e, --extensions EXT [EXT ...]                        only show filenames with these extensions (space-separated, e.g. `docx xlsx` for only word & excel docs)  --exclude-extensions EXT [EXT ...]                        ignore files with these extensions  -c, --content REGEX [REGEX ...]                        search for file content using regex (multiple supported)  --sharenames SHARE [SHARE ...]                        only search shares with these names (multiple supported)  --exclude-sharenames [SHARE ...]                        don't search shares with these names (multiple supported)  --dirnames DIR [DIR ...]                        only search directories containing these strings (multiple supported)  --exclude-dirnames DIR [DIR ...]                        don't search directories containing these strings (multiple supported)  -q, --quiet           don't display matching file content  -n, --no-download     don't download matching files  -mfail, --max-failed-logons INT                        limit failed logons  -o, --or-logic        use OR logic instead of AND (files are downloaded if filename OR extension OR content match)  -s, --max-filesize SIZE                        don't retrieve files over this size, e.g. "500K" or ".5M" (default: 10M)  -v, --verbose         show debugging messages  --modified-after DATE                        only show files modified after this date (format: YYYY-MM-DD)  --modified-before DATE                        only show files modified before this date (format: YYYY-MM-DD)
```

### ![人蛛](https://mmbiz.qpic.cn/mmbiz_png/EYGYnyEdzQVXicyVIDBdvRqibC5ledGy7FX6QlKKibGeQic1BA07hBxFnZIzev2Pa4ZNicVw6ERdr6UibIe6iasAEXdBjLXoTwjwYfdm7EGBnUuyrA/640?wx_fmt=png&from=appmsg)

GitHub地址：

```
https://github.com/blacklanternsecurity/manspider
```

注意：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。工具来自网络，安全性自测。

0x02 红蓝偶像练习生小圈子

********圈子主要研究方向渗透测试、红蓝对抗、钓鱼手法思路、武器化作，红队工具二开与免杀。圈内不定期分享红队技术文章，攻防经验总结，学习笔记以及自研工具与插件，目前圈子已满300人，欢迎各位进圈子交流学习！****

****圈子目前更新相关技术文章：**

***** HeavenlyBypassAV内部版-轻松免杀各大杀软
* Heavenly白加黑自动化生成免杀工具
* 冰蝎webshell免杀工具

* 哥斯拉webshell免杀工具
* 红队场景下lnk钓鱼Bypass国内AV
* Frp免杀隧道工具
* 1day和0dayPOC
* lnk钓鱼思路视频讲解
* lnk钓鱼Bypass天擎
* msi钓鱼
* chm钓鱼
* Kill360核晶
* AV对抗-致盲AV（核晶）
* 捆绑免杀360
* Kill火绒
* 火绒6.0内存免杀
* kill-windows Defender

* Defender分离免杀
* Defender知识点
* HeavenlyProtectionCS内部CS插件
* EDR对抗思路
* 进程注入知识点

* 自启动思路
* **多种维权手法**

* Fscan免杀核晶
* QVM解决思路
* 红队思路-钓鱼环境下小窗口截屏窃取
* 免杀Todesk/向日葵读取工具

* 渗透测试文章思路
* 内网对抗文章思路
* **还有更多红队思路文章！期待您的加入！！！************

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/EYGYnyEdzQXxP3YRhecEibkLJWZ6w0sYGTDPic4eoB6x4qVUR6NGFia4rmvObNK3C0uXWodUGZbtKhHb9pJCM6KxRfbEJyCpXgiclcnMEaktibEI/640?wx_fmt=jpeg&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=7)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/BvSCMR82FwFJAbuLxnpEkoczbwU8nmFmKaFw3zgem3QN1qrEVzBcicTB89hFKwPia7PYosgibSltTEK1h9YEhiblkA/0?wx_fmt=png)

安全天书

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/BvSCMR82FwFJAbuLxnpEkoczbwU8nmFmKaFw3zgem3QN1qrEVzBcicTB89hFKwPia7PYosgibSltTEK1h9YEhiblkA/0?wx_fmt=png)

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