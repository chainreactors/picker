---
title: 如何在 Go 中构建可插拔库
url: https://cloudsjhan.github.io/2024/08/24/%E5%A6%82%E4%BD%95%E5%9C%A8-Go-%E4%B8%AD%E6%9E%84%E5%BB%BA%E5%8F%AF%E6%8F%92%E6%8B%94%E5%BA%93/
source: cloud world
date: 2024-08-25
fetch_date: 2025-10-06T18:02:12.205269
---

# 如何在 Go 中构建可插拔库

[cloud world](/)

# To be A geek

* [home](/)
* [tags](/tags/)
* [categories](/categories/)
* [archives](/archives/)
* [top](/top)
* [about](/about/)
* search

## 如何在 Go 中构建可插拔库

posted

2024-08-24

|

in

[Go](/categories/Go/)

|

visitors:

|

|

wordcount:

3,972
|

min2read ≈

20

![](https://)

## 什么是 go buildmode=plugin?

go buildmode=plugin 选项允许开发者将 Go 代码编译成共享对象文件。另一个 Go 程序可以在运行时加载该文件。当我们想在应用程序中添加新功能而又不想重建它时，这个选项非常有用。可以将新功能作为插件加载。

Go 中的插件是编译成共享对象（.so）文件的软件包。可以使用 Go 中的 [plugin package](https://pkg.go.dev/plugin "plugin package") 加载该文件，打开插件，查找符号（如函数或变量）并使用它们。

## 实践范例

这里举了了一个简单的后端演示项目的示例，它提供了一个用于计算第 n 个 斐波那契数列的 API。出于演示目的，这里特意使用了慢速斐波那契实现。考虑到计算速度较慢，我需要添加了一个缓存层来存储结果，因此如果再次请求相同的 nth 斐波那契数字，无需重新计算，只需返回缓存结果即可。

API 是 GET /fib/{n} ，其中 n 是要计算的斐波纳契数。下面我们来看看 API 是如何实现的：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 ``` | ``` // Fibonacci calculates the nth Fibonacci number. // This algorithm is not optimized and is used for demonstration purposes. func Fibonacci(n int64) int64 {  if n <= 1 {   return n  }  return Fibonacci(n-1) + Fibonacci(n-2) }  // NewHandler returns an HTTP handler that calculates the nth Fibonacci number. func NewHandler(l *slog.Logger, c cache.Cache, exp time.Duration) http.HandlerFunc {  return func(w http.ResponseWriter, r *http.Request) {   started := time.Now()   defer func() {    l.Info("request completed", "duration", time.Since(started).String())   }()    param := r.PathValue("n")   n, err := strconv.ParseInt(param, 10, 64)   if err != nil {    l.Error("cannot parse path value", "param", param, "error", err)    sendJSON(l, w, map[string]any{"error": "invalid value"}, http.StatusBadRequest)    return   }    ctx := r.Context()    result := make(chan int64)   go func() {    cached, err := c.Get(ctx, param)    if err != nil {     l.Debug("cache miss; calculating the fib(n)", "n", n, "cache_error", err)     v := Fibonacci(n)     l.Debug("fib(n) calculated", "n", n, "result", v)     if err := c.Set(ctx, param, strconv.FormatInt(v, 10), exp); err != nil {      l.Error("cannot set cache", "error", err)     }     result <- v     return    }     l.Debug("cache hit; returning the cached value", "n", n, "value", cached)    v, _ := strconv.ParseInt(cached, 10, 64)    result <- v   }()    select {   case v := <-result:    sendJSON(l, w, map[string]any{"result": v}, http.StatusOK)   case <-ctx.Done():    l.Info("request cancelled")   }  } } ``` |

代码的解释如下:

* NewHandler 函数创建一个新的 http.Handler 程序。它依赖于日志记录器、缓存和过期时间。cache.Cache 是一个接口，我们很快就会定义它。
* 返回的 http.Handler 会解析路径参数中的 n 值。如果出现错误，它会发送错误响应。否则，它会检查缓存中是否已经存在第 n 个斐波那契数字。如果没有，处理程序会计算出该数字并将其存储在缓存中，以备将来请求之用。
* goroutine 在一个单独的进程中处理斐波那契计算和缓存，而 select 语句则等待计算完成或客户端取消请求。这样可以确保在客户端取消请求时，我们不会浪费资源等待计算完成。

现在，我们希望在运行时，即应用程序启动时，可以选择缓存的实现方式。一种直接的方法是在同一代码库中创建多个实现，并使用配置来选择所需的实现。但这样做的缺点是，未选择的实现仍将是编译后二进制文件的一部分，从而增加了二进制文件的大小。虽然构建标签可能是一种解决方案，但我们将留待下一篇文章讨论。现在，我们希望在运行时而不是在构建时选择实现。这就是 buildmode=plugin 的真正优势所在。

### 确保应用程序无需插件即可运行

由于我们已将 cache.Cache 定义为一个接口，因此我们可以在任何地方创建该接口的实现，甚至可以在不同的存储库中创建。但首先，让我们来看看 Cache 接口：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 ``` | ``` package cache  import ( 	"context" 	"log/slog" 	"time" )  // consterror is a custom error type used to represent specific errors in the cache implementation. // It is derived from the int type to allow it to be used as a constant, ensuring immutability across packages. type consterror int  // Possible errors returned by the cache implementation. const ( 	ErrNotFound consterror = iota 	ErrExpired )  // _text maps consterror values to their corresponding error messages. var _text = map[consterror]string{ 	ErrNotFound: "cache: key not found", 	ErrExpired:  "cache: key expired", }  // Error implements the error interface. func (e consterror) Error() string { 	txt, ok := _text[e] 	if !ok { 		return "cache: unknown error" 	} 	return txt }  // Cache defines the interface for a cache implementation. type Cache interface { 	// Set stores a key-value pair in the cache with a specified expiration time. 	Set(ctx context.Context, key, val string, exp time.Duration) error  	// Get retrieves a value from the cache by its key. 	// Returns ErrNotFound if the key is not found. 	// Returns ErrExpired if the key has expired. 	Get(ctx context.Context, key string) (string, error) }  // Factory defines the function signature for creating a cache implementation. type Factory func(log *slog.Logger) (Cache, error)  // nopCache is a no-operation cache implementation. type nopCache int  // NopCache a singleton cache instance, which does nothing. const NopCache nopCache = 0  // Ensure that NopCache implements the Cache interface. var _ Cache = NopCache  // Set is a no-op and always returns nil. func (nopCache) Set(context.Context, string, string, time.Duration) error { return nil }  // Get always returns ErrNotFound, indicating that the key does not exist in the cache. func (nopCache) Get(context.Context, string) (string, error) { return "", ErrNotFound } ``` |

由于 NewHandler 需要依赖于 cache.Cache 实现，因此最好有一个默认实现，以确保代码不会中断。因此，让我们创建一个什么都不做的 no-op（无操作）实现。

这个NopCache实现了cache.Cache接口，但实际上并不做任何事情。它只是为了确保处理程序正常工作。
如果我们不使用任何自定义的cache.Cache实现来运行代码，API将正常工作，但结果不会被缓存–这意味着每次调用都会重新计算斐波那契数字。以下是使用NopCache（n=45）时的日志：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ``` | ``` ./bin/demo -port=8080 -log-level=debug  time=2024-08-22T17:39:06.853+07:00 level=INFO msg="application started" time=2024-08-22T17:39:06.854+07:00 level=DEBUG msg="using configuration" config="{Port:8080 LogLevel:DEBUG CacheExpiration:15s CachePluginPath: CachePluginFactoryName:Factory}" time=2024-08-22T17:39:06.854+07:00 level=INFO msg="no cache plugin configured; using nop cache" time=2024-08-22T17:39:06.854+07:00 level=INFO msg=listening addr=:8080  time=2024-08-22T17:39:19.465+07:00 level=DEBUG msg="cache miss; calculating the fib(n)" n=45 cache_error="cache: key not found" time=2024-08-22T17:39:23.246+07:00 level=DEBUG msg="fib(n) calculated" n=45 result=1134903170 time=2024-08-22T17:39:23.246+07:00 level=INFO msg="request completed" duration=3.781674792s   time=2024-08-22T17:39:26.409+07:00 level=DEBUG msg="cache miss; calculating the fib(n)" n=45 cache_error="cache: key not found" time=2024-08-22T17:39:30.222+07:00 level=DEBUG msg="fib(n) calculated" n=45 result=1134903170 time=2024-08-22T17:39:30.222+07:00 level=INFO msg="request completed" duration=3.813693s ``` |

不出所料，由于没有缓存，两次调用都需要 3 秒左右。

## 插件实现

由于我们要实现可插拔的库是 cache.Cache，因此我们需要实现该接口。您可以在任何地方实现该接口，甚至是在单独的存储库中。在本例中，我创建了两个实现：一个使用内存缓存，另一个使用 Redis，两者都在独立的存储库中。

### In-Memory Cache Plugin

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 ``` | ``` package main  import (  "context"  "log/slog"  "sync"  "time"   "github.com/josestg/yt-go-plugin/cache" )  // Value represents a cache entry. type Value struct {  Data  string  ExpAt time.Time }  // Memcache is a simple in-memory cache. type Memcache struct {  mu    sync.RWMutex  log   *slog.Logger  store map[string]Value }  // Factory is the symbol the plugin loader will try to load. It must implement the cache.Factory signature. var Factory cache.Factory = New  // New creates a new Memcache instance. func New(log *slog.Logger) (cache.Cache, error) {  log.Info("[plugin/memcache] loaded")  c := &Memcache{   mu:    sync.RWMutex{},   log:   log,   store: make(map[string]Value),  }  return c, nil }  func (m *Memcache) Set(ctx context.Context, key, val string, exp time.Duration) error {  m.log.InfoContext(ctx, "[plugin/memcache] set", "key", key, "val", val, "exp", exp)  m.mu.Lock()  m.log.DebugContext(ctx, "[plugin/memcache] lock a...