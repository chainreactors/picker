---
title: SQLite3 generate_series Stack Buffer Underflow
url: https://cxsecurity.com/issue/WLB-2024110007
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-11-07
fetch_date: 2025-10-06T19:12:27.705468
---

# SQLite3 generate_series Stack Buffer Underflow

[![Home Page](https://cert.cx/cxstatic/images/12018/cxseci.png)](https://cxsecurity.com/)

* [Home](https://cxsecurity.com/)
* Bugtraq
  + [Full List](https://cxsecurity.com/wlb/)
  + [Only Bugs](https://cxsecurity.com/bugs/)
  + [Only Tricks](https://cxsecurity.com/tricks/)
  + [Only Exploits](https://cxsecurity.com/exploit/)
  + [Only Dorks](https://cxsecurity.com/dorks/)
  + [Only CVE](https://cxsecurity.com/cvelist/)
  + [Only CWE](https://cxsecurity.com/cwelist/)
  + [Fake Notes](https://cxsecurity.com/bogus/)
  + [Ranking](https://cxsecurity.com/best/1/)
* CVEMAP
  + [Full List](https://cxsecurity.com/cvemap/)
  + [Show Vendors](https://cxsecurity.com/cvevendors/)
  + [Show Products](https://cxsecurity.com/cveproducts/)
  + [CWE Dictionary](https://cxsecurity.com/allcwe/)
  + [Check CVE Id](https://cxsecurity.com/cve/)
  + [Check CWE Id](https://cxsecurity.com/cwe/)
* Search
  + [Bugtraq](https://cxsecurity.com/search/)
  + [CVEMAP](https://cxsecurity.com/search/cve/)
  + [By author](https://cxsecurity.com/search/author/)
  + [CVE Id](https://cxsecurity.com/cve/)
  + [CWE Id](https://cxsecurity.com/cwe/)
  + [By vendors](https://cxsecurity.com/cvevendors/)
  + [By products](https://cxsecurity.com/cveproducts/)
* RSS
  + [Bugtraq](https://cxsecurity.com/wlb/rss/all/)
  + [CVEMAP](https://cxsecurity.com/cverss/fullmap/)
  + [CVE Products](https://cxsecurity.com/cveproducts/)
  + [Bugs](https://cxsecurity.com/wlb/rss/vulnerabilities/)
  + [Exploits](https://cxsecurity.com/wlb/rss/exploit/)
  + [Dorks](https://cxsecurity.com/wlb/rss/dorks/)
* More
  + [cIFrex](http://cifrex.org/)
  + [Facebook](https://www.facebook.com/cxsec)
  + [Twitter](https://twitter.com/cxsecurity)
  + [Donate](https://cxsecurity.com/donate/)
  + [About](https://cxsecurity.com/wlb/about/)

* [Submit](https://cxsecurity.com/wlb/add/)

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | |  | | --- | | **SQLite3 generate\_series Stack Buffer Underflow** **2024.11.06**  Credit:  **[Google Security Research](https://cxsecurity.com/author/Google%2BSecurity%2BResearch/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

Vulnerability details
static int seriesBestIndex(
sqlite3\_vtab \*pVTab,
sqlite3\_index\_info \*pIdxInfo
){
int i, j; /\* Loop over constraints \*/
int idxNum = 0; /\* The query plan bitmask \*/
#ifndef ZERO\_ARGUMENT\_GENERATE\_SERIES
int bStartSeen = 0; /\* EQ constraint seen on the START column \*/
#endif
int unusableMask = 0; /\* Mask of unusable constraints \*/
int nArg = 0; /\* Number of arguments that seriesFilter() expects \*/
int aIdx[7]; /\* Constraints on start, stop, step, LIMIT, OFFSET,
\*\* and value. aIdx[5] covers value=, value>=, and
\*\* value>, aIdx[6] covers value<= and value< \*/
const struct sqlite3\_index\_constraint \*pConstraint;
/\* This implementation assumes that the start, stop, and step columns
\*\* are the last three columns in the virtual table. \*/
assert( SERIES\_COLUMN\_STOP == SERIES\_COLUMN\_START+1 );
assert( SERIES\_COLUMN\_STEP == SERIES\_COLUMN\_START+2 );
aIdx[0] = aIdx[1] = aIdx[2] = aIdx[3] = aIdx[4] = aIdx[5] = aIdx[6] = -1;
pConstraint = pIdxInfo->aConstraint;
for(i=0; i<pIdxInfo->nConstraint; i++, pConstraint++){
int iCol; /\* 0 for start, 1 for stop, 2 for step \*/
int iMask; /\* bitmask for those column \*/
int op = pConstraint->op;
if( op>=SQLITE\_INDEX\_CONSTRAINT\_LIMIT
&& op<=SQLITE\_INDEX\_CONSTRAINT\_OFFSET
){
if( pConstraint->usable==0 ){
[...]
}
continue;
}
if( pConstraint->iColumn==SERIES\_COLUMN\_VALUE ){
switch( op ){
[...]
}
continue;
}
iCol = pConstraint->iColumn - SERIES\_COLUMN\_START; // \*\*\* 1 \*\*\*
assert( iCol>=0 && iCol<=2 ); // \*\*\* 2 \*\*\*
iMask = 1 << iCol;
#ifndef ZERO\_ARGUMENT\_GENERATE\_SERIES
if( iCol==0 && op==SQLITE\_INDEX\_CONSTRAINT\_EQ ){
bStartSeen = 1;
}
#endif
if( pConstraint->usable==0 ){
unusableMask |= iMask;
continue;
}else if( op==SQLITE\_INDEX\_CONSTRAINT\_EQ ){
idxNum |= iMask;
aIdx[iCol] = i; // \*\*\* 3 \*\*\*
}
}
struct sqlite3\_index\_constraint {
int iColumn; /\* Column constrained. -1 for ROWID \*/ // \*\*\* 4 \*\*\*
unsigned char op; /\* Constraint operator \*/
unsigned char usable; /\* True if this constraint is usable \*/
int iTermOffset; /\* Used internally - xBestIndex should ignore \*/
} \*aConstraint; /\* Table of WHERE clause constraints \*/
The seriesBestIndex function doesn't handle rowid constraints correctly. The code at [1] expects iColumn to be one of SERIES\_COLUMN\_START, SERIES\_COLUMN\_STOP, or SERIES\_COLUMN\_STEP (values 1, 2, or 3). However, the line can also be reached with a rowid constraint with an iColumn value of -1. Depending on the build configuration, the negative iCol may either trigger an assertion failure at [2] or lead to an out-of-bounds memory write access at [3].
Version
3.47.0 2024-10-05 12:02:17 2f7eab381e16760952d1c90a9119d2a217933f0136442d8f6eeb6d95e366ca4f (64-bit)
Reproduction case
SELECT \* FROM generate\_series(1, 1) WHERE rowid = 1
When built with assertions, the SQLite shell crashes with an assertion failure:
shell.c:6816: seriesBestIndex: Assertion `iCol>=0 && iCol<=2' failed.
When built with NDEBUG and ASan, the program produces the following crash report:
==2623073==ERROR: AddressSanitizer: stack-buffer-underflow on address 0x7ff83210be18 at pc 0x55dbc9afcd14 bp 0x7ffc7a497cd0 sp 0x7ffc7a497cc8
WRITE of size 4 at 0x7ff83210be18 thread T0
#0 0x55dbc9afcd13 in seriesBestIndex shell.c:6828
#1 0x55dbc9d5aaa9 in vtabBestIndex sqlite3.c:164633
#2 0x55dbc9d66290 in whereLoopAddVirtualOne sqlite3.c:167237
#3 0x55dbc9d67e57 in whereLoopAddVirtual sqlite3.c:167549
#4 0x55dbc9d69f06 in whereLoopAddAll sqlite3.c:167822
#5 0x55dbc9d73724 in sqlite3WhereBegin sqlite3.c:169776
#6 0x55dbc9d1b3d2 in sqlite3Select sqlite3.c:151580
#7 0x55dbc9d8c131 in yy\_reduce sqlite3.c:177608
#8 0x55dbc9d98b5c in sqlite3Parser sqlite3.c:179058
#9 0x55dbc9d9cc59 in sqlite3RunParser sqlite3.c:180392
#10 0x55dbc9cf1863 in sqlite3Prepare sqlite3.c:143187
#11 0x55dbc9cf1f65 in sqlite3LockAndPrepare sqlite3.c:143262
#12 0x55dbc9cf2356 in sqlite3\_prepare\_v2 sqlite3.c:143349
#13 0x55dbc9b30f63 in shell\_exec shell.c:24228
#14 0x55dbc9b58583 in runOneSqlLine shell.c:31909
#15 0x55dbc9b59624 in process\_input shell.c:32097
#16 0x55dbc9b5d1b7 in main shell.c:33026
#17 0x7ff834243b89 in \_\_libc\_start\_call\_main ../sysdeps/nptl/libc\_start\_call\_main.h:58
#18 0x7ff834243c44 in \_\_libc\_start\_main\_impl ../csu/libc-start.c:360
#19 0x55dbc9ae27a0 in \_start (sq+0x4a7a0) (BuildId: 8e6639a5755a4687574b3d22d6cf593ca32bb8b6)
Address 0x7ff83210be18 is located in stack of thread T0 at offset 24 in frame
#0 0x55dbc9afc4b6 in seriesBestIndex shell.c:6732
This frame has 1 object(s):
[32, 60) 'aIdx' (line 6740) <== Memory access at offset 24 underflows this variable
We've observed that, depending on the compiler and SQLite build configuration, this issue may allow an attacker to overwrite pConstraint, which makes it likely exploitable. However, the generate\_series extension is only enabled by default in the shell binary and not the library itself, so the impact of the issue is limited.
Credit information
Sergei Glazunov of Google Project Zero
This bug is subject to a 90-day disclosure deadline. If a fix for this issue is made available to users before the end of the 90-day deadline, this bug report will become public 30 days after the fix was made available. Otherwise, this bug report will become public at the deadline. The scheduled deadline is 2025-01-07.
For more details, see the Project Zero vulnerability disclosure policy: https://googleprojectzero.blogspot.com/p/vulnerability-disclosure-policy.html

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024110007)

[Tweet](https://twitter.com/share)

Vote for this issue:
 0
 0

50%

50%

#### **Thanks for you vote!**

#### **Thanks for you comment!** Your message is in quarantine 48 hours.

Comment it here.

Nick (\*)

Email (\*)

Video

Text (\*)

(\*) - req...