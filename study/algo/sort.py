from typing import Callable, List


def quick_sort(nums: List[int]):

    def get_pivot(nums, start, end):
        return nums[start], start

    def hoare_partition(nums, start, end):
        i = start - 1
        j = end
        pivot, k = get_pivot(nums, start, end)
        nums[start], nums[k] = nums[k], nums[start]
        while i < j:
            i += 1
            while nums[i] < pivot:
                i += 1
            j -= 1
            while nums[j] > pivot:
                j -= 1
            if i >= j:
                return j
            nums[i], nums[j] = nums[j], nums[i]

    def qs(nums, start, end):
        if end - start <= 1:
            return
        p = hoare_partition(nums, start, end)
        qs(nums, start, p + 1)
        qs(nums, p + 1, end)
    qs(nums, 0, len(nums))
    return nums


def test_sort(sort_func: Callable[[List[int]], List[int]]):
    # 测试空列表
    assert sort_func([]) == []

    # 测试单元素列表
    assert sort_func([1]) == [1]

    # 测试已排序列表
    assert sort_func([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    # 测试逆序列表
    assert sort_func([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    # 测试随机顺序列表
    assert sort_func([3, 1, 4, 2, 5]) == [1, 2, 3, 4, 5]

    # 测试包含重复元素的列表
    assert sort_func([3, 2, 2, 1, 3]) == [1, 2, 2, 3, 3]

    # 测试所有元素相同的列表
    assert sort_func([2, 2, 2, 2]) == [2, 2, 2, 2]

    # 测试负数元素
    assert sort_func([-1, -3, 0, 2, -2]) == [-3, -2, -1, 0, 2]

    # 测试大数和小数混合
    assert sort_func([100, 1, 0.1, 10, 0.01]) == [0.01, 0.1, 1, 10, 100]