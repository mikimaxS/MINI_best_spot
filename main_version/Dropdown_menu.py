# ====================        IMPORTS         ====================
import ttkbootstrap as ttk
# ================================================================

# ====================    CONST VARIABLES     ====================
FONT_SIZE = 14
MENU_SIZE = 20
# ================================================================

# ====================      DMENU CLASS       ====================
class Dropdown_menu:
    # ====================       VARIABLES        ====================
    CHOSEN = ""  # I don't know if this should be initialized or not (or maybe initialized with __init__() ))
    # ================================================================

    # ====================    CREATE FUNCTION     ====================
    def create(self, root, VALUES, default):  # self makes sure it is non-static
        # ====================     CHOSEN DEFAULT     ====================
        self.CHOSEN = default
        # ================================================================

        # ====================       FUNCTIONS        ====================
        def fun(x):
            self.CHOSEN = x[0]
            my_menu.config(text = x[0], bootstyle = x[1])
        # ================================================================

        # ========================CREATE A MENUBUTTON ====================
        style = ttk.Style(theme = "darkly")
        my_menu = ttk.Menubutton(root, text = default, bootstyle = "secondary")
        my_menu.config(width = MENU_SIZE)

        # configure the style of the menubutton with larger font
        style.configure("secondary.TMenubutton", font = ("default", FONT_SIZE))
        style.configure("info.TMenubutton", font = ("default", FONT_SIZE))
        style.configure("danger.TMenubutton", font = ("default", FONT_SIZE))
        style.configure("success.TMenubutton", font = ("default", FONT_SIZE))
        style.configure("warning.TMenubutton", font = ("default", FONT_SIZE))

        # create inside menu
        inside_menu = ttk.Menu(my_menu, font = ("default", FONT_SIZE))

        # add items to our inside menu
        item_var = ttk.StringVar()
        for x in VALUES:
            inside_menu.add_radiobutton(label = x[0], variable = item_var, command = lambda x = x: fun(x))

        # associate the inside menu with the menubutton
        my_menu['menu'] = inside_menu
        # ================================================================

        return my_menu
    # ================================================================

# ================================================================
