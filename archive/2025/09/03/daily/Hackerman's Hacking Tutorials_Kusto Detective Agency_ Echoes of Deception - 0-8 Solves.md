---
title: Kusto Detective Agency: Echoes of Deception - 0-8 Solves
url: https://parsiya.net/blog/2025-kda-echoes/
source: Hackerman's Hacking Tutorials
date: 2025-09-03
fetch_date: 2025-10-02T19:33:39.491937
---

# Kusto Detective Agency: Echoes of Deception - 0-8 Solves

# [Hackerman's Hacking Tutorials](https://parsiya.net/)

## The knowledge of anything, since all things have causes, is not acquired or complete unless it is known by its causes. - Avicenna

Navigate…» About Me!» Cheat Sheet» My Clone» Source Repo» Manual Work is a Bug» The Other Guy from Wham!

* [About Me!](https://parsiya.net/about/ "About Me!")
* [Cheat Sheet](https://parsiya.net/cheatsheet/ "Cheat Sheet")
* [My Clone](https://parsiya.io/ "My Clone")
* [Source Repo](https://github.com/parsiya/parsiya.net "Source Repo")
* [Manual Work is a Bug](https://queue.acm.org/detail.cfm?id=3197520 "Manual Work is a Bug")
* [The Other Guy from Wham!](https://www.google.com/search?q=andrew+ridgeley "The Other Guy from Wham!")

Sep 1, 2025
- 33 minute read - [Kusto](https://parsiya.net/categories/kusto/)

# Kusto Detective Agency: Echoes of Deception - 0-8 Solves

* [Typical Workflow](#typical-workflow)
  + [Using AI](#using-ai)
* [0: Onboarding](#0-onboarding)
* [Case 1: To bill or not to bill?](#case-1-to-bill-or-not-to-bill)
* [Case 2: Catch the Phishermen!](#case-2-catch-the-phishermen)
* [Case 3: Return stolen cars!](#case-3-return-stolen-cars)
* [Case 4: Triple trouble!](#case-4-triple-trouble)
* [Case 5: Blast into the past](#case-5-blast-into-the-past)
* [Case 6: Hack this rack!](#case-6-hack-this-rack)
* [Case 7: Mission 'Connect'](#case-7-mission-connect)
* [Case 8: Catchy Run](#case-8-catchy-run)

Kusto is important at my current employer and one of my work besties does
SecOps. So, I've decided to learn more Kusto. Solves for the first eight tasks
for Kusto Detective Agency challenge Echoes of Deception.

It turns out Kusto is not just a better looking SQL, it does a lot more. E.g.,
it can make a graph and find paths (yes, as I've just searched, T-SQL can also
do this). It makes me wonder if we can do some esoteric data flow static
analysis by converting the AST into rows of data and finding paths from sources
to sinks (or am I reinventing CodeQL, again, lol [1](#fn:1)).

There are a series of challenges named [Kusto Detective Agency](https://detective.kusto.io/) which are
basically "find this flag in a bunch of logs using KQL." A few months ago, I was
enthusiastic and started season 3 `Call of the Cyber Duty` in real time with
almost zero Kusto background and did the first three before I realized, this is
much harder than I imagined.

I started from season 1 to learn and do the challenges. Here are the first eight
(or nine if you count onboarding) solves.

# Typical Workflow

Each challenge has a bunch of "training" material associated with it. These are
Kusto functionalities and tricks that can be used to solve the challenge. I
didn't notice them in my season 3 run.

Then I look at the tables. We can get the table columns and types with a query
like this:

```
TableName
| getschema
| project ColumnName, DataType
```

And it will give us something like this:

```
| ColumnName | DataType        |
| ---------- | --------------- |
| Timestamp  | System.DateTime |
| callsign   | System.String   |
| lat        | System.Double   |
| lon        | System.Double   |
```

Then I check the first 10 rows to see what the data looks like:

```
TableName
| take 10
```

Then I try to figure out how to solve the challenge using the training material.

## Using AI

AI (LLMs in this context) was both good and bad here. It was great for syntax
issues, AKA "I want to filter A and B, write a Kusto query for me", but not
great for the actual solves. I usually added all the data, table schemas and
other insights from training to a markdown file and asked different models in
GitHub Copilot Chat to solve. They actually worked for the first 2-3 challenges,
but not after.

I had the best results with Claude 4 and GPT-5. Both yap[2](#fn:2) and over complicate
things even with extensive instructions. It was a fun experience to yank them
often and try to herd them into the correct solve path.

LLMs are also good at formatting, so I asked them to format my text. E.g., the
markdown tables you see in this blog.

# 0: Onboarding

We need to find which detective has earned the most bounties.

```
DetectiveCases
| take 2
```

We have five columns:

```
Timestamp
EventType
DetectiveId
CaseId
Properties
```

See different types of `EventType`

```
DetectiveCases
| distinct EventType

CaseUnsolved
CaseAssigned
CaseSolved
CaseOpened
```

If `CaseOpened`, `Properties` will have the bounty: `{"Bounty":3146}`.

We can extract bounties:

```
let bounties = DetectiveCases
| where EventType == "CaseOpened"
| extend Bounty = tolong(Properties.Bounty)
| project CaseId, Bounty;
```

I wrote a query to sum up all detective bounties using `CaseSolved` events. It
was the wrong answer. I should have checked if the detective was assigned the
case in a `CaseAssigned` event AND if they had a `CaseSolved` event for the same
case ID. Apparently, you can solve a case and get no bounty if you were not
assigned to the case.

We can extract assignments like this:

```
let assignments = DetectiveCases
| where EventType == "CaseAssigned"
| project CaseId, AssignedDetectiveId = DetectiveId;
```

Sum for the IDs that are the same for assigned and solved.

```
let bounties = DetectiveCases
| where EventType == "CaseOpened"
| extend Bounty = tolong(Properties.Bounty)
| project CaseId, Bounty;
let assignments = DetectiveCases
| where EventType == "CaseAssigned"
| project CaseId, AssignedDetectiveId = DetectiveId;
DetectiveCases
| where EventType == "CaseSolved"
| project CaseId, SolvedDetectiveId = DetectiveId
| join kind=inner assignments on CaseId
| where SolvedDetectiveId == AssignedDetectiveId
| join kind=inner bounties on CaseId
| summarize total = sum(Bounty) by SolvedDetectiveId
| sort by total desc
```

And the top three are:

```
| DetectiveId            | Total Bounties |
| ---------------------- | -------------- |
| kvc61f0b891ee26195970a | 874,699        |
| kvc12a22e9e9e65c1694f1 | 838,852        |
| kvc29d392ca965f09646f8 | 812,028        |
```

Our answer is `kvc61f0b891ee26195970a`.

# Case 1: To bill or not to bill?

`What is the total bills amount due in April?`

Old SQL query to calculate bills:

```
SELECT SUM(Consumed * Cost) AS TotalCost
FROM Costs
JOIN Consumption ON Costs.MeterType = Consumption.MeterType
```

The `Costs` table has only two rows:

Cost columns:

```
| MeterType   | Unit  | Cost     |
| ----------- | ----- | -------- |
| Water       | Liter | 0.001562 |
| Electricity | kwH   | 0.3016   |
```

The `Consumption` table has four columns:

* `Timestamp`
* `HouseholdId`
* `MeterType`
* `Consumed`

So:

1. Timestamps are in April.
2. Ignore HouseholdId because we want the total.
3. Each bill is Consumed \* Cost based on MeterType.

We only have April data in the table so we don't need to check the Timestamp,
but I did it anyways. [getmonth](https://learn.microsoft.com/en-us/kusto/query/monthofyear-function) (also called `monthofyear`) is a fun
function and `getmonth(Timestamp) == 4` checks if the timestamp's month is
April.

```
Consumption
| where getmonth(Timestamp) == 4
| summarize total_consumed = sum(Consumed) by MeterType
| join kind=inner (Costs) on MeterType
| extend bill = total_consumed * Cost
| summarize total = sum(bill)
```

This works, but doesn't have the correct answer `35,637,875.19770707`.

Checking for duplicates:

```
Consumption
| where getmonth(Timestamp) == 4
| summarize Count = count() by Timestamp, HouseholdId, MeterType, Consumed
| where Count > 1
| take 10
```

There are a lot of 2 counts. So we try to get distinct

```
Consumption
| where getmonth(Timestamp) == 4
| distinct Timestamp, HouseholdId, MeterType, Consumed
| summarize total_consumed = sum(Consumed) by MeterType
| join kind=inner (Costs) on MeterType
| extend bill = total_consumed * Cost
| summarize total = sum(bill)
```

Looks like there might be multiple reports per household per day. Some of them
are negative which is curious. At first both AI and me thought a negative is
either correction or...