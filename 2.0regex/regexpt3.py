import sys; args = sys.argv[1:]
idx = int(args[0])-50


myRegexLst = [
  r"/\w*(\w)\w*\1\w*/i",
  r"/\w*([\w])\w*(\1\w*){3}/i",
  r"/^([01])[01]*\1$|^[01]?$/i",
  r"/\b(?=\w*cat)\w{6}\b/i",
  r"/\b(?=\w*bri)(?=\w*ing)\w{5,9}\b/i",
  r"/\b(?!\w*cat)\w{6}\b/i",
  r"/\b((\w)(?!\w*\2))+\b/im",
  r"/^(?!\d*10011)[01]+$|^$/i",
  r"/\w*([aeiou])(?!\1)[aeiou]\w*/i",
  r"/^(?!\d*(101|111))[01]+$|^$/i"
  


  
  
 ]

if idx < len(myRegexLst):
  print(myRegexLst[idx])

  # Alex Yung, 1, 2023