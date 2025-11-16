---
title: An Illustrated Guide to AP2 (Agent Payment Protocol) (2025)
url: https://arthurchiao.github.io/blog/ap2-illustrated-guide/
source: ArthurChiao's Blog
date: 2025-11-15
fetch_date: 2025-11-16T03:18:42.572993
---

# An Illustrated Guide to AP2 (Agent Payment Protocol) (2025)

# [ArthurChiao's Blog](https://arthurchiao.github.io/)

* [Home](/index.html)
* [Articles (EN)](/articles)
* [Articles (中文)](/articles-zh)
* [Categories](/categories)
* [About](/about)
* [Donate](/donate)

# An Illustrated Guide to AP2 (Agent Payment Protocol) (2025)

Published at 2025-11-15 | Last Update 2025-11-15

With the rapid evolution of GenAI and the growing trend of **`accomplishing more and more
tasks through chat`**, can you imagine a day (perhaps in the near future) we
can **`buy almost anything simply by chatting`**? Instead of browsing e-commerce
sites, comparing products yourself, you’ll just tell your agent what you need.
It will **`handle everything`**: selecting options, comparing features, negotiating
prices, making payments, and ensuring the product arrives at the right place
and time.

To bring this vision to life, one essential piece is still missing: **`a payment
protocol designed for agent-to-agent transactions`**. That’s exactly why AP2 was
created.

This post offers an illustrative guide to this emerging topic.

![](/assets/img/ap2-illustrated-guide/shopping-agent-view.png)

Fig. Shopping agent view of the "Buy a coffee maker" AP2 demo.

![](/assets/img/ap2-illustrated-guide/demo-call-flow.png)

Fig.
Call flow of the AP2 demo. Note: for clarity, the "Shopping Agent" shown
in this diagram combines the responsibilities of three distinct agents from the
actual demo: the shopping agent, address collection agent, and payment method
collection agent.

---

