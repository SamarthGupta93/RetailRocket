class TreeNode:
    def __init__(self,value,children=None):
        self.val = value
        self.children = children
        
class CategoryTree:
    def __init__(self, df_category_tree):
        self.df_category_tree = df_category_tree
        
    def get_children(self,cat):
        return self.df_category_tree.query("parentid=="+str(cat))['categoryid'].unique()

    def create_tree(self,rootCat):
        rootNode = TreeNode(rootCat)
        children = self.get_children(rootNode.val)
        if children is None or len(children)==0:
            return rootNode
        rootNode.children = []
        for child in children:
            rootNode.children.append(self.create_tree(child))
        return rootNode
    
    
    def search(self, category, tree):
        if tree is None:
            return False
        if tree.val==category:
            return True
        if tree.children is None:
            return False
        for subtree in tree.children:
            if self.search(category,subtree):
                return True
        return False
    
    
    def print_tree(self, root, depth):
        if root is None:
            return
        print("\t"*depth+"Root:",root.val)
        if root.children is None: return
        for subTree in root.children:
            self.print_tree(subTree,depth+1)