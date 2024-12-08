f = open("./day-2.txt", "r")
x = f.read()

reports = x.split("\n")[:-1]


def is_report_safe(elements):
    diffs = []
    for i in range(len(elements) - 1):
        current = int(elements[i])
        next = int(elements[i + 1])

        difference = current - next
        diffs.append(difference)

        if abs(difference) > 3 or difference == 0:
            return False

    diffs.sort()

    if diffs[0] < 0 and diffs[-1] > 0:
        return False

    return True


parsed_reports = [[int(el) for el in report.split(" ")] for report in reports]

checked_reports = [is_report_safe(report) for report in parsed_reports]

print(sum(checked_reports))

# --- 2nd star solution

checked_reports_lax = [
    any([is_report_safe(report[:i] + report[i + 1 :]) for i in range(len(report))])
    for report in parsed_reports
]

print(sum(checked_reports_lax))
