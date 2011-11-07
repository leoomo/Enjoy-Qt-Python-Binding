# System Tray Icon Demo


## Interaction

    click X on main window
        |
        |
        V
    trigger quit confirmation

    if settings["confirm"]:
        show options for config X action
        save settings

    quit or hide main window


(main window state is hide)

single click on tray icon
 -> popup specify window or show main window

mouse over on tray icon
 ->  show rich text menu items or webkit widget


## dialog text

    When you click the close button should me:

     O Minimize to system tray
     O Exit program

    [] Don\'t ask me again


## References

 - http://stackoverflow.com/questions/1414781/prompt-on-exit-in-pyqt-application


## UI Resources

 - /Users/lee/Downloads/mac_apps/adium/Resources/Status Icons/iBubble Status.AdiumStatusIcons/