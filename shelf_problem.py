def solution(clients):
    shelf = set()
    max_packages_on_shelf = 0

    first = 0
    second = 1

    for i in range(0, len(clients) + 1 ):
        for j in range(i, len(clients)):
            if clients[i] < clients[j]:
                shelf.add(clients[j])
            else:
                clients.remove(clients[i])

    print(shelf)
    return max_packages_on_shelf


print(solution([4, 1, 2, 1]))  # Output: 3
print(solution([3, 2, 4, 5, 11]))  # Output: 2
print(solution([11, 2, 3, 4, 5]))  # Output: 0
print(solution([3, 2, 7, 5, 4, 1, 6]))  # Output: 4
print(solution([1, 0, 0, 5]))  # Output: 1