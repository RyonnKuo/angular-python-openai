import re, os, random, string
from typing_extensions import Self
from flask import Flask, request, template_rendered, Blueprint, url_for, redirect, flash, render_template, jsonify
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from datetime import datetime
from sqlalchemy import null
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
from openai import OpenAI

OPEN_AI_KEY = 'Your openai api key'
client = OpenAI(api_key=OPEN_AI_KEY, timeout=30)
app = Flask(__name__)
CORS(app)

ALLOWED_EXTENSIONS = {"txt", "pdf", "png", "jpg", "jpeg", "gif", "csv"}

# headers = {
#     "Content-Type": "application/json",
#     "Authorization": f"Bearer {OPEN_AI_KEY}"
# }


@app.route('/api/call_gpt_4o', methods=['POST', 'GET'])
def call_gpt_4o():
  reqData = request.json
  prompt = reqData.get('prompt')

  MODEL="gpt-4o"
  response = client.chat.completions.create(
    model=MODEL,
    messages=[
      {"role": "user", "content": f"{prompt}"}
    ],
    response_format={
      "type": "text"
    },
    temperature=1,
    max_completion_tokens=2048,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )

  resJson = response.model_dump_json()
  print(resJson)
  # response = client.chat.completions.create(
  #   model=MODEL,
  #   messages=[
  #     {
  #       "role": "system",
  #       "content": "You are a helpful assistant that responds in Markdown. Help me with my math homework!"
  #     },
  #     {
  #       "role": "user",
  #       "content": [
  #         {
  #           "type": "text",
  #           "text": "What's the area of the shape in this image?"
  #         },
  #         {
  #           "type": "image_url",
  #           "image_url": {
  #             "url": f"data:image/png;base64,{base64_image}"
  #           }
  #         }
  #       ]
  #     }
  #   ],
  #   temperature=0.0,
  # )
  resData = {
    "status":200,
    "data": resJson
  }
  return jsonify(resData)

@app.route('/api/get_enroll', methods=['POST', 'GET'])
def get_enroll():
  if request.method == 'POST':
    reqData = request.json
    sid = reqData.get('sid')
    data = {"success": True, "message": "報名成功！"}
    print('get_enroll is called, sid = ' f"{type(data)}")
    return jsonify(data)

@app.route('/api/add_enroll', methods=['POST', 'GET'])
def add_enroll():
  if request.method == 'POST':
    reqData = request.json
    sid = reqData.get('sid')
    startdate = reqData.get('startdate')
    sname = reqData.get('sname')
    tno = reqData.get('tno')
    coupon = reqData.get('coupon')
    amount = reqData.get('amount')
    tdate = reqData.get('tdate')
    cardid = reqData.get('cardid')
    cardenddate = reqData.get('cardenddate')
    cardtype = reqData.get('cardtype')
    input = {
              'sid': sid,
              'startdate': startdate,
              'sname': sname,
              'tno': tno,
              'coupon': coupon,
              'amount': amount,
              'tdate': tdate,
              'cardid': cardid,
              'cardenddate': cardenddate,
              'cardtype': cardtype
          }
    data = {"success": True, "message": "報名成功！"}
    print('add_enroll is called, sid = ' f"{type(data)}")
    return jsonify(data), 200

app.secret_key = 'Your Key'

if __name__ == '__main__':
    app.debug = True
    app.secret_key = "Your Key"
    app.run(host='127.0.0.1', port = 5000, debug=True)
