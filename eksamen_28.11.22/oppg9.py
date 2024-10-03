def print_errors_and_warnings(a):
    result = ''
    for line in a:
        if "Error" in line:
            result += line + '\n'
        if "Warning" in line:
            result += line + '\n'
    return result

print(print_errors_and_warnings([
  "Info: had a good nights sleep before exam",
  "Warning: not enough snacks brought for exam",
  "Info: went for a walk before exam started",
  "Error: went to wrong exam location",
  "Debug: laptop_charge=92%, charing_cable_present=True",
  "Warning: time management is important",
]))
