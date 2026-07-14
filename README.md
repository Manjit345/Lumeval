# Lumeval

## Overview
I have made a few LLM based applications and as I was learning about AI agents and LLMs, I kept hearing about the issue of hallucinations and lack of reliability in LLM generated text. So, I decided to make a evaluation application to test LLM based projects. Lumeval is a dashboard that evaluates LLM based applications using DeepEval metrics to verify that they actually work correctly.

## Projects Evaluated

### MatchForge
It is an AI powered job application agent which takes your resume and a job description and identifies the skills gap. It also rewrites the resume if the user approves to match the job description. Click [here](https://github.com/Manjit345/MatchForge) to check out the Github repo.
- **Answer Relevancy** — Checks whether the skills gap analysis produced by the skills analyzer is actually relevant to the provided job description and resume, ensuring the output addresses what was asked.
- **Hallucination** — Checks whether the rewritten resume contains any fabricated skills, experience, or qualifications not present in the original resume.

### Scoute
It is AI powered research agent which lets you look for any topic and get detailed information about it in a well structured format along with the sources it cited the report from. Click [here](https://github.com/Manjit345/Scoute) to check out the Github repo.
- **Faithfulness** — Checks whether the synthesized research report stays faithful to the sources retrieved during the search, ensuring no claims are made beyond what the sources actually say.
- **Hallucination** — Checks whether the research report contains any fabricated information that contradicts or is absent from the retrieved source content.

### Evaluation Results
| Project | Metric | Score | Status |
|---------|--------|-------|--------|
| MatchForge | Answer Relevancy | 1.0 | ✅ Passed |
| MatchForge | Hallucination | 0.0 | ✅ Passed |
| Scoute | Faithfulness | 1.0 | ✅ Passed |
| Scoute | Hallucination | 0.0 | ✅ Passed |

## Tech Stack
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![DeepEval](https://img.shields.io/badge/DeepEval-000000?style=for-the-badge&logo=testinglibrary&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white)

## Architecture
The app follows a simple client-server architecture. The backend is built using FastAPI and is responsible for running the evaluations. The frontend is built using React and is responsible for displaying the results in the form of a dashboard.

## How to Run

### Live Demo
[Lumeval](https://lumeval.vercel.app)

### Local Setup

**Backend:**
1. Navigate to backend: `cd backend`
2. Create virtual environment: `uv venv`
3. Activate: `source .venv/Scripts/activate`
4. Install dependencies: `uv sync`
5. Create `.env` with your key: `GOOGLE_API_KEY=your_key_here`
6. Run: `python main.py`

**Frontend:**
1. Navigate to frontend: `cd frontend`
2. Install dependencies: `npm install`
3. Run: `npm run dev`

## Project Structure
```
lumeval/
├── backend/
│   ├── main.py                        # FastAPI server with evaluation endpoints
│   ├── evaluators/
│   │   ├── matchforge_evaluator.py    # DeepEval metrics for MatchForge
│   │   └── scoute_evaluator.py        # DeepEval metrics for Scoute
│   └── test_cases/
│       ├── matchforge_cases.py        # Sample inputs and outputs for MatchForge
│       └── scoute_cases.py            # Sample inputs and outputs for Scoute
└── frontend/
    └── src/
        ├── App.jsx                    # Main dashboard with sidebar and metric cards
        └── components/
            └── MetricCard.jsx         # Reusable metric display component
```

## Notes

### Judge Model
The Gemini 3.5 Flash model is used as the LLM judge which evaluates the metrics for my projects. Since my other projects also use the same model, there could be a possibility of self evaluation bias as Gemini might recognize it's own answering or generation style and might give it a higher score than it deserves.

### Cross-Model Evaluation Attempt
In order to reduce self-evaluation bias, Groq's Llama 3.3 70B and Llama 3.1 8B were tested as
alternative judge models via LiteLLM. Both of them failed due to incompatibility between DeepEval's internal JSON tool call format and Groq's strict schema enforcement. Cross-model evaluation remains a planned future improvement.

### API Usage
This project is a demo and runs on the Gemini's free tier which has got a daily request limit. If the limit of the live demo is exhausted, then it will throw an error asking you to try again later.

## Future Improvements
- Cross-model evaluations with other models
- Evaluate additional projects as I keep making more
- Add historical score tracking to monitor evaluation drift over time

## License
This project is open-source and available under the MIT License.

## Contact
For issues or questions, please open a GitHub issue.