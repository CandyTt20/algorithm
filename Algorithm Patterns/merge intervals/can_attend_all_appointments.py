def can_attend_all_appointments(intervals):
    # TODO: Write your code here
    intervals.sort(key=lambda x: x[0])
    if len(intervals) <= 1:
        return True
    else:
        i, j = 0, 1
        while j < len(intervals):
            if intervals[j][0] < intervals[i][1]:
                return False
            else:
                i, j = i + 1, j + 1
                
    return True


def main():
    print("Can attend all appointments: " + str(can_attend_all_appointments([[1, 4], [2, 5], [7, 9]])))
    print("Can attend all appointments: " + str(can_attend_all_appointments([[6, 7], [2, 4], [8, 12]])))
    print("Can attend all appointments: " + str(can_attend_all_appointments([[4, 5], [2, 3], [3, 6]])))


main()