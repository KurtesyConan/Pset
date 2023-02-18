## How many times shall I concatinte ##

def concate_n_times(string_concat, num_concat):
    concatenated_string = string_concat * int(num_concat)
    return concatenated_string
    
string_1 = "abcd"
concat_n = input("How many times do you want to concatinate: ")
#new_string_1 = string_1 * int(concat_n)
new_string_1 = concate_n_times(string_1, concat_n)
print(new_string_1)

