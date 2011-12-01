# Qt On Mac

 - [Qt/Mac Special Features](http://doc.qt.nokia.com/qq/qq18-macfeatures.html)
 - [Best Practice Guides](http://doc.qt.nokia.com/latest/best-practices.html)
 - [Qt Quick](http://doc.qt.nokia.com/latest/qtquick.html)

 - [Qt Quarterly - Qt on Mac OS X using Cocoa](Qt on Mac OS X using Cocoa](http://doc.qt.nokia.com/qq/QtQuarterly28.pdf)

## Native

 - [Qt for Mac OS X - Specific Issues](http://doc.qt.nokia.com/latest/mac-differences.html0
 - [Qt is Mac OS X Native](http://doc.qt.nokia.com/latest/qtmac-as-native.html)

## Window

 - [Window and Dialog Widgets](http://doc.qt.nokia.com/latest/application-windows.html)/The different between Window and Widget
 - [Cocoa Textured Window in QT](http://stackoverflow.com/questions/1413337/cocoa-textured-window-in-qt)

 - [About close() and hide()](http://lists.trolltech.com/qt-interest/2003-03/thread01019-0.html)

## Dock

 - [Getting Dock widget show/hide events](http://www.qtcentre.org/threads/31169-MAC-Getting-Dock-widget-show-hide-events)
 
 - [Mac OS X - Application icon clicked ?](http://lists.trolltech.com/qt-interest/2007-06/msg00820.html)

## Dock icon

 - [Disable the Dock icon for any Application](http://www.macosxtips.co.uk/index_files/disable-the-dock-icon-for-any-application.html)

 - [QT/C++ on MAC - How do I hide my dock icon?](http://stackoverflow.com/questions/4718668/qt-c-on-mac-how-do-i-hide-my-dock-icon)

 - [QT on OSX: Tray Icon - Icon Dock Problem](http://stackoverflow.com/questions/4997245/qt-on-osx-tray-icon-icon-dock-problem)

 - [How to change Qt applications's dock icon at run-time in MacOS?](http://stackoverflow.com/questions/981147/how-to-change-qt-applicationss-dock-icon-at-run-time-in-macos)

 - [cause the application icon to bounce in the dock](http://doc.qt.nokia.com/latest/qapplication.html#alert)


## Dialog

 - [Qt Quarterly - New Ways of Using Dialogs](http://doc.qt.nokia.com/qq/QtQuarterly30.pdf)


## Icon

 - [Does Qt Builder have a built-in tool for editing a toolbar?](http://stackoverflow.com/questions/2752259/does-qt-builder-have-a-built-in-tool-for-editing-a-toolbar)
 

## Thread

 - [Starting Threads with QThread](http://doc.qt.nokia.com/latest/threads-starting.html)

You have to terminate all threads(create from threading.Thread or QtCore.QThread),
before application quit, 
or your application will be freezon, it doesn't show any widgets, not responses for any keyboard/mouse event.

In Activity Monitor, it was mark as 'Python (Not Responding)'.

![alt](quit-in-alive-threads-python-not-responding-20111123.png)

‘It is not safe to use pixmaps outside the GUI thread’

 - [Qt-interest Archive - QPixmap: It is not safe to use pixmaps outside the GUI thread](http://lists.trolltech.com/qt-interest/2008-11/msg00534.html)
 - [QPixmap: It is not safe to use pixmaps outside the GUI thread](http://www.qtcentre.org/threads/41595-QPixmap-It-is-not-safe-to-use-pixmaps-outside-the-GUI-thread)
 - [Qt: Threads and QObjects](http://doc.qt.nokia.com/latest/threads-qobject.html)


 - [How can I change QT GUI widgets on a QMainWindow from a QThread which is a member?](http://stackoverflow.com/questions/1129587/how-can-i-change-qt-gui-widgets-on-a-qmainwindow-from-a-qthread-which-is-a-member)
 - [Qt: Background thread refreshing UI thread](http://stackoverflow.com/questions/2376835/qt-background-thread-refreshing-ui-thread)


problem:

    QThread: Destroyed while thread is still running

solution:



## Signals and Slots

### connect multiple slots to one signal

- [Two different slots for the same signal](http://stackoverflow.com/questions/8264107/two-different-slots-for-the-same-signal)

### arguments pass to emit 

    self.emit(QtCore.SIGNAL("recv_msg( QString, QString, QString )"), sender_user_id, sender_uri, msg)

You must convert msg to unicode object

    msg = web.utils.safeunicode(msg)

## Local

http://developer.qt.nokia.com/wiki/QtLocales
http://doc.qt.nokia.com/latest/qtextstream.html#setLocale
http://stackoverflow.com/questions/7333442/weird-strtod-behaviour
