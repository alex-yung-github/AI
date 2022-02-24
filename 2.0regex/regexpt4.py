import sys; args = sys.argv[1:]
idx = int(args[0])-60


myRegexLst = [
  r"/^(?!\d*010)[01]*$/",
  r"/^(?!\d*010|101)[01]+$/"
  


  
  
 ]

if idx < len(myRegexLst):
  print(myRegexLst[idx])

  # Alex Yung, 1, 2023