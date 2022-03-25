def even(nums):
    even_list = []
    for num in nums:
        if num % 2 == 0:
            even_list.append(num)
    return even_list
