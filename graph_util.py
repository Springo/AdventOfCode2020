def top_sort(adj_list):
    visited = dict()
    for key in adj_list:
        visited[key] = False

    stack = []

    for key in adj_list:
        if not visited[key]:
            _top_sort_helper(adj_list, key, visited, stack)

    return stack[::-1]


def _top_sort_helper(adj_list, v, visited, stack):
    visited[v] = True
    for neighb in adj_list[v]:
        if not visited[neighb]:
            _top_sort_helper(adj_list, neighb, visited, stack)

    stack.append(v)


if __name__ == "__main__":
    adj_list = dict()
    adj_list['x'] = ['y']
    adj_list['y'] = []
    adj_list['z'] = ['x', 'y']
    print(top_sort(adj_list))
