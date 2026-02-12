---
title: 2026丹麦国情局FE - 恶猿行动 Writeup
url: https://mp.weixin.qq.com/s/4qT8rp_bL5nXPr4KvvWR1g
source: Doonsec's feed
date: 2026-02-11
fetch_date: 2026-02-12T04:18:00.044816
---

# 2026丹麦国情局FE - 恶猿行动 Writeup

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6127EssiatlpbaIvuhVFK5beTGDx4gPDdrniaSicYB6Rtmfpe2aadAS2dsMRiaeCXoe91XYib3SzibDOfCrtw5qfmYWLxTPkbdLbiawQhZEb5fegH8/0?wx_fmt=jpeg)

# 2026丹麦国情局FE - 恶猿行动 Writeup

原创

M1n9K1n9
M1n9K1n9

APT250

![]()

在小说阅读器中沉浸阅读

OPERATION BAD PRIMATE

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6127EssiatloOAl1VziaicVhzSIHo5mvFHnAbeS622K20unZ6XqeYRGiaBMAibM1KibFm6BzULZGt8Hcial6eR7t4sFhibPFxZbuEBoMT7SgPYv7wlw/640?wx_fmt=png&from=appmsg)

前言

主要关键的攻击向量与密码学、二进制有很大关系

vpn network还差最后两个二进制接管vpn network，这也直接告诉我我应该回去学习一下二进制了

后面过完春节再把它协调进我的大师计划中吧，看来二进制始终是要面对的，既然他们给我开了一个头，那我一定会做到

---

机密：相对机密

日期：2026-01-29

来源：战略关注与考量部

致：计算机网络利用部（CNE）培训

部 截止日期：2026-02-30

合作服务宣布，MonkEZ/EDO公司可能参与官方武器生产，此外还有 其官方贸易的农业和兽用饲料产品; 花园。

调查显示该公司很可能正在使用 以饲料产品为掩护，掩护非法活动。

我们需要了解公司内部的情况，包括 可访问财务报表、供应商列表及内部沟通 确认或否认怀疑。

借助人力情报线人，我们已撤离出一份旧备份 公司的服务器之一。你的任务是分析这些备份 寻找并识别可能让我们访问 公司的服务器和系统。服务器无法再有互联网，但我们可以通过人力情报（HUMINT）进行网络访问。

我们的消息来源进一步报告，自从备份文件被获取后， MonkEZ/EDO 已经更改了所有密码和 ssh 密钥。 看起来其他方面都没变。

因此，重点是找到即使更改后也能正常运行的服务器路径。

行动目标：

尽可能多地识别旧服务器备份中的漏洞， 这些数据可以用来获得对正确服务器的全部或部分访问权限。

记录如何利用已识别的漏洞 并且合并。最终目标是获得根访问权限 服务器（root@printserver）。

虚拟机部署

下载vmdk后，在vm新建虚拟机并使用这个vmdk，

请注意：在不确定该虚拟机是否200%安全之前，不要按照FE官方指示那样设置为NAT，因为设置NAT可以导致该虚拟机访问你的本地网络、互联网，除非你知道你自己在干什么，否则请设置为“仅主机”模式

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6127EssiatlqHibxheCSL9lTkO2Gdw8ia2IrPnS69kwMBgAVx1jgteVlicQt6d0FRia46oGKrrfcBqn2iaZGa8m4bibC5uN5rbPbEwVId32GXEON9c/640?wx_fmt=png&from=appmsg)

外部侦察

nmap一扫，三个ssh和一个http，

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6127EssiatlqD5p5Rc4MHuv2I0xj6iaWeubmF6zRTh1MDyhRGduQw9UMauz5XAtKujoTnmcibobm9P8srXbp7ZkR6SxUEWV5s0vWDcficdEpc8w/640?wx_fmt=png&from=appmsg)

初始访问 - 立足点

进来一个登录框，随便输入并登录后，发现提示sqlite，

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6127EssiatlpQu5vwdjrNcWuWQ4YFM1bGxmY8wRDia3PibVWMoHXqgI0zNqMAy8t2YCI5Viaeib26YkiahPHt5eoYgiax8jZlr7ZyhENIbt1MsTIYg/640?wx_fmt=png&from=appmsg)

直接上sqlmap就能出来

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6127EssiatlooVna1ia8PWPCG69ziaibx2sMjQvTac3fWOWzlbC17PmLI21ibsyDiaoR5ruaYQ2gGzvKfu6z9FVMVT3O9xqWib7Xiby6fqLpcFwGEicU/640?wx_fmt=png&from=appmsg)

dump users表后去登录，

