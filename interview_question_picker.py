!pip install pandas

!pip install fpdf

import pandas as pd
import random
from fpdf import FPDF

# Load the dataset
file_path = '/content/interview_questions_dataset_2.csv'  # Path in Colab, modify if needed
df = pd.read_csv(file_path)

# Parameters
marks_min = int(input("Enter the required minimum weight (marks): "))
marks_max = int(input("Enter the required maximum weight (marks): "))

# Group by categories
easy_questions = df[df['Category'] == 'Easy']
medium_questions = df[df['Category'] == 'Medium']
hard_questions = df[df['Category'] == 'Hard']

# Function to select questions based purely on marks and distribute evenly across categories
def select_interview_questions_by_marks(df_easy, df_medium, df_hard, marks_min, marks_max):
    selected_questions = []
    total_marks = 0

    # Function to select questions from a given category within marks constraints
    def select_category_questions(df_category, category_marks_limit):
        selected_category_q = []
        total_category_marks = 0

        # Randomly shuffle and select questions from the category until the limit is reached
        df_category = df_category.sample(frac=1).reset_index(drop=True)  # Shuffle questions in the category

        for idx, question in df_category.iterrows():
            if total_category_marks + question['Weight'] <= category_marks_limit:
                selected_category_q.append(question)
                total_category_marks += question['Weight']

        return selected_category_q

    # Try selecting questions for each category to meet the marks requirement
    easy_q = select_category_questions(df_easy.copy(), marks_max // 3)  # Marks distributed evenly
    medium_q = select_category_questions(df_medium.copy(), marks_max // 3)
    hard_q = select_category_questions(df_hard.copy(), marks_max // 3)

    # Combine all selected questions
    selected_questions = easy_q + medium_q + hard_q

    # Shuffle to avoid any order bias
    random.shuffle(selected_questions)

    # Final check if marks constraints are met
    total_marks = sum([q['Weight'] for q in selected_questions])

    # If final marks constraints are not met, select additional questions from any category
    if total_marks < marks_min:
        remaining_questions = easy_q + medium_q + hard_q  # Remaining pool of questions
        # Check if we still have questions left to pick
        while total_marks < marks_min and remaining_questions:
            # Randomly select from the remaining questions
            question = random.choice(remaining_questions)
            selected_questions.append(question)
            total_marks += question['Weight']
            remaining_questions.remove(question)

    # If total_marks exceed the max limit, truncate the selected questions list
    if total_marks > marks_max:
        selected_questions = selected_questions[:(marks_max // selected_questions[0]['Weight'])]

    return selected_questions, total_marks

# Run the selection based on marks
selected_questions, final_marks = select_interview_questions_by_marks(
    easy_questions, medium_questions, hard_questions, marks_min, marks_max)

# Display results
print(f"✅ Selected {len(selected_questions)} questions for the interview.")
print(f"🏋️ Total Marks: {final_marks} marks")

# Check if questions are selected, otherwise indicate that no valid selection was made
if not selected_questions:
    print("❌ No questions selected. The constraints may be too strict for the available questions.")
else:
    # Convert the selected questions back to DataFrame and save
    selected_df = pd.DataFrame(selected_questions)

   # Convert the DataFrame to PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", size=12)

# Add a title
pdf.cell(200, 10, txt="Selected Interview Questions", ln=True, align='C')

# Add questions to PDF with difficulty level
for index, row in selected_df.iterrows():
    question_text = f"Q{row['ID']}: {row['Text']} - Difficulty: {row['Category']} - Marks: {row['Weight']} - Time: {row['Time (minutes)']} minutes"
    pdf.multi_cell(0, 10, question_text)

# Save the PDF to a file
pdf_output_path = "/content/selected_interview_questions.pdf"
pdf.output(pdf_output_path)

# Allow download of the selected questions in Colab
from google.colab import files
files.download(pdf_output_path)
