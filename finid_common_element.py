"""
https://somjang.tistory.com/entry/%EC%8B%A4%EC%A0%9C-%EB%A9%B4%EC%A0%91-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8-%EB%AC%B8%EC%A0%9C-Python
"""
a = [1, 3, 5, 7, 9, 13, 15]
b = [4, 5, 6, 8, 13]
c = [5, 8, 13, 19]

"""
using 3ea pointers
"""
a_ptr = 0
b_ptr = 0
c_ptr = 0
result = []
len_a, len_b, len_c = len(a), len(b), len(c)
while c_ptr < len_c:
    if a_ptr == len_a - 1 and b_ptr == len_b - 1 and c_ptr == len_c - 1:
        break

    if a[a_ptr] < c[c_ptr] and a_ptr < len_a - 1:
        a_ptr += 1
    if b[b_ptr] < c[c_ptr] and b_ptr < len_b - 1:
        b_ptr += 1

    if a[a_ptr] > c[c_ptr] or b[b_ptr] > c[c_ptr]:
        c_ptr += 1

    if a[a_ptr] == b[b_ptr] and b[b_ptr] == c[c_ptr]:
        result.append(a[a_ptr])
        c_ptr += 1

print(result)
"""
simple way
"""
print(set(a) & (set(b) & set(c)))
