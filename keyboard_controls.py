import keyboard

def disable_keyboard():
    for i in range(150):
        keyboard.block_key(i)


def enable_keyboard():
    for i in range(150):
        keyboard.unblock_key(i)