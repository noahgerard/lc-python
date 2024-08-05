def isAnagram(s, t):
	if len(s) != len(t):
		return False
	
	s_letters = {}

	for c in s:
		if c in s_letters:
			s_letters[c] += 1
		else:
			s_letters[c] = 1
	
	for c in t:
		if c in s_letters:
			s_letters[c] -= 1;
		else:
			return False
	
	for value in s_letters.values():
		if value != 0:
			return False
		
	return True

print(isAnagram("anagram", "nagaram"))