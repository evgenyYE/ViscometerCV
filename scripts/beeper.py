import winsound
import threading

def beep(if_allowed: bool = False) -> None:
    if if_allowed:
        def beeper():
            frequency = 2500  # Set Frequency To 2500 Hertz
            duration = 10000  # Set Duration To 1000 ms == 1 second
            winsound.Beep(frequency, duration)

        threading.Thread(target=beeper).start()