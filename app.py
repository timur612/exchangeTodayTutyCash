from nlu import NluService
from processor import Processor

cours = {"Ruble": 76,"Dollar":1,"Yen":104.73}

def get_answer(nlu: NluService, processor: Processor, text: str) -> str:
    prediction, original_text = nlu.predict(text)
    return processor.answer(intent=prediction, text=original_text)


def run(nlu: NluService, processor: Processor) -> None:
    text = input(
        "Привет, я простой бот, показывающий курс валют, напиши мне .\n"
        "Введите пустую строку [НАЗВАНИЕ ВАЛЮТЫ] к [НАЗВАНИЕ ВАЛЮТЫ] и я выведу курс!\n"
        "Если вас интересует сколько стоит X рублей в долларе, напишите N(число) Rub in Doll\n>"
    )
    while text:
        answer = get_answer(nlu, processor, text)
        answer = answer.lower()
        # query = input("Если вы хотите узнать курс 1 доллара к любой валюте напишите 1\n>"
        # "Если вы хотите узнать сколько в N рублях долларов, напишите 2")
        
        if "рубл" in answer and "доллар" in answer:
            print("Курс Доллара к Рублю:",cours["Dollar"],"=",cours["Ruble"])
        if "йен" in answer and "доллар" in answer:
            print("Курс Доллара к Японской Йене:",cours["Dollar"],"=",cours["Yen"])
        
        text = input("> ")
    print("Пока!")


if __name__ == '__main__':
    nlu = NluService()
    processor = Processor()
    run(nlu, processor)
