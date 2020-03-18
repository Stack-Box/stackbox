<template>
  <div class="hello">
    <b-container>
      <b-jumbotron
        header="StackBox"
        lead="Create app stacks loaded with all your favourite clients, services and infra in under 5 mins."
      >
        <b-button variant="primary" href="https://github.com/Stack-Box/StackBox"
          >GitHub</b-button
        >
      </b-jumbotron>
    </b-container>
  </div>
</template>

<script>
import { BJumbotron } from "bootstrap-vue";
export default {
  name: "HelloWorld",
  components: { BJumbotron },
  props: {
    msg: String
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
</style>
