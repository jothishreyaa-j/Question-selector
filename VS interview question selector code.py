import pandas as pd
import random
from fpdf import FPDF
import os

# -----------------------------
# 📂 Load the Dataset
# -----------------------------
file_path = r'C:\Users\jothishreyaa_j\Downloads\P1 - Interview question picker\interview_questions_dataset_2.csv'  # Local file path

# Check if the file exists
if not os.path.exists(file_path):
    raise FileNotFoundError(f"The file '{file_path}' was not found. Please ensure it's in the script directory.")

df = pd.read_csv(file_path)

# -----------------------------
# ⚙️ Parameters
# -----------------------------
marks = int(input("Enter the required weight (marks): "))

# -----------------------------
# 🗂️ Group by Categories
# -----------------------------
easy_questions = df[df['Category'] == 'Easy']
medium_questions = df[df['Category'] == 'Medium']
hard_questions = df[df['Category'] == 'Hard']

# -----------------------------
# 🎯 Select Questions by Marks
# -----------------------------
def select_interview_questions_by_marks(df_easy, df_medium, df_hard, marks):
    selected_questions = []
    total_marks = 0

    def select_category_questions(df_category, category_marks_limit):
        selected_category_q = []
        total_category_marks = 0
        df_category = df_category.sample(frac=1).reset_index(drop=True)  # Shuffle questions

        for idx, question in df_category.iterrows():
            if total_category_marks + question['Weight'] <= category_marks_limit:
                selected_category_q.append(question)
                total_category_marks += question['Weight']

        return selected_category_q

    # Select evenly from each category
    easy_q = select_category_questions(df_easy.copy(), marks // 3)
    medium_q = select_category_questions(df_medium.copy(), marks // 3)
    hard_q = select_category_questions(df_hard.copy(), marks // 3)

    selected_questions = easy_q + medium_q + hard_q
    random.shuffle(selected_questions)

    total_marks = sum([q['Weight'] for q in selected_questions])

    if total_marks < marks:
        remaining_questions = easy_q + medium_q + hard_q
        while total_marks < marks and remaining_questions:
            question = random.choice(remaining_questions)
            selected_questions.append(question)
            total_marks += question['Weight']
            # Remove by the index to avoid ambiguity
            remaining_questions = [q for q in remaining_questions if not q.equals(question)]

    if total_marks > marks:
        selected_questions = selected_questions[:(marks // selected_questions[0]['Weight'])]

    return selected_questions, total_marks

# -----------------------------
# 📊 Run Selection
# -----------------------------
selected_questions, final_marks = select_interview_questions_by_marks(
    easy_questions, medium_questions, hard_questions, marks)

print(f"✅ Selected {len(selected_questions)} questions for the interview.")
print(f"🏋️ Total Marks: {final_marks} marks")

# Check if questions are selected
if not selected_questions:
    print("❌ No questions selected. The constraints may be too strict for the available questions.")
    exit()
else:
    # Convert the list of selected questions to a DataFrame
    selected_df = pd.DataFrame.from_records(selected_questions)

# -----------------------------
# 📄 Generate PDF
# -----------------------------
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Selected Interview Questions", ln=True, align='C')

for index, row in selected_df.iterrows():
    question_text = f"Q{row['ID']}: {row['Text']} - Difficulty: {row['Category']} - Marks: {row['Weight']} - Time: {row['Time (minutes)']} minutes"
    pdf.multi_cell(0, 10, question_text)

# Save PDF locally
pdf_output_path = 'VS_selected_interview_questions1.pdf'
pdf.output(pdf_output_path)
print(f"📁 PDF saved successfully: {pdf_output_path}")

