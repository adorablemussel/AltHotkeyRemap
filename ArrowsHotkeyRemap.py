from pynput import keyboard, mouse

mouse_controller = mouse.Controller()
scroll_pressed = False

def on_press(key):
    global scroll_pressed
    if key in (keyboard.Key.left, keyboard.Key.right) and not scroll_pressed:
        mouse_controller.press(mouse.Button.middle)
        scroll_pressed = True
    elif key == keyboard.Key.esc:
        print("Closing...")
        return False  

def on_release(key):
    global scroll_pressed
    if key in (keyboard.Key.left, keyboard.Key.right) and scroll_pressed:
        mouse_controller.release(mouse.Button.middle)
        scroll_pressed = False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("The ← and → keys now act as the scroll (middle mouse button). Press ESC to exit.")
    listener.join()
