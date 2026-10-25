from flask import Flask, render_template, request, session, redirect,Response
from datetime import date, datetime
import random



app = Flask(__name__)

quiz_questions = {
    "python": [
        {"question": "Which keyword defines a function?", "options": ["function", "def", "fun", "define"], "answer": "def"},
        {"question": "Which data type stores True or False?", "options": ["int", "str", "bool", "list"], "answer": "bool"},
        {"question": "Which symbol starts a Python comment?", "options": ["//", "#", "/*", "$"], "answer": "#"},
        {"question": "Which function displays output?", "options": ["input()", "print()", "show()", "display()"], "answer": "print()"},
        {"question": "Which function accepts user input?", "options": ["scan()", "get()", "input()", "read()"], "answer": "input()"},
        {"question": "Which brackets create a list?", "options": ["()", "{}", "[]", "<>"], "answer": "[]"},
        {"question": "Which operator performs exponentiation?", "options": ["^", "**", "//", "%"], "answer": "**"},
        {"question": "Which keyword checks a condition?", "options": ["if", "for", "def", "import"], "answer": "if"},
        {"question": "Which loop iterates over a sequence?", "options": ["if", "for", "def", "class"], "answer": "for"},
        {"question": "Which value represents no value?", "options": ["NULL", "None", "empty", "zero"], "answer": "None"},
        {"question": "Which data type stores whole numbers?", "options": ["int", "str", "bool", "list"], "answer": "int"},
        {"question": "Which method adds an item to a list?", "options": ["add()", "append()", "insertEnd()", "pushItem()"], "answer": "append()"},
        {"question": "Which operator checks equality?", "options": ["=", "==", "!=", ":="], "answer": "=="},
        {"question": "Which keyword imports a module?", "options": ["include", "using", "import", "load"], "answer": "import"},
        {"question": "Which collection stores key-value pairs?", "options": ["List", "Tuple", "Dictionary", "String"], "answer": "Dictionary"},
        {"question": "Which function returns the length of an object?", "options": ["size()", "count()", "len()", "length()"], "answer": "len()"},
        {"question": "Which keyword handles exceptions?", "options": ["try", "check", "test", "catchError"], "answer": "try"},
        {"question": "Which keyword exits a loop?", "options": ["stop", "exit", "break", "close"], "answer": "break"},
        {"question": "Which data type stores text?", "options": ["int", "str", "float", "bool"], "answer": "str"},
        {"question": "Which keyword creates a class?", "options": ["object", "class", "define", "struct"], "answer": "class"}
    ],

    "java": [
        {"question": "Which keyword creates a class?", "options": ["class", "define", "struct", "create"], "answer": "class"},
        {"question": "What is the entry point of a Java program?", "options": ["start()", "run()", "main()", "open()"], "answer": "main()"},
        {"question": "Which company originally developed Java?", "options": ["Microsoft", "Sun Microsystems", "IBM", "Apple"], "answer": "Sun Microsystems"},
        {"question": "Which keyword creates an object?", "options": ["make", "new", "create", "object"], "answer": "new"},
        {"question": "Which type stores whole numbers?", "options": ["int", "String", "boolean", "char"], "answer": "int"},
        {"question": "Which type stores text objects?", "options": ["Text", "String", "char", "word"], "answer": "String"},
        {"question": "Which keyword inherits a class?", "options": ["implements", "extends", "inherits", "superclass"], "answer": "extends"},
        {"question": "Which keyword refers to the current object?", "options": ["self", "this", "current", "object"], "answer": "this"},
        {"question": "Which keyword prevents class inheritance?", "options": ["static", "private", "final", "void"], "answer": "final"},
        {"question": "Which type stores true or false?", "options": ["int", "boolean", "String", "char"], "answer": "boolean"},
        {"question": "Which symbol ends most Java statements?", "options": [".", ":", ";", ","], "answer": ";"},
        {"question": "Which access modifier allows access from anywhere?", "options": ["private", "protected", "public", "default"], "answer": "public"},
        {"question": "Which loop executes while a condition is true?", "options": ["while", "switch", "class", "import"], "answer": "while"},
        {"question": "Which keyword creates a subclass relationship?", "options": ["extends", "package", "return", "throw"], "answer": "extends"},
        {"question": "Which concept means one name with different forms?", "options": ["Encapsulation", "Polymorphism", "Compilation", "Iteration"], "answer": "Polymorphism"},
        {"question": "Which block handles an exception?", "options": ["final", "catch", "static", "import"], "answer": "catch"},
        {"question": "Which keyword declares a constant-like variable?", "options": ["fixed", "const", "final", "constant"], "answer": "final"},
        {"question": "Which keyword implements an interface?", "options": ["extends", "implements", "inherits", "interface"], "answer": "implements"},
        {"question": "Which package is automatically imported in Java?", "options": ["java.util", "java.io", "java.lang", "java.net"], "answer": "java.lang"},
        {"question": "Which method compares String contents?", "options": ["==", "equals()", "compareOnly()", "same()"], "answer": "equals()"}
    ],

    "dbms": [
        {"question": "What does DBMS stand for?", "options": ["Data Base Management System", "Digital Base Main System", "Data Backup Memory System", "Database Machine Setup"], "answer": "Data Base Management System"},
        {"question": "Which language is commonly used to query databases?", "options": ["HTML", "SQL", "CSS", "XML"], "answer": "SQL"},
        {"question": "What is a table made up of?", "options": ["Rows and columns", "Slides", "Pages only", "Files only"], "answer": "Rows and columns"},
        {"question": "What uniquely identifies a row in a table?", "options": ["Foreign key", "Primary key", "Duplicate key", "Null key"], "answer": "Primary key"},
        {"question": "What is a foreign key used for?", "options": ["Formatting text", "Linking tables", "Deleting databases", "Sorting files"], "answer": "Linking tables"},
        {"question": "Which SQL command retrieves data?", "options": ["GET", "OPEN", "SELECT", "FETCHALL"], "answer": "SELECT"},
        {"question": "Which SQL command adds new rows?", "options": ["INSERT", "UPDATE", "ALTER", "SELECT"], "answer": "INSERT"},
        {"question": "Which SQL command modifies existing rows?", "options": ["CHANGE", "UPDATE", "MODIFY TABLE", "REPLACE DB"], "answer": "UPDATE"},
        {"question": "Which SQL command removes rows?", "options": ["DROP", "DELETE", "CLEAR", "ERASE"], "answer": "DELETE"},
        {"question": "Which clause filters rows?", "options": ["WHERE", "ORDER BY", "GROUP BY", "SELECT"], "answer": "WHERE"},
        {"question": "Which clause sorts query results?", "options": ["SORT", "ORDER BY", "ARRANGE", "GROUP BY"], "answer": "ORDER BY"},
        {"question": "What does SQL stand for?", "options": ["Structured Query Language", "Simple Question Language", "System Quick Link", "Sequential Query Logic"], "answer": "Structured Query Language"},
        {"question": "What is normalization used for?", "options": ["Reducing data redundancy", "Increasing duplication", "Changing screen size", "Encrypting all files"], "answer": "Reducing data redundancy"},
        {"question": "What does ER model stand for?", "options": ["Entity Relationship model", "External Record model", "Easy Retrieval model", "Entry Reference model"], "answer": "Entity Relationship model"},
        {"question": "Which key can contain duplicate values?", "options": ["Primary key", "Candidate key", "A non-key attribute", "Unique key"], "answer": "A non-key attribute"},
        {"question": "What is a database transaction?", "options": ["A logical unit of work", "A screen design", "A programming language", "A type of printer"], "answer": "A logical unit of work"},
        {"question": "What does ACID stand for in DBMS?", "options": ["Atomicity, Consistency, Isolation, Durability", "Access, Control, Index, Data", "Automatic, Clear, Insert, Delete", "Accuracy, Code, Input, Design"], "answer": "Atomicity, Consistency, Isolation, Durability"},
        {"question": "Which SQL function counts rows?", "options": ["SUM()", "COUNT()", "TOTAL()", "NUMBER()"], "answer": "COUNT()"},
        {"question": "Which SQL command creates a table?", "options": ["MAKE TABLE", "CREATE TABLE", "NEW TABLE", "BUILD TABLE"], "answer": "CREATE TABLE"},
        {"question": "What is a database schema?", "options": ["Database structure or design", "A single row", "A password", "A query result only"], "answer": "Database structure or design"}
    ]
}
    
