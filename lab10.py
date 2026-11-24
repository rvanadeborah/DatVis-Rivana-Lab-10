
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =========================================================
# 1. PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Lab 10 | Frame the Data Story",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# 2. SESSION STATE
# =========================================================

default_ratings = {
    "Data storytelling": 2.4,
    "Python": 3.0,
    "Chart selection": 3.2,
    "Color and labels": 3.7,
    "Data cleaning": 4.1
}

if "lab10_ratings_v2" not in st.session_state:
    st.session_state.lab10_ratings_v2 = default_ratings.copy()

# =========================================================
# 3. CUSTOM CSS
# =========================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #F7F5FF 0%, #F0F6FF 55%, #FFF7F0 100%);
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1250px;
}

.hero {
    background: linear-gradient(120deg, #51418F, #8172BD, #A99BE0);
    padding: 55px 50px;
    border-radius: 25px;
    color: white;
    margin-bottom: 30px;
    box-shadow: 0 12px 30px rgba(81,65,143,0.15);
}

.hero-tag {
    display: inline-block;
    background: rgba(255,255,255,0.18);
    padding: 7px 16px;
    border-radius: 30px;
    font-size: 12px;
    letter-spacing: 1px;
    font-weight: 600;
    margin-bottom: 18px;
}

.hero h1 {
    color: white !important;
    font-size: 48px !important;
    font-weight: 800 !important;
    line-height: 1.15 !important;
    margin-bottom: 15px !important;
}

.hero p {
    color: #F2EEFF !important;
    font-size: 16px !important;
    max-width: 720px;
    line-height: 1.8;
}

.section-heading {
    color: #51418F;
    font-size: 25px;
    font-weight: 800;
    margin-top: 30px;
    margin-bottom: 8px;
}

.section-description {
    color: #77738A;
    font-size: 14px;
    margin-bottom: 20px;
}

.info-card {
    background: white;
    padding: 24px;
    border-radius: 18px;
    border: 1px solid #EAE5F8;
    box-shadow: 0 5px 18px rgba(70,55,120,0.05);
    height: 100%;
}

.info-card h3 {
    color: #51418F !important;
    font-size: 18px !important;
    font-weight: 700 !important;
}

.info-card p {
    color: #77738A !important;
    font-size: 14px !important;
    line-height: 1.7;
}

.metric-card {
    background: white;
    padding: 22px;
    border-radius: 18px;
    border: 1px solid #EAE5F8;
    text-align: center;
    box-shadow: 0 5px 18px rgba(70,55,120,0.05);
}

.metric-label {
    color: #89849B;
    font-size: 12px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.metric-value {
    color: #51418F;
    font-size: 34px;
    font-weight: 800;
    margin-top: 5px;
}

.takeaway {
    background: linear-gradient(120deg, #FFF0DC, #FFF8EF);
    border-left: 6px solid #F39A45;
    border-radius: 16px;
    padding: 25px;
    margin: 20px 0;
}

.takeaway h3 {
    color: #9B5B20 !important;
    font-size: 20px !important;
    font-weight: 800 !important;
}

.takeaway p {
    color: #77532F !important;
    font-size: 15px !important;
    line-height: 1.7;
}

.principle-card {
    background: linear-gradient(120deg, #51418F, #8172BD);
    border-radius: 18px;
    padding: 28px;
    margin-top: 20px;
    color: white;
}

.principle-card h3 {
    color: white !important;
    font-size: 21px !important;
}

.principle-card p {
    color: #F2EEFF !important;
    line-height: 1.8;
}

.footer {
    text-align: center;
    padding: 25px;
    color: #89849B;
    font-size: 12px;
    margin-top: 40px;
}

div[data-testid="stMetric"] {
    background: white;
    padding: 18px;
    border-radius: 15px;
    border: 1px solid #EAE5F8;
}

.stButton > button {
    background: #51418F;
    color: white;
    border-radius: 12px;
    border: none;
    padding: 10px 20px;
}

.stButton > button:hover {
    background: #8172BD;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# 4. HERO SECTION
# =========================================================

st.markdown("""
<div class="hero">
    <div class="hero-tag">TFB3133 / TEB3133 · LAB 10</div>
    <h1>FRAME THE DATA.<br>TELL THE STORY.</h1>
    <p>
        Numbers are only the beginning. Discover how to turn
        data into a meaningful message that your audience
        can understand, remember, and act on.
    </p>
</div>
""", unsafe_allow_html=True)

# =========================================================
# 5. INTRODUCTION
# =========================================================

st.markdown("""
<div class="section-heading">The Story Behind the Data</div>
<div class="section-description">
    Understanding the audience before presenting the numbers.
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="info-card">
        <h3>Our Audience</h3>
        <p>
            Students who completed a self-rating survey about
            their data visualization skills and are preparing
            for a future workshop.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
        <h3>Our Purpose</h3>
        <p>
            Identify which visualization skills need more
            improvement so that the next workshop can focus
            on the students' learning needs.
        </p>
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# 6. AUDIENCE SELECTION
# =========================================================

st.markdown("""
<div class="section-heading">Choose Your Audience</div>
<div class="section-description">
    The same data can tell different stories depending on who is reading it.
</div>
""", unsafe_allow_html=True)

audience = st.selectbox(
    "Who are you presenting this data to?",
    [
        "Students",
        "Workshop Organizers",
        "University Lecturers"
    ]
)

audience_messages = {
    "Students": "Use this information to understand which skills you should improve before the next workshop.",
    "Workshop Organizers": "Use these results to prioritize training topics and allocate workshop time effectively.",
    "University Lecturers": "Use these results to understand students' current abilities and identify learning gaps."
}

st.info(audience_messages[audience])

# =========================================================
# 7. DATA AND INTERACTIVE RATINGS
# =========================================================

st.markdown("""
<div class="section-heading">Explore the Data</div>
<div class="section-description">
    These are fictional example averages provided for this lab exercise,
    not actual survey findings. Adjust the ratings to explore the story.
</div>
""", unsafe_allow_html=True)

st.markdown("### Adjust the average self-ratings")

rating_cols = st.columns(5)

for i, (skill, rating) in enumerate(
    st.session_state.lab10_ratings_v2.items()
):
    with rating_cols[i]:
        st.session_state.lab10_ratings_v2[skill] = st.slider(
            skill,
            min_value=1.0,
            max_value=5.0,
            value=float(rating),
            step=0.1,
            key=f"rating_slider_{i}"
        )

ratings = st.session_state.lab10_ratings_v2

df = pd.DataFrame({
    "Skill": list(ratings.keys()),
    "Average Rating": list(ratings.values())
})

lowest_skill = df.loc[df["Average Rating"].idxmin()]
highest_skill = df.loc[df["Average Rating"].idxmax()]

# =========================================================
# 8. KEY METRICS
# =========================================================

st.markdown("""
<div class="section-heading">At a Glance</div>
""", unsafe_allow_html=True)

m1, m2, m3 = st.columns(3)

with m1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Lowest Rating</div>
        <div class="metric-value">{lowest_skill['Average Rating']:.1f}/5</div>
        <p>{lowest_skill['Skill']}</p>
    </div>
    """, unsafe_allow_html=True)

with m2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Highest Rating</div>
        <div class="metric-value">{highest_skill['Average Rating']:.1f}/5</div>
        <p>{highest_skill['Skill']}</p>
    </div>
    """, unsafe_allow_html=True)

with m3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Overall Average</div>
        <div class="metric-value">{df['Average Rating'].mean():.1f}/5</div>
        <p>Across five skills</p>
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# 9. DATA VISUALIZATION
# =========================================================

st.markdown("""
<div class="section-heading">Comparing Visualization Skills</div>
<div class="section-description">
    Average self-rating across five data visualization skills.
    Higher values indicate greater confidence.
</div>
""", unsafe_allow_html=True)

fig, ax = plt.subplots(figsize=(11, 5))

bar_colors = [
    "#F39A45" if skill == lowest_skill["Skill"] else "#9B8BD1"
    for skill in df["Skill"]
]

bars = ax.barh(
    df["Skill"],
    df["Average Rating"],
    color=bar_colors,
    height=0.58
)

ax.set_xlim(0, 5)
ax.set_xlabel("Average Self-Rating (1–5)", fontsize=11, labelpad=12)
ax.set_title(
    "Students' Data Visualization Skills",
    fontsize=17,
    fontweight="bold",
    color="#51418F",
    pad=20
)

ax.invert_yaxis()
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["bottom"].set_color("#DDD8EA")
ax.tick_params(axis="y", length=0, labelsize=11)
ax.tick_params(axis="x", labelsize=10)
ax.grid(axis="x", linestyle="--", alpha=0.25)
ax.set_axisbelow(True)

for bar, value in zip(bars, df["Average Rating"]):
    ax.text(
        value + 0.08,
        bar.get_y() + bar.get_height() / 2,
        f"{value:.1f}",
        va="center",
        fontsize=11,
        fontweight="bold",
        color="#51418F"
    )

fig.patch.set_facecolor("white")
ax.set_facecolor("white")
plt.tight_layout()

st.pyplot(fig, use_container_width=True)
plt.close(fig)

# =========================================================
# 10. KEY TAKEAWAY
# =========================================================

st.markdown(f"""
<div class="takeaway">
    <h3>What should the audience remember?</h3>
    <p style="font-size:17px; font-weight:700;">
        Focus on improving {lowest_skill['Skill']}.
        It currently has the lowest average self-rating
        at {lowest_skill['Average Rating']:.1f}/5.
    </p>
    <p>
        The highlighted orange bar directs attention to
        the lowest average rating. The title, color, and
        explanation all support the same message.
    </p>
</div>
""", unsafe_allow_html=True)

# =========================================================
# 11. DATA STORYTELLING PRINCIPLE
# =========================================================

st.markdown("""
<div class="section-heading">The Power of a Clear Message</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="principle-card">
    <h3>Make the message impossible to miss.</h3>
    <p>
        A successful data graphic does more than display numbers.
        It guides the audience toward the most important comparison,
        explains why that comparison matters, and leaves them with
        one clear message to remember.
    </p>
    <p style="font-weight:800; color:#FFD29D;">
        Good data visualization = Clear information + Meaningful emphasis.
    </p>
</div>
""", unsafe_allow_html=True)

# =========================================================
# 12. FIVE CHART READING QUESTIONS
# =========================================================

st.markdown("""
<div class="section-heading">How to Read the Chart</div>
<div class="section-description">
    Five questions that help the audience understand the visualization.
</div>
""", unsafe_allow_html=True)

questions = [
    (
        "1. What do the axes represent?",
        "The horizontal axis represents average self-rating from 1 to 5. The vertical axis lists five visualization skills."
    ),
    (
        "2. What does the color represent?",
        "Purple bars represent the other skills, while orange highlights the skill with the lowest rating."
    ),
    (
        "3. What level of detail is provided?",
        "The chart displays average ratings for five skills, without showing individual student responses."
    ),
    (
        "4. Which point should the audience notice?",
        f"The orange bar for {lowest_skill['Skill']} should receive the most attention."
    ),
    (
        "5. What is the key takeaway?",
        f"{lowest_skill['Skill']} is currently the area with the lowest average self-rating and may need more attention."
    )
]

for question, answer in questions:
    with st.expander(question):
        st.write(answer)

# =========================================================
# 13. KNOWLEDGE CHECK
# =========================================================

st.markdown("""
<div class="section-heading">Test Your Understanding</div>
<div class="section-description">
    Check whether you can identify the main message of the data story.
</div>
""", unsafe_allow_html=True)

quiz_answer = st.radio(
    "Which skill should receive more attention in the next workshop?",
    list(ratings.keys()),
    key="lab10_quiz"
)

if st.button("Check My Answer"):
    if quiz_answer == lowest_skill["Skill"]:
        st.success("Correct! You identified the skill with the lowest average rating.")
    else:
        st.warning(
            f"Not quite. The lowest-rated skill is {lowest_skill['Skill']}."
        )

# =========================================================
# 14. FINAL REFLECTION
# =========================================================

st.markdown("""
<div class="section-heading">Think About the Story</div>
""", unsafe_allow_html=True)

reflection = st.text_area(
    "In your own words, what is the most important message from this chart?",
    placeholder="Write your reflection here...",
    height=120
)

if st.button("Submit Reflection"):
    if reflection.strip():
        st.success("Your reflection has been recorded on this page.")
        st.write(reflection)
    else:
        st.warning("Please write your reflection before submitting.")

# =========================================================
# 15. FOOTER
# =========================================================

st.markdown("""
<div class="footer">
    <p><b>FRAME THE DATA. TELL THE STORY.</b></p>
    <p>TFB3133 / TEB3133 · Data Visualization · Lab 10</p>
    <p>Numbers become meaningful when they tell a clear story.</p>
</div>
""", unsafe_allow_html=True)
