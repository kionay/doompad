from typing import Optional

from win32 import win32api, win32gui
import win32con

import image_grab


def change_text(window_handle: int, text: str) -> bool:
    result = win32api.SendMessage(window_handle, win32con.WM_SETTEXT, None, text)
    if not result:
        print("error!")
        return win32api.GetLastError()


def find_notepad_window() -> Optional[int]:
    notepad_window_handle = win32gui.FindWindow(None, "Untitled - Notepad")
    return notepad_window_handle

def get_window_class_name(window_handle: int) -> Optional[str]:
    class_name = win32gui.GetClassName(window_handle)
    return class_name

def find_edit_window(notepad_window_handle: int):
    target_window_class_name = "RichEditD2DPT"
    child_handles = []
    def callback(h, l):
        child_handles.append(h)
        return True
    win32gui.EnumChildWindows(notepad_window_handle, callback, None)
    for child_window_handle in child_handles:
        if get_window_class_name(child_window_handle) == target_window_class_name:
            return child_window_handle

def get_edit_window(notepad_window_handle: int) -> Optional[int]:
    edit_window_handle = win32gui.GetWindow(notepad_window_handle, win32con.GW_CHILD)
    return edit_window_handle


def main():
    notepad_window = find_notepad_window()
    edit_window = find_edit_window(notepad_window)
    for ascii_image in image_grab.generate_ascii_screengrab():
        change_text(edit_window, ascii_image)
    return


if __name__ == "__main__":
    main()
