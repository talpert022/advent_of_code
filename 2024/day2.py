with open('input.txt') as txt:
    reports = txt.read().splitlines()

'''
PART 1

trend -> 0 (unset), 1 (ascending), -1 (descending)
'''
def is_safe_level(levels):
    last_level = None
    trend = 0
    for curr_level in levels:
        if last_level and not trend: # Entered on second level
            trend = 1 if (curr_level - last_level) > 0 else -1
        elif not trend: # Entered on first level
            last_level = curr_level
            continue

        # Make sure levels are ascending or descending
        if (trend > 0 and curr_level <= last_level) or (trend < 0 and curr_level >= last_level):
            return 0
        elif abs(curr_level - last_level) > 3:
            return 0

        last_level = curr_level

    return 1


safe_levels = 0

for report in reports:
    report = [int(level) for level in report.split()]
    safe_levels += is_safe_level(report)

print(f"PT1 RES: {safe_levels}")

'''
PART 2
Hella brute force but fuck it 🤷
'''

fault_tolerant_safe_levels = 0
for report in reports:
    report = [int(level) for level in report.split()]
    fault_tolerant_safe_levels += is_safe_level(report)
    if not is_safe_level(report):
        for idx in range(len(report)):
            new_report = report[:idx] + report[idx+1:]
            if is_safe_level(new_report):
                fault_tolerant_safe_levels += 1
                break

print(f"PT2 RES: {fault_tolerant_safe_levels}")