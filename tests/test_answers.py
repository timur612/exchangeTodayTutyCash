import pytest

from app import get_answer
from nlu import NluService
from processor import Processor


@pytest.fixture()
def predictor() -> NluService:
    return NluService()


@pytest.fixture
def dispatcher() -> Processor:
    return Processor()


def test_echoing(predictor, dispatcher):
    text = "sample"
    excepted = text
    return excepted == get_answer(nlu=predictor, processor=dispatcher, text=text)
