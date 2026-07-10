import mido

# 1. Detect and list all available MIDI input devices
input_names = mido.get_input_names()
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
            # Accessing individual attributes safely
            if message.type == "note_on" and message.velocity > 0:
                print(f"Note On : {message.note} | Velocity: {message.velocity}")
            if message.type == "note_on" and message.velocity == 0:
                print(f"Note Off: {message.note} | Velocity: {message.velocity}")

except KeyboardInterrupt:
    print("\nStopped listening to MIDI data.")
