"""
Scoute Evaluator: It runs DeepEval metrics on Scoute's synthesizer output to assess faithfulness to it's retrieved sources and hallucination in the research report.
"""

from deepeval.metrics import HallucinationMetric, FaithfulnessMetric
from deepeval.test_case import LLMTestCase
from test_cases.scoute_cases import RESEARCH_TOPIC, RESEARCH_REPORT, RESEARCH_SOURCES

def evaluate_faithfulness() -> dict:
    """
    Evaluates whether Scoute's report stays faithful to its retrieved sources or not. Checks if the synthesizer fabricates claims not supported by the sources.

    Returns:
        dict: Metric name, score, and pass/fail result.
    """

    # Extracting contents of the sources as a list of strings for DeepEval
    retrieval_context = [source["content"] for source in RESEARCH_SOURCES]

    test_case = LLMTestCase(
        input=RESEARCH_TOPIC,
        actual_output=RESEARCH_REPORT,
        retrieval_context=retrieval_context
    )

    metric = FaithfulnessMetric(threshold=0.7)
    metric.measure(test_case)

    return{
        "metric": "Faithfulness",
        "score": metric.score,
        "passed": metric.score >= 0.7,
        "reason": metric.reason
    }

def evaluate_hallucination() -> dict:
    """
    Evaluates whether Scoute's report contains hallucinationated information not present in the original sources

    Returns:
        dict: Metric name, score, and pass/fail result.
    """

    retrieval_context = [source["content"] for source in RESEARCH_SOURCES]

    test_case = LLMTestCase(
        input=RESEARCH_TOPIC,
        actual_output=RESEARCH_REPORT,
        context=retrieval_context
    )

    metric = HallucinationMetric(threshold=0.5)
    metric.measure(test_case)

    return{
        "metric": "Hallucination",
        "score": metric.score,
        "passed": metric.score <= 0.5,
        "reason": metric.reason
    }

def run_scoute_evaluation() -> dict:
    """
    Runs all evaluations for Scoute and returns combined results.

    Returns:
        dict: Dictionary containing the results of all Scoute evaluations.
    """

    return {
        "project": "Scoute",
        "evaluations": [
            evaluate_faithfulness(),
            evaluate_hallucination()
        ]
    }

#Code for unit testing the evaluator
if __name__ == "__main__":
    results = run_scoute_evaluation()
    print(f"Project: {results['project']}")
    for eval in results['evaluations']:
        print(f"\nMetric: {eval['metric']}")
        print(f"Score: {eval['score']}")
        print(f"Passed: {eval['passed']}")
        print(f"Reason: {eval['reason']}")