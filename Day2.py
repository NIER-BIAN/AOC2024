#=========================================================
# Pt1

allReports = []
with open('input.txt', 'r') as file:
    for report in file:
        strReport = report.split()
        intReport = [int(i) for i in strReport]
        allReports.append(intReport)

def isSorted(data):
    sorted_data_asc = sorted(data)
    sorted_data_desc = sorted(data, reverse=True)
    return data == sorted_data_asc or data == sorted_data_desc

sortedReports = [report for report in allReports if isSorted(report)]

def isSteadilyChanging(data):
    # return true if condition abs(data[i]-data[i+1]) <= 3 is True for all elements
    return all(
        (0 < abs(data[i]-data[i+1]) <= 3)
        for i in range(len(data)-1)
    )

safeReports = [report for report in sortedReports if isSteadilyChanging(report)]

print(len(safeReports))

#=======================================================================================
# Pt2

allReports = []
with open('input.txt', 'r') as file:
    for report in file:
        strReport = report.split()
        intReport = [int(i) for i in strReport]
        allReports.append(intReport)

def isSorted(data):
    sorted_data_asc = sorted(data)
    sorted_data_desc = sorted(data, reverse=True)
    return data == sorted_data_asc or data == sorted_data_desc

def isSteadilyChanging(data):
    # return true if condition abs(data[i]-data[i+1]) <= 3 is True for all elements
    return all(
        (0 < abs(data[i]-data[i+1]) <= 3)
        for i in range(len(data)-1)
    )

safeReports = []
almostSafeReports = []

for report in allReports:
    
    if isSorted(report) and isSteadilyChanging(report):
        safeReports.append(report)
    
    else:
        for i in range(len(report)):
            temp_report = report[:i] + report[i+1:]
            if isSorted(temp_report) and isSteadilyChanging(temp_report):
                almostSafeReports.append(report)
                break #No need to check further removals for this report

print(len(safeReports))
print(len(almostSafeReports))
