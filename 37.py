height = [125,127,136,134,137,138,126,135,140,145]
quility = []
for i in range(len(height)):
    if height[i] > 135:
        quility.append(height[i])
print('新增' + str(len(quility)) + '名成员，她们的身高从矮到高分别是：' + str(quility).strip('[]'))