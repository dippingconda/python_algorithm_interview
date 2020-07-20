"""
https://leetcode.com/problems/most-common-word
"""
from typing import List
import re

def mostCommonWord(para:str, ban:List[str]) -> str:
    words = [word for word in re.sub(r'[^\w]', ' ', para).lower().split() if word not in ban]
    word_dict = {}
    for word in words:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1

    return max(word_dict, key=word_dict.get)




if __name__ == "__main__":
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    print(f'"{mostCommonWord(paragraph, banned)}"')