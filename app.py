import streamlit as st
import random
import html

# ============================================================
# SkillDNA AI
# Class 11 AI Capstone Project
# ============================================================

st.set_page_config(
    page_title="SkillDNA AI",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# SESSION STATE
# ============================================================

DEFAULT_STATE = {
    "page": "Home",
    "student_name": "",
    "level": "",
    "questions": [],
    "answers": {},
    "current_question": 0,
    "completed": False
}

for key, value in DEFAULT_STATE.items():
    if key not in st.session_state:
        st.session_state[key] = value


def reset_app():
    for key, value in DEFAULT_STATE.items():
        st.session_state[key] = value


# ============================================================
# SKILLS
# ============================================================

SKILLS = [
    "Logic",
    "Creativity",
    "Scientific Thinking",
    "Data Analysis",
    "Problem Solving",
    "Communication",
    "Leadership",
    "Research",
    "Empathy",
    "Planning",
    "Critical Thinking",
    "Systems Thinking",
    "Decision Making"
]

SKILL_DESCRIPTIONS = {
    "Logic": "You naturally look for patterns, rules and relationships to reach a clear conclusion.",
    "Creativity": "You are comfortable generating original ideas and approaching situations from unusual angles.",
    "Scientific Thinking": "You tend to observe carefully, form explanations and test ideas using evidence.",
    "Data Analysis": "You are comfortable finding meaning in numbers, information, trends and comparisons.",
    "Problem Solving": "You tend to break difficult situations into smaller parts and search for workable solutions.",
    "Communication": "You tend to express ideas clearly and adapt your explanation to the people around you.",
    "Leadership": "You are comfortable taking initiative, coordinating people and helping a group move forward.",
    "Research": "You enjoy investigating questions, checking sources and finding information before reaching conclusions.",
    "Empathy": "You tend to notice how other people may feel and consider their perspective while responding.",
    "Planning": "You naturally organise tasks, priorities and resources before starting important work.",
    "Critical Thinking": "You tend to question assumptions and examine whether evidence actually supports a conclusion.",
    "Systems Thinking": "You tend to notice how different parts of a larger system affect one another.",
    "Decision Making": "You tend to compare options, trade-offs, risks and evidence before choosing a practical direction."
}

GROWTH = {
    "Logic": "Try puzzles, strategy games and everyday situations where you have to explain why your answer makes sense.",
    "Creativity": "Keep an idea journal and practise creating several different solutions before choosing one.",
    "Scientific Thinking": "Practise forming hypotheses and testing them with simple observations or experiments.",
    "Data Analysis": "Work with real datasets, charts or surveys and practise explaining what the numbers actually show.",
    "Problem Solving": "When stuck, define the problem first, list possible causes and test solutions one at a time.",
    "Communication": "Practise explaining the same idea in a short, simple version and then a detailed version.",
    "Leadership": "Take responsibility for small group tasks and learn to delegate instead of doing everything yourself.",
    "Research": "Compare multiple reliable sources and keep short notes about where each important fact came from.",
    "Empathy": "Listen without immediately giving advice and try to understand the other person's point of view.",
    "Planning": "Break large goals into smaller deadlines and review your plan when circumstances change.",
    "Critical Thinking": "Before accepting a claim, ask what evidence supports it and what evidence could prove it wrong.",
    "Systems Thinking": "Draw simple cause-and-effect maps to understand how changes in one part can affect the whole system.",
    "Decision Making": "When choosing between options, write down the evidence, benefits, risks and trade-offs before deciding."
}


# ============================================================
# CAREERS
# ============================================================

CAREERS = {
    "Logic": [
        ("Mathematician", "Uses mathematical reasoning to solve theoretical and real-world problems."),
        ("Economist", "Studies how people, organisations and governments make decisions using models and evidence."),
        ("Cybersecurity Analyst", "Uses logical thinking to identify vulnerabilities and protect digital systems.")
    ],

    "Creativity": [
        ("Architect", "Combines creativity, design and practical constraints to create useful spaces."),
        ("Product Designer", "Designs products and experiences around real user needs."),
        ("Advertising Creative", "Turns ideas and observations into campaigns, concepts and visual stories.")
    ],

    "Scientific Thinking": [
        ("Research Scientist", "Investigates questions through experiments, observations and evidence."),
        ("Environmental Scientist", "Studies environmental problems and develops evidence-based solutions."),
        ("Biotechnologist", "Uses biological science to develop applications in health, agriculture and industry.")
    ],

    "Data Analysis": [
        ("Data Analyst", "Turns datasets into patterns, insights and useful decisions."),
        ("Economist", "Uses statistics and models to understand economic behaviour and trends."),
        ("Market Research Analyst", "Studies consumers, markets and survey data to support business decisions.")
    ],

    "Problem Solving": [
        ("Civil Engineer", "Solves practical design and infrastructure problems using science and mathematics."),
        ("Operations Analyst", "Finds ways to make systems, organisations and processes more efficient."),
        ("Emergency Management Specialist", "Plans responses to complex situations and coordinates practical solutions.")
    ],

    "Communication": [
        ("Journalist", "Researches information and communicates important stories clearly to an audience."),
        ("Lawyer", "Builds arguments, interprets information and communicates complex ideas persuasively."),
        ("Public Relations Specialist", "Helps organisations communicate effectively with different audiences.")
    ],

    "Leadership": [
        ("Civil Services Officer", "Coordinates public programmes, resources and people to solve administrative problems."),
        ("Project Manager", "Guides a team through planning, execution, deadlines and problem solving."),
        ("Social Impact Manager", "Leads initiatives designed to create measurable benefits for communities.")
    ],

    "Research": [
        ("Policy Researcher", "Investigates social and public issues and uses evidence to inform policy."),
        ("Historian", "Studies primary and secondary sources to understand events and societies."),
        ("Scientific Researcher", "Builds knowledge through structured investigation and evidence.")
    ],

    "Empathy": [
        ("Psychologist", "Studies behaviour and supports people using evidence-based psychological approaches."),
        ("Social Worker", "Helps individuals and communities navigate social and practical challenges."),
        ("Human Resources Specialist", "Works with people, workplace concerns and organisational development.")
    ],

    "Planning": [
        ("Urban Planner", "Plans how cities and communities can develop efficiently and sustainably."),
        ("Project Manager", "Organises people, timelines and resources to complete complex projects."),
        ("Event Planner", "Coordinates multiple moving parts to deliver successful events and experiences.")
    ],

    "Critical Thinking": [
        ("Investigative Journalist", "Examines claims, evidence and sources to uncover reliable information."),
        ("Policy Analyst", "Evaluates evidence and possible consequences before recommending public policies."),
        ("Lawyer", "Analyses evidence, rules and competing arguments to build strong cases.")
    ],

    "Systems Thinking": [
        ("Systems Engineer", "Studies how interconnected technical components work together as a complete system."),
        ("Urban Planner", "Considers transportation, housing, environment and communities as connected systems."),
        ("Environmental Policy Analyst", "Studies how environmental, economic and social decisions influence one another.")
    ],

    "Decision Making": [
        ("Public Administration Officer", "Makes practical decisions while balancing rules, resources, evidence and public needs."),
        ("Operations Research Analyst", "Uses evidence, models and constraints to compare possible decisions."),
        ("Management Consultant", "Analyses complex organisational problems and recommends practical courses of action.")
    ]
}


# ============================================================
# PROJECTS
# ============================================================

PROJECTS = [
    {
        "name": "School Energy Audit",
        "category": "🌱 Environment",
        "description": "Measure electricity use in different school areas and identify realistic ways to reduce energy consumption.",
        "skills": ["Data Analysis", "Scientific Thinking", "Planning"],
        "link": "https://www.unep.org/"
    },
    {
        "name": "Water Conservation Survey",
        "category": "💧 Sustainability",
        "description": "Survey water-use habits in your school or neighbourhood and turn the findings into a conservation plan.",
        "skills": ["Research", "Data Analysis", "Communication"],
        "link": "https://www.unwater.org/"
    },
    {
        "name": "Student Mental-Wellbeing Awareness Campaign",
        "category": "🧠 Psychology",
        "description": "Design an evidence-based awareness campaign about healthy study habits, stress management and seeking support.",
        "skills": ["Empathy", "Communication", "Research"],
        "link": "https://www.apa.org/"
    },
    {
        "name": "Local Air Quality Investigation",
        "category": "🌍 Environment",
        "description": "Collect publicly available air-quality data, identify trends and explain possible factors affecting pollution.",
        "skills": ["Data Analysis", "Scientific Thinking", "Critical Thinking"],
        "link": "https://www.who.int/"
    },
    {
        "name": "SDG Community Project",
        "category": "🌎 Social Impact",
        "description": "Choose one Sustainable Development Goal and design a small project that could create measurable local impact.",
        "skills": ["Planning", "Leadership", "Research"],
        "link": "https://sdgs.un.org/goals"
    },
    {
        "name": "School Waste Management Plan",
        "category": "♻️ Environment",
        "description": "Study the types of waste generated at school and propose a practical segregation and reduction system.",
        "skills": ["Systems Thinking", "Problem Solving", "Planning"],
        "link": "https://www.unep.org/"
    },
    {
        "name": "Mini Data Journalism Report",
        "category": "📰 Media",
        "description": "Collect data about a local issue, analyse it and present the findings as a short evidence-based story.",
        "skills": ["Research", "Data Analysis", "Communication"],
        "link": "https://data.un.org/"
    },
    {
        "name": "Accessible School Map",
        "category": "🏫 Community",
        "description": "Map important school facilities and identify barriers faced by students with different accessibility needs.",
        "skills": ["Empathy", "Systems Thinking", "Creativity"],
        "link": "https://www.un.org/development/desa/disabilities/"
    },
    {
        "name": "Public Policy Proposal",
        "category": "🏛️ Government",
        "description": "Choose a local public issue, research existing approaches and create a practical policy proposal.",
        "skills": ["Critical Thinking", "Decision Making", "Research"],
        "link": "https://www.mygov.in/"
    },
    {
        "name": "Community Nutrition Awareness",
        "category": "🥗 Health",
        "description": "Research basic nutrition information and design a simple awareness resource for students or families.",
        "skills": ["Research", "Communication", "Empathy"],
        "link": "https://www.who.int/"
    },
    {
        "name": "School Transport Optimisation",
        "category": "🚍 Planning",
        "description": "Analyse routes, timings or transport patterns and propose ways to make school travel more efficient.",
        "skills": ["Logic", "Data Analysis", "Systems Thinking"],
        "link": "https://www.unece.org/"
    },
    {
        "name": "Heritage Documentation Project",
        "category": "🏛️ Culture",
        "description": "Document a local historical place, tradition or story using interviews, research and visual material.",
        "skills": ["Research", "Communication", "Creativity"],
        "link": "https://www.unesco.org/"
    },
    {
        "name": "Smart Study Planner",
        "category": "📚 Education",
        "description": "Design a study-planning system that uses priorities, deadlines and available time rather than simply counting hours.",
        "skills": ["Planning", "Logic", "Problem Solving"],
        "link": "https://www.education.gov.in/"
    },
    {
        "name": "Disaster Preparedness Guide",
        "category": "🚨 Safety",
        "description": "Research common local hazards and create a clear preparedness and response guide for your community.",
        "skills": ["Planning", "Systems Thinking", "Communication"],
        "link": "https://www.undrr.org/"
    }
]


# ============================================================
# QUESTIONS
# ============================================================

QUESTION_BANK = {

    "Class 5–7": [
        {
            "q": "Your group has to build a bridge using only paper and tape. What would you naturally do first?",
            "options": [
                ("Sketch a few different bridge ideas", "Creativity"),
                ("Think about how to make the structure strong", "Logic"),
                ("Ask everyone what they think the bridge should look like", "Communication"),
                ("Divide the work between group members", "Leadership")
            ]
        },
        {
            "q": "You notice that the school garden plants are growing differently. What interests you most?",
            "options": [
                ("Finding out what caused the difference", "Scientific Thinking"),
                ("Comparing the growth using numbers", "Data Analysis"),
                ("Thinking of a better way to care for them", "Problem Solving"),
                ("Drawing a plan for the garden", "Creativity")
            ]
        },
        {
            "q": "A friend is upset but doesn't explain why. What would you most likely do?",
            "options": [
                ("Listen and try to understand their feelings", "Empathy"),
                ("Ask questions to understand what happened", "Research"),
                ("Help them think about possible solutions", "Problem Solving"),
                ("Explain what you think they should do", "Communication")
            ]
        },
        {
            "q": "Your class is organising a small event. Which task sounds most interesting?",
            "options": [
                ("Making a timetable", "Planning"),
                ("Leading the team", "Leadership"),
                ("Designing decorations", "Creativity"),
                ("Talking to people and announcing things", "Communication")
            ]
        },
        {
            "q": "You hear a surprising fact online. What do you do?",
            "options": [
                ("Check whether reliable sources support it", "Critical Thinking"),
                ("Search for more information", "Research"),
                ("Look for numbers or evidence", "Data Analysis"),
                ("Think about whether the claim logically makes sense", "Logic")
            ]
        },
        {
            "q": "A game gives you a problem with several possible solutions. What do you enjoy most?",
            "options": [
                ("Finding the most efficient solution", "Logic"),
                ("Trying an unusual solution", "Creativity"),
                ("Testing different solutions", "Scientific Thinking"),
                ("Comparing the advantages and disadvantages", "Decision Making")
            ]
        },
        {
            "q": "Your class wants to reduce litter. What would you prefer to do?",
            "options": [
                ("Find out where most litter comes from", "Research"),
                ("Create a practical system for reducing it", "Systems Thinking"),
                ("Make posters that influence students", "Communication"),
                ("Organise students to run the project", "Leadership")
            ]
        },
        {
            "q": "You have several homework tasks due on the same day. What is your first instinct?",
            "options": [
                ("Arrange them by priority and time needed", "Planning"),
                ("Start with the hardest one", "Problem Solving"),
                ("Choose based on which decision gives the best result", "Decision Making"),
                ("Make a checklist", "Logic")
            ]
        },
        {
            "q": "Your team disagrees about how to complete a project.",
            "options": [
                ("Compare the strengths of each idea", "Critical Thinking"),
                ("Help everyone explain their viewpoint", "Communication"),
                ("Look for a solution that combines useful parts", "Problem Solving"),
                ("Think about how the decision affects the whole project", "Systems Thinking")
            ]
        },
        {
            "q": "You are given a blank notebook and asked to create something useful.",
            "options": [
                ("Invent something completely new", "Creativity"),
                ("Create an organised planner", "Planning"),
                ("Make a collection of facts and observations", "Research"),
                ("Design a system for solving a common problem", "Problem Solving")
            ]
        },
        {
            "q": "Your group has limited time and materials. What matters most?",
            "options": [
                ("Choosing the best use of the available resources", "Decision Making"),
                ("Making a clear plan before starting", "Planning"),
                ("Finding a clever alternative", "Creativity"),
                ("Understanding how all parts need to work together", "Systems Thinking")
            ]
        },
        {
            "q": "You are asked to explain something difficult to a younger student.",
            "options": [
                ("Use a simple example", "Communication"),
                ("Draw a diagram", "Creativity"),
                ("Break it into logical steps", "Logic"),
                ("First understand exactly what they are struggling with", "Empathy")
            ]
        }
    ],

    "Class 8–10": [
        {
            "q": "Your school wants to reduce electricity use. What would you start with?",
            "options": [
                ("Collect electricity-use data and compare areas", "Data Analysis"),
                ("Investigate what causes unnecessary consumption", "Research"),
                ("Design a practical reduction plan", "Planning"),
                ("Consider how changing one part may affect the whole school", "Systems Thinking")
            ]
        },
        {
            "q": "A viral post makes a strong claim without giving evidence. What would you do?",
            "options": [
                ("Check reliable sources", "Research"),
                ("Look for weaknesses in the argument", "Critical Thinking"),
                ("Check whether the numbers support the claim", "Data Analysis"),
                ("Ask what conclusion logically follows from the evidence", "Logic")
            ]
        },
        {
            "q": "Your team has three possible project ideas but enough time for only one.",
            "options": [
                ("Compare benefits, risks and feasibility", "Decision Making"),
                ("Choose the most creative idea", "Creativity"),
                ("Create criteria and score each idea", "Data Analysis"),
                ("Ask team members for their priorities", "Communication")
            ]
        },
        {
            "q": "You are investigating why students are often late to school.",
            "options": [
                ("Collect information about different causes", "Research"),
                ("Look for patterns in arrival times", "Data Analysis"),
                ("Map all the factors affecting arrival", "Systems Thinking"),
                ("Suggest and test possible solutions", "Problem Solving")
            ]
        },
        {
            "q": "A group project is falling behind schedule.",
            "options": [
                ("Reorganise the tasks and deadlines", "Planning"),
                ("Take initiative and coordinate everyone", "Leadership"),
                ("Find the biggest bottleneck and fix it", "Problem Solving"),
                ("Decide which tasks are actually essential", "Decision Making")
            ]
        },
        {
            "q": "You need to present a complex topic to your class.",
            "options": [
                ("Create a memorable analogy or visual", "Creativity"),
                ("Structure the explanation logically", "Communication"),
                ("Support key points with evidence", "Research"),
                ("Anticipate questions and challenge your own argument", "Critical Thinking")
            ]
        },
        {
            "q": "Two friends have completely different opinions during a discussion.",
            "options": [
                ("Try to understand why each person thinks that way", "Empathy"),
                ("Identify the evidence behind both positions", "Critical Thinking"),
                ("Help them communicate their points clearly", "Communication"),
                ("Find a practical compromise", "Problem Solving")
            ]
        },
        {
            "q": "You are given an experiment that produces unexpected results.",
            "options": [
                ("Check the method for possible errors", "Scientific Thinking"),
                ("Look for patterns in the observations", "Data Analysis"),
                ("Develop another explanation", "Creativity"),
                ("Investigate similar experiments", "Research")
            ]
        },
        {
            "q": "A city wants to improve public transport.",
            "options": [
                ("Study passenger data and traffic patterns", "Data Analysis"),
                ("Examine how roads, people and buses interact", "Systems Thinking"),
                ("Develop a practical implementation plan", "Planning"),
                ("Compare several possible solutions", "Decision Making")
            ]
        },
        {
            "q": "You have to solve a difficult maths or science problem.",
            "options": [
                ("Break it into smaller steps", "Problem Solving"),
                ("Look for an underlying pattern", "Logic"),
                ("Question whether your assumptions are valid", "Critical Thinking"),
                ("Try a different approach if the first fails", "Creativity")
            ]
        },
        {
            "q": "Your class wants to start a community project.",
            "options": [
                ("Coordinate people and responsibilities", "Leadership"),
                ("Research the actual community need first", "Research"),
                ("Plan the project timeline", "Planning"),
                ("Think about how the project could affect different groups", "Empathy")
            ]
        },
        {
            "q": "You are choosing between two opportunities that both look good.",
            "options": [
                ("List the long-term advantages and disadvantages", "Decision Making"),
                ("Think about which option fits your goals", "Critical Thinking"),
                ("Ask people with relevant experience", "Communication"),
                ("Research both opportunities carefully", "Research")
            ]
        }
    ],

    "Class 11–12": [
        {
            "q": "A school wants to understand why students perform differently despite having similar study hours. What would you investigate first?",
            "options": [
                ("Collect and compare relevant data", "Data Analysis"),
                ("Identify possible variables affecting performance", "Scientific Thinking"),
                ("Design a structured investigation", "Research"),
                ("Examine how sleep, teaching, environment and study methods interact", "Systems Thinking")
            ]
        },
        {
            "q": "You are given conflicting statistics from two sources.",
            "options": [
                ("Check methodology and source credibility", "Critical Thinking"),
                ("Look at how the data was collected", "Research"),
                ("Compare the datasets directly", "Data Analysis"),
                ("Work out which conclusion is logically justified", "Logic")
            ]
        },
        {
            "q": "A team has limited money and three possible projects.",
            "options": [
                ("Compare impact, cost, risks and feasibility", "Decision Making"),
                ("Build a priority-based plan", "Planning"),
                ("Find ways to redesign the projects to use fewer resources", "Problem Solving"),
                ("Consider how each choice affects different stakeholders", "Systems Thinking")
            ]
        },
        {
            "q": "Your research question turns out to be too broad.",
            "options": [
                ("Narrow it into a measurable question", "Scientific Thinking"),
                ("Search existing research to identify a gap", "Research"),
                ("Break the question into smaller problems", "Logic"),
                ("Reframe it in a more original way", "Creativity")
            ]
        },
        {
            "q": "A group is divided over an important decision.",
            "options": [
                ("Establish objective criteria before choosing", "Critical Thinking"),
                ("Make sure every person's concerns are heard", "Empathy"),
                ("Compare the possible consequences", "Decision Making"),
                ("Lead the group towards a workable conclusion", "Leadership")
            ]
        },
        {
            "q": "You need to communicate a technical idea to a non-technical audience.",
            "options": [
                ("Use an analogy or visual explanation", "Creativity"),
                ("Remove unnecessary technical detail", "Communication"),
                ("Anticipate misunderstandings", "Empathy"),
                ("Build the explanation from simple principles", "Logic")
            ]
        },
        {
            "q": "A practical problem keeps returning even after quick fixes.",
            "options": [
                ("Look for the root cause", "Problem Solving"),
                ("Map how different factors contribute to it", "Systems Thinking"),
                ("Collect evidence about when and why it occurs", "Research"),
                ("Test a controlled change and observe the result", "Scientific Thinking")
            ]
        },
        {
            "q": "You are analysing a dataset and notice an unusual pattern.",
            "options": [
                ("Check whether it could be an error or outlier", "Critical Thinking"),
                ("Investigate what could have caused it", "Research"),
                ("Test whether the pattern appears elsewhere", "Data Analysis"),
                ("Develop possible explanations", "Scientific Thinking")
            ]
        },
        {
            "q": "You have four weeks to complete a large project.",
            "options": [
                ("Create milestones and deadlines", "Planning"),
                ("Identify the highest-risk parts first", "Decision Making"),
                ("Divide responsibilities among the team", "Leadership"),
                ("Create a flexible plan for unexpected problems", "Problem Solving")
            ]
        },
        {
            "q": "A policy seems helpful overall but could negatively affect one group.",
            "options": [
                ("Study the effects on different stakeholders", "Empathy"),
                ("Examine the evidence for the policy", "Critical Thinking"),
                ("Compare alternative policies", "Decision Making"),
                ("Study how the policy changes the larger system", "Systems Thinking")
            ]
        },
        {
            "q": "You have to propose an original solution to a real-world problem.",
            "options": [
                ("Generate several unconventional possibilities", "Creativity"),
                ("Research what has already been tried", "Research"),
                ("Identify the core problem before designing the solution", "Problem Solving"),
                ("Develop criteria to judge whether a solution works", "Scientific Thinking")
            ]
        },
        {
            "q": "You are leading a team whose members have different strengths.",
            "options": [
                ("Assign responsibilities according to strengths", "Leadership"),
                ("Create a clear workflow and timeline", "Planning"),
                ("Make sure everyone understands their role", "Communication"),
                ("Think about how the different roles depend on one another", "Systems Thinking")
            ]
        }
    ],

    "Graduated": [
        {
            "q": "An organisation asks you to solve a complex problem with incomplete information.",
            "options": [
                ("Define the problem and identify missing information", "Problem Solving"),
                ("Research comparable situations", "Research"),
                ("Map the stakeholders and interacting factors", "Systems Thinking"),
                ("Set decision criteria before evaluating options", "Decision Making")
            ]
        },
        {
            "q": "You receive two reports that reach different conclusions from similar data.",
            "options": [
                ("Audit assumptions and methodology", "Critical Thinking"),
                ("Reanalyse the underlying data", "Data Analysis"),
                ("Investigate the original sources", "Research"),
                ("Determine which conclusion follows logically", "Logic")
            ]
        },
        {
            "q": "A project is innovative but has significant implementation risks.",
            "options": [
                ("Compare potential impact against risks", "Decision Making"),
                ("Develop a phased implementation plan", "Planning"),
                ("Redesign the idea to reduce the risks", "Creativity"),
                ("Identify how one risk could trigger others", "Systems Thinking")
            ]
        },
        {
            "q": "A team is technically strong but constantly misunderstands one another.",
            "options": [
                ("Improve how information and expectations are communicated", "Communication"),
                ("Understand the perspectives behind the disagreements", "Empathy"),
                ("Create clearer roles and processes", "Planning"),
                ("Take responsibility for coordinating the team", "Leadership")
            ]
        },
        {
            "q": "You are asked to evaluate whether a new programme actually works.",
            "options": [
                ("Define measurable outcomes", "Scientific Thinking"),
                ("Analyse before-and-after data", "Data Analysis"),
                ("Compare results with a suitable baseline", "Critical Thinking"),
                ("Review existing evidence about similar programmes", "Research")
            ]
        },
        {
            "q": "A company wants to improve a process that involves several departments.",
            "options": [
                ("Map the entire process and dependencies", "Systems Thinking"),
                ("Identify the main bottleneck", "Problem Solving"),
                ("Analyse performance data", "Data Analysis"),
                ("Coordinate the departments around a plan", "Leadership")
            ]
        },
        {
            "q": "You have to communicate an unpopular but necessary decision.",
            "options": [
                ("Explain the reasoning and evidence clearly", "Communication"),
                ("Acknowledge how different people may be affected", "Empathy"),
                ("Explain the alternatives that were considered", "Decision Making"),
                ("Prepare for objections and test the argument", "Critical Thinking")
            ]
        },
        {
            "q": "A solution that worked elsewhere may not work in your context.",
            "options": [
                ("Identify differences between the two situations", "Critical Thinking"),
                ("Study local conditions and evidence", "Research"),
                ("Adapt the solution creatively", "Creativity"),
                ("Examine how changing one factor could affect the whole system", "Systems Thinking")
            ]
        },
        {
            "q": "You are given a large amount of information and only one day to produce a recommendation.",
            "options": [
                ("Identify the information most relevant to the decision", "Decision Making"),
                ("Organise the information into a clear structure", "Planning"),
                ("Find patterns and trends", "Data Analysis"),
                ("Separate strong evidence from weak claims", "Critical Thinking")
            ]
        },
        {
            "q": "A project has failed despite careful planning.",
            "options": [
                ("Analyse what actually caused the failure", "Problem Solving"),
                ("Review the assumptions behind the plan", "Critical Thinking"),
                ("Study the system and unexpected interactions", "Systems Thinking"),
                ("Design a different approach", "Creativity")
            ]
        },
        {
            "q": "You are asked to lead a project with people you have never worked with.",
            "options": [
                ("Understand everyone's strengths and expectations", "Empathy"),
                ("Set roles, goals and milestones", "Leadership"),
                ("Create a communication structure", "Planning"),
                ("Adapt your approach as the project develops", "Decision Making")
            ]
        },
        {
            "q": "You discover that a popular explanation is not supported by the available evidence.",
            "options": [
                ("Present the evidence and explain the limitations", "Communication"),
                ("Investigate why the popular explanation became accepted", "Research"),
                ("Develop a better-supported explanation", "Scientific Thinking"),
                ("Challenge the assumptions behind the original claim", "Critical Thinking")
            ]
        }
    ]
}


# ============================================================
# CSS
# ============================================================

st.markdown("""
<style>
/* DARK BUTTONS — WHITE TEXT */
.stButton > button {
    color: #FFFFFF !important;
    background-color: #333333 !important;
    border: 1px solid #555555 !important;
    font-weight: 600 !important;
}

.stButton > button p,
.stButton > button span {
    color: #FFFFFF !important;
}

.stButton > button:hover {
    color: #FFFFFF !important;
    background-color: #444444 !important;
}

.stButton > button:hover p,
.stButton > button:hover span {
    color: #FFFFFF !important;
}
body, p, div, span, label, li, td, th {
    color: #222222 !important;
}

h1, h2, h3, h4, h5, h6 {
    color: #222222 !important;
}

.stMarkdown, .stText, .stCaption {
    color: #222222 !important;
}

[data-testid="stMarkdownContainer"] {
    color: #222222 !important;
}

.stRadio label,
.stSelectbox label,
.stTextInput label {
    color: #222222 !important;
}
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(255, 220, 235, 0.45), transparent 25%),
        radial-gradient(circle at 90% 10%, rgba(210, 230, 255, 0.40), transparent 25%),
        linear-gradient(135deg, #fff9fc 0%, #f7f8ff 50%, #f8fbff 100%);
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1250px;
}

.hero {
    padding: 35px 35px 30px 35px;
    border-radius: 28px;
    background: rgba(255,255,255,0.82);
    border: 1px solid rgba(180,170,190,0.22);
    box-shadow: 0 12px 35px rgba(80,70,100,0.08);
    margin-bottom: 25px;
}

.hero-title {
    font-size: 3.1rem;
    font-weight: 700;
    margin-bottom: 8px;
    letter-spacing: -1.5px;
}

.hero-subtitle {
    font-size: 1.15rem;
    color: #666477;
    line-height: 1.6;
}

.card {
    padding: 24px;
    border-radius: 22px;
    background: rgba(255,255,255,0.88);
    border: 1px solid rgba(160,150,180,0.18);
    box-shadow: 0 8px 25px rgba(70,60,90,0.06);
    margin-bottom: 18px;
}

.skill-card {
    padding: 22px;
    border-radius: 20px;
    background: rgba(255,255,255,0.94);
    border: 1px solid rgba(150,140,170,0.18);
    margin-bottom: 15px;
}

.big-number {
    font-size: 2.2rem;
    font-weight: 700;
}

.small-muted {
    color: #777386;
    font-size: 0.9rem;
}

.question-card {
    padding: 28px;
    border-radius: 24px;
    background: rgba(255,255,255,0.95);
    border: 1px solid rgba(150,140,170,0.18);
    box-shadow: 0 10px 30px rgba(60,50,80,0.07);
    margin-bottom: 20px;
}

.question-number {
    color: #76677d;
    font-size: 0.9rem;
    font-weight: 600;
    margin-bottom: 10px;
}

.question-text {
    font-size: 1.35rem;
    line-height: 1.55;
    font-weight: 600;
}

.result-title {
    font-size: 2rem;
    font-weight: 700;
    margin-bottom: 5px;
}

.badge {
    display: inline-block;
    padding: 7px 13px;
    border-radius: 20px;
    background: #f1edf8;
    color: #5f526b;
    font-size: 0.82rem;
    font-weight: 600;
    margin: 3px;
}

.footer {
    text-align: center;
    color: #858090;
    font-size: 0.82rem;
    margin-top: 40px;
}

@media (max-width: 700px) {
    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }

    .hero-title {
        font-size: 2.25rem;
    }

    .hero {
        padding: 25px 20px;
    }

    .question-text {
        font-size: 1.12rem;
    }
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HEADER
# ============================================================

def show_header():
    st.markdown("""
    <div class="hero">
        <div class="hero-title">🧬 SkillDNA AI</div>
        <div class="hero-subtitle">
            Discover how you naturally approach real-world challenges —
            then explore skills, career directions and projects that may fit them.
        </div>
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# HOME
# ============================================================

if st.session_state.page == "Home":

    show_header()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
            <h3>🎯 Challenge-based</h3>
            <p>
            No personality-test style questions. SkillDNA uses realistic
            situations to explore how you approach problems.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <h3>🧠 Multiple strengths</h3>
            <p>
            There isn't one "correct" personality or career.
            Your responses build a broader skill profile.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
            <h3>🚀 Real-world direction</h3>
            <p>
            Explore career areas and project ideas connected to your
            strongest skills.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### Start your assessment")

    name = st.text_input(
        "Your name",
        value=st.session_state.student_name,
        placeholder="Enter your name"
    )

    level = st.selectbox(
        "Choose your level",
        ["Select level"] + list(QUESTION_BANK.keys())
    )

    st.markdown("")

    if st.button("✨ Discover My SkillDNA", type="primary", use_container_width=True):

        if not name.strip():
            st.warning("Please enter your name first.")

        elif level == "Select level":
            st.warning("Please choose your level.")

        else:
            st.session_state.student_name = name.strip()
            st.session_state.level = level

            selected = QUESTION_BANK[level].copy()
            random.shuffle(selected)

            prepared = []

            for question in selected:
                options = question["options"].copy()
                random.shuffle(options)

                prepared.append({
                    "q": question["q"],
                    "options": options
                })

            st.session_state.questions = prepared
            st.session_state.answers = {}
            st.session_state.current_question = 0
            st.session_state.completed = False
            st.session_state.page = "Assessment"

            st.rerun()

    st.markdown("""
    <div class="footer">
        SkillDNA AI • Class 11 Artificial Intelligence Capstone Project
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# ASSESSMENT
# ============================================================

elif st.session_state.page == "Assessment":

    show_header()

    questions = st.session_state.questions
    current = st.session_state.current_question
    total = len(questions)

    if current >= total:
        st.session_state.page = "Results"
        st.session_state.completed = True
        st.rerun()

    question = questions[current]

    progress = current / total
    st.progress(progress)

    st.markdown(
        f"""
        <div class="question-card">
            <div class="question-number">
                QUESTION {current + 1} OF {total}
            </div>
            <div class="question-text">
                {html.escape(question["q"])}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    option_texts = [item[0] for item in question["options"]]

    previous = st.session_state.answers.get(current)

    selected_option = st.radio(
        "Choose the response that feels most natural to you:",
        option_texts,
        index=option_texts.index(previous) if previous in option_texts else None,
        key=f"question_{current}"
    )

    st.markdown("")

    col1, col2 = st.columns(2)

    with col1:
        if current > 0:
            if st.button("← Previous", use_container_width=True):
                st.session_state.answers[current] = selected_option
                st.session_state.current_question -= 1
                st.rerun()

    with col2:
        button_text = "Finish Assessment →" if current == total - 1 else "Next →"

        if st.button(button_text, type="primary", use_container_width=True):

            if selected_option is None:
                st.warning("Choose one response before continuing.")

            else:
                st.session_state.answers[current] = selected_option

                if current == total - 1:
                    st.session_state.completed = True
                    st.session_state.page = "Results"
                else:
                    st.session_state.current_question += 1

                st.rerun()


# ============================================================
# RESULTS
# ============================================================

elif st.session_state.page == "Results":

    show_header()

    questions = st.session_state.questions
    answers = st.session_state.answers

    scores = {skill: 0 for skill in SKILLS}

    for index, question in enumerate(questions):

        chosen = answers.get(index)

        if chosen:

            for option_text, skill in question["options"]:

                if option_text == chosen:
                    scores[skill] += 1
                    break

    total_questions = len(questions)

    skill_percentages = {}

    for skill in SKILLS:
        skill_percentages[skill] = round(
            (scores.get(skill, 0) / total_questions) * 100
        )

    ranked = sorted(
        skill_percentages.items(),
        key=lambda item: (-item[1], SKILLS.index(item[0]))
    )

    top_skills = ranked[:4]

    top_four_count = sum(
        scores.get(skill, 0) for skill, _ in top_skills
    )

    overall = round(
        (top_four_count / total_questions) * 100
    )

    # --------------------------------------------------------
    # Career recommendations
    # --------------------------------------------------------

    career_results = []
    used = set()

    for skill, score in ranked:

        if score <= 0:
            continue

        for name, description in CAREERS.get(skill, []):

            if name not in used:

                career_results.append({
                    "name": name,
                    "description": description,
                    "skill": skill,
                    "score": score
                })

                used.add(name)

    # --------------------------------------------------------
    # Project recommendations
    # --------------------------------------------------------

    project_results = []

    for project in PROJECTS:

        matched = []
        project_score = 0

        for skill, strength in top_skills:

            if skill in project["skills"]:
                matched.append(skill)
                project_score += strength

        if matched:
            project_results.append(
                (project_score, project, matched)
            )

    project_results.sort(
        key=lambda item: item[0],
        reverse=True
    )

    safe_name = html.escape(st.session_state.student_name)

    st.markdown(
        f"""
        <div class="card">
            <div class="result-title">
                {safe_name}'s SkillDNA
            </div>
            <p class="small-muted">
                Based on your responses to real-world challenge scenarios.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Top Skill", top_skills[0][0])

    with c2:
        st.metric("Strongest Score", f"{top_skills[0][1]}%")

    with c3:
        st.metric("Top 4 Strength Index", f"{overall}%")

    st.markdown("## 🧠 Your strongest skills")

    for rank, (skill, score) in enumerate(top_skills, start=1):

        st.markdown(
            f"""
            <div class="skill-card">
                <h3>{rank}. {skill} — {score}%</h3>
                <p>{SKILL_DESCRIPTIONS[skill]}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.progress(score / 100)

    st.markdown("## 📊 Your complete skill profile")

    chart_data = {
        skill: score
        for skill, score in ranked
        if score > 0
    }

    if chart_data:
        st.bar_chart(chart_data)
   top_skills = [
    (skill, score)
    for skill, score in ranked
    if score > 0
][:5]
    st.markdown("## 🧭 Explore your results")

    selected_tab = st.tabs(["Overview", "Careers", "Projects", "Growth", "Review"])
    # OVERVIEW
    # ========================================================

    with selected_tab[0]:

        st.markdown("""
        <div class="card">
            <h3>What does this mean?</h3>
            <p>
            Your SkillDNA is not a fixed personality label and it does not
            decide your career for you. It highlights patterns in the way
            you approached the situations in this assessment.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### Your skill combination")

        for skill, score in top_skills:
            st.markdown(
                f'<span class="badge">{skill} · {score}%</span>',
                unsafe_allow_html=True
            )

        st.info(
            "Use these results as a starting point for exploring what you "
            "enjoy, what you practise and what you may want to develop further."
        )

    # ========================================================
    # CAREERS
    # ========================================================

    with selected_tab[1]:

        st.markdown("### 🚀 Career directions")

        if not career_results:

            st.info(
                "Complete more assessment responses to generate career directions."
            )

        else:

            displayed = career_results[:8]

            for career in displayed:

                st.markdown(
                    f"""
                    <div class="card">
                        <h3>{career["name"]}</h3>
                        <p>{career["description"]}</p>
                        <span class="badge">
                            Connected skill: {career["skill"]}
                        </span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

    # ========================================================
    # PROJECTS
    # ========================================================

    with selected_tab[2]:

        st.markdown("### 🛠️ Real-world project ideas")

        if not project_results:

            st.info(
                "No project matched your current strongest skills."
            )

        else:

            for _, project, matched in project_results[:6]:

                st.markdown(
                    f"""
                    <div class="card">
                        <h3>{project["name"]}</h3>
                        <p>{project["description"]}</p>
                        <p>
                            <strong>Category:</strong> {project["category"]}
                        </p>
                        <p>
                            <strong>Skills involved:</strong>
                            {", ".join(matched)}
                        </p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.link_button(
                    "🔗 Explore resource",
                    project["link"]
                )

    # ========================================================
    # GROWTH
    # ========================================================

    with selected_tab[3]:

        st.markdown("### 🌱 How you can grow")

        for skill, score in top_skills:

            st.markdown(
                f"""
                <div class="card">
                    <h3>{skill}</h3>
                    <p>{GROWTH[skill]}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.success(
            "Your strongest skills are not permanent labels. Skills can grow "
            "through practice, projects, feedback and new experiences."
        )

    # ========================================================
    # REVIEW
    # ========================================================

    with tabs[4]:
        st.subheader("📝 Review Your Answers")
        st.write("See what each of your choices indicates about your strengths.")

    # Explanation for each skill
    explanations = {
        "Logic": "This choice indicates that you prefer using reasoning, patterns, and clear connections to reach a solution.",

        "Creativity": "This choice indicates that you are comfortable thinking of original ideas and exploring different possibilities.",

        "Scientific Thinking": "This choice indicates that you prefer observing evidence, testing ideas, and understanding how things work.",

        "Data Analysis": "This choice indicates that you like finding patterns and making conclusions from information or numbers.",

        "Problem Solving": "This choice indicates that you tend to break challenges into manageable steps and look for practical solutions.",

        "Communication": "This choice indicates that you value explaining ideas clearly and making sure others understand your point.",

        "Leadership": "This choice indicates that you are comfortable taking initiative, coordinating people, and helping a group move forward.",

        "Research": "This choice indicates that you like gathering information and investigating a topic before reaching a conclusion.",

        "Empathy": "This choice indicates that you consider other people's feelings, experiences, and perspectives when making decisions.",

        "Planning": "This choice indicates that you prefer organising tasks, resources, and steps before taking action.",

        "Critical Thinking": "This choice indicates that you prefer checking evidence and evaluating information before accepting a conclusion.",

        "Systems Thinking": "This choice indicates that you notice how different parts of a situation are connected and affect one another.",

        "Decision Making": "This choice indicates that you can compare possibilities and choose an appropriate course of action."
    }

    for i, answer in enumerate(st.session_state.answers):
        question = st.session_state.questions[i]

        # Find the skill connected to the selected answer
        selected_skill = None

        for option_text, skill in question["options"]:
            if option_text == answer:
                selected_skill = skill
                break

        with st.container():
            st.markdown(
                f"""
                <div class="question-card">
                    <h4>Question {i + 1}</h4>
                    <p><b>{html.escape(question["question"])}</b></p>
                    <p><b>Your choice:</b> {html.escape(answer)}</p>
                    <p><b>Skill indicated:</b> {html.escape(selected_skill or "Not identified")}</p>
                    <p><b>Why this choice?</b> {html.escape(explanations.get(selected_skill, "This choice contributes to the skill profile shown in your results."))}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
