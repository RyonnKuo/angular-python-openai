import { Component, OnInit } from '@angular/core';
import { PythonCollectionService } from '../../service/python-collection.service';
import { CommonModule } from '@angular/common';


@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  standalone: true,
  imports: [CommonModule]
})
export class MainComponent implements OnInit {

  gptInputContent: string = '';
  gpt4oResQue: string[] = [];

  constructor(
    public pcs: PythonCollectionService
  ){}

  ngOnInit(): void {

  }

  gptInputkeyUp(value: any) {
    this.gptInputContent = value;
  }

  async gpt4oChat(){
    if (this.gptInputContent !== '') {
      const res = await this.pcs.gpt4oChat(this.gptInputContent);
      console.log(JSON.stringify(res));

      this.gpt4oResQue.push(res);
    }
  }

}
