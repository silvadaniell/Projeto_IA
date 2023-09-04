import json

class Node:
    def __init__(self, data, yes=None, no=None):
        self.data = data
        self.yes = yes
        self.no = no

def ask(question):
    answer = input(f"{question} (y/n): ").strip().upper()
    return answer == "Y"

def build_tree(node, data):
    if "yes" in data:
        node.yes = Node(data["yes"]["data"])
        build_tree(node.yes, data["yes"])
    if "no" in data:
        node.no = Node(data["no"]["data"])
        build_tree(node.no, data["no"])

def start(node):
    while node.yes and node.no:
        if ask(node.data):
            node = node.yes
        else:
            node = node.no
    if not ask(f"{node.data}?"):
        print("Desculpe, não sei diagnosticar.")
    else:
        print("Agora você já sabe o seu diagnóstico.")

if __name__ == "__main__":
    with open('tree_b.json', 'r') as file:
        tree_data = json.load(file)
        root = Node(tree_data['data'])
        build_tree(root, tree_data)

    print("Diga y para sim ou n para não às minhas perguntas e eu descobrirei o seu diagnóstico.")

    while ask("Deseja iniciar?"):
        node = root
        start(node)
