# Prompt engineering for initializing learning modules:


SYSMTEM_MESSAGE = """
You are an expert programming and coding teacher, based on the contexts provided above answer the questions provided.
Always use best practices and try and give the most elegant solutions and simple explanations of underlying concepts.

You may use general python knowledge outside of the context contained in the standard library. 
However, clearly state that something is not within the context if doing so.

STUDENT / Development CONTEXT:
- Student has intermediate level understanding of Python itself and installing the library, therefore skip suggesting learning basic python for any module.
- Please provide responses in Markdown unless specified otherwise.
"""


####### define functions to generate various prompts:

def overview_prompt(library_name):
    """
    overview_prompt(library_name):
    - Generates a overview prompt given the library name
    """
    response_str = f"""

Please write me an overview of {library_name}. Why it is useful, and what are the common real world use caess and examples.
Please separate the answer in two sections overview and real world examples, the first section is the overview, the second section with bullet points of a maximum of two sentences each.
Keep the overivew short, in one paragraph.
The two sections MUST be divided by 20 '&' symbols as a divider, this is important.
"""
    return response_str


def real_world_example_prompt(library_name, examples):
    """
    
    """
    response_str = f"""
For each bullet point examples of {library_name} provided below, please give me code examples for each that leverages {library_name}.
{examples}
"""
    return response_str


def improve_code_prompt(library_name, sample_code):

    response_str = f"""
The below code are example usages of using {library_name}, for each snippet assess the code below and see if they can be improved in any way:
{sample_code}
"""
    return response_str



