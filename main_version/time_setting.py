from datetime import datetime

def get_now():
    d = datetime.now().hour
    if d < 10:
        return 0
    elif 10 <= d < 13:
        return 1
    elif 13 <= d < 16:
        return 2
    elif 16 <= d < 19:
        return 3
    else:
        return 0

def get_prze_lek():
    m = datetime.now().minute
    if 0 <= m <= 15:
        return 0
    else:
        return 1
