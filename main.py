from kivy.app import App 
from kivy.uix.button import Button 
from plyer import notification 

class MyApp(App): 
    def build(self): 
       return Button(text="Show Notification", 
       font_size=32, 
       on_release=self.ShowNotification 
       ) 
    def ShowNotification(self, instance): 
        notification.notify( 
            title="Hi", 
            message="Please subscribe me", 
            app_icon="icon.ico" 
        )

MyApp().run() 
