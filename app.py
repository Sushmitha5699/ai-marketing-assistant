import streamlit as st
import pandas as pd
from personas_generator import generate_personas
from PIL import Image

st.set_page_config(page_title="AI Marketing Assistant", layout="wide")

st.title("🧠 AI-Powered Marketing Persona Generator")

# Show the visual pipeline
st.subheader("🔍 How It Works")

# Load and show the pipeline image
image = Image.open("assets/pipeline.png")
st.image(image, caption="AI Persona Generation Pipeline", width=600)

# File upload
uploaded_file = st.file_uploader("📤 Upload your CSV file with a 'review' column", type=["csv"])


if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)

        if 'review' not in df.columns:
            st.error("⚠️ The CSV must contain a column named 'review'.")
        else:
            # Cluster control
            k = st.slider("🔢 How many personas would you like?", min_value=2, max_value=10, value=3)

            if st.button("🌀 Generate Personas"):
                with st.spinner("Clustering reviews and creating personas..."):
                    personas = generate_personas(df, k)

                st.success(f"{len(personas)} personas created!")

                for persona in personas:
                    with st.expander(f"📌 {persona['persona']} — Keywords: {', '.join(persona['keywords'])}"):
                        st.markdown(f"**Hook:** {persona['hook']}")
                        st.markdown(f"**Body:** {persona['body']}")
                        st.markdown(f"**CTA:** {persona['cta']}")

    except Exception as e:
        st.error(f"Something went wrong: {e}")
else:
    st.info("Please upload a CSV file to get started.")


st.markdown("""
### How This Works

This tool allows marketing executives to upload raw customer reviews in CSV format. Here's how it helps:

1. **Input**: Upload your reviews CSV file.
2. **Processing**: We analyze and cluster the text using AI.
3. **Output**: You get clear, data-backed marketing personas.

#### Why It Matters

- Each persona represents a group of similar customers.
- You can **generate content using AI tools** based on these personas (like Midjourney, DALL·E, or GPT-based tools).
- These insights help **graphic designers and copywriters** craft campaigns that resonate.
- Ultimately, this leads to **higher ROI** by creating audience-aligned messaging.

""")





# How it works
with st.expander("🧠 How does the tech work?"):
    st.markdown("""
    We use **KMeans clustering**, a type of machine learning, to group similar customer reviews together.  
    Each cluster represents a **persona** with common needs, language, and preferences.

    Here's the process:
    1. We convert reviews into numbers using **TF-IDF**, which tracks word importance.
    2. We then group similar reviews using **KMeans** into the number of personas you selected.
    3. For each group, we find the **top 5 keywords** and generate a sample marketing message using real review content.

    You can use this to:
    - Write better ad copy
    - Understand your audience
    - Tailor your campaigns
    """)

