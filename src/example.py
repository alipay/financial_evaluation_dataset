from utils.dataloader import load_dataset, load_dataset_SUFE, load_dataset_Ant

# dev有答案；test没答案；full是dev+test的集合
dataset = load_dataset_Ant("../data/Ant", "dev")
print("*"*30)
print("蚂蚁dev测评集总数：" + str(len(dataset)))
print("单个样例：")
print(dataset[0])

dataset = load_dataset_SUFE("../data/SUFE", "test")
print("*"*30)
print("上财test测评集总数：" + str(len(dataset)))
print("单个样例：")
print(dataset[0])

dataset = load_dataset("../data", "full")
print("*"*30)
print("整体测评集总数：" + str(len(dataset)))
print("单个样例：")
print(dataset[0])