app.secret_key = "study_planner_secret"


# ==========================================
# YOUTUBE STUDY VIDEOS
# ==========================================

youtube_links = {


    "java": [
        {
            "title": "Java Programming for Beginners",
            "url": "https://www.youtube.com/results?search_query=java+programming+for+beginners"
        },
        {
            "title": "Java OOP Concepts",
            "url": "https://www.youtube.com/results?search_query=java+oops+concepts"
        }
    ],

    "dbms": [
        {
            "title": "DBMS Full Course",
            "url": "https://www.youtube.com/results?search_query=dbms+full+course"
        },
        {
            "title": "SQL for Beginners",
            "url": "https://www.youtube.com/results?search_query=sql+for+beginners"
        }
    ],

    "c++": [
        {
            "title": "C++ Programming for Beginners",
            "url": "https://www.youtube.com/results?search_query=c%2B%2B+programming+for+beginners"
        },
        {
            "title": "C++ OOP Concepts",
            "url": "https://www.youtube.com/results?search_query=c%2B%2B+oops+concepts"
        }
    ],

    "artificial intelligence": [
        {
            "title": "Artificial Intelligence for Beginners",
            "url": "https://www.youtube.com/results?search_query=artificial+intelligence+for+beginners"
        },
        {
            "title": "AI Fundamentals",
            "url": "https://www.youtube.com/results?search_query=AI+fundamentals"
        }
    ],

    "machine learning": [
        {
            "title": "Machine Learning for Beginners",
            "url": "https://www.youtube.com/results?search_query=machine+learning+for+beginners"
        },
        {
            "title": "Machine Learning Basics",
            "url": "https://www.youtube.com/results?search_query=machine+learning+basics"
        }
    ],

    "cyber security": [
        {
            "title": "Cyber Security for Beginners",
            "url": "https://www.youtube.com/results?search_query=cyber+security+for+beginners"
        },
        {
            "title": "Cyber Security Fundamentals",
            "url": "https://www.youtube.com/results?search_query=cyber+security+fundamentals"
        }
    ],

    "data science": [
        {
            "title": "Data Science for Beginners",
            "url": "https://www.youtube.com/results?search_query=data+science+for+beginners"
        },
        {
            "title": "Data Science Fundamentals",
            "url": "https://www.youtube.com/results?search_query=data+science+fundamentals"
        }
    ],

    "data analytics": [
        {
            "title": "Data Analytics for Beginners",
            "url": "https://www.youtube.com/results?search_query=data+analytics+for+beginners"
        },
        {
            "title": "Data Analytics Fundamentals",
            "url": "https://www.youtube.com/results?search_query=data+analytics+fundamentals"
        }
    ],

    "web development": [
        {
            "title": "Web Development for Beginners",
            "url": "https://www.youtube.com/results?search_query=web+development+for+beginners"
        },
        {
            "title": "HTML CSS JavaScript Basics",
            "url": "https://www.youtube.com/results?search_query=HTML+CSS+JavaScript+basics"
        }
    ],

    "computer networks": [
        {
            "title": "Computer Networks for Beginners",
            "url": "https://www.youtube.com/results?search_query=computer+networks+for+beginners"
        },
        {
            "title": "Computer Networks Fundamentals",
            "url": "https://www.youtube.com/results?search_query=computer+networks+fundamentals"
        }
    ],

    "sql": [
        {
            "title": "SQL for Beginners",
            "url": "https://www.youtube.com/results?search_query=SQL+for+beginners"
        },
        
        

    ]
}


