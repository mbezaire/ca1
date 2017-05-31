set obj = CreateObject("Scriptlet.TypeLib")
WScript.StdOut.WriteLine Replace(Replace(obj.GUID,"{",""),"}","")
