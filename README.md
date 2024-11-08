# StringMatchCalc: Simplified String Matching & Calculation Tool 🔍  

## 📝 Project Description  
**StringMatchCalc** is a user-friendly Python tool designed to solve common string matching problems efficiently. It compares a main string with a secondary string (and its reverse), finds matching substrings, and performs calculations based on user-provided weights.

## 🚀 Key Features  
- **Quick String Matching**: Instantly matches substrings from the main string with the target string and its reverse.  
- **Customizable Calculations**: Apply user-defined multipliers to compute a final result.  
- **Simple Input & Output**: Minimal input needed; clear and concise output for easy understanding.  

## 🔧 How It Works  
1. **Input Strings**:  
   - Main string (`x`).  
   - Comparison string (`y`).  
   - A list of weights (space-separated numbers).  

2. **Reverse Match**:  
   - Automatically generates the reverse of `y`.  

3. **Matching Logic**:  
   - Finds and counts matching substrings in both `y` and `revY`.  

4. **Final Calculation**:  
   - Uses the counts and weights to calculate a final score.  

## 📂 Project Structure  
  /StringMatchCalc
      ├── string_match_calc.py # Python script 
      ├── README.md # Documentation
      
## 📋 Example Usage  
$ python string_match_calc.py
Enter the main string: abcdxyz
Enter the string to compare: xyz
Enter numbers separated by space: 10 20

Reverse of y: zyx
Selected substrings: ['xyz']
Substrings from substringsY: 1
Substrings from substringsRev: 0
The final answer: 10


💻 Installation & Setup
1. Clone the repository:
   git clone https://github.com/harish2326/StringMatchCalc.git
2. Navigate to the project directory:
   cd StringMatchCalc
3. Run The Script 
    python string_match_calc.py

🛠️ Technologies Used
Python 3

----------------------------------------------------------------------------------------
📬 Contact
SV Harish
Github:
https://github.com/harish2326
instagram :
https://www.instagram.com/iam___sv/profilecard/?igsh=MzM3N3premJrOGd6




