def sort(lst):
    lst = list(lst);
    swapped = True;
    while swapped:
        swapped = False;
        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i];
                swapped = True;
    return lst