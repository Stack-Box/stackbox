<template>
  <div class="container json-content" align="left">
    <vue-json-pretty
      :highlightMouseoverNode="true"
      :showLine="true"
      :path="'res'"
      :data="data"
    >
    </vue-json-pretty>
  </div>
</template>

<script>
import VueJsonPretty from "vue-json-pretty";
import axios from "axios";

export default {
  name: "Elasticsearch",
  components: {
    VueJsonPretty
  },
  data() {
    return {
      data: null
    };
  },
  mounted() {
    axios
      .get("http://localhost:80/elasticsearch_view_stacks")
      .then(response => {
        this.data = response.data;
      });
  }
};
</script>

<style scoped>
.json-content {
  padding: 1rem;
  background-color: #f9f9f9;
}
</style>
