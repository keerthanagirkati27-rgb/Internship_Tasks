
from solutions import (
    word_frequency,
    char_frequency,
    first_non_repeating,
    is_anagram,
    first_repeating,
    move_zeros,
    second_highest,
    remove_duplicates,
    missing_number,
    two_sum,
    closest_to_zero,
    common_elements,
    rotate_list,
    max_consecutive_sum,
    all_pairs
)

# Q1. Word Frequency
print(word_frequency("python is easy and python is powerful"))
print(word_frequency("hello hello world"))

# Q2. Character Frequency
print(char_frequency("banana"))
print(char_frequency("apple"))

# Q3. First Non-Repeating Character
print(first_non_repeating("swiss"))
print(first_non_repeating("aabbc"))

# Q4. Anagram Check
print(is_anagram("listen", "silent"))
print(is_anagram("hello", "world"))

# Q5. First Repeating Character
print(first_repeating("programming"))
print(first_repeating("abcda"))

# Q6. Move Zeros to End
print(move_zeros([0, 3, 0, 1, 2, 0, 4]))
print(move_zeros([1, 0, 2, 0, 3]))

# Q7. Second Highest Distinct Number
print(second_highest([10, 20, 40, 30, 40, 20]))
print(second_highest([5, 5, 3, 1]))

# Q8. Remove Duplicates
print(remove_duplicates([4, 2, 4, 5, 2, 7, 5]))
print(remove_duplicates([1, 1, 2, 3, 2]))

# Q9. Missing Number
print(missing_number([1, 2, 4, 5, 6], 6))
print(missing_number([1, 2, 3, 5], 5))

# Q10. Two Sum
print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))

# Q11. Closest to Zero
print(closest_to_zero([-8, -3, 2, 5, -2]))
print(closest_to_zero([-4, -1, 3, 6]))

# Q12. Common Elements
print(common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
print(common_elements([2, 3, 2, 4], [2, 4, 6]))

# Q13. Rotate List
print(rotate_list([1, 2, 3, 4, 5], 2))
print(rotate_list([10, 20, 30, 40], 1))

# Q14. Maximum Consecutive Sum
print(max_consecutive_sum([4, 7, 2, 9, 5]))
print(max_consecutive_sum([1, 5, 3, 8]))

# Q15. All Pairs
print(all_pairs([2, 4, 3, 5, 7, 8, 1], 9))
print(all_pairs([1, 2, 3, 4, 5], 6))
