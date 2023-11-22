text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# TODO
text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""
print(text.replace(',', '').replace('.', ''))

#  How I want a drink alcoholic of course after the heavy chapters involving quantum mechanics All of thy geometry Herr Planck is fairly hardが出力される
text = "How I want a drink alcoholic of course after the heavy chapters involving quantum mechanics All of thy geometry Herr Planck is fairly hard"
print(text.replace(' ', '", "'))
# How", "I", "want", "a", "drink", "alcoholic", "of", "course", "after", "the", "heavy", "chapters", "involving", "quantum", "mechanics", "All", "of", "thy", "geometry", "Herr", "Planck", "is", "fairly", "hardが出力される
text = "How", "I", "want", "a", "drink", "alcoholic", "of", "course", "after", "the", "heavy", "chapters", "involving", "quantum", "mechanics", "All", "of", "thy", "geometry", "Herr", "Planck", "is", "fairly", "hard"
list(map(len, text))
[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4]
t = "[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4]"
print(t.replace('[', '').replace(', ', '').replace(']', ''))
314159265358979323846264


  



  