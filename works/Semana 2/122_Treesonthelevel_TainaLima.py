import sys

def transformStringToGraph(case):
    list_nodes = case.split()
    list_nodes.remove("()")

    list_of_paths_from_root = []
    graph = {}
    root_node = ""
    
    for node in list_nodes:
        value, path_from_root = node[1:len(node)-1].split(",")

        if (not value):
            return {}, ""
        
        if not path_from_root:
            if not root_node:
                root_node = value
            else:
                return {}, ""
        else:
            if len(path_from_root) not in graph.keys():
                graph[len(path_from_root)] = {}
            
            if path_from_root in graph[len(path_from_root)].keys():
                return {}, ""
        
            graph[len(path_from_root)][path_from_root] = value
            list_of_paths_from_root.append(path_from_root)


    for i in range(len(list_of_paths_from_root)):
        list_without_path = list_of_paths_from_root[:i] +  list_of_paths_from_root[i:]
        path = list_of_paths_from_root[i]

        if (len(path[:len(path)-1]) == 1) and (path[:len(path)-1] not in list_without_path):
            return {}, ""
            
        elif (len(path[:len(path)-1]) > 1) and (path[:len(path)-1] not in "///".join(list_without_path)):
            return {}, ""

    return graph, root_node


def breadthFirstSearch(graph, root_node):
    path = [root_node]

    for level in sorted(graph):
        path.extend([graph[level][path_from_root]  for path_from_root in sorted(graph[level]) ])

    return " ".join(path)

if __name__ == "__main__":
    cases = []
    case = ""
    for line in sys.stdin:
        if line == '':
            break
        if(line.strip()[-2:] == "()"):
            case += (line.strip() + " ")
            cases.append(case)
            case = ""
        else:
            case += (line.strip() + " ")

    for case in cases:
        graph, root_node = transformStringToGraph(case)

        if root_node:

            print(breadthFirstSearch(graph, root_node))
        else:
            print("not complete")