![](https://mmbiz.qpic.cn/mmbiz_png/6127EssiatlpR2V6tEkpsOnJdGD7LJTNYiaibE31k7CgdjBic2v3ZAdGe8gicCDPAac0I6xWMI55CEyrKztJ7x0XJTsvoob69FWibDOLnw5aEMUUg/640?wx_fmt=png&from=appmsg)

拿到了ssh初始访问凭据

![](https://mmbiz.qpic.cn/mmbiz_png/6127EssiatlqOTFx3L5NPBSTHVRNUHqcdO8Nw3IdVJdzLrdcUB6oiaxwTHaY3ajkyNQU3lG6kyibt8BkmnvhzS4prIgopIAVYvm6XM4oHmDvUg/640?wx_fmt=png&from=appmsg)

直接登ssh，在docker

![](https://mmbiz.qpic.cn/mmbiz_png/6127EssiatlqeaexvtYxpXfgFWu5CPBGaqB8EZoQqiapFFa0WLaQ8qnZqa2qIq9WVF3OaJ7NIcibWCxmOQImX0ZO79BW4icHjpfLASlMQqiayvfs/640?wx_fmt=png&from=appmsg)

同时发现html注释提示至少2个漏洞

![](https://mmbiz.qpic.cn/mmbiz_png/6127Essiatlrlwsssv1KrCOkl6tWzoo076BwuPNeglT4LBdTP064HEbpeQeAC4M6eqIXPPKzvGwmWlyKqibRb61O4B4M01jFfxYe9PcoaH51Y/640?wx_fmt=png&from=appmsg)

目录扫描发现robots.txt，

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6127Essiatlo4yQzhLxKStgOcedMc49nzicfa6ibHqLZkN58zvKiapGQTIib6xyibX1Aj3mEkbA7Isaqus8GVPMQG6ATgXuG53w1DGeawgZufhVzo/640?wx_fmt=other&from=appmsg)

顺势发现路径穿越漏洞，获得一个aes加密的ssh私钥：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6127EssiatloHdpSoOS9NlFkYsp0k6P8EFMxurAyzBuys3IrshTHC6Sdt338wrzShvqotvmxXyYVVOmU3HyGFQ1iaqVpFjCnAslBGUxWoicJlI/640?wx_fmt=png&from=appmsg)

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6127EssiatlrDaP0FOM1jxylQUVEicWh4az6EQJDw4nQRUqr4fNoa4DrwRYI3AQ8ricR01sbDoTQbmu6VFEfu26ictv5szpK3C6FhJkuMpd07qQ/640?wx_fmt=other&from=appmsg)

docker逃逸

有bash\_history

![](https://mmbiz.qpic.cn/mmbiz_png/6127EssiatlppSoAOnwO2ReehXde7jwPZ8d1icEqVTzy2g363QqnfIsUWtQGZw0LrCerLw4ibPWW86aQibMkddshXmwmv5DRCiaKichLCvNhib8N0w/640?wx_fmt=png&from=appmsg)

很显然，经过尝试之后，想要访问docker，必须启用tls，

即携带客户端证书、密钥，但是它已经被删除了。

线索:

![](https://mmbiz.qpic.cn/mmbiz_png/6127EssiatlrcN6roQrZKQ6POHBYlq2Cs93agRJb5zxwpD5IRliaibmNVpI6hwd4sQL36hIO4B3MWpwBoZ3IbyicrUPPthVySdOdvdac9ncxrfk/640?wx_fmt=png&from=appmsg)

我们检查一下我们手上的东西，在hostconf/目录中：

![](https://mmbiz.qpic.cn/mmbiz_png/6127EssiatlqtGzEaL1botIPM1ygRnnVv98FTEjRYZBDbfqknlaXkmKmTg8K34okNSG0c1DOok6rPSyB2kSq7wkV1m6uANgNovz70xeZ2N6c/640?wx_fmt=png&from=appmsg)

makeCert.sh用于生成ca证书/私钥、服务器证书、客户端证书，最主要的内容:

# make CA

openssl asn1parse -genconf "key\_in\_text.txt" -out "key\_ca.der"

openssl rsa -inform DER -in key\_ca.der -out key\_ca.pem

openssl req -x509 -new -key key\_ca.pem -days 365 -sha256 -out ca.pem -config con\_ca.cnf

也就是ca key基于key\_in-text.txt的配置生成

makeKey.py主要是一个生成rsa key的脚本，但这个脚本存在漏洞，

![](https://mmbiz.qpic.cn/mmbiz_png/6127EssiatlpWay3T7M37JbhEqJ01BqAwG9t3hZholmujDmovMOQZEdfKmlsCSs3Ec83T4rkMAqfJ44GRrXjVRUEAOSQYalvX3tibtpibMBsPQ/640?wx_fmt=png&from=appmsg)

密码学不是我的强项，所以我把它交给了AI：

在 RSA 算法中，模数 $n$ 是两个素数 $p$ 和 $q$ 的乘积（$n = p \times q$）。根据算术基本定理，任何合数分解为素数乘积的形式在不计顺序的情况下是唯一的。

由于您提供的 Python 脚本逻辑中，$p$ 和 $q$ 的差值被限制在一个极小的范围内（约 1026 左右），这使得我们能够通过数学手段（费马分解法的变体）精确地锁定这对唯一的 $p$ 和 $q$。

所以根据这个漏洞，只要拿到服务器的n就能确定服务端使用的rsa私钥，恰好家目录/hostconf/目录中有ca.pem，我们从ca.pem拿到n然后结合py脚本的漏洞得到服务器使用的rsa私钥：（注意ca.pem的备份，否则运行makeCert.sh后会被覆盖

![](https://mmbiz.qpic.cn/mmbiz_png/6127Essiatlp6tJyibbgHRfyHWLvwG2I6Hohor4zCLHibbxeRpChfa4lXfUDMKia5lGL5JxWFXGL4E5eJ7c9wsLbNhpUG096lcxpvJibiaTqvL9ibk/640?wx_fmt=png&from=appmsg)

带着这个文件运行makeCert.sh就能生成合法的客户端证书和私钥，用于访问docker

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6127EssiatlrxbkOzM6Or8tjo9b6h8PZB2PCKIrProEB4VMaatU3WcOuibZzTBFWMbLAguJZCF4GliclsiccuzIibib3oEq8sOcZRR51icEJib9AjIM/640?wx_fmt=png&from=appmsg)

接着就是祖传挂载宿主机根目录，

![](https://mmbiz.qpic.cn/mmbiz_png/6127EssiatloSibhZyf8W1X2z70vvRa5797BO4n3sJwuXPOtS8wXyubT4iaTsa3qR9ic02mIF6gNibu264QYopb6gbnafics4W70rmnQJwm4w7Usw/640?wx_fmt=png&from=appmsg)

root目录中有ssh私钥、ssh服务配置，

ssh配置显示是2222端口

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6127EssiatloYr3cJlxswsuAsuAJfdBG5aNWXlyfvQowibPpVJNd3ibYLrtU6GX7aLcicmV0PeFLxNeO3BvD7ZMb1qX0gkgmwVmFAffYMlEF4c8/640?wx_fmt=png&from=appmsg)

拿到ssh私钥，没有密码，直接登2222端口ssh

![](https://mmbiz.qpic.cn/mmbiz_png/6127EssiatlrYmgf8LxnWG8kHLTr8gf0YRfpuia8qo7zfn25jLkKS5IFibBSOGIR4q9WBJOTwWhlicBP0w6KLFceWghC6kU87f7ZQLHCNUuK9HU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6127Essiatlp7XM27LdmVg2FgqFz6PBYjeJQFZu6jPia8fCIfSrWo6DicpR7rR0TibickvY4SfMU1CD5L71C2UyKyAVv2jDicABzfqic17pxeQ0E7Y/640?wx_fmt=png&from=appmsg)

内部侦察 - 核心网络

10.0.42.0/24有一台新主机

![](https://mmbiz.qpic.cn/mmbiz_png/6127EssiatlqLWREdlhye9oAVnC6CfTicVJsujSdUpOZwomhhr870VRx5icdya6luCicOhDyHepFl3t0ticMAIdSWjGJ8411Dnp7IhjwfvmS7B0Y/640?wx_fmt=png&from=appmsg)

横向移动 -> 核心网络

查看hostcontainer的bash\_history

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6127EssiatlrCcTmiaicQZWG3iaB1ricILykeIrfUgclFAQcKiauOD2G8sdPDza4yDSTSRoVmUcoIU0rNK8tzpKticZovHFPFugTGayeZEZm3hZxUg/640?wx_fmt=png&from=appmsg)

线索：

![](https://mmbiz.qpic.cn/mmbiz_png/6127EssiatlpVdib5QicQ5mko1brzGFLJrXFR0fapyQuyfib6eQJvicIZIdPUVyhvYicak57X25QTicXfMbc1LJekdh0kYnicqVv45Z0yGmNNNHQialU/640?wx_fmt=png&from=appmsg)

根据10.0.42.1的端口扫描结果看，它就是router

检查git目录:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6127EssiatlrO2aHcasuP5ic3nGlurrvh5NUwicB2YicZnLCiboa4djfd5qKqog3EJ96fcEAiaCQfhPXLAERsrkxKAkMNhs7xkBLicSgZpX5EzF6os/640?wx_fmt=png&from=appmsg)

总感觉这个存在至少两个攻击路径，但我率先发现了pwgen的密码爆破，

有一个shadow备份文件，经过对比，这个备份文件不是当前主机的，猜测应该就是router的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6127Essiatlq2jUiaibvgicvD89icvL1ckgcM3qPC3S7yTh4FSTSP0w3uks1PtQzoSTdeCDxHtEyUWvLUoLFdjA2cRE3nFpXhcEp8bsddRfCyJLM/640?wx_fmt=png&from=appmsg)

passwdGen.py使用的lcg算法存在漏洞，生成的密码范围在1677万个，

让ai写一个脚本，把这1677万个密码全部做成一个密码本，

`import string``import sys``# LCG Parameters``A = 6700419``C = 1331``M = 2**32 - 1``LCG_SEED = 0xfedd15``def get_passwords():``character_list = string.ascii_letters + string.digits + string.punctuation``num_chars = len(character_list)``max_seed = 2**24``pass_len = 16``# Pre-calculate state for seed 0``state = LCG_SEED % M``print(f"[*] Generating {max_seed} passwords...", file=sys.stderr)``# We can't easily jump seeds without the loop for the initial state``# as defined in the original script, but we can optimize the generation.``# The original script does:``# for i in range(1, seed): state = (a * sta...