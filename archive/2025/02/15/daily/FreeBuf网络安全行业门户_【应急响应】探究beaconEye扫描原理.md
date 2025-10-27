---
title: 【应急响应】探究beaconEye扫描原理
url: https://www.freebuf.com/articles/system/421791.html
source: FreeBuf网络安全行业门户
date: 2025-02-15
fetch_date: 2025-10-06T20:36:22.900335
---

# 【应急响应】探究beaconEye扫描原理

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

【应急响应】探究beaconEye扫描原理

* ![]()
* 关注

* [系统安全](https://www.freebuf.com/articles/system)

【应急响应】探究beaconEye扫描原理

2025-02-14 12:39:07

所属地 湖南省

## 项目文件解读

该项目一共分为三个部分：main.go、beaconEye以及win32。

### main.go

该文件主要是整个程序的入口文件，程序执行后会根据main文件中的执行顺序进行扫描工作。

### beaconEye

该文件夹下主要是涵盖BeaconEye所有的扫描文件，其中beaconEye.go是核心扫描代码文件。

而config.go主要是根据 ConfigShortItem结构体写的一些实现方法，我们从文件名不难看出主要是编写一些配置文件，比如内存解析后的结果配置等等。

process.go和utils.go，其实就是个工具代码文件，process.go主要是用来遍历当前系统进程，获取进程的一些相关信息.这里值得注意的是，process.go中的GetProcesses函数，返回的切片是关于正在运行状态的进程切片

```
func GetProcesses() (needScanProcesses []gops.Process, err error) {
var processes []gops.Process // 声明一个gops.Process类型的切片变量processes
processes, err = gops.Processes() // 调用gops库的Processes函数获取进程pid、ppid，并将结果赋值给processes变量
if err != nil {
return // 如果发生错误，则直接返回
}

for _, process := range processes { // 遍历processes切片
var basicInfo win32.PROCESS_BASIC_INFORMATION // 声明一个win32.PROCESS_BASIC_INFORMATION类型的变量basicInfo
var retLen win32.ULONG // 声明一个win32.ULONG类型的变量retLen
hProcess := win32.OpenProcess(win32.PROCESS_ALL_ACCESS, win32.FALSE, win32.DWORD(process.Pid())) // 调用win32库的OpenProcess函数打开进程，并将结果赋值给hProcess变量
if hProcess == 0 { // 如果hProcess为0，则表示打开进程失败，继续下一次循环
continue
}
_, err = win32.NtQueryInformationProcess(
hProcess,
win32.ProcessBasicInformation,
unsafe.Pointer(&basicInfo),
win32.ULONG(win32.SizeOfProcessBasicInformation),
&retLen,
) // 调用win32库的NtQueryInformationProcess函数获取进程的基本信息，并将结果赋值给err变量
if err != nil { // 如果发生错误，则将错误信息包装成fmt.Errorf类型，并继续下一次循环
err = fmt.Errorf("NtQueryInformationProcess error: %v", err)
continue
}
if basicInfo.ExitStatus == uintptr(win32.STATUS_PENDING) { // 如果进程的退出状态为win32.STATUS_PENDING（正在运行），则将该进程添加到needScanProcesses切片中
needScanProcesses = append(needScanProcesses, process)
}
}
return // 返回needScanProcesses切片和err变量
}
```

而utils就是个工具类，里面的函数主要是做一些常见的操作，具体如下：
UintptrListContains(list []uintptr, v uintptr) bool：检查给定的 uintptr 列表中是否包含指定的 uintptr 值。如果列表中存在该值，则返回 true，否则返回 false。
BytesIndexOf(b []byte, c byte, startIdx int) (ret int)：在字节切片 b 中查找第一个出现的字节 c 的索引位置。如果 c 不在 b 中，则返回 -1。
ReadInt64(r io.Reader) int64：从 io.Reader 中读取 8 个字节，并将其解析为一个有符号的 64 位整数（int64）。
ReadInt32(r io.Reader) int32：从 io.Reader 中读取 4 个字节，并将其解析为一个有符号的 32 位整数（int32）。
ReadInt16(r io.Reader) int16：从 io.Reader 中读取 2 个字节，并将其解析为一个有符号的 16 位整数（int16）。

## 主函数部分

主函数部分主要是先创建一个通道，用于在不同goroutine进行数据的传输，主要目的还是用来写入我们最后的扫描结果。

后面开启一个goroutine执行匿名函数，进行扫描。然后定义一个初始值count为0，用于计数当前主机有多少个C2进程，最后遍历evilResults切片，打印扫描结果，c2进程名、c2 pid以及分布在内存中的地址信息，FindEvil默认开启4个线程进行检索。

```
func main() {
fmt.Printf("%snnn", banner())
v1 := time.Now()
evilResults := make(chan beaconeye.EvilResult)
go func() {
err := beaconeye.FindEvil(evilResults, 4)
if err != nil {
panic(err)
}
}()
count := 0
for v := range evilResults {
fmt.Printf("%s (%d), Keys Found:True, Configuration Address: 0x%xn", v.Name, v.Pid, v.Address)
fmt.Printf("%sn", v.Extractor.GetConfigText())
count++
}
v2 := time.Now()
fmt.Printf("The program took %v to find out %d processesn", v2.Sub(v1), count)
}
```

## 恶意进程扫描

在FindEvil函数中。程序先获取所有的进程，并存储到一个切片里面，用于后面进行检索。

其中。searchIn 和 searchOut 是两个带缓冲的通道，分别用于输入和输出搜索任务。缓冲区大小为100。
searchIn 通道用于接收待搜索的内存块信息。
searchOut 通道用于输出搜索结果。

在进行检索的过程中，程序先后会调用GetMatchArrayAndNext->GetMatchArray->GetNext来初始化规则。方便后续在内存中进行扫描。

```
type sSearchIn struct {
procScan *ProcessScan
matchArray []uint16
nextArray []int16
memInfo win32.MemoryInfo
process gops.Process
}

var onceCloseSearchOut sync.Once

type sSearchOut struct {
procScan *ProcessScan
process gops.Process
addr uintptr
}

func FindEvil(evilResults chan EvilResult, threadNum int) (err error) {
var processes []gops.Process
processes, err = GetProcesses() //获取进程信息
if err != nil {
return
}
rule64 := "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ?? 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ?? ?? 00 00 00 00 00 00 02 00 00 00 00 00 00 00 ?? ?? ?? ?? 00 00 00 00 02 00 00 00 00 00 00 00 ?? ?? ?? ?? 00 00 00 00 01 00 00 00 00 00 00 00 ?? ?? 00 00 00 00 00 00"
rule32 := "00 00 00 00 00 00 00 00 01 00 00 00 ?? 00 00 00 01 00 00 00 ?? ?? 00 00 02 00 00 00 ?? ?? ?? ?? 02 00 00 00 ?? ?? ?? ?? 01 00 00 00 ?? ?? 00 00"
/*处理规则数组*/
matchArray64, nextArray64, err := GetMatchArrayAndNext(rule64)
if err != nil {
return
}
matchArray32, nextArray32, err := GetMatchArrayAndNext(rule32)
if err != nil {
return
}
/*处理规则数组结束*/
/*创建缓冲区大小*/
searchIn := make(chan sSearchIn, 100)
searchOut := make(chan sSearchOut, 100)

initMultiThreadSearchMemoryBlock(threadNum, searchIn, searchOut)
go handleItemFromSearchOut(searchOut, evilResults)
for _, process := range processes {
// if the process is itslef, then skip
if os.Getpid() == process.Pid() {
continue
}
processScan, err := NewProcessScan(win32.DWORD(process.Pid()))
if err != nil {
fmt.Printf("init process info error: %vn", err)
continue
}
nextArray := nextArray32
matchArray := matchArray32
if processScan.Is64Bit {
nextArray = nextArray64
matchArray = matchArray64
}
processScan.SearchMemory(matchArray, nextArray, process, searchIn)
}
close(searchIn)
return
}
```

memInfo win32.MemoryInfo
process gops.Process
}

