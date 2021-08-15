from GPTJ.Basic_api import SimpleCompletion
AI_questions = []
while True:
# In the prompt enter something you want to generate
    prompt = "Question: What is the capital of france?\n\
        Question: Ludwig Van Beethoven was born in 1770 in which city?\n\
        Question: Who discovered penicillin?\n\
        Question: Which country invented tea?\n\
        Question: What was the first toy to be advertised on television? \n\
        Question: What are the names of Cinderella’s stepsisters?\n\
        Question:"

    # The maximum length of the output response
    max_length = 15

    # Temperature controls the creativity of the model
    # A low temperature means the model will take less changes when completing a prompt
    # A high temperature will make the model more creative
    # Both temperature and top probability most be a float

    temperature = 0.5

    # top probability is an alternative way to control the randomness of the model
    # If you are using top probability set temperature one
    # If you are using temperature set top probability to one
    top_probability = 1.0

    # Initializing the SimpleCompletion class
    # Here you set query equal to the desired values
    # Note values higher that 512 tend to take more time to generate
    query = SimpleCompletion(prompt, length=max_length,
                            t=temperature, top=top_probability)
    # Finally you assign a variable the function simple completion
    finalquery = query.simple_completion()
    AI_questions = finalquery.split("?")
    print(AI_questions[0])
    prompt = f"What is the capital of france?\n\
            Paris\n\
            Ludwig Van Beethoven was born in 1770 in which city?\n\
            Berlin.\n\
            Who discovered penicillin?\n\
            Fleming\n\
            Which country invented tea?\n\
            China\n\
            What was the first toy to be advertised on television?\n\
            Mr Potato Head\n\
            {AI_questions[0]}?\n"
    temperature = 0.3
    query = SimpleCompletion(prompt, length=max_length,
                            t=temperature, top=top_probability)
    # Finally you assign a variable the function simple completion
    answer = query.simple_completion()
