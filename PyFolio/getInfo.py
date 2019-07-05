import requests

headers = {'Authorization': 'Bearer {token}'}
r=requests.get("https://api.typeform.com/forms/rNBx3n/responses", headers=headers)

data = r.json()

totalAmount = data['total_items']

myAnswers = []
for i in range(totalAmount):
	try:
		ans = data['items'][i]['answers']
		myAnswers.append(ans)
	except KeyError as e:
		continue

for i in range(len(myAnswers)):
	for j in range(len(myAnswers[i])):
		theKey = myAnswers[i][j]['type']
		print(myAnswers[i][j][theKey])


