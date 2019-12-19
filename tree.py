# len은 나무의 길이(글자수)
# while은 반복문 <20은 20번 반복하고 끝내라는 의미
tree = '나무'
deco = '장식'
print(len(tree))
while len(tree) < 20:
    print(tree)
    tree = tree + deco

christmas_tree = tree
print(christmas_tree)