# ==========================================
# RESEARCH PAPER RESOURCES
# ==========================================

research_resources = {

    "python": [
        {
            "title": "Python Programming Research",
            "type": "Research Collection",
            "description": "Explore research papers related to Python programming.",
            "url": "https://scholar.google.com/scholar?q=Python+programming+research"
        }
    ],

    "java": [
        {
            "title": "Java Programming Research",
            "type": "Research Collection",
            "description": "Explore research papers related to Java programming.",
            "url": "https://scholar.google.com/scholar?q=Java+programming+research"
        }
    ],

    "dbms": [
        {
            "title": "Database Management System Research",
            "type": "Research Collection",
            "description": "Explore research papers related to DBMS and databases.",
            "url": "https://scholar.google.com/scholar?q=database+management+systems+research"
        }
    ],

    "c++": [
        {
            "title": "C++ Programming Research",
            "type": "Research Collection",
            "description": "Explore research papers related to C++ programming.",
            "url": "https://scholar.google.com/scholar?q=C%2B%2B+programming+research"
        }
    ],

    "artificial intelligence": [
        {
            "title": "AI and Self-Regulated Learning",
            "type": "Systematic Review",
            "description": "Research on AI technologies supporting student self-regulated learning.",
            "url": "https://www.sciencedirect.com/science/article/pii/S1041608026000518"
        },
        {
            "title": "AI Empowered Self-Regulated Learning in Higher Education",
            "type": "Systematic Review",
            "description": "Research on AI-supported self-regulated learning in higher education.",
            "url": "https://www.nature.com/articles/s41539-025-00319-0"
        },
        {
            "title": "AI and Self-Regulated Learning",
            "type": "Systematic Mapping Review",
            "description": "Research mapping AI applications that support self-regulated learning.",
            "url": "https://link.springer.com/article/10.1186/s41239-025-00548-8"
        }
    ],

    "machine learning": [
        {
            "title": "Machine Learning Research",
            "type": "Research Collection",
            "description": "Explore research papers related to machine learning.",
            "url": "https://scholar.google.com/scholar?q=machine+learning+research"
        }
    ],

    "cyber security": [
        {
            "title": "Cyber Security Research",
            "type": "Research Collection",
            "description": "Explore research papers related to cybersecurity.",
            "url": "https://scholar.google.com/scholar?q=cybersecurity+research"
        }
    ],

    "data science": [
        {
            "title": "Data Science Research",
            "type": "Research Collection",
            "description": "Explore research papers related to data science.",
            "url": "https://scholar.google.com/scholar?q=data+science+research"
        }
    ],

    "data analytics": [
        {
            "title": "Data Analytics Research",
            "type": "Research Collection",
            "description": "Explore research papers related to data analytics.",
            "url": "https://scholar.google.com/scholar?q=data+analytics+research"
        }
    ],

    "web development": [
        {
            "title": "Web Development Research",
            "type": "Research Collection",
            "description": "Explore research papers related to web development.",
            "url": "https://scholar.google.com/scholar?q=web+development+research"
        }
    ],

    "computer networks": [
        {
            "title": "Computer Networks Research",
            "type": "Research Collection",
            "description": "Explore research papers related to computer networks.",
            "url": "https://scholar.google.com/scholar?q=computer+networks+research"
        }
    ],

    "sql": [
        {
            "title": "SQL and Database Research",
            "type": "Research Collection",
            "description": "Explore research papers related to SQL and databases.",
            "url": "https://scholar.google.com/scholar?q=SQL+database+research"
        }
    ]
}


