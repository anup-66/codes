# def maxTotalReward(self, rewardValues: List[int]) -> int:
dict_ = {}
# def find(reward,sum_,index):
#     if index>=len(reward):
#         return sum_
#     if (index,sum_) in dict_:
#         return dict_[(index,sum_)]
#     pick = 0
#     if sum_<reward[index]:
#         pick = find(reward,sum_+reward[index],index+1)
#     nopick = find(reward,sum_,index+1)
#     dict_[(index,sum_)] = max(pick,nopick)
#     return max(pick,nopick)
def find(reward):
    n = len(reward)

    # Dictionary to store maximum reward sums dynamically
    dp = {}

    # Initialize with base case
    dp[0] = 0

    # Process each reward
    for i in range(n):
        current_reward = reward[i]
        # Create a list of current states to avoid modifying the dictionary while iterating over it
        current_states = list(dp.items())
        for sum_, total_reward in current_states:
            if sum_ < current_reward:
                new_sum = sum_ + current_reward
                if new_sum not in dp or dp[new_sum] < total_reward + current_reward:
                    dp[new_sum] = total_reward + current_reward

    # Find the maximum reward
    max_reward = max(dp.values())

    return max_reward
print(find(sorted(list(map(int,input().split())))))