from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def Web():
	return render_template('index.html')

    

@app.route("/results", methods=['GET'])
def results():
	headers = {'Authorization': 'INSERT API KEY HERE'}
	r=requests.get("https://api.typeform.com/forms/DIR0KS/responses", headers=headers)
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


	template = 'resume1.html'
	return render_template(template,profile=profile)




if __name__ == "__main__":
    app.run(debug=True)
