def first_uncommon(matrix, n):
    # Your implementation here!
    # pass

    #  if nothing in matrix matrix count < n? at least one element 
    # legnth o matrix will be one
    # create dcitonary to maps the each to frequenct 
    # loop each row
        # each element
            # if value < n
                # return element

    letter_counts = {}
    for row in matrix:
        for letter in row:
            if letter not in letter_counts:
                letter_counts[letter] = 1
            elif letter in letter_counts:
                letter_counts[letter] += 1

    for row in matrix:
        for letter in row:
            if letter_counts[letter] < n:
                return letter

matrix_1 = (
    ('u','e','r','e', ' ', 'e'),
    ('d', 'z', 'o', 'b', 'i', 'v'),
    ('n',),
    ('w', 'g', 'q', ' ', '5', 'g', 'w'),
    ('r',),
    ('y', 'e'),
    ('u', 'a', 'u', 't')
)
assert first_uncommon(matrix_1, 2) == 'd'
assert first_uncommon(matrix_1, 3) == 'r'
assert first_uncommon(matrix_1, 4) == 'u'

matrix_2 = (
    ('💜',),
)
assert first_uncommon(matrix_2, 2) == '💜'
assert first_uncommon(matrix_2, 525600) == '💜'

print("All tests passed! Discuss time and space complexity if time remains!")