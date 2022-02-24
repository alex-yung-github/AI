import sys; args = sys.argv[1:]
idx = int(args[0])-60


myRegexLst = [
  r"/^(?!\d*010)[01]*$/",
  r"/^(?!\d*010|101)[01]*$/",
  r"/^([01])[01]*\1$|^[01]$/",
  r"/\b((\w)(?!\w*\2\b))+\b/i"
  


  
  
 ]

if idx < len(myRegexLst):
  print(myRegexLst[idx])

  # Alex Yung, 1, 2023