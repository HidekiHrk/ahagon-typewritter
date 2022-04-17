def generate_loop_numbers(max_num: int):
    current = 0
    while True:
        yield current
        if current >= max_num - 1:
            current = 0
        else:
            current += 1
