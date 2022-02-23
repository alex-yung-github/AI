import sys; args = sys.argv[1:]
idx = int(args[0])-30


myRegexLst = [
  r"/^10[10]$|^0$/",
  r"/^[01]*$/",
  r"/0$/",
  r"/\b\w*[aeiou]\w*[aeiou]\w*/mi",
  r"/^[^0a-z][01]*0$|^0$/i",
  r"/^[01]*110[01]*$/",
  r"/^[^/]{2,4}$/",
  r"/^\d{3} *-? *\d{2} *-? *\d{4}$/",
  r"/^.*?d.*?\b/im",
  r"/^1[01]*1$|^0[01]*0$|^$|^[01]$/i"
 ]

if idx < len(myRegexLst):
  print(myRegexLst[idx])

  # Alex Yung, 1, 2023