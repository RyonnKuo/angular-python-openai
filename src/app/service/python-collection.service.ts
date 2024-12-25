import { Injectable } from '@angular/core';

const API_URL = 'http://127.0.0.1:5000'

@Injectable({
  providedIn: 'root'
})
export class PythonCollectionService {

  constructor() { }

  async gpt4oChat(inputStr?: string): Promise<any> {
    try {
      // const res = await fetch(`${API_URL}/api/student_register`, {
      //   method: 'POST',
      //   mode: 'cors',
      //   headers: {
      //     "Access-Control-Allow-Origin": "*",
      //     "Content-Type": "application/json",
      //     "ngrok-skip-browser-warning": "69420"
      //   },
      //   body: JSON.stringify(param)
      // });
      const param = {
        prompt: inputStr || 'Say this is a test'
      }

      const res = await fetch(`${API_URL}/api/call_gpt_4o`, {
        method: 'POST',
        mode: 'cors',
        headers: {
          "Access-Control-Allow-Origin": "*",
          "Content-Type": "application/json",
          "ngrok-skip-browser-warning": "69420"
        },
        body: JSON.stringify(param)
      });

      const result = await res.json();

      if (result['status'] == 200) {
        console.log(`[py api] status is OK`);
        const data = await JSON.parse(result['data']);
        console.log(`data.choices = ${JSON.stringify(data.choices[0].message.content)}`);
        return data.choices[0].message.content;
      }
    } catch (error) {
      console.log(`[py api] try to get gpt response error happen: ${error}`);
      return 'gpt-4o api call fail...'
    }
  }

  async getAllStudent(): Promise<any> {

    try {
      const res = await fetch(`${API_URL}/api/get_all_student`, {
        method: 'GET',
        mode: 'cors',
        headers: {
          "Access-Control-Allow-Origin": "*",
          "Content-Type": "application/json",
          "ngrok-skip-browser-warning": "69420"
        },
      });

      const result = await res.json();
      console.log(`[py api] getAllStudent result: ${JSON.stringify(result)}`)
      return {
        "success": true,
        "result": result
      }
    } catch (error) {
      return {
        "success": false,
        "result": `[py api] getAllStudent error: ${error}`
      };
    }
  }
}
