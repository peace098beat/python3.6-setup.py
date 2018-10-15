# python3.6-setup.py
python3.6-setup.py


### gitignore

```
curl https://www.gitignore.io/api/python > .gitignore
```


### 整形
Cloud9でautopep8を使って整形する方法

```
まずはインストール
/usr/bin/python3 -m pip install autopep8
```

```
Cloud9の設定を追加
Cloud9 > Custom Code Formatter:
/usr/bin/python3 -m autopep8 -i "$file"
```


### JSONを使うhouhou 

http://flask.pocoo.org/docs/1.0/testing/

http://flask.pocoo.org/docs/1.0/api/#module-flask.json

POSTの受け方

```py
@app.route('/transactions/new', methods=['POST'])
def new_transactions():
    values = request.get_json()

    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return 'Missing values', 400

    index = blockchain.new_tansaction(
        values['sender'],
        values['recipient'],
        values['amount'])

    response = {'message': f'トランザクションはブロック{index}に追加されました',
                'Output': 'Hello Test'
                }
    return jsonify(response)
    # return Response(json.dumps(response), mimetype='application/json', status=200)

```

POSTのテストコード

```
def test_new(client):
    data = {
        "sender": "1234567890",
        "recipient": "0987654321",
        "amount": 1000}

    result = client.post("/transactions/new",
                         json=data,
                         content_type='application/json',
                         follow_redirects=True)
    result_data = result.get_data()
    response_body = json.loads(result_data)
    assert result.status_code == 200
    assert result.headers['Content-Type'] == 'application/json'
    assert response_body['Output'] == 'Hello Test'
```





