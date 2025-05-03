import ollama
import os

model = "llama3.2"

# path of input and output pathh
input_file = "./data/grocessy_list.txt"
output_file = "./data/categorise_grocessy_list.txt"

#check the file exist or not
if not os.path.exists(input_file):
    print(f"Input file '{input_file}' not found.")


# Read the unrecognized items from the grocessry list
with open(input_file, "r") as f:
    items = f.read().strip()

#prepare the prompt for the model
prompt = f"""

You are an assistant that categorizes and sorts grocery items.

here is a list of grocery items:

{items}

Please:

1.	sort the items alphabatically within each category.
2.	Predict or assign the most relevant category (like Dairy, Meat, Vegetables, etc.)
3.	Optionally return it in a consistent format (e.g., key-value pair)

"""

# send the prompt and get the response
try:
    response = ollama.generate(model = model, prompt=prompt)
    generated_text = response.get("response", "")
    print("===== Categorized List: ===== \n")
    print(generated_text)

    #write the categorized list to the output file
    with open(output_file, "w") as f:
        f.write(generated_text.strip())

    print(f"Categorized grocery list has been saved to '{output_file}'.")
except Exception as e:
    print("An error occured:", str(e))