"""
002 - Encyclopedia of Parentheses（★3）
https://atcoder.jp/contests/typical90/tasks/typical90_b
"""

import sys
N = int(input())

if N % 2 == 1:
    print("")
    sys.exit()

str_set = set()
str_set.add("")
for i in range(1, N//2 + 1):
    str_set_new = set()

    for current_string in str_set:
        for j in range(i*2+1):
            tmp_str = current_string[:j] + "()" + current_string[j:]
            if tmp_str not in str_set_new:
                str_set_new.add(tmp_str)
    str_set = str_set_new

for s in sorted(str_set):
    print(s)
