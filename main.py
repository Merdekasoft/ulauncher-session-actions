import os
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.client.Extension import Extension
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.client.EventListener import KeywordQueryEventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent

class I3wmControlExtension(Extension):
    def __init__(self):
        super(I3wmControlExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener(self.on_keyword_query))
        self.subscribe(ItemEnterEvent, ItemEnterEventListener(self.on_item_enter))

    def on_keyword_query(self, event):
        items = [
            ExtensionResultItem(icon='images/Logout.png',
                                name='Logout',
                                description='Logout from i3wm',
                                on_enter=ExtensionCustomAction('logout', keep_app_open=False)),
            ExtensionResultItem(icon='images/reboot.png',
                                name='Restart',
                                description='Restart the system',
                                on_enter=ExtensionCustomAction('restart', keep_app_open=False)),
            ExtensionResultItem(icon='images/shutdown.png',
                                name='Shutdown',
                                description='Shutdown the system',
                                on_enter=ExtensionCustomAction('shutdown', keep_app_open=False))
        ]
        return RenderResultListAction(items)

    def on_item_enter(self, event):
        action = event.get_data()
        if action == 'logout':
            os.system('i3-msg exit')
        elif action == 'restart':
            os.system('systemctl reboot')
        elif action == 'shutdown':
            os.system('systemctl poweroff')