# ==========================================
# TRUSTED STUDY WEBSITES
# ==========================================

trusted_websites = {

    "python": [
        {
            "title": "Python Official Documentation",
            "url": "https://docs.python.org/3/"
        },
        {
            "title": "W3Schools Python",
            "url": "https://www.w3schools.com/python/"
        }
    ],

    "java": [
        {
            "title": "Oracle Java Documentation",
            "url": "https://docs.oracle.com/en/java/"
        },
        {
            "title": "W3Schools Java",
            "url": "https://www.w3schools.com/java/"
        }
    ],

    "dbms": [
        {
            "title": "GeeksforGeeks DBMS",
            "url": "https://www.geeksforgeeks.org/dbms/"
        },
        {
            "title": "W3Schools SQL",
            "url": "https://www.w3schools.com/sql/"
        }
    ],

    "c++": [
        {
            "title": "Learn C++",
            "url": "https://www.learncpp.com/"
        },
        {
            "title": "W3Schools C++",
            "url": "https://www.w3schools.com/cpp/"
        }
    ],

    "artificial intelligence": [
        {
            "title": "IBM AI",
            "url": "https://www.ibm.com/think/topics/artificial-intelligence"
        },
        {
            "title": "Google AI",
            "url": "https://ai.google/"
        }
    ],

    "machine learning": [
        {
            "title": "Google Machine Learning",
            "url": "https://developers.google.com/machine-learning"
        },
        {
            "title": "Microsoft Machine Learning",
            "url": "https://learn.microsoft.com/en-us/training/"
        }
    ],

    "cyber security": [
        {
            "title": "OWASP",
            "url": "https://owasp.org/"
        },
        {
            "title": "Cisco Cybersecurity",
            "url": "https://www.cisco.com/site/us/en/learn/topics/security/what-is-cybersecurity.html"
        }
    ],

    "data science": [
        {
            "title": "Kaggle",
            "url": "https://www.kaggle.com/"
        },
        {
            "title": "IBM Data Science",
            "url": "https://www.ibm.com/think/topics/data-science"
        }
    ],

    "data analytics": [
        {
            "title": "Microsoft Learn",
            "url": "https://learn.microsoft.com/en-us/training/"
        },
        {
            "title": "Kaggle",
            "url": "https://www.kaggle.com/"
        }
    ],

    "web development": [
        {
            "title": "MDN Web Docs",
            "url": "https://developer.mozilla.org/en-US/"
        },
        {
            "title": "W3Schools",
            "url": "https://www.w3schools.com/"
        }
    ],

    "computer networks": [
        {
            "title": "Cisco Networking",
            "url": "https://www.cisco.com/site/us/en/learn/topics/networking/what-is-computer-networking.html"
        },
        {
            "title": "GeeksforGeeks Computer Networks",
            "url": "https://www.geeksforgeeks.org/computer-networks/"
        }
    ],

    "sql": [
        {
            "title": "W3Schools SQL",
            "url": "https://www.w3schools.com/sql/"
        },
        {
            "title": "SQL Tutorial",
            "url": "https://www.sqltutorial.org/"
        }
    ]
}


