from flask import Flask, render_template
import requests
app = Flask(__name__)
 
@app.route("/")
def index():
	headers = {'Authorization': 'Bearer (paste the api key here,remove parentheses)'}
	r=requests.get("https://api.typeform.com/forms/(paste the form is here, remove the parentheses)/responses", headers=headers)
	data = r.json()

	totalAmount = data['total_items']

	myAnswers = []
	for i in range(totalAmount):
		try:
			ans = data['items'][i]['answers']
			myAnswers.append(ans)
		except KeyError as e:
			continue
			#list of list containing all the responses
	profile = list()
	#goes through each response 
	for i in range(1):
		#goes through data of each response
		for j in range(len(myAnswers[i])):
			theKey = myAnswers[i][j]['type']
			field = myAnswers[i][j][theKey]
			profile.append(field)
			#print(field)
	
		
	
	name = profile[0]
	title = profile[1]
	template = 'index.html'
	return render_template(template,name=name,title =title)
 
 
if __name__ == "__main__":
	app.run()


