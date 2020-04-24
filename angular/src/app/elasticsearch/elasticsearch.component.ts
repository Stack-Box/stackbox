import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './elasticsearch.component.html',
  styleUrls: ['../app.component.css']
})
export class ElasticsearchComponent implements OnInit {
  constructor(private http: HttpClient) { }
  dataSource;
  ngOnInit() {
    this.http.get('http://localhost/elasticsearch_view_stacks').subscribe(
      response => {this.dataSource=response});
  }
}


