print("Starting")
import board
import neopixel
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from kmk.extensions.RGB import RGB
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.peg_oled_Display import Oled,OledDisplayMode,OledReactionType,OledData
from kmk.extensions.rgb import AnimationModes

# Uncomment to turn off board LED
# ixel=neopixel.NeoPixel(board.NEOPIXEL, 1)
# ixel.brightness=0.0

# Initialization
keyboard = KMKKeyboard()
layers = Layers()

# keyboard.debug_enabled = True
keyboard.extensions.clear()
keyboard.extensions.append(MediaKeys())

# Declarations
FN = KC.MO(1)
XXXXXXX = KC.NO

# Rotary encoder
encoder_handler = EncoderHandler()
keyboard.modules = [layers, encoder_handler]

# volume control and brightness when fn is held
encoder_handler.pins = ((board.GP27, board.GP26, None, False, 4),)
encoder_handler.map = [((KC.AUDIO_VOL_DOWN, KC.AUDIO_VOL_UP),)]

# Keys
keyboard.col_pins = (board.GP25, board.GP24, board.GP23, board.GP22, board.GP21, board.GP19, board.GP18, board.GP16, board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP9, board.GP8, board.GP7, board.GP1, board.GP0)
keyboard.row_pins = (board.GP15, board.GP6, board.GP5, board.GP4, board.GP3, board.GP2)
keyboard.diode_orientation = DiodeOrientation.COL2ROW


# LEDs
rgb = RGB(pixel_pin=board.GP17, 
        num_pixels=106, 
        val_limit=25, 
        val_step=2, 
        val_default=2, 
        hue_step=5,
        hue_default=0,
        sat_step=5,
        sat_default=100,
        rgb_order=(1, 0, 2),
        animation_speed=1,
        breathe_center=1,  # 1.0-2.7a
        knight_effect_length=3,
        animation_mode=AnimationModes.STATIC,
        reverse_animation=False,
        refresh_rate=60,)
keyboard.extensions.append(rgb)

# Key map
keyboard.keymap = [
    [KC.ESCAPE, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, KC.PGUP, KC.PGDOWN, KC.INSERT, KC.KP_SLASH, KC.AUDIO_MUTE,
     KC.TILDE, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINUS, KC.EQUAL, KC.BSPACE, KC.HOME, KC.NUMLOCK, KC.KP_8, KC.KP_MINUS,
     KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRACKET, KC.RBRACKET, KC.BSLASH, KC.END, KC.KP_7, KC.KP_6, KC.KP_ASTERISK,
     KC.CAPSLOCK, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCOLON, KC.QUOTE, KC.ENTER, KC.DELETE, KC.KP_4, KC.KP_5, KC.KP_3, KC.KP_9,
     KC.LSHIFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMMA, KC.DOT, KC.SLASH, XXXXXXX, KC.RSHIFT, KC.UP, KC.KP_1, KC.KP_2, KC.KP_DOT, KC.KP_PLUS,
     KC.LCTRL, KC.LGUI, KC.LALT, KC.RGB_TOG, KC.LWIN(KC.LSFT(KC.S)), KC.SPACE, KC.LWIN(KC.E), KC.LCTL(KC.C), KC.LCTL(KC.V), KC.RALT, KC.APPLICATION, FN, KC.RCTRL, KC.LEFT, KC.DOWN, KC.RIGHT, KC.KP_0, KC.PENT],

    # Next layer here (when you press fn button)
    [KC.ESCAPE, KC.MEDIA_PLAY_PAUSE, KC.MEDIA_STOP, KC.MEDIA_PREV_TRACK,  KC.MEDIA_NEXT_TRACK, KC.AUDIO_VOL_UP, KC.AUDIO_VOL_DOWN, KC.AUDIO_MUTE, XXXXXXX, KC.BRIGHTNESS_UP, KC.BRIGHTNESS_DOWN, XXXXXXX, XXXXXXX, KC.RGB_VAI, KC.RGB_VAD, XXXXXXX, XXXXXXX, XXXXXXX,
    XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
    KC.TAB, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
    KC.CAPSLOCK, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
    KC.LSHIFT, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
    KC.LCTRL, KC.LGUI, KC.LALT, XXXXXXX, XXXXXXX, KC.SPACE, XXXXXXX, XXXXXXX, XXXXXXX, KC.RALT, KC.LGUI,FN, KC.RCTRL, KC.LEFT, KC.DOWN, KC.RIGHT,XXXXXXX, XXXXXXX],
]

# Oled display 
keyboard.SCL=board.GP29
keyboard.SDA=board.GP28

oled_ext = Oled(
    OledData(
        corner_one={0:OledReactionType.STATIC,1:["layer"]},
        corner_two={0:OledReactionType.LAYER,1:["1","2"]},
        corner_three={0:OledReactionType.LAYER,1:["base","raise"]},
        corner_four={0:OledReactionType.LAYER,1:["qwerty","functions"]}
        ),
        toDisplay=OledDisplayMode.TXT,flip=True)
keyboard.extensions.append(oled_ext)

if __name__ == '__main__':
    keyboard.go()
