import sys
import copy

def read_file():
    f = open(sys.argv[1] if len(sys.argv) > 1 else "ex.txt", "r")
    l = f.readline()
    f.close()
    return l

line = list(read_file())
line = list(map(int, list(line)))


def part_1():
    file_id_to_len = line[::2]
    l = 0
    checksum = 0
    checksum_i = 0
    id_num = 0
    file_i = len(file_id_to_len) - 1
    res = []
    while l != len(line) - 1:
        start = checksum_i
        for n in range(file_id_to_len[id_num]):
            checksum += id_num * (start + n)
            checksum_i += 1
            file_id_to_len[id_num] -= 1
            res.append(id_num)
        id_num += 1
        if l + 1 >= len(line):
            break
        num_free = line[l + 1]
        start = checksum_i
        for i in range(num_free):
            if file_i <= 0:
                break
            while file_i >= 0 and file_id_to_len[file_i] <= 0:
                file_i -= 1
            if file_i < 0:
                break
            res.append(file_i)
            checksum += file_i * (start + i)
            checksum_i += 1
            file_id_to_len[file_i] -= 1
        l += 2
    
    print(checksum)

class Node:
    def __init__(self, file_id, block_size, is_free):
        self.file_id = file_id # 0 if this is a free space
        self.block_size = block_size 
        self.is_free = is_free
    def __repr__(self):
        return str(self.file_id) + " " + str(self.block_size) + " " + str(self.is_free)
    def __str__(self):
        return str(self.file_id) + " " + str(self.block_size) + " " + str(self.is_free)


def debug(nodes):
    res = ""
    for node in nodes:
        for i in range(node.block_size):
            if node.is_free:
                res += "."
            else:
                res += str(node.file_id)
    print(res)

def part_2():
    nodes = []
    file_index = 0
    for i, elem in enumerate(line):
        if i % 2 == 0:
            nodes.append(Node(file_index, elem, False))
            file_index += 1
        else:
            nodes.append(Node(0, elem, True))
    
    nodes_copy = copy.deepcopy(nodes)
    for i, file_node in reversed(list(enumerate(nodes_copy))):
        if file_node.is_free:
            continue

        for j, free_node in enumerate(nodes):
            if not free_node.is_free:
                continue
            if file_node.block_size <= free_node.block_size:
                index_to_remove = -1
                for k, f in reversed(list(enumerate(nodes))):
                    if not f.is_free and f.file_id == file_node.file_id:
                        index_to_remove = k
                        break
                if index_to_remove <= j:
                    break
                f = nodes.pop(index_to_remove)
                nodes.insert(index_to_remove, Node(0, file_node.block_size, True))
                nodes.insert(j, f)
                free_node.block_size -= file_node.block_size
                if free_node.block_size == 0:
                    nodes.pop(j + 1)
                break

    checksum = 0
    checksum_i = 0
    for node in nodes:
        for i in range(node.block_size):
            checksum += node.file_id * checksum_i
            checksum_i += 1
    print(checksum)

part_1()
part_2() 