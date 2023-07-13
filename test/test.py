import requests

def get_lat_lng(address):
    url = "https://dapi.kakao.com/v2/local/search/address.json"
    headers = {
        "Authorization": "dfaaa8c3a89330253639482c63a0eb80"
    }

    params = {
        "query": address
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    if 'documents' in data:
        if len(data['documents']) > 0:
            latitude = data['documents'][0]['y']
            longitude = data['documents'][0]['x']
            return latitude, longitude

    return None, None

# 예시 주소
address = "서울특별시 강남구 역삼동 123-45"

latitude, longitude = get_lat_lng(address)

if latitude and longitude:
    print("위도:", latitude)
    print("경도:", longitude)
else:
    print("주소를 찾을 수 없습니다.")

