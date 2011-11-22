# Notes On Resources

Qt resource system 用于在可执行应用程序里面保存二进制文件(icons, translation files 等等)。

 - [The Qt Resource System](http://doc.qt.nokia.com/latest/resources.html)
 - [Resource Compiler (rcc)](http://doc.qt.nokia.com/latest/rcc.html)

rcc means Qt's **r**esour**c**e **c**ompiler .


## Example

    find . | grep -v DS_Store

    .
    ./foo.py
    ./resources
    ./resources/icons
    ./resources/icons/camera.png
    ./resources/icons/iblah.png
    ./resources/icons/mic.png
    ./resources/icons/send_files.png


    rcc -project -o bar.qrc
    pyrcc4-2.7 -no-compress bar.qrc -o bar.py


in foo.py

    import bar

    ...
    pix = QtGui.QPixmap(":/resources/icons/camera.png")