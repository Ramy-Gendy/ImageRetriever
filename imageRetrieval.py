from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import AsyncImage
import requests
from random import randrange


class RootWidget(StackLayout):

    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(RootWidget, self).__init__(**kwargs)


class MainApp(App):

    def build(self):
        self.root = root = RootWidget()
        self.search_query_input = TextInput(
            text="Hello World",
            size_hint=(.5, .1),
            multiline=False)

        self.search_button = Button(
            text="Get An Image",
            size_hint=(.5, .1)
        )

        self.search_button.bind(on_press=self.searchAndDisplay)
        root.add_widget(self.search_query_input)
        root.add_widget(self.search_button)
        self.image_widget = AsyncImage(source='https://i.ytimg.com/vi/xRZB5KBLdOA/maxresdefault.jpg')
        root.add_widget(self.image_widget)
        return root

    def searchAndDisplay(self,event):
        query = self.search_query_input.text
        url = 'https://www.googleapis.com/customsearch/v1?key=AIzaSyDXXdpKNA1pQF9YjwIO56KRkL2yJfQFkl0&cx=48a33cb3cfeacb82b&searchType=image&q=' + query
        data = requests.get(url).json()

        search_items = data.get('items')

        print("Searching")
        i = randrange(10)
        image = search_items[i].get('link')
        print(image)
        self.image_widget.source = image
        
            
        


if __name__ == '__main__':
    MainApp().run()
