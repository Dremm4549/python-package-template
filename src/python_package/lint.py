#lint.py 

import sys 

from pylint import lint  
from pylint.lint import Run

THRESHOLD = 9  

score = Run(["hello_world.py"], exit=False).linter.stats.global_note
print(score)
if score < THRESHOLD: 

    print("Linter failed: Score < threshold value") 

    sys.exit(1) 


sys.exit(0) 