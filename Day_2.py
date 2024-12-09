if __name__ == '__main__':

    def safety_check(report):
        safe = True
        if report[1] > report[0]:
            type = 'asc'
        else:
            type = 'desc'
        for i in range(1,len(report)):
            if type == 'asc':
                if report[i] < report[i-1]:
                    safe = False
            else:
                if report[i] > report[i-1]:
                    safe = False
            diff = abs(report[i] - report[i-1])
            if  diff > 3 or diff == 0:
                safe = False
        return(safe)

    # Import txt file
    file = open('input_day2_part1.txt', 'r')
    # Save all lines into a list
    reports = []
    for line in file:
        data = line.strip().split()
        reports.append([int(num) for num in data])

    # Part 1
    safe_reports = 0 
    for report in reports:
        safe_return = safety_check(report)
        if safe_return:
            safe_reports += 1

    # Part 2
    safe_reports_damp = 0
    for report in reports:
        safe_return = safety_check(report)
        if not safe_return:
            for i in range(len(report)):
                report_damp = report[:]
                del report_damp[i]
                safe_return = safety_check(report_damp)
                if safe_return:
                    break
        if safe_return:
            safe_reports_damp += 1
        print(report, safe_return)
    
    print(safe_reports_damp)

# Part 2
