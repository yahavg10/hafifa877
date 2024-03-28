sum_list = lambda lst: 0 if not lst else lst[0] + sum_list(lst[1:])


print(sum_list([1, 2, 3, 4, 5]))

#done
