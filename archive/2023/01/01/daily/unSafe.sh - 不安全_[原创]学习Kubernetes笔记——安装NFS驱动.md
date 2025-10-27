---
title: [原创]学习Kubernetes笔记——安装NFS驱动
url: https://buaq.net/go-143568.html
source: unSafe.sh - 不安全
date: 2023-01-01
fetch_date: 2025-10-04T02:50:21.318012
---

# [原创]学习Kubernetes笔记——安装NFS驱动

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

![]()

[原创]学习Kubernetes笔记——安装NFS驱动

1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515253545
*2022-12-31 14:56:54
Author: [bbs.pediy.com(查看原文)](/jump-143568.htm)
阅读量:26
收藏*

---

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53  54  55  56  57  58  59  60  61  62  63  64  65  66  67  68  69  70  71  72  73  74  75  76  77  78  79  80  81  82  83  84  85  86  87  88  89  90  91  92  93  94  95  96  97  98  99  100  101  102  103  104  105  106  107  108  109  110  111  112  113  114  115  116  117  118  119  120  121  122  123  124  125  126  127  128 | `apiVersion: apps``/``v1`  `kind: Deployment`  `metadata:`  `name: nfs``-``client``-``provisioner`  `namespace: default`  `labels:`  `app: nfs``-``client``-``provisioner`  `spec:`  `replicas:` `1`  `strategy:`  `type``: Recreate`  `selector:`  `matchLabels:`  `app: nfs``-``client``-``provisioner`  `template:`  `metadata:`  `labels:`  `app: nfs``-``client``-``provisioner`  `spec:`  `serviceAccountName: nfs``-``client``-``provisioner`  `containers:`  `-` `name: nfs``-``client``-``provisioner`  `image: kubebiz``/``nfs``-``subdir``-``external``-``provisioner:v4.``0.2`  `volumeMounts:`  `-` `name: nfs``-``client``-``root`  `mountPath:` `/``persistentvolumes`  `env:`  `-` `name: PROVISIONER_NAME`  `value: k8s``-``sigs.io``/``nfs``-``subdir``-``external``-``provisioner`  `-` `name: NFS_SERVER`  `value:` `10.3``.``243.101`  `-` `name: NFS_PATH`  `value:` `/``data``/``nfs`  `volumes:`  `-` `name: nfs``-``client``-``root`  `nfs:`  `server:` `10.10``.``30.211`  `path:` `/``k8s`  `-``-``-`  `apiVersion: storage.k8s.io``/``v1`  `kind: StorageClass`  `metadata:`  `name: nfs``-``storage`  `annotations:`  `storageclass.kubernetes.io``/``is``-``default``-``class``:` `"true"`  `provisioner: k8s``-``sigs.io``/``nfs``-``subdir``-``external``-``provisioner`  `allowVolumeExpansion: true`  `parameters:`  `archiveOnDelete:` `"false"`  `-``-``-`  `apiVersion: v1`  `kind: ServiceAccount`  `metadata:`  `name: nfs``-``client``-``provisioner`  `namespace: default`  `-``-``-`  `apiVersion: rbac.authorization.k8s.io``/``v1`  `kind: ClusterRole`  `metadata:`  `name: nfs``-``client``-``provisioner``-``runner`  `rules:`  `-` `apiGroups: [""]`  `resources: [``"nodes"``]`  `verbs: [``"get"``,` `"list"``,` `"watch"``]`  `-` `apiGroups: [""]`  `resources: [``"persistentvolumes"``]`  `verbs: [``"get"``,` `"list"``,` `"watch"``,` `"create"``,` `"delete"``]`  `-` `apiGroups: [""]`  `resources: [``"persistentvolumeclaims"``]`  `verbs: [``"get"``,` `"list"``,` `"watch"``,` `"update"``]`  `-` `apiGroups: [``"storage.k8s.io"``]`  `resources: [``"storageclasses"``]`  `verbs: [``"get"``,` `"list"``,` `"watch"``]`  `-` `apiGroups: [""]`  `resources: [``"events"``]`  `verbs: [``"create"``,` `"update"``,` `"patch"``]`  `-``-``-`  `apiVersion: rbac.authorization.k8s.io``/``v1`  `kind: ClusterRoleBinding`  `metadata:`  `name: run``-``nfs``-``client``-``provisioner`  `subjects:`  `-` `kind: ServiceAccount`  `name: nfs``-``client``-``provisioner`  `namespace: default`  `roleRef:`  `kind: ClusterRole`  `name: nfs``-``client``-``provisioner``-``runner`  `apiGroup: rbac.authorization.k8s.io`  `-``-``-`  `kind: Role`  `apiVersion: rbac.authorization.k8s.io``/``v1`  `metadata:`  `name: leader``-``locking``-``nfs``-``client``-``provisioner`  `namespace: default`  `rules:`  `-` `apiGroups: [""]`  `resources: [``"endpoints"``]`  `verbs: [``"get"``,` `"list"``,` `"watch"``,` `"create"``,` `"update"``,` `"patch"``]`  `-``-``-`  `kind: RoleBinding`  `apiVersion: rbac.authorization.k8s.io``/``v1`  `metadata:`  `name: leader``-``locking``-``nfs``-``client``-``provisioner`  `namespace: default`  `subjects:`  `-` `kind: ServiceAccount`  `name: nfs``-``client``-``provisioner`  `namespace: default`  `roleRef:`  `kind: Role`  `name: leader``-``locking``-``nfs``-``client``-``provisioner`  `apiGroup: rbac.authorization.k8s.io` |

这里pod的运行状态一直不是Running，排查问题后发现我只在master上安装了NFS服务，需要在node节点上都安装好nfs-unitl，再查看pod发现状态为Running

文章来源: https://bbs.pediy.com/thread-275686.htm
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)