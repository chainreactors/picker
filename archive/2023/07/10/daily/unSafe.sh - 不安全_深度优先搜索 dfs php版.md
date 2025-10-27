---
title: 深度优先搜索 dfs php版
url: https://buaq.net/go-171555.html
source: unSafe.sh - 不安全
date: 2023-07-10
fetch_date: 2025-10-04T11:51:51.268937
---

# 深度优先搜索 dfs php版

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

深度优先搜索 dfs php版

1216：红与黑【题目描述】有一间长方形的房子，地上铺了红色、黑色两种颜色的正方形瓷砖。你站在其中一块黑色的瓷砖上，只能向相邻的黑色瓷砖移动。请写一个程序，计算你总共能够到达多少块黑色的瓷
*2023-7-9 20:16:31
Author: [www.yanglong.pro(查看原文)](/jump-171555.htm)
阅读量:22
收藏*

---

1216：红与黑

【题目描述】

【输入】
包括多组数据。每组数据的第一行是两个整数W和H，分别表示x方向和y方向瓷砖的数量。W和H都不超过20。在接下来的H行中，每行包括W个字符。每个字符表示一块瓷砖的颜色，规则如下:

1）‘.’：黑色的瓷砖；

2）‘#’：白色的瓷砖；

3）‘@’：黑色的瓷砖，并且你站在这块瓷砖上。该字符在每组数据中唯一出现一次。

当在一行中读入的是两个零时，表示输入结束。

【输出】
对每组数据，分别输出一行，显示你从初始位置出发能到达的瓷砖数(记数时包括初始位置的瓷砖)。

【输入样例】
6 9
….#.
…..#
……
……
……
……
……
#@…#
.#..#.
0 0
【输出样例】
45

```
<?php

function t4(int $i, int $j): array {
    return [
        [$i + 1, $j,],
        [$i - 1, $j,],
        [$i, $j + 1,],
        [$i, $j - 1,],
    ];
}

function read($G, int $i, int $j) {
    return $G[$i][$j];
}

function inG($G, int $i, int $j): bool {
    if ($j < 0) return false;
    if (isset($G[$i][$j])) return true;
    return false;
}

function dfs($G, $i, $j, &$dp, &$count, &$map = []): void {
    $dp++;
    $map[$i][$j] = true;
    $oo = read($G, $i, $j);
    if ($oo === '.' || $oo === '@') {
        $count++;
        $mm = t4($i, $j);
        foreach ($mm as $item) {
            [$i0, $j0] = $item;
            if (!isset($map[$i0][$j0])) {
                if (inG($G, $i0, $j0)) {
                    echo str_repeat(" ", $dp);
                    echo "dfs($i0, $j0)\n";
                    dfs($G, $i0, $j0, $dp, $count, $map);
                }
            }
        }
    }
    $dp--;
}

$G = [
    '....#.',
    '.....#',
    '......',
    '......',
    '......',
    '......',
    '......',
    '#@...#',
    '.#..#.',
];

foreach ($G as $i => $item) {
    $len = strlen($item);
    for ($j = 0; $j < $len; $j++) {
        if ($item[$j] === '@') {
            break 2;
        }
    }
}

$count = 0;
$dp = 0;

dfs($G, $i, $j, $dp, $count);

var_dump($count);
```

输出：

```
php /var/www/php/test.php
 dfs(8, 1)
 dfs(6, 1)
  dfs(5, 1)
   dfs(4, 1)
    dfs(3, 1)
     dfs(2, 1)
      dfs(1, 1)
       dfs(0, 1)
        dfs(0, 2)
         dfs(1, 2)
          dfs(2, 2)
           dfs(3, 2)
            dfs(4, 2)
             dfs(5, 2)
              dfs(6, 2)
               dfs(7, 2)
                dfs(8, 2)
                 dfs(8, 3)
                  dfs(7, 3)
                   dfs(6, 3)
                    dfs(5, 3)
                     dfs(4, 3)
                      dfs(3, 3)
                       dfs(2, 3)
                        dfs(1, 3)
                         dfs(0, 3)
                          dfs(0, 4)
                         dfs(1, 4)
                          dfs(2, 4)
                           dfs(3, 4)
                            dfs(4, 4)
                             dfs(5, 4)
                              dfs(6, 4)
                               dfs(7, 4)
                                dfs(8, 4)
                                dfs(7, 5)
                               dfs(6, 5)
                                dfs(5, 5)
                                 dfs(4, 5)
                                  dfs(3, 5)
                                   dfs(2, 5)
                                    dfs(1, 5)
        dfs(0, 0)
         dfs(1, 0)
          dfs(2, 0)
           dfs(3, 0)
            dfs(4, 0)
             dfs(5, 0)
              dfs(6, 0)
               dfs(7, 0)
/var/www/php/test.php:69:
int(45)
```

文章来源: https://www.yanglong.pro/%e6%b7%b1%e5%ba%a6%e4%bc%98%e5%85%88%e6%90%9c%e7%b4%a2-dfs-php%e7%89%88/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)