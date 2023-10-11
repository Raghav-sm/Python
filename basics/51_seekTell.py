# ' iHaveNoIdeaHowThisWorks ' the txt in test2.txt
with open('test2.txt','r') as f: 
  f.seek(10)#Basically sets the pointer tp 10th position
  data = f.read(5)
  print(data) # aHowT o/p
with open('test2.tx','w') as b:
  b.write('Bagge bage billiya da ki karegi')
  bb = b.seek(11)
  bb = b.truncate(5)
with open('test2.tx','r') as b:
  bb = b.read()
  print(bb)
