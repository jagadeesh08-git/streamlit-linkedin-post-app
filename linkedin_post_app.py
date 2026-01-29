import streamlit as st
import random
import requests
from io import BytesIO

# Human-like post generator
def generate_post(topic):
    return f"""
Today I was thinking about **{topic}**.

Technology and learning are changing very fast, and we must keep updating our skills.  
As a student, I realized that small daily learning can create big opportunities in the future.

What are your thoughts on {topic}?
"""

# Hashtag generator
def generate_hashtags(topic):
    words = topic.split()
    hashtags = ["#" + w.capitalize() for w in words]
    hashtags += ["#LinkedIn", "#Career", "#Learning", "#Tech", "#Growth"]
    return " ".join(hashtags)

# Sample images
images = [
    "https://images.unsplash.com/photo-1519389950473-47ba0277781c",
    "https://images.unsplash.com/photo-1527430253228-e93688616381",
    "https://images.unsplash.com/photo-1504384308090-c894fdcc538d"
]

# UI
st.title("🚀 LinkedIn Humanized Post Generator")

topic = st.text_input("Enter topic:")

if st.button("Generate Post"):
    post = generate_post(topic)
    hashtags = generate_hashtags(topic)

    st.subheader("📝 LinkedIn Post")
    st.markdown(post)

    st.subheader("🏷️ Hashtags")
    st.write(hashtags)

    # Pick random image
    img_url = random.choice(images)
    st.subheader("🖼️ Generated LinkedIn Post Image")
    st.image(img_url, caption="LinkedIn Banner Image")

    # Download image
    response = requests.get(img_url)
    image_bytes = BytesIO(response.content)

    st.download_button(
        label="⬇️ Download Image Post",
        data=image_bytes,
        file_name="linkedin_post_image.jpg",
        mime="image/jpeg"
    )

