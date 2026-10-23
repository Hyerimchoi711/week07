"""tools.py: 박스오피스 정보를 가져오는 도구 모음"""
import requests
from secret import API_KEY

BASE_URL = ("http://www.kobis.or.kr/kobisopenapi/webservice/"
            "rest/boxoffice/searchDailyBoxOfficeList.json")

def get_boxoffice_rank_1(date):
    """
    그 날짜의 박스오피스 1위 영화 제목을 입력한다

    받는 것: data(문자열) - 8자리 날짜 예: "20260824"
    돌려주는 것: (문자열) - 1위 영화 제목 예: "오디세이"
    """
    params = {"key": API_KEY, "targetDt": date}
    response = requests.get(BASE_URL, params=params, timeout=10)
    data = response.json()
    movies = data["boxOfficeResult"]["dailyBoxOfficeList"]
    return movies[0]["movieNm"]


def get_movie_audience(date, title):
    """
    그 날짜의 박스오피스에서 특정 영화의 관객 수를 가져온다

    받는 것:  date(문자열) - 8자리 날짜 예: "20260824"
            title(문자열) - 영화 제목 예: "오디세이"
    돌려주는 것: (문자열) - 관객 수 예: "123,456명"
    """
    params = {"key": API_KEY, "targetDt": date}
    response = requests.get(BASE_URL, params=params, timeout=10)
    data = response.json()
    movies = data["boxOfficeResult"]["dailyBoxOfficeList"]
    
    for movie in movies:
        if movie["movieNm"] == title:
            return f"{int(movie['audiCnt']):,}명"
    
    return f"'{title}'은 {date} 순위에 없습니다."  # 'title'은 date 순위에 없습니다. 형식으로 출력