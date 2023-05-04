while True:
    try:
        n, p = map(int, input().split())
        heights = list(map(int, input().split()))
        widths = list(map(int, input().split()))
    except:
        break
    
    max_height = 0
    poster_idx = 0
    available_width = 0
    
    for i in range(n):
        available_width += 1
        while poster_idx < p and widths[poster_idx] == available_width:
            if all(heights[j] >= max_height + 1 for j in range(i - available_width + 1, i + 1)):
                max_height += 1
            poster_idx += 1
            available_width = 0
        
    print(max_height)
    