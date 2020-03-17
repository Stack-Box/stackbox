<template>
  <div>
    <vue-json-pretty
      :path="'res'"
      :data="data"
      @click="handleClick">
    </vue-json-pretty>
  </div>
</template>

<script>
import VueJsonPretty from 'vue-json-pretty'
import axios from 'axios'

export default {
  name: 'Elasticsearch',
  components: {
    VueJsonPretty
  },
  data() {
    return {
      data: null
    }
  },
  mounted(){
    axios.get('http://localhost:80/elasticsearch_view_stacks').then(response => {
      this.data = response.data.res
    })
  }
}

</script>
