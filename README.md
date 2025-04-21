# 🧠 AI Marketing Assistant

A user-friendly, AI-powered tool that helps marketers understand their customer base by clustering reviews into personas — no coding required!

---

## 🚀 Features

- 📂 **Upload CSV File** of customer reviews  
- 🎯 **Choose Number of Clusters (K)** to generate customer personas  
- 💡 **Auto-Generated Personas** with keywords and sample messaging  
- 📸 **Visual Workflow** to explain how the tool works  
- 📤 Export results as JSON for use with other tools like image generators, content creation AIs, or design briefs

---

## 🤖 How It Works

1. **Input**: Upload your CSV file containing customer reviews (a column named `review`).
2. **Processing**:
   - TF-IDF vectorizes the text.
   - K-Means clustering groups similar reviews.
   - Top keywords from each cluster generate a customer persona.
3. **Output**:
   - You get **detailed personas** with top keywords, example ad copy, and a structured description.
   - Use these personas to **create targeted ads**, **guide designers**, or even **feed into AI tools** like Midjourney or GPT for visual/content creation.

---

## 📸 Example Workflow

![Marketing Persona Pipeline](assets/images/flowchart.png)

---

## 🛠️ Installation & Running Locally

```bash
git clone https://github.com/your-username/ai-marketing-assistant.git
cd ai-marketing-assistant
pip install -r requirements.txt
streamlit run app.py