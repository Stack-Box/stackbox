<template>
  <div class="base-demo" style="width: 400px">
    <vue-table-dynamic :params="params"></vue-table-dynamic>
  </div>
</template>

<script>
import VueTableDynamic from "vue-table-dynamic";
import axios from "axios";

export default {
  name: "Mysql",
  data() {
    return {
      params: {
        data: null,
        header: "row",
        border: true
      }
    };
  },
  mounted() {
    axios.get("http://localhost:80/view_stacks").then(response => {
      this.params.data = response.data.res;
    });
  },
  components: { VueTableDynamic }
};
</script>
