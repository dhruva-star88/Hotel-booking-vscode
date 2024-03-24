import pandas as pd
df_cards = pd.read_csv("cards.csv", dtype=str)
df_sec_card = pd.read_csv("card_security.csv", dtype=str)
print(df_sec_card)
password = df_sec_card.loc[df_sec_card["number"] == "1234", "password"].squeeze()
print(password)