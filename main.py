import draw_calculator as dc
import streamlit as st

st.title('Card Draw Chance Calculator')
st.subheader('Show the odds of you drawing your deck\'s combo piece(s).')

deck_size = st.number_input(label='The deck size:',value=12,format='%a')
freq = st.number_input(label='Number of combo piece(s):',value=3,format='%a')
draw = st.number_input(label='Number of card(s) in your starting hand:',value=4,format='%a')
n_expected = st.number_input(label='Number of combo piece(s) you expect to draw in starting hand:',value=1,format='%a')


p_exactly_n = dc.p_exactly(n_expected,freq, draw, deck_size)
p_at_least_one = dc.p_at_least_one(freq, draw, deck_size)
p_at_least_n = dc.p_at_least(n_expected, freq, draw, deck_size)
p_exactly_one = dc.p_exactly_one(freq, draw, deck_size)
p_none = dc.p_none(freq, draw, deck_size)


# Display the probs on the streamlit

p_at_least_n = round(p_at_least_n*100,1)
p_at_least_one = round(p_at_least_one*100,1)
p_at_least_n = round(p_at_least_n*100,1)
p_exactly_n = round(p_exactly_n*100,1)
p_none = round(p_none*100,1)

if n_expected == 1:
    st.success(f"{p_at_least_n}% to draw at least {n_expected} of the combo piece(s).")
    st.success(f"{p_exactly_n}% to draw exactly {n_expected} of the combo piece(s).")    
    st.error(f"{p_none}% to draw none of the combo piece(s).")
else:
    st.success(f"{p_at_least_one}% to draw at least 1 of the combo piece(s).")
    st.success(f"{p_at_least_n}% to draw at least {n_expected} of the combo piece(s).")
    st.success(f"{p_exactly_n}% to draw exactly {n_expected} of the combo piece(s).")
    st.error(f"{p_none}% to draw none of the combo piece(s).")