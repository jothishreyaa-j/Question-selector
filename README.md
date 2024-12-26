# Question-selector
A Python project that randomly selects questions from a generated dataset as per given constraints using uniform distribution. Useful for interviews and recruitment processes, allowing for a diverse pool of questions to be randomly picked for candidate assessments.

Project Overview: 

Interview Question Selector
This project is designed to automate the selection of interview questions based on predefined categories and a specified total weight (marks). It helps recruiters or hiring managers generate customized interview question sets, which can be evenly distributed across categories such as Easy, Medium, and Hard, while adhering to specific mark constraints. The selected questions are then downloaded as a PDF file to your system.

Logic Behind the Code

Dataset Loading:

The project begins by loading a CSV file containing interview questions. The dataset includes columns like:
ID: Unique identifier for each question.
Text: The actual interview question.
Category: The difficulty level of the question (Easy, Medium, or Hard).
Weight: The mark assigned to the question.
Time (minutes): Estimated time required to answer the question.
Parameters Input:

The user is prompted to input the required total weight (marks) for the interview session. This value will dictate how many questions are selected and from which categories.
Category Filtering:

The dataset is divided into three categories: Easy, Medium, and Hard. These categories are used to ensure a balanced selection of questions across different difficulty levels.

Question Selection:

Even Distribution: The algorithm attempts to distribute the total weight evenly across the three categories, selecting questions randomly from each category. This ensures that the selection is not biased towards any particular difficulty.
Marks Constraints: The selection process continues until the total weight of selected questions meets the minimum and maximum weight criteria set by the user.
If the selected questions' total marks are below the required minimum, additional questions are randomly chosen from the remaining pool of questions.
If the total exceeds the maximum weight, the algorithm truncates the selection.
PDF Generation:

After selecting the interview questions, the script generates a PDF document containing the selected questions and their associated details, such as the question ID, text, category, marks, and time.
The PDF serves as a printable format for the interview, making it easy to share or print for in-person use.

Error Handling:

The script includes error handling to ensure that the dataset file exists and that all selected questions meet the weight constraints.
Use Cases
Automated Interview Preparation:

Recruiters and HR personnel can use this script to generate tailored interview question sets based on the total marks or weight they wish to assign to each interview session.
Fair and Balanced Question Distribution:

The script ensures that questions are evenly distributed across various difficulty levels (Easy, Medium, Hard), helping create balanced interview sets that test candidates on a range of skills.

Customizable Interview Templates:

The ability to set a total weight (marks) allows for flexible interview configurations, ensuring that different roles or job requirements can have varied sets of questions.
Efficient Resource Management:

Automating the question selection process saves time for hiring teams, reducing the effort required to manually create and format interview questions.

Applications in Industry:
This tool can be applied in any industry that conducts technical interviews, including:

Tech Companies: For software development or engineering interviews, ensuring questions cover various difficulty levels.
Consulting Firms: For assessing candidates across different problem-solving and technical skills.
Educational Institutions: To create fair and objective assessments or mock interviews for students.

How to Use:
Clone the repository to your local machine.
Ensure you have Python installed along with the required libraries (pandas, random, fpdf).
Place your interview questions dataset (CSV format) in the same directory or modify the file path in the script.
Run the Python script and input the required total marks when prompted.
The selected interview questions will be saved in a PDF file, which can be printed or shared.

Dependencies:
Python 3.x
Pandas: For reading and manipulating CSV files.
fpdf: For generating PDF files from the selected questions.
This project simplifies the process of preparing customized interview question sets, ensuring a structured and objective interview process.
