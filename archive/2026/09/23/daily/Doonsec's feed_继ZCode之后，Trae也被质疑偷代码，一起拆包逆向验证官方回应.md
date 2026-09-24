---
title: 继ZCode之后，Trae也被质疑偷代码，一起拆包逆向验证官方回应
url: https://mp.weixin.qq.com/s/vI6xvY6FLfGjTJrAKiIS_Q
source: Doonsec's feed
date: 2026-09-23
fetch_date: 2026-09-24T06:58:33.555778
---

# 继ZCode之后，Trae也被质疑偷代码，一起拆包逆向验证官方回应

# 继ZCode之后，Trae也被质疑偷代码，一起拆包逆向验证官方回应

原创

佚名
佚名

星宇Sec

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

近日，字节跳动旗下AI编程工具Trae在官方论坛卷入"偷代码"风波。有用户发帖质疑Trae存在与ZCode类似的后台上传行为，称"三千个文件全部上传"，甚至有人称"上万份样本库"被传走。随后Trae官方技术人员在帖子中作出三点澄清。为核验双方说法，笔者对TraeCode与TraeWork两个安装包及其安装产物进行了完整逆向分析，逐条比对官方回应，结果显示：官方回应基本属实，当前版本中不存在ZCode式Git历史外传链路，但产品在遥测与数据链路设计上仍有值得商榷之处。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rapaL0gDxQqLrcNiahbLamjDOgCLOua1a0gdODBUmK6K7U6axpPsF8kOWsXL2Nwny71RvZqZ7p29XnnWOLq4S9ia383CM71BYL5oPBwD8W1Ag/640?wx_fmt=png&from=appmsg)

## 事件背景：ZCode上传Git历史风波

此前，AI编程工具ZCode被曝出上传用户仓库数据。安全研究人员从zcode.z.ai域名下取得凭证后，发现ZCode持续向阿里云OSS上传加密文件，解包统计显示86.6%的内容来自.git目录，包括提交历史、LFS对象与reflog。这意味着用户仓库的完整演变记录——包括已删除的旧版本文件——在用户不知情的情况下被整体搬运至云端。该事件将"AI IDE究竟在上传什么"推上舆论焦点。

## Trae遭质疑

近日，Trae官方论坛出现主题为《字节跳动 我丢雷劳莫》的帖子（https://forum.trae.cn/t/topic/182208），楼主称"刚刚ZCODE出事 现在你又偷信息，国产厂商没一个好种"。回帖中，有用户称"三千个文件全部上传"，有用户称"上万份样本库"被上传，还有用户质疑隐私模式的有效性。矛头集中指向Trae的"远程embedding"代码索引功能，怀疑其复刻ZCode的数据外传模式。

## 官方回应

针对上述质疑，Trae技术支持人员（ID:麻辣鸡腿堡）在帖子中作出三点回应：

一、所谓"远程embedding"是Trae的代码索引功能，用于让AI理解项目上下文。代码仅临时上传用于向量计算，计算完成后明文即被永久删除，云端不保留完整源码；

二、索引上传范围有严格过滤机制：依赖目录（node\_modules等）、构建产物、二进制文件、图片、音视频、压缩包均不上传；以.开头的隐藏目录（包括.git）不上传；.gitignore中列出的文件默认忽略，用户可在.trae/.ignore中自定义排除规则；单文件大小与行数设有上限；

三、隐私模式控制的是对话内容是否用于数据分析与模型训练，与代码索引功能无关。官方文档明确："无论隐私模式是否开启，TRAE绝不会将你的代码库文件用于数据分析、产品优化或模型训练。"

