import datetime
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="CAT 2026 Overloaded Crash Course Tracker",
    page_icon="🎓",
    layout="wide",
)

# ---------------------------------------------------------
# Overloaded Schedule Data (Oct 25 to Nov 29, 2026)
# ---------------------------------------------------------
OVERLOADED_DATA = [
    (
        "QA: Percentages + VARC: RC Foundations",
        "Search: 2IIM Percentages & RC Strategy",
        (
            "Master Percentage fractions (1/2 to 1/20) + Learn RC passage"
            " structure & tone"
        ),
        (
            "https://www.youtube.com/results?search_query=2IIM+CAT+Percentages+and+RC+Strategy"
        ),
    ),
    (
        "QA: Profit & Loss + DILR: Linear Arrangements",
        "Search: 2IIM Profit Loss & Linear Arrangements",
        "CP/SP/MP multipliers + Solve 2 1D row/column arrangement sets",
        (
            "https://www.youtube.com/results?search_query=2IIM+Profit+Loss+and+Linear+Arrangements"
        ),
    ),
    (
        "QA: Ratios & Averages + VARC: Para-Summary",
        "Search: 2IIM Ratios Averages & Para Summary",
        (
            "Ratio scaling, weighted averages + Practice 5 Para-Summary"
            " questions"
        ),
        (
            "https://www.youtube.com/results?search_query=2IIM+Ratios+and+Para+Summary"
        ),
    ),
    (
        "QA: Mixtures & Alligations + DILR: Circular Seating",
        "2IIM Question Bank: Mixtures & Circular DILR",
        "Solve 6 mixture replacement problems + 2 circular seating sets",
        "https://questions.2iim.com/cat-exam/quant/mixtures-alligations/",
    ),
    (
        "QA: Time & Work + VARC: Para-Jumbles (TITA)",
        "Search: 2IIM Time Work & Para Jumbles",
        (
            "LCM efficiency approach for pipes/work + 8 TITA Para-Jumble"
            " practice Qs"
        ),
        (
            "https://www.youtube.com/results?search_query=2IIM+Time+Work+and+Para+Jumbles"
        ),
    ),
    (
        "QA: Time Speed Distance + DILR: Matrix & Grids",
        "Search: 2IIM TSD & Matrix Grid DILR",
        (
            "Proportionality ratio method, relative speed + 2 attribute matrix"
            " sets"
        ),
        (
            "https://www.youtube.com/results?search_query=2IIM+TSD+and+Matrix+Grid+DILR"
        ),
    ),
    (
        "QA: Linear & Quadratics + VARC: Odd Sentence Out",
        "Search: 2IIM Equations & Odd One Out",
        "Roots, discriminant, integral solutions + 8 Odd-One-Out verbal Qs",
        (
            "https://www.youtube.com/results?search_query=2IIM+Quadratic+Equations+and+Odd+One+Out"
        ),
    ),
    (
        "QA: Logarithms & Indices + DILR: 3-Set Venn Diagrams",
        "Search: 2IIM Logarithms & Venn Diagrams",
        "Log rules & domain constraints + Maxima/Minima in 3-set Venn diagrams",
        (
            "https://www.youtube.com/results?search_query=2IIM+Logarithms+and+Venn+Diagrams"
        ),
    ),
    (
        "QA: Sequences (AP/GP) + DILR: Games & Tournaments",
        "Search: 2IIM AP GP & Games Tournaments",
        "nth term, sum formulas + Round-robin & knockout tournament tables",
        (
            "https://www.youtube.com/results?search_query=2IIM+AP+GP+and+Games+Tournaments"
        ),
    ),
    (
        "QA: Geometry (Triangles/Circles) + VARC: Reading",
        "Search: 2IIM Geometry Triangles & Aeon Essays",
        (
            "Triangle similarity, tangent-chord theorem + Read 1 Aeon essay"
            " with summary"
        ),
        "https://aeon.co",
    ),
    (
        "Syllabus Drill (QA + DILR + VARC)",
        "2IIM Question Bank: Mixed Practice",
        "Solve 10 mixed Quant Qs + 1 DILR Set + 2 RCs under timed conditions",
        "https://questions.2iim.com/",
    ),
    (
        "QA Revision + VARC Traps Drill",
        "Search: 2IIM Quant Revision & RC Traps",
        (
            "Formula flash recall + Review extreme option traps in Reading"
            " Comprehension"
        ),
        (
            "https://www.youtube.com/results?search_query=2IIM+CAT+Quant+Revision+RC+Traps"
        ),
    ),
    (
        "DILR Selection Drill + QA Speed Drill",
        "2IIM Question Bank: Speed Drills",
        "Practice ranking 4 DILR sets in 8 mins + 8 Arithmetic Qs in 30 mins",
        "https://questions.2iim.com/cat-exam/quant/",
    ),
    (
        "Error Notebook Clear + Weak Concept Clearing",
        "Personal Error Notebook & 2IIM Videos",
        "Review every past mistake; rewatch weak topic concept walkthroughs",
        (
            "https://www.youtube.com/results?search_query=CAT+Error+Log+Analysis"
        ),
    ),
    (
        "VARC Full Sectional (CAT 2021) + Analysis",
        "CAT 2021 Slot 1 VARC",
        "Strict 40-min test run (2 RCs + 4 VA) + 20-min error diagnostic",
        "https://questions.2iim.com/cat-exam/",
    ),
    (
        "DILR Full Sectional (CAT 2021) + Analysis",
        "CAT 2021 Slot 1 DILR",
        "Strict 40-min test run (Solve easiest 1-2 sets) + 20-min analysis",
        "https://questions.2iim.com/cat-exam/",
    ),
    (
        "QA Full Sectional (CAT 2021) + Analysis",
        "CAT 2021 Slot 1 QA",
        (
            "Strict 40-min test run (Target 8-10 Arithmetic/Algebra Qs) +"
            " 20-min analysis"
        ),
        "https://questions.2iim.com/cat-exam/",
    ),
    (
        "Triple Sectional Review + Error Notebook",
        "2IIM Past Papers Analysis",
        "Consolidate CAT 2021 mistakes; record root causes in error book",
        "https://questions.2iim.com/cat-exam/",
    ),
    (
        "VARC Sectional (CAT 2022 Slot 1) + Analysis",
        "CAT 2022 Slot 1 VARC",
        "40-min timed test + 20-min analysis & option elimination review",
        "https://questions.2iim.com/cat-exam/",
    ),
    (
        "DILR Sectional (CAT 2022 Slot 1) + Analysis",
        "CAT 2022 Slot 1 DILR",
        "40-min timed test + 20-min analysis & setup mapping review",
        "https://questions.2iim.com/cat-exam/",
    ),
    (
        "QA Sectional (CAT 2022 Slot 1) + Analysis",
        "CAT 2022 Slot 1 QA",
        "40-min timed test + 20-min analysis & formula gap fix",
        "https://questions.2iim.com/cat-exam/",
    ),
    (
        "DILR Puzzle Deconstruction",
        "CAT Past Papers DILR Sets",
        "Untimed step-by-step solving of 2 hard matrix & tournament sets",
        "https://questions.2iim.com/cat-exam/",
    ),
    (
        "VARC Sectional (CAT 2023 Slot 1) + Analysis",
        "CAT 2023 Slot 1 VARC",
        "40-min timed test + 20-min passage breakdown analysis",
        "https://questions.2iim.com/cat-exam/",
    ),
    (
        "DILR Sectional (CAT 2023 Slot 1) + Analysis",
        "CAT 2023 Slot 1 DILR",
        "40-min timed test + 20-min set selection analysis",
        "https://questions.2iim.com/cat-exam/",
    ),
    (
        "QA Sectional (CAT 2023 Slot 1) + Analysis",
        "CAT 2023 Slot 1 QA",
        "40-min timed test + 20-min speed & calculation check",
        "https://questions.2iim.com/cat-exam/",
    ),
    (
        "CAT Question Selection Strategy",
        "2IIM CAT Question Selection Strategy",
        "Learn to identify and skip trap questions within the first 30 seconds",
        (
            "https://www.youtube.com/results?search_query=2IIM+CAT+Question+Selection+Strategy"
        ),
    ),
    (
        "Full Mock Part 1: VARC & DILR",
        "Free Mock (Cracku / Hitbullseye)",
        "Attempt VARC (40 min) + DILR (40 min) under exam conditions",
        "https://cracku.in/cat-mock-test",
    ),
    (
        "Full Mock Part 2: QA + Full Diagnostic",
        "Free Mock (Cracku / Hitbullseye)",
        (
            "Attempt QA (40 min) + 40-min comprehensive score & accuracy"
            " review"
        ),
        "https://cracku.in/cat-mock-test",
    ),
    (
        "CAT 2024 Past Paper (VARC & DILR)",
        "CAT 2024 Past Paper Slot 1",
        "Solve 2 RCs + 1 DILR set untimed for 100% conceptual clarity",
        "https://questions.2iim.com/cat-exam/",
    ),
    (
        "CAT 2024 Past Paper (QA)",
        "CAT 2024 Past Paper Slot 1",
        "Solve all Arithmetic & Algebra questions untimed with accuracy",
        "https://questions.2iim.com/cat-exam/",
    ),
    (
        "Formula Flash Recall",
        "Handwritten Quant Formula Sheet",
        "Write out all Arithmetic, Algebra & Geometry formulas from memory",
        (
            "https://www.youtube.com/results?search_query=CAT+Quant+Formula+Revision"
        ),
    ),
    (
        "Final Timed Sectional: VARC & DILR",
        "Timed Sectional Practice",
        "Strict 40 mins VARC + Strict 40 mins DILR; test final execution",
        "https://questions.2iim.com/cat-exam/",
    ),
    (
        "Final Timed Sectional: QA & Log Clear",
        "Timed Sectional Practice",
        "Strict 40 mins QA + Final review of all logged calculation errors",
        "https://questions.2iim.com/cat-exam/",
    ),
    (
        "Light Revision & Logistics",
        "Admit Card & Formula Sheet",
        "30 mins light formula reading + Print admit card & verify travel route",
        "https://iimcat.ac.in",
    ),
    (
        "COMPLETE REST & MENTAL RESET",
        "Relaxation & Sleep",
        "Zero studying! Rest well, hydrate, and prepare exam kit for tomorrow",
        "https://www.youtube.com/results?search_query=CAT+Exam+Day+Tips",
    ),
    (
        "CAT EXAM DAY 🎓",
        "Exam Center Execution",
        "Execute your 40-minute sectional strategy with calm confidence!",
        "https://iimcat.ac.in",
    ),
]

