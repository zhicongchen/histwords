# -*- coding: UTF-8 -*-

from representations.sequentialembedding import SequentialEmbedding

if __name__ == "__main__":

    ch_embeddings = SequentialEmbedding.load("embeddings/CN", range(1950, 2000, 10))
    A = "电脑"
    B = "病毒"
    print((A, B))
    time_sims = ch_embeddings.get_time_sims(A, B)
    for year, sim in time_sims.items():
        print("CH {year:d}, cosine similarity={sim:0.2f}".format(year=year, sim=sim))

    ch_embeddings = SequentialEmbedding.load("embeddings/CN", range(1950, 2000, 10))
    A = "传统"
    B = "近代"
    print((A, B))
    time_sims = ch_embeddings.get_time_sims(A, B)
    for year, sim in time_sims.items():
        print("CH {year:d}, cosine similarity={sim:0.2f}".format(year=year, sim=sim))

    ch_embeddings = SequentialEmbedding.load("embeddings/CN", range(1950, 2000, 10))
    A = "传统"
    B = "孝"
    print((A, B))
    time_sims = ch_embeddings.get_time_sims(A, B)
    for year, sim in time_sims.items():
        print("CH {year:d}, cosine similarity={sim:0.2f}".format(year=year, sim=sim))

    ch_embeddings = SequentialEmbedding.load("embeddings/CN", range(1950, 2000, 10))
    A = "传统"
    B = "孝順"
    print((A, B))
    time_sims = ch_embeddings.get_time_sims(A, B)
    for year, sim in time_sims.items():
        print("CH {year:d}, cosine similarity={sim:0.2f}".format(year=year, sim=sim))
