flag_dog = True
flag_cat = True

get_dog = False
get_cat = False

box_states = {}

questions = [{"question": "Which of the following is the correct way to create a dictionary in Python?", "options": ["A: dict1 = {1: 'a', 2: 'b', 3: 'c'}", "B: dict1 = (1: 'a', 2: 'b', 3: 'c') ", "C: dict1 = [1: 'a', 2: 'b', 3: 'c']", "D: dict1 = <1: 'a', 2: 'b', 3: 'c'>"], "answer": "A", "state": "False"},
             {"question": "How can you remove the first occurrence of an item from a list? ", "options": ["A: list.delete(item) ", "B: list.pop(item) ", "C: list.remove(item)", "D: list.discard(item)"], "answer": "C", "state": "False"},
             {"question": "What does the list.pop() method do? ", "options": ["A: Removes the last element from the list ", "B: Removes the first element from the list ", "C: Removes a specific element", "D: Returns a list of the popped elements"], "answer": "A", "state": "False"},
             {"question": "Which of the following can be used to remove duplicates from a list L = [1, 2, 2, 3, 4, 4, 5] ", "options": ["A: L.remove_duplicates() ", "B: L.pop_duplicates() ", "C: L.clear_duplicates() ", "D: list(set(L))"], "answer": "D", "state": "False"},
             {"question": "Which keyword is used to exit a loop in Python? ", "options": ["A: exit ", "B: break ", "C: continue ", "D: stop"], "answer": "B", "state": "False"},
             {"question": "What is the difference between a list and a tuple? ", "options": ["A: Tuples are mutable, lists are immutable ", "B: Tuples are immutable, lists are mutable ", "C: Both lists and tuples are mutable ", "D: Both lists and tuples are immutable"], "answer": "B", "state": "False"},
             {"question": "Which of the following operations will raise an error? ", "options": ["A: tuple1 = (1, 2, 3) ", "B: len(tuple1) ", "C: tuple1 = tuple1 + (4, 5) ", "D: tuple1[0] = 10"], "answer": "D", "state": "False"},
             {"question": "What will be the result of 3 == '3' in Python? ", "options": ["A: False ", "B: True ", "C: TypeError ", "D: SyntaxError"], "answer": "A", "state": "False"}
            ]

question_clues = [{"clue": "The cats and dogs in the village might know something……", "state": "False"},
             {"clue": "Be careful! There might be monsters in the box!", "state": "False"},
             {"clue": "There might be some clues in the village chief's house.", "state": "False"},
             {"clue": "Few days ago, someone saw the village chief hurrying toward the edge of the village.", "state": "False"},
             {"clue": "Open all the boxes, and something new will happen...", "state": "False"},
             {"clue": "someone saw the village chief being swept away by a tornado!", "state": "False"},
             {"clue": "There might be nothing in the box……", "state": "False"},
             {"clue": "You can only open the box once!", "state": "False"},
             {"clue": "If you want to see your pet, press the 'tab' key!", "state": "False"},
             {"clue": "Defeat the monsters! The warrior will receive a well-deserved reward!", "state": "False"},
             ]

get_clues = []

box_count = 0

flag_see = True

            