var onceCloseSearchOut sync.Once

【ps】​ARBITRARY​​ 和 NOP​​ 是特殊标记，可能用于处理通配符匹配和无匹配情况。

```
func GetMatchArrayAndNext(rule string) (matchArray []uint16, nextArray []int16, err error) {
matchArray, err = GetMatchArray(rule)
if err != nil {
return
}
nextArray = GetNext(matchArray)
return
}

// GetMatchArray get []uint16 from string
func GetMatchArray(matchStr string) ([]uint16, error) {
codes := strings.Split(matchStr, " ")
result := make([]uint16, len(codes))
for i, c := range codes {
if c == "??" {
result[i] = ARBITRARY
} else {
bs, err := hex.DecodeString(c)
if err != nil {
return nil, err
}
result[i] = uint16(bs[0])
}
}
return result, nil
}

func GetNext(matchArray []uint16) []int16 {
//特征码（字节集）的每个字节的范围在0-255（0-FF）之间，256用来表示问号，到260是为了防止越界
next := make([]int16, 260)
for i := 0; i < len(next); i++ {
next[i] = NOP
}
for i := 0; i < len(matchArray); i++ {
next[matchArray[i]] = int16(i)
}
return next
}
```

return
}
nextArray = GetNext(matchArray)
return
}

而核心调用则是initMultiThreadSearchMemoryBlock会去调用SearchMemoryBlock，也就是说，initMultiThreadSearchMemoryBlock(threadNum, searchIn, searchOut)创建了四个SearchMemoryBlock函数用于接收并处理searchIn通道传过来的数据，处理结束后，则会将结果存储在resultArray中。

```
func initMultiThreadSearchMemoryBlock(threadNum int, searchIn chan sSearchIn, searchOut chan sSearchOut) {
for i := 0; i < threadNum; i++ {
go func() {
for item := range searchIn {
var resultArray []MatchResult
if err := SearchMemoryBlock(item.procScan.Handle, item.matchArray, uint64(item.memInfo.BaseAddress), int64(item.memInfo.RegionSize), item.nextArray, &resultArray); err != nil {
fmt.Printf("SearchMemoryBlock error: %vn", err)
continue
}
for j := range resultArray {
searchOut <- sSearchOut{
procScan: item.procScan,
process: item.process,
addr: uintptr(resultArray[j].Addr),
}
}
}
onceCloseSearchOut.Do(func() {
close(searchOut)
})
}()
}
}
```

而检索恶意进程的核心代码则是SearchMemoryBlock，采用了sunday算法实现比较，具体代码如下，该函数的作用则搜索指定进程内存块中是否存在与给定模式数组 matchArray 匹配的子串，并将匹配结果存储在 ResultArray 中。

```
func SearchMemoryBlock(hProcess win32.HANDLE, matchArray []uint16, startAddr uint64, size int64, next []int16, pResultArray *[]MatchResult) (err error) {
var memBuf []byte
memBuf,...