import ast
master_data ={"functions": [], "expressions": [], "ifs": []}


def node_iterator(nodes):
    global master_data
    for node in nodes:
        if isinstance(node, ast.FunctionDef):
            print(f"Function name: {node.name}")
            print(f"Arguments: {[arg.arg for arg in node.args.args]}\n")  
            master_data["functions"].append(node.name)
            node_iterator(ast.iter_child_nodes(node))

        elif isinstance(node, ast.Expr):
            print(f"Node Value: {node.value}")
            master_data["expressions"].append(ast.dump(node.value))
            node_iterator(ast.iter_child_nodes(node))
        
        elif isinstance(node, ast.If):
            print(f"Type {node.test}\n")
            master_data["ifs"].append(ast.dump(node.test))
            print(len(node.body))
            print("END IF BODY")
            node_iterator(ast.iter_child_nodes(node))

        elif isinstance(node, ast.Call):
            print(f"Function Call: {ast.dump(node)}\n")
            node_iterator(ast.iter_child_nodes(node))
        
        elif isinstance(node, ast.Assign):
            print(f"Assignment: {ast.dump(node)}\n")
            node_iterator(ast.iter_child_nodes(node))

        elif isinstance(node, ast.Return):
            print(f"Return Statement: {ast.dump(node)}\n")
            node_iterator(ast.iter_child_nodes(node))

        elif isinstance(node, ast.Compare):
            print(f"Comparison: {ast.dump(node)}\n")
            node_iterator(ast.iter_child_nodes(node))

        elif isinstance(node, ast.arguments):
            print(f"Arguments: {ast.dump(node)}\n")
            node_iterator(ast.iter_child_nodes(node))

        else:
            print(f"NO Node type matched {type(node)}\n")


call_tree = []
with open("./tests/test.py", "r") as file:
    content = file.read()
    root = ast.parse(content, filename="./tests/test.py")
    #print(ast.dump(tree, indent=2))

    #walker = ast.walk(tree)
    #for node in walker:
        #print(node)


        #if isinstance(node, ast.FunctionDef):
        #    print(f"Function name: {node.name}")
        #    print(f"Arguments: {[arg.arg for arg in node.args.args]}") 

    #print(ast.iter_child_nodes(tree))#So tree is the modele itself, This is then everything inside it. Walk not typically important becuase its documented as Recursively yield all descendant nodes in the tree starting at node (including node itself), in no specified order. This is useful if you only want to modify nodes in place and don’t care about the context. 
    """
    <ast.Expr object at 0x0000025FA67C66D0>
    <ast.FunctionDef object at 0x0000025FA67C6610>
    <ast.FunctionDef object at 0x0000025FA67C5B50>
    <ast.FunctionDef object at 0x0000025FA67C5550>
    <ast.If object at 0x0000025FA67C4E10>
    """

    node_iterator(ast.iter_child_nodes(root))

#print(master_data)
#print("Call Tree")
