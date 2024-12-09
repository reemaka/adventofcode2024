import sys

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
    r = len(line) - 1
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

part_1()