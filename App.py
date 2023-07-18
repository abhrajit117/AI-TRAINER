import streamlit as st

st.set_page_config(
    page_title="AI Trainer",
    page_icon="💪",
)
st.title("Choose Exercise to Track 😉��💪")
st.sidebar.success("Select a Exercise Above")

# with open("style.css") as f:
#     st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# col1, col2, col3, col4, col5 = st.columns(5)
# col1.metric("Using Dumble", "Hammer Curl", "Accuracy 95%")
# col2.metric("Using hads", "Pushup", "Accuracy 85%")
# col3.metric("Using Legs", "Jumping", "Accuracy 90%")
# col4.metric("Using Weights", "Lifting", "Accuracy 97%")
# col5.metric("Using Bichi ", "India curl", "Accuracy 93%")


def generate_card(title, description,links):
    card_html = f"""
        <div style="background-color: #141414;border: 4px solid green; padding: 20px; border-radius: 10px; margin-bottom: 20px;">
            <h2>{title}</h2>
            <p>{description}</p>
            <a href="{links}" >
                <button style="padding: 10px 20px; background-color: green; color: #bcff96; border-radius: 5px; cursor: pointer;font-size: 1.2rem">
                Start Exercise
                </button>
            </a>
        </div>
    """
    return card_html


# Create responsive cards using HTML
st.markdown(
    """
    <style>
        @media (min-width: 600px) {
            .cards-container {
                display: flex;
                flex-wrap: wrap;
                justify-content: space-between;
            }
        }
    </style>
""",
    unsafe_allow_html=True,
)

st.markdown("<div class='cards-container'>", unsafe_allow_html=True)

# Generate and display multiple cards
card1 = generate_card("Hammer Curl", "This is the description for Card 1.","http://localhost:8501/HammerCurl")
card2 = generate_card("Jump", "This is the description for Card 2.","http://localhost:8501/Jump")
card3 = generate_card("Lifting", "This is the description for Card 3.","http://localhost:8501/Lifting")
card4 = generate_card("Pushup", "This is the description for Card 4.","http://localhost:8501/Pushup")
card5 = generate_card("Indian Curl", "This is the description for Card 5.","http://localhost:8501/Indian_Curl")

st.markdown(card1, unsafe_allow_html=True)
st.markdown(card2, unsafe_allow_html=True)
st.markdown(card3, unsafe_allow_html=True)
st.markdown(card4, unsafe_allow_html=True)
st.markdown(card5, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
