nambers = []
def calculate_structure_sum(*data_structure):
    for i in data_structure:
        if isinstance(i, int):
            nambers.append(i)
        elif isinstance(i, str):
            nambers.append(len(i))
        elif isinstance(i, dict):
            for key, znach in i.items():
                calculate_structure_sum(key)
                calculate_structure_sum(znach)
        elif isinstance(i, tuple):
            for j in i:
                calculate_structure_sum(j)
        else:
            isinstance(i, set)
            for k in i:
                calculate_structure_sum(k)
        return sum(nambers)

data_structure = [[1,2,3],{'a':4,'b':5},(6,{'cube':7,'drum':8}),'Hello',((),[{(2,'Urban',('Urban2',35))}])]
result = calculate_structure_sum(data_structure)
print(result)