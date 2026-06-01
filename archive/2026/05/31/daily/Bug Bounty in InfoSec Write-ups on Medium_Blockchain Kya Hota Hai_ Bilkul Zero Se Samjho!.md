---
title: Blockchain Kya Hota Hai? Bilkul Zero Se Samjho!
url: https://infosecwriteups.com/blockchain-kya-hota-hai-bilkul-zero-se-samjho-7eb4a11d0596?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-05-31
fetch_date: 2026-06-01T06:47:02.617129
---

# Blockchain Kya Hota Hai? Bilkul Zero Se Samjho!

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fblockchain-kya-hota-hai-bilkul-zero-se-samjho-7eb4a11d0596&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fblockchain-kya-hota-hai-bilkul-zero-se-samjho-7eb4a11d0596&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-7eb4a11d0596---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-7eb4a11d0596---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

# Blockchain Kya Hota Hai? Bilkul Zero Se Samjho!

[![Hacker MD](https://miro.medium.com/v2/resize:fill:64:64/1*mArHieH3GY7HX9TX7ZAoIg.jpeg)](https://medium.com/%40HackerMD?source=post_page---byline--7eb4a11d0596---------------------------------------)

[Hacker MD](https://medium.com/%40HackerMD?source=post_page---byline--7eb4a11d0596---------------------------------------)

14 min read

·

May 11, 2026

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D7eb4a11d0596&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fblockchain-kya-hota-hai-bilkul-zero-se-samjho-7eb4a11d0596&source=---header_actions--7eb4a11d0596---------------------post_audio_button------------------)

Share

Press enter or click to view image in full size

![]()

**Series: Web3 Security Zero se Advance | Article #1**
*By HackerMD | 18 min read*

## Aaj Kya Seekhenge?

* Blockchain kya hota hai real life example se
* Web2 vs Web3 fark kya hai?
* Block kya hota hai andar kya hota hai?
* Chain kaise banti hai?
* Decentralization kya hota hai?
* Consensus mechanisms network agree kaise karta hai?
* Hash kya hota hai security kaise kaam karti hai?
* Blockchain ke types Public, Private, Hybrid
* Real world use cases
* Web3 Security mein kyu zaroori hai yeh sab samajhna?

> **Note:** Yeh series **Web3 Security** ke liye hai isliye har concept ko **hacker ki nazar se** samjhenge! Jo samjha woh attack kar sakta hai jo attack kar sakta hai woh **defend aur bug bounty** bhi kar sakta hai!

## Pehle Ek Story Sab Clear Ho Jaayega!

Socho tumhare mohalle mein ek **dukaan** hai

```
Ramesh Ki Dukaan
   Ek register hai — jisme sab kuch likha hai:
   → Kisne kitne paise diye
   → Kisne kitna udhaara liya
   → Kab diya, kab liya

Problem:
   → Register sirf Ramesh ke paas hai
   → Ramesh galat likh sakta hai
   → Register jal sakta hai, kho sakta hai
   → Ramesh cheat kar sakta hai — koi rok nahi!

Yeh hai Web2 / Traditional System:
   CENTRALIZED — ek jagah, ek insaan ka control
```

Ab socho yeh register ki **1000 copies** ho jaayein

```
 Register Copy #1   → Ramesh ke paas
 Register Copy #2   → Suresh ke paas
 Register Copy #3   → Mahesh ke paas
 Register Copy #4   → Ganesh ke paas
... aur 996 aur copies duniya bhar mein ...

Ab agar Ramesh apni copy mein fraud kare:
   → Baaki 999 copies se compare hoga
   → 999 copies bolegi — "Yeh GALAT hai!"
   → Ramesh ki fraud copy REJECT ho jaayegi!
   → Koi ek akela insaan system ko corrupt
     NAHI kar sakta!

Yeh hai BLOCKCHAIN!
```

## PART 1: Blockchain Exact Definition

```
Blockchain = Block + Chain

Block  = Data ka ek packet (register ka ek page)
Chain  = Sare blocks ek dusre se linked hain

Simple definition:
"Ek distributed digital register jo
 hazaaron computers pe exist karta hai,
 jisme data secure, transparent aur
 tamper-proof tarike se store hota hai"

Technical definition:
"A decentralized, immutable ledger of
 transactions maintained across a
 peer-to-peer network using cryptography"
```

## PART 2: Block Kya Hota Hai? Andar Kya Hai?

Ek block ek **dabba** ki tarah hai usme yeh hota hai:

```
┌─────────────────────────────────────┐
│           BLOCK #4721               │
├─────────────────────────────────────┤
│ Block Number   : 4721               │
│ Timestamp      : 2024-01-15 14:23   │
│ Nonce          : 83729              │
│                                     │
│ Previous Hash  :                    │
│ 0x1a2b3c4d5e6f...                   │
│ ← Pichle block ka "fingerprint"     │
│                                     │
│ Current Hash   :                    │
│ 0x9z8y7x6w5v4u...                   │
│ ← Is block ka "fingerprint"         │
│                                     │
│ Transactions   :                    │
│  → Alice → Bob   : 0.5 ETH          │
│  → Bob   → Carol : 1.2 ETH          │
│  → Carol → Dave  : 0.3 ETH          │
│  → [50+ aur transactions...]        │
│                                     │
│ Merkle Root    : 0xabc123...        │
└─────────────────────────────────────┘
```

## Har Field Ka Matlab:

**1. Block Number:**

```
Har block ka serial number hota hai
Block #0 = Genesis Block (sabse pehla)
Block #1, #2, #3... aise badhte hain
Ethereum pe ab 19 million+ blocks hain!
```

**2. Timestamp:**

```
Exactly kab yeh block create hua
Unix timestamp format mein store hota hai
Tamper proof baad mein change nahi hota
```

**3. Nonce (Number Used Once):**

```
Yeh ek magic number hai
Miners isko trial-and-error se dhundhte hain
Proof of Work (PoW) mein critical role hai
Baad mein PoW section mein detail mein samjhenge
```

**4. Previous Hash Sabse Important!**

```
Yeh woh cheez hai jo CHAIN banati hai!

Block #1 ka Previous Hash = Block #0 ka Hash
Block #2 ka Previous Hash = Block #1 ka Hash
Block #3 ka Previous Hash = Block #2 ka Hash

Agar koi Block #2 mein koi cheez change kare:
   → Block #2 ka Hash bilkul ALAG ho jaayega
   → Block #3 ka "Previous Hash" match nahi karega!
   → Block #3 INVALID!
   → Block #4 bhi INVALID!
   → Poori aage ki chain break!

ISLIYE blockchain tamper-proof hai!
```

**5. Current Hash:**

```
Is block ka unique fingerprint
Block ke saare data se milke banta hai
Ek bhi byte change → Hash bilkul alag ho jaata hai!

Example:
"Hello"  → Hash: 185f8db32921bd46...
"hello"  → Hash: 2cf24dba5fb0a30e...
(sirf capital H se lowercase h — completely different!)
```

**6. Transactions:**

```
Is block mein recorded sabhi transactions
Bitcoin pe : Kisne kitna kisko bheja
Ethereum pe: Transactions + Smart contract calls
Ek block mein typically 100–3000 transactions
```

**7. Merkle Root:**

```
Sabhi transactions ka ek combined "summary hash"
Merkle Tree se banta hai (binary tree structure)
Ek bhi transaction change → Merkle Root change!
Quick verification allow karta hai
```

## PART 3: Chain Kaise Banti Hai? Visual!

```
GENESIS BLOCK (Block #0)
┌──────────────────────┐
│ Block   #0           │
│ PrevHash: 0x0000000  │ ← Koi prev nahi!
│ Hash    : 0xAAA111   │
│ Txns    : [...]      │
└────────────────────...