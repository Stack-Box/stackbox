import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import {HttpClientModule} from '@angular/common/http';
import {MatTableModule} from '@angular/material/table';
import { NgxJsonViewerModule } from 'ngx-json-viewer';


import { MysqlComponent } from './mysql/mysql.component';
import { ElasticsearchComponent } from './elasticsearch/elasticsearch.component';

@NgModule({
  exports: [
    MatTableModule
    ],
  declarations: [
    MysqlComponent,
    AppComponent,
    ElasticsearchComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatTableModule,
    HttpClientModule,
    NgxJsonViewerModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
