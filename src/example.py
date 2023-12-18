from utils.dataloader import load_dataset

dataset = load_dataset("../data", "dev")

print("测评集总数：" + str(len(dataset)))
print("单个样例：")
print(dataset[0])
