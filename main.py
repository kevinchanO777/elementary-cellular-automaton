def generate_rule_pattern(rule):
    # Convert rule number to binary and reverse the order
    rule_binary = format(rule,"08b")[::-1]
    pattern = {key: rule_binary[key] for key in range(8)}
    for key in pattern:
        pattern[key] = '.' if pattern[key] == '0' else 'x'
    return pattern

def int_represent(pattern):
    pattern = ''.join(['0' if item == '.' else '1' for item in pattern])
    pattern = int(pattern,2)
    return pattern

def generate_elementary_ca(rule, num_steps):

    rule_pattern = generate_rule_pattern(rule)
 
    # Initial state with a single 'x' in the middle
    state = ['.'] * (2 * num_steps + 1)
    state[num_steps] = 'x'

    # Print the initial state
    print(''.join(state))

    # Generate the subsequent states
    for i in range(num_steps):
        new_state = ['.'] * (2 * num_steps + 1)

        new_state[0] = rule_pattern[int_represent([state[-1],state[0],state[1]])]
        for i in range(1,len(state)-1):
           new_state[i] = rule_pattern[int_represent(state[i-1:i+2])]
        new_state[-1] = rule_pattern[int_represent([state[-2],state[-1],state[0]])]

        state = new_state
        print(''.join(state))

# Example usage
# Rule 18: give a fractal like pattern
# Rule 30: interesting triangles too ...
# Adjust your terminal size to fit the grid

steps = 200

for i in range(256):
    print(f"Rule {i}: ")
    generate_elementary_ca(i, steps)
    print("\n")