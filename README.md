<img src="https://github.com/JuliaLWang8/Custom-Keyboard/blob/main/Keyboard.jpg" alt="Keyboard">

# Custom Keyboard

Using RP2040 Stamp with [kmk firmware](http://kmkfw.io/) with the layout below.
<img src="https://github.com/JuliaLWang8/Custom-Keyboard/blob/main/layout.png" alt="Full keyboard layout">


### Features in [code.py](https://github.com/JuliaLWang8/Custom-Keyboard/blob/main/code.py):
- OLED display showing the current keyboard layer, CapsLock, and NumLock in real time
- Second layer of keys activated by pressing FN, switches off when FN is let go (KC.MO in kmk layers)
- Rotary encoder for volume control 
- RGB LEDs for each key - toggled on and off by RGB macro (KC.RGB_TOG)
- Current macros: 
    - M1: undo (Ctrl+Z)
    - M2: screen snipping tool (Win+Shift+S)
    - M3: opening file explorer (Win+E)
    - M4: copy (Ctrl+C)
    - M5: paste (Ctrl+V)

See [kmk/extensions](https://github.com/JuliaLWang8/Custom-Keyboard/tree/main/kmk/extensions) for full extensions classes.

RP2040 stamp pinout for keyboard keymap:
<img src="https://github.com/JuliaLWang8/Custom-Keyboard/blob/main/rp2040stamp_pinout.png" alt="rp2040 matrix">