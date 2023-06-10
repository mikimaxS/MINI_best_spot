# ====================        IMPORTS         ====================
import Dropdown_menu

# ================================================================

# ====================    CONST VARIABLES     ====================
import random
N = 6  # number of questions

# noinspection SpellCheckingInspection
VAL = ["Wspólnie                         ", "Samemu"], \
    ["Tak                              ", "Nie"], \
    ["Tak, mam swojego laptopa         ", "Tak, potrzebuję dostępu do komputera stacjonarnego", "Nie"], \
    ["Rano 08:00-10:00                 ", "Poludnie 10:00-13:00", "Popołudnie 13:00-16:00", "Wieczór 16:00-19:00"], \
    ["Przerwa                          ", "Zajecia"]
# ================================================================

# ====================       VARIABLES        ====================
index = [0, 1, 2, 3, 4, 5]
tmp = ["", "", "", "", ""]
# ================================================================

# ====================      ASSIGN INDEX      ====================
def assign_index(DMenu):
    global index
    global tmp

    for i in range(5):
        if tmp[i] != DMenu[i].CHOSEN:
            for j in range(5):
                tmp[j] = DMenu[j].CHOSEN
            random.shuffle(index)
            return index

    return index
# ================================================================
