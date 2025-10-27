---
title: Dissecting the Bybit Cryptocurrency Exchange Malicious UI Spoofing Javascript
url: https://ddanchev.blogspot.com/2025/02/dissecting-bybit-cryptocurrency.html
source: Dancho Danchev's Blog - Mind Streams of Information Security Knowledge
date: 2025-02-27
fetch_date: 2025-10-06T20:35:54.201289
---

# Dissecting the Bybit Cryptocurrency Exchange Malicious UI Spoofing Javascript

# [Dancho Danchev's Blog - Mind Streams of Information Security Knowledge](https://ddanchev.blogspot.com/)

Independent Contractor. Bitcoin: 15Zvie1j8CjSR52doVSZSjctCDSx3pDjKZ Email: dancho.danchev@hush.com OMEMO: ddanchev@conversations.im | OTR: danchodanchev@xmpp.jp | TOX ID: 53B409440A6DC34F1BA458869A0462D92C15B467AF6319D481CA353690C88667833A0EE82969

## Wednesday, February 26, 2025

### Dissecting the Bybit Cryptocurrency Exchange Malicious UI Spoofing Javascript

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh3mrFxe_0lPQtvGTPyek8Gxhdo02PCsQ8i1Qp9VEIvAmr_Y2FeOZZO5TV3oPfqMcpptRhgP4ui0nJpkireGaB26ksSlBZSUq9J0RwN3joTF3eXYpGX1WL7mu0XJZQEJ2vdXUyv0fKnffyLLxj7BCQcun1K3zuc5J4ppToPa_AiG-huG3kLDYIW/s320/Bybit_Malicious_Javascript_Ethereum_Addressess_01.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh3mrFxe_0lPQtvGTPyek8Gxhdo02PCsQ8i1Qp9VEIvAmr_Y2FeOZZO5TV3oPfqMcpptRhgP4ui0nJpkireGaB26ksSlBZSUq9J0RwN3joTF3eXYpGX1WL7mu0XJZQEJ2vdXUyv0fKnffyLLxj7BCQcun1K3zuc5J4ppToPa_AiG-huG3kLDYIW/s807/Bybit_Malicious_Javascript_Ethereum_Addressess_01.jpg)

