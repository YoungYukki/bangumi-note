import sys
sys.dont_write_bytecode = True


if __name__ == '__main__':
    from plugins import manager, screenshot
    screenshot(manager())
