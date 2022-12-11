I saw a youtube video of "Doom In Notepad" so I thought it would be funny to use Python to make a generic screen-grabbing ASCII viewer.

If the screen being displayed is watching that youtube video this could be called "Doom In Notepad... In Notepad."




Uses PIL to greyscale-convert the grabbed screen and approximate it with ASCII symbols.
Then the Microsoft Windows API is used to constantly change a Notepad window handle's text to the ASCII text.
With the Notepad window's text format set to sufficiently small enough characters it works quite well.
