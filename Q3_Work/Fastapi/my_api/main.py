from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_my_details():
    return {
        "name" : "Muhammad Daniyal",
         "education": {
            "primary_middle": "Completed primary to 8th grade from Labaik Public School.",
            "ssc": "Passed Secondary School Certificate (SSC) from Noor Eastern School.",
            "hssc": "Passed Higher Secondary School Certificate (HSSC) in Computer Science from Govt. Degree College Nawabshah.",
            "giaic": "Currently enrolled in the Generative AI and Python Programming course at GIAIC, Karachi.",
            "Bachelor" : "First year student in Bs Data Science from Quaid-e-awam University Nawabshah."
        },
        "born" : "26-November-2003",
        "father_name" : "Ashraf ali",
        "surname" : "Rajput",
        "religion" : "Islam",
        "city" : "Live in Nawabshah",
        "Province" : "Sindh",
        "skills" : [
            "Python",
            "FastAPI",
            "Next.js",
            "Tailwind CSS",
            "Sanity CMS",
            "Streamlit",
            "Chainlit",
        ],
        "currently_learning" : "Agentic AI",
        "language" : ["Urdu","English"],
        "linkin_profile_link" : "www.linkedin.com/in/muhammad-daniyal-a626812ba",
        "email" : "daniyalashraf9790@gmail.com",
        "facebook" : "https://web.facebook.com/M.DANII97",
        "github": "https://github.com/Danii9790",
        "weekly_plan" : "Monday to Friday in university , Saturday - Some rest and Working on Learning and bulid Project , Sunday- Attend Class at Karachi  Governor Sindh It Initative for Artifical Intelligence and Computing .",

    }