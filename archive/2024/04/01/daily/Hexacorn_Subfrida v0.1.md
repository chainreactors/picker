---
title: Subfrida v0.1
url: https://www.hexacorn.com/blog/2024/03/31/subfrida-v0-1/
source: Hexacorn
date: 2024-04-01
fetch_date: 2025-10-04T12:15:07.993216
---

# Subfrida v0.1

[Skip to primary content](#content)

# [Hexacorn](https://www.hexacorn.com/blog/)

## Hexacorn

Search

### Main menu

* [Home](https://www.hexacorn.com/)
* [Services](https://www.hexacorn.com/services.html)
* [Products & Freebies](https://www.hexacorn.com/products_and_freebies.html)
* [Case Studies](https://www.hexacorn.com/case_studies.html)
* [Contact Us](https://www.hexacorn.com/contact.html)

### Post navigation

[← Previous](https://www.hexacorn.com/blog/2024/03/16/stuffing-up-the-windir-env-var-with-the-space/)
[Next →](https://www.hexacorn.com/blog/2024/04/05/the-art-of-cutting-corners/)

# Subfrida v0.1

Posted on [2024-03-31](https://www.hexacorn.com/blog/2024/03/31/subfrida-v0-1/ "12:57 am")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

As many of you know, I am a big fan of [Frida](https://frida.re/) framework and I love its intuitiveness and flexibility, especially when it comes to auto-generating handlers for hooked functions, even if they are randomly chosen.

In my older Frida [Delphi](https://www.hexacorn.com/blog/2022/02/20/delphi-api-monitoring-with-frida-part-3/) project I focused on functions that I could define. Today, I will focus on functions that are unknown.

How?

We are going to write an IdaPython script that will generate simple logging/tracing function stubs for all the subroutines that IDA ‘sees’ inside the executable.

When you load any executable into IDA it parses the analyzed program’s segments, recognizes the code, and… in it – many functions. We don’t really know or care what they do, other than being aware that they exist. FLIRT signatures help in recognizing some, but it is non-trivial, as well.

So, the value-proposition here is that we will try to use Frida to run the program and log calls to every subroutine ‘discovered’ or ‘recognized’ by IDA, and print out the strings that subroutine arguments may point to when the function is executed — for this exercise we will try to log ANSI and WIDE strings potentially passed to these functions, and strings delivered in their output.

Why?

This may help us to quickly understand the inner-workings of the program, and in some lucky cases extract IOCs, and overall, help in reverse engineering efforts. Especially for samples that are written in modern languages like Rust, Go, Nim.

The idea sounds great, but there is a problem. One that I don’t know how to solve, but by publishing my partial research, I hope someone more knowledgeable will help me to address… The problem is that any error in your OnEnter or OnLeave Frida handler function forces the script to bail out.

It’s a pity.

My ‘original’ code for this exercise looked like this:

```
import os
import shutil
import idautils
import idaapi
import idc
import re

idf = idc.get_idb_path()

print ("Original IDA File: %s" % idf)

m = re.match(r"\.idb", idf)

arch = 0
if m:
   arch = 32
   print ("- 32-bit")
else:
   arch = 64
   print ("- 64-bit")

if arch == 32:
   idf = idf.replace('.idb','.frida')
else:
	 idf = idf.replace('.i64','.frida')

print ("Output idf: %s" % idf)

filename=re.sub(r"\.frida", "", re.sub(r"^.+[\\/]", "", idf))
handlers=re.sub(r"[^\\/]+$", "", idf) + "__handlers__" + "/" + filename + "/"

if os.path.isdir(handlers):
	 print ("Deleting old handlers directory: %s" % handlers)
	 shutil.rmtree(handlers)

os.mkdir(handlers)

print ("Saving frida input file to '%s'" % idf)
print ("Saving '%s' handlers to '%s'" % (filename, handlers) )
g = open(idf, 'w')
base = idaapi.get_imagebase()
for f in idautils.Functions():
    dism_addr = list(idautils.FuncItems(f))
    ofs = "%X"%(dism_addr[0]-base)
    g.write ("-a %s!0x%s\n" % (filename, ofs))
    h = open(handlers + "/" + "sub_"+ofs+".js", 'w')
    h.write("""
{

  onEnter(log, args, state) {
    out = 'onenter: """+ofs+"""\\n'

    log(out)

    for (i = 0; i < 4; i++)
    {
       if (args[i]>0)
       {
          console.log(args[i].readUtf8String());
          console.log(args[i].readUtf16String());
          a = args[i].readUtf8String(256)
          if (a > 0)
          {
             out = out + ' [' + i + ']a ' + JSON.stringify(a) + '\\n'
          }
          w = args[i].readUtf16String(256)
          if (w > 0)
          {
             out = out + ' [' + i + ']w ' + JSON.stringify(w) + '\\n'
          }
       }
       this.args [i] = args [i]
    }

    if (typeof state ['log_file'] === 'undefined' || state ['log_file'] === null)
    {
        state ['log_file']=new File('logfile.bin', 'wb');
    }

    if (! (typeof state ['log_file'] === 'undefined' || state ['log_file'] === null) )
    {
        state ['log_file'].write(out);
        state ['log_file'].flush();
    }

  },

  onLeave(log, retval, state) {
    out = 'onenter: """+ofs+"""\\n'

    log(out)

    for (i = 0; i < 4; i++)
    {
       if (this.args[i]>0)
       {
          console.log(this.args[i].readUtf8String());
          console.log(this.args[i].readUtf16String());
          a = this.args[i].readUtf8String(256)
          if (a > 0)
          {
             out = out + ' [' + i + ']a ' + JSON.stringify(a) + '\\n'
          }
          w = this.args[i].readUtf16String(256)
          if (w > 0)
          {
             out = out + ' [' + i + ']w ' + JSON.stringify(w) + '\\n'
          }
       }
    }

    if (typeof state ['log_file'] === 'undefined' || state ['log_file'] === null)
    {
        state ['log_file']=new File('logfile.bin', 'wb');
    }

    if (! (typeof state ['log_file'] === 'undefined' || state ['log_file'] === null) )
    {
        state ['log_file'].write(out);
        state ['log_file'].flush();
    }
  }
}
    """)
    h.close()

g.close()
```

When executed in a Windows IDA the code generates:

* a .frida file with a list of RVA addresses for *frida-trace* to intercept
* a list of generic handlers and their code for all these subroutines that simply try to log 4 first arguments passed to these functions – both at the entry point, and the function return.

Unfortunately, Frida is very sensitive and any error during processing of these handlers forces a bail out :(.

So, after toying around with different variations of this, and similar code, I came up with this dumb script:

```
import os
import shutil
import idautils
import idaapi
import idc
import re

idf = idc.get_idb_path()

print ("Original IDA File: %s" % idf)

m = re.match(r"\.idb", idf)

arch = 0
if m:
   arch = 32
   print ("- 32-bit")
else:
   arch = 64
   print ("- 64-bit")

if arch == 32:
   idf = idf.replace('.idb','.frida')
else:
	 idf = idf.replace('.i64','.frida')

print ("Output idf: %s" % idf)

filename=re.sub(r"\.frida", "", re.sub(r"^.+[\\/]", "", idf))
handlers=re.sub(r"[^\\/]+$", "", idf) + "__handlers__" + "/" + filename + "/"

if os.path.isdir(handlers):
	 print ("Deleting old handlers directory: %s" % handlers)
	 shutil.rmtree(handlers)

os.mkdir(handlers)

print ("Saving frida input file to '%s'" % idf)
print ("Saving '%s' handlers to '%s'" % (filename, handlers) )
g = open(idf, 'w')
base = idaapi.get_imagebase()
for f in idautils.Functions():
    dism_addr = list(idautils.FuncItems(f))
    ofs = "%X"%(dism_addr[0]-base)
    g.write ("-a %s!0x%s\n" % (filename, ofs))
    h = open(handlers + "/" + "sub_"+ofs+".js", 'w')
    h.write("""
{

  onEnter(log, args, state) {
    out = 'onenter: """+ofs+"""\\n'
    log(out)

    for (i = 0; i < 4; i++)
    {
       console.log(' - '+ args[i] + 'a->' + args[i].readUtf8String()+'\\n');
       console.log(' - '+ args[i] + 'w->' + args[i].readUtf16String()+'\\n');
       this.args [i] = args [i]
    }
  },

  onLeave(log, retval, state) {
    out = 'onenter: """+ofs+"""\\n'
    log(out)
    for (i = 0; i < 4; i++)
    {
       console.log(' - '+ this.args[i] + 'a->' + this.args[i].readUtf8String()+'\\n');
       console.log(' - '+ this.args[i] + 'w->' + this.args[i].readUtf16String()+'\\n');
    }

  }
}
    """)
    h.close()

g.close()
```

It at least populates the *console.log* file with anything that *may ...