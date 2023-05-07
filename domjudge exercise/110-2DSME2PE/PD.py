while True:
    try:
        n = int(input())
        tree = [[] for _ in range(n+1)]
        for i in range(1, n+1):
            l, r = map(int, input().split())
            tree[i].extend([l, r])
        depth = 0
        queue = [(1, 1)]
        while queue:
            node, level = queue.pop(0)
            if tree[node][0] == 0 and tree[node][1] == 0:
                depth = max(depth, level)
            if tree[node][0] != 0:
                queue.append((tree[node][0], level+1))
            if tree[node][1] != 0:
                queue.append((tree[node][1], level+1))
        print(depth)
    except:
        break