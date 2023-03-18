print("Starting")
import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()
encoder_handler = EncoderHandler()
layers = Layers()

keyboard.modules = [layers, encoder_handler]

# Keys
keyboard.col_pins = (board.GP26, board.GP25, board.GP24, board.GP23, board.GP22, board.GP19, board.GP18, board.GP16, board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP9, board.GP8, board.GP7, board.GP1, board.GP0)
keyboard.row_pins = (board.GP15, board.GP6, board.GP5, board.GP4, board.GP3, board.GP2)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.ESCAPE, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, KC.INSERT, KC.DELETE, KC.PGUP, KC.KP_SLASH, KC.MUTE, 
     KC.TILDE, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINUS, KC.EQUAL, KC.BSPACE, KC.PGDOWN, KC.NUMLOCK, KC.KP_8, KC.KP_MINUS, 
     KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRACKET, KC.RBRACKET, KC.BSLASH, KC.HOME, KC.KP_7, KC.KP_6, KC.KP_ASTERISK,
     KC.CAPSLOCK, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCOLON, KC.QUOTE, KC.ENTER, KC.END, KC.KP_4, KC.KP_5, KC.KP_3, KC.KP_9,
     KC.LSHIFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMMA, KC.DOT, KC.SLASH, KC.xxxxxxx, KC.RSHIFT, KC.UP, KC.KP_1, KC.KP_2, KC.KP_DOT, KC.KP_PLUS,
     KC.LCTRL, KC.LGUI, KC.LALT, KC.LWIN(KC.LSFT(KC.S)), KC.SCROLLLOCK, KC.SPACE, KC.LWIN(KC.E), KC.LCTL(KC.C), KC.LCTL(KC.V), KC.RALT, KC.APPLICATION, FN, KC.RCTRL, KC.LEFT, KC.DOWN, KC.RIGHT, KC.KP_0, KC.KP_EQUAL]

    # Next layer here
]

# Rotary encoder
encoder_handler.pins = (
    (board.GP27, board.GP26, None,)
)

encoder_handler.map = [ ((KC.VOLD, KC.VOLU),), #volume control
                        ]

if __name__ == '__main__':
    keyboard.go()