import sys; args = sys.argv[1:]
idx = int(args[0])-50


myRegexLst = [
  r"/\w*(\w)\w*\1\w*/i",
  r"/\w*([\w])\w*\1\w*\1\w*\1\w*/i",
  
  
  
 ]

if idx < len(myRegexLst):
  print(myRegexLst[idx])

  # Alex Yung, 1, 2023