class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		if len(s) < 2:
			return len(s)

		k, max_len, count = 0, 0, 0

		for i in range(1, len(s)):
			for j in range(k, i):
				if s[i] == s[j]:
					k = j + 1

			count = i - k + 1

			if count > max_len:
				max_len = count

		return max_len