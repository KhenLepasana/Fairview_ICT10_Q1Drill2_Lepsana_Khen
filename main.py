from pyscript import document, display

# runs when button is clicked
def generate_message(e):
    # Get values from input fields
    name = document.getElementById("Name").value
    age = document.getElementById("Age").value
    school = document.getElementById("School").value

    # Multiline string
    message = f'''👩‍🎓 Student Profile
\nName   : {name}\nAge    : {age} years old\n School: {school}\n\n📌 Notes:
{name} is currently {age} years old and is enrolled at {school}. This information was gathered through input fields and displayed using a multiline string in Python via PyScript.'''

    # Show the message inside the output box; used innerText for new lines to work
    document.getElementById("output").innerText = message
