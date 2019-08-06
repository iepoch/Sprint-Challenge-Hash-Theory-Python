# 1.
for a in range(2):
    for b in range(2):
        # for c in range(2):
        result = not(a or not b)
        print(f'A: {a} B: {b} , Result:{result}')


# # 2.
# for a in range(2):
#     for b in range(2):
#         # for c in range(2):
#         result = (not a) or b and not(a and (not b))
#         print(f'A: {a} B: {b} , Result:{result}')


# # 3.
# for a in range(2):
#     for b in range(2):
#         for c in range(2):
#             result = (not (a or b) or (a or c) and not(b or not c))
#             print(f'A: {a} B: {b} C: {c}, Result: {result}')
