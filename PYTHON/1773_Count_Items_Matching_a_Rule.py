# 06/09/2026
# Easy
# LeetCode 1773: Count Items Matching a Rule using dictionary mapping.

class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        rule_dict = {"type": 0, "color": 1, "name": 2}
        key_index = rule_dict[ruleKey]
        count = 0
        
        for item in items:
            if item[key_index] == ruleValue:
                count += 1
                
        return count