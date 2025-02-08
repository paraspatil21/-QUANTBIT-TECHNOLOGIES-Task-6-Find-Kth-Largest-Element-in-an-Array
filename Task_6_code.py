def find_kth_largest(nums: list, k: int) -> int:
    nums.sort(reverse=True)
    return nums[k - 1]


nums = list(map(int, input("Enter the numbers in the array separated by spaces: ").split()))
k = int(input("Enter the value of k: "))
print("The k-th largest element is:", find_kth_largest(nums, k))
