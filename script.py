from SZI_INFO import SZI_models
print(SZI_models[0][0])
with open('price.txt', 'w') as f:
    for i in range(len(SZI_models)):
        f.write(SZI_models[i][0])
        f.write(f"{SZI_models[i][1]}\n")
f.close()