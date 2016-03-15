def getchar(word, pos):
	if pos<0 or pos>=len(word): return None
	return word[pos]

def scan(text, transition_table, accept_states):

	pos = 0
	state = 's0'
	while True:
		curr_char = getchar(text,pos)
		if curr_char in transition_table[state]:
			state = transition_table[state][curr_char] # set new state
			pos += 1  # advance to next char
			# check if new state is accepting
			if state in accept_states:
				return accept_states[state],pos
		else:# no transition found
			return 'ERROR', pos
	



# the transition table, as a dictionary	
transition_t = {
		's0':{ '0':'s1', '1':'s4', '2':'s4','3':'s5', '4':'s2', '5':'s2','6':'s2', '7':'s2', '8':'s2','9':'s2' },

		's1':{ '1':'s2', '2':'s2', '3':'s2','4':'s2', '5':'s2', '6':'s2','7':'s2', '8':'s2', '9':'s2' },

		's2':{ '/':'s3', '-':'s3','.':'s3' },

		's3':{ '0':'s7', '1':'s6', '2':'s8','3':'s8', '4':'s8', '5':'s8','6':'s8', '7':'s8', '8':'s8','9':'s8' },

		's4':{ '0':'s2', '1':'s2', '2':'s2', '3':'s2', '4':'s2', '5':'s2','6':'s2', '7':'s2', '8':'s2','9':'s2','/':'s3','-':'s3','.':'s3'},

		's5':{ '0':'s2', '1':'s2','/':'s3','-':'s3','.':'s3' },

		's6':{ '0':'s8', '1':'s8', '2':'s8','/':'s9', '-':'s9','.':'s9' },

		's7':{ '1':'s8', '2':'s8', '3':'s8','4':'s8', '5':'s8', '6':'s8','7':'s8', '8':'s8', '9':'s8' },

		's8':{ '/':'s9', '-':'s9','.':'s9' },

		's9':{ '1':'s10', '2':'s11' },

		's10':{ '9':'s12' },

		's11':{ '0':'s12' },

		's12':{ '0':'s13', '1':'s13', '2':'s13','3':'s13', '4':'s13', '5':'s13','6':'s13', '7':'s13', '8':'s13','9':'s13'},

		's13':{ '0':'DATE', '1':'DATE', '2':'DATE','3':'DATE', '4':'DATE', '5':'DATE','6':'DATE', '7':'DATE', '8':'DATE','9':'DATE'}
}
# the dictionary of accepting state and their
# corresponding token
accept_states = {
	    'DATE': 'DATE_TOKEN'
}
# get a string from input	
word = raw_input('give a date>')

	
while len(word)>0:
        # get next token and position after last char recognized
	tok,pos = scan(word, transition_t, accept_states)
	if tok == 'ERROR':
		print ('unrecognized input at pos=',pos,'of',word)
		break
	print 'token...:', tok,',text:',word[:pos]
	# new text for next scan
	word = word[pos:]
