# - 절차

# 1. 블로그 글에서 텍스트 추출
# 2. 추출된 내용 60초 길이의 대본화
# 3. 한 소주제에 대응하는 이미지 생성
# 4. 나레이션 / 배경음 을 통한 편집

# 테스트할 Tistory 블로그 URL
from TistoryCrawler import TistoryCrawler


test_url = "https://giftedmbti.tistory.com/184"

# 블로그 크롤러 인스턴스 생성
crawler = TistoryCrawler(test_url)

content_title = crawler.title
print(content_title)

# 블로그 글 내용 출력
blog_content = crawler.content
print(blog_content)