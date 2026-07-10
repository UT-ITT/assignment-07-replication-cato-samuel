import mido
from pynput.keyboard import Controller, Key

# 1. Detect and list all available MIDI input devices
input_names = mido.get_input_names()
keyboard = Controller()
NOTE_MAPPING = {
    # Octave 1
    48: "t",  # C
    49: "h",  # C#
    50: "x",  # D
    51: "g",  # D#
    52: "j",  # E
    53: "e",  # F
    54: "z",  # F#
    55: "p",  # G
    56: "k",  # G#
    57: "f",  # A
    58: "y",  # A#
    59: "m",  # B
    # Octave 2
    60: "d",  # C (Middle C)
    61: "w",  # C#
    62: "a",  # D
    63: "u",  # D#
    64: "o",  # E
    65: "r",  # F
    66: "n",  # F#
    67: "e",  # G
    68: "c",  # G#
    69: "t",  # A
    70: "l",  # A#
    71: "i",  # B
    # Octave 3
    72: "s",  # C
    73: "g",  # C#
    74: "h",  # D
    75: "v",  # D#
    76: "b",  # E
    77: "d",  # F
    78: "q",  # F#
    79: "a",  # G
    80: "m",  # G#
    81: "e",  # A
    82: "u",  # A#
    83: "o",  # B
    # Octave 4
    84: "r",  # C
    85: "f",  # C#
    86: "n",  # D
    87: "w",  # D#
    88: "c",  # E
    89: "k",  # F
    90: "y",  # F#
    91: "p",  # G
    92: "h",  # G#
    93: "t",  # A
    94: "a",  # A#
    95: "i",  # B
    # Octave 5
    96: "s",  # C
    97: "o",  # C#
    98: "j",  # D
    99: "l",  # D#
    100: "z",  # E
    101: "e",  # F
    102: "f",  # F#
}


print("Detected MIDI Input Devices:")
for index, name in enumerate(input_names):
    print(f"[{index}] {name}")

if not input_names:
    print("\nNo MIDI devices detected. Please plugin a device and try again.")
    exit()

# 2. Automatically select and open the first connected device
target_device = input_names[0]
print(f"\nOpening and listening to: {target_device}")

try:
    with mido.open_input(target_device) as inport:
        print("Listening for MIDI messages... \n")
        # 3. Continuously read incoming real-time MIDI data
        for message in inport:
            if hasattr(message, "note") and message.note in NOTE_MAPPING:
                target_key = NOTE_MAPPING[message.note]
                if message.type == "note_on" and message.velocity > 0:
                    keyboard.press(target_key)
                    print(f"Note On : {message.note} | Velocity: {message.velocity}")
                if message.type == "note_on" and message.velocity == 0:
                    print(f"Note Off: {message.note} | Velocity: {message.velocity}")


except KeyboardInterrupt:
    print("\nStopped listening to MIDI data.")
