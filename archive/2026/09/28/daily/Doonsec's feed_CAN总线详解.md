---
title: CAN总线详解
url: https://mp.weixin.qq.com/s/g818U098pLSbI0SJdc0vjA
source: Doonsec's feed
date: 2026-09-28
fetch_date: 2026-09-29T07:39:55.617414
---

# CAN总线详解

# CAN总线详解

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBvgQxffuoSxCK5zHBjMe1zHgWJ84eiapLGn9OJxaSDIkr7ZxqlZePY6F37BhEGKickoLHqodK770FzBXHPlIuxyHCSicGTiaF5FP4/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247580896&idx=1&sn=36a65f68d014c79310fdeb0e1e55b6b0&scene=21#wechat_redirect)

**01**

**CAN总线基础概念**

**1.1 CAN总线简介**

控制器局域网（Controller Area Network, CAN）是由Bosch公司开发的串行通信协议，专为汽车电子和工业控制设计，具有以下核心特性：

* 多主控制架构：所有节点均可主动发送数据
* 差分信号传输：CAN\_H与CAN\_L双绞线抗干扰
* 非破坏性仲裁：基于ID优先级的冲突解决机制
* 高可靠性：CRC校验、错误帧检测等安全机制

**1.2 CAN物理层结构**

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaDbkxibbBhXG5GQLx3iaxuSudGbLlEBpMJAOGibzmcZdmRfMMDKbiab12niak2HjiaHoVWY05fib0vUOrdN5cQN5mmGWHKQrSWzzodHmY/640?wx_fmt=png&from=appmsg)

物理连接示意图：

```
|  |
| --- |
| STM32 CAN收发器 CAN总线|------| |------| |--------| | | TX ----| TXD | | CAN_H | | CAN | | |--------| | | 控制 | RX ----| RXD | | CAN_L | | 器 | |------| |--------| |------| ↑ VCC(5V) |
```

###

**02**

**STM32 CAN控制器架构**

关键效果单元

1、发送邮箱：3个独立邮箱（F1/F4系列）

* 优先级管理机制
* 自动重传特性

2、接收FIFO：2个FIFO（FIFO0/FIFO1）

* 每个FIFO深度3个报文
* 可配置溢出处理

3、过滤器组：最多28个（F4系列）

* 工作模式：掩码模式/列表模式
* 尺度选择：16位/32位

**03**

**CAN通信协议详解**

**3.1 数据帧结构**

```
|  |
| --- |
| ┌───┬───────┬──────┬───┬───────┬──────┬──────┬───┬───┐ │SOF│Arbitr.│Control│IDE│Data │ CRC │ ACK │EOF│IFS│ │1 │11/29 │6 │1 │0-64 │16 │2 │7 |3 |└───┴───────┴──────┴───┴───────┴──────┴──────┴───┴───┘ |
```

* SOF：帧起始（显性电平）
* Arbitration：ID+ RTR位（11位标准/29位扩展）
* Control：DLC（数据长度0-8字节）
* CRC：15位校验 + 1位界定符
* ACK：应答槽 + 应答界定符

**3.2 波特率配置**

计算公式：

```
|  |
| --- |
| 波特率 =APB1时钟/ (Prescaler* (BS1 + BS2 + 1 ) ) |
```

**位时间组成**：

```
|  |
| --- |
| ┌───┬──────────────┬──────────────┐ │SYNC│BS1(Prop) │ BS2(Ph2)│ ├───┼─────┬────┬───┼─────┬────┬───┤ │1│ TQ1│...│TQn│ TQ1│...│TQm│ └───┴─────┴────┴───┴─────┴────┴───┘ |
```

* SYNC\_SEG：固定1个时间量子(TQ)
* BS1：传播时间段（1-16 TQ）
* BS2：相位缓冲段2（1-8 TQ）

**04**

**STM32CubeMX配置步骤**

**4.1 基础配置流程**

1、在Pinout视图启用CAN

2、配置参数：

* Mode：Normal/Loopback
* Bit Timings：设置Prescaler/BS1/BS2

3、过滤器配置：

* Filter Activate：Enable
* Scale：32-bit/16-bit
* Mode：Mask/List

