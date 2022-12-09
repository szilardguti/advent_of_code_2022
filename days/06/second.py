def is_marker(four_digit_string):
    for wanted_chr in four_digit_string:
        count = 0
        for got_chr in four_digit_string:
            if wanted_chr == got_chr:
                count = count + 1
        if count > 1:
            return False
    return True

with open("input.txt", "r") as f:
    data_stream = f.read()
    
    buffer_size = 14
    max_index = len(data_stream)-buffer_size+1

    for i in range(max_index):
        current_window = data_stream[i:i+buffer_size]

        if(is_marker(current_window)):
            print(i+buffer_size)
            break