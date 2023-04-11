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
from kmk.extensions.lock_status import LockStatus
from kmk.handlers.sequences import simple_key_sequence
from kmk.extensions.wpm import WPM

# Uncomment to turn off board LED
# ixel=neopixel.NeoPixel(board.NEOPIXEL, 1)
# ixel.brightness=0.0

# Initialization
keyboard = KMKKeyboard()
layers = Layers()

keyboard.debug_enabled = False
keyboard.extensions.clear()
keyboard.extensions.append(MediaKeys())

# Declarations
FN = KC.MO(1)
XXXXXXX = KC.NO
CAPS_WITH_FN = simple_key_sequence((KC.CAPSLOCK, KC.MO(1),))
NUMS_WITH_FN = simple_key_sequence((KC.NUMLOCK, KC.MO(1),))

# Rotary encoder
encoder_handler = EncoderHandler()
keyboard.modules = [layers, encoder_handler]

# encoder volume control
encoder_handler.pins = ((board.GP27, board.GP26, None, False, 4),)
encoder_handler.map = [((KC.AUDIO_VOL_DOWN, KC.AUDIO_VOL_UP),)]

# Keys (row and column pinout)
keyboard.col_pins = (board.GP25, board.GP24, board.GP23, board.GP22, board.GP21, board.GP19, board.GP18, board.GP16, board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP9, board.GP8, board.GP7, board.GP1, board.GP0)
keyboard.row_pins = (board.GP15, board.GP6, board.GP5, board.GP4, board.GP3, board.GP2)
keyboard.diode_orientation = DiodeOrientation.COL2ROW


# LEDs
rgb = RGB(pixel_pin=board.GP17, num_pixels=106, val_limit=25, val_step=2, val_default=4,
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

# Keymap
keyboard.keymap = [
    [KC.GRAVE, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, KC.PGDOWN, KC.PGUP, KC.RGB_TOG, KC.KP_SLASH, KC.AUDIO_MUTE,
     KC.GESC, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINUS, KC.EQUAL, KC.BSPACE, KC.HOME, NUMS_WITH_FN, KC.KP_8, KC.KP_MINUS,
     KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRACKET, KC.RBRACKET, KC.BSLASH, KC.END, KC.KP_7, KC.KP_6, KC.KP_ASTERISK,
     CAPS_WITH_FN, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCOLON, KC.QUOTE, KC.ENTER, KC.DELETE, KC.KP_4, KC.KP_5, KC.KP_3, KC.KP_9,
     KC.LSHIFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMMA, KC.DOT, KC.SLASH, XXXXXXX, KC.RSHIFT, KC.UP, KC.KP_1, KC.KP_2, KC.KP_DOT, KC.KP_PLUS,
     KC.LCTRL, KC.LGUI, KC.LALT, KC.LCTL(KC.Z), KC.LWIN(KC.LSFT(KC.S)), KC.SPACE, KC.LWIN(KC.E), KC.LCTL(KC.C), KC.LCTL(KC.V), KC.RALT, KC.APPLICATION, FN, KC.RCTRL, KC.LEFT, KC.DOWN, KC.RIGHT, KC.KP_0, KC.PENT],

    # Next layer here (when you press fn button)
    [XXXXXXX, KC.MEDIA_PLAY_PAUSE, KC.MEDIA_STOP, KC.MEDIA_PREV_TRACK,  KC.MEDIA_NEXT_TRACK, KC.AUDIO_VOL_DOWN, KC.AUDIO_VOL_UP, KC.AUDIO_MUTE, XXXXXXX, KC.BRIGHTNESS_DOWN, KC.BRIGHTNESS_UP, XXXXXXX, XXXXXXX, KC.RGB_VAD, KC.RGB_VAI, XXXXXXX, XXXXXXX, XXXXXXX,
    KC.GRAVE, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, KC.INSERT, KC.SCROLLLOCK, XXXXXXX, XXXXXXX,
    KC.TAB, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
    CAPS_WITH_FN, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
    KC.LSHIFT, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
    KC.LCTRL, KC.LGUI, KC.LALT, XXXXXXX, XXXXXXX, KC.SPACE, XXXXXXX, XXXXXXX, XXXXXXX, KC.RALT, KC.LGUI,FN, KC.RCTRL, KC.LEFT, KC.DOWN, KC.RIGHT,XXXXXXX, XXXXXXX],
    ]

# OLED display
keyboard.SCL=board.GP29
keyboard.SDA=board.GP28

oled_ext = Oled(
    OledData(
        corner_one={0:OledReactionType.STATIC,1:["layer"]},
        corner_two={0:OledReactionType.LAYER,1:["1","2"]},
        corner_three={0:OledReactionType.STATIC,1:[""]},
        corner_four={0:OledReactionType.STATIC,1:["NumLk"]},
        corner_five={0:OledReactionType.STATIC,1:["wpm"]},
        corner_six={0:OledReactionType.STATIC,1:["ScrlLk"]},
        ),
        toDisplay=OledDisplayMode.TXT,flip=True)

# created a class to display CapsLock/Lower or NumLock/NumUnlock on OLED
class OLEDLockStatus(LockStatus):
    def set_lock_oled(self):
        caps = ""
        nums = "NumLk"
        scroll = ""
        if self.get_caps_lock():
            caps = "Caps"
        else:
            caps = ""
        if self.get_num_lock():
            nums = "NumLk"
        else:
            nums= ""
        if self.get_scroll_lock():
            scroll = "ScrlLk"
        else:
            scroll = ""
        oled_ext._views[2] = {0:OledReactionType.STATIC,1:[caps]}
        oled_ext._views[3] = {0:OledReactionType.STATIC,1:[nums]}
        oled_ext._views[5] = {0:OledReactionType.STATIC,1:[scroll]}

        keyboard.sandbox.lock_update = 1

    def after_hid_send(self, sandbox):
        super().after_hid_send(sandbox)
        if self.report_updated:
            self.set_lock_oled()

keyboard.extensions.append(oled_ext)
keyboard.extensions.append(OLEDLockStatus())

wpm_ext = WPM()
keyboard.extensions.append(wpm_ext)
print(wpm_ext.calculate_wpm())

if __name__ == '__main__':
    keyboard.go()
