# indexing = accessing elements of a sequence using [] (Indexing operations
#            [ start : end : step ]

credit = "1234-5678-9012-3456"

# print(credit[0])
# print(credit[:4])
# print(credit[5:9])
# print(credit[10:])
# print(credit[-4:])
# print(credit[::3])

print(credit[::-1])
last_dig = credit[-4:]
print(f"XXXX-XXXX-XXXX-{last_dig}")

