from ._anvil_designer import MainTemplate
from anvil import *
import anvil.server



class Main(MainTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def Wallpaperbutton_click(self, **event_args):
    wallpaper()
    pass

  def Wallpaperbutton_show(self, **event_args):
    """This method is called when the Button is shown on the screen"""
    pass

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass
