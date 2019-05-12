<template>
  <mdb-container>
    <mdb-datatable :data="data" striped bordered arrows :display="3"/>
  </mdb-container>
</template>




<script>
import { mapState } from "vuex";
import axios from "axios";
import { mdbDatatable, mdbContainer } from "mdbvue";
export default {
  components: {
    mdbDatatable,
    mdbContainer
  },
  computed: {
    data() {
      return {
        columns: [],
        rows: []
      };
    },
    ...mapState(["token", "userID"])
  },
  methods: {
    filterData(dataArr, keys) {
      let data = dataArr.map(entry => {
        let filteredEntry = {};
        keys.forEach(key => {
          if (key in entry) {
            filteredEntry[key] = entry[key];
          }
        });
        return filteredEntry;
      });
      return data;
    }
  },
  mounted() {
    var url =
      "http://127.0.0.1:5000/logs/" + this.token + "?userID=" + this.userID;
    fetch(url)
      .then(res => res.json())
      .then(json => {
        let keys = ["id", "type", "text", "date"];
        let entries = this.filterData(json, keys);
        //columns
        keys.map(key =>
          this.data.columns.push({
            label: key.toUpperCase(),
            field: key,
            sort: "asc"
          })
        );

        //rows
        entries.map(entry => this.data.rows.push(entry));
      })
      .catch(err => console.log(err));
  }
};
</script>
