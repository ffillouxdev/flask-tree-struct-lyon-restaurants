class TreeNode:
    def __init__(self, category):
        self.category = category
        self.children = []
        self.restaurants = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def add_restaurant(self, restaurant):
        self.restaurants.append(restaurant)

    def __repr__(self):
        return f"TreeNode({self.category.name})"
