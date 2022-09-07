def sus(speed: int = 1):
    import time
    import winsound

    note2freq = lambda n: int(2 ** ((n - 49) / 12) * 440)
    duration = lambda t: int(t / speed)
    play = lambda f, t: winsound.Beep(note2freq(f), duration(t))
    
    for note in (40, 43, 45, 46, 45, 43, 40):
        play(note, 250)
    time.sleep(1 / speed)
    for note in (38, 42, 40):
        play(note, 175)

# ඞ sus
sus()
