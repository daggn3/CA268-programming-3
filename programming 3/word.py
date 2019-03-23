vowels ="aeiou"
es_endings "ch", "sh", "x", "s", "z", "o"


def get_plural(word):

	if word[-2:] in es_endings or word[-1:] in es_endings:
		return(word + "es" )

	elif word[-2] not in vowels and s[-1] == "y":
		return(word[:-1] + "ies")

	elif word [-2] = "fe":
		return (word [:-2] + "ves")

	elif word[-1] = "f":
		return (word [:-1] + "ves")

	

	else:
		return (word + "s")