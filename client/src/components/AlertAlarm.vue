<template>

  <mdb-tbl btn responsive striped>
    <mdb-tbl-head>
      <tr>

        <th>Type</th>
        <th>Start Time</th>
        <th>End Time</th>
        <th></th>
      </tr>
    </mdb-tbl-head>
    <mdb-tbl-body>
        <alert-row v-for="(item, index) in rows"
        :row=item
        :items=rows
        index=index
        v-on:itemRemoved="fetchAlerts"
        v-bind:key="item.id"></alert-row>
    </mdb-tbl-body>
  </mdb-tbl>
</template>

<script>
  import { mdbTbl, mdbTblHead, mdbTblBody } from 'mdbvue';
  export default {
    name: 'TableAdditionalPage',
    components: {
      mdbTbl,
      mdbTblHead,
      mdbTblBody,
    },
    data: function(){
      return {rows: []}
    },

    methods: {
      fetchAlerts: function(){
        fetch('http://127.0.0.1:5000/alert')
        .then((res) => { return res.json() })
        .then((res) => {
          console.log(res)
          this.rows = res;
        })

      },
      handleRemoveItem(){
        console.log("handle")
      }

    },

    created() {
      this.fetchAlerts()
    }

  }



  /*
          <tr v-for="(item) in rows">
            <td>{{ item.type }}</td>
            <td>{{ item.starttime }}</td>
            <td>{{ item.endtime }}</td>
          </tr>

  */
</script>
