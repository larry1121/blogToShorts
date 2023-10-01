import re
from tqdm import tqdm
import openai
import fitz # pip install --upgrade pymupdf or pip install PyMuPDF
import time


def summary():
    global summary_list

    openai.api_key = 'sk-본인의 openai API키를 입력해주세요'

    ############### pdf to text #############################
    book_path = 'paper_list/001.pdf'

    doc = fitz.open(book_path)
    #########################################################

    start_pno = 0
    summarize_every = 1
    summary_list = [{
        'role': 'system',
        'content': 'You are a helpful assistant for summarizing blog article.'
    }]

    count = 0
    content = ''

    for pno in tqdm(range(start_pno, doc.page_count)):
        text = doc.get_page_text(pno=pno)
        # Preprocess text
        text = re.sub(r"\s+", " ", text)
        text = text.replace('THIRD CONCEPT, NOVEMBER 2020', '').strip()
        text = ' '.join(text.split(' ')[1:])

        if count == summarize_every:
            messages = [{
                'role': 'system',
                'content': 'You are a helpful assistant for summarizing blog article.'
            }, {
                'role': 'user',
                'content': f'Summarize this: {content}'
            }]
            # chatGPT3.5 사용시
            res = openai.ChatCompletion.create(
                model='gpt-3.5-turbo',
                messages=messages
                )
            print(res,"++++++++++++++++++++++++++++ 6")

            msg = res['choices'][0]['message']['content']
            print(msg,"++++++++++++++++++++++++++++ 7")

            summary_list.append({
                'role': 'user',
                'content': msg
            })
            count = 0
            content = ''
        else:
            content += text + ' '
            count += 1
        time.sleep(3)
    return summary_list
    
summary()