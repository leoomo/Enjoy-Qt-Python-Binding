## diff listView, treeView and tableView

 - listView 显示相同 item 的组合，跟 Python list 概念相似
 - tree 显示二维表里面的数据, 坐标、目录
 - table 显示有层次的 list, like the layout of a spreadsheet application, 
    such as Microsoft Excel, Apple Numbers or NeoOffice Presentation on Mac OS X.

|| widget\features || horizontal or vertical headers ||
| QListView | x |
| QTreeView | v |
| QTableView | _ |


QAbstractItemModel

 - QAbstractListModel
    - QStringListModel
      - QHelpIndexModel

 - QStandardItemModel

 - QFileSystemModel

 - QAbstractTableModel
    - QSqlQueryModel
       - QSqlTableModel
         - QSqlRelationalTableModel

 - QAbstractProxyModel
    - QSortFilterProxyModel

 - QDirModel
 - QHelpContentModel
 - QProxyModel


QAbstractScrollArea
 - QAbstractItemView
   - QColumnView
   - QHeaderView
   - QListView
     - QListWidget
   - QTableView
     - QTreeWidget
   - QTreeView
     - QTableWidget

QAbstractItemDelegate
 - QItemDelegate
 - QStyledItemDelegate

## Logo resources

Ubuntu
http://www.ubuntu.com

Mac OS X
http://www.guidebookgallery.org/screenshots/macosx103

Plan9
http://plan9.bell-labs.com/plan9/

## External links

 - [Qt Reference Documentation - Model/View Programming](http://doc.qt.nokia.com/latest/model-view-programming.html)
