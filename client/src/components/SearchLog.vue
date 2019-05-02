<template>
  <mdb-container>
    <mdb-datatable
      :data="data"
      striped
      bordered
      arrows
      :display="3"
    />
  </mdb-container>
</template>




<script>
  import { mdbDatatable, mdbContainer } from 'mdbvue';
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
        }
      },
    },
    methods: {
      filterData(dataArr, keys) {
        let data = dataArr.map(entry => {
          let filteredEntry = {};
          keys.forEach(key => {
            if(key in entry) {
              filteredEntry[key] = entry[key];
            }
          })
          return filteredEntry;
        })
        return data;
      }
    },
    mounted(){
      fetch('http://127.0.0.1:5000/logs/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4iLCJwYXNzd29yZCI6ImFkbWluIn0.zy8qt30iqkmtZ4vP-ZkFJ08RyfMnXpphPWnYJKZfWSY')
        .then(res => res.json())
        .then(json => {
          console.log(json)
          let keys = ["date", "type"];
          let entries = this.filterData(json, keys);
          //columns
          this.data.columns = [
            {
              label: 'Name',
              field: 'name',
              sort: 'asc'
            },
            {
              label: 'Position',
              field: 'position',
              sort: 'asc'
            },

          ]
          //rows
          entries.map(entry => this.data.rows.push(entry));
        })
        .catch(err => console.log(err));
    }
  };
</script>
