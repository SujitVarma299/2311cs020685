dict1 = {"a":12,"abc":123,"def":45}
result = {value: key for key,value in dict1.items()}
print(result)