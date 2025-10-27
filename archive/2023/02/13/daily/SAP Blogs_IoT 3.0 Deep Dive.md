---
title: IoT 3.0 Deep Dive
url: https://blogs.sap.com/2023/02/12/iot-3.0-deep-dive/
source: SAP Blogs
date: 2023-02-13
fetch_date: 2025-10-04T06:27:50.947399
---

# IoT 3.0 Deep Dive

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* IoT 3.0 Deep Dive

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/163297&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [IoT 3.0 Deep Dive](/t5/technology-blog-posts-by-members/iot-3-0-deep-dive/ba-p/13568791)

![architectSAP](https://avatars.profile.sap.com/6/5/id6544ac82713fdb21f40ece80ffaa37cf2c9082b9239fc96979954e809dbcc04a_small.jpeg "architectSAP")

![SAP Mentor](/html/@F4C200E47DAE3459A6BD3FBB7F9955B8/rank_icons/mentor-rank-16x16.svg "SAP Mentor")
[architectSAP](https://community.sap.com/t5/user/viewprofilepage/user-id/207)

SAP Mentor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=163297)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/163297)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13568791)

‎2023 Feb 12
6:24 PM

[1
Kudo](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/163297/tab/all-users "Click here to see who gave kudos to this post.")

1,045

