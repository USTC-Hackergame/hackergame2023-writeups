orig_data = [53, 41, 85, 109, 75, 1, 33, 48, 77, 90,
             17, 118, 36, 25, 13, 89, 90, 3, 63, 25,
             31, 77, 27, 60, 3, 118, 24, 62, 54, 61,
             25, 63, 77, 36, 5, 32, 60, 67, 113, 28]

tuple_data = [divmod(i, 24) for i in orig_data]

code_dict = [
#    012345678901234567890123
    'nymeh1niwemflcir}echaet',
#    ~~~~~~~~~~~~~~~~~^
    'a3g7}kidgojernoetlsup?h',
# }l ~~~~^~~~~~~~~~~~~^
    'ulw! f5soadrhwnrsnstnoeq',
#         ^~~~~~~~~~~~~~~~~~~ f
    ' ct{l-findiehaai{oveatas',
#       ^~~~~~~~~~~~~~~~~~~~~ {
    ' ty9kxborszstguyd?!blm-p',
#                 ^~~~~~~~~~~ g
#    012345678901234567890123
]

code_ranges = [
    range(18),
    range(18),
    # range(5, 25),
    {0, *range(5, 25)},
    range(3, 25),
    range(13, 25),
]

def known_chars_iter():
    for line, column in tuple_data:
        if column in code_ranges[line]:
            yield code_dict[line][column]
        else:
            yield (line, column)

known_chars = list(known_chars_iter())
print(known_chars)
print("".join(known_chars))
