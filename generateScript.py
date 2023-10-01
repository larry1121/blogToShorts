import openai
from config import *
openai.api_key = OPENAI_API_KEY


# summary_list = [{'role': 'system', 'content': 'You are a helpful assistant for summarizing books.'}, {'role': 'user', 'content': "The Indian village has often been portrayed as a closed and isolated system, but recent studies show that this is not true. Contrary to the depiction of the Indian village as a self-sufficient republic, it has always had links with the wider society, such as migration, trade, administrative connections, inter-village economic and caste links, and religious pilgrimage. The concept of a village in India for government purposes is defined in terms of revenue, and the determinants of rural social formation include geographic, social, and cultural environments. India's rural social structure is shaped by its ancient civilization, and while there have been periods of urbanization, the Indian village has always been connected to the wider society."}, {'role': 'user', 'content': 'This passage discusses the economic, social, religious, and political structures of Indian villages. The economic structure has shifted from being self-sufficient to being part of a wider economic network due to industrialisation and urbanisation. The social structure is based on caste and kinship, with vertical interdependence among castes and horizontal ties of caste and kinship. The religious structure shows a double process of interaction between local and all-India Hinduism, with the spread of Sanskritic elements through technology such as railways and media. The political structure was described by British administrators in the 19th century.'}]
summary_list = [{'role': 'system', 'content': 'You are a helpful assistant for summarizing books.'}, {'role': 'user', 'content': 'The Indian village was once portrayed as a "closed" and "isolated" system by British administrator Charles Metcalf. However, recent studies suggest that Indian villages were never self-sufficient and had connections with wider society, including migration, trade, and religious pilgrimages. For government purposes, a village is defined as a revenue village with surveyed boundaries, and rural social life is determined by factors such as geographic and cultural environments, as well as social stratification and mobility. India has an ancient civilization that dates back to the Indus valley civilization and has a complex rural social structure influenced by various factors.'}, {'role': 'user', 'content': 'The article discusses the economic, social, and religious aspects of Indian villages. The villages were not economically self-sufficient even in British times and have been affected by industrialization and urbanization. Villagers have horizontal ties of caste and kinship that extend beyond the village to other villages and even towns. Intra-caste relations and caste matters are regulated by a caste panchayat whose members belong to different villages. The spread of Sanskritic theological ideas increased during British rule and after, due to the development of communications and spread of literacy. Western technology has helped the spread of Sanskritization. The article also discusses the political system of Indian villages.'}]

def generateScript():
    global script_ko

    summary_list.append({
        'role': 'user',
        'content': '위 문장들을 60초 발표 분량으로 요약해줘'
    })


    res = openai.ChatCompletion.create(
        # model='gpt-4',
        model='gpt-3.5-turbo',
        messages=summary_list
    )

    script = res['choices'][0]['message']['content']

    print(script)


    messages = [{
        'role': 'system',
        'content': 'You are a helpful assistant for summarizing and translating books.'
    }, {
        'role': 'user',
        'content': f'한국어로 번역해줘: {script}'
    }]

    res = openai.ChatCompletion.create(
        # model='gpt-4',
        model='gpt-3.5-turbo',
        messages=messages
    )

    script_ko = res['choices'][0]['message']['content']

    print(script_ko)

    # script_ko = "이 문장은 영국의 식민지 시절에 인도 농촌 주변의 신화와 편견에 대한 도전으로, 인도 농촌은 항상 넓은 사회와 연결되어 있었으며 지리적, 사회적, 문화적 환경 에 의해 형성되어, 계급 간 상호의존성과 다른 마을 및 도시와의 친족 관계에 반영되는 지방 사회 생활이 형성되고 있습니다. 농촌은 경제적으로 자급자족하지 않 으며, 넓은 경제적 네트워크의 일부가 되었습니다. 인도 농촌의 정치 체제는 19세기 초 영국 행정 관리자들에 의해 설명되었으며, 사상 기술과 커뮤니케이션의 발 전으로 인해 생상교의 확산이 증가하였습니다. 궁극적으로, 이 글은 식민지 시대의 고정관념에 도전하며, 인도 농촌 생활에 대한 세부적인 이해를 제공합니다."

    return script_ko

script_ko = generateScript()
print(script_ko)

# script_ko = "이 글은 인도 마을의 경제, 사회, 종교 및 정치 구조를 포함한 다양한 측면을 탐구한다. 이전에는 인도 마을이 자급자족이라는 믿음이 있었지만 최근 연구는 이들이 이주, 무역, 종교적 순례를 비롯한 보다 광범위한 사회와의 관계를 갖는다는 점을 강조한다. 마을 주민들은 소계와 계급에 기반한 수평적인 관계와 마을을 넘어 확장되는 친족관계를 가지며, 계급 판차야트에 의해 규제되며, 사회 계층화와 이동성과 같은 요인의 영향을 받는다. 사스크리트 신학 아이디어도 의사소통과 문맹율의 발전 때문에 전파되고 있다. 전반적으로, 인도 마을은 지리적 및 문화적 환경을 비롯한 다양한 요인에 영향을 받은 복잡한 농촌 사회 구조를 가지고 있다."