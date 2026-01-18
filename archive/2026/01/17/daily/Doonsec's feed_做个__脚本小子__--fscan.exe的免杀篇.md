---
title: 做个\"脚本小子\"--fscan.exe的免杀篇
url: https://mp.weixin.qq.com/s/sxN4YXF6Qg2NHZIVeI0dww
source: Doonsec's feed
date: 2026-01-17
fetch_date: 2026-01-18T03:33:06.696391
---

# 做个\"脚本小子\"--fscan.exe的免杀篇

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/XxjRljYHYk0SaTgP2s3YtHwwdatfIlDrweGOezXyJoF0gjibwbhvw79TxME1xYCngEANa0PQKcic9aTAeyBGLFfw/0?wx_fmt=jpeg)

# 做个"脚本小子"--fscan.exe的免杀篇

原创

lawliet
lawliet

kingman安全

![]()

在小说阅读器中沉浸阅读

声明:

由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，文章作者不为此承担任何责任。同时所有相关行为均已取得授权，未经作者同意禁止转载

文章参考:[新手如何快速做到免杀fscan](https://mp.weixin.qq.com/s?__biz=Mzg3NDc3NDQ3NA==&mid=2247484796&idx=1&sn=366ad20cf8ab3ced714d8ae7875100b2&scene=21&click_id=1#wechat_redirect)

文章有点长希望你有所收获

# 环境

win10和一台linux(就win10也可以，无所谓，命令看着转换就好)

# linux准备

```
wget https://go.dev/dl/go1.21.13.linux-amd64.tar.gz
```

```
sudo tar -C /usr/local -xzf go1.21.13.linux-amd64.tar.gz
```

```
vim ~/.zshrc
```

```
export GO111MODULE=onexport GOPATH=$HOME/goexport GOROOT=/usr/local/goexport PATH=$PATH:$GOROOT/bin:$GOPATH/binexport GOPROXY=https://goproxy.cn,directexport GOSUMDB=off
```

```
source ~/.zshrc
```

```
go install mvdan.cc/garble@v0.12.1
```

```
cp /root/go/bin/* /root/Downloads
```

如果wget不了，可以直接去下载，然后解压，可以通过

```
go env | grep GOPATH
```

确认garble位置，因为我们要将它移动到fscan里面

![](https://mmbiz.qpic.cn/mmbiz_png/XxjRljYHYk0SaTgP2s3YtHwwdatfIlDrDL7K29hSZSQaoClg7zEQCdic8apstw5RU0vGBEKmfytYRD2yyDicick2g/640?wx_fmt=png&from=appmsg)

# win准备

下载好fscan

```
git  clone https://github.com/shadow1ng/fscan.git
```

然后打开vscode

开始编辑

新建一个文件夹scan将4个功能的文件夹放进去

![](https://mmbiz.qpic.cn/mmbiz_png/XxjRljYHYk0SaTgP2s3YtHwwdatfIlDrKFDRsXfmDe9LvTfnfj2IPZ7Lmh5L9fbamuf35ibQ4NnDbFG5w6lBMKQ/640?wx_fmt=png&from=appmsg)

# 修改go.mod

![](https://mmbiz.qpic.cn/mmbiz_png/XxjRljYHYk0SaTgP2s3YtHwwdatfIlDr1SvIzcKibeRvjWGhbcu5wYTmCEIIsJtOE0rZAWCP7A0BgGYPM8iaibLmQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/XxjRljYHYk0SaTgP2s3YtHwwdatfIlDrvLomyk7EGjhP6Ueaz2OjgWmic2Td6zCbRnJDXic1HmIQg8dAXEvYkzdQ/640?wx_fmt=png&from=appmsg)

选择scan，ctrl+shift+f，搜索

```
github.com/shadow1ng/fscan
```

替换

![](https://mmbiz.qpic.cn/mmbiz_png/XxjRljYHYk0SaTgP2s3YtHwwdatfIlDrKXowqMmkhNHLcHppO3nzp9L7VvH8xdZGhHCKujn3cEEhPj9M9rHJibA/640?wx_fmt=png&from=appmsg)

再找找有哪些go文件有fscan全改掉

![](https://mmbiz.qpic.cn/mmbiz_png/XxjRljYHYk0SaTgP2s3YtHwwdatfIlDrGjEhgTHwzzbpIPcS1ga1ILElG3KZMuZKLR7QdQlHOicsg2ymunlmHpA/640?wx_fmt=png&from=appmsg)

# Cassandra.go

因为garble 混淆 Go 代码时遇到了结构体类型不匹配的编译错误

所以我们要改掉Cassandra.go文件，以下为全部

```
package Plugins
import ( "context" "fmt" "github.com/gocql/gocql" "OpsTool/scan/Common" "strconv" "strings" "sync" "time")
// =======================// 类型定义（新增，garble-safe）// =======================
// cassandraSessionResult 用于会话创建结果type cassandraSessionResult struct { session *gocql.Session err error}
// cassandraQueryResult 用于查询测试结果type cassandraQueryResult struct { success bool err error}
// =======================// 原有结构体// =======================
// CassandraCredential 表示一个Cassandra凭据type CassandraCredential struct { Username string Password string}
// CassandraScanResult 表示扫描结果type CassandraScanResult struct { Success bool IsAnonymous bool Error error Credential CassandraCredential}
// =======================// 扫描主逻辑// =======================
func CassandraScan(info *Common.HostInfo) (tmperr error) { if Common.DisableBrute { return }
 target := fmt.Sprintf("%v:%v", info.Host, info.Ports) Common.LogDebug(fmt.Sprintf("开始扫描 %s", target))
 ctx, cancel := context.WithTimeout( context.Background(), time.Duration(Common.GlobalTimeout)*time.Second, ) defer cancel()
 // 先尝试无认证 Common.LogDebug("尝试无认证访问...") anonymousCredential := CassandraCredential{} anonymousResult := tryCassandraCredential( ctx, info, anonymousCredential, Common.Timeout, Common.MaxRetries, )
 if anonymousResult.Success { saveCassandraSuccess(info, target, anonymousResult.Credential, true) return nil }
 credentials := generateCassandraCredentials( Common.Userdict["cassandra"], Common.Passwords, )
 Common.LogDebug(fmt.Sprintf( "开始尝试用户名密码组合 (用户:%d 密码:%d 组合:%d)", len(Common.Userdict["cassandra"]), len(Common.Passwords), len(credentials), ))
 result := concurrentCassandraScan( ctx, info, credentials, Common.Timeout, Common.MaxRetries, )
 if result != nil { saveCassandraSuccess(info, target, result.Credential, false) }
 return nil}
// =======================// 工具函数// =======================
func generateCassandraCredentials(users, passwords []string) []CassandraCredential { var credentials []CassandraCredential for _, user := range users { for _, pass := range passwords { actualPass := strings.Replace(pass, "{user}", user, -1) credentials = append(credentials, CassandraCredential{ Username: user, Password: actualPass, }) } } return credentials}
func concurrentCassandraScan( ctx context.Context, info *Common.HostInfo, credentials []CassandraCredential, timeoutSeconds int64, maxRetries int,) *CassandraScanResult {
 maxConcurrent := Common.ModuleThreadNum if maxConcurrent <= 0 { maxConcurrent = 10 } if maxConcurrent > len(credentials) { maxConcurrent = len(credentials) }
 var wg sync.WaitGroup resultChan := make(chan *CassandraScanResult, 1) workChan := make(chan CassandraCredential, maxConcurrent)
 scanCtx, scanCancel := context.WithCancel(ctx) defer scanCancel()
 for i := 0; i < maxConcurrent; i++ { wg.Add(1) go func() { defer wg.Done() for cred := range workChan { select { case <-scanCtx.Done(): return default: result := tryCassandraCredential( scanCtx, info, cred, timeoutSeconds, maxRetries, ) if result.Success { select { case resultChan <- result: scanCancel() default: } return } } } }() }
 go func() { for i, cred := range credentials { select { case <-scanCtx.Done(): break default: Common.LogDebug(fmt.Sprintf( "[%d/%d] 尝试: %s:%s", i+1, len(credentials), cred.Username, cred.Password, )) workChan <- cred } } close(workChan) }()
 go func() { wg.Wait() close(resultChan) }()
 select { case result := <-resultChan: return result case <-ctx.Done(): return nil }}
// =======================// 核心：连接与验证（已修复 garble 问题）// =======================
func tryCassandraCredential( ctx context.Context, info *Common.HostInfo, credential CassandraCredential, timeoutSeconds int64, maxRetries int,) *CassandraScanResult {
 var lastErr error
 for retry := 0; retry < maxRetries; retry++ { select { case <-ctx.Done(): return &CassandraScanResult{ Success: false, Error: ctx.Err(), Credential: credential, } default: connCtx, cancel := context.WithTimeout( ctx, time.Duration(timeoutSeconds)*time.Second, )
 success, err := CassandraConn( connCtx, info, credential.Username, credential.Password, ) cancel()
 if success { return &CassandraScanResult{ Success: true, IsAnonymous: credential.Username == "" && credential.Password == "", Credential: credential, } }
 lastErr = err } }
 return &CassandraScanResult{ Success: false, Error: lastErr, Credential: credential, }}
func CassandraConn( ctx context.Context, info *Common.HostInfo, user, pass string,) (bool, error) {
 cluster := gocql.NewCluster(info.Host) cluster.Port, _ = strconv.Atoi(info.Ports) cluster.Timeout = time.Duration(Common.Timeout) * time.Second cluster.ConnectTimeout = cluster.Timeout cluster.ProtoVersion = 4 cluster.Consistency = gocql.One
 if user != "" || pass != "" { cluster.Authenticator = gocql.PasswordAuthenticator{ Username: user, Password: pass, } }
 sessionChan := make(chan cassandraSessionResult, 1)
 go func() { session, err := cluster.CreateSession() select { case <-ctx.Done(): if session != nil { session.Close() } case sessionChan <- cassandraSessionResult{session, err}: } }()
 var session *gocql.Session select { case result := <-sessionChan: if result.err != nil { return false, result.err } session = result.session case <-ctx.Done(): return false, ctx.Err() }
 defer session.Close()
 queryChan := make(chan cassandraQueryResult, 1)
 go func() { var tmp string err := session.Query( "SELECT peer FROM system.peers", ).WithContext(ctx).Scan(&tmp)
 if err != nil { err = session.Query( "SELECT now() FROM system.local", ).WithContext(ctx).Scan(&tmp) }
 select { case <-ctx.Done(): case queryChan <- cassandraQueryResult{err == nil, err}: } }()
 select { case result := <-queryChan: return res...