---
title: 吾爱破解2025春节红包活动番外篇第三题
url: https://fuping.site/2025/02/12/52pj-web03-2025/
source: 浮萍's Blog
date: 2025-02-13
fetch_date: 2025-10-06T20:34:59.402203
---

# 吾爱破解2025春节红包活动番外篇第三题

[![logo](/favicon.png)](/)

* [主页](/)
* [所有文章](/archives/)
* [标签](/tags)
* [关于](/about)
* [RSS](/atom.xml)

# 吾爱破解2025春节红包活动番外篇第三题

Feb 12, 2025[#CTF](/categories/CTF/)

## 0x00 前言

番外篇第三题刚开始是有难度的，玩家会相互干扰，想要获取flag，还是需要靠一点运气的。后面修改了难度，分 IP 抽奖，互相不干扰了。难度就降低了不少。

## 0x01 分析

第三题是抽奖的，地址：<https://2025challenge.52pojie.cn/lottery.html> ，看一下题目。

![要求](01.png)

抽奖算法也给出了

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` blockNumber=$(curl -s -H 'Content-type: application/json' --data-raw '{"body":{}}' 'https://api.upowerchain.com/apis/v1alpha1/statistics/overview' | jq -r '.blockHeight') blockHash=$(curl -s -H 'Content-type: application/json' --data-raw '{"number":"'$blockNumber'"}' 'https://api.upowerchain.com/apis/v1alpha1/block/get' | jq -r '.data.blockHash') userCount=10001 userIndex=$(python -c "print($blockHash % $userCount)") echo $userIndex ``` |

以之前中奖的为例，`blockNumber=29443498`，可以看到

`blockHash=0xed10c6b62d163279cfff03e39a8017e303a03d48a6a314d24c47596b998ae30b`

参与抽奖人数是10071

![案例](02.png)

那么我们可以通过计算，获取中奖人的序号

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` blockHash = 0xed10c6b62d163279cfff03e39a8017e303a03d48a6a314d24c47596b998ae30b userCount=10071 print(blockHash % userCount) ``` |

验证结果是3000。

`blockNumber`在每次开奖前也给出了，那么可以根据`blockNumber`请求API获取`blockHash`。知道`blockHash`后，如果可以控制参与抽奖的人数，那么获奖人员的编号也能够确定了。

所以之前的难度是比较大的，都是真人玩家，不好确定参与人数和位置。后面降低了难度，分IP抽奖，互不干扰。

另外需要注意的是，每次抽奖系统会自动添加 9980 个机器人，所以如果参与抽奖的话，编号是从9980开始的。因此需要找到中奖序号大于等于9980的，才能保证自己中奖。而且满10000人才开奖，所以还要添加虚假的UID，来凑人数。

## 0x02 解题

> 由于现在答题地址下线，所以以之前已开奖的来模拟答题。找到一个中奖序号大于等于9980的blockNumber。

![案例](03.png)

这里的blockNumber为29439513，假如参与抽奖的人数是10000-10300，主要代码

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 ``` | ``` async function findWinningUserCount(blockNumber) {         try {             // 获取指定区块的哈希             const r = await fetch('https://api.upowerchain.com/apis/v1alpha1/block/get', {                 method: 'POST',                 headers: {'Content-Type': 'application/json'},                 body: JSON.stringify({"number": blockNumber.toString()})             });             const data = await r.json();             console.log("\n=== API响应 ===");             console.log(JSON.stringify(data, null, 2));                          if (!data || !data.data || !data.data.blockHash) {                 console.error("无效的API响应:", data);                 return null;             }                          const hash = data.data.blockHash;             const hashWithPrefix = hash.startsWith('0x') ? hash : '0x' + hash;             console.log(`\n区块哈希: ${hashWithPrefix}`);             //从10000开始尝试不同的userCount             for (let userCount = 10000; userCount <= 10300; userCount++) {                 const result = BigInt(hashWithPrefix) % BigInt(userCount);                                  if(result >= 9980n) {                     const position = Number(result - 9980n);                     console.log(`\n!!! FOUND WINNING COMBINATION !!!`);                     console.log(`Block: ${blockNumber}`);                     console.log(`Hash: ${hashWithPrefix}`);                     console.log(`User Count: ${userCount}`);                     console.log(`Absolute Position: ${result}`);                     console.log(`Relative Position: ${position}\n`);                     return {position, userCount};                 }             }                          console.log("\n没有找到合适的参与人数组合");             return null;         } catch(e) {             console.error(`\n[错误] 检查区块 ${blockNumber} 失败:`);             console.error("错误详情:", e);             console.error("错误堆栈:", e.stack);             return null;         }     } const blockNumber = 29439513 const result = await findWinningUserCount(blockNumber); ``` |

![寻找](05.png)

根据计算的结果，答题人需要有10201个，中奖的序号是10067，实际位置是第87。剩余的位置都添加虚假的UID。

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 ``` | ``` async function joinMultiple() {     let timestamp = Math.floor(Date.now() / 1000);     let code = await getVerifyCode(timestamp.toString() + "|");          // 需要221个UID (10201 - 9980 = 221)     const uids = [];          // 生成221个UID，确保自己的UID在第87位     for(let i = 0; i < 221; i++) {         if(i === 87) {             uids.push("你的UID");  // 中奖位置         } else {             uids.push((200000 + i).toString());  // 其他位置用虚假UID         }     }          console.log(`\n=== 开始提交抽奖请求 ===`);     console.log(`时间戳: ${timestamp}`);     console.log(`总UID数量: ${uids.length}`);     console.log(`你的位置: 87\n`);          for(let uid of uids) {         try {             let response = await fetch('https://2025challenge.52pojie.cn/api/lottery/join', {                 method: 'POST',                 headers: {'Content-Type': 'application/json'},                 body: JSON.stringify({                     "timestamp": timestamp,                     "uid": uid,                     "verify_code": code                 })             });             const textResponse = await response.text();             try {                 console.log(`UID ${uid}:`, JSON.parse(textResponse));             } catch(e) {                 console.log(`UID ${uid}:`, textResponse);             }             await new Promise(r => setTimeout(r, 100));  // 添加延迟避免请求过快         } catch(e) {             console.error(`Error submitting UID ${uid}:`, e.message);         }     }          console.log("\n=== 提交完成 ==="); }  joinMultiple(); ``` |

然后就等开奖即可。这里之所以和实际不一样，是因为参与人数不一样也会导致中奖的序号不一样的。

例如我们将参与人数变动一下，范围为10230-10300，得出的中奖序号是一样的。

![寻找](06.png)

## 0x03 更新（02-14）

今天发现题目又可以打开了，再来做一次题，当前blockNum为29550216

![查看blockNum](07.png)

当然在实际做题过程中，不是手动来获取blockNum的，因为不是每一次抽奖的序号都大于9980。所以通过接口获取当前要开奖的blockNum，通过计算如果中奖序号大于9980，则继续，否则等待下一次抽奖。

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``` | ``` async function getLotteryInfo() {     const r = await fetch('https://2025challenge.52pojie.cn/api/lottery/history');     const data = await r.json();     return data.data.history[0];  // 获取最新一条记录 } ... // 获取开奖区块号 const lotteryInfo = await getLotteryInfo(); const blockNumber = lotteryInfo.block_number; console.log(`\n开奖区块号: ${blockNumber}`);  // 寻找合适的参与人数 const result = await findWinningUserCount(blockNumber); if(result) {     const nextLotteryTime = getNextLotteryTime();     const submitTime = Math.floor(nextLotteryTime.getTime() / 1000);     await submitEntries(result, submitTime); } else {     console.log("\n未找到合适的参与人数组合"); } ``` |

根据blockNum获取blockHash

![获取blockHash](08.png)

计算出来人数和位置后，修改代码进行提交，主要代码

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ``` | ``` ... const count = 10063 - 9980; const pos = 44; const uids = [];   for(let i = 0; i < count; i++) {     if(i === pos) {         uids.push("88888");  // 模拟UID为88888     } else {         uids.push((200000 + i).toString());  // 其他位置用虚假UID     } } let timestamp = Math.floor(Date.now() / 1000); let code = await getVerifyCode(timestamp.toString() + "|");  console.log(`\n=== 开始提交抽奖请求 ===`); console.log(`时间戳: ${timestamp}`); console.log(`总UID数量: ${uids.length}`); console.log(`你的位置: ${pos}\n`); ... ``` |

提交数据要注意两点：一是速率不要太快、太多，否则会被拦截；二是需要在一分钟内提交（当前的代码），否则验证不通过，需要重新获取时间戳和VerifyCode。可以继续优化代码，这里为了演示成功，找了一个需要提交人数不是那么多的情况。

![参与抽奖](09.png)

时间到了查看中奖结果

![中奖结果查看](10.png)

可以看到成功中奖。

## 0x04总结

这道题的解题思路比较清晰：通过分析抽奖算法，发现中奖序号是由区块哈希值对参与总人数取模得到的。系统会自动添加 9980 个机器人账号，真实玩家的序号从 9980 开始。在后期分 IP 抽奖的调整下，不同 IP 之间互不干扰，这让解题变得更加可控。

解题步骤主要是：首先通过 API 获取指定区块的哈希值，然后遍历可能的参与总人数（比如 10000-10300），找到一个合适的总人数，使得计算出的中奖序号大于等于 9980。确定好参与总人数后，计算出自己需要在机器人之后的第几个位置（中奖序号减去 9980），然后将自己的 UID 放在这个位置，其他位置用虚假 UID 填充。最后等待开奖即可获得 flag。

[#52破解](/tags/52%E7%A0%B4%E8%A7%A3/)[#CTF](/tags/CTF/)[#writeup](/tags/writeup/)

[下一篇](/2025/01/15/fakelocatioin-fix-journey/)

© 2016 - 2025 [浮萍](https://fuping.site).