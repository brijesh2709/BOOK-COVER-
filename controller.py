# imports model and view
import model as b
import view as v


# a new class open source controller
class opensourcecontroller:

    # initialize the view class
    def __init__(self):
        self.x = v.Main_GUI()

    # links the model and view
    def photo(self, txt):
        search_image = b.Opensourcemodel()
        y = search_image.sub_url_open(txt)
        x = search_image.url_open(y)
        return x
    
    # prints the GUI screen
    def GUI_screen(self):
        self.x.run()

# main functionality of the program       
if __name__ == '__main__':
    u = opensourcecontroller()
    u.GUI_screen()
