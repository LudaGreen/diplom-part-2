import request


#Людмила Гринчук, 18-я когорта "Дипломный проект 2-я часть, инженер по тестированию плюс"
# Тест проверки создания заказа
def test_order_creation():
    creation_response = request.post_new_order()
    track_id = creation_response.json()['track']
    response = request.get_orders_track(track_id)
    assert response.status_code == 200
