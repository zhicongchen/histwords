# -*- coding: UTF-8 -*-

from representations.sequentialembedding import SequentialEmbedding

if __name__ == "__main__":

    # ch_embeddings = SequentialEmbedding.load("embeddings/CN", range(1950, 2000, 10))
    # A = ch_embeddings.get_seq_closest("尊重", 1990)
    # print(A)

    ch_embeddings = SequentialEmbedding.load("embeddings/CN", range(1950, 2000, 10))
    for year in range(1950, 2000, 10):
        A = ch_embeddings.get_seq_closest("尊重", year)
        print(year, A)

# result after running
# python3 respect.py 
# 1950 ['尊重', '平等', '主权', '侵犯', '信任', '互利', '关心', '领土', '遵守', '信仰']
# 1960 ['尊重', '平等', '侵犯', '主权', '信任', '互利', '关心', '遵守', '领土', '信仰']
# 1970 ['尊重', '爱护', '平等', '侵犯', '首创', '平易近人', '尊', '互利', '信任', '取长补短']
# 1980 ['尊重', '尊', '平等', '爱护', '信赖', '侵犯', '诚心', '和睦', '爱戴', '藏族']
# 1990 ['尊重', '尊', '求同存异', '互信', '平等', '侵犯', '藏族', '信赖', '爱护', '平易近人']
