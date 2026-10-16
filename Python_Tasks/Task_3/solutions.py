# Q1. Word Frequency

def word_frequency(sentence):
    words = sentence.split()
    d = {}

    for word in words:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1

    return d

# Q2. Character Frequency

def char_frequency(word):
    d = {}

    for ch in word:
        if ch in d:
            d[ch] += 1
        else:
            d[ch] = 1

    return d

# Q3. First Non-Repeating Character

def first_non_repeating(word):
    for ch in word:
        if word.count(ch) == 1:
            return ch

    return None

# Q4. Anagram Check

def is_anagram(s1, s2):
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False
  # Q5. First Repeating Character

def first_repeating(s):
    seen = []

    for ch in s:
        if ch in seen:
            return ch
        seen.append(ch)

    return None  

# Q6. Move Zeros to End

def move_zeros(nums):
    result = []
    count = 0

    for num in nums:
        if num == 0:
            count += 1
        else:
            result.append(num)

    for i in range(count):
        result.append(0)

    return result

# Q7. Second Highest Number

def second_highest(nums):
    unique = list(set(nums))

    if len(unique) < 2:
        return None

    unique.sort()

    return unique[-2]

# Q8. Remove Duplicates

def remove_duplicates(nums):
    result = []

    for num in nums:
        if num not in result:
            result.append(num)

    return result

# Q9. Missing Number

def missing_number(nums, n):
    total = n * (n + 1) // 2

    actual = sum(nums)

    return total - actual

# Q10. Two Sum

def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] + nums[i] == target:
                return [nums[j], nums[i]]

    return []

# Q11. Closest to Zero

def closest_to_zero(nums):
    closest = nums[0]

    for num in nums:
        if abs(num) < abs(closest):
            closest = num
        elif abs(num) == abs(closest) and num > closest:
            closest = num

    return closest


# Q12. Common Elements

def common_elements(list1, list2):
    result = []

    for num in list1:
        if num in list2 and num not in result:
            result.append(num)

    return result

# Q13. Rotate List

def rotate_list(nums, k):
    if len(nums) == 0:
        return []

    k = k % len(nums)

    return nums[-k:] + nums[:-k]

# Q14. Maximum Consecutive Sum

def max_consecutive_sum(nums):
    maximum = nums[0] + nums[1]

    for i in range(len(nums) - 1):
        total = nums[i] + nums[i + 1]

        if total > maximum:
            maximum = total

    return maximum

# Q15. All Unique Pairs

def all_pairs(nums, target):
    result = []

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                pair = sorted([nums[i], nums[j]])

                if pair not in result:
                    result.append(pair)

    result.sort()

    return result