import random
import time
import hashlib
import itertools
from IPython.display import Image, display, clear_output
from ipywidgets import widgets, Layout
from IPython.display import HTML
from ipywidgets import TwoByTwoLayout

#TO GENERATE SOLUTION
#import hashlib
#hashlib.md5('soln_str'.encode()).hexdigest()

def si330_lab_questions(prob_no):    
                
    def create_textinputquiz_widget(description, text_description, correct_answer, a2, hint): ##grid for option table
        correct_answer = correct_answer ##float ##str   
        alternativ = widgets.Text(value = '',
                                 placeholder = '',
                                 description = '',
                                 disabled = False, layout=Layout(width = 'auto'))
        ##question description
        description_out = widgets.Output(layout=Layout(width='auto')) 
        with description_out:
            print(description)
        ##description before text widget    
        text_description_out = widgets.Output(layout=Layout(width='auto'))  
        with text_description_out:
            print (text_description)
        ##description after text widget e.g. units        
        a2_out = widgets.Output(layout=Layout(width='auto'))  
        with a2_out:
            print(a2)        

        feedback_out = widgets.Output()

        def check_selection(b):
            a = hashlib.md5(alternativ.value.encode()).hexdigest()
            if a==correct_answer:
                s = '\x1b[6;30;42m' + " Correct! " + '\x1b[0m' +"\n" #green color
            else:
                s = '\x1b[5;30;41m' + " Incorrect. Please try again. " + '\x1b[0m' +"\n" #red color
            with feedback_out:
                feedback_out.clear_output()
                print(s)
            return

        check = widgets.Button(description="check")
        check.on_click(check_selection)


        return widgets.VBox([description_out,
                             widgets.HBox([text_description_out, alternativ, a2_out]), 
                             widgets.HBox([check]), feedback_out], 
                            layout=Layout(display='flex',
                                         flex_flow='column',
                                         align_items='stretch',
                                         width='auto'))

    num_questions = 2
    choices = 'ABCDE'
    solution_hash = 'f85b7b377112c272bc87f3e73f10508d'
    question_text = [
        """Given the dataframes/series above, match each output to the correct code. Your answer should be a 8 char. string like 'ABCDEDCB' (where A corresponds to 1, B -> 2, etc.). Some answer choices may be used more than once.
        
        1     df[['Rupees (Buy)', 'Rupees (Sell)']].apply(price_markup, axis=0)
        2     df[['Rupees (Buy)', 'Rupees (Sell)']].apply(price_markup, axis=1)
        3     df[['Rupees (Buy)', 'Rupees (Sell)']].apply(price_markup)
        4     df[['Rupees (Buy)', 'Rupees (Sell)']].apply(price_markdown_sell, axis=1)
        5     df[['Rupees (Buy)', 'Rupees (Sell)']].apply(price_markdown_buy, axis=1)
        6     df[['Rupees (Buy)', 'Rupees (Sell)']].apply(price_markdown_buy, axis=0)
        7     df['Rupees (Buy)'].apply(price_markdown)
        8     df['Rupees (Buy)'].apply(price_markdown, axis=1)  
        """
    ]

    
    answers = ['8edc636404609482be57e44feaa7452f']
    
    return create_textinputquiz_widget(question_text[prob_no], "Answer: ", answers[prob_no], "(no spaces, ALL CAPS!)", "")