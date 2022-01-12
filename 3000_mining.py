import subprocess
import sys
import os
import csv

# Install required packages [Numpy, OpenAI]

try:
    import numpy as np
    import openai
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'numpy'])
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'openai'])
finally:
    import numpy as np
    import openai

# Import dataset
filename = 'data/1000popularwords.txt'
dataset = np.loadtxt(filename, delimiter=',', dtype=str)
print(dataset)

# OpenAI API key
openai.api_key = "#"

# Iterate over dataset and write each iteration to csv file
with open('data/does_1000.csv', 'w') as f1:
    # Dictionary writing
    fieldnames = ['prompt', 'output']
    writer=csv.DictWriter(f1, delimiter='\t',lineterminator='\n', fieldnames=fieldnames)
    
    # For x in 1000 word dataset, replace selected word with x
    for x in dataset:
        row = [x]

        response = openai.Completion.create(
        engine="davinci-codex",
        prompt="# Python 3 \ndef find_missing_number(nums):\n    i = 0\n    while i < len(nums):\n        j = nums[i]\n        if nums[i] < len(nums) and nums[i] != nums[j]:\n            nums[i], nums[j] = nums[j], nums[i]\n        else:\n            i += 1\n    for i in range(len(nums)):\n        if i != nums[i]:\n            return i\n    return len(nums)\n\n# Explanation of what the code {} in natural language one by one 1.\n#".format(x),
        temperature=0,
        max_tokens=210,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        
        codex_output = response["choices"][0]["text"].strip()

        writer.writerow({'prompt' : row, 'output' : codex_output})
        # Status of script
        print(x, 'completed')