from typing import Optional

from win32 import win32api, win32gui
import win32con

import image_grab


def change_text(window_handle: int, text: str) -> bool:
    win32api.SendMessage(window_handle, win32con.WM_SETTEXT, None, text)


def find_notepad_window() -> Optional[int]:
    notepad_window_handle = win32gui.FindWindow(None, "Untitled - Notepad")
    return notepad_window_handle


def get_edit_window(notepad_window_handle: int) -> Optional[int]:
    edit_window_handle = win32gui.GetWindow(notepad_window_handle, win32con.GW_CHILD)
    return edit_window_handle


def main():
    notepad_window = find_notepad_window()
    edit_window = get_edit_window(notepad_window)
    for ascii_image in image_grab.generate_ascii_screengrab():
        change_text(edit_window, ascii_image)
    return


if __name__ == "__main__":
    main()
