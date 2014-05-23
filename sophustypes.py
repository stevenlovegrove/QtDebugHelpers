############################################################################
## Sophus (https://github.com/strasdat/Sophus) QtCreator Python Debug Helpers
## Author: Steven Lovegrove
############################################################################
## These helpers have been tested with QT Creator 3.1.0 on OSX 10.9.2
## Using lldb-310.2.37. My platform doesn't seem to recognise class namespaces,
## and to function correctly these have been omitted.

from dumper import *

# Sophus::SO3Group, expected function name qdump__Sophus__SO3Group
def qdump__SO3Group(d, value):
    coeffs = value["unit_quaternion_"]["m_coeffs"]
    d.putValue("")
    d.putNumChild(1)
    with Children(d):
        d.putSubItem( "Unit Quaternion", coeffs )

# Sophus::RxSO3Group, expected function name qdump__Sophus__RxSO3Group
def qdump__RxSO3Group(d, value):
    coeffs = value["quaternion_"]["m_coeffs"]
    d.putValue("")
    d.putNumChild(1)
    with Children(d):
        d.putSubItem( "Quaternion", coeffs )

# Sophus::SE3Group, expected function name qdump__Sophus__SE3Group
def qdump__SE3Group(d, value):
    quat = value["so3_"]["unit_quaternion_"]["m_coeffs"]
    trans = value["translation_"]
    d.putValue("")
    d.putNumChild(2)
    with Children(d):
        d.putSubItem( "Unit Quaternion", quat )
        d.putSubItem( "Translation", trans )

# Sophus::Sim3Group, expected function name qdump__Sophus__Sim3Group
def qdump__Sim3Group(d, value):
    quat = value["rxso3_"]["quaternion_"]["m_coeffs"]
    trans = value["translation_"]
    d.putValue("")
    d.putNumChild(2)
    with Children(d):
        d.putSubItem( "Quaternion", quat )
        d.putSubItem( "Translation", trans )
