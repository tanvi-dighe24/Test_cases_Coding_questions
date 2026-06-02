Given an integer array arr of length n, compute how many strictly increasing subsequences of length 3 can be formed, and return the result modulo ($10^9 + 7$).Note:A subsequence is obtained by deleting zero or more elements from the array without changing the order of the remaining elements.A subsequence of length 3 is strictly increasing if it consists of indices $i < j < k$ such that:$arr[i] < arr[j] < arr[k]$.



def countIncreasingTriplets(arr):
    n = len(arr)
    MOD = 10**9 + 7
    
    # left_smaller[i] will store how many elements to the left of i are smaller than arr[i]
    left_smaller = [0] * n
    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:
                left_smaller[i] += 1
                
    # right_greater[i] will store how many elements to the right of i are greater than arr[i]
    right_greater = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] > arr[i]:
                right_greater[i] += 1
                
    # Count total triplets by treating each element as the middle element
    total_triplets = 0
    for i in range(n):
        total_triplets = (total_triplets + left_smaller[i] * right_greater[i]) % MOD
        
    return total_triplets