st.title("🔥 CAT 2026 Overloaded 36-Day Crash Tracker")
st.markdown(
    "Target Date: **Sunday, November 29, 2026** | Daily double-module crash"
    " plan."
)

start_date = st.sidebar.date_input(
    "Start Date (Day 1)", value=datetime.date(2026, 10, 25)
)

if "completed_tasks" not in st.session_state:
  st.session_state["completed_tasks"] = set()

processed_data = []
for i, item in enumerate(OVERLOADED_DATA):
  day_num = i + 1
  task_date = start_date + datetime.timedelta(days=i)
  date_str = task_date.strftime("%b %d (%a)")

  processed_data.append({
      "Day": f"Day {day_num}",
      "Date": date_str,
      "Daily Overloaded Focus": item[0],
      "Resource": item[1],
      "Action Item": item[2],
      "Link": item[3],
      "Task_ID": f"task_{day_num}",
  })

df = pd.DataFrame(processed_data)

# Metrics
total_tasks = len(df)
completed_count = len(st.session_state["completed_tasks"])
progress_pct = completed_count / total_tasks

col1, col2, col3 = st.columns(3)
col1.metric("Total Days", total_tasks)
col2.metric("Completed", completed_count)
col3.metric("Remaining", total_tasks - completed_count)

st.progress(progress_pct)
st.caption(f"Overall Completion: {progress_pct * 100:.1f}%")

st.divider()

# Schedule Table Display
for idx, row in df.iterrows():
  task_id = row["Task_ID"]
  is_checked = task_id in st.session_state["completed_tasks"]

  col_check, col_day, col_topic, col_action, col_link = st.columns(
      [0.6, 1.2, 2.5, 3.5, 1.5]
  )

  with col_check:
    checked = st.checkbox(
        "", value=is_checked, key=f"chk_{task_id}", label_visibility="collapsed"
    )
    if checked:
      st.session_state["completed_tasks"].add(task_id)
    else:
      st.session_state["completed_tasks"].discard(task_id)

  with col_day:
    st.write(f"**{row['Day']}**\n\n`{row['Date']}`")

  with col_topic:
    st.write(f"**{row['Daily Overloaded Focus']}**")
    st.caption(row["Resource"])

  with col_action:
    st.write(row["Action Item"])

  with col_link:
    if row["Link"]:
      st.markdown(f"[🔗 Open Resource]({row['Link']})")

  st.divider()
