from platform import system


def toast(title, message):
    if system() == 'Linux':
        import notify2 as toaster

        toaster.init('Cryto Prices Getter')
        linux_toast = toaster.Notification('Your coins:', message)
        linux_toast.show()
    elif system() == 'Windows':
        import win10toast as toaster

        win_toast = toaster.ToastNotifier()
        win_toast.show_toast("Your coins:", message, icon_path='get-crypto-prices\\test.ico')
