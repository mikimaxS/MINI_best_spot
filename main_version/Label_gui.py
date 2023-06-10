# ====================        IMPORTS         ====================
import ttkbootstrap as ttk
import model
# ================================================================

# ====================    CONST VARIABLES     ====================
SIZE_FONT = 14

# noinspection SpellCheckingInspection
titles = ["Czy będziesz współpracować z innymi studentami czy uczyć się samemu w ciszy?",
          "Czy przeszkadza Ci hałas?",
          "Czy będziesz potrzebował/a dostępu do komputera?",
          "Jaki teraz jest czas?", "Przerwa/zajecia"]

# noinspection SpellCheckingInspection
titles2 = ["NAJLEPSZE DOPASOWANIE", "break", "kanapy przy wejsciu", "laboratorium komputerowe (311)",
           'KLUB WRS w "nodze"', "stoliki pod sala 311", "biblioteka glowna"]
# ================================================================

# ====================    CREATE FUNCTION     ====================
def create(question_index: int, frame):
    return ttk.Label(master = frame, bootstyle = "default", text = titles[question_index], font = ("default", SIZE_FONT))
# ================================================================

# ====================   CREATE_2 FUNCTION    ====================
def create_2(question_index: int, frame, index):
    if question_index == 0:
        return ttk.Label(master = frame, bootstyle = "default", text = titles2[question_index],
                         font = ("default", SIZE_FONT + 8), style = "warning")
    else:
        return ttk.Label(master = frame, bootstyle = "default", text = titles2[index[question_index - 1] + 1],
                         font = ("default", SIZE_FONT))
# ================================================================
