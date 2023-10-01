from tqdm import tqdm
import openai
import urllib
import os
from config import *
openai.api_key = OPENAI_API_KEY

summary_list = [{'role': 'system', 'content': 'You are a helpful assistant for summarizing books.'}, {'role': 'user', 'content': 'The Indian village was once portrayed as a "closed" and "isolated" system by British administrator Charles Metcalf. However, recent studies suggest that Indian villages were never self-sufficient and had connections with wider society, including migration, trade, and religious pilgrimages. For government purposes, a village is defined as a revenue village with surveyed boundaries, and rural social life is determined by factors such as geographic and cultural environments, as well as social stratification and mobility. India has an ancient civilization that dates back to the Indus valley civilization and has a complex rural social structure influenced by various factors.'}, {'role': 'user', 'content': 'The article discusses the economic, social, and religious aspects of Indian villages. The villages were not economically self-sufficient even in British times and have been affected by industrialization and urbanization. Villagers have horizontal ties of caste and kinship that extend beyond the village to other villages and even towns. Intra-caste relations and caste matters are regulated by a caste panchayat whose members belong to different villages. The spread of Sanskritic theological ideas increased during British rule and after, due to the development of communications and spread of literacy. Western technology has helped the spread of Sanskritization. The article also discusses the political system of Indian villages.'}]

def generateImage():

    os.makedirs('temp2', exist_ok=True)

    for i, summary in tqdm(enumerate(summary_list)):
        if summary['role'] != 'user':
            continue

        res_img = openai.Image.create(
            prompt=f'book illustration, {summary["content"][-390:]}',
            n=1,
            size='512x512'
        )

        img_url = res_img['data'][0]['url']
        img_path = f'temp2/{str(i).zfill(3)}.png'

        urllib.request.urlretrieve(img_url, img_path) # img_url url의 이미지를 img_path 경로에 저장하라
    
generateImage()