
class Question:
    def __init__(self, que, a, b, c, d, correct_answer):
        self.que = que
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.correct_answer = correct_answer

Questions = [
    # Turkish
    Question("Which sentence has a verb?", "Kedi masanin ustunde.", "Eve geç kaldım.", "Ali çok çalışkandır.", "Kalem masanın üstünde.", "b"),
    Question("Which one is a pronoun?", "Evim", "Sen", "Kalem", "Masa", "b"),
    Question("Which sentence uses an adjective?", "Hızlı koşan çocuk kazandı.", "Kitap okudu.", "Ali geldi.", "Oturdu.", "a"),
    Question("Which one is a noun?", "Güzel", "Sevgi", "Koşmak", "Kırmızı", "b"),
    Question("Which sentence uses a conjunction?", "Eve gittim ama onu bulamadım.", "Yemek yedik.", "Ali okula gitti.", "Kitabı aldım.", "a"),

    # Russian
    Question("Which word is a verb?", "Книга", "Бежать", "Красный", "Стол", "b"),
    Question("Which one is a noun?", "Читать", "Любовь", "Быстро", "Бежать", "b"),
    Question("Which one is a pronoun?", "Я", "Книга", "Бегать", "Красный", "a"),
    Question("Which sentence uses an adjective?", "Быстрая машина остановилась.", "Я читаю.", "Они идут.", "Книга лежит.", "a"),
    Question("Which sentence uses a conjunction?", "Я хотел уйти, но остался.", "Он пишет.", "Они сидят.", "Мы читаем.", "a"),

    # English
    Question("Which sentence contains a verb?", "The book is red.", "I run every day.", "The sky is blue.", "The cat is on the mat.", "b"),
    Question("Which one is a pronoun?", "House", "They", "Run", "Blue", "b"),
    Question("Which sentence uses an adjective?", "The fast car won the race.", "He is reading.", "She arrived.", "They slept.", "a"),
    Question("Which word is a noun?", "Happiness", "Quickly", "Run", "Beautiful", "a"),
    Question("Which sentence uses a conjunction?", "I wanted to go, but it rained.", "He ate dinner.", "She walked home.", "They played.", "a"),
    Question("Which word is an adverb?", "Quickly", "House", "Beautiful", "Run", "a"),
    Question("Which sentence uses a preposition?", "The cat is under the table.", "I will eat now.", "She is happy.","The book is blue.", "a"),
    Question("Which one is a determiner?", "The", "Run", "Beautiful", "Quickly", "a"),
    Question("Which word is a conjunction?", "And", "Happy", "Run", "House", "a"),
    Question("Which sentence contains a compound noun?", "My mother-in-law is kind.", "She runs fast.","The weather is great.", "I love reading.", "a"),
    Question("Which word is a verb in the past tense?", "Walked", "Walk", "Walking", "Walker", "a"),
    Question("Which sentence is in the future tense?", "I will go to the park.", "I am eating now.", "She went home.","They are running.", "a"),
    Question("Which word is a collective noun?", "Team", "Book", "Quickly", "Blue", "a"),
    Question("Which sentence contains a modal verb?", "You should study more.", "I like swimming.", "She is reading.","They are late.", "a"),
    Question("Which one is an interrogative sentence?", "Where are you going?", "I like apples.", "She is happy.","The cat is sleeping.", "a"),
    Question("Which word is a gerund?", "Swimming", "Swim", "Swam", "Swims", "a"),
    Question("Which sentence uses a passive voice?", "The cake was baked by Mary.", "She is baking a cake.","Mary bakes cakes.", "Mary is a baker.", "a"),
    Question("Which word is a superlative adjective?", "Biggest", "Big", "Bigger", "Bigly", "a"),
    Question("Which one is a synonym for 'happy'?", "Joyful", "Sad", "Angry", "Tired", "a"),
    Question("Which sentence uses a conditional clause?", "If it rains, we will stay home.", "I love pizza.","She is reading.", "They went outside.", "a"),

]
