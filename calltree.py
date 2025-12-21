import ast
root_info = {"num_functions": 0, "functions":{}}


def node_iterator(nodes, parent):
    for node in nodes:
        
        if not isinstance(node, ast.FunctionDef) and not isinstance(node, ast.ClassDef):
            #print(f"Type: {type(node).__name__}")
            if isinstance(node, ast.If):
                node_iterator(node.body, node) #Right now only recuring the call not the test statement
            elif isinstance(node, ast.Expr):
                node_iterator(ast.iter_child_nodes(node), node)
            elif isinstance(node, ast.Assign):
                node_iterator(ast.iter_child_nodes(node), node)
            elif isinstance(node, ast.Call):
                function_name= node.func.id
                print(f"| {function_name}")
                node_iterator(ast.iter_child_nodes(node), node)
            elif isinstance(node, ast.Return):
                node_iterator(ast.iter_child_nodes(node), node)
            else:
                node_iterator(ast.iter_child_nodes(node), node)
            #print("Recuse into children\n")
            #node_iterator(ast.iter_child_nodes(node), node)
            #print(f"End Recurse Type: {type(node).__name__}\n")
            
        else:
            #print(f"{type(node).__name__} name: {node.name}")
            root_info["num_functions"] += 1
            root_info["functions"][node.name] = {"type": type(node).__name__, "parent": parent, "obj": node}
    

with open("./tests/test.py", "r") as file:
    content = file.read()
    root = ast.parse(content, filename="./tests/test.py")
    
    print("test.py")
    node_iterator(ast.iter_child_nodes(root), "test.py")


    #print(root_info)
    
