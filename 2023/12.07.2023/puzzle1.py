from collections import Counter
import pandas as pd

with open("input.txt", "r") as f:
    lines = f.read().splitlines()

hands = [line.split()[0] for line in lines]
bids = [int(line.split()[1]) for line in lines]

hand_bid = dict(zip(hands,bids))

def card_numeric(card: str) -> int:
    m = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 11,
        "T": 10
    }
    if card in m:
        return m[card]
    else:
        return int(card)

def get_rank_info(hand_bid: tuple) -> list:
    dist = Counter(hand_bid[0]).most_common(5)
    if len(dist) == 1:
        kind = 7
    elif dist[0][1] == 4:
        kind = 6
    elif dist[0][1] == 3 and dist[1][1] == 2:
        kind = 5
    elif dist[0][1] == 3 and len(dist) == 3:
        kind = 4
    elif dist[0][1] == 2 and len(dist) == 3:
        kind = 3
    elif dist[0][1] == 2:
        kind = 2
    else:
        kind = 1
    return [kind]+[card_numeric(c) for c in hand_bid[0]] + [hand_bid[1]]
    
df = pd.DataFrame([get_rank_info((hand, bid)) for hand, bid in hand_bid.items()])
df.columns = ["kind","card1","card2","card3","card4","card5","bid"]
df = df.sort_values(["kind","card1","card2","card3","card4","card5"]).reset_index()
df["rank"] = df.index+1
df["winnings"] = df["bid"]*df["rank"]

print(df["winnings"].sum())