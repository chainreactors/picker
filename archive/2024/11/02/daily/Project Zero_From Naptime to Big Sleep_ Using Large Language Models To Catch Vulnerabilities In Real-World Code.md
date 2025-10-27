---
title: From Naptime to Big Sleep: Using Large Language Models To Catch Vulnerabilities In Real-World Code
url: https://googleprojectzero.blogspot.com/2024/10/from-naptime-to-big-sleep.html
source: Project Zero
date: 2024-11-02
fetch_date: 2025-10-06T19:17:20.620078
---

# From Naptime to Big Sleep: Using Large Language Models To Catch Vulnerabilities In Real-World Code

# [Project Zero](https://googleprojectzero.blogspot.com/)

News and updates from the Project Zero team at Google

## Friday, November 1, 2024

### From Naptime to Big Sleep: Using Large Language Models To Catch Vulnerabilities In Real-World Code

Posted by the [Big Sleep team](#bigsleepteam)

Introduction

In our previous post, [Project Naptime: Evaluating Offensive Security Capabilities of Large Language Models](https://googleprojectzero.blogspot.com/2024/06/project-naptime.html), we introduced our framework for large-language-model-assisted vulnerability research and demonstrated its potential by improving the state-of-the-art performance on Meta's CyberSecEval2 benchmarks. Since then, Naptime has evolved into Big Sleep, a collaboration between Google Project Zero and Google DeepMind.

Today, we're excited to share the first real-world vulnerability discovered by the Big Sleep agent: an exploitable stack buffer underflow in [SQLite](https://sqlite.org/), a widely used open source database engine. We discovered the [vulnerability](https://project-zero.issues.chromium.org/issues/372435124) and reported it to the developers in early October, who [fixed it](https://sqlite.org/src/info/41d58a014ce89356) on the same day. Fortunately, we found this issue before it appeared in an official release, so SQLite users were not impacted.

We believe this is the first public example of an AI agent finding a previously unknown exploitable memory-safety issue in widely used real-world software. Earlier this year at the DARPA AIxCC event, Team Atlanta [discovered a null-pointer dereference](https://team-atlanta.github.io/blog/post-asc-sqlite/) in SQLite, which inspired us to use it for our testing to see if we could find a more serious vulnerability.

We think that this work has tremendous defensive potential. Finding vulnerabilities in software before it's even released, means that there's no scope for attackers to compete: the vulnerabilities are fixed before attackers even have a chance to use them. Fuzzing has helped significantly, but we need an approach that can help defenders to find the bugs that are difficult (or impossible) to find by fuzzing, and we're hopeful that AI can narrow this gap. We think that this is a promising path towards finally turning the tables and achieving an asymmetric advantage for defenders.

The vulnerability itself is quite interesting, along with the fact that the existing testing infrastructure for SQLite (both through OSS-Fuzz, and the project's own infrastructure) did not find the issue, so we did some further investigation.

Methodology

A key motivating factor for Naptime and now for Big Sleep has been the [continued in-the-wild discovery](https://blog.google/threat-analysis-group/0-days-exploited-wild-2022/%23%3A~%3Atext%3DOver%252040%2525%2520of%2520the%25200%252Ddays%2520discovered%2520were%2520variants%2520of%2520previously%2520reported%2520vulnerabilities) of exploits for variants of previously found and patched vulnerabilities. As this trend continues, it's clear that fuzzing is not succeeding at catching such variants, and that for attackers, manual variant analysis is a cost-effective approach.

We also feel that this variant-analysis task is a better fit for current LLMs than the more general open-ended vulnerability research problem. By providing a starting point – such as the details of a previously fixed vulnerability – we remove a lot of ambiguity from vulnerability research, and start from a concrete, well-founded theory: "This was a previous bug; there is probably another similar one somewhere".

Our project is still in the research stage, and we are currently using small programs with known vulnerabilities to evaluate progress. Recently, we decided to put our models and tooling to the test by running our first extensive, real-world variant analysis experiment on SQLite. We collected a number of recent commits to the SQLite repository, manually removing trivial and documentation-only changes. We then adjusted the prompt to provide the agent with both the commit message and a diff for the change, and asked the agent to review the current repository (at [HEAD](https://sqlite.org/src/info/2f7eab381e167609)) for related issues that might not have been fixed.

Discovered Vulnerability

The vulnerability is an interesting one where a special sentinel value -1 is used in an (otherwise) index-typed field iColumn:

7476:   struct sqlite3\_index\_constraint {

7477:      int iColumn;              /\* Column constrained.  -1 for ROWID \*/

7478:      unsigned char op;         /\* Constraint operator \*/

7479:      unsigned char usable;     /\* True if this constraint is usable \*/

7480:      int iTermOffset;          /\* Used internally - xBestIndex should ignore \*/

7481:   } \*aConstraint;            /\* Table of WHERE clause constraints \*/

This pattern creates a potential edge-case that needs to be handled by all code that uses the field, since the expectation would be that a valid column index is non-negative.

The function [seriesBestIndex](https://sqlite.org/src/file?ci=2f7eab381e167609&name=ext/misc/series.c&ln=578-778) failed to correctly handle this edge-case, resulting in a write into a stack buffer with a negative index when handling a query with a constraint on the rowid column. In the build that we provided to our agent, debug assertions were enabled, and this condition was checked by the assertion at line [706](https://sqlite.org/src/file?ci=2f7eab381e167609&name=ext/misc/series.c&ln=706):

619 static int seriesBestIndex(

620   sqlite3\_vtab \*pVTab,

621   sqlite3\_index\_info \*pIdxInfo

622 ){

...

630   int aIdx[7];           /\* Constraints on start, stop, step, LIMIT, OFFSET,

631                          \*\* and value.  aIdx[5] covers value=, value>=, and

632                          \*\* value>,  aIdx[6] covers value<= and value< \*/

633   const struct sqlite3\_index\_constraint \*pConstraint;

...

642   for(i=0; i<pIdxInfo->nConstraint; i++, pConstraint++){

643     int iCol;    /\* 0 for start, 1 for stop, 2 for step \*/

644     int iMask;   /\* bitmask for those column \*/

645     int op = pConstraint->op;

...

705     iCol = pConstraint->iColumn - SERIES\_COLUMN\_START;

706     assert( iCol>=0 && iCol<=2 );

707     iMask = 1 << iCol;

...

713     if( pConstraint->usable==0 ){

714       unusableMask |=  iMask;

715       continue;

716     }else if( op==SQLITE\_INDEX\_CONSTRAINT\_EQ ){

717       idxNum |= iMask;

718       aIdx[iCol] = i;

719     }

720   }

In a release build, however, this assertion is not present, and in our testing (this will vary depending on compiler and optimization level) the subsequent write at line [718](https://sqlite.org/src/file?ci=2f7eab381e167609&name=ext/misc/series.c&ln=718) will write below the aIdx buffer, corrupting the least significant 32 bits of the pConstraint pointer, which will be dereferenced in the next iteration of the loop, leading to a likely exploitable condition.

However, given this explanation of the vulnerability – it's not trivial (at least for us) as human researchers to understand precisely how to trigger it – clearly a constraint on the ROWID column would be a good starting point, but more detailed reading of the code would certainly be required. The agent already seems to know a lot more about SQLite than we do, so it can cut some corners!

One common case of this is that the model would immediately use the generate\_series virtual table when generating testcases. (We also saw cases where the model researched the available virtual tables first, but it's clearly able to apply pre-existing knowledge here).

# Trajectory Highlights

In this successful run based on Gemini 1.5 Pro, the seed commit was [[1976c3f7]](https://sqlite.org/src/info/1976c3f7e1fe77cf); which is a fairly large and non-obvious change. The bug found by our agent is only loosely related to the changes in the seed commit - this is not uncommon in manual ...