---
title: Crystal Palace API
url: https://rastamouse.me/crystal-palace-api/
source: Rasta Mouse
date: 2025-09-15
fetch_date: 2025-10-02T20:10:19.965127
---

# Crystal Palace API

[Rasta Mouse](https://rastamouse.me)

* [Home](https://rastamouse.me/)

14 Sep 2025

4 min read

# Crystal Palace API

Crystal Palace provides two command-line tools, called `link` and `piclink`, which are used with a specification file to combine a reflective loader with one or more capabilities (DLLs and/or COFFs).

`link` takes the path to a spec file, the path to a DLL or COFF, and outputs PIC:

```
./link [/path/to/loader.spec] [/path/to/file.dll|file.o] [out.bin]
```

This is suitable for building a single capability using the `$VAR` syntax in the spec, e.g:

```
x64:
    load "bin/loader.x64.o"
        make pic

    push $DLL
        link "my_data"

    export
```

`piclink` is similar but it doesn't take the path to a capability. It relies on them being defined in the spec, e.g:

```
x64:
    load "bin/loader.x64.o"
        make pic

    load "bin/coff.x64.o"
        make object
        export
        link "my_data"

    export
```

The Crystal Palace JAR archive exposes an API designed for external programs to apply specifications. The only class that's [documented](https://tradecraftgarden.org/api/crystalpalace/spec/package-summary.html) is the `LinkSpec`. The idea is to call the static `Parse` method with the path to a spec file, and then the instance'd `run` method to produce the PIC. For example:

```
import crystalpalace.spec.*;
import crystalpalace.util.*;

...

var spec = LinkSpec.Parse("/path/to/spec");
var capability = CrystalUtils.readFromFile("/path/to/capability");
var args = new HashMap();
var pic = spec.run(capability, args);
```

💡

Under the hood, `run` looks at the MZ header of the provided capability and calls `runDll` if it's a DLL and `runObject` if it's a COFF. Furthermore, `runDll` automatically adds `"$DLL"` to the argument HashMap and `runObject` adds `"$OBJECT"`. That's why these variables work in spec files without you needing to provide them explicity in a HashMap, or with the `link` tool.

Pretty simple really - and quite easy to replicate what the CLI tools do.

However, I wanted to explore the possibility of using/abusing the API to create PIC without a pre-defined spec file. To that end, I wrote a basic "COFF Merger" app:

![](https://rastamouse.me/content/images/2025/09/image-1.png)

This merges the provided COFFs and combines them with the provided loader (basically what I wrote about in the [last post](https://rastamouse.me/modular-pic-c2-agents-reprise/)). It also allows you to toggle the link-time optimization, function order randomization, and code mutator options. The output is obviously a PIC blob that can be injected into a process.

Even though it's not documented, the `SpecParser` class (which is what `LinkSpec.Parse` uses to parse a specification file) is set to public and allows you to pass raw specification content, rather than the path to a specification file. A `SpecParser` instance also has a `getSpec` method, which returns a functional `LinkSpec`.

```
var content = "...";
var parser = new SpecParser();
parser.parse(content, "foobar.spec");
var spec = parser.getSpec();
var args = new HashMap();
var pic = spec.buildPic("x64", args);
```

The `buildPic` method also differs from `run` as it doesn't attempt to check what capabilities are being provided, and therefore doesn't add anything to the HashMap for you.

To build the actual specification content, I just used a `StringBuilder` based on the values populated in the UI:

```
var arch = x64CheckBox.isSelected() ? "x64" : "x86";

var sb = new StringBuilder();

sb.append(arch).append(":\n");

// reflective loader
sb.append("push $LOADER\n");
sb.append("make pic\n");

// coffs
var coffPaths = coffList.getText().split("\n");

// push the first coff
sb.append("push $COFF0\n");

// create coff exporter
sb.append("make coff\n");

// merge the remaining coffs
for (int i = 1; i < coffPaths.length; i++) {
    sb.append("push $COFF").append(i).append("\n");
    sb.append("merge\n");
}

// export them
sb.append("export\n");

// now turn merged coffs into a pico
sb.append("make object");

// add any optimizations
if (optimizeCheckBox.isSelected())
    sb.append(" +optimize");
if (discoCheckBox.isSelected())
    sb.append(" +disco");
if (mutateCheckBox.isSelected())
    sb.append(" +mutate");

sb.append("\n");

// export pico and link to reflective loader
sb.append("export\n");
sb.append("link \"merged_pico\"\n");

// export the lot
sb.append("export");

var content = sb.toString();
```

This produces a string that looks something like this:

```
x64:
push $LOADER
make pic
push $COFF0
make coff
push $COFF1
merge
export
make object +optimize +disco +mutate
export
link "merged_pico"
export
```

💡

Fortunately, Crystal Palace is not sensitive to indenting.

After parsing the above spec, we need to populate the HashMap with the `$LOADER` and `$COFF` variables. This needs to be the raw bytes of each file.

```
var args = new HashMap();

// read the loader
args.put("$LOADER", CrystalUtils.readFromFile(loaderPath.getText()));

// read each coff
for (int i = 0; i < coffPaths.length; i++) {
    args.put("$COFF" + i, CrystalUtils.readFromFile(coffPaths[i]));
}

// build the pic
var pic = spec.buildPic(arch, args);
```

Testing the output with `run.x64.exe` shows that it worked as expected.

![](https://rastamouse.me/content/images/2025/09/image-2.png)

## Closing

I have no idea if the `SpecParser` class being public is by design or just an oversight. Given that only `LinkSpec` has published documentation, I assume it's the only intended way to use the API, rather than what I have written here. It would be cool if there was a "SpecBuilder" class that provided a fluent API to build the spec without parsing string commands. Maybe something like:

```
var builder = new SpecBuilder();
builder.push("$LOADER");
builder.makePic().optimize();
builder.push("$COFF");
builder.makeObject().optimize().disco().mutate();
builder.export();
builder.link("my_data");
builder.export();

var spec = builder.toSpec();

var args = new HashMap();
args.put("$LOADER", [loader bytes]);
args.put("$COFF", [coff bytes]);

var pic = spec.buildPic("x64", args);
```

But perhaps this is straying into use-cases that CP isn't intended to accomodate and that I have nothing better to do on a Sunday afternoon...

### Published by:

[![Rasta Mouse](https://www.gravatar.com/avatar/2b44f5ca5458931c49e1fa57da6705c1?s=250&r=x&d=mp)](/author/rasta/ "Rasta Mouse")

Rasta Mouse © 2025

* [Sign up](#/portal/)

[Powered by Ghost](https://ghost.org/)