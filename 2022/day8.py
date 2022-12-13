with open('input.txt') as txt:
    input = txt.read().splitlines()

# part 1

trees = [[int(t) for t in row] for row in input]
num_vis = 2*len(trees) + 2*len(trees[0]) - 4

for i, tree_row in enumerate(trees[1:-1]):
    for j, tree in enumerate(tree_row[1:-1]):
        r = i + 1
        c = j + 1
        visible = False
        # visible from top
        for a in reversed(range(r)):
            if trees[a][c] >= tree:
                break
            if a == 0:
                visible = True
        # visible from right
        for a in range(c+1, len(tree_row)):
            if trees[r][a] >= tree:
                break
            if a == len(tree_row)-1:
                visible = True
        # visible from bottom
        for a in range(r+1, len(trees)):
            if trees[a][c] >= tree:
                break
            if a == len(trees)-1:
                visible = True
        # visible from right
        for a in reversed(range(c)):
            if trees[r][a] >= tree:
                break
            if a == 0:
                visible = True
        num_vis += 1 if visible else 0

print(num_vis)

# part 2
scenic_score = float('-inf')
for i, tree_row in enumerate(trees[1:-1]):
    for j, tree in enumerate(tree_row[1:-1]):
        r = i + 1
        c = j + 1
        # visible from top
        vis_top = 0
        for a in reversed(range(r)):
            if trees[a][c] >= tree:
                vis_top += 1
                break
            else:
                vis_top += 1
        # visible from right
        vis_right = 0
        for a in range(c+1, len(tree_row)):
            if trees[r][a] >= tree:
                vis_right += 1
                break
            else:
                vis_right += 1
        # visible from bottom
        vis_bot = 0
        for a in range(r+1, len(trees)):
            if trees[a][c] >= tree:
                vis_bot += 1
                break
            else:
                vis_bot += 1
        # visible from left
        vis_left = 0
        for a in reversed(range(c)):
            if trees[r][a] >= tree:
                vis_left += 1
                break
            else:
                vis_left += 1
        scenic_score = max(scenic_score, vis_left*vis_right*vis_top*vis_bot)

print(scenic_score)