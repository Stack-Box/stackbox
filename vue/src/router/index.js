import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Mysql from '@/components/Mysql'
import Elasticsearch from '@/components/Elasticsearch'

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      name: "HelloWorld",
      component: HelloWorld
    },
    {
      path: "/mysql",
      name: "Mysql",
      component: Mysql
    },
    {
      path: '/elasticsearch',
      name: 'Elasticsearch',
      component: Elasticsearch
    }
  ]
});
