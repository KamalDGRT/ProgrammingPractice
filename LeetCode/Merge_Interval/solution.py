# intervals = [[1,6],[2,3],[8,10],[15,18]]

# start = 1
# end = 3

# next_start = 2
# next_end = 6

# if next_start less than or equal to end,
#     then,
#         new_end = max(end, next_end)
#         merged_list = [start, new_end]
#         e.g.
#         merged_list = [1, 6]


intervals = [[1,6],[2,7],[8,10],[9,18]]
result = []

intervalLength = len(intervals) - 1
for pair in range(intervalLength):

    current_start = intervals[pair][0]
    current_end = intervals[pair][1]
    print("index = ", pair)
    print("current_start = ", current_start)
    print("current_end = ", current_end)

    next_pair = intervals[pair + 1]
    next_start = next_pair[0]
    next_end = next_pair[1]
    print(next_pair, "\nNext_Start : ", next_start, "\nNext End: ", next_end, "\n")

    # [1,6] [1, 8]
    if current_start <= next_start and ((current_end >= next_start) or (current_end < next_end)):
        new_end = max(current_end, next_end)
        merged_list = [current_start, new_end]
        result.append(merged_list)
        intervals.remove([next_start, next_end])
        intervalLength -= 1
        print(intervals)
        print("Merged List: ", merged_list)

    else:
        merged_list = [current_start, current_end]
        result.append(merged_list)

result.append(intervals[-1])
print(result)
