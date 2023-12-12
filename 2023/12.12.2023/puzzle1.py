import re

with open("input.txt", "r") as f:
    lines = f.read().splitlines()
lines = [line.split() for line in lines]
lines = [(line[0].replace(".","o").replace("#","d").replace("?","."), [int(x) for x in line[1].split(",")]) for line in lines]


def find_streak_strings(n, streaks, current_config=[], start=0, results=[]):
    if not streaks:
        trial_sequence = ["o"] * n
        for streak in current_config:
            for pos in range(streak[0], streak[1] + 1):
                trial_sequence[pos] = "d"
        results.append("".join(trial_sequence))
        return

    current_streak = streaks[0]
    remaining_streaks = streaks[1:]

    for i in range(start, n - current_streak + 1):
        current_config.append((i, i + current_streak - 1))
        find_streak_strings(n, remaining_streaks, current_config, i + current_streak + 1, results)
        current_config.pop()

    return results

def compare(line):
    n = len(line[0])
    streaks = line[1]
    configurations = find_streak_strings(n, streaks, current_config=[], start=0, results=[])
    return sum([bool(re.search(line[0],x)) for x in configurations])

print(sum([compare(line) for line in lines]))