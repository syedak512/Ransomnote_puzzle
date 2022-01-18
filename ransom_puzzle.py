def can_construct(ransomNote, magazine):
 # we have a function here that has the parameters ransomNote and magazine  
    if ransomNote == '':
        # If the ransomNote has an empty string
        return False
        # Return false because empty won't make anything
    if magazine == '':
        # if magazine is an empty string
        return False
        # Return false because empty won't make anything
    letters_counter = {} 
    # A dictionary to hold the characters of "magazine" and the number of time they occur
    for letter in magazine: 
    # loops through each character of "magazine"
        if letter in letters_counter:
        # If the current letter is in the letters_counter
            letters_counter[letter] += 1
            #than adds one and assigns it for its accurance
        else:
            #otherwise
            letters_counter[letter] = 1
            # Sets it counter to 1 because it's the first time
    for letter in ransomNote:
    # loops through each letter in ransomNote
        if letter not in letters_counter or letters_counter[letter] == 0:
        # if letter is not in dictionary or if the letter counter is zero because it was used up
            return False
            # returns False
        else:
            letters_counter[letter] -= 1
            # if letter is found, dictionary counter decreases
            return True
            # return true
if(can_construct('ransomNote','magazine')):
    print('true')
else:
    print('false')