4、NVIC设置：启用接收中断

**4.2 推荐调整参数（500kbps）**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAic5jg2UKzqGzMDba7yibhz5lqnDt0kxzVUicbln6PvVGgFwGZdryTudDPWvaclEFqtQibkm7Te6RhE3QtuPXNIKzlibDzibjxzhfp4/640?wx_fmt=png&from=appmsg)

**05**

**HAL库编程实战**

#### 5.1 CAN初始化代码

```
|  |
| --- |
| CAN_HandleTypeDef hcan;CAN_FilterTypeDef filter; voidCAN_Init( void ) { hcan.Instance= CAN1; hcan.Init.Prescaler= 6 ; hcan.Init.Mode =CAN_MODE_NORMAL; hcan.Init.SyncJumpWidth=CAN_SJW_1TQ; hcan.Init.TimeSeg1=CAN_BS1_8TQ; hcan.Init.TimeSeg2=CAN_BS2_3TQ; hcan.Init.TimeTriggeredMode=DISABLE; hcan.Init.AutoBusOff=DISABLE; hcan.Init.AutoWakeUp=DISABLE; hcan.Init.AutoRetransmission=ENABLE; hcan.Init.ReceiveFifoLocked=DISABLE; hcan.Init.TransmitFifoPriority=DISABLE; if (HAL_CAN_Init(&hcan) !=HAL_OK) { Error_Handler( ) ; } // 配备过滤器（接收所有消息）filter.FilterBank= 0 ;filter.FilterMode=CAN_FILTERMODE_IDMASK;filter.FilterScale=CAN_FILTERSCALE_32BIT;filter.FilterIdHigh= 0x0000 ;filter.FilterIdLow= 0x0000 ;filter.FilterMaskIdHigh= 0x0000 ;filter.FilterMaskIdLow= 0x0000 ;filter.FilterFIFOAssignment=CAN_FILTER_FIFO0;filter.FilterActivation=ENABLE; HAL_CAN_ConfigFilter(&hcan, &filter) ; HAL_CAN_Start(&hcan) ; HAL_CAN_ActivateNotification(&hcan,CAN_IT_RX_FIFO0_MSG_PENDING) ; } |
```

#### 5.2 素材发送函数

```
|  |
| --- |
| uint8_tCAN_Send(uint32_t id, uint8_t* data, uint8_t len) {CAN_TxHeaderTypeDef txHeader; uint32_ttxMailbox;txHeader.StdId = id; // 标准IDtxHeader.ExtId = 0 ; // 扩展ID（标准帧设为0）txHeader.IDE =CAN_ID_STD; // 使用标准帧txHeader.RTR =CAN_RTR_DATA; // 数据帧txHeader.DLC = len; // 数据长度txHeader.TransmitGlobalTime=DISABLE; if(HAL_CAN_AddTxMessage(&hcan, &txHeader, data, &txMailbox) !=HAL_OK) { return 0 ; // 发送失败 } // 等待发送完成 while(HAL_CAN_GetTxMailboxesFreeLevel(&hcan) != 3 ) ; return 1 ; } |
```

#### 5.3 中断接收处理

```
|  |
| --- |
| voidHAL_CAN_RxFifo0MsgPendingCallback(CAN_HandleTypeDef*hcan) {CAN_RxHeaderTypeDef rxHeader; uint8_trxData[8] ; if(HAL_CAN_GetRxMessage(hcan,CAN_RX_FIFO0, &rxHeader,rxData) ==HAL_OK) { uint32_t id =rxHeader.StdId; // 获取标准ID uint8_t len =rxHeader.DLC; // 素材长度 // 处理接收数据 (示例: 串口转发) printf("ID:0x%X Data:" , id) ; for( int i=0 ; i<len; i++ ) { printf("%02X " ,rxData[i] ) ; } printf("\n" ) ; } } |
```

###

**06**

**调试技巧与软件**

**6.1 常见调试工具**

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCzS8eE83X6jaEZfggqzk4yCNsgAU5wiawT4hbk8LAvvW4ibI9ianYarDL6BblpbtYnfmGaBnwDTgkAqick39kxowh5w7HYdULsRuc/640?wx_fmt=png&from=appmsg)

