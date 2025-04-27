romman_digits_dict = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}


class Solution(object):
    def romanToInt(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        number = 0
        new_s = s[::-1]
        pred_number = 0
        for n in range(len(new_s)):
            if pred_number <= romman_digits_dict[new_s[n]] :
                number += romman_digits_dict[new_s[n]]
            else:
                number -= romman_digits_dict[new_s[n]]
            pred_number = romman_digits_dict[new_s[n]]
        return number

# Bst solution
class SolutionBest(object):
    def romanToInt(self, s):
        roman_dist = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        prev_vel = 0

        for char in reversed(s):
            cur_vel = roman_dist[char]
            if cur_vel < prev_vel:
                result -= cur_vel
            else:
                result += cur_vel
            prev_vel = cur_vel

        return result
if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt('MCMXCIV'))