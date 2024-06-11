from textwrap import dedent

from crewai import Task

from src.infra.ai.agents.social_media import social_media
from src.infra.ai.tasks.content_creation import content_creation_task

create_carousel_task = Task(
    description=dedent(
        """
        Please turn the following article written by Editor agent into a LinkedIn carousel post showcasing the main points, using a step-by-step approach with chapters and steps in each chapter. 
        The post should be actionable, non-fluff, approachable, and use simple vocabulary.
        Each slide should start with the step number and title, followed by bullet points for each substep inside the step. 
        Each substep should have an example that demonstrates the wrong and right way to do it, with these examples presented on separate slides.
        Please only leverage the prompts I share on my articles as the right example and create a wrong one that's lacking the essential things from the right example.
        Example:
            "Slide 2:
                Step 1: Create the Perfect Prompt
                - Remember: The quality of your input to chatGPT equals the output.
                - Use specific, tailored prompts for your newsletter content.
            Slide 3:
                Example (Wrong):
                - Prompt: "Create a newsletter."
            Slide 4:
                Example (Right):
                - Prompt: "Create a newsletter for ambitious founders, marketers, and salespeople who can spare only 5 minutes to read."
                
        Connect each slide fluently, ensuring the tone of voice is consistent throughout the carousel. 
        Highlight the reader's pain points and provide step-by-step solutions.‍    
        The first slide should include the title.
        The second slide should be a brief introduction to the carousel based on the article.
        The third slide should always include a concise 5 or fewer bullet points of what the reader will get from reading this post.
        it should look like this example:
        "Slide 3: By the end of this post, you will have:
            - [ ] A ready-to-use prompt to get SQL queries in no time.
            - [ ] Discovered how to create precise, clear prompts to make ChatGPT your new Data Expert.
            - [ ] Ended SQL struggles and time-consuming data analysis with the power of AI."
        
        The final four slides should include calls to action, no need for you to do them as I will use the same I have already ready every time.
        Use the AIDA framework (Attention, Interest, Desire, Action) to structure the content. 
        Use bullet points and emojis to enhance readability but avoid using hashtags. 
        Remember to keep the content engaging and easy to follow.
        Write 5 slides. Use bullet points and emojis to enhance readability but avoid using hashtags. 

        Your tone should be:
        -Actionable
        -Catchy
        -Non fluff
        -simple vocabulary (a 6th grader should understand it)
        Article:
        ---
        {context}
        ---
        Retorne o resultado em pt-br.
    """
    ),
    expected_output='An engaging post ready to be published on LinkedIn in pt-br',
    agent=social_media,
)

create_carousel_task.context = [content_creation_task]