* [1 Why AP2?](#1-why-ap2)
  + [1.1 An Era of Agentic Commerce](#11-an-era-of-agentic-commerce)
  + [1.2 AP2: Payment Protocol for Agents](#12-ap2-payment-protocol-for-agents)
* [2 How AP2 Works](#2-how-ap2-works)
  + [2.1 Core Concepts](#21-core-concepts)
    - [2.1.1 Mandate](#211-mandate)
    - [2.1.2 VC (Verifiable Credential)](#212-vc-verifiable-credential)
  + [2.2 Working Fashions (Scenarios)](#22-working-fashions-scenarios)
    - [2.2.1 Real-time purchases (human present)](#221-real-time-purchases-human-present)
    - [2.2.2 Delegated tasks (human not present)](#222-delegated-tasks-human-not-present)
* [3 Demo: Buy A Coffee Maker Through Chat](#3-demo-buy-a-coffee-maker-through-chat)
  + [3.1 Components](#31-components)
  + [3.2 Agent Card & System Prompt](#32-agent-card--system-prompt)
    - [3.2.1 Shopping Agent](#321-shopping-agent)
    - [3.2.2 Merchant Agent](#322-merchant-agent)
    - [3.2.3 Merchant Payment Agent](#323-merchant-payment-agent)
    - [3.2.4 Payment Credential Provider Agent](#324-payment-credential-provider-agent)
  + [3.3 Run The Demo (Chat to Buy a Coffee Maker)](#33-run-the-demo-chat-to-buy-a-coffee-maker)
  + [3.4 Detailed Traces](#34-detailed-traces)
  + [3.5 Detailed A2A/AP2 Messages](#35-detailed-a2aap2-messages)
    - [`ShoppingAgent -> MerchantAgent`: Find products matching user’s IntentMandate](#shoppingagent---merchantagent-find-products-matching-users-intentmandate)
    - [`ShoppingAgent -> PaymentCredentialProviderAgent`: Get the user’s shipping address](#shoppingagent---paymentcredentialprovideragent-get-the-users-shipping-address)
    - [`ShoppingAgent -> MerchantAgent`: Update the cart with the user’s shipping address](#shoppingagent---merchantagent-update-the-cart-with-the-users-shipping-address)
    - [`ShoppingAgent -> PaymentCredentialProviderAgent`: Get a filtered list of the user’s payment methods](#shoppingagent---paymentcredentialprovideragent-get-a-filtered-list-of-the-users-payment-methods)
    - [`ShoppingAgent -> PaymentCredentialProviderAgent`: Get a payment credential token for the user’s payment method](#shoppingagent---paymentcredentialprovideragent-get-a-payment-credential-token-for-the-users-payment-method)
    - [`ShoppingAgent -> PaymentCredentialProviderAgent`: This is the signed payment mandate](#shoppingagent---paymentcredentialprovideragent-this-is-the-signed-payment-mandate)
    - [`ShoppingAgent -> MerchantAgent`: Initiate a payment](#shoppingagent---merchantagent-initiate-a-payment)
    - [`MerchantAgent -> MerchantPaymentAgent`: Initiate a payment](#merchantagent---merchantpaymentagent-initiate-a-payment)
    - [`ShoppingAgent -> MerchantAgent`: Initiate a payment. Include the challenge response.](#shoppingagent---merchantagent-initiate-a-payment-include-the-challenge-response)
    - [`MerchantAgent -> MerchantPaymentAgent`: Initiate a payment (include the challenge response)](#merchantagent---merchantpaymentagent-initiate-a-payment-include-the-challenge-response)
    - [`MerchantPaymentAgent -> PaymentCredentialProviderAgent`: Give me the payment method credentials for the given token](#merchantpaymentagent---paymentcredentialprovideragent-give-me-the-payment-method-credentials-for-the-given-token)
  + [3.6 Summary: Interactions Between Agents](#36-summary-interactions-between-agents)
* [References](#references)

---

# 1 Why AP2?

## 1.1 An Era of Agentic Commerce

The digital interaction fashion is likely to enter a new phase:

* Now and the past: people interact directly with **`websites and applications`**.
  Such as, people browse websites or apps, select the products they like and add to cart, and finally click the “Buy” or “Pay” button;
* The future: may shift toward an era of **`conversational and delegated task`** execution **`via agents`**;
  no manually browsing, **`just chat with your AI assistant`**.

This means agents will manage various daily tasks for users (humans), such as

* routine purchases
* complex product research
* price negotiations, and more.

This new era of **`agentic commerce`** will bring new opportunities for both users and businesses:

* For users: get a highly personalized, seamless shopping experience
* For businesses: open up a new, intelligent channel for reaching customers

## 1.2 AP2: Payment Protocol for Agents

The above mentiond scenario raises new challenges for payments, and it is in this background,
Google introduced the **`Agent Payments Protocol (AP2)`** in September, 2025:
[Powering AI commerce with the new Agent Payments Protocol (AP2)](https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol).

> Today, Google announced the Agent Payments Protocol (AP2), an open protocol
> developed with leading payments and technology companies to securely initiate
> and transact agent-led payments across platforms. The protocol can be used as
> **`an extension of the Agent2Agent (A2A) protocol`** and Model Context Protocol (MCP).
> In concert with industry rules and standards, it establishes a
> payment-agnostic framework for users, merchants, and payments providers to
> transact with confidence across all types of payment methods.

# 2 How AP2 Works

In a nutshell: **`establishing trust via Mandates and Verifiable Credentials (VCs)`**.

## 2.1 Core Concepts

### 2.1.1 Mandate

* Mandates are tamper-proof, **`cryptographically-signed digital contracts`**;
* Mandates serve as **`verifiable proof of a user's instructions`**;
* Mandates are **`signed by VC`**.

### 2.1.2 VC (Verifiable Credential)

* VC is a special kind of **`data payload between agents`**.

## 2.2 Working Fashions (Scenarios)

### 2.2.1 Real-time purchases (human present)

![](/assets/img/ap2-illustrated-guide/ap2-human-present.png)

Image source: [1]

1. `User -> Agent`: “Find me new white running shoes”
2. `Agent`: capture the request in an initial **`IntentMandate`**. This provides the auditable context for the entire interaction in a transaction process.
3. `Agent -> Merchant Agents`: find shoes with IntentMandate; get some candidates;
4. `Agent -> User`: present a cart with the shoes users would like;
5. `User`: select the item he/she likes;
6. `Agent`: sign a **`CartMandate`**. This is a critical step that creates a secure, unchangeable record of the exact items and price, ensuring what user see is what them pay for.
7. `Agent -> Merchant Agent & Credential Provider Agent`: complete payment with a **`PaymentMandate`**.

### 2.2.2 Delegated tasks (human ...