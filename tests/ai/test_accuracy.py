from dataclasses import dataclass

import pytest

deepeval = pytest.importorskip("deepeval")
from deepeval import assert_test
from deepeval.metrics import AnswerRelevancyMetric, GEval
from deepeval.test_case import LLMTestCase, LLMTestCaseParams


@dataclass(frozen=True)
class AccuracyCase:
    name: str
    question: str
    expected_answer: str
    threshold: float = 0.6
    tags: tuple[str, ...] = ()


CASES = [
    AccuracyCase(
        name="capital_of_france",
        question="What is the capital of France?",
        expected_answer="Paris",
        threshold=0.8,
        tags=("smoke",),
    ),
]


def _to_param(case: AccuracyCase):
    marks = [getattr(pytest.mark, tag) for tag in case.tags]
    return pytest.param(case, id=case.name, marks=marks)


@pytest.mark.ai
@pytest.mark.parametrize("case", [_to_param(case) for case in CASES])
def test_chatbot_accuracy(ai_client, system_prompt: str, case: AccuracyCase):
    response = ai_client.ask(system_prompt=system_prompt, question=case.question)

    test_case = LLMTestCase(
        input=case.question,
        actual_output=response,
        expected_output=case.expected_answer,
    )

    metrics = [
        AnswerRelevancyMetric(threshold=case.threshold),
        GEval(
            name="Factual Correctness",
            criteria="Determine whether the answer is factually correct and directly answers the question.",
            evaluation_params=[
                LLMTestCaseParams.INPUT,
                LLMTestCaseParams.ACTUAL_OUTPUT,
                LLMTestCaseParams.EXPECTED_OUTPUT,
            ],
            threshold=case.threshold,
        ),
    ]

    assert_test(test_case, metrics)
