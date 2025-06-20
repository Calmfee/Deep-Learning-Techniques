#This code is done by Jaihind Subaash M D, 2117230020074
def mcp_neuron(inputs, weights, threshold):
    summation = sum(i * w for i, w in zip(inputs, weights))
    return 1 if summation >= threshold else 0

def AND(x1, x2):
    return mcp_neuron([x1, x2], [1, 1], 2)

def OR(x1, x2):
    return mcp_neuron([x1, x2], [1, 1], 1)

def NOT(x1):
    return mcp_neuron([x1], [-1], 0)

def NOR(x1, x2):
    return mcp_neuron([x1, x2], [-1, -1], 0)

def XOR(x1, x2):
    return x1 ^ x2  


inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]


print("AND")
for x in inputs:
    print(f"{x} -> {AND(x[0], x[1])}")

print("\nOR")
for x in inputs:
    print(f"{x} -> {OR(x[0], x[1])}")

print("\nNOT")
for x in [0, 1]:
    print(f"{x} -> {NOT(x)}")

print("\nNOR")
for x in inputs:
    print(f"{x} -> {NOR(x[0], x[1])}")

print("\nXOR")
for x in inputs:
    print(f"{x} -> {XOR(x[0], x[1])}")

print("\nResult")
print("Thus the program for logical functions using McCulloch-Pitts Neuron has been executed successfully.")
