import sys; args = sys.argv[1:]
idx = int(args[0])-40


myRegexLst = [
  r"/^[xo.]{64}$/i",
  r"/^[xo]*\.[xo]*$/i",
  r"/(^[x]+[o]*\.|\.[o]*[x]+$|^\.|\.$)/i",
  r"/^.(..)*$/is",
  r"/^(0([01]{2})*|1[01]([01]{2})*)$/i",
  r"/\b\w*(a[eiou]|e[aiou]|i[aeou]|o[aeiu]|u[aeio])\w*\b/mi",
  r"/^^(0*(10+)*1*)$/",
  r"/^\b[bc]*[a]?[bc]*$/",
  r"/^\b((([bc]*[a][bc]*){2})*|[bc]*)$/",
  r"/\b(([2]|(1[02]*1))[02]*)((1[02]*){2})*$/"
  
  
 ]

if idx < len(myRegexLst):
  print(myRegexLst[idx])

  # Alex Yung, 1, 2023