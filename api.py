import openai
import sys
import nbformat
from nbconvert import PythonExporter

# Set your API key
openai.api_key = "Your_API-Key"

# Set the model to use
model_engine = "text-davinci-002"

# Set the prompt
prompt = input(": ") 
to_file = input("Send to file (Y/n) ")
# Set the number of completions
n = 1

# Set the temperature
temperature = 0.5

# Set the max length of the completion
max_tokens = 1024

# Set the top_p
top_p = 1

# Set the frequency penalty
frequency_penalty = 0

# Set the presence penalty
presence_penalty = 0

# Set the best_of
best_of = 1

# Set the stop
stop = None


completions = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    n=n,
    max_tokens=max_tokens,
    temperature=temperature,
    top_p=top_p,
    frequency_penalty=frequency_penalty,
    presence_penalty=presence_penalty,
    best_of=best_of,
    stop=stop
)

# Print the completions
for completion in completions.choices:
    if(to_file == "y" or to_file =="Y"):
        fname = input("Enter file name (e.g. result.pdf, answer.txt etc) ")
        with open(fname, "w") as f:
            f.write(str(completion.text))

    else:
        print(completion.text)
    

        
