QtDebugHelpers
==============

Collection of useful Python debug helpers for use with QtCreator. Package currently includes basic Eigen and Sophus debug formatters for quickly inspecting variable values.

Installation
==============

* OSX 10.9
 Documentation implies that these helpers should function if added to .gdbinit or .lldbinit but I've not been able to get that to work. Instead, symlink these files to the following folder location:
```
ln -s `pwd`/*types.py /Applications/Qt\ Creator.app/Contents/Resources/debugger
```
 and import these python modules by editing ```/Applications/Qt\ Creator.app/Contents/Resources/debugger/lldbbridge.py``` and adding the following lines:
```
from eigentypes import *
from sophustypes import *
```
 For this to work, a recent version of lldb and Qt Creator are required. Please let me know if you come up with a simpler installation method.
* Linux
 Let me know!
* Windows
 Let me know!
