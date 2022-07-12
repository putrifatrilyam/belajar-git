import os

def make_commit(days : int):
    if days < 1:
      return os.system("git push")
    else:
        dates = f'{days} days ago'
        with open('README.md', 'a') as f:
            f.write(f'{dates}\n')
# stagging 
    os.system('git add .')
    os.system('git commit --date="'+dates+' -m "first message"')
    
    return days * make_commit(days - 1)

make_commit(7)