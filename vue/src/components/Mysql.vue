<template>
  <div class="mx-auto">
    <b-container fluid="sm">
      <b-form-group>
        <b-input-group>
          <b-form-input
            v-model="filter"
            type="search"
            id="filterInput"
            placeholder="Type to Search"
          ></b-form-input>
          <b-input-group-append>
            <b-button :disabled="!filter" @click="filter = ''">Clear</b-button>
          </b-input-group-append>
        </b-input-group>
      </b-form-group>

      <b-table
        striped
        bordered
        responsive
        hover
        :per-page="perPage"
        :current-page="currentPage"
        :items="items"
        :fields="fields"
        :filter="filter"
        :filterIncludedFields="filterOn"
      ></b-table>

      <b-row class="text-center">
        <b-col md="auto">
          <div style="margin:auto;text-align: left;">
            <ul class="pagination">
              <li class="page-item active">
                <a class="page-link">Total {{ rows }}</a>
              </li>
            </ul>
          </div>
        </b-col>

        <b-col md="auto">
          <b-pagination
            v-model="currentPage"
            :total-rows="rows"
            :per-page="perPage"
          ></b-pagination>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import { BTable } from "bootstrap-vue";
import axios from "axios";

export default {
  name: "Mysql",
  components: { BTable },
  computed: {
    rows() {
      return this.items.length;
    }
  },
  data() {
    return {
      filter: null,
      filterOn: [],
      perPage: 3,
      currentPage: 1,
      items: [],
      fields: [
        {
          key: "build",
          sortable: true
        },
        {
          key: "image",
          sortable: true
        },
        {
          key: "port",
          label: "Port",
          sortable: true
        }
      ]
    };
  },
  mounted() {
    this.getMySqlData();
  },
  methods: {
    onFiltered(filteredItems) {
      // Trigger pagination to update the number of buttons/pages due to filtering
      this.totalRows = filteredItems.length;
      this.currentPage = 1;
    },
    makeToast(variant = null, error) {
      this.$bvToast.toast(error, {
        title: "ERROR",
        variant: variant,
        solid: true
      });
    },
    getMySqlData() {
      axios
        .get("http://localhost:80/mysql_view_stacks")
        .then(response => {
          this.items = response.data;
        })
        .catch(e => {
          this.makeToast("danger", e.message);
        });
    }
  }
};
</script>
