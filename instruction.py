import filters as filter
import operations as operation
import create_selection as cs

selection = [True, True, False, True, True, False, False, False, False, False, True, False, False, False, False, False, False]

received = cs.Select_data([], selection, info = True)
received = received + cs.M_select_data("E:/20111231_20/", 0, 60, selection)
received = received + cs.M_select_data("E:/20111231_21/", 0, 60, selection)
received = received + cs.M_select_data("E:/20111231_22/", 0, 60, selection)
received = received + cs.M_select_data("E:/20111231_23/", 0, 60, selection)

filtered = filter.country(received, "US")
filtered = filter.friends(filtered, min_nof=100)

filtered = operation.Merge(filtered, "Hashtag")
filtered = operation.RemoveUnimportant(filtered, 3, 1)
filtered = operation.SortDec(filtered, 1)

for item in filtered:
    print(item)
