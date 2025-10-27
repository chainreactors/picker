---
title: PHP使用PhpSpreadsheet读取Excel多个工作薄
url: https://buaq.net/go-169785.html
source: unSafe.sh - 不安全
date: 2023-06-22
fetch_date: 2025-10-04T11:44:19.882549
---

# PHP使用PhpSpreadsheet读取Excel多个工作薄

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

PHP使用PhpSpreadsheet读取Excel多个工作薄

PHP使用PhpSpreadsheet可以很方便读取Excel文件，包括多个工作薄的Excel.安装依赖
*2023-6-21 22:44:9
Author: [www.uedbox.com(查看原文)](/jump-169785.htm)
阅读量:16
收藏*

---

PHP使用PhpSpreadsheet可以很方便读取Excel文件，包括多个工作薄的Excel.

### 安装依赖

|  |  |
| --- | --- |
|  | composer require phpoffice/phpspreadsheet |

### 使用

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20 | use PhpOffice\PhpSpreadsheet\IOFactory;  $path = ROOT\_PATH . '/public/test.xlsx';  $reader = IOFactory::createReader('Xlsx'); // 创建读操作  $excel = $reader->load($path); // 载入excel表格  $sheets = $excel->getAllSheets();  $sheets\_count = count($sheets);  echo "共 {$sheets\_count} 个工作薄 \n";  foreach ($sheets as $sheet\_idx=>$sheet){      $sheet\_idx1 = $sheet\_idx + 1;      $rows\_count = $sheet->getHighestRow();      echo "工作薄 {$sheet\_idx1} 共 {$rows\_count} 行 \n";      for ($i = 2; $i <= $rows\_count; $i++){          $account = $sheet->getCell("G{$i}")->getValue();          $num = $sheet->getCell("I{$i}")->getValue();          $rate = $sheet->getCell("J{$i}")->getValue();          echo "工作薄 {$sheet\_idx1} {$account} {$num} {$rate} \n";      }  } |

这个示例是循环每个工作薄，获取所有行特定列的值。

### 其它用法

|  |  |
| --- | --- |
|  | //设置活跃的工作薄，下标从0开始  $excel->setActiveSheetIndex(0);  //获取活跃的工作薄  $sheet = $spreadsheet->getActiveSheet();  //获取第2列第3行单元格的值  $value = $sheet->getCellByColumnAndRow(2, 3)->getValue();  //等价于  $value = $sheet->getCell("B3")->getValue(); |

更多用法：<https://www.cnblogs.com/makalochen/p/13385758.html>

文章来源: https://www.uedbox.com/post/69054/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)