Based on the recently released [Bybit Investigation](https://docsend.com/view/s/rmdi832mpt8u93s7) documents I was able to obtain the malicious javascript in question and I decided to dig a little bit deeper into its inner workings and try to provide actionable intelligence on the topic and who the malicious attackers might be.

**Javascript MD5:** [be9397a0b6f01d21e15c70c4b37487fe](https://www.virustotal.com/gui/file/fbd5e3eb17ef62f2ecf7890108a3af9bcc229aaa51820a6e5ec08a56864d864d/detection)

What I did was the following. I managed to partly reproduce the campaign and while looking for clues I managed to obtain an actual copy of the Bybit cryptocurrency exchange malicious UI spoofing javascript.

What I did next as the script was logically not obfuscated was to look for additional clues such as for instance phone back URLs or Ethereum addresses which I did with a lot of success which I decided to share with everyone.

**Full list of URLs found in the malicious Bybit cryptocurrency exchange malicious UI spoofing javascript:**

hxxp://fb.me/use-check-prop-types
hxxp://hxxp://example.com
hxxp://hxxp://w3.org/2000/svg
hxxp://12cd7127f9cfb1cddab1f354252074b7@o4507209696739328.ingest.de.sentry.io/4507215200256080
hxxp://abitype.dev
hxxp://api.arbiscan.io
hxxp://api.basescan.org
hxxp://api.bscscan.com
hxxp://api.etherscan.io
hxxp://api.polygonscan.com
hxxp://api.spindl.xyz/v1
hxxp://api-amoy.polygonscan.com
hxxp://api-goerli.arbiscan.io
hxxp://api-goerli.etherscan.io
hxxp://api-goerli-optimistic.etherscan.io
hxxp://api-holesky.etherscan.io
hxxp://api-optimistic.etherscan.io
hxxp://api-sepolia.basescan.org
hxxp://api-sepolia.etherscan.io
hxxp://api-testnet.bscscan.com
hxxp://api-testnet.polygonscan.com
hxxp://app.getbeamer.com/js/beamer-embed.js
hxxp://app.safe.global/images/social-share.png
hxxp://beaconcha.in
hxxp://bit.ly/3cXEKWf
hxxp://chat.safe.global
hxxp://client.blockaid.io
hxxp://cloudflare-eth.com/
hxxp://community.safe.global
hxxp://developer.mozilla.org/en-US/docs/Web/API/File\_System\_Access\_API
hxxp://developer.mozilla.org/en-US/docs/Web/HTTP/Basics\_of\_HTTP/MIME\_types/Common\_types
hxxp://docs.ethers.org/api-keys/
hxxp://docs.soliditylang.org/en/latest/cheatsheet.html
hxxp://fcmregistrations.googleapis.com/v1/projects/
hxxp://firebaseinstallations.googleapis.com/v1/projects/
hxxp://gasstation.polygon.technology/v2
hxxp://gasstation-testnet.polygon.technology/v2
hxxp://gateway.ipfs.io/ipfs/
hxxp://github.com/5afe/safe-cli
hxxp://github.com/date-fns/date-fns/blob/master/docs/unicodeTokens.md
hxxp://github.com/date-fns/date-fns/blob/master/docs/upgradeGuide.md#string-arguments
hxxp://github.com/ethers-io/ethers.js/issues/4537
hxxp://github.com/safe-global/safe-wallet-web
hxxp://help.safe.global
hxxp://help.safe.global/en/articles/145503-how-to-create-a-safe-app-with-safe-apps-sdk-and-list-it
hxxp://holesky.beaconcha.in
hxxp://links.ethers.org/v5-errors-
hxxp://mui.com/production-error/?code=
hxxp://nextjs.org/docs/app/api-reference/functions/unstable\_cache
hxxp://nextjs.org/docs/app/api-reference/functions/use-search-params#updating-searchparams
hxxp://nextjs.org/docs/app/building-your-application/rendering/static-and-dynamic#dynamic-rendering
hxxp://nextjs.org/docs/messages/dynamic-server-error
hxxp://nextjs.org/docs/messages/next-dynamic-api-wrong-context
hxxp://nextjs.org/docs/messages/next-prerender-missing-suspense
hxxp://nextjs.org/docs/messages/next-request-in-use-cache
hxxp://nextjs.org/docs/messages/ppr-caught-error
hxxp://noteforms.com/forms/safe-feedback-form-hk16ds?notionforms=1&utm\_source=notionforms
hxxp://npms.io/search?q=ponyfill
hxxp://polygon-rpc.com/
hxxp://redux.js.org/Errors?code=
hxxp://redux-toolkit.js.org/Errors?code=
hxxp://relay.gelato.digital/tasks/status
hxxp://rpc-amoy.polygon.technology/
hxxp://rsms.me/inter/font-files/InterVariable.woff2
hxxp://safe.mirror.xyz/rInLWZwD\_sf7enjoFerj6FIzCYmVMGrrV8Nhg4THdwI
hxxp://safe.widget.kiln.fi/overview
hxxp://safe.widget.testnet.kiln.fi/overview
hxxp://safe-claiming-app-data.safe.global/allocations/
hxxp://safe-claiming-app-data.staging.5afe.dev/allocations/
hxxp://safe-client.safe.global
hxxp://safe-client.staging.5afe.dev
hxxp://safe-dao-governance.dev.5afe.dev
hxxp://safe-firebase-mainnet.firebaseio.com
hxxp://sentry.io
hxxp://simulation.safe.global
hxxp://spindl.link
hxxp://ssl.google-analytics.com
hxxp://status.safe.global
hxxp://third-party-cookies-check.gnosis-safe.com
hxxp://viem.sh
hxxp://hxxp://google-analytics.com
hxxp://hxxp://googletagmanager.com
hxxp://hxxp://googletagmanager.com/gtm.js?id=

**Sample Ethereum addresses found in the malicious Bybit cryptocurrency exchange malicious UI spoofing javascript:**

0x0100004124426fb9ebb25e27d670c068e52f9ba6
0x017062a1dE2FE6b99BE3d9d37841FeD19F573804
0x017e9a83d5513f503fb85274f4d1ad1811040d7c
0x0208282bd262360d0320862c5ac70f375f5ed3b9
0x03e69f7ce809e81687c69b19a7d7cca45b6d551f
0x064ddbf252714bcd4cb79f679e8c12df96d998ce
0x0a7CB434f96f65972D46A5c1A64a9654dC9959b2
0x0dFcccB95225ffB03c6FBB2559B530C2B7C8A912
0x0e4f7fc66550a322d1e7688e181b75e217e662a4
0x0f0bb9c13be3b595d6f0fde841d5247a96f7e315
0x12302fE9c02ff50939BaAaaf415fc226C078613C
0x1727c2c531cf966f902E5927b98490fDFb3b2b70
0x18c486b76cb76981360e96ca4f90fc745fde6a85
0x19c6876e978d9f128147439ac4cd9ea2582cd141
0x1Fb403834C911eB98d56E74F5182b0d64C3b3b4D
0x1d31F259eE307358a26dFb23EB365939E8641195
0x1db92e2eebc8e0c075a02bea49a2935bcd2dfcf4
0x1fe2df852ba3299d6534ef416eefa406e56ced99
0x2020dba91b30cc0006188af794c2fb30dd8520db
0x21842597390c4c6e3c1239e434a682b054bd9548
0x29a6194691f91a73715209ef6512e576722830a2
0x29fcB43b46531BcA003ddC8FCB67FFE91900C762
0x2ae2d1231f0d754a7fa4f5e5d0e5554085e1b500
0x2b3060c55fcb8275653e99ad511a71f67ba76934
0x2dd68b007B46fBe91B9A7c3EDa5A7a1063cB5b47
0x2f25df28caf984366ee584e13241707e85dcd5a6
0x2f55e8b20D0B9FEFA187AA7d00B6Cbe563605bF5
0x2f684bda12f684bda12f684bda12f684bda12f68
0x2f870a80647BbC554F3a0EBD093f11B4d2a7492A
0x337d7f54be11b6ed55fef7b667ea5488db53db83
0x34CfAC646f301356fAa8B21e94227e3583Fe3F5F
0x357147caf9C0cCa67DfA0CF5369318d8193c8407
0x38869bf66a61cF6bDB996A6aE40D5853Fd43B526
0x3E5c63644E683549055b9Be8653de26E0B4CD36E
0x3ac65dea3cc9dd0d7b7b800f834e3d73415b4e94
0x3c8acc1e7b08d8e76f9fda015ef48dc8c710a73c
0x3d4BA2E0884aa488718476ca2FB8Efc291A46199
0x3f8731abdd661adca08a5558f0f5d272e953d363
0x40A2aCCbd92BCA938b02010E17A5b8929b49130D
0x40c57923924b5c5c5455c48d93317139addac8fb
0x41675C099F32341bf84BFc5382aF534df5C7461a
0x4191E2e12E8BC5002424CE0c51f9947b02675a44
0x445a0683e494ea0c5AF3E83c5159fBE47Cf9e765
0x4Aa5Bf7D840aC607cb5BD3249e6Af6FC86C04897
0x4a204f620c8c5ccdca3fd54d003badd85ba50043
0x4bda12f684bda12f684bda12f684bda12f684bda
0x4e1DCf7AD4e460CfD30791CCC4F9c8a4f820ec67
0x50c3cdc4074750a7a974204a716c999edd37482f
0x525c754a46b79e05543a59bb61e8de3c9eee0d95
0x526643F69b81B008F46d95CD5ced5eC0edFFDaC6
0x534c328d23f234e6e2a413deca25caece4506144
0x551b7fdfd2dbcec4f785059e1ef6e0b40ca2...