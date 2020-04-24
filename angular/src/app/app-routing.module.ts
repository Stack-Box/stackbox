import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {MysqlComponent} from "./mysql/mysql.component";
import {ElasticsearchComponent} from "./elasticsearch/elasticsearch.component";


const routes: Routes = [
  { path: 'mysql', component: MysqlComponent },
  { path: 'elasticsearch', component: ElasticsearchComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
