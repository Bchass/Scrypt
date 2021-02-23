import pyscrypt

phrase = input("Enter a phrase: ").encode()

hash = pyscrypt.hash(
        password=phrase,
        salt=b"seasalt",
        N=1024,
        r=1,
        p=1,
        dkLen=12
    )

print(hash)

converted_list = list(hash)
for i in converted_list[:1]:
    print(converted_list)


def QuickSort(converted_list):
    if len(converted_list) <=1:
        return converted_list
    else:
        pivot = converted_list.pop()
        high = []
        low = []

    for value in converted_list:
        if value > pivot:
            high.append(value)
        else:
            low.append(value)
    return QuickSort(low) + [pivot] + QuickSort(high)
print(QuickSort(converted_list))
