import random


next_id = 0


class Question:
    def __init__(self, content, answer_notes):
        global next_id
        self.id = next_id
        next_id += 1

        self.content = content
        self.answer_notes = answer_notes


QUESTIONS = {
    "far east": {
        "zen": [
            Question(
                "What is zen buddhism?",
                [
                    "zazen meditation",
                    "satori (awakening)",
                    "its attitudes to scripture and transmission of wisdom",
                    "the Rinzai and Soto schools",
                ],
            ),
            Question(
                "What is satori?",
                ["Zen Buddhism", "awakening"],
            ),
            Question(
                "What is zazen meditation?",
                ["Zen Buddhism", "satori (awakening)"],
            ),
            Question(
                "Compare the Rinzai and Soto schools of Zen Buddhism.",
                ["satori (awakening)"],
            ),
            Question(
                "Discuss the implications of Zen Buddhism's rejection of theory, ritual, and the use of language to express truth.",
                [],
            ),
        ],
        "pure land": [
            Question(
                "What is Pure Land Buddhism?",
                [
                    "Amitabha",
                    "rebirth in a Pure Land",
                    "chanting",
                    "Jōdo-shū and Jōdo Shinshū",
                ],
            ),
            Question(
                "What is Amitabha?",
                ["Pure Land Buddhism"],
            ),
            Question(
                "Discuss the importance and purpose of chanting in Pure Land Buddhism.",
                [],
            ),
            Question(
                "Compare Jōdo-shū and Jōdo Shinshū.",
                ["Pure Land Buddhism"],
            ),
            Question(
                "Is Pure Land Buddhism an 'easy' path?",
                [],
            ),
            Question(
                "How can Siddhartha's original teachings be seen in Zen and Pure Land Buddhism?",
                [],
            ),
        ],
    },
    "engaged": {
        "engaged": [
            Question(
                "What is engaged Buddhism?",
                [
                    "its origins",
                    "its aims",
                    "the ideas of Thich Nhat Hanh",
                    "the Fourteen Precepts",
                ],
            ),
            Question(
                "What are the ideas of Thich Nhat Hanh, and the Fourteen Precepts?",
                ["engaged Buddhism"],
            ),
            Question(
                "Should engaged Buddhism be a central part of the Buddhism path?",
                [],
            ),
            Question(
                "How does engaged Buddhism affect the stereotypical view of Buddhism as inward-looking?",
                [
                    "activism",
                    "opposition to social injustice",
                    "environmental awareness",
                ],
            ),
        ],
        "activism": [
            Question(
                "Why might activism be important in Buddhist practice?",
                ["engaged Buddhism"],
            ),
            Question(
                "Discuss engaged Buddhist views on environmental issues.",
                [],
            ),
            Question(
                "Discuss engaged Buddhist views on social injustice issues.",
                [],
            ),
            Question(
                "Could a Buddhist ever support war?",
                ["engaged Buddhism"],
            ),
        ],
    },
    "gender": {
        "awakening": [
            Question(
                "Discuss the theoretical and practical possibility of women attaining awakening in Buddhism.",
                [
                    "the Theravada and Mahayana schools",
                    "The Dragon King's Daughter",
                    "different societal/cultural contexts around the world",
                ],
            ),
            Question(
                "What are the Theravada and Mahayana schools of Buddhism?",
                ["views on gender"],
            ),
            Question(
                "What is the Sakyadhita International Association of Buddhist Women?",
                [],
            ),
        ],
        "monks": [
            Question(
                "Can women become monks?",
                [
                    "gurudharma (specific monastic rules for women)",
                    "the Theravadin tradition",
                    "the 'eight precept women'",
                    "Mahayana female monastic traditions",
                    "differing status of women in Buddhism in different societies (e.g. Thailand, Myanmar/Burma)",
                ],
            ),
            Question(
                "Discuss the difficulty of ordaining women in the Theravadin tradition.",
                [],
            ),
            Question(
                "Compare the status of female monks in different countries/societies.",
                [],
            ),
        ],
    },
}

REWARDS = [
    "eat a cookie",
    "watch a 5 minute video",
    "watch https://youtu.be/dQw4w9WgXcQ",
]


def get_question(valid_ids):
    while True:
        category = random.choice(list(QUESTIONS.keys()))
        sub = random.choice(list(QUESTIONS[category].keys()))
        question = random.choice(QUESTIONS[category][sub])

        if question.id in valid_ids:
            valid_ids.remove(question.id)
            return question


valid_ids = list(range(next_id))
while valid_ids:
    question = get_question(valid_ids)

    print(question.content)
    input("\nPress ENTER when you are finished...")

    if question.answer_notes:
        print("\nDid you talk about:")
        for note in question.answer_notes:
            print("- " + note)
    else:
        print("\n(ngl bestie idk what you were supposed to say for this one)")
    print("\nDid you get it right? " + random.choice(REWARDS) + " if so <3\n")
    print("=====\n")
print("well done!! that's all i could come up w")