![](https://mmbiz.qpic.cn/mmbiz_png/rapaL0gDxQrIOBOH1XtniaVOlFPaTmswJ9oDjlDz6wq0GZJ0ibS0yOjoFR1n4x7Tsic0WwNNbnhsaseoPnczb8MhgYDd2q9o46rXYqEJ6Lue9A/640?wx_fmt=png&from=appmsg)

## 逆向分析验证

为核验上述回应，笔者对TraeCode与TraeWork两个安装包及其安装产物（Trae CN与TRAE SOLO CN）进行了分析。安装包为定制Inno Setup stub，常规解包工具失效，遂通过卸载清单unins000.dat取得完整文件列表，对安装目录内二进制逐一进行字符串提取，并实际运行程序观察进程日志。以下逐条核验。

### 一、"远程embedding"链路存在，但默认本地向量化

代码索引由ckg模块负责，对应文件为resources\app\modules\ckg\binary\libckg.dll。该二进制为Go编译，符号表未做裁剪，从中提取到的类型符号完整还原了其内部数据模型：

```
*knowledgebase.Client
*knowledgebase.Embedding
*knowledgebase.SplitFile
*knowledgebase.CodeChunk
*knowledgebase.CKGConfig
*knowledgebase.FileSegment
*knowledgebase.TextSegment
!UploadKnowledgebaseFilesBatchSize,json:"upload_knowledgebase_files_batch_size"
```

其中Embedding（向量化）、SplitFile（文件切分）、CodeChunk（代码块）等类型与官方对索引功能的描述一一对应；结构体标签upload\_knowledgebase\_files\_batch\_size则表明批量上传配置确有实现。同一二进制中提取到的远端端点字符串证实，远程上传链路在产品中真实存在：

```
/api/ide/v1/knowledgebase/upload
/api/ide/v1/knowledgebase/create
/api/ide/v1/knowledgebase/embedding_v2
/api/ide/v1/knowledgebase/files/split_files
/api/ide/v1/knowledgebase/retrieve
/api/ide/v1/knowledgebase/ckg_config
/api/ide/v1/features
/api/ide/v1/report/clients
```

但链路存在不等于默认启用。主进程main.js第911行中，ckg进程的启动参数被硬编码为本地模式：

```
String(e.defaultCkgFreePort),version_code:2,storage_path:r,local_embedding:!0,embedding_storage_type:"sqlite_vec",app_id:"6eefa01c-103...
```

实测运行后，ckg进程启动日志打印的配置为"local\_embedding":true、"embedding\_storage\_type":"sqlite\_vec"，向量库落盘路径为本机AppData\Roaming\Trae CN\ModularData\ckg\_server。在实测的3.3.104版本中，索引默认在本地完成向量化，代码明文不出本机。远程embedding模式受服务端功能开关（enable\_local\_embedding）控制，默认未启用。

### 二、过滤机制真实存在，.git目录被明确排除

libckg.dll中内嵌了完整的忽略规则检查器实现，符号表字符串如下：

```
ce/ignore_rule_checker.(*GitIgnoreRuleChecker).UpdateRulesFromTCC
ce/ignore_rule_checker.(*TCCIgnoreRuleChecker).UpdateRules
```

即.gitignore规则检查器与TCC（.trae配置）规则检查器并存，与官方所称".gitignore默认生效、支持.trae/.ignore自定义排除"一致。gitignore解析能力来自内嵌的第三方库，二进制中可见其依赖路径：

```
github.com/denormal/go-gitignore
./thirdparty/go-gitignore
```

在默认忽略列表中，二进制及媒体文件扩展名与.git、.idea等目录规则连排出现，字符串提取结果节选：

```
*.log*.map*.mid*.pdf*.pyc*.wav.git/.idea.lib//ios/...
```

另有.git/info/exclude条目。.git目录在索引模块二进制层面即被排除，这一点与ZCode事件形成关键区别——后者外传数据的86.6%恰为.git内容。索引整体数据流与过滤机制如下图所示：

![图1_ckg代码索引数据流](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQr1aWCFvPdarNEDyglBfRCOutVibVVeTup6ryPkaWmtO7ibtCp82flN9EgY72Z3KmdnylQBKFLXle1Dxics0fqQzAliaHdR4Rg6wia8/640?wx_fmt=webp&from=appmsg)

图1\_ckg代码索引数据流

### 三、隐私模式与索引无关，官方说法成立

从配置与代码看，隐私模式仅作用于对话数据是否进入训练管线，代码索引为独立链路，二者无联动。官方所称"隐私模式不豁免索引"属实，论坛中"隐私模式毛用没有"的质疑，本质是用户预期与产品设计错位：隐私模式防的是训练使用，而非索引扫描。

### 四、未发现ZCode式Git历史外传代码

针对"是否复刻ZCode"的核心质疑，笔者在两个安装目录内对git log、reflog、history相关上传路径进行了全局检索，未发现任何批量上传Git历史的代码路径。

唯一相关的上报逻辑为企业版Git AI扩展（tob-git-ai）的checkpoint上报，位于extensions\byted-icube.trae-tob-git-ai-vscode\out\contribution\checkpoint.js。该模块对上报数据做了严格裁剪：

```
const DEFAULT_LIMITS = {
    maxChanges: 200,
    maxPatchChars: 256 * 1024,
    maxTotalPatchChars: 2 * 1024 * 1024,
    maxAcceptedCodeChars: 256 * 1024,
    maxTotalAcceptedCodeChars: 2 * 1024 * 1024,
};
...
normalizedChanges.push({
    path: normalizedPath,
    patchSize,
    acceptedCodeSize,
    acceptedBlockCount: Array.isArray(change.acceptedBlocks) ? change.acceptedBlocks.length : 0,
});
...
const checkpoint = {
    repoPath,
    sessionId: payload?.sessionId,
    commit: payload?.commit,
    model: payload?.model ?? payload?.chatModel,
    changes: normalizedChanges,
};
```

可见上报字段全部为元数据——仓库路径、会话ID、提交哈希、模型名，以及每个变更的文件路径、补丁长度与接受代码字节数，不含任何代码内容；单次最多200个变更、单补丁上限256KB、总量上限2MB。

更关键的是激活门槛。该扩展的tenant-config.js对租户信息做了严格判空：

```
const account = userInfo.account;
if (account && typeof account === "object" && !Array.isArray(account)) {
    const tenantId = account.tenant_id;
    if (typeof tenantId === "string" && tenantId.trim()) {
        logger.info("tenant resolved", { tenantId });
        return tenantId.trim();
    }
}
return null;
```

即取不到account.tenant\_id时直接返回null，扩展不启用；extension.js中的运行时注释亦说明其"daemon home与投递队列数据库由启用时解析的租户ID派生"，属企业租户专属能力，个人版不加载。此外，ai-completion扩展中的gitDiff逻辑仅对当前打开文件执行git diff以获取补全上下文，与批量历史搬运无关。上报字段裁剪逻辑如下图所示：![图3：checkpoint上报字段裁剪](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQqYicz8pc0cq9HQtn7tSvFA32RyqeiaNu0aSBAVSrxDrzwYIrGQ38plrCiaaWlqRs9F3j4lb2hU5FfTFr1GWxjjMkKA4CDdxdlN70/640?wx_fmt=webp&from=appmsg)

### 五、运行时网络行为实录

静态结论之外，笔者实际运行了Trae CN并检查了进程日志。ckg进程的标准输出与静态配置完全一致：

```
"local_embedding":true
"embedding_storage_type":"sqlite_vec"
"storage_path":"C:\\Users\\Thanatos\\AppData\\Roaming\\Trae CN\\ModularData\\ckg_server"
"HttpAddr":"https://mcs.zijieapi.com"
```

即向量化在本地sqlite完成，同时该进程向DataRangers数据分析平台（mcs.zijieapi.com，AppKeys：20010662/20010768）上报统计信息——此为产品分析SDK行为，与代码内容无关。

主进程启动后立即向iCube拉取远程配置，日志中的请求URL原文如下：

```
https://api.trae.com.cn/icube/api/v1/native/config/query?mid=0c42d50480239312380d32204eded2ea46f12423e88ea9f4ce94082b1b96c300&did=1061488551026375&packageType=stable_cn&productCode=TRAE&platform=Win&arch=x64&appVersion=3.3.104...
```

同一日志中可见设备ID解析记录：

```
ICDRS] (init) resolve rdid: 1061488551026375
```

运行期网络行为总览如下图所示：

![图2：Trae运行期网络行为总览](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rapaL0gDxQo18qHuEnHSWhicx199eefEP7ZVmHygCJ7Tv15vRqJeHGX3nFtynAXGB1c50YCVYKA0LOAicViaY5ReMX01AeCOBHpC9vXibILgpAM/640?wx_fmt=webp&from=appmsg)

图2：Trae运行期网络行为总览

## 其他检查结果

签名方面，两个安装包均由DigiCert签发至北京引力弹弓科技有限公司（Trae CN运营实体），安装目录内217个二进制文件签名全部有效。卸载清单显示无捆绑软件、无开机启动项、无后台服务，仅注册trae-cn://协议处理器用于浏览器唤起IDE。

遥测配置在安装目录根部的manifest.json中明文可见，节选如下：

```
{"appId":"787976","appVersion":"3.3.104","registryUrl":"https://log.snssdk.com/service/2/desktop/device_register/","slardarDomain":"pc-mon.zijieapi.com","ahaNet":{"ttnet_params":{"domain_httpdns":"dig.bdurl.net","domain_netlog":"crash.snssdk.com","tnc_host_first":"tnc3-bjlgy.zijieapi.com","app_name":"trae"}}}
```

即设备注册（log.snssdk.com）、崩溃上报（crash.snssdk.com）、监控上报（pc-mon.zijieapi.com）、远程配置（tnc3-bjlgy.zijieapi.com）等域名均在配置中静态声明，与运行时流量互相印证。安装器亦采集SMBIOS硬件信息（debug.log含read\_smbios记录）。此类遥测属字节系产品通用方案，与"搬运Git历史"性质不同，但隐私敏感用户有理由关注。

ZCode与Trae的关键行为对比如下：

| 维度 | ZCode | Trae（实测3.3.104） |
| --- | --- | --- |
| 上传.git目录数据 | 是，占比86.6% | 否，.git/被过滤层排除 |
| 整库历史外传 | 是（历史、LFS、reflog） | 未发现对应代码路径 |
| 索引向量化位置 | — | 默认本地（sqlite\_vec） |
| 远程embedding链路 | — | 存在，默认关闭（服务端开关） |
| 上报代码内容 | 加密文件上传OSS | 无，checkpoint仅元数据 |
| 遥测链路 | — | 设备注册/崩溃/监控/分析/配置多条 |

## 结语

综合逆向结果，官方三点回应均得到证实：索引默认本地向量化，.git目录被二进制层面排除，隐私模式与索引无关；Trae当前版本中不存在ZCode式整库Git历史外传链路。但"未偷代码"不等于"无懈可击"：遥测链路繁多是客观事实，远程embedding能力受服务端开关控制，隐私模式不覆盖索引的设计易致误解。若产品方能将索引的扫描范围与数据流向做成用户可见、可关的显式设置，此类争议或可避免。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/O57ZTjAp9KOL0JJPSBRFM8Y3GwpOwWSpDSvWexu4uJ40TCnMzqRM9JQOxx8KibqwU...