

class SmartACController:

    def __init__(self):
        # Store previous AC mode
        self.previous_mode = "OFF"

    def control_ac(self, temperature, occupied):

        # Occupancy has highest priority
        if not occupied:
            target_mode = "OFF"

        elif temperature < 18:
            target_mode = "HEAT"

        elif temperature > 26:
            target_mode = "COOL"

        else:
            target_mode = "OFF"

        
        command_required = (target_mode != self.previous_mode)

        self.previous_mode = target_mode

        return target_mode, command_required



ac = SmartACController()


tests = [
    (17, True),   # Case 1: HEAT
    (17, True),   # Case 2: Repeated percept
    (18, True),   # Case 3: Lower boundary
    (26, True),   # Case 4: Upper boundary
    (27, True),   # Case 5: COOL transition
    (25, False)   # Case 6: Empty room
]


for temperature, occupied in tests:

    previous = ac.previous_mode

    target, send_command = ac.control_ac(
        temperature, occupied
    )

    print("\n------------------------")
    print("Previous Mode:", previous)
    print("Temperature:", temperature)
    print("Occupied:", occupied)
    print("Target Mode:", target)

    if send_command:
        print("Result: SEND COMMAND")
    else:
        print("Result: NO COMMAND")