# ==========================================
# COMPLETE
# ==========================================

@app.route("/complete")
def complete():

    completed = session.get("completed", 0)

    if completed < 10:
        completed += 1

    session["completed"] = completed

    return redirect("/planner")


# ==========================================
# HOME PAGE
# ==========================================

@app.route("/")
def home():

    return render_template("index.html")


@app.route("/details")
def details():

    details_data = session.get("details_data")

    if not details_data:
        return redirect("/planner")

    return render_template("details.html", **details_data)


    


# ==========================================
# STUDY PLANNER
# ==========================================

@app.route("/planner", methods=["GET", "POST"])
def planner():

    if request.method == "POST":

        name = request.form["name"]
        subject = request.form["subject"]
        google_search = "https://www.google.com/search?q=" + subject.replace(" ", "+") + "+study+materials"
        hours = request.form["hours"]
        exam_date = request.form["exam_date"]
        

        # Calculate days left
        today = date.today()

        exam = datetime.strptime(
            exam_date,
            "%Y-%m-%d"
        ).date()

        days_left = (exam - today).days

        # Study hours
        study_hours = int(hours)

        # ==================================
        # SUGGESTED PLAN
        # ==================================

        plans = {

            "python":
                "Learn Python basics, practice programs, revise syntax, and solve previous questions.",

            "java":
                "Study OOP concepts, practice Java programs, revise important topics, and solve previous questions.",

            "dbms":
                "Study SQL, ER diagrams, normalization, practice queries, and revise important questions.",

            "c++":
                "Study C++ basics, OOP concepts, practice programs, and revise important questions.",

            "artificial intelligence":
                "Study AI fundamentals, intelligent agents, search techniques, machine learning basics, and solve previous questions.",

            "machine learning":
                "Study supervised learning, unsupervised learning, algorithms, model evaluation, and practice examples.",

            "cyber security":
                "Study cybersecurity fundamentals, threats, network security, malware, and security practices.",

            "data science":
                "Study data preprocessing, statistics, visualization, machine learning basics, and practical examples.",

            "data analytics":
                "Study data cleaning, analysis, visualization, Excel, SQL concepts, and analytical methods.",

            "web development":
                "Study HTML, CSS, JavaScript, web concepts, and practice building simple web pages.",

            "computer networks":
                "Study networking fundamentals, OSI model, TCP/IP, protocols, routing, and network security.",

            "sql":
                "Study SQL commands, queries, joins, subqueries, functions, and database operations."
        }

        plan = plans.get(
            subject.lower(),
            "Study important concepts, make short notes, revise regularly, and practice previous questions."
        )

        # ==================================
        # DAILY STUDY SCHEDULE
        # ==================================

        schedules = {

            "python": [
                "Python Basics",
                "Variables and Data Types",
                "Operators and Expressions",
                "If-Else Statements",
                "Loops",
                "Functions",
                "Lists and Dictionaries",
                "Practice Programs",
                "Previous Questions",
                "Final Revision"
            ],

            "java": [
                "Java Basics",
                "Variables and Data Types",
                "Control Statements",
                "Classes and Objects",
                "Inheritance",
                "Polymorphism",
                "Exception Handling",
                "Practice Programs",
                "Previous Questions",
                "Final Revision"
            ],

            "dbms": [
                "DBMS Basics",
                "ER Model",
                "SQL Commands",
                "Normalization",
                "Transactions",
                "Practice SQL Queries",
                "Previous Questions",
                "Final Revision"
            ],

            "c++": [
                "C++ Basics",
                "Variables and Data Types",
                "Operators and Expressions",
                "Classes and Objects",
                "Inheritance",
                "Polymorphism",
                "Exception Handling",
                "Practice Programs",
                "Previous Questions",
                "Final Revision"
            ],

            "artificial intelligence": [
                "AI Fundamentals",
                "Intelligent Agents",
                "Problem Solving",
                "Search Techniques",
                "Knowledge Representation",
                "Machine Learning Basics",
                "AI Applications",
                "Practice Questions",
                "Previous Questions",
                "Final Revision"
            ],

            "machine learning": [
                "ML Fundamentals",
                "Supervised Learning",
                "Unsupervised Learning",
                "Regression",
                "Classification",
                "Clustering",
                "Model Evaluation",
                "Practice Examples",
                "Previous Questions",
                "Final Revision"
            ],

            "cyber security": [
                "Cybersecurity Basics",
                "Cyber Threats",
                "Malware",
                "Phishing",
                "Network Security",
                "Authentication",
                "Security Tools",
                "Practice Questions",
                "Previous Questions",
                "Final Revision"
            ],

            "data science": [
                "Data Science Basics",
                "Data Collection",
                "Data Cleaning",
                "Statistics",
                "Data Visualization",
                "Machine Learning",
                "Data Analysis",
                "Practice Examples",
                "Previous Questions",
                "Final Revision"
            ],

            "data analytics": [
                "Analytics Basics",
                "Data Collection",
                "Data Cleaning",
                "Excel Concepts",
                "SQL Concepts",
                "Data Visualization",
                "Analysis Techniques",
                "Practice Examples",
                "Previous Questions",
                "Final Revision"
            ],

            "web development": [
                "HTML Basics",
                "HTML Forms",
                "CSS Basics",
                "CSS Layout",
                "JavaScript Basics",
                "JavaScript Events",
                "Web Forms",
                "Practice Website",
                "Previous Questions",
                "Final Revision"
            ],

            "computer networks": [
                "Networking Basics",
                "OSI Model",
                "TCP/IP",
                "Network Devices",
                "Protocols",
                "IP Addressing",
                "Routing",
                "Network Security",
                "Previous Questions",
                "Final Revision"
            ],

            "sql": [
                "SQL Basics",
                "SELECT Commands",
                "WHERE and ORDER BY",
                "Functions",
                "GROUP BY",
                "Joins",
                "Subqueries",
                "Practice Queries",
                "Previous Questions",
                "Final Revision"
            ]
        }

        topic_list = schedules.get(
            subject.lower(),
            [
                "Basic Concepts",
                "Important Topics",
                "Short Notes",
                "Practice Questions",
                "Previous Questions",
                "Final Revision"
            ]
        )

        schedule = []

        for index, topic in enumerate(topic_list, start=1):

            if index == len(topic_list):
                day_text = f"Final Day → {topic}"
            else:
                day_text = f"Day {index} → {topic}"

            schedule.append(
                f"{day_text} ({study_hours} hours)"
            )

        # ==================================
        # SAVE DETAILS
        # ==================================

        session["name"] = name
        session["subject"] = subject
        session["hours"] = hours
        session["exam_date"] = exam_date

        # ==================================
        # GET YOUTUBE VIDEOS
        # ==================================

        videos = youtube_links.get(
            subject.lower(),
            [
                {
                    "title": f"{subject} Study Videos",
                    "url":
                        "https://www.youtube.com/results?search_query="
                        + subject.replace(" ", "+")
                        + "+tutorial"
                }
            ]
        )

        # ==================================
        # GET RESEARCH PAPERS
        # ==================================

        resources = research_resources.get(
            subject.lower(),
            [
                {
                    "title": f"{subject} Research Papers",
                    "type": "Research Collection",
                    "description":
                        f"Explore research papers related to {subject}.",
                    "url":
                        "https://scholar.google.com/scholar?q="
                        + subject.replace(" ", "+")
                        + "+research"
                }
            ]
        )

        # ==================================
        # GET TRUSTED WEBSITES
        # ==================================

        websites = trusted_websites.get(
            subject.lower(),
            [
                {
                    "title": f"{subject} Learning Resources",
                    "url":
                        "https://www.google.com/search?q="
                        + subject.replace(" ", "+")
                        + "+learning"
                }
            ]
        )
       
        # ==================================
        # SEND DATA TO details.html
        #    ==================================

        return render_template(
            "details.html",
            name=name,
            subject=subject,
            hours=hours,
            exam_date=exam_date,
            days_left=days_left,
            plan=plan,
            schedule=schedule,
            videos=videos,
            resources=resources,
            websites=websites,
            google_search=google_search
        )

    return render_template("planner.html")


