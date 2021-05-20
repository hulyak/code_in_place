import random


def main():
    # 1. Understand how to create a list and add values
    # A list is an ordered collection of values
    names = ['Julie', 'Mehran', 'Simba', 'Ayesha']
    names.append('Karel')

    # 2. Understand how to loop over a list
    # Prints the list to the screen one value at a time
    for value in names:
        print(value)

    # 3. Understand how to look up the length of a list
    # Use randint to select a valid "index"
    max_index = len(names) - 1
    index = random.randint(0, max_index)

    # 4. Understand how to get a value by its index
    # Get the item at the chosen index
    correct_answer = names[index]

    # This is just like in Khansole Academy...
    # Prompt user for an answer and check whether correct or not
    prompt = 'Who is in index...' + str(index) + '? '
    answer = input(prompt)
    if answer == correct_answer:
        print('Good job')
    else:
        print('Correct answer was', correct_answer)


if __name__ == '__main__':
    main()
