import mido
from pynput.keyboard import Controller, Key

#velocity threshold above which the letters are uppercase
THRESHOLD = 63

#detect and list all available MIDI input devices
input_names = mido.get_input_names()
keyboard = Controller()

#note mappings for single keys
NOTE_MAPPING_LOWERCASE = {
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
NOTE_MAPPING_UPPERCASE = {
    # Octave 1
    48: "T",  # C
    49: "H",  # C#
    50: "X",  # D
    51: "G",  # D#
    52: "J",  # E
    53: "E",  # F
    54: "Z",  # F#
    55: "P",  # G
    56: "K",  # G#
    57: "F",  # A
    58: "Y",  # A#
    59: "M",  # B
    # Octave 2
    60: "D",  # C (Middle C)
    61: "W",  # C#
    62: "A",  # D
    63: "U",  # D#
    64: "O",  # E
    65: "R",  # F
    66: "N",  # F#
    67: "E",  # G
    68: "C",  # G#
    69: "T",  # A
    70: "L",  # A#
    71: "I",  # B
    # Octave 3
    72: "S",  # C
    73: "G",  # C#
    74: "H",  # D
    75: "V",  # D#
    76: "B",  # E
    77: "D",  # F
    78: "Q",  # F#
    79: "A",  # G
    80: "M",  # G#
    81: "E",  # A
    82: "U",  # A#
    83: "O",  # B
    # Octave 4
    84: "R",  # C
    85: "F",  # C#
    86: "N",  # D
    87: "W",  # D#
    88: "C",  # E
    89: "K",  # F
    90: "Y",  # F#
    91: "P",  # G
    92: "H",  # G#
    93: "T",  # A
    94: "A",  # A#
    95: "I",  # B
    # Octave 5
    96: "S",  # C
    97: "O",  # C#
    98: "J",  # D
    99: "L",  # D#
    100: "Z",  # E
    101: "E",  # F
    102: "F",  # F#
}


print("Detected MIDI Input Devices:")
for index, name in enumerate(input_names):
    print(f"[{index}] {name}")

if not input_names:
    print("\nNo MIDI devices detected. Please plugin a device and try again.")
    exit()

#let user select input device from printed list (number input required)
input_device_num = int(input("\nSelect input device: "))
target_device = input_names[input_device_num]
print(f"\nOpening and listening to: {target_device}")

try:
    with mido.open_input(target_device) as inport:
        print("Listening for MIDI messages... \n")
        #continuously read incoming real-time MIDI data
        for message in inport:
            if hasattr(message, "note") and message.note in range(48, 103):
                if message.type == "note_on" and message.velocity > 0:
                    #translate note and velocity into keystroke
                    if message.velocity > THRESHOLD:
                        target_key = NOTE_MAPPING_UPPERCASE[message.note]
                    else:
                        target_key = NOTE_MAPPING_LOWERCASE[message.note]
                    keyboard.press(target_key)
                    print(f"Note On : {message.note} | Velocity: {message.velocity}")
                if message.type == "note_on" and message.velocity == 0:
                    print(f"Note Off: {message.note} | Velocity: {message.velocity}")


except KeyboardInterrupt:
    print("\nStopped listening to MIDI data.")
