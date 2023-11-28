import matplotlib.pyplot as plt

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert_node(root, value):
    if root is None:
        return Node(value)

    if value < root.value:
        root.left = insert_node(root.left, value)
    elif value > root.value:
        root.right = insert_node(root.right, value)
    else:
        root.right = insert_node(root.right, value)  # Вставка справа для одинаковых значений

    return root

def visualize_tree(root, x, y, ax):
    if root is None:
        return

    ax.text(x, y, str(root.value), fontsize=12, fontweight='bold', ha='center', va='center')

    if root.left:
        ax.plot([x, x-1], [y-1, y+1], color='black')  # Левая связь
        visualize_tree(root.left, x-1, y+1, ax)

    if root.right:
        ax.plot([x, x+1], [y-1, y+1], color='black')  # Правая связь
        visualize_tree(root.right, x+1, y+1, ax)

def search_value(root, value):
    if root is None or root.value == value:
        return root

    if value < root.value:
        return search_value(root.left, value)
    else:
        return search_value(root.right, value)

# Создание дерева
root_value = int(input("Введите значение корневого узла: "))
root = Node(root_value)

more_values = input("Введите значения узлов через пробел: ").split()
for value in more_values:
    root = insert_node(root, int(value))

# Визуализация дерева
fig, ax = plt.subplots(figsize=(8, 6))
visualize_tree(root, 0, 0, ax)
ax.set_xlim(-5, 5)
ax.set_ylim(0, 10)
ax.axis('off')
plt.title('Binary Search Tree')
plt.show()

# Поиск значения в дереве
search_value_input = int(input("Введите значение для поиска: "))
result = search_value(root, search_value_input)
if result:
    print("Значение найдено в дереве!")
else:
    print("Значение не найдено в дереве.")