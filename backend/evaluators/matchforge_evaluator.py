"""
MatchForge Evaluator: It runs DeepEval metrics on MatchForge's skills analyzer and resume rewriter outputs to assess hallucination, faithfulness, and answer relevancy metrics.
"""

from deepeval.metrics import HallucinationMetric, AnswerRelevancyMetric
from deepeval.test_case import LLMTestCase
from test_cases.matchforge_cases import RESUME_TEXT, JOB_DESCRIPTION, SKILLS_GAP_OUTPUT, REWRITTEN_RESUME
from deepeval.models import GeminiModel
import time

gemini = GeminiModel(model="gemini-3.5-flash")

def evaluate_skills_analyzer() -> dict:
    """
    Evaluates MatchForge's skills analyzer for answer relevancy. Checks whether the skills gap analysis is relevant to the job description.

    Returns:
        dict: Metric name, score, and pass/fail result.
    """
    
    test_case = LLMTestCase(
        input=f"Resume: {RESUME_TEXT}\nJob Description: {JOB_DESCRIPTION}",
        actual_output=SKILLS_GAP_OUTPUT
    )

    metric = AnswerRelevancyMetric(threshold=0.7, model=gemini)
    metric.measure(test_case)

    return{
        "metric": "Answer Relevancy",
        "score": metric.score,
        "passed": metric.score >= 0.7,
        "reason": metric.reason
    }

def evaluate_resume_rewriter() -> dict:
    """
    Evaluates MatchForge's resume rewriter for hallucination. Checks if the rewritten resume contains only the information present in the original resume and does not fabricate any information.

    Returns:
        dict: Metric name, score, and pass/fail result.
    """

    test_case = LLMTestCase(
        input=RESUME_TEXT,
        actual_output=REWRITTEN_RESUME,
        context=[RESUME_TEXT]
    )

    metric = HallucinationMetric(threshold=0.5, model=gemini)
    metric.measure(test_case)

    return{
        "metric": "Hallucination",
        "score": metric.score,
        "passed": metric.score <= 0.5,
        "reason": metric.reason
    }

def run_matchforge_evaluation() -> dict:
    """
    Runs all evaluations for MatchForge and returns combined results.

    Returns:
        dict: Dictionary containing the results of all MatchForge evaluations.
    """
    
    results = []
    results.append(evaluate_skills_analyzer())
    time.sleep(15)  # wait 15 seconds between metrics
    results.append(evaluate_resume_rewriter())
    return {
        "project": "MatchForge",
        "evaluations": results
    }

#Code for unit testing the evaluator
if __name__ == "__main__":
    results = run_matchforge_evaluation()
    print(f"Project: {results['project']}")
    for eval in results['evaluations']:
        print(f"\nMetric: {eval['metric']}")
        print(f"Score: {eval['score']}")
        print(f"Passed: {eval['passed']}")
        print(f"Reason: {eval['reason']}")