# ==========================================
# RUN APPLICATION
# ==========================================



@app.route("/quiz", methods=["GET", "POST"])
def quiz():

    subject = request.args.get(
        "subject",
        session.get("subject", "python")
    ).lower()

    question_bank = quiz_questions.get(
        subject,
        quiz_questions["python"]
    )

    if request.method == "POST":

        quiz_list = session.get("active_quiz", [])
        score = 0

        for i, question in enumerate(quiz_list):
            selected = request.form.get(f"q{i}")

            if selected == question["answer"]:
                score += 1

        session.pop("active_quiz", None)

        return render_template(
            "quiz.html",
            questions=quiz_list,
            subject=subject.title(),
            score=score,
            submitted=True
        )

    # New attempt: choose 15 random questions
    quiz_list = random.sample(
        question_bank,
        min(20, len(question_bank))
    )

    session["active_quiz"] = quiz_list

    return render_template(
        "quiz.html",
        questions=quiz_list,
        subject=subject.title(),
        score=None,
        submitted=False
    )

@app.route('/timetable')
def timetable():
    return render_template('timetable.html')


@app.route("/download-reminders")
def download_reminders():
    from datetime import datetime, timedelta
    from urllib.parse import quote

    exam_date_text = session.get("exam_date")
    subject = session.get("subject", "Study")
    study_hours = session.get("hours", "2")

    if not exam_date_text:
        return redirect("/planner")

    try:
        exam_date = datetime.strptime(
            exam_date_text, "%Y-%m-%d"
        ).date()
    except ValueError:
        return "Invalid exam date. Please create your study plan again.", 400

    today = date.today()
    events = []

    def add_event(title, event_date, description):
        start = datetime.combine(
            event_date, datetime.min.time()
        ).replace(hour=18)

        end = start + timedelta(hour=1)

        def format_date(dt):
            return dt.strftime("%Y%m%dT%H%M%S")

        events.append(
            "BEGIN:VEVENT\n"
            f"UID:{format_date(start)}-{len(events)}@studyplanner.local\n"
            f"DTSTAMP:{datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')}\n"
            f"DTSTART:{format_date(start)}\n"
            f"DTEND:{format_date(end)}\n"
            f"SUMMARY:{title}\n"
            f"DESCRIPTION:{description}\n"
            "BEGIN:VALARM\n"
            "TRIGGER:-PT10M\n"
            "ACTION:DISPLAY\n"
            "DESCRIPTION:Study reminder\n"
            "END:VALARM\n"
            "END:VEVENT"
        )

    # Daily study reminders at 6 PM
    current_date = today
    while current_date <= exam_date:
        add_event(
            f"Study {subject}",
            current_date,
            f"Study for {study_hours} hours. Open your AI Student Study Planner."
        )
        current_date += timedelta(days=1)

    # Extra reminders before the exam
    for days_before in (3, 1):
        reminder_date = exam_date - timedelta(days=days_before)
        if today <= reminder_date < exam_date:
            add_event(
                f"Exam Reminder: {subject}",
                reminder_date,
                f"Your exam is in {days_before} day(s). Revise important topics."
            )

    add_event(
        f"Exam Day: {subject}",
        exam_date,
        "Review your notes and prepare for your exam."
    )

    calendar_text = (
        "BEGIN:VCALENDAR\n"
        "VERSION:2.0\n"
        "PRODID:-//AI Student Study Planner//EN\n"
        "CALSCALE:GREGORIAN\n"
        + "\n".join(events)
        + "\nEND:VCALENDAR\n"
    )

    return Response(
        calendar_text,
        mimetype="text/calendar",
        headers={
            "Content-Disposition":
                'attachment; filename="study_reminders.ics"'
        }
    )





if __name__ == "__main__":
    app.run(debug=True)