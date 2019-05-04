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

  import { mapState } from 'vuex'
  import axios from 'axios'
  import { mdbDatatable, mdbContainer } from 'mdbvue';
  export default {
    components: {
      mdbDatatable,
      mdbContainer
    },
    computed: {
      ...mapState([
        'token',
        'userID'
      ]),
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

      console.log(this.userID)
      axios({ url: 'http://127.0.0.1:5000/logs/' + this.token, params: {userID: this.userID} ,method: 'GET' })
      .then(res => res.data)
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
