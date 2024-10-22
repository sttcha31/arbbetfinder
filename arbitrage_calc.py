
def odd_to_prob(moneyline):
    if(moneyline < 0):
        return (-moneyline/(-moneyline+100))
    else:
        return (100/(moneyline+100))

    
def arbitrage_find(book1, book2, budget):
    if (total:=odd_to_prob(book1[0]) + odd_to_prob(book2[1])) < 1:
        return (budget*odd_to_prob(book1[0])/total, budget*odd_to_prob(book2[1])/total)
    if (total:=odd_to_prob(book1[1]) + odd_to_prob(book2[0])) < 1:
        return (budget*odd_to_prob(book1[1])/total, budget*odd_to_prob(book2[0])/total)

print(arbitrage_find((-333,270),(-250,198),100))