from kmk.extensions import Extension
from kmk.kmktime import ticks_diff, ticks_ms

class WPM(Extension):
    def __init__(self, debug=True):
        self.enable = True
        self.history = [0]
        self.timeout = 1000
        self.checkpoint = ticks_ms()
        self.debug = debug
        self.counter = 0
        self.old_wpm = 0
        self.wpm = 0

    def on_runtime_enable(self, sandbox):
        sandbox.wpm = 0
        return

    def on_runtime_disable(self, sandbox):
        sandbox.wpm = None
        return

    def during_bootup(self, sandbox):
        sandbox.wpm = 0
        return

    def before_matrix_scan(self, sandbox):
        return

    def after_matrix_scan(self, sandbox, matrix_update):
        if self.enable:
            new_history = self._add_character(
                matrix_update,
                sandbox.secondary_matrix_update)
            if new_history is not None:
                self.history.append(new_history)
            if len(self.history) > 10:
                self.history.pop(0)
            self.wpm = self.calculate_wpm()

            if self.wpm != 0 and self.wpm != self.old_wpm:
                sandbox.wpm = self.wpm
                print(f'WPM: {self.wpm}')
                if self.debug:
                    print(f'WPM: {self.wpm}')
                self.old_wpm = self.wpm
        return

    def before_hid_send(self, sandbox):
        return

    def after_hid_send(self, sandbox):
        return

    def on_powersave_enable(self, sandbox):
        self.enable = False
        return

    def on_powersave_disable(self, sandbox):
        self.enable = True
        sandbox.wpm = self.wpm
        return

    def _add_character(self, matrix_update, second_update):
        if ticks_diff(ticks_ms(), self.checkpoint) > self.timeout:
            self.checkpoint = ticks_ms()
            ret = self.counter
            self.counter = 0
            return ret
        if matrix_update or second_update:
            self.counter += 1

    def calculate_wpm(self):
        # No, there is no real math here, though it seems to work out sorta.
        return int(sum(self.history[:-1]) * .6)
