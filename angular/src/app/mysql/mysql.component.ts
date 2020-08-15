import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './mysql.component.html',
  styleUrls: ['../app.component.css']
})
export class MysqlComponent implements OnInit {
  constructor(private http: HttpClient) { }
  displayedColumns: string[] = ['build', 'image', 'name', 'port'];
  dataSource;
  ngOnInit() {
    this.dataSource=this.http.get('http://localhost/mysql_view_stacks');
  }
}


