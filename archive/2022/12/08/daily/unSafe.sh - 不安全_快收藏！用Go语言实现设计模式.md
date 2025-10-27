---
title: 快收藏！用Go语言实现设计模式
url: https://buaq.net/go-139040.html
source: unSafe.sh - 不安全
date: 2022-12-08
fetch_date: 2025-10-04T00:52:12.725918
---

# 快收藏！用Go语言实现设计模式

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

![](https://8aqnet.cdn.bcebos.com/c337e765d63ed78d8533ca8349ce57ee.jpg)

快收藏！用Go语言实现设计模式

导语| 设计模式是针对软件设计中常见问题的工具箱，其中的工具就是各种经过实践验证的解决方案。即使你从未遇到过这些问题，了解模式仍然非常有用，因为它能指导你如何使用面向对象的设计原则来解决各种问题，提高
*2022-12-7 18:12:28
Author: [mp.weixin.qq.com(查看原文)](/jump-139040.htm)
阅读量:15
收藏*

---

导语| 设计模式是针对软件设计中常见问题的工具箱，其中的工具就是各种经过实践验证的解决方案。即使你从未遇到过这些问题，了解模式仍然非常有用，因为它能指导你如何使用面向对象的设计原则来解决各种问题，提高开发效率，降低开发成本；本文囊括了GO语言实现的经典设计模式示例，每个示例都精心设计，力求符合模式结构，可作为日常编码参考，同时一些常用的设计模式融入了开发实践经验总结，帮助大家在平时工作中灵活运用。

![](https://mmbiz.qpic.cn/mmbiz_jpg/VY8SELNGe94QeANounecCYXmibLibjDT9FiaZYIGick0nWJJXC1lSLI8zy2asbcicfNgvgJXexvB9rOnicPxbKFdEibPg/640?wx_fmt=jpeg)

## **(一）概念**

责任链模式是一种行为设计模式， 允许你将请求沿着处理者链进行发送。收到请求后，每个处理者均可对请求进行处理，或将其传递给链上的下个处理者。

该模式允许多个对象来对请求进行处理，而无需让发送者类与具体接收者类相耦合。链可在运行时由遵循标准处理者接口的任意处理者动态生成。

一般意义上的责任链模式是说，请求在链上流转时任何一个满足条件的节点处理完请求后就会停止流转并返回，不过还可以根据不同的业务情况做一些改进：

* 请求可以流经处理链的所有节点，不同节点会对请求做不同职责的处理；
* 可以通过上下文参数保存请求对象及上游节点的处理结果，供下游节点依赖，并进一步处理；
* 处理链可支持节点的异步处理，通过实现特定接口判断，是否需要异步处理；
* 责任链对于请求处理节点可以设置停止标志位，不是异常，是一种满足业务流转的中断；
* 责任链的拼接方式存在两种，一种是节点遍历，一个节点一个节点顺序执行；另一种是节点嵌套，内层节点嵌入在外层节点执行逻辑中，类似递归，或者“回”行结构；
* 责任链的节点嵌套拼接方式多被称为拦截器链或者过滤器链，更易于实现业务流程的切面，比如监控业务执行时长，日志输出，权限校验等；

## **（二）示例**

本示例模拟实现机场登机过程，第一步办理登机牌，第二步如果有行李，就办理托运，第三步核实身份，第四步安全检查，第五步完成登机；其中行李托运是可选的，其他步骤必选，必选步骤有任何不满足就终止登机；旅客对象作为请求参数上下文，每个步骤会根据旅客对象状态判断是否处理或流转下一个节点；

### **（三）登机过程**

```
package chainofresponsibility
import "fmt"
// BoardingProcessor 登机过程中，各节点统一处理接口type BoardingProcessor interface {  SetNextProcessor(processor BoardingProcessor)  ProcessFor(passenger *Passenger)}
// Passenger 旅客type Passenger struct {  name                  string // 姓名  hasBoardingPass       bool   // 是否办理登机牌  hasLuggage            bool   // 是否有行李需要托运  isPassIdentityCheck   bool   // 是否通过身份校验  isPassSecurityCheck   bool   // 是否通过安检  isCompleteForBoarding bool   // 是否完成登机}
// baseBoardingProcessor 登机流程处理器基类type baseBoardingProcessor struct {  // nextProcessor 下一个登机处理流程  nextProcessor BoardingProcessor}
// SetNextProcessor 基类中统一实现设置下一个处理器方法func (b *baseBoardingProcessor) SetNextProcessor(processor BoardingProcessor) {  b.nextProcessor = processor}
// ProcessFor 基类中统一实现下一个处理器流转func (b *baseBoardingProcessor) ProcessFor(passenger *Passenger) {  if b.nextProcessor != nil {    b.nextProcessor.ProcessFor(passenger)  }}
// boardingPassProcessor 办理登机牌处理器type boardingPassProcessor struct {  baseBoardingProcessor // 引用基类}
func (b *boardingPassProcessor) ProcessFor(passenger *Passenger) {  if !passenger.hasBoardingPass {    fmt.Printf("为旅客%s办理登机牌;\n", passenger.name)    passenger.hasBoardingPass = true  }  // 成功办理登机牌后，进入下一个流程处理  b.baseBoardingProcessor.ProcessFor(passenger)}
// luggageCheckInProcessor 托运行李处理器type luggageCheckInProcessor struct {  baseBoardingProcessor}
func (l *luggageCheckInProcessor) ProcessFor(passenger *Passenger) {  if !passenger.hasBoardingPass {    fmt.Printf("旅客%s未办理登机牌，不能托运行李;\n", passenger.name)    return  }  if passenger.hasLuggage {    fmt.Printf("为旅客%s办理行李托运;\n", passenger.name)  }  l.baseBoardingProcessor.ProcessFor(passenger)}
// identityCheckProcessor 校验身份处理器type identityCheckProcessor struct {  baseBoardingProcessor}
func (i *identityCheckProcessor) ProcessFor(passenger *Passenger) {  if !passenger.hasBoardingPass {    fmt.Printf("旅客%s未办理登机牌，不能办理身份校验;\n", passenger.name)    return  }  if !passenger.isPassIdentityCheck {    fmt.Printf("为旅客%s核实身份信息;\n", passenger.name)    passenger.isPassIdentityCheck = true  }  i.baseBoardingProcessor.ProcessFor(passenger)}
// securityCheckProcessor 安检处理器type securityCheckProcessor struct {  baseBoardingProcessor}
func (s *securityCheckProcessor) ProcessFor(passenger *Passenger) {  if !passenger.hasBoardingPass {    fmt.Printf("旅客%s未办理登机牌，不能进行安检;\n", passenger.name)    return  }  if !passenger.isPassSecurityCheck {    fmt.Printf("为旅客%s进行安检;\n", passenger.name)    passenger.isPassSecurityCheck = true  }  s.baseBoardingProcessor.ProcessFor(passenger)}
// completeBoardingProcessor 完成登机处理器type completeBoardingProcessor struct {  baseBoardingProcessor}
func (c *completeBoardingProcessor) ProcessFor(passenger *Passenger) {  if !passenger.hasBoardingPass ||    !passenger.isPassIdentityCheck ||    !passenger.isPassSecurityCheck {    fmt.Printf("旅客%s登机检查过程未完成，不能登机;\n", passenger.name)    return  }  passenger.isCompleteForBoarding = true  fmt.Printf("旅客%s成功登机;\n", passenger.name)}
```

### **（四）测试程序**

```
package chainofresponsibility
import "testing"
func TestChainOfResponsibility(t *testing.T) {  boardingProcessor := BuildBoardingProcessorChain()  passenger := &Passenger{    name:                  "李四",    hasBoardingPass:       false,    hasLuggage:            true,    isPassIdentityCheck:   false,    isPassSecurityCheck:   false,    isCompleteForBoarding: false,  }  boardingProcessor.ProcessFor(passenger)}
// BuildBoardingProcessorChain 构建登机流程处理链func BuildBoardingProcessorChain() BoardingProcessor {  completeBoardingNode := &completeBoardingProcessor{}
  securityCheckNode := &securityCheckProcessor{}  securityCheckNode.SetNextProcessor(completeBoardingNode)
  identityCheckNode := &identityCheckProcessor{}  identityCheckNode.SetNextProcessor(securityCheckNode)
  luggageCheckInNode := &luggageCheckInProcessor{}  luggageCheckInNode.SetNextProcessor(identityCheckNode)
  boardingPassNode := &boardingPassProcessor{}  boardingPassNode.SetNextProcessor(luggageCheckInNode)  return boardingPassNode}
```

### **（五）运行结果**

```
=== RUN   TestChainOfResponsibility为旅客李四办理登机牌;为旅客李四办理行李托运;为旅客李四核实身份信息;为旅客李四进行安检;旅客李四成功登机;--- PASS: TestChainOfResponsibility (0.00s)PASS
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/VY8SELNGe94QeANounecCYXmibLibjDT9F812pnpTVKsrLmlcKHlIuuBvuwqeIqmOLOsD9nTpkow7FlAh45LKRLA/640?wx_fmt=jpeg)

**（一）概念**

##

命令模式是一种行为设计模式，它可将请求转换为一个包含与请求相关的所有信息的独立对象。该转换让你能根据不同的请求将方法参数化、延迟请求执行或将其放入队列中，且能实现可撤销操作。

方法参数化是指将每个请求参数传入具体命令的工厂方法（go语言没有构造函数）创建命令，同时具体命令会默认设置好接受对象，这样做的好处是不管请求参数个数及类型，还是接受对象有几个，都会被封装到具体命令对象的成员字段上，并通过统一的Execute接口方法进行调用，屏蔽各个请求的差异，便于命令扩展，多命令组装，回滚等；

## **（二）示例**

控制电饭煲做饭是一个典型的命令模式的场景，电饭煲的控制面板会提供设置煮粥、蒸饭模式，及开始和停止按钮，电饭煲控制系统会根据模式的不同设置相应的火力，压强及时间等参数；煮粥，蒸饭就相当于不同的命令，开始按钮就相当命令触发器，设置好做饭模式，点击开始按钮电饭煲就开始运行，同时还支持停止命令；

### **（三）电饭煲接收器**

```
package command
import "fmt"
// ElectricCooker 电饭煲type ElectricCooker struct {  fire     string // 火力  pressure string // 压力}
// SetFire 设置火力func (e *ElectricCooker) SetFire(fire string) {  e.fire = fire}
// SetPressure 设置压力func (e *ElectricCooker) SetPressure(pressure string) {  e.pressure = pressure}
// Run 持续运行指定时间func (e *ElectricCooker) Run(duration string) string {  return fmt.Sprintf("电饭煲设置火力为%s,压力为%s,持续运行%s;", e.fire, e.pressure, duration)}
// Shutdown 停止func (e *ElectricCooker) Shutdown() string {  return "电饭煲停止运行。"}
```

**（四）电饭煲命令**

```
package command
// CookCommand 做饭指令接口type CookCommand interface {  Execute() string // 指令执行方法}
// steamRiceCommand 蒸饭指令type steamRiceCommand struct {  electricCooker *ElectricCooker // 电饭煲}
func NewSteamRiceCommand(electricCooker *ElectricCooker) *steamRiceCommand {  return &steamRiceCommand{    electricCooker: electricCooker,  }}
func (s *steamRiceCommand) Execute() string {  s.electricCooker.SetFire("中")  s.electricCooker.SetPressure("正常")  return "蒸饭:" + s.electricCooker.Run("30分钟")}
// cookCongeeCommand 煮粥指令type cookCongeeCommand struct {  electricCooker *ElectricCooker}
func NewCookCongeeCommand(electricCooker *ElectricCooker) *cookCongeeCommand {  return &cookCongeeCommand{    electricCooker: electricCooker,  }}
func (c *cookCongeeCommand) Execute() string {  c.electricCooker.SetFire("大")  c.electricCooker.SetPressure("强")  return "煮粥:" + c.electricCooker.Run("45分钟")}
// shutdownCommand 停止指令type shutdownCommand struct {  electricCooker *ElectricCooker}
func NewShutdownCommand...