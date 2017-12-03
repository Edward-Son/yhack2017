import { Component, OnInit } from '@angular/core';
import {Http} from "@angular/http";
import 'rxjs/add/operator/map';


@Component({
  selector: 'app-table-list',
  templateUrl: './table-list.component.html',
  styleUrls: ['./table-list.component.css']
})
export class TableListComponent implements OnInit {

  resolution1 = [];
  resolution2 = [];
  resolution = [];

  data: any;
    dict = [1,0,1,1,1,0,0,0,0,0];

  constructor(private http: Http) { }

  ngOnInit() {
    this.getResolution().then((data) => {
      console.log("what is in the data ", data);

      //for(let bad of data){
      for(let i =0;i<10;i++){
          this.resolution1.push(data["1"][i]);
         this.resolution2.push(data["2"][i]);
         this.resolution.push({r1: data["1"][i], r2: data["2"][i], r3:this.dict[i]});

      }


    });

      console.log(this.resolution);
  }

  getResolution(){
    if (this.data) {
      return Promise.resolve(this.data);
    }


    return new Promise(resolve => {
      this.http.get('assets/resolutionstuff.json')
          .map(res => res.json())
          .subscribe(data => {
            this.data = data;
            resolve(this.data);
          });
    });
  }

}
