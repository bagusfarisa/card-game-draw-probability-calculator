# Chance to draw none of the combo pieces
def p_none(freq, draw=7, deck_size=60):
    p_not = 1.0;
    for j in range(draw):
        p_not *= float(deck_size - j - freq) / float(deck_size - j)
        
    return p_not

# Chance to draw at least one of the expected combo pieces
def p_at_least_one(freq, draw=7, deck_size=60):
    if draw == 0:
        return 0.0
        
    if draw > deck_size:
        raise Exception('trying to draw more cards than there are in the deck')
        
    return 1 - p_none(freq, draw=draw, deck_size=deck_size)

# Chance to draw one of the combo pieces
def p_exactly_one(freq, draw=7, deck_size=60):
    if draw == 0:
        return 0.0
        
    if draw > deck_size:
        raise Exception('trying to draw more cards than there are in the deck')
    
    p_got_one = float(freq) / float(deck_size)
    if draw == 1:
        result = p_got_one
    else:
        r1 = p_got_one * p_none(freq - 1, draw=draw-1, deck_size=deck_size - 1)
        r2 = (1 - p_got_one) * p_exactly_one(freq, draw=draw-1, deck_size= deck_size - 1)
        result = r1 + r2

    return result

# Chance to draw n number of combo pieces
def p_exactly(n, freq, draw=7, deck_size=60):
    if draw == 0 or deck_size == 0:
        return 0.0
        
    if n==1:
        result = p_exactly_one(freq, draw=draw, deck_size=deck_size)
        
    else:
        p_got_one = float(freq) / float(deck_size)
        r1 = p_got_one * p_exactly(n - 1, freq - 1, draw=draw-1, deck_size=deck_size-1)
        r2 = (1 - p_got_one) * p_exactly(n, freq, draw=draw-1, deck_size=deck_size-1)
        result = r1 + r2
        
    return result
    

# Chance to draw at least n number of the combo pieces
def p_at_least(n, freq, draw=7, deck_size=60):
    # n is how many you want at least
    if draw == 0 or deck_size == 0:
        return 0.0
        
    if n==1:
        result = p_at_least_one(freq, draw=draw, deck_size=deck_size)
    
    else:
        p_got_one = float(freq) / float(deck_size)
        r1 = p_got_one * p_at_least(n - 1, freq - 1, draw=draw-1, deck_size=deck_size-1)
        r2 = (1 - p_got_one) * p_at_least(n, freq, draw=draw-1, deck_size=deck_size-1)
        result = r1 + r2
    
    return result
