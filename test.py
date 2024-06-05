from plyer import notification


def show_notification():
    notification.notify(
        title='Hello',
        message='This is a test notification',
        app_icon=None,  # Path to an .ico file
        app_name="k-chat"
    )


show_notification()