* SAP Managed Tags
* [Blockchain](https://community.sap.com/t5/c-khhcw49343/Blockchain/pd-p/774381146224104075682835994387196)

* [Blockchain

  Topic](/t5/c-khhcw49343/Blockchain/pd-p/774381146224104075682835994387196)

View products (1)

In my last blog [IoT 3.0](https://blogs.sap.com/2023/01/03/iot-3.0/), I demonstrated the difference between sending IoT data to a central database versus to a distributed ledger. To do so, I leveraged [Duino IoT](https://github.com/revoxhere/duino-coin/wiki/Duino%27s-take-on-the-Internet-of-Things) that is a feature of [Duino-Coin](https://github.com/revoxhere/duino-coin), a hybrid crypto currency.

In this blog, I will look under the covers how this works and deploy IoT data via [Apache Kafka](https://kafka.apache.org/) to my own local blockchain as follows:

1. Install Microsoft [Visual Studio Code](https://code.visualstudio.com/Download).

2. Install Microsoft [Windows Subsystem for Linux](https://learn.microsoft.com/en-us/windows/wsl/install).

3. Install [Node.js](https://nodejs.org/en/).

4. Install [Hardhat](https://hardhat.org/).

5. Deploy smart contract.

6. Send IoT data to local blockchain.

7. Read IoT Data from local blockchain.

## Install Visual Studio Code.

Microsoft Visual Studio Code could not be easier to install and comes in editions for macOS, Windows x64 and Linux x64. It supports many programming languages, among these, for this blog, [Solidity](https://soliditylang.org/) and [TypeScript](https://www.typescriptlang.org/).

## Install the Microsoft Windows Subsystem for Linux.

I work on Microsoft Windows, but if you work on macOS or Linux, you can omit this step.

```
wsl –install
```

## Install Node.js

Since I need [Node.js](https://nodejs.org/en/) as my TypeScript runtime, I install it with the [Node Version Manager](https://github.com/nvm-sh/nvm).

```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash

nvm install node
```

## Install Hardhat.

[Hardhat](https://hardhat.org/) is a development environment for Ethereum software that I leverage for this blog.

```
npm install --save-dev hardhat

mkdir raspi

cd raspi

yarn hardhat init
```

## Deploy smart contract.

My smart contract is very simple with a read and set function.

```
// SPDX-License-Identifier: MIT

pragma solidity ^0.8.17;

contract Raspi {

    int public pressure;

    function read() public view returns (int) {

        return pressure;

    }

    function set(int _pressure) public {

        pressure = _pressure;

    }

}
```

After compiling, it is ready for deployment.

```
yarn hardhat compile
```

In preparation for deployment, I start a local HTTP and WebSocket JSON-RPC server.

```
yarn hardhat node

yarn run v1.22.19

$ /home/architectSAP/raspi/node_modules/.bin/hardhat node

Started HTTP and WebSocket JSON-RPC server at http://127.0.0.1:8545/
```

And add it to hardhat.config.ts.

```
import { HardhatUserConfig } from "hardhat/config";

import "@nomicfoundation/hardhat-toolbox";

const config: HardhatUserConfig = {

  solidity: "0.8.17",

  networks: {

    localhost: {

      url: "http://127.0.0.1:8545/",

      chainId: 31337,

    },

  },

};

export default config;
```

Deployment is via TypeScript and provides me with its address.

```
import { ethers } from "hardhat";

async function main() {

  const Lock = await ethers.getContractFactory("Raspi");

  const lock = await Lock.deploy();

  await lock.deployed();

  console.log(`${lock.address}`);

}

main().catch((error) => {

  console.error(error);

  process.exitCode = 1;

});
```

```
yarn hardhat run scripts/raspi.ts --network localhost

yarn run v1.22.19

$ /home/architectSAP/raspi/node_modules/.bin/hardhat run scripts/raspi.ts --network localhost

0x5FbDB2315678afecb367f032d93F642f64180aa3
```

I also see that Contract deployment: Raspi is the first block in my local blockchain and how much Gas it used.

```
  Contract deployment: Raspi

  Contract address:    0x5fbdb2315678afecb367f032d93f642f64180aa3

  Transaction:         0xbd67c6963243a392ecce06e8c3baefd469295f6adb1212fd09907f26756404bc

  From:                0xf39fd6e51aad88f6f4ce6ab8827279cfffb92266

  Value:               0 ETH

  Gas used:            135811 of 135811

  Block #1:            0x5a30a5ae9cbf37838660c4ee41b3df457f7d840b1f6181cdcd1ee4f238e25d93
```

## Send IoT data to local blockchain.

Given my smart contract address, I sent my IoT data to it via [Apache Kafka](https://kafka.apache.org/).

```
import { Kafka } from "kafkajs"

import { ethers } from "hardhat"

const kafka = new Kafka({

    brokers: ["your.kafka.server:9092"],

    clientId: "goerli",

})

const consumer = kafka.consumer({ groupId: "raspi" })

const contractAddress = "0x5fbdb2315678afecb367f032d93f642f64180aa3"

const raspi = async () => {

    const raspi = await ethers.getContractAt("Raspi", contractAddress)

    await consumer.connect()

    await consumer.subscribe({ topic: "bme680", fromBeginning: true })

    await consumer.run({

        eachMessage: async ({ topic, partition, message }) => {

            const obj = JSON.parse(message.value as unknown as string)[0]

            console.log({ pressure: obj.pressure, millis: obj.millis })

            await raspi.set((obj.pressure * 100).toFixed(0))

        },

    })

}

raspi().catch((e) => console.error(e))
```

```
yarn hardhat run scripts/set.ts --network localhost

yarn run v1.22.19

$ /home/architectSAP/raspi/node_modules/.bin/hardhat run scripts/set.ts --network localhost

{"level":"INFO","timestamp":"2023-02-11T00:49:53.156Z","logger":"kafkajs","message":"[Consumer] Starting","groupId":"raspi"}

{"level":"INFO","timestamp":"2023-02-11T00:49:57.886Z","logger":"kafkajs","message":"[ConsumerGroup] Consumer has joined the group","groupId":"raspi","memberId":"goerli-d802a384-618e-4d3a-a241-2105df0d1cf1","leaderId":"goerli-d802a384-618e-4d3a-a241-2105df0d1cf1","isLeader":true,"memberAssignment":{"bme680":[0]},"groupProtocol":"RoundRobinAssigner","duration":4727}

{ pressure: 1030.84, millis: '2023-02-12 19:35:01.900606'...