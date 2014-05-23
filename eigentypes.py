############################################################################
## Eigen (http://eigen.tuxfamily.org/) QtCreator Python Debug Helpers
## Author: Steven Lovegrove
############################################################################
## These helpers have been tested with QT Creator 3.1.0 on OSX 10.9.2
## Using lldb-310.2.37. My platform doesn't seem to recognise class namespaces,
## and to function correctly these have been omitted.

from dumper import *

# Eigen::Matrix, expected function name qdump__Eigen__Matrix
# This dumper will work for all template instantiations of Eigen::Matrix and
# typedefs there-of such as Vector3f, MatrixXd, etc.
def qdump__Matrix(d, value):
    m_storage = value[0]["m_storage"]
    m_data = m_storage["m_data"]
    rows = d.numericTemplateArgument(value.type, 1)
    cols = d.numericTemplateArgument(value.type, 2)
    # Test for Eigen::Dynamic dimensions
    if rows==-1:
        rows = int(m_storage["m_rows"])
    if cols==-1:
        cols = int(m_storage["m_cols"])
    size = rows*cols
    if rows == 1 and cols == 1:
        # Just emit single element
        d.putItem( m_data[0][0] )
    else:
        # Emit rows x cols, with data array as child elements
        d.putValue( "%dx%d" % (rows,cols) )
        d.putNumChild(size)
        if d.isExpanded():
            innerType = d.templateArgument(value.type, 0)
            # Check if m_data is an array or pointer on the heap
            if m_data.TypeIsPointerType():
                d.putPlotData(innerType, m_data, size)
            else:
                d.putPlotData(innerType, d.addressOf(value), size)

# Eigen::Array, expected function name qdump__Eigen__Array
# Eigen::Array is organised identically to Eigen::Matrix
def qdump__Array(d, value):
    qdump__Matrix(d, value)

# Eigen::Quaternion, expected function name qdump__Eigen__Quaternion
def qdump__Quaternion(d, value):
    d.putValue( "" )
    d.putNumChild(4)
    if d.isExpanded():
        m_storage = value[0]["m_storage"]
        m_data = m_storage["m_data"]
        innerType = d.templateArgument(value.type, 0)
        d.putPlotData(innerType, d.addressOf(value), 4)
