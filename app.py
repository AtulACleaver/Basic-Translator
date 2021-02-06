# Look what this will do:
"""
This will convert every vowel into 'b' you can easy do that
"""


def translate(phrase):
    # This is function variable to for the final output
    translation = ""
    for letter in phrase:
        # Now this if-else statement says if the letter in the phase given by the user is equal to either of the
        # letters "AEIOUaeiou" then exchange the letter with 'b'
        if letter in "AEIOUaeiou":
            translation = translation + "b"     # You can change it to what ever letter you want
        # What this will do that it will just write the whole text one by one if the digit is not a vowel...
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a phrase: ")))
