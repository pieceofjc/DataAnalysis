def custom_min(args):
    result = 100001
    idx = 0
    while idx < len(args):
        if result > args[idx]:
            result = args[idx]
        idx += 1
    return result

def custom_max(args):
    result = -100001
    idx = 0
    while idx < len(args):
        if result < args[idx]:
            result = args[idx]
        idx += 1
    return result

def custom_sort(args, desc = False):
    length = len(args)
    for idx in range(length):
        remove_data = custom_min(args[:length-idx]) if not desc else custom_max(args[:length-idx])
        args.remove(remove_data)
        args.append(remove_data)
    return args

a = 1
b = 1
