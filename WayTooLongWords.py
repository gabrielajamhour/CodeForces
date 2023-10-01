num_inputs = int(input())
palavrastotal = []

for i in range(num_inputs):
    palavra = input()
    palavrastotal.append(palavra)

for palavra in palavrastotal:
    if len(palavra)>10:
        print(palavra[0],len(palavra)-2,palavra[-1],sep="")
    else:
        print(palavra)
