import re
from collections import defaultdict

def parse_instructions(instructions):
    bot_states = defaultdict(list)
    bot_actions = defaultdict(list)

    for instruction in instructions:
        value_search = re.search("value (\d+) goes to bot (\d+)", instruction)
        if value_search:
            value = int(value_search.group(1))
            bot = int(value_search.group(2))
            bot_states[bot].append(value)

        action_search = re.search("bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)", instruction)
        if action_search:
            action_bot = int(action_search.group(1))
            low_type = action_search.group(2)
            low_index = int(action_search.group(3))
            high_type = action_search.group(4)
            high_index = int(action_search.group(5))
            bot_actions[action_bot].append(((low_type, low_index), (high_type, high_index)))
    
    return (bot_states, bot_actions)

def give_value(bot_states, outputs, value, dest):
    if dest[0] == 'bot':
        bot_states[dest[1]].append(value)
    elif dest[0] == 'output':
        outputs[dest[1]].append(value)

def do_bot_action(bot_states, bot_actions, outputs, bot):
    low = min(bot_states[bot])
    high = max(bot_states[bot])
    bot_states[bot] = []
    action = bot_actions[bot].pop(0)
    give_value(bot_states, outputs, low, action[0])
    give_value(bot_states, outputs, high, action[1])

def run_instructions(instructions, cmp_callback):
    bot_states, bot_actions = parse_instructions(instructions)
    outputs = defaultdict(list)
    while True:
        actionable_bots = [bot for bot, state in bot_states.iteritems() if len(state) == 2]
        bots_with_actions = [bot for bot, actions in bot_actions.iteritems() if (bot in actionable_bots and len(actions) > 0)]
        if bots_with_actions:
            bot = bots_with_actions[0]
            if cmp_callback:
                cmp_callback(bot, bot_states[bot])
            do_bot_action(bot_states, bot_actions, outputs, bot)
        else:
            break

    return outputs

run_instructions([
    "value 5 goes to bot 2",
    "bot 2 gives low to bot 1 and high to bot 0",
    "value 3 goes to bot 1",
    "bot 1 gives low to output 1 and high to bot 0",
    "bot 0 gives low to output 2 and high to output 0",
    "value 2 goes to bot 2",
], None)

with open('day10.input', 'rt') as f:
    raw_input = f.readlines()

def cmp(bot, bot_state):
    if (61 in bot_state) and (17 in bot_state):
        print bot

outputs = run_instructions(raw_input, cmp)
print outputs[0][0] * outputs[1][0] * outputs[2][0]