**6.2 典型问题排查**

1、无法通信：

* 检查终端电阻（总线两端各120Ω）
* 验证波特率配置一致性
* 测量CAN\_H-CAN\_L差分电压（2V左右）

2、数据丢失：

* 增加接收FIFO深度
* 优化过滤器设置减少无关报文
* 提升中断优先级

3、总线错误：

* 使用HAL\_CAN\_GetError()获取错误码
* 否受干扰就是检查物理线路
* 降低波特率测试稳定性

**07**

**应用案例**

**7.1 汽车电子网络**

```
|  |
| --- |
| ┌──────────────┐ ┌──────────────┐ │ 发动机控制器 │◄─────►│ 车身控制模块 │ ├──────────────┤ ├──────────────┤ │ CAN总线 │◄──┐ ┌─►│ 仪表盘显示 │ └──────▲───────┘ │ │ └──────────────┘ │ ▼ ▼ ┌──────┴───────┐ ┌──────────────┐ │ 制动框架 │ │ 网关控制器 │ └──────────────┘ └──────────────┘ |
```

**7.2 工业控制系统**

最佳实践提示：在工业环境中，建议使用带隔离的CAN收发器（如ISO1050）并增加TVS管保护电路，可显著提升系统抗干扰能力。

**附录：CAN资源速查表**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaD6CIeHkUr8zm75rXpeyFeL0UhibQibWY5Ztdc6ueNJQyKu7ribCNE6AVzL2h76U284G34Fy0sic7JJg8ia2bXl462ov3YichfAdliaAA/640?wx_fmt=png&from=appmsg)

来源：

https://www.cnblogs.com/ljbguanli/p/18916660

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=appmsg)

**谈思汽车媒体门户**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9hgqzDyib0J4ico1LVFEZ2QnqGKQhnxdoZeiaZAHaGnnTnFGDvlfibtd8h389z8H20gh1icn8yhxrx8yw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyODQzMDI3Mw==&mid=2247549590&idx=1&sn=b5ea25965c057d1ca2913d900f77799d&scene=21#wechat_redirect)

**精品活动推荐**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAI8KMQg42koBCmQ8xCYRUVtiaem7dsJtOqV3DGOX6iaYEHyxflLz2KpKog3fHia0MOsJl0uRNIdyy32iaibZKpdT4LKv907eGCWcdA/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247572036&idx=3&sn=2410465a682d6b6c1f8b801eb583cdae&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaA7BGa1vwHmHNlluBv83nX42cOwngUmsgRicQ6oyhxN3HmOsFIml2sUM8Yibk5GELQqiaFLt2dVzmf01r90xrW0vMWGpJX7zOsmkM/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247575659&idx=3&sn=1b3acb3a33e0fc992b67b37bc4d04a0e&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBvgQxffuoSxCK5zHBjMe1zHgWJ84eiapLGn9OJxaSDIkr7ZxqlZePY6F37BhEGKickoLHqodK770FzBXHPlIuxyHCSicGTiaF5FP4/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247580896&idx=1&sn=36a65f68d014c79310fdeb0e1e55b6b0&scene=21#wechat_redirect)

**AutoSec系列沙龙**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkP4bDWQkLJvELA6L8vJsCRctQMTiasyhKEkb1ujgIjlGBVx91jbsQ29g/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247548574&idx=1&sn=11f37456b4f45c0fdbf795c21e201c03&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkO7zMw9U0oRCldUrRpcKyGwogwoUbpTJXic56yibibZ6Wqzr6C2P6iaFJWQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247551934&idx=2&sn=50785b76c512a88b30455fc1e8fa188c&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkVh6Z43iczWWhmnKMicdo0WU9VCzDFa2N2eiaJIogkxsLEEFt8wJ6W0CUA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247557132&idx=2&sn=2e44d4c2d77a2eec377d0553442d2c1b&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw80qwJ0DQGXJ8KiakP0yVicGI8mlMKIokicyytiaYrN6BIBOybqkYX7KSXwbia50cic232dG7BnYibKqHasA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247561775&id...