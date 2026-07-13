import mido
from pynput.keyboard import Controller, Key

# velocity threshold above which the letters are uppercase
THRESHOLD = 63

# detect and list all available MIDI input devices
input_names = mido.get_input_names()
keyboard = Controller()

# note mappings for single keys
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


pressed_keys = []


# get the key of the pitch
def get_key(pitch):
    return pitch % 12 + 1


# translate note and velocity into keystroke
def get_letter(key, velocity):
    if velocity > THRESHOLD:
        return NOTE_MAPPING_UPPERCASE[key]
    else:
        return NOTE_MAPPING_LOWERCASE[key]


def capitalize_n_gram(n_gram, chord):
    if any(c["letter"].isupper() for c in chord):
        return n_gram.capitalize()
    return n_gram


# return n_gram if it is a valid 2-key chord
def get_double_n_gram(chord):
    keys = (chord[0]["key"], chord[1]["key"])

    n_grams = {
        (8, 12): "the",
        (5, 8): "that",
        (8, 11): "th",
        (7, 10): "and",
        (4, 8): "to",
        (12, 3): "in",
        (6, 10): "ment",
        (11, 3): "with",
        (1, 4): "ing",
        (1, 5): "this",
        (10, 1): "which",
        (1, 8): "there",
        (3, 6): "up",
        (6, 1): "where",
        (2, 5): "pl",
        (3, 8): "him",
        (5, 12): "have",
        (3, 10): "able",
        (8, 3): "for",
        (7, 3): "use",
        (3, 12): "over",
        (8, 1): "inter",
        (5, 10): "but",
        (6, 3): "not",
        (12, 8): "ent",
        (4, 1): "would",
        (1, 1): "what",
        (3, 3): "by",
        (6, 6): "will",
        (10, 10): "other",
        (12, 12): "ter",
        (8, 5): "nes",
        (1, 9): "one",
        (1, 10): "between",
        (8, 4): "ate",
        (5, 1): "because",
        (5, 9): "yes",
        (3, 11): "ly",
        (5, 2): "could",
        (4, 12): "of",
        (7, 12): "about",
        (12, 5): "ted",
        (7, 11): "like",
        (11, 6): "her",
        (12, 7): "just",
        (10, 3): "many",
    }

    n_gram = n_grams.get(keys, "")
    return capitalize_n_gram(n_gram, chord)


# return n_gram if it is a valid 3-key chord
def get_tripple_n_gram(chord):
    if len(chord) != 3:
        return ""

    keys = (
        chord[0]["key"],
        chord[1]["key"],
        chord[2]["key"],
    )

    n_grams = {
        (12, 5, 9): "from",
        (11, 3, 8): "ver",
        (8, 12, 3): "these",
        (6, 11, 3): "tion",
        (8, 1, 5): "make",
        (5, 8, 12): "con",
        (1, 5, 8): "take",
        (12, 5, 8): "ght",
        (1, 5, 10): "how",
        (5, 10, 1): "when",
        (5, 8, 1): "good",
    }

    n_gram = n_grams.get(keys, "")
    return capitalize_n_gram(n_gram, chord)


print("Detected MIDI Input Devices:")
for index, name in enumerate(input_names):
    print(f"[{index}] {name}")

if not input_names:
    print("\nNo MIDI devices detected. Please plugin a device and try again.")
    exit()

# let user select input device from printed list (number input required)
input_device_num = int(input("\nSelect input device: "))
target_device = input_names[input_device_num]
print(f"\nOpening and listening to: {target_device}")

try:
    with mido.open_input(target_device) as inport:
        print("Listening for MIDI messages... \n")
        # continuously read incoming real-time MIDI data
        for message in inport:
            if hasattr(message, "note") and message.note in range(48, 103):
                if message.type == "note_on" and message.velocity > 0:
                    pressed_keys.append(
                        {
                            "key": get_key(message.note),
                            "letter": get_letter(message.note, message.velocity),
                        }
                    )
                if message.type == "note_on" and message.velocity == 0:
                    letters = ""
                    while len(pressed_keys) > 0:
                        if len(pressed_keys) > 2:
                            n_gram = get_tripple_n_gram(pressed_keys[:3])
                            if n_gram != "":
                                letters += n_gram
                                pressed_keys = pressed_keys[3:]
                                continue
                        if len(pressed_keys) > 1:
                            n_gram = get_double_n_gram(pressed_keys[:2])
                            if n_gram != "":
                                letters += n_gram
                                pressed_keys = pressed_keys[2:]
                                continue
                        letters += pressed_keys[0]["letter"]
                        pressed_keys = pressed_keys[1:]
                    for letter in letters:
                        keyboard.press(letter)
                    # if len(letters) > 0:
                    #     print(letters)
                    pressed_keys = []


except KeyboardInterrupt:
    print("\nStopped listening to MIDI data.")
