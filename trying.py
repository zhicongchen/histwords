from representations.sequentialembedding import SequentialEmbedding

if __name__ == "__main__":
    print(("japan", "china"))
    eng_embeddings = SequentialEmbedding.load("embeddings/EN", range(1950, 1990, 10))
    time_sims = eng_embeddings.get_time_sims("japan", "china")   
    for year, sim in time_sims.items():
        print("ENG {year:d}, cosine similarity={sim:0.2f}".format(year=year,sim=sim))

    ch_embeddings = SequentialEmbedding.load("embeddings/CN", range(1950, 1990, 10))
    print(("电脑", "病毒"))
    time_sims = ch_embeddings.get_time_sims("电脑", "病毒")   
    for year, sim in time_sims.items():
        print("CH {year:d}, cosine similarity={sim:0.2f}".format(year=year,sim=sim))

    ch_embeddings = SequentialEmbedding.load("embeddings/CN", range(1950, 1990, 10))
    print(("月", "年"))
    time_sims = ch_embeddings.get_time_sims("月", "年")   
    for year, sim in time_sims.items():
        print("CH {year:d}, cosine similarity={sim:0.2f}".format(year=year,sim=sim))

    ch_embeddings = SequentialEmbedding.load("embeddings/CN", range(1950, 1990, 10))
    print(("父", "母"))
    time_sims = ch_embeddings.get_time_sims("父", "母")
    for year, sim in time_sims.items():
        print("CH {year:d}, cosine similarity={sim:0.2f}".format(year=year,sim=sim))
