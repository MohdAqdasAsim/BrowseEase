import webbrowser,sys,json,os

script_dir = os.path.dirname(os.path.realpath(__file__))

json_file_custom = os.path.join(script_dir, 'custom-search-operators.json')
json_file_google = os.path.join(script_dir, 'google-search-operators.json')

args = sys.argv[1:]

with open(json_file_custom, 'r', encoding='utf-8') as file_custom:
    custom_operators_data = json.load(file_custom)

with open(json_file_google, 'r', encoding='utf-8') as file_google:
    google_operators_data = json.load(file_google)

if(len(args) == 0):
  print('What do you want to search?\nFor example, try \'search youtube\' or try \'search --help\'')
elif args[0] in ["--help", "-h", "--h", "-help"]:
  for operator in custom_operators_data:
    print(f"{operator['term']} = {operator['use']}\nExample = {operator['example']}\n")
  print('################################################################################\n')
  for operator in google_operators_data:
    print(f"{operator['term']} = {operator['use']}\nExample = {operator['example']}\n")
elif(args[0] in ["-y","--y","-Y","--Y"]):
  searchURL = 'https://www.youtube.com/results?search_query='+'+'.join(map(str,sys.argv[2:]))
  webbrowser.open(searchURL)
elif args[0] in ["/","\\"]:
  searchURL = 'https://www.google.com/search?q='+' '.join(map(str,sys.argv[2:]))
  webbrowser.open_new(searchURL)
elif(args[0] == "!"):
  searchURL = ' '.join(map(str,sys.argv[2:]))
  webbrowser.open(searchURL)
else:
  searchURL = 'https://www.google.com/search?q='+' '.join(map(str,sys.argv[1:]))
  webbrowser.open(searchURL)
