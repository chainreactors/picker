---
title: unixODBC <=2.3.14 Multiple Races
url: https://seclists.org/fulldisclosure/2026/Nov/9
source: Full Disclosure
date: 2026-11-05
fetch_date: 2026-11-06T08:41:46.033521
---

# unixODBC <=2.3.14 Multiple Races

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

[![Previous](/images/left-icon-16x16.png)](8)
[By Date](date.html#9)
[![Next](/images/right-icon-16x16.png)](10)

[![Previous](/images/left-icon-16x16.png)](8)
[By Thread](index.html#9)
[![Next](/images/right-icon-16x16.png)](10)

![](/shared/images/nst-icons.svg#search)

# unixODBC <=2.3.14 Multiple Races

---

*From*: Daniel Owens via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 4 Nov 2026 13:14:51 +0000

---

```
The unixODBC driver manager library contains multiple races of importance / interest, including a set of data races in
the connection-pooling configuration state data that can cause one thread to read a half-written pool-size or timeout
value, which can lead to a variety of harmful effects, as well as a race between teardown and error-handling
functionality that can result in double-frees and use-after-frees.  Other races exist within the code, as well, but,
for brevity, are left as exercises for the reader.

Examples
Sample Data Races
While 7 distinct data races were discovered, the following serves as a blueprint to find both the examples below and
other instances.

Connection-Pooling Configuration State Data Races
The DriverManager's connection-pooling configuration state -- the globals `pooling_enabled`, `pool_max_size`, and
`pool_wait_timeout` declared in `SQLConnect.c` -- is read and written from `SQLAllocHandle`, `SQLSetEnvAttr`,
`SQLConnect`, `SQLDriverConnect`, `SQLDisconnect`, and `SQLFreeHandle` without any of the write paths acquiring a lock,
despite such a lock -- a mutex in `__handles.c` -- already existing expressly for this purpose.  Since the variables in
question are neither atomic nor `volatile`, directly accessing them in such a fashion via reads and writes creates a
data race, with the compiler and central processing unit (CPU) being free to tear, cache, and reorder the accesses (and
the compiler will, more generally, assume single-threaded execution for non-atomic globals, which may cause aggressive
optimisations, like moving reads out of loops, that further break runtime assumptions).  While there are multiple sites
with this specific problem, we will only show code for one for the sake of brevity.  The sample code to reproduce the
issue will, across multiple runs, demonstrate races in `SQLSetEnvAttr`, `SQLAllocHandle`, etc., so running it multiple
times will provide a better example thereof, as one would expect with such an issue.

```c
int pooling_enabled = 0;
int pool_max_size = 0;
int pool_wait_timeout;
```
Code snippet from `unixODBC`'s DriverManager/SQLConnect.c, lines 738-740

```c
/** Lines 255-261 **/
/*
* connection pooling stuff
*/

extern int pooling_enabled;
extern int pool_max_size;
extern int pool_wait_timeout;
/** ... **/
/** Lines 302-323 **/
            if ( pooling_string[ 0 ] == '1' ||
                toupper( pooling_string[ 0 ] ) == 'Y' ||
                ( toupper( pooling_string[ 0 ] ) == 'O' &&
                    toupper( pooling_string[ 1 ] ) == 'N' ))
            {
                pooling_enabled = 1;
            }

#ifdef WITH_SHARDENV
            if ( pooling_enabled )
            {
                int first;

                SQLGetPrivateProfileString( "ODBC", "PoolMaxSize", "0",
                    pool_max_size_string, sizeof( pool_max_size_string ),
                    "ODBCINST.INI" );
                pool_max_size = atoi( pool_max_size_string );

                SQLGetPrivateProfileString( "ODBC", "PoolWaitTimeout", "30",
                    pool_wait_timeout_string, sizeof( pool_wait_timeout_string ),
                    "ODBCINST.INI" );
                pool_wait_timeout = atoi( pool_wait_timeout_string );
/** .. **/
/** Lines 383-397 **/
#else

            if ( pooling_enabled )
            {
                int first;

                SQLGetPrivateProfileString( "ODBC", "PoolMaxSize", "0",
                    pool_max_size_string, sizeof( pool_max_size_string ),
                    "ODBCINST.INI" );
                pool_max_size = atoi( pool_max_size_string );

                SQLGetPrivateProfileString( "ODBC", "PoolWaitTimeout", "30",
                    pool_wait_timeout_string, sizeof( pool_wait_timeout_string ),
                    "ODBCINST.INI" );
                pool_wait_timeout = atoi( pool_wait_timeout_string );
```
Snippets from `unixODBC`'s DriverManager/SQLAllocHandle.c

```c
#include <stdio.h>
#include <pthread.h>
#include <sql.h>
#include <sqlext.h>

#define ITER 2000

static void *setter_thread(void *arg) {
   (void)arg;
   for (int i = 0; i < ITER; i++) {
        SQLSetEnvAttr(SQL_NULL_HENV, SQL_ATTR_CONNECTION_POOLING,
                       (SQLPOINTER)SQL_CP_ONE_PER_DRIVER, 0);
     }
     return NULL;
}

static void *alloc_thread(void *arg) {
    (void)arg;
    for (int i = 0; i < ITER; i++) {
        SQLHENV henv = SQL_NULL_HENV;
        SQLAllocHandle(SQL_HANDLE_ENV, SQL_NULL_HANDLE, &henv);
        if (henv != SQL_NULL_HENV) {
            SQLFreeHandle(SQL_HANDLE_ENV, henv);
        }
    }
    return NULL;
}

int main(void) {
    pthread_t t1, t2;
    pthread_create(&t1, NULL, setter_thread, NULL);
    pthread_create(&t2, NULL, alloc_thread, NULL);
    pthread_join(t1, NULL);
    pthread_join(t2, NULL);
    printf("done\n");
    return 0;
}
```
Sample code to cause the data race

```text
WARNING: ThreadSanitizer: data race (pid=1369482)
  Read of size 4 at 0x7f6f9fff8c28 by thread T2:
    #0 __SQLAllocHandle .../DriverManager/SQLAllocHandle.c:387:18 ...
    #1 SQLAllocHandle .../DriverManager/SQLAllocHandle.c:1396:12 ...
    #2 alloc_thread .../poc_pool_race.c:41:24 ...
  Previous write of size 4 at 0x7f6f9fff8c28 by thread T1:
    #0 SQLSetEnvAttr .../DriverManager/SQLSetEnvAttr.c:156:33 ...
    #1 setter_thread .../poc_pool_race.c:31:9 ...
  Location is global 'pooling_enabled' of size 4 at 0x7f6f9fff8c28 (libodbc.so.2+0x8ec28)
  ...
SUMMARY: ThreadSanitizer: data race .../SQLAllocHandle.c:387:18 in __SQLAllocHandle
ThreadSanitizer: reported 1 warnings
```
Output from ThreadSanitizer

Sample Double-Free/Use-After-Free Race
Although there are multiple instances of this issue within the code base, the following shall serve as a template to
find the others.

Racing on a Shared Handle
The `__release_env`, `__release_dbc`, `__release_stmt`, and `__release_desc` cleanup functions in `__handles.c` perform
`memset` and `free` operations to the caller-supplied handle pointer regardless of whether that pointer was actually
found and unlinked from the handle list, but handle validation acquires and releases the shared `mutex_lists` lock
before the caller proceeds to release the handle such that two threads that call `SQLFreeHandle` on the same handle
simultaneously can both pass validation, so that both either free the same handle (a double-free) or one frees and the
other then reads the freed handle (a use-after-free).  Such bugs can, for example, result in a crash or exploitable
memory corruption.  Please note that our example only shows some of the instances and that the exact same paradigm
exists elsewhere in the code.

It should also be noted, for completeness, that the code in question and in our sample code snippets contain a variety
of other bugs, including the handle being freed inside of the `mutex_lists` lock and then being unlinked from the list
after validation has already occurred in a separate lock cycle.  Also, `SQLFreeHandle` performs validation, drops the
lock, and then calls `__release_env` -- it is this process that is allowing the race.

Re...