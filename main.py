friends = ['Chelsea Moreno',
 'Jessica Ritter',
 'Jessica Wilson',
 'Christina Tucker',
 'Stanley Jackson',
 'Christine Stout',
 'Lori Roberts',
 'Monique Johnson',
 'Penny Kline',
 'Jennifer Johnson',
 'Bill Adams',
 'Brenda Rosario',
 'Kimberly Ray',
 'Thomas West',
 'Joy Shaw',
 'Robert Briggs',
 'Angela Morrison',
 'Peter Phillips',
 'David Torres',
 'Kathryn Barnes']

print(friends)
JPgroup = [] 
for f in friends:
  if f[0] in ["J","P","j","p"]:
    JPgroup.append(f)
  
friend = "Joy Shaw"
def name_splitter(friend):
  for letter in friend:
    if letter == " ":
      space_index = friend.index(letter)
      
  return friend[:space_index], friend[space_index + 1:]

print(name_splitter("Charlie Brown"))


    
