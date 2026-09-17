import requests

# Step 1: Create record
r1 = requests.post('http://localhost:8080/api/normal-records', json={
    'name': 'TestPhoto', 'age': 30,
    'campId': 'd9b26e72-803d-4558-82e7-ac7a251099c7',
    'campName': 'Camp Alpha', 'officerUid': 'test',
    'officerName': 'Test', 'officerContact': 'test@test.com',
    'status': 'AT_CAMP', 'additionalDetails': '',
    'foundAt': '2026-01-01T00:00:00'
})
record_id = r1.json()['id']
print(f'Step 1: Record created - {record_id}')

# Step 2: Upload photo
r2 = requests.post('http://localhost:8080/api/v1/images/normal',
    files={'file': ('test.jpg', open(r'C:\Users\Udaypratap Singh\StudioProjects\Aasha-Final\ai-service\tests\data\mask_black.jpg', 'rb'), 'image/jpeg')},
    data={'record_id': record_id}
)
print(f'Step 2: Upload - {r2.status_code} {r2.text[:200]}')

# Step 3: Check photo URL
r3 = requests.get(f'http://localhost:8080/api/normal-records/{record_id}')
photo_url = r3.json().get('photoUrl')
print(f'Step 3: photoUrl = {photo_url}')

# Step 4: Verify photo accessible
if photo_url:
    r4 = requests.get(f'http://localhost:8080{photo_url}')
    print(f'Step 4: Accessible - {r4.status_code} size={len(r4.content)}')
else:
    print('Step 4: NO URL')
