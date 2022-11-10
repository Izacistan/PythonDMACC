def score_input(test_name, test_score = -1, invalid_message="Invalid test score!"):
    #Get test_score and verify(Optional)
    scores = test_score
    while True:
        if scores == str(scores):
            raise ValueError("ValueError encountered!")
            break
        elif scores > 100 or scores < 1:
            return(test_name, invalid_message)
            break
        else:
            return(test_name, scores)


display_string = score_input("Test 1: ", 70)
print(display_string)

display_string = score_input("Test 2: ", 0)
print(display_string)

display_string = score_input("Test 3", 101)
print(display_string)

display_string = score_input("Test 4", "ABC")
print(display_string)