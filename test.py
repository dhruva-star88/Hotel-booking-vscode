import pandas as pd
df_cards = pd.read_csv("cards.csv", dtype=str)
print(df_cards)
enquire = df_cards.loc[df_cards["number"] == "1234", "number"].squeeze()
print(enquire)